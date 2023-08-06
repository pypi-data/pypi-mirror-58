# -*- coding: utf-8 -*-
# Copyright (c) 2013, Michael Nooner
# Copyright (c) 2018 - 2020, Lars Heuer
# All rights reserved.
#
# License: BSD License
#
"""This module does the actual generation of the QR codes. The QRCodeBuilder
builds the code. While the various output methods draw the code into a file.

This module does not belong to the public API.
"""
from __future__ import absolute_import, division, print_function, unicode_literals
import io
import re
import math
import codecs
import itertools
from itertools import chain
from contextlib import contextmanager
from functools import partial, reduce
from xml.sax.saxutils import quoteattr
import pyqrcodeng.tables as tables
_PY2 = False
try:  # pragma: no cover
    from itertools import zip_longest
except ImportError:  # pragma: no cover
    # Py2
    _PY2 = True
    from itertools import izip_longest as zip_longest, imap as map
    range = xrange
    str = unicode
    open = io.open
_PYPNG_AVAILABLE = False
try:
    import png
    _PYPNG_AVAILABLE = True
except ImportError:
    pass

_ALPHANUMERIC_PATTERN = re.compile(br'^[' + re.escape(tables.ALPHANUMERIC_CHARS) + br']+\Z')

# <https://wiki.python.org/moin/PortingToPy3k/BilingualQuickRef#New_Style_Classes>
__metaclass__ = type


class QRCodeBuilder:
    """This class generates a QR code based on the standard. It is meant to
    be used internally, not by users!!!

    This class implements the tutorials found at:

    * http://www.thonky.com/qr-code-tutorial/

    * http://www.matchadesign.com/blog/qr-code-demystified-part-6/

    This class also uses the standard, which can be read online at:
        http://raidenii.net/files/datasheets/misc/qr_code.pdf

    Test codes were tested against:
        http://zxing.org/w/decode.jspx

    Also, reference codes were generat/ed at:
        http://www.morovia.com/free-online-barcode-generator/qrcode-maker.php
        http://demos.telerik.com/aspnet-ajax/barcode/examples/qrcode/defaultcs.aspx

    QR code Debugger:
        http://qrlogo.kaarposoft.dk/qrdecode.html
    """
    def __init__(self, content, version, mode, error, encoding=None):
        """See :py:class:`pyqrcode.QRCode` for information on the parameters."""

        if version is not None:
            if 1 <= version <= 40:
                self.version = version
            else:
                raise VersionError("Illegal version {0}, version must be between "
                                    "1 and 40.".format(version))

        # Guess the mode of the code, this will also be used for
        # error checking
        guessed_content_type, guessed_encoding = QRCodeBuilder._detect_content_type(content, encoding)

        if mode == 'binary' and isinstance(content, bytes):
            self.data = content
            self.encoding = None
        else:
            if isinstance(content, int):
                content = str(content)

            encoding_provided = encoding is not None
            if not encoding_provided:
                encoding = 'iso-8859-1' if guessed_encoding is None else guessed_encoding

            # Store the encoding for use later
            if guessed_content_type == 'kanji':
                self.encoding = 'shiftjis'
            else:
                self.encoding = encoding

            # Decode a 'byte array' contents into a string format
            if isinstance(content, bytes):
                self.data = content.decode(encoding)
            # Give a string an encoding
            elif hasattr(content, 'encode'):
                try:
                    self.data = content.encode(self.encoding)
                except UnicodeEncodeError as ex:
                    if not encoding_provided:
                        self.encoding = 'utf-8'
                        self.data = content.encode(self.encoding)
                    else:
                        raise ex
            else:
                # The contents are not a byte array or string, so
                # try naively converting to a string representation.
                self.data = str(content)  # str == unicode in Py 2.x, see file head

        if mode is None:
            # Use the guessed mode
            mode = guessed_content_type
        else:
            # Force a passed in mode to be lowercase
            mode = mode.lower()
            try:
                self.mode_num = tables.modes[mode]
            except KeyError:
                raise ModeError('{0} is not a valid mode.'.format(mode))
            if guessed_content_type != mode:
                # Binary is only guessed as a last resort, if the
                # passed in mode is not binary the data won't encode
                if guessed_content_type == 'binary':
                    raise DataOverflowError('The content provided cannot be encoded with '
                                     'the mode {}, it can only be encoded as '
                                     'binary.'.format(mode))
                elif mode in ('numeric', 'kanji'):
                    raise DataOverflowError('The content cannot be encoded as {0}. Proposal: "{1}".'.format(mode, guessed_content_type))
        self.mode = mode
        self.mode_num = tables.modes[mode]
        # Check that the user passed in a valid error level
        try:
            self.error = tables.error_level[error]
        except KeyError:
            raise ErrorLevelError('{0} is not a valid error level.'.format(error))

        # Guess the "best" version
        guessed_version = QRCodeBuilder._pick_best_fit(self.data, error=self.error,
                                                       mode_num=self.mode_num)
        if version is None:
            version = guessed_version
            self.version = version
        # If the user supplied a version, then check that it has
        # sufficient data capacity for the contents passed in
        if guessed_version > version:
            raise DataOverflowError('The data will not fit inside a version {} '
                                    'code with the given encoding and error '
                                    'level (the code must be at least a '
                                     'version {}).'.format(version, guessed_version))

        # Look up the proper row for error correction code words
        self.error_code_words = tables.eccwbi[version][self.error]
        # This property will hold the binary string as it is built
        self.buffer = io.StringIO()
        # Create the binary data block
        self.add_data()
        # Create the actual QR code
        self.make_code()

    @staticmethod
    def _detect_content_type(content, encoding):
        """This method tries to auto-detect the type of the data. It first
        tries to see if the data is a valid integer, in which case it returns
        numeric. Next, it tests the data to see if it is 'alphanumeric.' QR
        Codes use a special table with very limited range of ASCII characters.
        The code's data is tested to make sure it fits inside this limited
        range. If all else fails, the data is determined to be of type
        'binary.'

        Returns a tuple containing the detected mode and encoding.

        Note, encoding ECI is not yet implemented.
        """

        def next_byte_py2(b):
            return ord(b)

        def next_byte_py3(b):
            return b

        next_byte = next_byte_py3 if not _PY2 else next_byte_py2

        def two_bytes(c):
            """Output two byte character code as a single integer."""
            # Go through the data by looping to every other character
            for i in range(0, len(c), 2):
                yield (next_byte(c[i]) << 8) | next_byte(c[i+1])

        # See if the data is a number
        try:
            if str(content).isdigit():
                return 'numeric', encoding
        except (TypeError, UnicodeError):
            pass

        try:
            if isinstance(content, bytes):
                c = content.decode('ASCII')
            else:
                c = str(content).encode('ASCII')
            if _ALPHANUMERIC_PATTERN.match(c):
                return 'alphanumeric', 'ASCII'
        # This occurs if the content does not contain ASCII characters.
        # Since the whole point of the if statement is to look for ASCII
        # characters, the resulting mode should not be alphanumeric.
        # Hence, this is not an error.
        except TypeError:
            pass
        except UnicodeError:
            pass

        try:
            if isinstance(content, bytes):
                if encoding is None:
                    encoding = 'shiftjis'
                c = content.decode(encoding).encode('shiftjis')
            else:
                c = content.encode('shiftjis')

            # All kanji characters must be two bytes long, make sure the
            # string length is not odd.
            if len(c) % 2 != 0:
                return 'binary', encoding

            # Take sure the characters are actually in range.
            for asint in two_bytes(c):
                # Shift the two byte value as indicated by the standard
                if not (0x8140 <= asint <= 0x9FFC or
                        0xE040 <= asint <= 0xEBBF):
                    return 'binary', encoding
            return 'kanji', encoding
        except UnicodeError:
            # This occurs if the content does not contain Shift JIS kanji
            # characters. Hence, the resulting mode should not be kanji.
            # This is not an error.
            pass
        except LookupError:
            # This occurs if the host Python does not support Shift JIS kanji
            # encoding. Hence, the resulting mode should not be kanji.
            # This is not an error.
            pass
        # All of the other attempts failed. The content can only be binary.
        return 'binary', encoding

    @staticmethod
    def _pick_best_fit(content, error, mode_num):
        """This method return the smallest possible QR code version number
        that will fit the specified data with the given error level.
        """
        for version in range(1, 41):
            # Get the maximum possible capacity
            capacity = tables.data_capacity[version][error][mode_num]
            # Check the capacity
            # Kanji's count in the table is "characters" which are two bytes
            if mode_num == tables.MODE_KANJI \
                    and capacity >= math.ceil(len(content) / 2):
                return version
            if capacity >= len(content):
                return version
        raise DataOverflowError('The data will not fit in any QR code version '
                                'with the given encoding and error level.')


    @staticmethod
    def grouper(n, iterable, fillvalue=None):
        """This generator yields a set of tuples, where the
        iterable is broken into n sized chunks. If the
        iterable is not evenly sized then fillvalue will
        be appended to the last tuple to make up the difference.

        This function is copied from the standard docs on
        itertools.
        """
        args = [iter(iterable)] * n
        return zip_longest(*args, fillvalue=fillvalue)

    @staticmethod
    def binary_string(data, length):
        """This method returns a string of length n that is the binary
        representation of the given data. This function is used to
        basically create bit fields of a given size.
        """
        return '{{0:0{0}b}}'.format(length).format(int(data))

    def get_data_length(self):
        """QR codes contain a "data length" field. This method creates this
        field. A binary string representing the appropriate length is
        returned.
        """
        # The "data length" field varies by the type of code and its mode.
        # discover how long the "data length" field should be.
        if 1 <= self.version <= 9:
            max_version = 9
        elif 10 <= self.version <= 26:
            max_version = 26
        elif 27 <= self.version <= 40:
            max_version = 40
        data_length = tables.data_length_field[max_version][self.mode_num]
        if self.mode_num != tables.MODE_KANJI:
            length_string = QRCodeBuilder.binary_string(len(self.data), data_length)
        else:
            length_string = QRCodeBuilder.binary_string(len(self.data) / 2, data_length)
        if len(length_string) > data_length:
            raise DataOverflowError('The supplied data will not fit '
                                    'within this version of a QRCode.')
        return length_string

    def encode(self, mode_num):
        """This method encodes the data into a binary string using
        the appropriate algorithm specified by the mode.
        """
        if mode_num == tables.MODE_ALPHANUMERIC:
            encoded = self.encode_alphanumeric()
        elif mode_num == tables.MODE_NUMERIC:
            encoded = self.encode_numeric()
        elif mode_num == tables.MODE_BYTE:
            encoded = self.encode_bytes()
        elif mode_num == tables.MODE_KANJI:
            encoded = self.encode_kanji()
        return encoded

    def encode_alphanumeric(self):
        """This method encodes the QR code's data if its mode is
        alphanumeric. It returns the data encoded as a binary string.
        """
        # Change the data such that it uses a QR code ascii table
        to_byte = tables.ALPHANUMERIC_CHARS.find
        ascii_data = map(to_byte, self.data)
        # Now perform the algorithm that will make the ascii into bit fields
        with io.StringIO() as buf:
            for a, b in QRCodeBuilder.grouper(2, ascii_data, fillvalue=None):
                if b is not None:
                    buf.write(QRCodeBuilder.binary_string(45 * a + b, 11))
                else:
                    # This occurs when there is an odd number
                    # of characters in the data
                    buf.write(QRCodeBuilder.binary_string(a, 6))
            # Return the binary string
            return buf.getvalue()

    def encode_numeric(self):
        """This method encodes the QR code's data if its mode is
        numeric. It returns the data encoded as a binary string.
        """
        with io.StringIO() as buf:
            # Break the number into groups of three digits
            for triplet in QRCodeBuilder.grouper(3, self.data):
                number = ''
                for digit in triplet:
                    if isinstance(digit, int):
                        digit = chr(digit)
                    # Only build the string if digit is not None
                    if digit:
                        number = ''.join([number, digit])
                    else:
                        break
                # If the number is one digits, make a 4 bit field
                if len(number) == 1:
                    bin = QRCodeBuilder.binary_string(number, 4)
                elif len(number) == 2:  # If the number is two digits, make a 7 bit field
                    bin = QRCodeBuilder.binary_string(number, 7)
                else:  # Three digit numbers use a 10 bit field
                    bin = QRCodeBuilder.binary_string(number, 10)
                buf.write(bin)
            return buf.getvalue()

    def encode_bytes(self):
        """This method encodes the QR code's data if its mode is
        8 bit mode. It returns the data encoded as a binary string.
        """
        with io.StringIO() as buf:
            for char in self.data:
                if not isinstance(char, int):
                    buf.write('{{0:0{0}b}}'.format(8).format(ord(char)))
                else:
                    buf.write('{{0:0{0}b}}'.format(8).format(char))
            return buf.getvalue()

    def encode_kanji(self):
        """This method encodes the QR code's data if its mode is
        kanji. It returns the data encoded as a binary string.
        """
        def two_bytes(data):
            """Output two byte character code as a single integer."""
            def next_byte(b):
                """Make sure that character code is an int. Python 2 and
                3 compatibility.
                """
                if not isinstance(b, int):
                    return ord(b)
                else:
                    return b

            # Go through the data by looping to every other character
            for i in range(0, len(data), 2):
                yield (next_byte(data[i]) << 8) | next_byte(data[i+1])
        # Force the data into Kanji encoded bytes
        if isinstance(self.data, bytes):
            data = self.data.decode('shiftjis').encode('shiftjis')
        else:
            data = self.data.encode('shiftjis')
        # Now perform the algorithm that will make the kanji into 13 bit fields
        with io.StringIO() as buf:
            for asint in two_bytes(data):
                # Shift the two byte value as indicated by the standard
                if 0x8140 <= asint <= 0x9FFC:
                    difference = asint - 0x8140
                elif 0xE040 <= asint <= 0xEBBF:
                    difference = asint - 0xC140
                # Split the new value into most and least significant bytes
                msb = (difference >> 8)
                lsb = (difference & 0x00FF)
                # Calculate the actual 13 bit binary value
                buf.write('{0:013b}'.format((msb * 0xC0) + lsb))
            # Return the binary string
            return buf.getvalue()

    def add_data(self):
        """This function properly constructs a QR code's data string. It takes
        into account the interleaving pattern required by the standard.
        """
        # Encode the data into a QR code
        self.buffer.write(QRCodeBuilder.binary_string(self.mode_num, 4))
        self.buffer.write(self.get_data_length())
        self.buffer.write(self.encode(self.mode_num))
        # Converts the buffer into "code word" integers.
        # The online debugger outputs them this way, makes
        # for easier comparisons.
        # s = self.buffer.getvalue()
        # for i in range(0, len(s), 8):
        #    print(int(s[i:i+8], 2), end=',')
        # print()
        
        # Fix for issue #3: https://github.com/mnooner256/pyqrcode/issues/#3
        # I was performing the terminate_bits() part in the encoding.
        # As per the standard, terminating bits are only supposed to
        # be added after the bit stream is complete. I took that to
        # mean after the encoding, but actually it is after the entire
        # bit stream has been constructed.
        bits = self.terminate_bits(self.buffer.getvalue())
        if bits is not None:
            self.buffer.write(bits)
        # delimit_words and add_words can return None
        add_bits = self.delimit_words()
        if add_bits:
            self.buffer.write(add_bits)
        fill_bytes = self.add_words()
        if fill_bytes:
            self.buffer.write(fill_bytes)
        # Get a numeric representation of the data
        data = [int(''.join(x),2)
                    for x in QRCodeBuilder.grouper(8, self.buffer.getvalue())]
        # This is the error information for the code
        error_info = tables.eccwbi[self.version][self.error]
        # This will hold our data blocks
        data_blocks = []
        # This will hold our error blocks
        error_blocks = []
        # Some codes have the data sliced into two different sized blocks
        # for example, first two 14 word sized blocks, then four 15 word
        # sized blocks. This means that slicing size can change over time.
        data_block_sizes = [error_info[2]] * error_info[1]
        if error_info[3] != 0:
            data_block_sizes.extend([error_info[4]] * error_info[3])
        # For every block of data, slice the data into the appropriate
        # sized block
        current_byte = 0
        for n_data_blocks in data_block_sizes:
            data_blocks.append(data[current_byte:current_byte+n_data_blocks])
            current_byte += n_data_blocks
        # I am not sure about the test after the "and". This was added to
        # fix a bug where after delimit_words padded the bit stream, a zero
        # byte ends up being added. After checking around, it seems this extra
        # byte is supposed to be chopped off, but I cannot find that in the
        # standard! I am adding it to solve the bug, I believe it is correct.
        if current_byte < len(data):
            raise DataOverflowError('Too much data for this code version.')
        # Calculate the error blocks
        for n, block in enumerate(data_blocks):
            error_blocks.append(self.make_error_block(block, n))
        # Buffer we will write our data blocks into
        data_buffer = io.StringIO()
        # Add the data blocks
        # Write the buffer such that: block 1 byte 1, block 2 byte 1, etc.
        largest_block = max(error_info[2], error_info[4]) + error_info[0]
        for i in range(largest_block):
            for block in data_blocks:
                if i < len(block):
                    data_buffer.write(QRCodeBuilder.binary_string(block[i], 8))
        # Add the error code blocks.
        # Write the buffer such that: block 1 byte 1, block 2 byte 2, etc.
        for i in range(error_info[0]):
            for block in error_blocks:
                data_buffer.write(QRCodeBuilder.binary_string(block[i], 8))
        self.buffer = data_buffer

    def terminate_bits(self, payload):
        """This method adds zeros to the end of the encoded data so that the
        encoded data is of the correct length. It returns a binary string
        containing the bits to be added.
        """
        data_capacity = tables.data_capacity[self.version][self.error][0]
        if len(payload) > data_capacity:
            raise DataOverflowError('The supplied data will not fit '
                                    'within this version of a QR code.')
        # We must add up to 4 zeros to make up for any shortfall in the
        # length of the data field.
        if len(payload) == data_capacity:
            return None
        elif len(payload) <= data_capacity - 4:
            bits = QRCodeBuilder.binary_string(0, 4)
        else:
            # Make up any shortfall need with less than 4 zeros
            bits = QRCodeBuilder.binary_string(0, data_capacity - len(payload))
        return bits

    def delimit_words(self):
        """This method takes the existing encoded binary string
        and returns a binary string that will pad it such that
        the encoded string contains only full bytes.
        """
        bits_short = 8 - (len(self.buffer.getvalue()) % 8)
        # The string already falls on an byte boundary do nothing
        if bits_short == 0 or bits_short == 8:
            return None
        else:
            return QRCodeBuilder.binary_string(0, bits_short)

    def add_words(self):
        """The data block must fill the entire data capacity of the QR code.
        If we fall short, then we must add bytes to the end of the encoded
        data field. The value of these bytes are specified in the standard.
        """
        data_blocks = len(self.buffer.getvalue()) // 8
        total_blocks = tables.data_capacity[self.version][self.error][0] // 8
        needed_blocks = total_blocks - data_blocks
        if needed_blocks == 0:
            return None
        # This will return item1, item2, item1, item2, etc.
        block = itertools.cycle(['11101100', '00010001'])
        # Create a string of the needed blocks
        return ''.join([next(block) for x in range(needed_blocks)])

    def make_error_block(self, block, block_number):
        """This function constructs the error correction block of the
        given data block. This is *very complicated* process. To
        understand the code you need to read:

        * http://www.thonky.com/qr-code-tutorial/part-2-error-correction/
        * http://www.matchadesign.com/blog/qr-code-demystified-part-4/
        """
        # Get the error information from the standards table
        error_info = tables.eccwbi[self.version][self.error]
        # This is the number of 8-bit words per block
        if block_number < error_info[1]:
            code_words_per_block = error_info[2]
        else:
            code_words_per_block = error_info[4]
        # This is the size of the error block
        error_block_size = error_info[0]
        # Copy the block as the message polynomial coefficients
        mp_co = block[:]
        # Add the error blocks to the message polynomial
        mp_co.extend([0] * (error_block_size))
        # Get the generator polynomial
        generator = tables.generator_polynomials[error_block_size]
        # This will hold the temporary sum of the message coefficient and the
        # generator polynomial
        gen_result = [0] * len(generator)
        # Go through every code word in the block
        for i in range(code_words_per_block):
            # Get the first coefficient from the message polynomial
            coefficient = mp_co.pop(0)
            # Skip coefficients that are zero
            if coefficient == 0:
                continue
            else:
                # Turn the coefficient into an alpha exponent
                alpha_exp = tables.galois_antilog[coefficient]
            # Add the alpha to the generator polynomial
            for n in range(len(generator)):
                gen_result[n] = alpha_exp + generator[n]
                if gen_result[n] > 255:
                    gen_result[n] = gen_result[n] % 255
                # Convert the alpha notation back into coefficients
                gen_result[n] = tables.galois_log[gen_result[n]]
                # XOR the sum with the message coefficients
                mp_co[n] = gen_result[n] ^ mp_co[n]
        # Pad the end of the error blocks with zeros if needed
        if len(mp_co) < code_words_per_block:
            mp_co.extend([0] * (code_words_per_block - len(mp_co)))
        return mp_co

    def make_code(self):
        """This method returns the best possible QR code."""
        # Get the size of the underlying matrix
        matrix_size = _get_symbol_size(self.version, scale=1, quiet_zone=0)[0]
        # Create a template matrix we will build the codes with
        row = [None for x in range(matrix_size)]
        matrix = [list(row) for x in range(matrix_size)]
        # Add the dark module
        matrix[-8][8] = 1
        # Add mandatory information to the matrix
        QRCodeBuilder.add_finder_patterns(matrix)
        QRCodeBuilder.add_alignment_patterns(matrix, self.version)
        QRCodeBuilder.add_version_pattern(matrix, self.version)
        QRCodeBuilder.add_timing_pattern(matrix)
        # Create the various types of masks of the matrix
        masks = QRCodeBuilder.make_masks(matrix, self.buffer.getvalue(), self.error)
        best_mask = QRCodeBuilder.choose_best_mask(masks)
        self.code = masks[best_mask]

    @staticmethod
    def add_detection_pattern(matrix):
        import warnings
        warnings.warn('Deprecated since 1.3.5, use add_finder_patterns', DeprecationWarning)
        QRCodeBuilder.add_finder_patterns(matrix)
        # Add the dark module
        matrix[-8][8] = 1
        # Add timing pattern
        QRCodeBuilder.add_timing_pattern(matrix)

    @staticmethod
    def add_finder_patterns(matrix):
        """This method adds the finder patterns to the QR code. This lets
        the scanner orient the pattern. It is required for all QR codes.
        The finder pattern consists of three boxes located at the upper
        left, upper right, and lower left corners of the matrix.
        """
        # Draw outer black box
        for i in range(7):
            inv = -(i + 1)
            for j in (0, 6, -1, -7):
                row = matrix[j]
                row[i] = 1
                matrix[i][j] = 1
                matrix[inv][j] = 1
                row[inv] = 1
        # Draw inner white box
        for i in range(1, 6):
            inv = -(i + 1)
            for j in (1, 5, -2, -6):
                row = matrix[j]
                row[i] = 0
                matrix[i][j] = 0
                matrix[inv][j] = 0
                row[inv] = 0
        # Draw inner black box
        for i in range(2, 5):
            row = matrix[i]
            for j in range(2, 5):
                inv = -(i + 1)
                row[j] = 1
                matrix[inv][j] = 1
                matrix[j][inv] = 1
        # Draw white border
        for i in range(8):
            inv = -(i + 1)
            row = matrix[i]
            for j in (7, -8):
                row[j] = 0
                matrix[j][i] = 0
                matrix[inv][j] = 0
                matrix[j][inv] = 0
        # To keep the code short, it draws an extra box
        # in the lower right corner, this removes it.
        for i in range(-8, 0):
            for j in range(-8, 0):
                matrix[i][j] = None

    @staticmethod
    def add_timing_pattern(matrix):
        """Adds the timing pattern
        """
        # Add the timing pattern
        bit = itertools.cycle([1,0])
        for i in range(8, (len(matrix) - 8)):
            b = next(bit)
            matrix[i][6] = b
            matrix[6][i] = b

    @staticmethod
    def add_position_pattern(matrix, version):
        import warnings
        warnings.warn('Deprecated since 1.3.5, use add_alignment_patterns', DeprecationWarning)
        QRCodeBuilder.add_alignment_patterns(matrix, version)

    @staticmethod
    def add_alignment_patterns(matrix, version):
        """This method draws the alignment patterns onto the QR
        Code. All QR code versions larger than one require these special boxes
        called position alignment patterns.
        """
        # Version 1 does not have a position adjustment pattern
        if version == 1:
            return
        # Get the coordinates for where to place the boxes
        coordinates = tables.position_adjustment[version]
        # Get the max and min coordinates to handle special cases
        min_coord = coordinates[0]
        max_coord = coordinates[-1]
        # Draw a box at each intersection of the coordinates
        for i, j in ((i, j) for i in coordinates for j in coordinates):
            # Do not draw these boxes because they would
            # interfere with the detection pattern
            if (i == min_coord and j == min_coord) or \
               (i == min_coord and j == max_coord) or \
               (i == max_coord and j == min_coord):
                continue
            row = matrix[i]
            # Center black pixel
            row[j] = 1
            # Surround the pixel with a white box
            for x in (-1, 1):
                matrix[i + x][j + x] = 0
                matrix[i + x][j] = 0
                row[j + x] = 0
                matrix[i - x][j + x] = 0
                matrix[i + x][j - x] = 0
            # Surround the white box with a black box
            for x in (-2, 2):
                for y in (0, -1, 1):
                    matrix[i + x][j + x] = 1
                    matrix[i + x][j + y] = 1
                    matrix[i + y][j + x] = 1
                    matrix[i - x][j + x] = 1
                    matrix[i + x][j - x] = 1

    @staticmethod
    def add_version_pattern(matrix, version):
        """For QR codes with a version 7 or higher, a special pattern
        specifying the code's version is required.

        For further information see:
        http://www.thonky.com/qr-code-tutorial/format-version-information/# example-of-version-7-information-string
        """
        if version < 7:
            return
        # Get the bit fields for this code's version
        # We will iterate across the string, the bit string
        # needs the least significant digit in the zero-th position
        field = iter(tables.version_pattern[version][::-1])
        # Where to start placing the pattern
        start = len(matrix) - 11
        # The version pattern is pretty odd looking
        for i in range(6):
            row = matrix[i]
            # The pattern is three modules wide
            for j in range(start, start + 3):
                bit = int(next(field))
                # Bottom Left
                row[j] = bit
                # Upper right
                matrix[j][i] = bit

    @staticmethod
    def make_masks(matrix, data, error):
        """This method generates all seven masks so that the best mask can
        be determined. The template parameter is a code matrix that will
        server as the base for all the generated masks.
        """
        masks = []
        matrix_size = len(matrix)
        for n, pattern in enumerate(tables.mask_patterns):
            cur_mask = [list(row) for row in matrix]
            masks.append(cur_mask)
            # Add the type pattern bits to the code
            QRCodeBuilder.add_type_pattern(cur_mask, tables.type_bits[error][n])
            # Get the mask pattern
            # This will read the 1's and 0's one at a time
            bits = iter(data)
            # These will help us do the up, down, up, down pattern
            row_start = itertools.cycle([matrix_size - 1, 0])
            row_stop = itertools.cycle([-1, matrix_size])
            direction = itertools.cycle([-1, 1])
            # The data pattern is added using pairs of columns
            for column in range(matrix_size - 1, 0, -2):
                # The vertical timing pattern is an exception to the rules,
                # move the column counter over by one
                if column <= 6:
                    column -= 1
                # This will let us fill in the pattern
                # right-left, right-left, etc.
                column_pair = itertools.cycle([column, column - 1])
                # Go through each row in the pattern moving up, then down
                for i in range(next(row_start), next(row_stop), next(direction)):
                    row = cur_mask[i]
                    # Fill in the right then left column
                    for x in range(2):
                        j = next(column_pair)
                        # Go to the next column if we encounter a
                        # preexisting pattern (usually an alignment pattern)
                        if row[j] is not None:
                            continue
                        # Some versions don't have enough bits. You then fill
                        # in the rest of the pattern with 0's. These are
                        # called "remainder bits."
                        try:
                            bit = int(next(bits))
                        except:
                            bit = 0
                        # If the pattern is True then flip the bit
                        row[j] = bit ^ pattern(i, j)
        return masks

    @staticmethod
    def choose_best_mask(masks):
        """This method returns the index of the "best" mask as defined by
        having the lowest total penalty score. The penalty rules are defined
        by the standard. The mask with the lowest total score should be the
        easiest to read by optical scanners.
        """
        scores = []
        matrix_size = len(masks[0])
        patterns = ((0,0,0,0,1,0,1,1,1,0,1),
                    (1,0,1,1,1,0,1,0,0,0,0))
        matrix_range = range(matrix_size)
        for mask in masks:
            # Score penalty rule number 1
            # Look for five consecutive squares with the same color.
            # Each one found gets a penalty of 3 + 1 for every
            # same color square after the first five in the row.
            pr1 = 0
            # Examine the mask row wise
            for i in matrix_range:
                counter = 0
                current = -1
                row = mask[i]
                for j in matrix_range:
                    bit = row[j]
                    if bit == current:
                        counter += 1
                    else:
                        if counter >= 5:
                            pr1 += (counter - 5) + 3
                        counter = 1
                        current = bit
                if counter >= 5:
                    pr1 += (counter - 5) + 3
            # Examine the mask column wise
            for j in matrix_range:
                counter = 0
                current = -1
                for i in matrix_range:
                    bit = mask[j][i]
                    if bit == current:
                        counter += 1
                    else:
                        if counter >= 5:
                            pr1 += (counter - 5) + 3
                        counter = 1
                        current = bit
                if counter >= 5:
                    pr1 += (counter - 5) + 3

            # Score penalty rule 2
            # This rule will add 3 to the score for each 2x2 block of the same
            # colored pixels there are.
            pr2 = 0
            # Don't examine the 0th and Nth row/column
            for i in range(matrix_size - 1):
                row = mask[i]
                for j in range(matrix_size - 1):
                    if row[j] == mask[i + 1][j] and \
                       row[j] == mask[i][j + 1] and \
                       row[j] == mask[i + 1][j + 1]:
                        pr2 += 3

            # Score penalty rule 3
            # This rule looks for 1011101 within the mask prefixed
            # and/or suffixed by four zeros.
            pr3 = 0
            for i in matrix_range:
                for j in matrix_range:
                    for pattern in patterns:
                        match = True
                        k = j
                        # Look for row matches
                        for p in pattern:
                            if k >= len(mask) or mask[i][k] != p:
                                match = False
                                break
                            k += 1
                        if match:
                            pr3 += 1
                        match = True
                        k = j
                        # Look for column matches
                        for p in pattern:
                            if k >= len(mask) or mask[k][i] != p:
                                match = False
                                break
                            k += 1
                        if match:
                            pr3 += 1
            pr3 *= 40
            # Score the last rule, penalty rule 4. This rule measures how close
            # the pattern is to being 50% black. The further it deviates from
            # this this ideal the higher the penalty.
            percent = float(sum(map(sum, mask))) / (matrix_size ** 2)
            pr4 = 10 * int(abs(percent * 100 - 50) / 5)  # N4 = 10
            scores.append((pr1, pr2, pr3, pr4))
        # Calculate the total for each score
        totals = tuple(map(sum, scores))
        # The lowest total wins
        return totals.index(min(totals))

    @staticmethod
    def add_type_pattern(matrix, type_bits):
        """This will add the pattern to the QR code that represents the error
        level and the type of mask used to make the code.
        """
        field = iter(type_bits)
        for i in range(7):
            bit = int(next(field))
            # Skip the timing bits
            if i < 6:
                matrix[8][i] = bit
            else:
                matrix[8][i + 1] = bit
            if -8 < -(i + 1):
                matrix[-(i + 1)][8] = bit
        for i in range(-8, 0):
            bit = int(next(field))
            matrix[8][i] = bit
            i = -i
            # Skip timing column
            if i > 6:
                matrix[i][8] = bit
            else:
                matrix[i - 1][8] = bit


def _get_symbol_size(version, scale, quiet_zone=4):
    """See: QRCode.symbol_size()

    This function was abstracted away from QRCode to allow for the output of
    QR codes during the build process, i.e. for debugging. It works
    just the same except you must specify the code's version. This is needed
    to calculate the symbol's size.
    """
    # Formula: scale times number of modules plus the border on each side
    dim = version * 4 + 17
    dim += 2 * quiet_zone
    dim *= scale
    return dim, dim


@contextmanager
def _writable(file_or_path, mode, encoding=None):
    """\
    Returns a writable file-like object.

    Usage::

        with writable(file_name_or_path, 'wb') as f:
            ...


    :param file_or_path: Either a file-like object or a filename.
    :param str mode: String indicating the writing mode (i.e. ``'wb'``)
    """
    f = file_or_path
    must_close = False
    try:
        file_or_path.write
        if encoding is not None:
            f = codecs.getwriter(encoding)(file_or_path)
    except AttributeError:
        f = open(file_or_path, mode, encoding=encoding)
        must_close = True
    try:
        yield f
    finally:
        if must_close:
            f.close()


def _text(code, version, scale=1, quiet_zone=4):
    """This method returns a text based representation of the QR code.
    This is useful for debugging purposes.
    """
    buf = io.StringIO()
    for row in _matrix_iter(code, version, scale=scale, quiet_zone=quiet_zone):
        # Actually draw the QR code
        for bit in row:
            if bit == 1:
                buf.write('1')
            elif bit == 0:
                buf.write('0')
            else:
                # This is for debugging unfinished QR codes,
                # unset pixels will be spaces.
                buf.write(' ')
        buf.write('\n')
    return buf.getvalue()


def _xbm(code, version, scale=1, quiet_zone=4):
    """This function will format the QR code as a X BitMap.
    This can be used to display the QR code with Tkinter.
    """
    row_iter = _matrix_iter(code, version, scale, quiet_zone)
    width, height = _get_symbol_size(version, scale=scale, quiet_zone=quiet_zone)
    buf = io.StringIO()
    with _writable(buf, 'wt') as f:
        write = f.write
        write('#define im_width {0}\n'
              '#define im_height {1}\n'
              'static unsigned char im_bits[] = {{\n'.format(width, height))
        i = 0
        for row in row_iter:
            iter_ = zip_longest(*[iter(row)] * 8, fillvalue=0x0)
            # Reverse bits since XBM uses little endian
            bits = ['0x{0:02x}'.format(reduce(lambda x, y: (x << 1) + y, bits[::-1])) for bits in iter_]
            i += 1
            write('    ')
            write(', '.join(bits))
            write(',\n' if i < height else '\n')
        write('};')
    return buf.getvalue()


def _svg(code, version, file, scale=1, module_color='#000', background=None,
              quiet_zone=4, xmldecl=True, svgns=True, title=None, svgclass='pyqrcode',
              lineclass='pyqrline', omithw=False, debug=False):
    """This function writes the QR code out as an SVG document. The
    code is drawn by drawing only the modules corresponding to a 1. They
    are drawn using a line, such that contiguous modules in a row
    are drawn with a single line. The file parameter is used to
    specify where to write the document to. It can either be a writable (binary)
    stream or a file path. The scale parameter is sets how large to draw
    a single module. By default one pixel is used to draw a single
    module. This may make the code to small to be read efficiently.
    Increasing the scale will make the code larger. This method will accept
    fractional scales (e.g. 2.5).

    :param module_color: Color of the QR code (default: ``#000`` (black))
    :param background: Optional background color.
            (default: ``None`` (no background))
    :param quiet_zone: Border around the QR code (also known as  quiet zone)
            (default: ``4``). Set to zero (``0``) if the code shouldn't
            have a border.
    :param xmldecl: Inidcates if the XML declaration header should be written
            (default: ``True``)
    :param svgns: Indicates if the SVG namespace should be written
            (default: ``True``)
    :param title: Optional title of the generated SVG document.
    :param svgclass: The CSS class of the SVG document
            (if set to ``None``, the SVG element won't have a class).
    :param lineclass: The CSS class of the path element
            (if set to ``None``, the path won't have a class).
    :param omithw: Indicates if width and height attributes should be
            omitted (default: ``False``). If these attributes are omitted,
            a ``viewBox`` attribute will be added to the document.
    :param debug: Inidicates if errors in the QR code should be added to the
            output (default: ``False``).
    """
    def write_unicode(write_meth, unicode_str):
        """\
        Encodes the provided string into UTF-8 and writes the result using
        the `write_meth`.
        """
        write_meth(unicode_str.encode('utf-8'))

    def line(x, y, length, relative):
        """Returns coordinates to draw a line with the provided length.
        """
        return '{0}{1} {2}h{3}'.format(('m' if relative else 'M'), x, y, length)

    def errline(col_number, row_number):
        """Returns the coordinates to draw an error bit.
        """
        # Debug path uses always absolute coordinates
        # .5 == stroke / 2
        return line(col_number + quiet_zone, row_number + quiet_zone + .5, 1, False)

    width, height = _get_symbol_size(version, scale, quiet_zone)
    with _writable(file, 'wb') as f:
        write = partial(write_unicode, f.write)
        write_bytes = f.write
        # Write the document header
        if xmldecl:
            write_bytes(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        write_bytes(b'<svg')
        if svgns:
            write_bytes(b' xmlns="http://www.w3.org/2000/svg"')
        if not omithw:
            write(' width="{0}" height="{1}"'.format(width, height))
        else:
            write(' viewBox="0 0 {0} {1}"'.format(width, height))
        if svgclass is not None:
            write_bytes(b' class=')
            write(quoteattr(svgclass))
        write_bytes(b'>')
        if title is not None:
            write('<title>{0}</title>'.format(title))
        # Draw a background rectangle if necessary
        if background is not None:
            write('<path fill="{2}" d="M0 0h{0}v{1}h-{0}z"/>'
                    .format(width, height, background))
        write_bytes(b'<path')
        if scale != 1:
            write(' transform="scale({0})"'.format(scale))
        if module_color is not None:
            write_bytes(b' stroke=')
            write(quoteattr(module_color))
        if lineclass is not None:
            write_bytes(b' class=')
            write(quoteattr(lineclass))
        write_bytes(b' d="')
        # Used to keep track of unknown/error coordinates.
        debug_path = ''
        # Current pen pointer position
        x, y = -quiet_zone, quiet_zone - .5  # .5 == stroke-width / 2
        wrote_bit = False
        # Loop through each row of the code
        for rnumber, row in enumerate(code):
            start_column = 0  # Reset the starting column number
            coord = ''  # Reset row coordinates
            y += 1  # Pen position on y-axis
            length = 0  # Reset line length
            # Examine every bit in the row
            for colnumber, bit in enumerate(row):
                if bit == 1:
                    length += 1
                else:
                    if length:
                        x = start_column - x
                        coord += line(x, y, length, relative=wrote_bit)
                        x = start_column + length
                        y = 0  # y-axis won't change unless the row changes
                        length = 0
                        wrote_bit = True
                    start_column = colnumber + 1
                    if debug and bit != 0:
                        debug_path += errline(colnumber, rnumber)
            if length:
                x = start_column - x
                coord += line(x, y, length, relative=wrote_bit)
                x = start_column + length
                wrote_bit = True
            write(coord)
        # Close path
        write_bytes(b'"/>')
        if debug and debug_path:
            write_bytes(b'<path')
            if scale != 1:
                write(' transform="scale({0})"'.format(scale))
            write(' class="pyqrerr" stroke="red" d="{0}"/>'.format(debug_path))
        # Close document
        write_bytes(b'</svg>\n')


def _png(code, version, file, scale=1, module_color=(0, 0, 0, 255),
         background=(255, 255, 255, 255), quiet_zone=4):
    """See: pyqrcode.QRCode.png()
    This function was abstracted away from QRCode to allow for the output of
    QR codes during the build process, i.e. for debugging. It works
    just the same except you must specify the code's version. This is needed
    to calculate the PNG's size.
    This method will write the given file out as a PNG file. Note, it
    depends on the PyPNG module to do this.
    :param module_color: Color of the QR code (default: ``(0, 0, 0, 255)`` (black))
    :param background: Optional background color. If set to ``None`` the PNG
            will have a transparent background.
            (default: ``(255, 255, 255, 255)`` (white))
    :param quiet_zone: Border around the QR code (also known as quiet zone)
            (default: ``4``). Set to zero (``0``) if the code shouldn't
            have a border.
    """
    if not _PYPNG_AVAILABLE:
        raise ValueError('PNG support needs PyPNG. Please install via pip --install pypng')
    # Coerce scale parameter into an integer
    try:
        scale = int(scale)
    except ValueError:
        raise ValueError('The scale parameter must be an integer')

    def png_bits(row):
        """\
        Inverts the row bits 0 -> 1, 1 -> 0 and scales the bits along the x-axis
        """
        for b in row:
            bit = b ^ 1
            for s in scale_range:
                yield bit

    def png_row(row):
        row = tuple(row)
        for i in scale_range:
            yield row

    def png_pallete_color(color):
        """This creates a palette color from a list or tuple. The list or
        tuple must be of length 3 (for rgb) or 4 (for rgba). The values
        must be between 0 and 255. Note rgb colors will be given an added
        alpha component set to 255.
        The pallete color is represented as a list, this is what is returned.
        """
        if color is None:
            return ()
        if not isinstance(color, (tuple, list)):
            r, g, b = _hex_to_rgb(color)
            return r, g, b, 255
        rgba = []
        if not (3 <= len(color) <= 4):
            raise ValueError('Colors must be a list or tuple of length '
                             ' 3 or 4. You passed in "{0}".'.format(color))
        for c in color:
            c = int(c)
            if 0 <= c <= 255:
                rgba.append(int(c))
            else:
                raise ValueError('Color components must be between 0 and 255')
        # Make all colors have an alpha channel
        if len(rgba) == 3:
            rgba.append(255)
        return tuple(rgba)

    if module_color is None:
        raise ValueError('The module_color must not be None')

    scale_range = range(scale)
    # foreground aka module color
    fg_col = png_pallete_color(module_color)
    transparent = background is None
    # If background color is set to None, the inverse color of the
    # foreground color is calculated
    bg_col = png_pallete_color(background) if background is not None else tuple([255 - c for c in fg_col])
    # Assume greyscale if module color is black and background color is white
    greyscale = fg_col[:3] == (0, 0, 0) and (transparent or bg_col == (255, 255, 255, 255))
    transparent_color = 1 if transparent and greyscale else None
    palette = (fg_col, bg_col) if not greyscale else None
    # The size of the PNG
    width, height = _get_symbol_size(version, scale, quiet_zone)
    # Write out the PNG
    w = png.Writer(width=width, height=height, greyscale=greyscale,
                   transparent=transparent_color, palette=palette,
                   bitdepth=1)
    with _writable(file, 'wb') as f:
        w.write_passes(f, chain.from_iterable(map(png_row, (map(png_bits, _matrix_iter(code, version,
                                                            scale=1,
                                                            quiet_zone=quiet_zone))))))


def _eps(code, version, file_or_path, scale=1, module_color=(0, 0, 0),
              background=None, quiet_zone=4):
    """This function writes the QR code out as an EPS document. The
    code is drawn by drawing only the modules corresponding to a 1. They
    are drawn using a line, such that contiguous modules in a row
    are drawn with a single line. The file parameter is used to
    specify where to write the document to. It can either be a writable (text)
    stream or a file path. The scale parameter is sets how large to draw
    a single module. By default one point (1/72 inch) is used to draw a single
    module. This may make the code to small to be read efficiently.
    Increasing the scale will make the code larger. This function will accept
    fractional scales (e.g. 2.5).

    :param module_color: Color of the QR code (default: ``(0, 0, 0)`` (black))
            The color can be specified as triple of floats (range: 0 .. 1) or
            triple of integers (range: 0 .. 255) or as hexadecimal value (i.e.
            ``#36c`` or ``#33B200``).
    :param background: Optional background color.
            (default: ``None`` (no background)). See `module_color` for the
            supported values.
    :param quiet_zone: Border around the QR code (also known as  quiet zone)
            (default: ``4``). Set to zero (``0``) if the code shouldn't
            have a border.
    """
    import time
    import textwrap

    def write_line(writemeth, content):
        """\
        Writes `content` and ``LF``.
        """
        # Postscript: Max. 255 characters per line
        for line in textwrap.wrap(content, 255):
            writemeth(line)
            writemeth('\n')

    def line(offset, length):
        """\
        Returns coordinates to draw a line with the provided length.
        """
        res = ''
        if offset > 0:
            res = ' {0} 0 m'.format(offset)
        res += ' {0} 0 l'.format(length)
        return res

    def rgb_to_floats(color):
        """\
        Converts the provided color into an acceptable format for Postscript's
         ``setrgbcolor``
        """
        def to_float(clr):
            if isinstance(clr, float):
                if not 0.0 <= clr <= 1.0:
                    raise ValueError('Invalid color "{0}". Not in range 0 .. 1'
                                     .format(clr))
                return clr
            if not 0 <= clr <= 255:
                raise ValueError('Invalid color "{0}". Not in range 0 .. 255'
                                 .format(clr))
            return 1/255.0 * clr if clr != 1 else clr

        if not isinstance(color, (tuple, list)):
            color = _hex_to_rgb(color)
        return tuple([to_float(i) for i in color])

    width, height = _get_symbol_size(version, scale, quiet_zone)
    with _writable(file_or_path, 'w') as f:
        writeline = partial(write_line, f.write)
        # Write common header
        writeline('%!PS-Adobe-3.0 EPSF-3.0')
        writeline('%%Creator: PyQRCode <https://pypi.python.org/pypi/PyQRCode/>')
        writeline('%%CreationDate: {0}'.format(time.strftime("%Y-%m-%d %H:%M:%S")))
        writeline('%%DocumentData: Clean7Bit')
        writeline('%%BoundingBox: 0 0 {0} {1}'.format(width, height))
        # Write the shortcuts
        writeline('/M { moveto } bind def')
        writeline('/m { rmoveto } bind def')
        writeline('/l { rlineto } bind def')
        mod_color = module_color if module_color == (0, 0, 0) else rgb_to_floats(module_color)
        if background is not None:
            writeline('{0:f} {1:f} {2:f} setrgbcolor clippath fill'
                      .format(*rgb_to_floats(background)))
            if mod_color == (0, 0, 0):
                # Reset RGB color back to black iff module color is black
                # In case module color != black set the module RGB color later
                writeline('0 0 0 setrgbcolor')
        if mod_color != (0, 0, 0):
            writeline('{0:f} {1:f} {2:f} setrgbcolor'.format(*mod_color))
        if scale != 1:
            writeline('{0} {0} scale'.format(scale))
        writeline('newpath')
        # Current pen position y-axis
        # Note: 0, 0 = lower left corner in PS coordinate system
        y = _get_symbol_size(version, scale=1, quiet_zone=0)[1] + quiet_zone - .5  # .5 = linewidth / 2
        last_bit = 1
        # Loop through each row of the code
        for row in code:
            offset = 0  # Set x-offset of the pen
            length = 0
            y -= 1  # Move pen along y-axis
            coord = '{0} {1} M'.format(quiet_zone, y)  # Move pen to initial pos
            for bit in row:
                if bit != last_bit:
                    if length:
                        coord += line(offset, length)
                        offset = 0
                        length = 0
                    last_bit = bit
                if bit == 1:
                    length += 1
                else:
                    offset += 1
            if length:
                coord += line(offset, length)
            writeline(coord)
        writeline('stroke')
        writeline('%%EOF')


def _hex_to_rgb(color):
    """\
    Helper function to convert a color provided in hexadecimal format
    as RGB triple.
    """
    if color[0] == '#':
        color = color[1:]
    if len(color) == 3:
        color = color[0] * 2 + color[1] * 2 + color[2] * 2
    if len(color) != 6:
        raise ValueError('Input #{0} is not in #RRGGBB format'.format(color))
    return [int(n, 16) for n in (color[:2], color[2:4], color[4:])]


def _matrix_iter(code, version, scale=1, quiet_zone=4):
    """\
    Returns an iterator / generator over the provided matrix which includes
    the border and the scaling factor.

    :param code: An iterable of integer lists
    :param int version: A version constant.
    :param int scale: The scaling factor (default: ``1``).
    :param int quiet_zone: The border size.
    """
    width, height = _get_symbol_size(version, scale=1, quiet_zone=0)  # scale=1, quiet_zone=0 is used by intention!
    border_row = [0] * width
    rng = range(-quiet_zone, height + quiet_zone)
    scale_range = range(scale)
    for i in rng:
        row = code[i] if 0 <= i < height else border_row
        scaled_row = tuple(chain.from_iterable([[1 if 0 <= j < width and row[j] else 0] * scale for j in rng]))
        for s in scale_range:
            yield scaled_row


def _terminal(code, version, out, quiet_zone=None):
    """\
    Function to write to a terminal which supports ANSI escape codes.

    :param code: The matrix to serialize.
    :param int version: The (Micro) QR code version.
    :param out: Filename or a file-like object supporting to write text.
    :param int quiet_zone: Integer indicating the size of the quiet zone.
            If set to ``None`` (default), the recommended border size
            will be used (``4`` for QR Codes, ``2`` for a Micro QR Codes).
    """
    with _writable(out, 'wt') as f:
        write = f.write
        colours = ['\033[{0}m'.format(i) for i in (7, 49)]
        for row in _matrix_iter(code, version, scale=1, quiet_zone=quiet_zone):
            prev_bit = -1
            cnt = 0
            for bit in row:
                if bit == prev_bit:
                    cnt += 1
                else:
                    if cnt:
                        write(colours[prev_bit])
                        write('  ' * cnt)
                        write('\033[0m')  # reset color
                    prev_bit = bit
                    cnt = 1
            if cnt:
                write(colours[prev_bit])
                write('  ' * cnt)
                write('\033[0m')  # reset color
            write('\n')


def _terminal_win(code, version, quiet_zone=None):  # pragma: no cover
    """\
    Function to write a QR Code to a MS Windows terminal.

    :param code: The matrix to serialize.
    :param int version: The (Micro) QR code version
    :param int quiet_zone: Integer indicating the size of the quiet zone.
            If set to ``None`` (default), the recommended border size
            will be used (``4`` for QR Codes, ``2`` for a Micro QR Codes).
    """
    import sys
    import struct
    import ctypes
    write = sys.stdout.write
    std_out = ctypes.windll.kernel32.GetStdHandle(-11)
    csbi = ctypes.create_string_buffer(22)
    res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(std_out, csbi)
    if not res:
        raise OSError('Cannot find information about the console. '
                      'Not running on the command line?')
    default_color = struct.unpack(b'hhhhHhhhhhh', csbi.raw)[4]
    set_color = partial(ctypes.windll.kernel32.SetConsoleTextAttribute, std_out)
    colours = (240, default_color)
    for row in _matrix_iter(code, version, scale=1, quiet_zone=quiet_zone):
        prev_bit = -1
        cnt = 0
        for bit in row:
            if bit == prev_bit:
                cnt += 1
            else:
                if cnt:
                    set_color(colours[prev_bit])
                    write('  ' * cnt)
                prev_bit = bit
                cnt = 1
        if cnt:
            set_color(colours[prev_bit])
            write('  ' * cnt)
        set_color(default_color)  # reset color
        write('\n')


def _terminal_deprecated(code, module_color='default', background='reverse', quiet_zone=4):
    """This method returns a string containing ASCII escape codes,
    such that if printed to a terminal, it will display a vaild
    QR code. The module_color and the background color should be keys
    in the tables.term_colors table for printing using the 8/16
    color scheme. Alternatively, they can be a number between 0 and
    256 in order to use the 88/256 color scheme. Otherwise, a
    ValueError will be raised.
    Note, the code is outputted by changing the background color. Then
    two spaces are written to the terminal. Finally, the terminal is
    reset back to how it was.
    """
    buf = io.StringIO()

    #: This is a table of ASCII escape code for terminal colors. QR codes
    #: are drawn using a space with a colored background. Hence, only
    #: codes affecting background colors have been added.
    #: http://misc.flogisoft.com/bash/tip_colors_and_formatting
    term_colors = {
        'default': 49,
        'background': 49,

        'reverse': 7,
        'reversed': 7,
        'inverse': 7,
        'inverted': 7,

        'black': 40,
        'red': 41,
        'green': 42,
        'yellow': 43,
        'blue': 44,
        'magenta': 45,
        'cyan': 46,
        'light gray': 47,
        'light grey': 47,
        'dark gray': 100,
        'dark grey': 100,
        'light red': 101,
        'light green': 102,
        'light blue': 103,
        'light yellow': 104,
        'light magenta': 105,
        'light cyan': 106,
        'white': 107
    }

    def draw_border():
        for i in range(quiet_zone):
            buf.write(background)

    if module_color in term_colors:
        data = '\033[{0}m  \033[0m'.format(
            term_colors[module_color])
    elif 0 <= module_color <= 256:
        data = '\033[48;5;{0}m  \033[0m'.format(module_color)
    else:
        raise ValueError('The module color, {0}, must a key in '
                         'pyqrcode.tables.term_colors or a number '
                         'between 0 and 256.'.format(
                         module_color))

    if background in term_colors:
        background = '\033[{0}m  \033[0m'.format(term_colors[background])
    elif 0 <= background <= 256:
        background = '\033[48;5;{0}m  \033[0m'.format(background)
    else:
        raise ValueError('The background color, {0}, must a key in '
                         'pyqrcode.tables.term_colors or a number '
                         'between 0 and 256.'.format(
                         background))

    #This will be the beginning and ending row for the code.
    border_row = background * (len(code[0]) + (2 * quiet_zone))

    #Make sure we begin on a new line, and force the terminal back
    #to normal
    buf.write('\n')

    #QRCodes have a quiet zone consisting of background modules
    for i in range(quiet_zone):
        buf.write(border_row)
        buf.write('\n')

    for row in code:
        #Each code has a quiet zone on the left side, this is the left
        #border for this code
        draw_border()

        for bit in row:
            if bit == 1:
                buf.write(data)
            elif bit == 0:
                buf.write(background)

        #Each row ends with a quiet zone on the right side, this is the
        #right hand border background modules
        draw_border()
        buf.write('\n')

    #QRCodes have a background quiet zone row following the code
    for i in range(quiet_zone):
        buf.write(border_row)
        buf.write('\n')

    return buf.getvalue()


#
# The exceptions are copied from Segno <https://pypi.org/project/segno/>  by 1:1
#
class QRCodeError(ValueError):
    """\
    Generic QR Code error.
    """


class VersionError(QRCodeError):
    """\
    Indicates errors related to the QR Code version.
    """


class ModeError(QRCodeError):
    """\
    Indicates errors related to QR Code mode.
    """


class ErrorLevelError(QRCodeError):
    """\
    Indicates errors related to QR Code error correction level.
    """


class MaskError(QRCodeError):
    """\
    Indicates errors related to QR Code data mask.
    """


class DataOverflowError(QRCodeError):
    """\
    Indicates a problem that the provided data does not fit into the
    provided QR Code version or the data is too large in general.
    """

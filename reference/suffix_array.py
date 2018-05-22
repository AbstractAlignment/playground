from __future__ import print_function
import pprint


class ArrayGenerator(object):
    def __init__(self):
        "Handle transformation operations on sequence strings"

    def generate_suffixes(self, sequence):
        """
        Generate all suffixes from a given string
        """
        # Add a terminator sigil to the string
        if (sequence is None):
            raise "No sequence provided to generate suffixes"

        sequence = sequence + "$"
        # Pre-allocate matrix
        matrix = [[None] * (len(sequence) + 1) for i in range(len(sequence))]

        for x in xrange(0, len(sequence)):
            rotated_seq = self.generate_rotamer(sequence, x)
            for y in range(len(sequence)):
                matrix[x][y] = rotated_seq[y]
            matrix[x][-1] = x

        # Now sort the matrix asciibetically
        # matrix.sort?
        pp = pprint.PrettyPrinter()
        pp.pprint(matrix)

        return matrix

    def generate_rotamer(self, sequence, suffix):
        """
        Given an input sequence and the suffix array index, generate the
        original sequence
        """
        if not isinstance(suffix, int):
            raise Exception("suffix is invalid")

        # Might need the sigil to be there. We'll see
        if (sequence[-1] != "$"):
            sequence = sequence + "$"

        return sequence[suffix:] + sequence[:suffix]

    def generate_suffix_array(self, matrix):
        """
        Turn a sorted suffix matrix into a suffix array
        """
        def matrix_sort_property(k):
            return tuple(k[i] for i in range(len(k) - 1))

        pp = pprint.PrettyPrinter()
        matrix.sort(key=matrix_sort_property)
        pp.pprint(matrix)

        return [matrix[x][-1] for x in range(len(matrix))]

    def burrows_wheeler_transform(self, matrix):
        """
        Given a lexically sorted suffix array, extract the BWT string from it
        """

        bwt = ""
        for x in xrange(0, (len(matrix))):
            # exclude the original ordering index in the final column of the matrix
            bwt += matrix[x][-2]
        return bwt


if __name__ == "__main__":
    agen = ArrayGenerator()
    suffixes = agen.generate_suffixes("AATGA")
    suffix_array = agen.generate_suffix_array(suffixes)
    pp = pprint.PrettyPrinter()
    pp.pprint(suffix_array)
    pp.pprint(agen.burrows_wheeler_transform(suffixes))

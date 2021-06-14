#!/usr/bin/python

import sys
import getopt
from defs import *


def main(argv):
    inputblastout = ''
    mutation = ''

    example_cmd = "mutation_detecter.py -i <BLAST out in xml format> -m <mutation e.g. K27F>"
    try:
        opts, args = getopt.getopt(
            argv, "hi:m:", ["ifile=", "mutation="])
    except getopt.GetoptError:
        print(example_cmd)
        sys.exit(2)
    if len(argv) != 4:
        print(example_cmd)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(example_cmd)
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputblastout = arg
        elif opt in ("-m", "--mutation"):
            mutation = arg

    fasta = writeproteinfasta(inputblastout)
    getMutation(fasta, mutation)


if __name__ == "__main__":
    main(sys.argv[1:])

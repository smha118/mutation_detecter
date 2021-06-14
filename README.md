# Mutation Detecter

## Description

This python code was initially designed for study "Using a public database of Neisseria gonorrhoeae genomes
to detect mutations associated with zoliflodacin resistance" by Adamson <em>et al.</em> 2021 (pending)

The code simply parses BLAST result in xml format and translate the sequence to check if given mutation is actually present.

## Dependencies:

python ver. 3.8.3+\
Biopython ver. 1.78+

## Usage:

```bash
$ ./mutation_detecter.py -i examples/DRR099842.xml -m S91F
```

-i BLAST result in xml format as an input \
-m Mutation interested

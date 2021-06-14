# Mutation Detecter

## Description

This python code was initially designed for the study "Using a public database of Neisseria gonorrhoeae genomes to detect mutations associated with zoliflodacin resistance" by Adamson et al. 2021 (pending)
The code simply parses BLAST result in XML format and translates the sequence to check if the given mutation is present.

## Dependencies:

python ver. 3.8.3+\
Biopython ver. 1.78+

## Usage:

```bash
$ ./mutation_detecter.py -i examples/DRR099842.xml -m S91F
```

-i BLAST result in xml format as an input \
-m Mutation interested

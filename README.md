# Mutation Detector

## Description

This Python code was initially designed for the study titled 'Using a Public Database of Neisseria gonorrhoeae Genomes to Detect Mutations Associated with Zoliflodacin Resistance' by [Adamson et al. 2021](https://doi.org/10.1093/jac/dkab262). 
It has also been utilized in two subsequent studies:

* 'Reliability of Genetic Alterations in Predicting Ceftriaxone Resistance in Neisseria gonorrhoeae Globally' by [Lin et al. 2022](https://doi.org/10.1128/spectrum.02065-21)
* 'Machine learning to predict ceftriaxone resistance using single nucleotide polymorphisms within a global database of Neisseria gonorrhoeae genomess' by [Ha et al. 2024](https://doi.org/10.1128/spectrum.01703-23)

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

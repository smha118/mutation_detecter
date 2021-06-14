from Bio.Seq import Seq
import sys
import os
from Bio.Blast import NCBIXML


def writeproteinfasta(blastXml):
    foutpath = "tmp/"
    if not os.path.exists(foutpath):
        os.makedirs(foutpath)

    path = os.path.splitext(blastXml)

    acc = os.path.basename(path[0])
    fname = open(blastXml)

    blast_records = NCBIXML.parse(fname)
    blast_record = next(blast_records)
    fout = foutpath+acc+".fasta"
    with open(fout, 'w') as protein_fasta:
        dnas = list()
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                coding_dna = Seq(hsp.sbjct.replace("-", ""))
                dnas.append(coding_dna)
        dnas = sorted(dnas, key=len)
        if not dnas:
            print(acc)
        else:
            longest_dna = dnas[-1]
            frame1 = str(longest_dna[0:].translate())
            if frame1.count("*") == 1 and frame1.startswith("M"):
                protein_fasta.write(
                    ">"+acc+"|"+str(hsp.sbjct_start)+"|" + "\n")
                protein_fasta.write(frame1+"\n")
            elif frame1.count("*") > 1 and frame1.startswith("M"):
                print("Deleterious mutation found! Abort!")
                print(frame1)
                sys.exit(2)
            else:
                print("Only partial genes found")
                print(frame1)
                sys.exit(2)

    fname.close()
    return fout


def addMutationDictionary(path, protein_sequence, position, mutations):
    position = position-1
    acc = os.path.basename(path).replace(".fasta", "")
    if(len(protein_sequence) >= position):
        mutations[acc] = protein_sequence[position]
    else:
        if "partial" not in mutations.keys():
            mutations["partial"] = list()
        mutations["partial"].append(
            os.path.basename(path).replace(".fasta", ""))
    return mutations


def getMutation(input_fasta_path, mutation):
    i = 0
    mutations = dict()
    path = input_fasta_path
    aa_position = int(mutation[1:len(mutation)-1])
    ref_aa = mutation[0]
    exp_aa = mutation[-1]

    with open(path) as lines:
        i = i+1
        for line in lines:
            if ">" not in line:
                # if(gene == 'gyrA'):
                if(len(line) < 930 and len(line) > 850):
                    mutations = addMutationDictionary(
                        path, line, aa_position, mutations)
                    print(mutations)
                else:
                    if "partial" not in mutations.keys():
                        mutations["partial"] = list()
                    mutations["partial"].append(
                        os.path.basename(path).replace(".fasta", ""))

import sys
import pandas as pd
from Bio import SeqIO
import gzip
import bz2
import argparse
from .genbank import extract_cds_annot, extract_seq_annot

def readparse(args): 
    parser = argparse.ArgumentParser(description="Description:\nThis Script was designed to extract sequences, the descriptions of seqences\nand the annotation of CDS from GenBank files.\n"
            "Developer: Shuangbin Xu.\n"
            "Email: xshuangbin@163.com\n", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("genbank_file", metavar="genbank", type=str, help="input file, the GenBank format file")
    parser.add_argument("-s", dest="seqfasta", metavar="seqfasta", type=str, \
                        default="GenBankSeq.fasta", help="the output of sequences, default is GenBankSeq.fasta")
    parser.add_argument("-t", dest="seqannot", metavar="seqannot", type=str, \
                        default="GenBankSeq.annot", help="the output of sequences annotation, default is GenBankSeq.annot")
    parser.add_argument("-c", dest="cdsannot", metavar="cdsannot", type=str, \
                        default="GenBankCDS.annot", help="the output of CDS annotation, default is GenBankCDS.annot")
    args = parser.parse_args()
    return (vars(args))

def main():
    params = readparse(sys.argv)
    genbank = params["genbank_file"]
    seqfa = params["seqfasta"]
    seqannot = params["seqannot"]
    cdsannot = params["cdsannot"]
    if genbank.endswith(".gz"):
        input_handle = gzip.open(genbank, "rt")
    elif genbank.endswith(".bz2"):
        input_handle = bz2.open(genbank, "rt")
    else:
        input_handle = open(genbank, "r")
    cdslist = []
    seqlist = []
    seqfa = open(seqfa, "w")
    for seq_record in SeqIO.parse(input_handle, "genbank"):
        print ("Parsing GenBank record: %s" % seq_record.id)
        cds = extract_cds_annot(seq_record)
        cdslist.append(cds)
        seqann = extract_seq_annot(seq_record)
        seqlist.append(seqann)
        seqfa.write(">%s\n%s\n" % (seq_record.id,str(seq_record.seq)))
    input_handle.close()
    cdslist = pd.concat(cdslist, sort=False)
    seqlist = pd.concat(seqlist, sort=False)
    cdslist.to_csv(cdsannot, sep="\t", index=False)
    seqlist.to_csv(seqannot, sep="\t", index=False)
    seqfa.close()

if __name__ == "__main__":
    main()

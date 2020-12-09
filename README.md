# BioFtParse

This package will save some scripts to parse some common bioinformatic
format file. Now, it only contain `parse_genbank.py` to parse the
`genebank` file, and generate `fasta` file contained sequences, `CDS`
annotation table, and `Seq` annotation table.

## Install

It depends on `python3`. So your computer should have been installed
`python3` before install it.

``` bash
git clone https://github.com/xiangpin/BioFtParse.git
python setup.py install
# or sudo python setup.py install
```

## Usage

These some examples in
[examples](https://github.com/xiangpin/BioFtParse/tree/master/examples).
Or you can view the help information with the following code.

``` bash
parse_genbank.py -h
```

    ## usage: parse_genbank.py [-h] [-s seqfasta] [-t seqannot] [-c cdsannot] genbank
    ## 
    ## Description:
    ## This Script was designed to extract sequences, the descriptions of seqences
    ## and the annotation of CDS from GenBank files.
    ## Developer: Shuangbin Xu.
    ## Email: xshuangbin@163.com
    ## 
    ## positional arguments:
    ##   genbank      input file, the GenBank format file
    ## 
    ## optional arguments:
    ##   -h, --help   show this help message and exit
    ##   -s seqfasta  the output of sequences, default is GenBankSeq.fasta
    ##   -t seqannot  the output of sequences annotation, default is GenBankSeq.annot
    ##   -c cdsannot  the output of CDS annotation, default is GenBankCDS.annot

#!/bin/bash


input="output_files/second_protein.fasta"
output="output_files/motifs.patmatmotifs"
download=false

if $download
then
    wget https://ftp.expasy.org/databases/prosite/prosite.dat
    wget https://ftp.expasy.org/databases/prosite/prosite.doc
    mkdir prosite
    mv prosite.dat prosite
    mv prosite.doc prosite
fi
prosextract prosite
patmatmotifs -sequence $input -outfile $output
#!/bin/bash


printUsage(){
    echo "Usage blast.sh (local|remoto)";
    exit 1
}

INPUT_FILE="output_files/all_proteins_longer_than_30.fasta"
OUTPUT_FILE="output_files/resultados_blast/resultado_blast.json"

echo "Doing a local search from $INPUT_FILE to $OUTPUT_FILE"
blastp -db swissprotDB -query $INPUT_FILE -out $OUTPUT_FILE -outfmt 13
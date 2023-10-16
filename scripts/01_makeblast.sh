#!/bin/bash

# Check if the required parameters are provided
if [ $# -ne 3 ]; then
    echo "Usage: $0 <reference_genome_path> <database_name> <probe_sequences_fasta>"
    exit 1
fi

# Extract parameters
reference_genome_path="$1"
database_name="$2"
probe_sequences_fasta="$3"

# Navigate to the "blast" directory
cd ../blast

# Create a BLAST database from the reference genome
#makeblastdb -in "$reference_genome_path" -dbtype nucl -parse_seqids -out "$database_name"

# Create an index with a specified word size (e.g., 15) in the "blast" directory (optional)
makembindex -input "$database_name" -iformat blastdb -nmer 15

# Perform BLAST using the specified parameters
blastn -db "$database_name" -word_size 30 -perc_identity 100 -outfmt "6 qseqid sseqid pident sstart send" -query "../probes/$probe_sequences_fasta" -use_index True -index_name "$database_name" -num_threads 8 -out blast_out.txt

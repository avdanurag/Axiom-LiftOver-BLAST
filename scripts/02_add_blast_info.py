import argparse

def merge_axiom_with_blast(axiom_file_path, blast_file_path, output_file_path):

    # Create a dictionary to store BLAST information based on the common identifier (Probe-Id)
    blast_info = {}

    # Read BLAST results and store them in the dictionary
    with open(blast_file_path, 'r') as blast_file:
        for line in blast_file:
            fields = line.strip().split('\t')
            if len(fields) >= 5:
                probe_id, chromosome, identity, start, end = fields[0], fields[1], fields[2], fields[3], fields[4]
                blast_info[probe_id] = {'chromosome': chromosome, 'identity': identity, 'start': start, 'end': end}

    # Read the Axiom array file and merge BLAST information
    with open(axiom_file_path, 'r') as axiom_file, open(output_file_path, 'w') as output_file:
        # Read the header line from the Axiom array file and write it to the output file
        header = axiom_file.readline().strip()
        output_file.write(f'{header}\tchromosome\tidentity\tstart\tend\n')

        # Iterate through the Axiom array data
        for line in axiom_file:
            fields = line.strip().split('\t')
            probe_id = fields[0]

            # Check if the Probe-Id exists in the BLAST information dictionary
            if probe_id in blast_info:
                blast_data = blast_info[probe_id]
                chromosome, identity, start, end = blast_data['chromosome'], blast_data['identity'], blast_data['start'], blast_data['end']
            else:
                # If no BLAST information is available, use placeholders or handle it as needed
                chromosome, identity, start, end = '', '', '', ''

            # Write the merged data to the output file
            output_file.write(f'{line.strip()}\t{chromosome}\t{identity}\t{start}\t{end}\n')

    print(f'Merged data has been written to "{output_file_path}"')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('axiom_file', help='Path to the Axiom array file')
    parser.add_argument('blast_file', help='Path to the BLAST results file')
    parser.add_argument('output_file', help='Path to the output file')
    args = parser.parse_args()

    merge_axiom_with_blast(args.axiom_file, args.blast_file, args.output_file)


if __name__ == '__main__':
    main()


import sys

def create_fasta_file(input_file_name, output_file_name):

    # Open the tab-delimited input file
    with open(input_file_name, 'r') as input_file:
        # Open a FASTA output file for writing
        with open(output_file_name, 'w') as output_file:
            # Initialize a counter to keep track of lines
            line_count = 0

            # Iterate through each line in the input file
            for line in input_file:
                # Increment the line count
                line_count += 1

                # Skip the first two lines (header lines)
                if line_count <= 2:
                    continue

                # Split the line into columns using tab as the delimiter
                columns = line.strip().split('\t')

                # Check if there are at least 2 columns (Probe-Id and sequence)
                if len(columns) >= 2:
                    probe_id, sequence = columns[0], columns[1]

                    # Write the FASTA entry to the output file
                    output_file.write(f'> {probe_id}\n{sequence}\n')

    print(f'FASTA file "{output_file_name}" has been created.')


if __name__ == '__main__':

    # Get the input and output file names from the command line
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]

    # Create the FASTA file
    create_fasta_file(input_file_name, output_file_name)


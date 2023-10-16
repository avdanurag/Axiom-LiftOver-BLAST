import argparse
import pandas as pd

def update_mo17_pos(input_file_path, output_file_path):

    # Read the input file
    df = pd.read_csv(input_file_path, sep='\t')

    # Define a function to calculate Pos-Mo17 based on Tile_strand
    def calculate_pos(tile_strand, start, end):
        if pd.isna(tile_strand):
            return 'NA'
        if tile_strand == 'f':
            result = end + 1
            return int(result) if not pd.isna(result) else 'NA'
        if tile_strand == 'r':
            result = start - 1
            return int(result) if not pd.isna(result) else 'NA'
        return 'NA'

    # Apply the function to create the Chr-Mo17 and Pos-Mo17 columns
    df['Chr-Mo17'] = df['chromosome'].apply(lambda x: 'NA' if pd.isna(x) else x)
    df['Pos-Mo17'] = df.apply(lambda row: calculate_pos(row['Tile_strand'], row['start'], row['end']), axis=1)

    # Save the modified DataFrame to a new file
    df.to_csv(output_file_path, sep='\t', index=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Path to the input file')
    parser.add_argument('output_file', help='Path to the output file')
    args = parser.parse_args()

    update_mo17_pos(args.input_file, args.output_file)


if __name__ == '__main__':
    main()


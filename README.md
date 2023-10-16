# Axiom-LiftOver-BLAST
Coordinate conversion of Axiom SNP array markers using BLAST.

## Folder Structure

The project is organized into the following directories and scripts:

- **blast**: use to store blast results and databses.
- **data**: conatins demo vcf file.
- **probes**: contains demo probe list.
- **scripts**: This is where all the conversion scripts are located.

## Getting Started

To use these scripts effectively, follow the steps outlined below:

### Prerequisites

1. **NCBI BLAST**
2. **Python modules** : argpars, pandas

### Installation

1. Clone or download this repository to your local machine:

   ```bash
   git clone https://github.com/avdanurag/Axiom-LiftOver-BLAST.git

## Usage

The scripts are organized in the `scripts` directory and can be used sequentially for coordinate conversion. Here's a brief overview of each script:

- **00_create_fasta.py**: This script is used to create a FASTA file from your SNP array probe list.

- **01_makeblast.sh**: A shell script for running BLAST to align probes with a reference genome.

- **02_add_blast_info.py**: This script is used to combine BLAST alignment information probe list.

- **03_update_marker_pos.py**: This script adds new marker positions of markers based on BLAST results.

- **04_update_vcf_coordinates.py**: Use this script to update VCF coordinates

For detailed instructions on how to use each script, refer to the individual script files.


## Probe list format
Arrange you probe information in following format:

| Probe-Id     | sequence                       | allele | Tile_strand | ID          | probe_set_ID | Affy_SNP_ID   | cust_ID     |
|--------------|--------------------------------|--------|-------------|-------------|--------------|---------------|-------------|
| 10-148972870 | ATCGGGGCCTAAGGTAGACGCCAGTGGTTC | C/T    | f           | AX-90525723 | AX-90525723  | Affx-90758874 | PHM1506.18  |
| 10-10882576  | AACGACGCTCTTCCGCACGTCCAACCGCAG | C/T    | f           | AX-90525726 | AX-90525726  | Affx-90293863 | PHM15331.16 |
| 3-156482775  | TTTCGAGTTCATCTTCTGGACCTCCTCCTT | C/T    | f           | AX-90525729 | AX-90525729  | Affx-90864597 | PHM1626.34  |
| 3-191612649  | CACAGTTCCGGCAATGTTCCGATGAGAAAA | C/T    | f           | AX-90525738 | AX-90525738  | Affx-90967383 | PHM3075.15  |
| 2-5839907    | CGTTTTGAAACGACTGTAAATCCCTCTGTA | C/T    | f           | AX-90525741 | AX-90525741  | Affx-90601730 | PHM3309.8   |
| 5-2926821    | GAAGAGTGTGCTCAGAGCAGAGAAGATAGG | A/G    | f           | AX-90525746 | AX-90525746  | Affx-90194631 | PHM3714.12  |
| 1-83780916   | AAGCATCAGCATTTTGAGGCAACATGAGCT | A/G    | f           | AX-90525748 | AX-90525748  | Affx-91054640 | PHM4185.17  |
| 1-67646946   | TTTGCGTTTCCAGAGCCATGCGGTGCTTGC | C/T    | f           | AX-90525756 | AX-90525756  | Affx-90294728 | PHM5098.25  |
| 5-44407599   | GCAGGGCCATTATACCAGAGGATACGGCGA | C/T    | f           | AX-90525763 | AX-90525763  | Affx-90315003 | PHM6795.5   |
| 10-80719215  | ATACTAATGGAACTTTGCGCAAAGAAGAAG | C/T    | f           | AX-90525768 | AX-90525768  | Affx-91218396 | PHM9266.23  |
| 10-80719268  | GTACTTATCTAAGTGCTTTGTGAGTTGTTT | A/G    | f           | AX-90525769 | AX-90525769  | Affx-91102582 | PHM9266.25  |
| 9-17750933   | TATTGCAGCATGCCAGCATTTACATGCTAA | C/T    | f           | AX-90525770 | AX-90525770  | Affx-90145683 | PHM9374.5   |
| 3-161257992  | CGACACCGATCATGAGGAGATGCTATCTGG | A/G    | f           | AX-90525773 | AX-90525773  | Affx-90559611 | PHM9914.11  |

## Example Usage

Here's an example of how to run these scripts:

1. Prepare your Axiom SNP marker data in a suitable format.

2. Ensure you have a reference genome in a format that is compatible with BLAST.

3. Execute the scripts sequentially, following the instructions provided in each script's documentation.


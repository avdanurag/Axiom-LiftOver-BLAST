
import argparse
import pandas as pd

# Define command-line arguments using argparse
parser = argparse.ArgumentParser(description="Update VCF file based on Probe-ID mapping")
parser.add_argument("vcf_file", help="Path to the VCF file")
parser.add_argument("axiom_id_file", help="Path to the Axiom ID file")
parser.add_argument("output_file", help="Path to the output VCF file")

# Parse the command-line arguments
args = parser.parse_args()

# Create a dictionary to store the mapping of Probe-Ids to chromosome and position
mapping = {}

# Read the Axiom ID file and populate the mapping dictionary
with open(args.axiom_id_file, "r") as axiom_id:
    next(axiom_id)  # Skip the header line
    for line in axiom_id:
        fields = line.strip().split("\t")
        probe_id = fields[0]
        chromosome_mo17 = fields[-2]
        position_mo17 = fields[-1]
        mapping[probe_id] = (chromosome_mo17, position_mo17)
       #print(mapping)

# Open the output VCF file for writing
with open(args.output_file, "w") as output:
    # Read the VCF file and update chromosome and position based on the mapping
    with open(args.vcf_file, "r") as vcf:
        for line in vcf:
            if line.startswith("#"):
                output.write(line)  # Write header lines to the output
            else:
                fields = line.strip().split("\t")
                temp_id = f"{fields[0]}-{fields[1]}"
                #print(temp_id)

                if temp_id in mapping:
                    chromosome_mo17, position_mo17 = mapping[temp_id]
                    fields[0] = chromosome_mo17
                    fields[1] = position_mo17
                    output.write("\t".join(fields) + "\n")  # Write the updated line to the output

print(f"Updated VCF file saved as {args.output_file}")


import os, argparse
from pipeline_functions import kmer_alignment, taxonomic_assignments
from basic_function import get_fastq_files_set, sort_dictionary_key_value


parser=argparse.ArgumentParser()
parser.add_argument("-f" ,"--fastq_files", type = str, help="-- FastQ files folder --")
args=parser.parse_args()
fastq_files_path = args.fastq_files

for sample in sort_dictionary_key_value(get_fastq_files_set(fastq_files_path)):
    for sample_prefix,fastq in sample.items():
        fastq_R1 = fastq[0]
        fastq_R2 = fastq[1]
        kmer_alignment(sample_prefix, fastq_R1, fastq_R2)
        taxonomic_assignments(sample_prefix)
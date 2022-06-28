import os
from argparse import ArgumentParser
from pipeline_functions import kmer_alignment, taxonomic_assignments
from basic_function import get_fastq_files_set, sort_dictionary_key_value
from toil.common import Toil
from toil.job import Job
from toil.realtimeLogger import RealtimeLogger


parser = ArgumentParser()
Job.Runner.addToilOptions(parser)
parser.add_argument("--fastq_files", type = str, help="-- FastQ files folder --")
options = parser.parse_args()

fastq_files_path = options.fastq_files

alignment_job = Job()
taxonomic_assignments_job = Job()

for sample in sort_dictionary_key_value(get_fastq_files_set(fastq_files_path)):
    for sample_prefix,fastq in sample.items():
        fastq_R1 = fastq[0]
        fastq_R2 = fastq[1]
        alignment_job.addChildFn(kmer_alignment, sample_prefix, fastq_R1, fastq_R2)
        taxonomic_assignments_job.addChildFn(taxonomic_assignments, sample_prefix)

alignment_job.addFollowOn(taxonomic_assignments_job)



options.clean = "always"
with Toil(options) as toil:
    output = toil.start(alignment_job)

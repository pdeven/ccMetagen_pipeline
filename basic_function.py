
def singularity_call(tool, command_list):
    # singularity exec ccmetagen1.4.0.sif kma -1t1 -mem_mode -and -apm f -nc -status -verbose -ef -t 5 -ipe /mnt/data/ccmetagene/sample_data/16s_rna_fastq_files/O-KE2_R1.fq.gz /mnt/data/ccmetagene/sample_data/16s_rna_fastq_files/O-KE2_R2.fq.gz -tmp /mnt/data/ccmetagene/sample_data/temp_directory -o results/O-KE1_output -t_db /mnt/data/ccmetagene/database/ncbi_16s 2>&1 | tee /mnt/data/ccmetagene/sample_data/log_dir/O-KE1_output_kma.log
    commands = " ".join(command_list)

    singularity_base_command = "singularity exec " + tool + commands

    return singularity_base_command

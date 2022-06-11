import os

# generic lambdas
sort_dictionary_key_value = lambda dictionary : [ {iter:sorted(values)} for iter,values in sorted(dictionary.items())]


# Methods
def singularity_call(tool, command_list):
    commands = " ".join(command_list)
    singularity_base_command = "singularity exec " + tool + commands
    return singularity_base_command

def get_fastq_files_set(fastq_files_path):
    split_before = lambda st : st.split("_")[0]
    fastq_files_directory = os.listdir(fastq_files_path)
    file_set = set()
    for files in fastq_files_directory: file_set.add(split_before(files))
    file_set_map = {}
    for single in file_set: file_set_map[single]=[]
    for files in fastq_files_directory:
        sample_prefix = split_before(files)
        file_set_map[sample_prefix].append(os.path.realpath(os.path.join(fastq_files_path, files)))
    return file_set_map
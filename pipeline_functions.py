# ccMetagen pipeline utility functions
# Use these functions by import pipeline

import os
import subprocess
from base_config import KMA_INDEXED_DATABASE , TEMPORARY_DIRECTORY , LOG_DIRECTORY , RESULTS_FOLDER
from basic_function import singularity_call
from tools_config import k_mer_align

def kmer_alignment(
    PREFIX,
    R1,
    R2
    ):
    
    RESULTS_PATH = os.path.join(RESULTS_FOLDER , "result_" + PREFIX , PREFIX + "_kma")
    LOG_PATH = os.path.join(LOG_DIRECTORY, "log_"+ PREFIX, PREFIX +"_log")
    command = [
        "-1t1",
        "-mem_mode",
        "-and",
        "-apm",
        "f",
        "-nc",
        "-status",
        "-verbose",
        "-ef",
        "-t",
        "5",
        "-ipe",    
        R1,
        R2,    
        "-tmp",
        TEMPORARY_DIRECTORY,
        "-o",
        RESULTS_PATH,  
        "-t_db",
        KMA_INDEXED_DATABASE,
        "2>&1",        
        "|",
        "tee",
        LOG_PATH 
    ]

    cmd = singularity_call(k_mer_align, command)

    
    # subprocess.run(cmd, shell=True)
    return cmd
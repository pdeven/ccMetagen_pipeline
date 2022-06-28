# ccMetagen pipeline utility functions
# Use these functions by import pipeline

import os
import subprocess
from base_config import KMA_INDEXED_DATABASE , TEMPORARY_DIRECTORY , LOG_DIRECTORY , RESULTS_FOLDER, MEMORY , CORES , DISK 
from basic_function import singularity_call
from tools_config import k_mer_align , taxonomic_assign
from toil.common import Toil
from toil.job import Job
from toil.realtimeLogger import RealtimeLogger

def kmer_alignment(
    PREFIX,
    R1,
    R2,
    memory=MEMORY,
    cores=CORES,
    disk=DISK
    ):
    res = os.path.join ( RESULTS_FOLDER , PREFIX )
    log = os.path.join ( LOG_DIRECTORY , PREFIX )
    os.makedirs(res, exist_ok = True )
    os.makedirs(log, exist_ok = True )

    RESULTS_PATH = os.path.join(RESULTS_FOLDER , PREFIX , PREFIX + "_kma")
    LOG_PATH = os.path.join(LOG_DIRECTORY, PREFIX , PREFIX +"_log")
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

    subprocess.run(cmd, shell=True)
    
def taxonomic_assignments(
    PREFIX,
    memory=MEMORY,
    cores=CORES,
    disk=DISK
    ):
    
    RESULTS_PATH = os.path.join(RESULTS_FOLDER , PREFIX , PREFIX + "_kma.res")
    TAXONOMY_FILE_PATH = os.path.join(RESULTS_FOLDER , PREFIX , PREFIX + "_taxonomy")

    command = [
        "-i",
        RESULTS_PATH,
        "-o",
        TAXONOMY_FILE_PATH
    ]
    
    cmd = singularity_call(taxonomic_assign, command)

    subprocess.run(cmd, shell=True)
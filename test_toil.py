import os
import sys
import random
from toil.common import Toil
from toil.job import Job
from toil.realtimeLogger import RealtimeLogger
from memory_profiler import profile
c_memory = '1GB'

parent = Job()

lines = lambda x:[y for y in open(x,'r').readlines()]
out=open("log.txt",'w')
out.write("counts\n")
out.close()
def c(line_R):
    m_r= [0]*4
    for line in line_R:
        if line[0]!="@" and line[0]!="+":
            for el in line:
                if el=="A": m_r[0]+=1
                elif el=="T": m_r[1]+=1
                elif el=="G": m_r[2]+=1
                elif el=="C": m_r[3]+=1
    return m_r

def sum(a1,a2):
    return [a1[0]+a2[0],a1[1]+a2[1],a1[2]+a2[2],a1[3]+a2[3]]
@profile
def count_ATGC(R1, R2):
    lines_R1 = lines(R1)
    lines_R2 = lines(R2)
    c1=c(lines_R1)
    c2=c(lines_R2)
    out = open("log.txt",'a')
    sum2 = str(sum(c1,c2))
    out.write(sum2+"\n")
    out.close()
    print(f"======================== > {sum2}   < =================================================")

count_ATGC("/mnt/data/ccmetagen/sample_data/16s_rna_fastq_files/KE1_R1.fq",
         "/mnt/data/ccmetagen/sample_data/16s_rna_fastq_files/KE1_R2.fq")
count_ATGC("/mnt/data/ccmetagen/sample_data/16s_rna_fastq_files/KE1_R1.fq",
         "/mnt/data/ccmetagen/sample_data/16s_rna_fastq_files/KE1_R2.fq")

'''
if __name__ == "__main__":
    parser = Job.Runner.getDefaultArgumentParser()
    options = parser.parse_args()
    options.clean = "always"

    f1 = Job.wrapFn(count_ATGC, "/mnt/data/ccmetagen/sample_data/16s_rna_fastq_files/KE1_R1.fq",
         "/mnt/data/ccmetagen/sample_data/16s_rna_fastq_files/KE1_R2.fq")
    f2 = Job.wrapFn(count_ATGC, "/mnt/data/ccmetagen/sample_data/16s_rna_fastq_files/KE2_R1.fq",
        "/mnt/data/ccmetagen/sample_data/16s_rna_fastq_files/KE2_R2.fq")
    f3 = Job.wrapFn(count_ATGC, "/mnt/data/ccmetagen/sample_data/16s_rna_fastq_files/KE6_R1.fq",
        "/mnt/data/ccmetagen/sample_data/16s_rna_fastq_files/KE6_R2.fq")
    f4 = Job.wrapFn(count_ATGC, "/mnt/data/ccmetagen/sample_data/16s_rna_fastq_files/KE6_R1.fq",
        "/mnt/data/ccmetagen/sample_data/16s_rna_fastq_files/KE6_R2.fq")
    parent.addChild(f1)
    parent.addChild(f2)
    parent.addChild(f3)
    parent.addFollowOn(f4)
    with Toil(options) as toil:
        output = toil.start(parent)

    print(output)
'''
#!/bin/bash
#$ -N d_ukbb
#$ -cwd
#$ -l h_vmem=8G
#$ -l h_rt=10:00:00

module load Anaconda/3.7
module load general-softwares
python ukbb_download_results.py

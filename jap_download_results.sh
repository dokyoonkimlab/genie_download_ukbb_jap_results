#!/bin/bash
#$ -N d_jap
#$ -cwd
#$ -l h_vmem=8G
#$ -l h_rt=10:00:00

module load general-softwares
python jap_download_results.py

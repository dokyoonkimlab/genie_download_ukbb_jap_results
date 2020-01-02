import sys
import os
import apsw
import csv

input_file = os.path.join("manifest_files", "Matching_phe_genie_ukbb_jap.txt") #sys.argv[1]
input_ukbb_manifest_file = os.path.join("manifest_files", "UKBB GWAS Imputed v3 - File Manifest Release 20180731 - Manifest 201807.txt")

ukbb_phe_set = set()
with open(input_file) as inf:
	reader = csv.reader(inf, delimiter = '\t')
	next(reader)
	for parts in reader:
		for i in range(3, 8):
			parts[i] = parts[i].strip()
			if parts[i]:
				ukbb_phe_set.add(parts[i])

if not os.path.exists("ukbb_results"):
	os.mkdir("ukbb_results")

with open(input_ukbb_manifest_file) as inf:
	for i in range(0, 26):
		next(inf)
	for line in inf:
		line = line.strip()
		parts = line.split('\t')
		parts[1] = parts[1].strip()
		parts[1] = parts[1].strip('\"')
		if parts[3] == "both_sexes" and parts[1] in ukbb_phe_set:
			out_dir = os.path.join("ukbb_results", parts[0])
			if not os.path.exists(out_dir):
				os.mkdir(out_dir)
			# wget command - download the file
			print("Downloading file : " + parts[4])
			download_command = parts[5].split()
			os.system(" ".join(download_command[0:3]) + " " + os.path.join(out_dir, download_command[3]))
	
			input_file = os.path.join(out_dir, download_command[3])
			if input_file.endswith("bgz"):
				gz_file = input_file[0:(len(input_file) -3)] + "gz"
				os.system("mv " + input_file + " " + gz_file)
				os.system("gunzip -d " + gz_file)




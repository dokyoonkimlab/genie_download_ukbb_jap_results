import sys
import os
import apsw
import csv

input_file = os.path.join("manifest_files", "Matching_phe_genie_ukbb_jap.txt") #sys.argv[1]
input_jap_manifest_file = os.path.join("manifest_files" , "jap_riken_manifest.txt")

jap_phe_set = set()
with open(input_file) as inf:
	reader = csv.reader(inf, delimiter = '\t')
	next(reader)
	for parts in reader:
		for i in range(1,3):
			parts[i] = parts[i].strip()
			if parts[i] and "chrX" not in parts[i]:
				jap_phe_set.add(parts[i])
			
if not os.path.exists("jap_results"):
	os.mkdir("jap_results")

with open(input_jap_manifest_file) as inf:
	for line in inf:
		line = line.strip()
		row = line.split('\t')
		row[1] = row[1].strip()
		row[1] = row[1].strip('\"')
		if row[1] in jap_phe_set:
			out_dir = os.path.join("jap_results", row[0])
			if row[8] == "Yes":
				out_dir = os.path.join("jap_results", "QTL_" + row[0])
			#os.system("rm -rf " + out_dir)
			if not os.path.exists(out_dir):
				os.mkdir(out_dir)

			compression = ".tar.gz"
			if row[6].strip():
				compression = ".txt.gz"

			filepath = os.path.join(out_dir, row[0] + compression)

			if row[8] == "No":
				os.system("wget http://jenger.riken.jp/" + row[0] + " -O " + os.path.join(out_dir, row[0] + compression))
			else:
				os.system("wget http://jenger.riken.jp/" + row[0] + "analysisresult_qtl_download -O " + os.path.join(out_dir, row[0] + compression))


			if compression == ".tar.gz":
				os.system("tar zxf " + filepath + " -C " + out_dir)
				gz_files = os.listdir(out_dir)
				for gz_file in gz_files:
					if gz_file.endswith("txt.gz"):
						os.system("bgzip -d " + os.path.join(out_dir, gz_file))
			else:
				os.system("bgzip -d " + filepath)




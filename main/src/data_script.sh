#SCRIPT TO AUTOMATE DATA PROCESSING FROM RAW READS TO BAGEL CALCULATIONS

#BUILDING LIBRARY INDEX
bowtie-build TKOv3_lib.fasta TKOv3_index

#MAPPING RAW READS TO LIBRARY
bowtie -v 2 -m 1 -t TKOv3_index T0.fastq T0_TKOv3.map.txt
bowtie -v 2 -m 1 -t TKOv3_index T18A.fastq T18A_TKOv3.map.txt

#GENERATING READ COUNTS MATRIX FILE FROM BOWTIE OUTPUT
python readcounts.py

#USING BAGEL

#CALCULATING FOLD CHANGE
python BAGEL.py fc -i readcounts.merged.txt -o T18A -c 1

#CALCULATING BAYES FACTORS
python BAGEL.py bf -i T18A.foldchange -o T18A.bf -e CEGv2.txt -n NEGv1.txt -c 1

#CALCULATING PRECISION RECALL
python BAGEL.py pr -i T18A.bf -o T18A.pr -e CEGv2.txt -n NEGv1.txt


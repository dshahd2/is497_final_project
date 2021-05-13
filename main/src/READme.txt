INCLUDED IN src:

data_script.sh - shell script to process raw fastq data to BAGEL calculations (fold change, bayes factors, precision recall, etc)

readcounts.py - python script to tally reads from bowtie output and generate a read count matrix

BAGEL.py - python script to use BAGEL software

VISUALIZATIONS

For visualizations, it is recommended to run the commands outside of the data_script. By doing so, you can alter the labels, titles, or add other data to the plots. For this particular pipeline, here is how to go about carrying out the visualizations. In the command line (and still in the same directory), run the following:

>python 
>import pandas as pd 
>import numpy as np 
>import matplotlib.pyplot as plt 
>from pylab import* 
>pr_data = pd.read_table('hap1-t18.pr', index_col=0) 
>pr_data.info() 
>figure(figsize(4,4)) 
>plot( pr_data.Recall, pr_data.Precision, linewidth=2) 
>xlim(0,1.01) 
>ylim(0,1.02) 
>xlabel('Recall') 
>ylabel('Precision (1-FDR)') 
>title('Precision-Recall Plot') 
>show() 

The “>” indicates a new line. This will produce the precision recall plot. 
For the ideal Bayes factors distribution, run the following:

>figure(figsize(4,4)) 
>pr_data.hist('BF', bins=50, range=(-100,100)) 
>xlabel('Bayes Factor') 
>ylabel('Number of Genes') 
>show() 

#   Import both packages
import pandas as pd
import numpy as np

#   Creating a function returnDF that takes our .map file (filename) and a column header (dataTy).
#   This function will extract the columns we need from the .map file (the location on the chromosome and the gene name (extracted from the chromosome location)).
#   It will then tally the number of times each read appears in the .map file and add that number to a separate column.
#   Finally, it will sort the output file alphabetically based on the gene.
def returnDF(filename, dataTy):
    data = pd.read_csv(filename, names=range(0,10), delimiter="\s+")
    cols = [0,1,2]
    data[10] = data[cols].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)

    print(data.head())
    print(data[4].value_counts())
    grouped = data.groupby([4]).size().reset_index(name=dataTy)
    grouped = grouped.sort_values(dataTy)

    def func(sgRNA):
        s = str(sgRNA)
        lst = s.split('_')
        return lst[1]

    grouped.sort_values(by=[4], inplace=True)
    grouped = grouped.rename(columns={4: 'CHR LOCATION'})
    grouped['GENE'] = grouped.apply (lambda sgRNA: func(sgRNA), axis=1)
    grouped.sort_values(by='GENE', inplace=True)
    grouped = grouped[['CHR LOCATION', 'GENE', dataTy]]
    grouped.set_index('GENE')
    return grouped

#   Here, we are using the function to create an output from each .map file.
T0 = returnDF("T0_TKOv3.map.txt", "T0")
T18A = returnDF("T18A_TKOv3.map.txt", "T18A")

#   Here, we are merging the outputs together.
merge_df = T0.merge(T18A, how='inner', left_on=["CHR LOCATION", "GENE"], right_on=["CHR LOCATION", "GENE"])
#   saving the output merge of both maps as readcounts.merged.txt
merge_df.to_csv("readcounts.merged.txt", sep = '\t', index=False)

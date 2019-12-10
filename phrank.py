#!/bin/python3

from phrank import Phrank
from phrank import utils as phrank_utils
#import pandas as pd
import sys
import csv

DAG="demo/data/hpodag.txt"
DISEASE_TO_PHENO="demo/data/disease_to_pheno.build127.txt"
DISEASE_TO_GENE="demo/data/gene_to_disease.build127.txt"
p_hpo = Phrank(DAG, diseaseannotationsfile=DISEASE_TO_PHENO, diseasegenefile=DISEASE_TO_GENE)

ensembl = []
with open('demo/data/ensembl_gene.tsv', 'r') as csvfile:
    ensembl_hgnc = csv.reader(csvfile ,delimiter="\t") 
    for row in ensembl_hgnc:
        ensembl.append(row[1])

while 'NA' in ensembl: ensembl.remove('NA')

with open('demo/data/ensembl_gene.tsv') as fh:
    next(fh)
    hgnc = csv.reader(fh, delimiter='\t')    
    for row in hgnc:
        hgnc_dict = {row[0]:row[1] for row in hgnc}


hpo_list = sys.argv[1]

patient_genes = set(ensembl)
patient_phenotypes = hpo_list.split(",")

print(patient_phenotypes)

gene_ranking = p_hpo.rank_genes(patient_genes, patient_phenotypes)

def get_key(val): 
    for key, value in hgnc_dict.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"

print ("\nGene ranking")
for gene_info in gene_ranking:
     print ("gene: %s\tsimilarity_score: %.2f"%(get_key(gene_info[1]),gene_info[0]))
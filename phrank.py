#!/bin/python3

from phrank import Phrank
from phrank import utils as phrank_utils
import pandas as pd
import sys

DAG="demo/data/hpodag.txt"
DISEASE_TO_PHENO="demo/data/disease_to_pheno.build127.txt"
DISEASE_TO_GENE="demo/data/gene_to_disease.build127.txt"
GENE_TO_PHENO="demo/data/gene_to_pheno.amelie.txt"
p_hpo = Phrank(DAG, diseaseannotationsfile=DISEASE_TO_PHENO, diseasegenefile=DISEASE_TO_GENE)
all_genes = pd.read_csv("demo/data/ensembl_gene.tsv", sep="\t")

id_name = sys.argv[1]
hpo_list = sys.argv[2]

patient_genes = set(all_genes.iloc[:,1].tolist())
patient_phenotypes = hpo_list.split(",")

print(id_name)
print(patient_phenotypes)

gene_ranking = p_hpo.rank_genes(patient_genes, patient_phenotypes)

d = []
for gene_info in gene_ranking:
    #print ("%s\t%.2f"%(gene_info[1],gene_info[0]))
    d.append({"gene" : gene_info[1], "phrank_score" : gene_info[0]})

data = pd.DataFrame(d)
data["Phrank"] = data["phrank_score"].rank(ascending=False, method="min") 
data["ID"] = id_name

data_hgnc = pd.merge(data,all_genes,how="left",on="gene")
data_hgnc.to_csv("results/"+id_name+"_phrank.csv", sep= "\t", header=False,index=False)
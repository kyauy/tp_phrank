#!/bin/python3

from phrank import Phrank
from phrank import utils as phrank_utils


DAG="data/hpodag.txt"
DISEASE_TO_PHENO="data/disease_to_pheno.build127.txt"
DISEASE_TO_GENE="data/gene_to_disease.build127.txt"
GENE_TO_PHENO="data/gene_to_pheno.amelie.txt"
p_hpo = Phrank(DAG, diseaseannotationsfile=DISEASE_TO_PHENO, diseasegenefile=DISEASE_TO_GENE)


# defining the phenotype sets
phenotypeset1 = ['HP:0000077','HP:0030765','HP:0012115','HP:0002088','HP:0002099','HP:0001945','HP:0000719']
phenotypeset2 = ['HP:0000975','HP:0002018','HP:0000421','HP:0012393','HP:0004406','HP:0002321']

# computing the similarity between two sets of phenotypes
matchscore = p_hpo.compute_phenotype_match(phenotypeset1, phenotypeset2)

print ("the phenotype similarity score is %.2f"%matchscore)


# defining patient genes and phenotypes
patient_genes = set(['ENSG00000000419','ENSG00000000971','ENSG00000000971','ENSG00000001626','ENSG00000001626','ENSG00000001631','ENSG00000002822','ENSG00000003137'])
patient_phenotypes = phenotypeset1

# sorting the disease by best match
disease_ranking = p_hpo.rank_diseases(patient_genes, patient_phenotypes)
print ("Disease ranking")
for disease_info in disease_ranking:
    print ("disease id: %s\tsimilarity score: %.2f"%(disease_info[1],disease_info[0]))

# sorting the genes by best match
gene_ranking = p_hpo.rank_genes(patient_genes, patient_phenotypes)
print ("\nGene ranking")
for gene_info in gene_ranking:
    print ("ensembl gene id: %s\tsimilarity score: %.2f"%(gene_info[1],gene_info[0]))


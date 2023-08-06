# MOB-suite: Software tools for clustering, reconstruction and typing of plasmids from draft assemblies

## Introduction ## 
Plasmids are mobile genetic elements (MGEs), which allow for rapid evolution and adaption of
bacteria to new niches through horizontal transmission of novel traits to different genetic
backgrounds. The MOB-suite is designed to be a modular set of tools for the typing and
reconstruction of plasmid sequences from WGS assemblies.


The MOB-suite depends on a series of databases which are too large to be hosted in git-hub. They can be downloaded or updated by running mob_init or if running any of the tools for the first time, the databases will download and initialize automatically. However, they are quite large so the first run will take a long time depending on your connection and speed of your computer.
The databases can be downloaded from figshare here: https://ndownloader.figshare.com/articles/5841882/versions/1 and https://share.corefacility.ca/index.php/s/oeufkw5HyKz0X5I/download

### MOB-init
On first run of MOB-typer or MOB-recon, MOB-init should run to download the databases from figshare, sketch the databases and setup the blast databases. However, it can be run manually if the databases need to be re-initialized.

```
% mob_init
```

### MOB-cluster
This tool creates plasmid similarity groups using fast genomic distance estimation using MASH.  Plasmids are grouped into clusters using single-linkage clustering and the cluster codes provided by the tool provide an approximation of operational taxonomic units OTU’s 

### MOB-recon
This tool reconstructs individual plasmid sequences from draft genome assemblies using the clustered plasmid reference databases provided by MOB-cluster.

### MOB-typer
Provides in silico predictions of the replicon family, relaxase type, mate-pair formation type and predicted transferability of the plasmid

### MOB-hostrange
Provides information on plasmid reproductive host range and transfer rate using both sequencing and experimental data from public databases (NCBI) and publications (PubMED). 
The predicted host range represents a range of putative hosts where a given plasmid can stably replicate and be maintained by the host. 
The host range module makes no source attribution predictions of a plasmid.

The host range and the transfer rate predictions are based on the experimental evidence reported in the surveyed literature.
Currently the host range is predicted based on two databases: NCBI Nucleotide plasmid database of 11856 records and literature curated plasmid database containing 313 records. 
The outputs are text reports and phylogenetic trees rendered in Newick and PNG image formats. This allows for easy visualization and data interpretation.


## Installation ##

## Requires
+ Python v. 3.6 +
+ ete3 >= 3
+ biopython >= 1.70
+ pytables  >= 3.3
+ pycurl >= 7.43
+ pyqt  >= 5
+ numpy >= 1.11.1
+ scipy >= 1.1

## Dependencies

+ blast+ v. 2.3.0
+ mash


## Installation
We recommend MOB-Suite installation as a conda package due to large number of dependencies. The package is available through bioconda channel.

```
% conda config --add channels defaults
% conda config --add channels conda-forge
% conda config --add channels bioconda
% conda install -c bioconda mob_suite
```



### Pip

We recommend installing MOB-Suite via bioconda but you can install it via pip using the command below

```
% pip3 install mob_suite

```

### Docker image
A docker image is also available at [https://hub.docker.com/r/kbessonov/mob_suite](https://hub.docker.com/r/kbessonov/mob_suite)
```
% docker pull kbessonov/mob_suite:2.0.0 
% docker run --rm -v $(pwd):/mnt/ "kbessonov/mob_suite:2.0.0 " mob_recon -i /mnt/assembly.fasta -t -o /mnt/mob_recon_output

```

### Singularity image
A singularity image could be built via singularity recipe donated by Eric Deveaud. 
The recipe (`recipe.singularity`) is located in the singularity folder of this repository. 
The docker image section also has instructions on how to create singularity image from a docker image.

```bash
% singularity build mobsuite.simg recipe.singularity
```

## Using MOB-typer to perform replicon and relaxase typing of complete plasmids and to predict mobility

### Setuptools
Clone this repository and install via setuptools. 

```
% git clone https://github.com/phac-nml/mob-suite.git
% cd mob-suite
% python setup.py install
```

## Using MOB-typer to perform replicon and relaxase typing of complete plasmids and predict mobility

You can perform plasmid typing using a fasta formated file containing a single plasmid represented by one or more contigs. Do not include multiple unrelated plasmids in the file as they will be treated as a single plasmid.


```
# Basic Mode
% mob_typer --infile assembly.fasta --outdir my_out_dir

# Look for a file called mobtyper_(input_file)_report.txt
% cat my_out_dir/mobtyper_(input_file)_report.txt
```

## Using MOB-recon to reconstruct plasmids from draft assemblies
This procedure works with draft or complete genomes and is agnostic of assembler choice but if
unicycler is used, then the circularity information can be parsed directly from the header of the unmodified assembly.

```
### Basic Mode
% mob_recon --infile assembly.fasta --outdir my_out_dir
```

```
### Full Mode
# In this mode, MOB-typer will be run on each identified plasmid grouping and will produce a summary report
% mob_recon --infile assembly.fasta --outdir my_out_dir --run_typer
```

## Using MOB-cluster
Use this tool only to update the plasmid databases or build a new one and should only be completed with closed high quality plasmids. If you add in poor quality data it will severely impact MOB-recon

```
### Build a new database
% mob_cluster --mode build --infile plasmid.fasta --outdir output_directory
```

```
### Add a sequence to an existing database
% mob_cluster --infile update_sequences.fasta --ref_fasta_file original.fasta --ref_mash_db original.msh --ref_cluster_file original_clusters.txt 
```

```
### Test new plasmid database with MOB-recon
% makeblastdb -in path_to_plasmid_testing_db -dbtype nucl
% mash sketch -i path_to_plasmid_testing_db   <---- produces mash sketch file with format "path_to_plasmid_testing_db.msh"
% mob_recon --infile assembly.fasta --outdir my_out_dir --run_typer --plasmid_mash_db path_to_mash_testing_db --plasmid_db path_to_plasmid_testing_db
```


```
### Update MOB-suite plasmid databases
% mv new_mob_formated_db.fasta mob_db_path/ncbi_plasmid_full_seqs.fas
% makeblastdb -in mob_db_path/ncbi_plasmid_full_seqs.fas -dbtype nucl
% mash sketch -i mob_db_path/ncbi_plasmid_full_seqs.fas 
```




# Output files
| file | Description |
| ------------ | ------------ |
| contig_report.txt | This file describes the assignment of the contig to chromosome or a particular plasmid grouping |
| repetitive_blast_report | Summary information of contigs found to consist of nothing but a repetitive element |
| chromosome.fasta | Fasta file of all contigs found to belong to the chromosome |
| plasmid_(X).fasta | Each plasmid group is written to an individual fasta file which contains the assigned contigs |
| mobtyper_(input_file)_report.txt | Individual MOB-typer report files for each identified plasmid |
| mobtyper_aggregate_report.txt | Aggregate MOB-typer report files for all identified plasmid |

# MOB-recon contig report format
| field id | description |
| -------- | ------------|
| file_id | Name of the input file  |
| cluster_id | MOB-cluster type of reference match |
| contig_id | Unique identifier of the contig |
| contig_length | Length of the contig |
| circularity_status | Circular if Circlator or Unicycler find it to be circular, and incomplete if not |
| rep_type | Replicon types idenfied |
| rep_type_accession | Accessions of replicons identified |
| relaxase_type | Relaxase types identified |
| relaxase_type_accession | Accessions of relaxases identified |
| mash_nearest_neighbor | Mate-pair formation types identified |
| mash_neighbor_distance | Mate-pair formation type accessioons |
| repetitive_dna_id | Repetitive DNA match id |
| match_type | Repetitive element class |
| score | Blast bitscore of match |
| contig_match_start | Start of match on contig |
| contig_match_end | End of match on contig |



# MOB-typer report file format
| field name | description|
| -----------| -----------|
| file_id | Name of the input file |
| num_contigs | Number of sequences identified in the file |
| total_length | Total number of bases in all sequences |
| gc | GC% of all sequences |
| rep_type(s) | Replicon types idenfied |
| rep_type_accession(s) | Accessions of replicons identified |
| relaxase_type(s) | Relaxase types identified |
| relaxase_type_accession(s) | Accessions of relaxases identified |
| mpf_type | Mate-pair formation types identified |
| mpf_type_accession(s) | Mate-pair formation type accessioons |
| orit_type(s) | Relaxase type of oriT sequence |
| orit_accession(s) | Accession for oriT |
| PredictedMobility | Mobility prediction for the plasmid (Conjugative, Mobilizable, Non-mobilizable) |
| mash_nearest_neighbor | Accession of closest database match |
| mash_neighbor_distance | Mash distance from query to match |
| mash_neighbor_cluster | MOB-cluster type of reference match |



# MOB-hostrange report file format

The table describes output fields found in the `mobtyper_*_report.txt`, `*_literature_report.txt` and `mobtyper_aggregate_report.txt` 
report files.

| field name    | description                           |
| --------------| --------------------------------------|
| NCBI-HR-Rank  | NCBI Nucleotide host range prediction expressed as a taxonomic rank  | 
| NCBI-HR-Name  | NCBI Nucleotide host range prediction expressed as a taxonomic scintific name                 |
|LitPredDBHRRank | Literature-based host range rank prediction (LiteratureDB) |
|LitPredDBHRRankSciName| Literature-based host range  prediction expressed as taxanomic scientific name (LiteratureDB) |
|LitRepHRRankInPubs | Literature-reported host range  expressed as taxanomic rank |
|LitRepHRNameInPubs | Literature-reported host range  expressed as taxanomic scientific name |
|LitMeanTransferRate| Literature-reported plasmid transfer mean rate |
|LitClosestRefAcc | NCBI Nucleotide literature-reported plasmid accession number closest to the query plasmid |
|LitClosestRefDonorStrain| The donor stain used in the conjugation experiment with the plasmid reported in `LitClosestRefAcc` field |
|LitClosestRefRecipientStrain| The recipient stain used in the conjugation experiment |
|LitClosestRefTransferRate|The literature-reported plasmid transfer rate of the closest literature-reported plasmid |
|LitClosestConjugTemp |The literature-reported conjugation temperature  during the plasmid transfer of the literature-reported plasmid (reported in `LitClosestRefAcc` field) |
|LitPMIDs | PubMED articles identifiers linked to the query plasmid | 
|LitPMIDsNumber | Number of PubMED articles identifiers reporting on the provided query plasmid |
|LitClosestMashDist | MASH distance between the query plasmid and the closest literature plasmid (the lower the better) | 


# blast report file format
| field name | description|
| -----------| -----------|
| qseqid | query sequence id |
| sseqid | subject sequence id |
| qlen | query length |
| slen | subject length |
| qstart | match start query |
| qend | match end query |
| sstart | match subject start|
| send | match subject end|
| length | length of alignment|
| mismatch | number of mismatches|
| pident | identity|
| qcovhsp | query coverage by hsp|
| qcovs | query coverage by subject|
| sstrand | strad of hit in subject|
| evalue | evalue of match|
| bitscore | bitscore of match |



## Contact

James Robertson - james.robertson@canada.ca
Kyrylo Bessonov - kyrylo.bessonov@canada.ca

## License

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this work except in
compliance with the License. You may obtain a copy of the License at:

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
implied. See the License for the specific language governing permissions and limitations under the
License.

# phylogenetic-tree
An implementation of creating phylogenetic tree structures from nucleotide strings

About: 

The script "jukesCantor.py" reads in a FASTA format file of nucleotide strings in 'ACTG' acid format only.  It will generate a genetic distance matrix for all entities in the FASTA file, creating the output as [file_name.fasta].dist and [file_name.fasta].names.

The dist file is a ssv of distance values and simple tags for the actual organism names, with a mapping of the names to id's in the names file.

The agglomeritiveCluster.py takes the dist file and performs clustering to create iterative joining on close distance clusters, which can be used to create a Newick format reprensentation of the data.

HOWTO:

python3 jukesCantor.py [fasta file]

python3 agglomeritiveCluster.py [fasta file].dist

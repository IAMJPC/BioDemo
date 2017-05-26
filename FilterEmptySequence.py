from Bio import SeqIO

# Name of the input file
fh = open('out22.fas')
# Name of the output file
newfh = open('out22-GOOD.fas', 'w')


def retseq(seqfh):
    """ Parse a fasta file and store non empty records
        into the fullseqs list. 
    """
    # Empty list to store good sequences
    fullseqs = []
    for record in SeqIO.parse(seqfh, 'fasta'):
        if len(record.seq) != 0:
            fullseqs.append(record)
    seqfh.close()
    return fullseqs


SeqIO.write(retseq(fh), newfh, 'fasta')
newfh.close()
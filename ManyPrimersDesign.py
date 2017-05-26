import glob

from Bio import SeqIO

fout = open('/home/sb/bioinfo/mfdir/forprimer3.txt', 'w')
for x in glob.glob('/home/sb/bioinfo/mfdir/*.fasta'):
    # Read both records in each fasta file.
    seq1 = SeqIO.parse(open(x), "fasta").next()
    seq2 = SeqIO.parse(open(x), "fasta").next()
    # Get the title of each fasta record.
    seq1title = seq1.description
    seq2title = seq2.description
    # Get the sequence. In seq2, get the reverse complement.
    seq1 = str(seq1.seq)  # or str(seq1.seq)
    seq2 = str(seq2.seq.reverse_complement())
    # Generate a dummy sequence title in the form:
    # "title1--title2".
    totaltitle = seq1title + '--' + seq2title
    # Generate the dummy sequence.
    totalseq = seq1 + seq2
    fout.write(
        '''PRIMER_SEQUENCE_ID=%s
    SEQUENCE=%s
    TARGET=%s,2
    PRIMER_OPT_SIZE=18
    PRIMER_MIN_SIZE=15
    PRIMER_MAX_SIZE=20
    PRIMER_NUM_NS_ACCEPTED=0
    PRIMER_EXPLAIN_FLAG=1
    PRIMER_PRODUCT_SIZE_RANGE=30-5000
    =
    ''' % (totaltitle, totalseq, len(seq1)))
# Write the primer3 input file.
fout.close()
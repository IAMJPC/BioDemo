import random

from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio import SeqIO


def new_rnd_seq(sl):
    """ Generate a random DNA sequence with a sequence length
        of "sl" (int).
    """
    s = ''
    for x in range(sl):
        s += random.choice('ATCG')
        # s += random.sample('ATCG',1)[0] is not so fast.
    return s


newfh = open('randomseqs.txt', 'w')
for i in range(1, 501):
    # Creates a random number in the range of 4000-15000
    rsl = random.randint(4000, 15000)
    # Generate the random sequence
    rawseq = new_rnd_seq(rsl)
    # Generate a correlative name
    seqname = 'Sequence_number_' + str(i)
    rec = SeqRecord(Seq(rawseq), id=seqname, description='')
    SeqIO.write([rec], newfh, 'fasta')
newfh.close()
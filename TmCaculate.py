from Bio.SeqUtils import MeltingTemp


primerFile = 'primerlist.txt'
for line in open(primerFile, 'rU'):
    # prm stores the primer, without EOL character.
    prm = line.replace('\n', '')
    # %2.2f is used to print up to two integers, the
    # decimal separator and two decimal numbers.
    print '%s,%2.2f' % (prm, MeltingTemp.Tm_staluc(prm))

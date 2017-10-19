import glob
from Bio import SeqIO
import maximal_repeats as mr

FASTA_PATTERN = "../data/proteins/familyDataset/**/*.fasta"
# FASTA_PATTERN = "../data/proteins/testGroupDataset/**/*.fasta"


def find_max_record_length():
  max_len = 0
  max_len_id = ""
  i = 0

  for filename in glob.iglob(FASTA_PATTERN):
    for seq_record in SeqIO.parse(filename, "fasta"):
      i += 1
      if len(seq_record) > max_len:
        max_len = len(seq_record)
        max_len_id = seq_record.id
      max_len = max(max_len, len(seq_record))
      if i % 1000 == 0:
        print("%d %s" % (i, str(seq_record)))
        print("max_len = %d" % max_len)
        print("max_len_id = %s" % max_len_id)

  print ("%d records parsed. Max record length: %d, id: %s." % \
      (i, max_len, max_len_id))

def find_proteins_with_singletons():
  i = 0
  proteins_with_singletons = 0
  smallest_protein_with_singletons = None
  for filename in glob.iglob(FASTA_PATTERN):
    for seq_record in SeqIO.parse(filename, "fasta"):
      i += 1
      if len(mr.get_singletons(str(seq_record.seq))) > 0:
        proteins_with_singletons += 1
        if smallest_protein_with_singletons is None or len(seq_record.seq) < len(smallest_protein_with_singletons):
          smallest_protein_with_singletons = seq_record.seq
          print(str(seq_record.seq))
          print("length: %d" % len(seq_record.seq))
        # import ipdb; ipdb.set_trace()
        # import sys; sys.exit()
      if i % 1000 == 0:
        # print("%d %s" % (i, str(seq_record)))
        print("i = %d, proteins_with_singletons = %d" % (
          i, proteins_with_singletons))

if __name__ == "__main__":
  find_max_record_length()

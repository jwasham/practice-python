from collections import Counter
import sys

try:
    num_words = int(sys.argv[1])
except ValueError:
    print("usage: most_common_words.py num_words")
    sys.exit(1)

counter = Counter(word.lower()
                  for line in sys.stdin
                  for word in line.strip().split()
                  if word)

for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")

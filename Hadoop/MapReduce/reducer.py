import sys
from collections import defaultdict
import heapq

# Initialize a dictionary to count words
word_count = defaultdict(int)

# Read input line by line
for line in sys.stdin:
    word, count = line.strip().split("\t")
    word_count[word] += int(count)

# Find the top N words (e.g., top 5)
N = 5
top_words = heapq.nlargest(N, word_count.items(), key=lambda x: x[1])

# Output the top N words
for word, count in top_words:
    print(f"{word}\t{count}")

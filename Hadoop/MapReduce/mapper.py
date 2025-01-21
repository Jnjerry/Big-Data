import sys

# Define keywords for sentiment
POSITIVE_WORDS = {"good", "great", "excellent", "amazing", "happy", "love"}
NEGATIVE_WORDS = {"bad", "terrible", "poor", "sad", "hate",dislike}

# Read input line by line
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    # Check sentiment
    positive_count = sum(1 for word in words if word.lower() in POSITIVE_WORDS)
    negative_count = sum(1 for word in words if word.lower() in NEGATIVE_WORDS)
    # Output sentiment classification
    if positive_count > negative_count:
        print(f"positive\t1")
    elif negative_count > positive_count:
        print(f"negative\t1")
    else:
        print(f"neutral\t1")

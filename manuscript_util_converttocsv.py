import csv
import re

# Load the manuscript
with open('files/draft/ProtestWisdomCondensed.txt', 'r') as f:
    text = f.read()

# Split the manuscript into paragraphs
paragraphs = re.split(r'\n{2,}', text.strip())  # split on two or more newlines

# Write the paragraphs and their numbers to a CSV file
with open('files/draft/ProtestWisdomCondensed.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Paragraph Number", "Paragraph Text"])  # write the header
    for i, paragraph in enumerate(paragraphs, start=1):
        writer.writerow([i, paragraph.strip()])  # strip leading/trailing whitespace from each paragraph

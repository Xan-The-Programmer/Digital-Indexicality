import os
import csv
from gensim.models import FastText

with open("Test Comments.csv", newline='', encoding='utf-8') as test:
    content = csv.reader(test, delimiter= ',')
    comments = [row[1] for row in content]

print(comments)

model = FastText(
    sentences=comments,
    vector_size=200,
    window=5,
    min_count=3,
    workers=8,
    sg=1,              # skip-gram preserves stylistic nuance better
    min_n=3,
    max_n=6,
    epochs=10
)

# Sanity checks
print("Vector size:", model.wv.vector_size)
print("Vocabulary size:", len(model.wv))

for comment in comments:
    vec = model.wv.get_vector(comment)
    print(f"{comment} is embedded as: {vec}")
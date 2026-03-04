import os
import csv
import Directory as d

from gensim.models import FastText

def fast_text(data = d.testcoms, debug = False):
    #this function takes in a csv and returns a list of each comment to its embeding
    with open(data, newline='', encoding='utf-8') as test:
        content = csv.reader(test, delimiter= ',')
        comments = [row[1] for row in content]

        if debug:
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

    if debug:
        # Sanity checks
        print("Vector size:", model.wv.vector_size)
        print("Vocabulary size:", len(model.wv))

    coms = []
    vectors = []

    for comment in comments:
        coms.append(comment)
        vec = model.wv.get_vector(comment)
        vectors.append(vec)

        if debug:
            print(f"{comment} is embedded as: {vec}")

    if debug:
        print(coms)
        print(vectors)

    comment_data = list(zip(coms, vectors))

    if debug:
        print(comment_data)

    return comment_data

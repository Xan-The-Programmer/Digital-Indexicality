import os
import csv

head = "C:/Users/david/OneDrive - Osceola County School District/2025-2026 School Year/AP Research Evans Xan/"
ana = head + "Analysis/"
genf = ana + "General Files/"
testcoms = genf +"Test Comments.csv"

def readto(data = testcoms, debug = False):
    with open(data, newline='', encoding='utf-8') as test:
        content = csv.reader(test, delimiter= ',')
        comments = [row[1] for row in content]

        if debug:

            print(comments)

    return comments
    

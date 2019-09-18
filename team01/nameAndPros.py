import csv

csv_file = csv.reader(open("./data/training.csv"))
header = next(csv_file)
name = header.index("name")
pros = header.index("pros")

print("name: ", name, " pros: ", pros)
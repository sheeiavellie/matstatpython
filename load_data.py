import csv

def load_sample_csv(filename):
    with open(filename, newline='') as csvfile:
        data = list(csv.reader(csvfile))
        data = [item for sublist in data for item in sublist]
        data = list(map(float, data))
    return data

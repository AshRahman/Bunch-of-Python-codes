from itertools import groupby

def read_parag(filename):
    with open(filename) as f:
        for k,g in groupby((line.strip() for line in f),bool):
            if k:
                yield list(g)

list(read_parag('myfile.txt'))

##### not yet working
            
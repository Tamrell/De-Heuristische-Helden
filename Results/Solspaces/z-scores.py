import statistics
def z_score(filename, value):
    with open(filename) as f:
        data=[int(line) for line in f]
    return (value - statistics.mean(data)) / statistics.stdev(data)

print(z_score("SS1.csv", 3486))
print(z_score("SS2.csv", 2292))
print(z_score("SS3.csv", 2069))
print("#"*90)
print(z_score("SS1.csv", 3132))
print(z_score("SS2.csv", 2252))
print(z_score("SS3.csv", 1957))

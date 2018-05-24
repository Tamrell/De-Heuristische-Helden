import csv
import tqdm
import statistics

data_1 = {"mean":0, "sigma":0}
data_2 = {"mean":0, "sigma":0}
data_3 = {"mean":0, "sigma":0}

random = [data_1, data_2, data_3]

for n in tqdm.tqdm([1, 2, 3]):
    with open("Results/Solspaces/SS" + str(n) + ".csv") as file:
        results = csv.reader(file)
        numbers = []
        for number in tqdm.tqdm(results):
            numbers.append(int(number[0]))

        print("Wijk", n)

        numbers_mean = statistics.mean(numbers)
        numbers_sigma = statistics.stdev(numbers)

        print("Mean\t", numbers_mean)
        print("Dev\t", numbers_sigma)

        random[n - 1]["mean"] = numbers_mean
        random[n - 1]["sigma"] = numbers_sigma

def z_score(value, nbh):
    grid_values = random[nbh - 1]
    return (value - grid_values["mean"]) / grid_values["sigma"]

print(z_score(3486, 1))
print(z_score(2292, 2))
print(z_score(2069, 3))

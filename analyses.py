import csv
import tqdm
import statistics
import copy

data_1 = {"mean":0, "sigma":0}
data_2 = {"mean":0, "sigma":0}
data_3 = {"mean":0, "sigma":0}

random_a = [data_1, data_2, data_3]
random_b = [copy.copy(element) for element in random_a]

for n in [1, 2, 3]:
    with open("Results/Solspaces/SS" + str(n) + ".csv") as file:
        results = csv.reader(file)
        numbers = []
        for number in results:
            numbers.append(int(number[0]))

        print("Wijk", n)

        numbers_mean = statistics.mean(numbers)
        numbers_sigma = statistics.stdev(numbers)

        print("Mean\t", numbers_mean)
        print("Dev\t", numbers_sigma)

        random_a[n - 1]["mean"] = numbers_mean
        random_a[n - 1]["sigma"] = numbers_sigma

    with open("Results/Solspaces/SSB" + str(n) + ".csv") as file:
        results = csv.reader(file)
        numbers = []
        for number in results:
            numbers.append(int(number[0]))

        print("wijk", n, "deel 2")

        numbers_mean = statistics.mean(numbers)
        numbers_sigma = statistics.stdev(numbers)

        print("Mean deel 2\t", numbers_mean)
        print("Dev deel 2\t", numbers_mean)

        random_b[n - 1]["mean"] = numbers_mean
        random_b[n - 1]["sigma"] = numbers_sigma

def z_score_a(value, nbh):
    grid_values = random_a[nbh - 1]
    return (value - grid_values["mean"]) / grid_values["sigma"]

def z_score_b(value, nbh):
    grid_values = random_b[nbh - 1]
    return (value - grid_values["mean"]) / grid_values["sigma"]

print("\nRBCHC")
print(z_score_a(3486, 1))
print(z_score_a(2292, 2))
print(z_score_a(2069, 3))

print("\nRBC")
print(z_score_a(3517, 1))
print(z_score_a(2302, 2))
print(z_score_a(2069, 3))

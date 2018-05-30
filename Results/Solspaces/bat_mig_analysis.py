import csv
import statistics
import matplotlib.pyplot as plt
for nbh in [1, 2, 3]:
    with open("K_means"+str(nbh)+".csv", "r") as f:
        table = csv.reader(f)
        best = []
        worst = []
        means = []
        devs = []
        mean_capacities = []
        for line in table:
            batteries = eval(line[0])
            values = []
            for bat in batteries:
                values.append(bat[0])
            mean_capacities.append(statistics.mean(values))
            best.append(float(line[1]))
            worst.append(float(line[2]))
            means.append(float(line[3]))
            devs.append(float(line[4]))

    plt.scatter(mean_capacities, means)
    plt.ylim(22000,40000)
    plt.savefig("scatter_K_"+str(nbh)+".png")
    plt.close()

    print("caps", mean_capacities, nbh)
    print("best",statistics.mean(best), nbh)
    print("mean",statistics.mean(means), nbh)
    print("devs",statistics.mean(devs), nbh)

#     with open("Move"+str(nbh)+".csv", "r") as f:
#         table = csv.reader(f)
#         best = []
#         worst = []
#         means = []
#         devs = []
#         mean_capacities = []
#         for line in table:
#             batteries = eval(line[0])
#             values = []
#             for bat in batteries:
#                 values.append(bat[0])
#             mean_capacities.append(statistics.mean(values))
#             #mean_capacities[-1] = sum(values)
#             best.append(float(line[1]))
#             worst.append(float(line[2]))
#             means.append(float(line[3]))
#             devs.append(float(line[4]))
#
#     plt.scatter(mean_capacities, means, c="r")
#     plt.title("Scatterplot of mean battery capacity per solution and solution score")
#     plt.xlabel("Mean battery capacity")
#     plt.ylabel("Score (mean of 200 RBC runs)")
#     plt.ylim(22000,28000)
#     plt.savefig("scatter_K_move_and_normal"+str(nbh)+".png")
#     plt.close()
#
#     q = [len([mean for mean in means if mean < 22500]), len([mean for mean in means if ((mean >= 25000) and (mean < 27500))]),
#                     len([mean for mean in means if ((mean >= 27500) and (mean < 20000))]), len([mean for mean in means if mean > 20000])]
#     plt.bar([1,2,3,4],q)
#     plt.savefig("bar_K_move"+str(nbh)+".png")
#     plt.close()
#
#
#     print("caps", mean_capacities)
#     print("best",statistics.mean(best), nbh)
#     print("mean",statistics.mean(means), nbh)
#     print("devs",statistics.mean(devs), nbh)
#     print("Length", len(mean_capacities), nbh)
#     # 200 bc
#
# def z_score(filename, value):
#     with open(filename) as f:
#         data=[int(line) for line in f]
#     return (value - statistics.mean(data)) / statistics.stdev(data)
#
# print("#"*90)
# print("Best")
# print(z_score("SSB1.csv", 24809.5))
# print(z_score("SSB2.csv", 24213.4))
# print("#"*90)
# print("Avg")
# print(z_score("SSB1.csv", 25270.2))
# print(z_score("SSB2.csv", 24726.1))
# print(z_score("SSB3.csv", 2069))
# print("#"*90)
# print(z_score("SSB1.csv", 3132))
# print(z_score("SSB2.csv", 2252))
# print(z_score("SSB3.csv", 1957))

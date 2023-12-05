import random
import copy
import matplotlib.pyplot as plt

N = 20  # Number of genes in the individual
Generations = 200  # Number of iterations
MAX = 10  # Maximum value for a gene
MIN = -10  # Minimum value for a gene

fitness_list = []  # List to store fitness for each generation

# Define the individual class
class Individual:
    def __init__(ind):
        ind.gene = [random.uniform(MIN, MAX) for _ in range(N)]
        ind.fitness = ind.test_function()

    def test_function(ind):
        utility = sum(i * ((2 * (g * g) - ind.gene[i - 1]) ** 2) for i, g in enumerate(ind.gene, start=1))
        return ((ind.gene[0] - 1) ** 2) + utility

    def mutate(ind):
        index = random.randint(0, N - 1)
        ind.gene[index] = random.uniform(MIN, MAX)
        ind.fitness = ind.test_function()

# Initialize an individual
individual = Individual()

# Hill climbing iterations
for generation in range(Generations):
    new_individual = copy.deepcopy(individual)
    new_individual.mutate()

    if new_individual.fitness < individual.fitness:
        individual = new_individual

    fitness_list.append(individual.fitness)
    print(f"Generation {generation+1}: Fitness = {individual.fitness}")

# Plotting the results
plt.plot(range(Generations), fitness_list)
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.title('Hill Climbing Optimization')
plt.grid(True)
plt.show()

import random
import copy
import matplotlib.pyplot as plt

N = 20  # Number of genes in the individual
Generations = 200  # Number of iterations
MAX = 10  # Maximum value for a gene
MIN = -5  # Minimum value for a gene

fitness_list = []  # List to store fitness for each generation

# Define the individual class
class Individual:
    def __init__(ind):
        ind.gene = [random.uniform(MIN, MAX) for _ in range(N)]
        ind.fitness = ind.test_function()

    def test_function(ind):
        answer1 = 0
        answer2 = 0
        answer3 = 0
        for i in range(N):
            answer1 += ind.gene[i] * ind.gene[i]
        for i in range(N):
            answer2 += 0.5 * (i + 1) * ind.gene[i]
        answer2 = answer2 * answer2
        for i in range(N):
            answer3 += 0.5 * (i + 1) * ind.gene[i]
        answer3 = answer3 * answer3 * answer3 * answer3
        return answer1 + answer2 + answer3

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
    print(f"Generation {generation}: Fitness = {individual.fitness}")

# Plotting the results
plt.plot(range(Generations), fitness_list)
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.title('Hill Climbing Optimization')
plt.grid(True)
plt.show()

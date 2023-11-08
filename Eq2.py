import random
import copy
import matplotlib.pyplot as plt

# User-defined parameters
P = 100  # Population size
GEN = 150  # Number of generations
MUTRATE = 0.08  # Mutation rate
MUTSTEP = 0.05  # Mutation step
T = 5  # Tournament size
CROSS_POINTS = 2  # Number of crossover points

# Rest of your constants
N = 20  # Number of genes in each individual
MAX = 10  # Maximum value for a gene
MIN = -10  # Minimum value for a gene

# Define a class 'individual' to represent each individual in the population
class individual:
    def __init__(self):
        self.gene = [0] * N  # Initialize a list of genes with all zeros
        self.fitness = 0  # Initialize fitness value to zero

# Define a function to evaluate the fitness of an individual based on its genes
def test_function(ind):
    answer1 = 0
    answer2 = 0
    answer3 = 0
    for i in range(0,N):
        answer1 = answer1 + (ind.gene[i]*ind.gene[i])
    for i in range(0,N):
        answer2 = answer2 + (0.5*i*ind.gene[i])
    answer2 = answer2*answer2
    for i in range(0,N):
        answer3 = answer3 + (0.5*i*ind.gene[i])
    answer3 = answer3*answer3*answer3*answer3
    utility = answer1 + answer2 + answer3
    return utility

# Tournament selection
def tournament_selection(population, t_size):
    best = None
    for i in range(t_size):
        ind = population[random.randint(0, len(population) - 1)]
        if best is None or ind.fitness < best.fitness:  # Assuming lower fitness is better
            best = ind
    return copy.deepcopy(best)

# Modified crossover to support multiple crossover points
def multi_point_crossover(parent1, parent2, points):
    offspring1, offspring2 = copy.deepcopy(parent1), copy.deepcopy(parent2)
    for i in range(1, points + 1):
        crosspoint = i * (N // (points + 1))
        offspring1.gene[crosspoint:], offspring2.gene[crosspoint:] = offspring2.gene[crosspoint:], offspring1.gene[crosspoint:]
    return offspring1, offspring2

# Initialize the population with random genes
population = []
for x in range(P):
    newind = individual()
    newind.gene = [random.uniform(MIN, MAX) for _ in range(N)]
    population.append(newind)

# Calculate and assign fitness to each individual in the population
for ind in population:
    ind.fitness = test_function(ind)

# Lists to store fitness statistics
average_fitness_list = []
best_fitness_list = []

# Main genetic algorithm loop
for x in range(GEN):
    new_population = []

    # Selection and crossover
    while len(new_population) < P:
        parent1 = tournament_selection(population, T)
        parent2 = tournament_selection(population, T)
        off1, off2 = multi_point_crossover(parent1, parent2, CROSS_POINTS)
        new_population.extend([off1, off2])

    # Mutation
    for ind in new_population:
        for i in range(N):
            if random.random() < MUTRATE:
                ind.gene[i] += random.uniform(-MUTSTEP, MUTSTEP)
                ind.gene[i] = min(max(ind.gene[i], MIN), MAX)

    # Fitness evaluation
    for ind in new_population:
        ind.fitness = test_function(ind)

    # Replacing the old population
    population = new_population

    # Calculate average and best fitness
    average_fitness = sum(ind.fitness for ind in population) / P
    best_individual = min(population, key=lambda ind: ind.fitness)
    average_fitness_list.append(average_fitness)
    best_fitness_list.append(best_individual.fitness)

    # Print the statistics for each generation
    print("Generation:", x)
    print("Average population fitness:", average_fitness)
    print("Best population fitness:", best_individual.fitness)
    print("\n")

# Plot the evolution of fitness over generations
plt.plot(range(GEN), average_fitness_list, label='Average Fitness')
plt.plot(range(GEN), best_fitness_list, label='Best Fitness')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.title('Evolution of Fitness over Generations')
plt.legend()
plt.show()

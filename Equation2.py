import random
import copy
import matplotlib.pyplot as plt
import math

N = 20  # Number of genes in each individual
P = 100  # Population size
MUTRATE = 0.2  # Mutation rate
Generations = 200  # Number of generations
MUTSTEP = 0.2  # Mutation step
MAX = 10  # maximum value for a gene
MIN = -5  # minimum value for a gene

average_fitness_list = []  # List to store average fitness for each generation
best_fitness_list = []  # List to store best fitness for each generation

# Define a class 'individual' to represent each individual in the population
class individual:
    def __init__(self):
        self.gene = [0] * N  # Initialize a list of genes with all zeros
        self.fitness = 0  # Initialize fitness value to zero

population = []  # Initialize an empty list to hold the population

# Initialize the population with random genes
for x in range(0, P):
    tempgene = []
    for y in range(0, N):
        tempgene.append(random.uniform(MIN, MAX))  # Generate a random binary gene
    newind = individual()
    newind.gene = tempgene.copy()  # Assign the generated gene to the individual
    population.append(newind)  # Add the individual to the population

# Define a function to evaluate the fitness of an individual based on its genes
def test_function(ind):
    answer1 = 0
    answer2 = 0
    answer3 = 0
    for i in range(0,N):
        answer1 = answer1 + (ind.gene[i]*ind.gene[i])
    for i in range(0,N):
        answer2 = answer2 + (0.5*(i+1)*ind.gene[i])
    answer2 = answer2*answer2
    for i in range(0,N):
        answer3 = answer3 + (0.5*(i+1)*ind.gene[i])
    answer3 = answer3*answer3*answer3*answer3
    utility = answer1 + answer2 + answer3
    return utility

# Calculate and assign fitness to each individual in the population
for ind in population:
    ind.fitness = test_function(ind)

# Perform evolution for a specified number of generations
for x in range(Generations):
    offspring = []  # Create an empty list to store offspring

    # Select parents for reproduction
    for i in range(0, P):
        parent1 = random.randint(0, P - 1)
        off1 = copy.deepcopy(population[parent1])  # Create a copy of parent1
        parent2 = random.randint(0, P - 1)
        off2 = copy.deepcopy(population[parent2])  # Create a copy of parent2

        # Select the worse parent based on fitness
        if off1.fitness > off2.fitness:
            offspring.append(off2)
        else:
            offspring.append(off1)

    toff1 = individual()
    toff2 = individual()
    temp = individual()

    # Perform crossover (recombination) on selected parents
    for i in range(0, P, 2):
        toff1 = copy.deepcopy(offspring[i])
        toff2 = copy.deepcopy(offspring[i + 1])
        temp = copy.deepcopy(offspring[i])
        crosspoint = random.randint(1, N)
        for j in range(crosspoint, N):
            toff1.gene[j] = toff2.gene[j]
            toff2.gene[j] = temp.gene[j]
        offspring[i] = copy.deepcopy(toff1)
        offspring[i + 1] = copy.deepcopy(toff2)

    new_offspring = []  # Create a new list to store mutated offspring

    # Apply mutation to the offspring
    for i in range(0, P):
        newind = individual()
        newind.gene = []
        for j in range(0, N):
            gene = offspring[i].gene[j]
            mutprob = random.random()
            if mutprob < MUTRATE:
                alter = random.uniform(-MUTSTEP, MUTSTEP)
                gene = gene - alter  # Adjust towards worst fitness
                if gene > MAX:
                    gene = MAX
                if gene < MIN:
                    gene = MIN
            newind.gene.append(gene)
        new_offspring.append(newind)

    # Calculate and assign fitness to the mutated offspring
    for newind in new_offspring:
        newind.fitness = test_function(newind)

    for i in range(0,P):
        if (population[i].fitness > new_offspring[i].fitness):
           population[i]  = new_offspring[i]
        # else:
        #     population = copy.deepcopy(new_offspring)  # Replace the old population with the new offspring
      
    # Calculate the average fitness of the population
    average_fitness = sum(ind.fitness for ind in population) / P

    # Find the individual with the highest fitness
    best_individual = min(population, key=lambda ind: ind.fitness)

    average_fitness_list.append(average_fitness)  # Add average fitness to the list
    best_fitness_list.append(best_individual.fitness)  # Add best fitness to the list

    print("Average population fitness:", average_fitness)
    print("Best population fitness:", best_individual.fitness)
    print("\n")

# Plot the evolution of fitness over generations
plt.plot(range(Generations), average_fitness_list, label='Average Fitness')
plt.plot(range(Generations), best_fitness_list, label='Best Fitness')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.legend()
plt.show()

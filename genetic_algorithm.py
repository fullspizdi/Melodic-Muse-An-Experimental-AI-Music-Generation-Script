# genetic_algorithm.py
# Module for genetic algorithm in the Melodic Muse AI Music Generation Script

import numpy as np
from mido import Message, MidiFile, MidiTrack
from config import GA_POPULATION_SIZE, GA_MUTATION_RATE, GA_GENERATIONS, MIDI_DEFAULT_TEMPO, MIDI_DEFAULT_VELOCITY, MIDI_DEFAULT_INSTRUMENT

def generate_initial_population(size, length):
    """
    Generate an initial population of random MIDI note sequences.

    Args:
    size (int): Number of individuals in the population.
    length (int): Length of each individual's note sequence.

    Returns:
    list of np.array: List containing the initial population of note sequences.
    """
    population = [np.random.randint(60, 72, length) for _ in range(size)]
    return population

def fitness_function(individual):
    """
    Calculate the fitness of an individual note sequence.

    Args:
    individual (np.array): The individual note sequence.

    Returns:
    float: The fitness score of the individual.
    """
    # Example fitness function: Higher diversity of notes might be considered better
    unique_notes = len(set(individual))
    return unique_notes / len(individual)

def select_parents(population, fitness_scores):
    """
    Select parents for the next generation using roulette wheel selection.

    Args:
    population (list of np.array): The current population of individuals.
    fitness_scores (list of float): The fitness scores for each individual.

    Returns:
    tuple: Two individuals selected as parents.
    """
    total_fitness = sum(fitness_scores)
    selection_probs = [score / total_fitness for score in fitness_scores]
    parents = np.random.choice(len(population), 2, p=selection_probs, replace=False)
    return population[parents[0]], population[parents[1]]

def crossover(parent1, parent2):
    """
    Perform a single-point crossover between two parents.

    Args:
    parent1 (np.array): The first parent.
    parent2 (np.array): The second parent.

    Returns:
    np.array: The generated offspring.
    """
    crossover_point = np.random.randint(1, len(parent1))
    offspring = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
    return offspring

def mutate(individual, mutation_rate):
    """
    Mutate an individual by randomly altering its notes.

    Args:
    individual (np.array): The individual to mutate.
    mutation_rate (float): The probability of each note being mutated.

    Returns:
    np.array: The mutated individual.
    """
    for i in range(len(individual)):
        if np.random.rand() < mutation_rate:
            individual[i] = np.random.randint(60, 72)
    return individual

def generate_midi_from_sequence(sequence, file_name):
    """
    Generate a MIDI file from a note sequence.

    Args:
    sequence (np.array): The note sequence.
    file_name (str): The output file name.
    """
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    track.append(Message('program_change', program=MIDI_DEFAULT_INSTRUMENT, time=0))
    delta_time = int(480 / len(sequence))  # Assuming a fixed length for simplicity

    for note in sequence:
        track.append(Message('note_on', note=note, velocity=MIDI_DEFAULT_VELOCITY, time=0))
        track.append(Message('note_off', note=note, velocity=MIDI_DEFAULT_VELOCITY, time=delta_time))

    mid.save(file_name)

def main():
    """
    Main function to run the genetic algorithm and generate music.
    """
    population = generate_initial_population(GA_POPULATION_SIZE, 16)
    for generation in range(GA_GENERATIONS):
        fitness_scores = [fitness_function(individual) for individual in population]
        new_population = []
        while len(new_population) < len(population):
            parent1, parent2 = select_parents(population, fitness_scores)
            offspring = crossover(parent1, parent2)
            offspring = mutate(offspring, GA_MUTATION_RATE)
            new_population.append(offspring)
        population = new_population
        print(f"Generation {generation + 1} complete.")

    # Select the best individual
    best_individual = max(population, key=fitness_function)
    generate_midi_from_sequence(best_individual, 'output_song.midi')
    print("MIDI file generated: 'output_song.midi'.")

if __name__ == "__main__":
    main()

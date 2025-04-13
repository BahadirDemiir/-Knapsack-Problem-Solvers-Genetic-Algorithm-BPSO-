import math
import random
import copy

class Bag:
    def __init__(self):
        self.indexes = []
        self.velocities = []
        self.fitness = 0
        self.best_indexes = []
        self.best_fitness = 0
        self.initialize()

    def initialize(self):
        for _ in range(len(InfoAboutProblem.prices)):
            velocity = InfoAboutProblem.min_velocity + random.random() * (InfoAboutProblem.max_velocity - InfoAboutProblem.min_velocity)
            self.velocities.append(velocity)
            if random.random() > self.sigmoid(velocity):
                self.indexes.append(0)
            else:
                self.indexes.append(1)
        self.calculate_fitness()
        self.best_indexes = self.indexes.copy()
        self.best_fitness = self.fitness

    def sigmoid(self, velocity):
        return 1 / (1 + math.exp(-velocity))

    def calculate_fitness(self):
        total_price = sum(self.indexes[i] * InfoAboutProblem.prices[i] for i in range(len(self.indexes)))
        total_weight = sum(self.indexes[i] * InfoAboutProblem.weights[i] for i in range(len(self.indexes)))
        if total_weight > InfoAboutProblem.max_weight:
            total_price *= -1
        self.fitness = total_price

class Helper:
    @staticmethod
    def create_population():
        my_population = [Bag() for _ in range(InfoAboutProblem.population_size)]
        return my_population

class Swarm:
    def __init__(self, population):
        self.population = population
        self.update_all_time_global_best()

    def update_all_time_global_best(self):
        max_value = max(self.population, key=lambda bag: bag.best_fitness)  # Gbest, Pbest'lerin en iyisi olarak güncellendi
        if BestBagOfAllTime.best_of_the_best_of_the_best is None or max_value.best_fitness > BestBagOfAllTime.best_of_the_best_of_the_best.best_fitness:
            BestBagOfAllTime.best_of_the_best_of_the_best = copy.deepcopy(max_value)

    def update_velocities_of_population(self):
        w = 0.689343
        c1 = 1.42694
        c2 = 1.42694
        for bag in self.population:
            for i in range(len(bag.indexes)):
                rand1 = random.random()
                rand2 = random.random()
                bag.velocities[i] = (
                    w * bag.velocities[i]
                    + c1 * rand1 * (bag.best_indexes[i] - bag.indexes[i])
                    + c2 * rand2 * (BestBagOfAllTime.best_of_the_best_of_the_best.indexes[i] - bag.indexes[i])
                )

                if bag.velocities[i] > InfoAboutProblem.max_velocity:
                    bag.velocities[i] = InfoAboutProblem.max_velocity
                if bag.velocities[i] < InfoAboutProblem.min_velocity:
                    bag.velocities[i] = InfoAboutProblem.min_velocity
            bag.calculate_fitness()

    def update_position_of_population(self):
        for bag in self.population:
            bag.calculate_fitness()
            for i in range(len(bag.indexes)):
                if random.random() > bag.sigmoid(bag.velocities[i]):
                    bag.indexes[i] = 0
                else:
                    bag.indexes[i] = 1
            bag.calculate_fitness()
            if bag.best_fitness < bag.fitness:
                bag.best_fitness = bag.fitness
                bag.best_indexes = bag.indexes.copy()

class InfoAboutProblem:
    prices = [170, 90, 50, 100, 200, 120, 350, 70, 90, 30]
    weights = [1, 0.2, 1.5, 1.3, 2, 2.3, 0.6, 2.8, 4, 3.5]
    max_weight = 7.5
    population_size = 100
    number_of_iteration = 100
    max_velocity = 4
    min_velocity = -4

class BestBagOfAllTime:
    best_of_the_best_of_the_best = None

def start(s1):
    for k in range(InfoAboutProblem.number_of_iteration):
        s1.update_all_time_global_best()
        s1.update_velocities_of_population()
        s1.update_position_of_population()
        x = 0
        print("--------{a}.POPULASYON-------:".format(a=x))
        x = x+1
        for i in my_population:
            print("canta değeri = {a}".format(a = i.fitness))
            


if __name__ == "__main__":
    helper = Helper()
    my_population = helper.create_population()
    s1 = Swarm(my_population)
    start(s1)
    
    
        
        

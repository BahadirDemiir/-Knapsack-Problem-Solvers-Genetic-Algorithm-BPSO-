# -Knapsack-Problem-Solvers-Genetic-Algorithm-BPSO-
Knapsack Problem Solvers: Genetic Algorithm & Binary PSO
This project provides two powerful Python-based metaheuristic solutions for the classic 0/1 Knapsack Problem, using:

Genetic Algorithm (GA)

Binary Particle Swarm Optimization (BPSO)

Genetic Algorithm (GA)
The GA module (GENETİC.py) simulates the natural selection process, evolving generations of "bags" (solutions) through:

Selection: Individuals with higher fitness are more likely to reproduce

Crossover: Randomly mixes features of two parent bags

Mutation: Randomly flips items in the bag for diversity

Repair: Ensures weight constraints are respected

Elitism: Retains high-performing solutions over generations

It outputs:

Iterative fitness improvements

Average fitness of the population

The best value solution per iteration

Binary PSO (BPSO)
The BPSO implementation (BPSO.py) models a swarm of particles (bags) moving through the solution space using:

Sigmoid-based Position Updates

Velocity Control with Inertia and Cognitive/Social Factors

Global Best & Personal Best Memory

Fitness Penalization for Overweight Solutions

It emphasizes:

High-speed convergence

Strong global exploration

Fitness tracking of individuals and global best

Problem Setup
Items: 10 real-world items (e.g., phone, ring, laptop, toaster, etc.)

Constraints: Max weight limit = 7.5

Goal: Maximize total value without exceeding the weight limit

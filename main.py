import random
import math

def sphere_function(x):
    return sum(xi ** 2 for xi in x)

def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    dim = len(bounds)
    current_solution = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current_solution)
    
    for _ in range(iterations):
        new_solution = [current_solution[i] + random.uniform(-0.1, 0.1) for i in range(dim)]
        new_solution = [max(min(new_solution[i], bounds[i][1]), bounds[i][0]) for i in range(dim)]
        new_value = func(new_solution)
        
        if new_value < current_value:
            current_solution, current_value = new_solution, new_value
        
        if abs(new_value - current_value) < epsilon:
            break
    
    return current_solution, current_value

def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    dim = len(bounds)
    best_solution = [random.uniform(b[0], b[1]) for b in bounds]
    best_value = func(best_solution)
    
    for _ in range(iterations):
        candidate_solution = [random.uniform(b[0], b[1]) for b in bounds]
        candidate_value = func(candidate_solution)
        
        if candidate_value < best_value:
            best_solution, best_value = candidate_solution, candidate_value
        
        if best_value < epsilon:
            break
    
    return best_solution, best_value

def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    dim = len(bounds)
    current_solution = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current_solution)
    
    for _ in range(iterations):
        new_solution = [current_solution[i] + random.uniform(-0.5, 0.5) for i in range(dim)]
        new_solution = [max(min(new_solution[i], bounds[i][1]), bounds[i][0]) for i in range(dim)]
        new_value = func(new_solution)
        
        if new_value < current_value or random.random() < math.exp((current_value - new_value) / temp):
            current_solution, current_value = new_solution, new_value
        
        temp *= cooling_rate
        
        if temp < epsilon:
            break
    
    return current_solution, current_value

if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]

    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)

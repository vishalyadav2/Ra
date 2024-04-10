import random


def objective_function(x):
    
    return -(x ** 2) + 2 * x + 1


def hill_climbing(max_iter, step_size, min_val, max_val):
    
    current_solution = random.uniform(min_val, max_val)
    current_value = objective_function(current_solution)

   
    for _ in range(max_iter):
       
        new_solution = current_solution + random.uniform(-step_size, step_size)
        new_solution = max(min_val, min(max_val, new_solution)) 

       
        new_value = objective_function(new_solution)

        
        if new_value > current_value:
            current_solution = new_solution
            current_value = new_value

    return current_solution, current_value


def main():
    max_iter = 1000  
    step_size = 0.1  
    min_val = -10    
    max_val = 10     

   
    best_solution, best_value = hill_climbing(max_iter, step_size, min_val, max_val)

   
    print("Best solution:", best_solution)
    print("Best value:", best_value)

if __name__ == "__main__":
    main()

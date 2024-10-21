""" from 'Tech with Tim' video https://www.youtube.com/watch?v=21FnnGKSRZo """

import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 2
MAX_OPERAND = 9
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press enter to start!")
print("--------------------")

start_time =  time.time()

for i in range( TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problen #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = end_time - start_time

print("--------------------")
print("Nice work! You finished in", total_time, "seconds!")

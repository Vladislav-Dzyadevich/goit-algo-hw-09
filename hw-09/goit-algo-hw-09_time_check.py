import time
from goit_algo_hw_09 import find_coins_greedy, find_min_coins

amount = 113

start_time = time.time()
greedy_result = find_coins_greedy(amount)
greedy_time = time.time() - start_time

start_time = time.time()
min_coins_result = find_min_coins(amount)
min_coins_time = time.time() - start_time

print("Greedy Algorithm Result:", greedy_result)
print("Greedy Algorithm Time:", greedy_time)

print("Dynamic Programming Result:", min_coins_result)
print("Dynamic Programming Time:", min_coins_time)
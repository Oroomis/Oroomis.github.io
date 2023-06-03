import pygal as pg
import numpy as np
import timeit

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
fact_list = [factorial(i) for i in range(11)]
    
bar_chart = pg.Bar()
bar_chart = pg.Bar(height=400)
bar_chart.add('Factorial', fact_list)

print("Saving the chart...")
start = timeit.default_timer()
bar_chart.render_to_file('bar_chart.svg') 
print("Done in", round(timeit.default_timer() - start, 2), "seconds")
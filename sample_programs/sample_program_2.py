import numpy as np
import pandas as pd

def simple_program(w, x, y=6, z=10):
    a = w + x + y + z
    print("a:", a)
    return a

print("begin program")
x = -5
result = simple_program(2, x, y=8)
print("the result:", result)
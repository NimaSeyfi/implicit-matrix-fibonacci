import matplotlib.pyplot as plt
import time
from implicit_matrix_memoized import digits_sequence


x = []
y = []
step = 1000
i = 0
limit = 1500000000
while i < limit:
    x.append(i)
    start = time.perf_counter()
    digits_sequence(i)
    y.append(time.perf_counter() - start)
    i += step
    if i >= 10000000:
        step *= 4
    if i >= 100000000:
        step *= 4


# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('n')
# naming the y axis
plt.ylabel('time (s)')

# giving a title to my graph
plt.title('Implicit Matrix Fibonacci (Memoized)!')

# function to show the plot
plt.show()
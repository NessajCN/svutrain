import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":
    x = np.arange(0,100) 
    y = 3 * (x**3) + 5 *x + 1
    plt.xlabel("x axis caption") 
    plt.ylabel("y axis caption") 
    plt.plot(x,y)
    plt.savefig("output/plot.png")

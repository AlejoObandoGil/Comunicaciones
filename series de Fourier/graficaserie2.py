import numpy as np
import matplotlib.pyplot as plt

def f(n):
    return np.sin(n * np.pi / 2)/(n * np.pi / 2)

def main():
    index=[]
    vals=[]
    iteraciones=11
    for i in range(-iteraciones+1, iteraciones, 1):
        print(i)
        index.append(i)
        if (i == 0):
            vals.append(2)
        else:
            vals.append(f(i))
    print(vals)
    plt.figure(figsize=(10,5))
    plt.axis([-iteraciones-1, iteraciones+1, -0.5, 2.5])
    plt.grid(True)
    plt.stem(index, vals)
    plt.show()

if __name__ == "__main__":
    main()
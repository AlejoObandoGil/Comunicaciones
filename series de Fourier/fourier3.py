from sympy import *
from sympy.abc import t, n

def main():
    a0 = integrate(2 / pi, (t, -pi / 2, pi / 2))
    print("a0 = ")
    pprint(a0)

    an = integrate((2 / pi) * cos(n * t), (t, -pi / 2, pi / 2))
    print("an = ")
    pprint(an)

    bn = together(integrate((2 / pi) * sin(n * t), (t, -pi / 2, pi / 2)))
    print("bn = ")
    pprint(bn)

    print("f(x) = ")
    armonicos = 10
    serie = (a0/2) + 1
    for i in range(1, armonicos + 1):
        serie = serie + (an * cos(n*(t - pi/4))).subs(n, i)
    for j in range(1, armonicos + 1):
        serie = serie + (bn * sin(n*(t - pi/4))).subs(n, j)
    pprint(serie)

    plotting.plot(serie, ylim=(-3, 5), xlim=(-10, 10))

    

if __name__ == "__main__":
    main()
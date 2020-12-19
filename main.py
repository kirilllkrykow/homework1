def my_f():
    import matplotlib.pyplot as plt
    import numpy as np
    from random import randint
    k=1
    x = np.linspace(0,10,20)
    plt.plot(x,np.cos(k*x))
    print(x)
    k= randint(1,10)
    plt.plot(x, np.cos(k * x))
    return x
print(my_f())
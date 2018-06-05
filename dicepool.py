import numpy as np
import matplotlib.pyplot as plt

def dpool(n, again=10, extra=0, rote=False):
    """
    dicepool, -1 encodes fatal failure
    """
    a = 0
    if n < 1:
        r = np.random.rand()
        if r < 0.1:
            a = -1
        elif r > 0.9:
            a = 1
        elif rote:
            a = dpool(1, again=again)
            
    else:
        for i in range(0, n):
            r = np.random.rand()
            if r < 0.1*(11-again):
                a = a + 1 + dpool(1, again=again)
            elif r < 0.3:
                a = a + 1
            elif rote:
                a = a + dpool(1, again=again)
                
    
    if a > 0:
        a = a + extra        
        
    return a
       
if __name__ == "__main__":
 
    print(dpool(10))
    local_a = []
    for i in range(0,10000):
        local_a.append(dpool(1, again=8, extra=2, rote=True))
 
    #print(local_a)
    
    # the histogram of the data
    n, bins, patches = plt.hist(local_a, bins=range(-1,15), density=True, facecolor='g', align='mid')

    #plt.xlabel('Smarts')
    #plt.ylabel('Probability')
    #plt.title('Histogram of IQ')
    #plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    #plt.axis([40, 160, 0, 0.03])
    plt.grid(True)
    plt.show()
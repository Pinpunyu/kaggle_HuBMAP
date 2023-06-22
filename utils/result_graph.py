import matplotlib.pyplot as plt
import numpy as np

def loss_fig(train , name):
    
    plt.plot([*range(1,len(train)+1)] , train , label = "loss")
    plt.xticks(np.arange(0, len(train)+1, 5))
    plt.legend(loc="upper right")

    plt.savefig(f'{name}.png')
    plt.show()

def acc_fig(bbox , segm , name):
    
    plt.plot([*range(1,len(bbox)+1)] ,bbox , label = "bbox")
    plt.plot([*range(1,len(segm)+1)] ,segm , label = "segm")
    plt.xticks(np.arange(0, len(bbox)+1, 5))
    plt.legend(loc="upper left")

    plt.savefig(f'{name}.png')
    plt.show()
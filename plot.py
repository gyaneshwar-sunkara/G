import numpy as np
import matplotlib.pyplot as plt

def samples(images, labels=None, shape=[1, 1], cmap="gray", ticks=False, figsize=None):
    n = np.prod(shape)
    x = shape[0]
    y = shape[1]

    plt.figure(figsize=figsize)
    for i in range(n):
        plt.subplot(x, y, i+1)
        if not ticks:
            plt.xticks([])
            plt.yticks([])
        plt.grid(False)
        plt.imshow(images[i], cmap=cmap)
        if labels is not None:
            plt.xlabel(labels[i])
    
    plt.tight_layout()
    return plt

def metrics(metric, metric2=None, label='loss'):
    epochs = range(1, len(metric)+1)
    plt.plot(epochs, metric, label='Training ' + label)
    plt.title('Training ' + label)
    if metric2 is not None:
        plt.title('Training & validation ' + label)
        plt.plot(epochs, metric2, label='Validation ' + label)
    plt.xlabel('Epochs')
    plt.ylabel(label)
    plt.legend()
    return plt



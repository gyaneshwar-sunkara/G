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

def evaluate(*args, labels):
    n = len(args)
    
    for i in range(n):
        metric = args[i]
        label = labels[i]
        metric_label = label[0].split(" ")[-1]
        epochs = range(1, len(metric[0]) + 1)

        plt.subplot(1, n, i+1)
        plt.plot(epochs, metric[0], label=label[0])
        plt.plot(epochs, metric[1], label=label[1])
        plt.title(' & '.join(label))
        plt.xlabel('Epochs')
        plt.ylabel(metric_label)
        plt.legend()
        
    return plt
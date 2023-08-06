import queue

import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

from ctarn.cluster import Dend


def draw_labels(labels, pos, size=4, path=None):
    labels = np.array(labels)
    pos = np.array(pos)
    fig = plt.figure()
    plt.axis('off')
    sets = [(pos[labels == label, 0], pos[labels == label, 1]) for label in np.unique(labels)]
    sets.sort(key=lambda s: np.mean(s))
    for x, y in sets:
        plt.scatter(x, y, s=size)
    if path is not None:
        plt.savefig(path)
    return fig


def draw_dendrogram(dend, pos, size=4, duration=1000, path=None):
    pos = np.array(pos)
    frames = []
    fig = plt.figure()
    plt.axis('off')
    fifo = queue.Queue()
    fifo.put(dend)
    while not fifo.empty():
        dend = fifo.get()
        for child in dend:
            items = child.items
            plt.scatter(pos[items, 0], pos[items, 1], s=size)
            if type(child) is Dend:
                fifo.put(child)
        fig.canvas.draw()
        frames.append(Image.frombytes('RGB', fig.canvas.get_width_height(), fig.canvas.tostring_rgb()))
    if path is not None:
        frames[0].save(path, save_all=True, append_images=frames, duration=duration)
    return frames

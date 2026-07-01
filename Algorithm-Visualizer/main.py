# Simple algorithm animation tool I wrote to learn sorting & graph algorithms
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Bubble sort animation
def bubble_sort_anim(arr):
    n = len(arr)
    frames = []
    temp_arr = arr.copy()
    for i in range(n):
        for j in range(n - i - 1):
            if temp_arr[j] > temp_arr[j+1]:
                temp_arr[j], temp_arr[j+1] = temp_arr[j+1], temp_arr[j]
            frames.append(temp_arr.copy())
    return frames

# Dijkstra path finding for simple graph
def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    visited = []
    current = start
    while len(visited) < len(graph):
        visited.append(current)
        for neighbor, weight in graph[current].items():
            if dist[neighbor] > dist[current] + weight:
                dist[neighbor] = dist[current] + weight
        # find next min unvisited node
        min_dist = float('inf')
        next_node = None
        for node in dist:
            if node not in visited and dist[node] < min_dist:
                min_dist = dist[node]
                next_node = node
        current = next_node
    return dist

# run bubble sort demo
if __name__ == "__main__":
    test_data = random.sample(range(1, 30), 12)
    anim_frames = bubble_sort_anim(test_data)

    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(test_data)), test_data)

    def update_frame(frame):
        for rect, val in zip(bar_rects, frame):
            rect.set_height(val)
        return bar_rects

    ani = animation.FuncAnimation(fig, update_frame, frames=anim_frames, interval=150)
    plt.show()

    # test graph example
    sample_graph = {
        'A': {'B': 2, 'C': 5},
        'B': {'A': 2, 'D': 1},
        'C': {'A': 5, 'D': 3},
        'D': {'B': 1, 'C': 3}
    }
    res = dijkstra(sample_graph, 'A')
    print("Shortest distance from A:", res)
import re
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
from itertools import combinations

def load_box_positions_from_input(file):
    box_positions = []
    with open(file) as f:
        for line in f.readlines():
            match_xyz = re.match(r'(\d+),(\d+),(\d+)', line)
            x, y, z = match_xyz.groups()
            box_positions.append((int(x), int(y), int(z)))
    return box_positions

def init_graph(positions):
    G = nx.Graph()
    for pos in positions:
        x, y, z = pos
        G.add_node((x, y, z))
    return G
    
def draw(graph):
    plt.figure(figsize=(10, 10))
    nx.draw(
        graph,
        with_labels=True,
        font_size=6,
        node_size=500,
        
    )
    plt.show()

def draw_3d(graph):
    fig = plt.figure(figsize=(10, 10))  # large 3D window
    ax = fig.add_subplot(111, projection='3d')

    xs = [n[0] for n in graph.nodes()]
    ys = [n[1] for n in graph.nodes()]
    zs = [n[2] for n in graph.nodes()]
    ax.scatter(xs, ys, zs)
    
    # draw edges as line segments
    for u, v in graph.edges():
        x_vals = [u[0], v[0]]
        y_vals = [u[1], v[1]]
        z_vals = [u[2], v[2]]
        ax.plot(x_vals, y_vals, z_vals)

    # label each point
    # for x, y, z in graph.nodes():
    #     ax.text(x, y, z, f'({x},{y},{z})', fontsize=8)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

def distance(a, b):
    x1, y1, z1 = a
    x2, y2, z2 = b
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def find_pairwise_distances(positions):
    distances = {}
    for pos1, pos2 in combinations(positions, 2):
        key = frozenset((pos1, pos2))
        distances[key] = math.dist(pos1, pos2)
    sorted_distances = dict(sorted(distances.items(), key=lambda x: x[1]))
    return sorted_distances

def print_distances(distances):
    for key, dist in distances.items():
        print(f'key: {key}, D={dist}')

def solve_part1(input):
    print('Solving Part 1...\n')
    box_positions = load_box_positions_from_input(input)
    # print(f'Box positions: \n{box_positions}')
    G = init_graph(box_positions)
    
    distances = find_pairwise_distances(box_positions)
    # print_distances(distances)

    distances_to_check = 1000
    for k, d in distances.items():
        if distances_to_check == 0:
            break
        distances_to_check -= 1
        posA, posB = k
        if nx.has_path(G, posA, posB):
            continue
        else:
            G.add_edge((posA), (posB), weight=round(d, 2))

    components = list(nx.connected_components(G))
    components_sorted = sorted(components, key=len, reverse=True)

    largest_three = [len(component) for component in components_sorted[:3]]

    solution = 1
    for box_count in largest_three:
        solution *= box_count

    print(f'Edge count: {G.number_of_edges()}')
    print(f'Components: {len(components)}')
    print(f'largest 3 len: {largest_three}')
    print(f'Solution p1: {solution}')
    # draw(G)
    draw_3d(G)

    return solution

def print_distances(distances):
    for key, dist in distances.items():
        print(f'key: {key}, D={dist}')

def solve_part2(input):
    print('Solving Part 2...\n')
    box_positions = load_box_positions_from_input(input)
    G = init_graph(box_positions)
    
    distances = find_pairwise_distances(box_positions)

    box_count = G.number_of_nodes()
    for k, d in distances.items():
        posA, posB = k

        if nx.has_path(G, posA, posB):
            continue

        G.add_edge((posA), (posB), weight=round(d, 2))

        if G.number_of_edges() == box_count - 1:
            last_connection_pair = (posA, posB)
            break

    solution = last_connection_pair[0][0] * last_connection_pair[1][0]

    print(f'Solution p2: {solution}')
    draw_3d(G)

    return solution

def main():
    print('Solving Advent of Code day 8...\n')
    solve_part1('./day8/input.txt')
    solve_part2('./day8/input.txt')


if __name__ == "__main__":
    main()
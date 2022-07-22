def find_shortest_path(n_intersection, shortcuts):
    path_length = [i for i in range(n_intersection)]
    #next_intersection = i for i in range(n_intersection)]
    optimal = False
    while not optimal:
        optimal = True
        for intersection_to in range(n_intersection):
            for intersection_from in range(n_intersection):
                length = abs(intersection_from - intersection_to)
                if shortcuts[intersection_from] == intersection_to:
                    length = 1
                if path_length[intersection_to] > path_length[intersection_from] + length:
                    optimal = False
                    path_length[intersection_to] = path_length[intersection_from] + length
    return path_length

if __name__ == "__main__":
    n_intersection = int(input())
    shortcuts = [int(i) - 1 for i in input().split(" ")]
    shortest_paths = [str(i) for i in find_shortest_path(n_intersection, shortcuts)]
    print(" ".join(shortest_paths))

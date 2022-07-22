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

def find_shortest_path_shortcut_first(n_intersection, shortcuts):
    path_length = [i for i in range(n_intersection)]
    optimal = False
    modified_paths = set([i for i in range(n_intersection)])
    while not optimal:
        optimal = True
        shortcut_modified_paths = set()
        standard_modified_path = set()
        for modified_path in modified_paths:
            if path_length[modified_path] + 1 < path_length[shortcuts[modified_path]]:
                optimal = False
                path_length[shortcuts[modified_path]] = path_length[modified_path] + 1
                shortcut_modified_paths.add(shortcuts[modified_path])
        for intersection_from in shortcut_modified_paths:
            for intersection_to in range(intersection_from - 1, 0, -1):
                length = abs(intersection_to - intersection_from)
                if path_length[intersection_to] > path_length[intersection_from] + length:
                    optimal = False
                    path_length[intersection_to] = path_length[intersection_from] + length
                    standard_modified_path.add(intersection_to)
                else:
                    break
            for intersection_to in range(intersection_from +1, n_intersection):
                length = abs(intersection_to - intersection_from)
                if path_length[intersection_to] > path_length[intersection_from] + length:
                    optimal = False
                    path_length[intersection_to] = path_length[intersection_from] + length
                    standard_modified_path.add(intersection_to)
                else:
                    break
        modified_paths = standard_modified_path | shortcut_modified_paths
    return path_length

if __name__ == "__main__":
    n_intersection = int(input())
    shortcuts = [int(i) - 1 for i in input().split(" ")]
    shortest_paths = [str(i) for i in find_shortest_path_shortcut_first(n_intersection, shortcuts)]
    print(" ".join(shortest_paths))

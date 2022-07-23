# MikeShortcut
This is a solution to [this code forces problem](https://codeforces.com/problemset/problem/689/B)
## How does it work?

We consider a simplified graph of intersections were we remove edges from intersection i to j if |i - j| is not 1, or using a shorcut. We can do this since we don't care about the number of steps but only the path length, and you can always go through i+1, i+2, ..., j to get a path of the same length. This has two main benefits:
- It makes the graph sparse. We now only have only 3 intersection to check for each intersection instead of n
- It makes each edges have the same weight. This means that if we handle them from the closest intersection to the furthest, we're garanted that the first path to a point is the shortest, removing useless comparisons

## Complexity
The algorithm's complexity is O(n)

In the worst case, n loop iterations are performed. It occurs all shortcuts lead to beginning (or any place closest to home)

In the best case, n/3 loop iteration are performed. It occurs if there is a spanning tree that has 1 as root, is ternary (except for the root) has minimal height, because this means that for each iteration we find the shortest path for 3 intersections
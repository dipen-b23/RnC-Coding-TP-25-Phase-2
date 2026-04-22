#include <stdio.h>

#define V 5

void addEdge(int adj[V][V], int u, int v) {
    adj[u][v] = 1;
    adj[v][u] = 1;   // remove this line if directed
}

void DFS(int adj[V][V], int visited[], int curr) {
    visited[curr] = 1;
    printf("%d ", curr);

    for (int i = 0; i < V; i++) {
        if (adj[curr][i] == 1 && visited[i] == 0) {
            DFS(adj, visited, i);
        }
    }
}

int main() {
    int adj[V][V] = {0};
    int visited[V] = {0};

    addEdge(adj, 0, 1);
    addEdge(adj, 0, 2);
    addEdge(adj, 1, 3);
    addEdge(adj, 2, 4);

    printf("DFS Traversal: ");
    DFS(adj, visited, 0);

    return 0;
}

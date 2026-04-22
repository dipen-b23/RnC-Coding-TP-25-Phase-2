#include <stdio.h>

#define V 5

void addEdge(int adj[V][V], int u, int v) {
    adj[u][v] = 1;
    adj[v][u] = 1;   
}

void BFS(int adj[V][V], int start) {
    int visited[V] = {0};
    int queue[V];
    int front = 0, rear = 0;

    visited[start] = 1;
    queue[rear++] = start;

    while (front < rear) {
        int curr = queue[front++];
        printf("%d ", curr);

        for (int i = 0; i < V; i++) {
            if (adj[curr][i] == 1 && visited[i] == 0) {
                visited[i] = 1;
                queue[rear++] = i;
            }
        }
    }
}

int main() {
    int adj[V][V] = {0};

    addEdge(adj, 0, 1);
    addEdge(adj, 0, 2);
    addEdge(adj, 1, 3);
    addEdge(adj, 2, 4);

    printf("BFS Traversal: ");
    BFS(adj, 0);

    return 0;
}
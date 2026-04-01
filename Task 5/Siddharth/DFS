
def dfs(graph, vertex, visited):
   
    visited.add(vertex)
    print(vertex, end=" ")

   
    for neighbor in graph[vertex]:
      
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

if __name__ == "__main__":
    
    graph = {
        0: [1, 2],      
        1: [2, 3],       
        2: [3],          
        3: [4],          
        4: [0, 1, 5],   
        5: []           
    }

    print("DFS Traversal starting from node 0:")
  
    visited_nodes = set()
    dfs(graph, 0, visited_nodes)

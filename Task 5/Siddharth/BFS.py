
import collections

def bfs(graph, root):
 
    visited = set([root])
  
    queue = collections.deque([root])
    
    print(f"BFS Traversal starting from node {root}:")
    
    while queue:
       
        vertex = queue.popleft()
        print(vertex, end=" ")
        
      
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

if __name__ == "__main__":
  
    graph = {
        0: [1, 2],       
        1: [2, 3],       
        2: [3],         
        3: [4],          
        4: [0, 1, 5],    
        5: []            
    }

    bfs(graph, 0)

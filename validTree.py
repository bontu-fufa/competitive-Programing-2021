
# DFS
class Solution:
    def dfs_check(self, node, parent, graph, visited):
        
        visited.add(node)
        
        for n in graph[node]: 
            if n not in visited: 
                if not self.dfs_check(n , node , graph, visited): 
                    return False
            # if cyclic
            elif n != parent: 
                return False
        return True
    
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        
        for x , y in edges: 
            graph[x].append(y) 
            graph[y].append(x)
            
        
        visited = set()
        # if cyclic
        if not self.dfs_check(0,-1, graph, visited): 
            print('is cyclic')
            return False
        
        # if disconnected
        if len(visited) != n : 
            print('not connected')
            return False
        
        return True 
#   BFS

class Solution:
    
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        
        for x , y in edges: 
            graph[x].append(y) 
            graph[y].append(x)
            
        
        visited = set()
        
        queue = deque()
        
        queue.append((0,-1))
        
        while queue: 
            node , parent = queue.popleft()
            # if cyclic
            if node in visited: 
                # print('cyclic at', node,parent)
                return False
            
            for neighbor in graph[node] : 
                if neighbor != parent: 
                    queue.append((neighbor,node))
                    
            visited.add(node)
            
        # if disconnected
        if len(visited) != n: return False 
        
        return True 
    
    

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hash_map = {}
        for edge in edges:
            a = edge[0]
            b = edge[1]
            
            if a not in hash_map:
                hash_map[a] = []
            if b not in hash_map:
                hash_map[b] = []
                
            hash_map[a].append(b)
            hash_map[b].append(a)
            
        visited = set()
        count = 0
        print(hash_map)
        for i in range(n):
            if i not in hash_map:
                count += 1
            if i in hash_map and self.dfs(hash_map, i, visited) == True:
                count += 1
        return count
            
    def dfs(self, hash_map, node, visited):
        if node in visited:
            return False
        visited.add(node)
        
        for neighbor in hash_map[node]:
            print(neighbor)
            self.dfs(hash_map, neighbor, visited)
        return True
#cutting edge:
def dfs(node,graph,visited,comp):
    comp.append(node)
    visited[node]:True
    for child in graph[node]:
        if not visited[child]:
            dfs(child,graph,visited,comp)


if __name__=="__main__":#DFS
    graph={
        0:[2],
        1:[2,3],
        2:[0,1,4],
        3:[1,4],
        4:[2,3]
    }
    node=0
    visited=[False]*len(graph)
    comp=[]
    print(dfs(node,graph,visited,comp))
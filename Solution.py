
n = 0
wc = []
rv = []
adj = []
parent = []
performance = []
performance_subtree = []
visited = []
root_node = 0
ans = []


def dfs(node):

    if visited[node]:
        return
    visited[node] = True
    subtree_per = 0
    for neigh in adj[node]:
        if not visited[neigh]:
            dfs(neigh)
        if performance_subtree[neigh]>=0:
            subtree_per += performance_subtree[neigh]

    subtree_per += performance[node]
    performance_subtree[node] = subtree_per

def calc_subtree_perf():
    global n, visited, nodes_to_be_removed, performance_subtree
    visited = [False for _ in range(n)]
    performance_subtree = [0 for _ in range(n)]
    dfs(root_node)

def can_be_removed(node):
    p = parent[node]
    while p!=-1:
        if performance_subtree[p] > performance_subtree[node]:
            ans.append([node+1, p+1])
            return True
        p = parent[p]
    return False

def calc_firing_ancess():
    global ans
    ans = []
    que = []
    que.append(root_node)
    visited = [False for _ in range(n)]
    visited[root_node] = True
    que_pointer = 0
    nodes_to_be_removed = []
    while que_pointer < len(que):
        node = que[que_pointer]
        que_pointer+=1
        if performance_subtree[node] < 0 and can_be_removed(node):
            nodes_to_be_removed.append(node)
        else:
            for neigh in adj[node]:
                if not visited[neigh]:
                    visited[neigh] = True
                    que.append(neigh)



def solve():
    global n, wc, rv, performance, adj, root_node, parent
    n = int(input())
    wc = list(map(int, input().split()))
    rv = list(map(int, input().split()))
    adj = [[] for _ in range(n)]
    performance = [rv[i] - wc[i] for i in range(n)]

    parent = [-1 for _ in range(n)]
    for i in range(n-1):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
        parent[v-1] = (u-1)

    for i in range(n):
        if parent[i]==-1:
            root_node = i

    calc_subtree_perf()

    calc_firing_ancess()
    # print(performance)
    # print(performance_subtree)
    k = len(ans)

    print(k)
    ans.sort()
    for i in range(k):
        print(*ans[i])

solve()

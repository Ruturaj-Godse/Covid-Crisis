import random

N_MAX = 1000
WC_MAX = 100000
RV_MAX = 100000

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


def solve_test_case(_n, _wc, _rv, edge_list):
    global n, wc, rv, performance, adj, root_node, parent
    # n = int(input())
    # wc = list(map(int, input().split()))
    # rv = list(map(int, input().split()))
    n = _n
    wc = _wc
    rv = _rv
    adj = [[] for _ in range(n)]
    performance = [rv[i] - wc[i] for i in range(n)]
    print(performance)
    parent = [-1 for _ in range(n)]
    for i in range(n-1):
        u, v = edge_list[i]
        adj[u-1].append(v-1)
        parent[v-1] = (u-1)

    for i in range(n):
        if parent[i]==-1:
            root_node = i

    calc_subtree_perf()

    calc_firing_ancess()



def make_test_case(file, no):
    global ans
    line = "Test case " + str(no) + "\n"
    file.write(line)
    line = "Input :" + "\n"
    file.write(line)
    n = random.randint(1, N_MAX)
    wc = [random.randint(0, WC_MAX) for _ in range(n)]
    rv = [random.randint(0, RV_MAX) for _ in range(n)]

    line = str(n) + "\n"
    file.write(line)

    line = ""
    for i in range(n-1):
        line += str(wc[i]) + " "
    line += str(wc[-1]) + "\n"
    file.write(line)

    line = ""
    for i in range(n-1):
        line += str(rv[i]) + " "
    line += str(rv[-1]) + "\n"
    file.write(line)

    edge_list = []
    rem_nodes = [i for i in range(1, n+1)]
    used_nodes = []

    root_node = random.choice(rem_nodes)
    rem_nodes.remove(root_node)
    used_nodes.append(root_node)

    for _ in range(n-1):
        v = random.choice(rem_nodes)
        u = random.choice(used_nodes)
        edge_list.append((u, v))
        line = str(u) + " " + str(v) + "\n"
        file.write(line)
        rem_nodes.remove(v)
        used_nodes.append(v)

    solve_test_case(n, wc, rv, edge_list)

    line = "\n"
    file.write(line)

    line = "Output :" + "\n"
    file.write(line)

    k = len(ans)
    line = str(k) + "\n"
    file.write(line)

    ans.sort()

    for i in range(k):
        line = str(ans[i][0]) + " " + str(ans[i][1]) + "\n"
        file.write(line)

    line = "\n\n"
    file.write(line)


if __name__ == "__main__":

    file = open("test_cases", "w")
    for i in range(1, 11):
        N_MAX = 10
        WC_MAX = 100
        RV_MAX = 100
        make_test_case(file, i)
    for i in range(11, 31):
        N_MAX = 1000
        WC_MAX = 100000
        RV_MAX = 100000
        make_test_case(file, i)

    file.close()

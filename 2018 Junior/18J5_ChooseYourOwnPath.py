N = int(input())

pages = []

for i in range(N):
    N, *current_page = map(int, input().split())

    pages.append(current_page)

def bfs(pages):
    shortest_path = 0
    all_pages_visible = 'N'
    q = [(1, 1)]
    visited = [0]

    while q:
        elem, level = q.pop(0)
        adjavent_pages = pages[elem-1]

        if adjavent_pages == [] and shortest_path == 0:
            shortest_path = level

        for p in adjavent_pages:
            if p not in visited:
                q.append((p, level + 1))
                visited.append(p)

    all_pages = range(1,N + 1)
    if set(visited) == set(all_pages):
        all_pages_visible = 'Y'

    return all_pages_visible, shortest_path

all_pages_visible, shortest_path = bfs(pages)

print(all_pages_visible)
print(shortest_path)

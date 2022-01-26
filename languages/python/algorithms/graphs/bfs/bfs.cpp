#include <iostream>
#include <queue>
#include <unordered_map>
#include <unordered_set>

void bfs(std::unordered_map<char, std::vector<char>> &graph, char startnode)
{
    std::queue<char> bfs_q;
    std::unordered_set<char> visited;
    bfs_q.emplace(startnode);

    while(!bfs_q.empty())
    {
        auto node = bfs_q.front();
        bfs_q.pop();
        if (visited.find(node) == visited.end())
        {
            visited.insert(node);
            std::cout << node << " ";
            for (auto &child: graph[node])
            {
                bfs_q.emplace(child);
            }
        }
    }
    std::cout << std::endl;
}

int main()
{
    std::unordered_map<char, std::vector<char>> graph = {
        {'A', {'B', 'C'}},
        {'B', {'D', 'E'}},
        {'C', {'F'}},
        {'D', {}},
        {'E', {'F'}},
        {'F', {}},
    };

    bfs(graph, 'A');

    return 0;
}
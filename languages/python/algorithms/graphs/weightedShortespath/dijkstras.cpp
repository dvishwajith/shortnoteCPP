#include <iostream>
#include <queue>
#include <unordered_map>
#include <unordered_set>

class Graph
{

    public:
    Graph(int numberofnodes, std::vector<std::vector<int>> &adjacency_list);
    ~Graph();
    void dijkstras(int startnode);
    void dijkstrasMethod2(int startnode);
    private:
        // U : [(V1,W1), [V2,W2]]
        std::unordered_map<int,std::vector<std::pair<int,int>>>   m_graph;
        std::vector<int> m_distance;
        int m_number_of_nodes;


};

Graph::Graph(int numberofnodes, std::vector<std::vector<int>> &adjacency_list)
{
    m_number_of_nodes = numberofnodes;
    for (auto &edge: adjacency_list)
    {
        auto u = edge[0];
        auto v = edge[1];
        auto w = edge[2];

        if (m_graph.find(u) == m_graph.end()){ 
            m_graph[u] = std::vector<std::pair<int,int>>();
        }
        if (m_graph.find(v) == m_graph.end()) {
            m_graph[v] = std::vector<std::pair<int,int>>();
        }

        m_graph[u].push_back(std::pair<int, int>(v, w));
        m_graph[v].push_back(std::pair<int, int>(u, w));
        /*
        This works too
        m_graph[u].push_back({v, w});
        m_graph[v].push_back({u, w});
        */
        
    }

    for(int i=0;i < numberofnodes; i++)
    {
        m_distance.push_back(INT32_MAX);
    }
}

Graph::~Graph()
{}

void Graph::dijkstras(int startnode)
{

    std::unordered_set<int> visited;
    // weight, node(contaner type)
    /*
    // This method works too. Using a lambda function. But there is some decltype magic here
    auto comparison_func = [&](std::pair<int,int> const &a, std::pair<int,int> const &b){ return a.first > b.first ;};
    std::priority_queue<std::pair<int,int>, std::vector<std::pair<int,int>>, decltype(comparison_func)> pq{comparison_func}; // using std::greater<int> will force  this to become ascending order
    */

    std::priority_queue<std::pair<int,int>, std::vector<std::pair<int,int>>, std::greater<std::pair<int, int>>> pq; // using std::greater<std::pair<int, int>>>will force  this to become ascending order
    pq.push({0,startnode});
    m_distance[0] = 0;

    while(!pq.empty())
    {
        auto weight_node = pq.top();
        pq.pop();
        auto weight = weight_node.first;
        auto node = weight_node.second;
        if (visited.find(node) == visited.end())
        {
            visited.insert(node);
            for(auto &child_weight_pair:m_graph[node])
            {
                auto child = child_weight_pair.first;
                auto ch_weight = child_weight_pair.second;
                if( m_distance[node] < INT32_MAX && m_distance[child] > m_distance[node] + ch_weight)
                {
                    m_distance[child] = m_distance[node] + ch_weight;
                    pq.push({ch_weight, child});
                }
                

            }
        }

    }

    for(const auto &d:m_distance)
    {
        std::cout<< d << " ";
    }
    std::cout << std::endl;
}

/**
 * @brief Using a Vector to hold [weight,node] insted of a pair. First value will e choosen as weight
 * by default
 * 
 * @param startnode 
 */
void Graph::dijkstrasMethod2(int startnode)
{
    std::unordered_set<int> visited;
    // weight, node(contaner type)
    std::priority_queue<std::vector<int>, std::vector<std::vector<int>>, std::greater<std::vector<int>>> pq; // using std::greater<int> will force  this to become ascending order
    pq.push({0,startnode});
    m_distance[0] = 0;

    while(!pq.empty())
    {
        auto weight_node = pq.top();
        pq.pop();
        auto weight = weight_node[0];
        auto node = weight_node[1];
        if (visited.find(node) == visited.end())
        {
            visited.insert(node);
            for(auto &child_weight_pair:m_graph[node])
            {
                auto child = child_weight_pair.first;
                auto ch_weight = child_weight_pair.second;
                if( m_distance[node] < INT32_MAX && m_distance[child] > m_distance[node] + ch_weight)
                {
                    m_distance[child] = m_distance[node] + ch_weight;
                    pq.push({ch_weight, child});
                }
                

            }
        }

    }

    for(const auto &d:m_distance)
    {
        std::cout<< d << " ";
    }
    std::cout << std::endl;
}



int main()
{
        std::vector<std::vector<int>> adjacency_list = {
            //u , v, Weight    
            {0, 1,  4},
            {0, 6,  7},
            {1, 6,  11},
            {1, 7,  20},
            {1, 2,  9},
            {2, 3,  6},
            {2, 4,  2},
            {3, 4,  10},
            {3, 5,  5},
            {4, 5,  15},
            {4, 7,  1},
            {4, 8,  5},
            {5, 8,  12},
            {6, 7,  1},
            {7, 8,  3}
    };

    Graph test(9, adjacency_list);
    test.dijkstras(0);
    test.dijkstrasMethod2(0);
    return 0;
}
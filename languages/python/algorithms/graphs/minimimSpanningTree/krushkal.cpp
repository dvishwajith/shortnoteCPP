#include <iostream>
#include <vector>
#include <algorithm>

class Krushkal
{
    private:
        std::vector<int> m_parent_arr;

    public:
        Krushkal(int nodes);
        ~Krushkal();
        int mst(std::vector<std::vector<int>> &adjacency_list);
        int find(int node);
        bool doUnion(int a, int b);

};


int Krushkal::find(int node)
{
    if ( m_parent_arr[node] == node)
    {
        return node;
    }
    else
    {
        return find(m_parent_arr[node]);
    }
}

bool Krushkal::doUnion(int a, int b)
{
    auto parent_a = find(a);
    auto parent_b = find(b);
    if (parent_a == parent_b)
    {
        return false;
    }
    else
    {
        m_parent_arr[parent_b] = parent_a;
        return true;
    }
}

Krushkal::Krushkal(int nodes)
{
    for(int i=0; i < nodes; i++)
    {
        m_parent_arr.push_back(i);
    }

}



Krushkal::~Krushkal(){
}




int Krushkal::mst(std::vector<std::vector<int>> &adjacency_list)
{
    int mstweight = 0;
    std::sort(adjacency_list.begin(), adjacency_list.end(), [](std::vector<int> &a, std::vector<int> &b)
                                                            { 
                                                                return a[2] < b[2];
                                                            });

    for(const auto &edge: adjacency_list)
    {
        auto u = edge[0];
        auto v = edge[1];
        auto weight = edge[2];
        if(doUnion(u, v))
        {
            mstweight += weight;
        }
    }

    return mstweight;
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
    Krushkal test(9);
    std::cout << test.mst(adjacency_list) << std::endl;
    return 0;
}
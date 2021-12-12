#include <iostream>
#include <memory>

class Node
{
private:
    /* data */
public:
    int data;
    std::shared_ptr<Node> m_next;
    std::shared_ptr<Node> m_prev;
    Node(int obj);
    ~Node();
};

Node::Node(int obj) : m_next(nullptr), m_prev(nullptr)
{
    data = obj;
}

Node::~Node()
{
    std::cout << " Destructor called " << __FUNCTION__  << ":" << __LINE__<< std::endl;
}


class DoubleLinkedList
{
private:
    /* data */
public:
    std::shared_ptr<Node> m_head;
    std::shared_ptr<Node> m_tail;
    DoubleLinkedList(/* args */);
    ~DoubleLinkedList();
    void addItem(int obj);
    void removeItem(int obj);
    void printall();
};

DoubleLinkedList::DoubleLinkedList(/* args */) : m_head(nullptr), m_tail(nullptr)
{
}

DoubleLinkedList::~DoubleLinkedList()
{
    std::cout << " Destructor called " << __FUNCTION__  << ":" << __LINE__<< std::endl;
}

void DoubleLinkedList::addItem(int obj)
{
    auto node = std::make_shared<Node>(obj);
    if(m_head)
    {
        m_head->m_prev = node;
    }

    node->m_next = std::move(m_head);
    m_head = std::move(node);

    if(m_tail == nullptr)
    {
        m_tail = node;
    }
}

void DoubleLinkedList::printall()
{
    auto temp_node = m_head;
    while(temp_node != nullptr)
    {
        std::cout << temp_node->data << std::endl;
        temp_node = temp_node->m_next;
    }
}


void DoubleLinkedList::removeItem(int obj)
{
    
    if(m_head->data == obj)
    {
        m_head = (m_head->m_next);
    }

    std::shared_ptr<Node> temp_node = m_head;  

    while(temp_node != nullptr)
    {
        if(temp_node->data == obj)
        {
            if(auto prev_node = temp_node->m_prev)
            {
                prev_node->m_next = std::move(temp_node->m_next);
                if(temp_node->m_next)
                {
                    temp_node->m_next->m_prev = prev_node;
                }
                else
                {
                    m_tail = prev_node;
                }           
            }
        }
        temp_node = temp_node->m_next;
    }
}

int main()
{
    auto linkedlist  = std::unique_ptr<DoubleLinkedList>(new DoubleLinkedList());
    linkedlist->addItem(1);
    linkedlist->addItem(2);
    linkedlist->addItem(3);
    linkedlist->addItem(4);
    linkedlist->addItem(5);
    linkedlist->printall();
    linkedlist->removeItem(3);
    linkedlist->printall();
    return 0;
}
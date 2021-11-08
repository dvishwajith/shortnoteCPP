#include <iostream>
#include <memory>

class Node
{
private:
    /* data */
public:
    int data;
    std::shared_ptr<Node> m_next;
    Node(int obj);
    ~Node();
};

Node::Node(int obj) : m_next(nullptr)
{
    data = obj;
}

Node::~Node()
{
}


class LinkedList
{
private:
    /* data */
public:
    std::shared_ptr<Node> m_head;
    LinkedList(/* args */);
    ~LinkedList();
    void addItem(int obj);
    void removeItem(int obj);
    void printall();
};

LinkedList::LinkedList(/* args */) : m_head(nullptr)
{
}

LinkedList::~LinkedList()
{
}

void LinkedList::addItem(int obj)
{
    auto node = std::make_shared<Node>(obj);
    node->m_next = std::move(m_head);
    m_head = std::move(node);
}

void LinkedList::printall()
{
    auto temp_node = m_head;
    while(temp_node != nullptr)
    {
        std::cout << temp_node->data << std::endl;
        temp_node = temp_node->m_next;
    }
}

void LinkedList::removeItem(int obj)
{
    auto temp_node = m_head;  //  auto&  temp_node = m_head; reference& will make output so diffrent. Find out why
    if(m_head->data == obj)
    {
        m_head = (m_head->m_next);
    }
    else
    {
        while(temp_node->m_next != nullptr)
        {
            if(temp_node->m_next->data == obj)
            {
                temp_node->m_next = std::move(temp_node->m_next->m_next);
            }
            else
            {
                temp_node = temp_node->m_next;
            }
            
        }
    }
    
}

int main()
{
    auto linkedlist  = std::make_unique<LinkedList>();
    linkedlist->addItem(1);
    linkedlist->addItem(2);
    linkedlist->addItem(3);
    linkedlist->addItem(4);
    linkedlist->addItem(5);
    linkedlist->printall();
    linkedlist->removeItem(1);
    linkedlist->printall();
    return 0;
}
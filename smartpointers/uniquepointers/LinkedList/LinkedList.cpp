#include <iostream>
#include <memory>

class Node
{
private:
    /* data */
public:
    int data;
    std::unique_ptr<Node> m_next;
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
    std::unique_ptr<Node> m_head;
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
    auto node = std::make_unique<Node>(obj);
    node->m_next = std::move(m_head);
    m_head = std::move(node);
}

void LinkedList::removeItem(int obj)
{
    auto temp_node = m_head.get();
    while(temp_node != nullptr)
    {
        /**
         * This part will looks like normal LinkedList with plain raw pointers.
         * LinkedLisst with unique pointers cannot be implemented without using raw pinters. Which violate the principal.
         * 
         */

        // if(temp_node->data == obj)
        // {
            
        // }
        // std::cout << temp_node->data << std::endl;
        // temp_node = temp_node->m_next.get();
    }

    auto node = std::make_unique<Node>(obj);
    node->m_next = std::move(m_head);
    m_head = std::move(node);
}



void LinkedList::printall()
{
    /**
     * if we declared m_head as a shared pointer, then we will not have to use raw pointers here
     */
    auto& temp_node = m_head; 
    while(temp_node != nullptr)
    {
        std::cout << temp_node->data << std::endl;
        temp_node = (temp_node->m_next);
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
    linkedlist->printall();
    return 0;
}
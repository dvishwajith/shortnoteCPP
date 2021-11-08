#ifndef __LINKED_LIST_H__
#define __LINKED_LIST_H__

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


class DoubleLinkedList
{
private:
    /* data */
public:
    std::unique_ptr<Node> m_head;
    DoubleLinkedList(/* args */);
    ~DoubleLinkedList();
    void addItem(int obj);
    void printall();
};

DoubleLinkedList::DoubleLinkedList(/* args */) : m_head(nullptr)
{
}

DoubleLinkedList::~DoubleLinkedList()
{
}

void DoubleLinkedList::addItem(int obj)
{
    auto node = std::make_unique<Node>(Node(obj));
    node->m_next = std::move(m_head);
    m_head = std::move(node);
}

void DoubleLinkedList::printall()
{
    auto temp_node = m_head.get();
    while(temp_node != nullptr)
    {
        std::cout << temp_node->data << std::endl;
    }
}

int main()
{
    auto linkedlist  = std::make_unique<DoubleLinkedList>();
    linkedlist->addItem(1);
    linkedlist->addItem(2);
    linkedlist->addItem(3);
    linkedlist->addItem(4);
    linkedlist->addItem(5);
    linkedlist->printall();
    return 0;
}


#endif // __LINKED_LIST_H__

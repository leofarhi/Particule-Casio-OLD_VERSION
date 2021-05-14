#pragma once
#ifndef List_H_
#define List_H_
#include "usefull.h"


template <typename T>
struct Node {
    T data;
    Node* next;
    Node* prev;
};

template <typename T> class List {
private:
    Node<T>* head;
    Node<T>* tail;
    Node<T>* get_node(int index)
    {
        int i = 0;
        Node<T>* it = head;
        for (; it != NULL && i != index; it = it->next)
        {
            i++;
        }

        return it;
    }

    T prepop()
    {
        if (head == NULL)
            return NULL;
        T value = head->data;

        if (head == tail)
        {
            head = NULL;
            tail = NULL;
        }
        else
        {
            head = head->next;
            head->prev = NULL;
        }
        Count--;
        return value;
    }

    T get(int index)
    {
        if (index < -1)
            return NULL;

        Node<T>* it = get_node(index);

        if (it == NULL)
            return NULL;

        return it->data;
    }

    
public:
    int Count;
    List() {
        Count = 0;
        head = NULL;
        tail = NULL;
    }
    /*List(T* arr,int count) {
        Count = 0;
        head = NULL;
        tail = NULL;
        for (int i = 0; i < Count; i++)
        {
            Add(arr[i]);
        }
    }*/
    
    T operator[](int index) {
        return get(index);
    }
    void Add(T val) {
        Node<T>* n = new Node<T>();
        n->data = val;
        Count++;
        if (head == NULL)
        {
            head = n;
            tail = n;
        }
        else
        {
            n->prev = tail;
            tail->next = n;
            tail = n;
        }
    }

    T Pop() {
        T value = tail->data;

        if (head == tail)
        {
            head = NULL;
            tail = NULL;
        }
        else
        {
            tail = tail->prev;
            tail->next = NULL;
        }
        Count--;
        return value;
    }

    T RemoveAt(int index) {
        if (index < 0)
            return NULL;

        if (index == 0)
            return prepop();

        Node<T>* it = get_node(index);

        if (it == NULL)
            return NULL;

        if (it->next == NULL)
            return Pop();
        T value = it->data;
        it->next->prev = it->prev;
        it->prev->next = it->next;

        delete it;
        Count--;
        return value;
    }

    void Clear() {
        while(Count>0)
        {
            Pop();
        }
    }

    int IndexOf(T val) {
        Node<T>* temp = head;
        int i = 0;
        while (temp->next) {
            if (temp->data == val) return i;
            else temp = temp->next;
            i++;
        }
        delete temp;
        return -1;
    }

    bool Contains(T val) {
        Node<T>* temp = head;
        while (temp->next) {
            if (temp->data == val) return true;
            else temp = temp->next;
        }
        delete temp;
        return false;
    }
};

#endif
"""Fibonacci Heap Implementation
This module provides an implementation of Fibonacci Heap, a data structure 
that supports a collection of priority queue operations with efficient 
amortized time complexity. Fibonacci heaps are particularly useful for 
graph algorithms like Dijkstra's shortest path and Prim's minimum spanning 
tree."""
from math import inf, log2
COUNT = 1

class FibonacciHeap:
    """Represents the main Fibonacci heap structure. 
    Supports operations like insertion, extraction of the minimum element, 
    union, decrease key, and delete."""
    def __init__(self, node=None):
        self.nodes_to_visit = []
        if node is None:
            self.root_list=None
            self.n=0
            self.i=None
        else:
            self.root_list=List(node)
            self.n=1
            self.i=self.root_list.guard

    def add_to_root_list(self, x):
        x.parent=None
        self.root_list.add_element(x)

    def aet_as_minimum(self, x):
        x.parent=None
        self.root_list.set_as_guard(x)

    def fib_heap_insert(self, x):
        if self.root_list.guard is None or x.key < self.root_list.guard.key:
            self.add_to_root_list(x)
            self.aet_as_minimum(x)
        else:
            self.add_to_root_list(x)
        self.n+=1

    def fib_heap_link(self, y, x):
        x.add_to_children_list(y)
        x.degree+=1
        y.mark=False

    def consolidate(self):
        max_degree=int(log2(self.n))+1
        aux=[None]*max_degree
        for w in self.root_list:
            x=w
            d=x.degree
            while aux[d]:
                y=aux[d]
                if x.key > y.key:
                    x, y = y, x
                self.fib_heap_link(y, x)
                aux[d]=None
                d+=1
            aux[d]=x
        self.root_list=List()
        for i in range(max_degree):
            if aux[i]:
                self.add_to_root_list(aux[i])
                if aux[i].key<self.root_list.guard.key:
                    self.aet_as_minimum(aux[i])

    def extract_min(self):
        z=self.root_list.guard
        if z:
            if z.children_list:
                for x in z.children_list:
                    self.add_to_root_list(x)
            self.root_list.remove_first()
            self.consolidate()
            self.n-=1
        return z

    def cut(self, node, parent):
        parent.delete_child(node)
        self.add_to_root_list(node)
        node.mark=False
        print("cut finish")

    def cascading_cut(self, x, decrease):
        print(f" stopien wezla {x.key} to {x.degree}")
        if decrease!=-1:
            x.degree-=decrease
        print(f" zmniejsza stopien wezla {x.key} na {x.degree}")
        z=x.parent
        if z:
            print(f" zmniejsza stopien wezla {z.key}")
            if x.mark is False:
                x.mark=True
                print("change mark")
                if decrease!=0:
                    while True:
                        decrease_degree=1 if z.children_list.list_max_deg()<x.degree+1 else 0
                        z.degree-=decrease_degree
                        if z.parent is None:
                            break
                        x=z
                        z=z.parent
                        print(f"klucz z {z.key}")
            else:
                self.cut(x, z)
                print("cascading")
                if decrease!=0:
                    decrease_degree=1 if z.children_list.list_max_deg()<x.degree+1 else 0
                self.cascading_cut(z, decrease_degree)

    def fib_heap_decrease_key(self, node, new_value):
        if new_value>node.key:
            raise ValueError("New value is larger than current")
        node.key=new_value
        y=node.parent
        if y is not None and node.key<y.key:
            self.cut(node, y)
            decrease_degree=-1
            print(decrease_degree)
            print(y.children_list)
            if not y.children_list.empty():
                decrease_degree=1 if y.children_list.list_max_deg()<node.degree else 0
            print(decrease_degree)
            self.cascading_cut(y, decrease_degree)
        if node.key<self.root_list.guard.key:
            self.aet_as_minimum(node)

    def fib_heap_delete(self, node):
        self.fib_heap_decrease_key(node, float(-inf))
        self.extract_min()

    def __iter__(self):
        self.nodes_to_visit=[]
        if self.root_list is not None:
            for x in self.root_list:
                self.add_to_stack(x)
        return self

    def __next__(self):
        if not self.nodes_to_visit:
            raise StopIteration()
        current_node=self.nodes_to_visit.pop()
        return current_node

    def add_to_stack(self, node):
        self.nodes_to_visit.append(node)
        if node.children_list is None:
            return
        for x in node.children_list:
            self.add_to_stack(x)

    def __str__(self):
        print(f"drukuje kopiec, liczba wezlow: {self.n}")
        print_2d_util(self.root_list, 0)
        return ""

def print_2d_util(my_list, space):
    if my_list is None:
        return
    space += COUNT
    licznik = 0
    for node in my_list:
        print_2d_util(node.children_list, space)
        line = " " * space + f"{node.key}"
        print(line)
        licznik += 1


def union(h1, h2):
    h=FibonacciHeap()
    g1=h1.root_list.guard.key
    g2=h2.root_list.guard.key
    if g1<g2:
        h=h1
        h3=h2
    else:
        h=h2
        h3=h1
    temp=h.root_list.guard.right
    temp2=h3.root_list.guard.left
    h.root_list.guard.right=h3.root_list.guard
    h3.root_list.guard.left=h.root_list.guard
    temp2.right=temp
    temp.left=temp2
    return h

class Node:
    def __init__(self, key, parent=None):
        self.key=key
        self.parent=parent
        self.children_list=None
        self.left=self
        self.right=self
        self.degree=0
        self.mark=False

    def add_to_children_list(self, child):
        child.parent=self
        if self.children_list is None:
            self.children_list=List(child)
        else:
            self.children_list.add_element(child)

    def delete_child(self, x):
        if self.children_list is None:
            raise ValueError("brak dzieci")
        if len(self.children_list)>1:
            print(f"usuwam element {x.key}")
            self.children_list.remove(x)
        else:
            self.children_list.remove_first()
            self.degree-=1

    def clear(self, node):
        if node.children_list is None:
            del node
        else:
            for x in node.children_list:
                self.clear(x)

class List:
    def __init__(self, node=None):
        self.guard=node
        if self.guard:
            self.guard.left=self.guard
            self.guard.right=self.guard
        self.i=None
        self.iteration_start=False
        self.size=1

    def list_max_deg(self):
        max1 = self.guard.degree
        for x in self:
            max1 = max(max1, x.degree)
        return max1


    def empty(self):
        if self.guard is None or self is None:
            return True
        return False

    def add_element(self, node):
        if self.guard is None:
            self.guard=node
            self.guard.left=self.guard
            self.guard.right=self.guard
        else:
            last=self.guard.left
            last.right=node
            node.left=last
            node.right=self.guard
            self.guard.left=node
        self.size+=1

    def __len__(self):
        return self.size

    def remove(self, node):
        if self.guard is None:
            print("Lista jest pusta, nie można usunąć elementu.")
            return
        if node is self.guard:
            self.remove_first()
            return
        node.left.right=node.right
        node.right.left=node.left
        self.size-=1

    def remove_first(self):
        if self.guard==self.guard.right:
            self.guard=None
            self.size=0
            return
        self.guard.right.left=self.guard.left
        self.guard.left.right=self.guard.right
        self.guard=self.guard.right
        self.size-=1

    def set_as_guard(self, node):
        self.guard=node

    def __iter__(self):
        self.i=self.guard
        self.iteration_start=True
        return self

    def __next__(self):
        if self.iteration_start is False or self.guard is None:
            raise StopIteration()
        if self.i.right is self.guard:
            self.iteration_start=False
        obj=self.i
        self.i=self.i.right
        return obj

    def __str__(self):
        if self.guard is None:
            return "empty"
        result=[]
        for x in self:
            result.append(str(x.key))
        return " -> ".join(result)

from printable_heap import PrintableHeap
from fib_heap_utils import FibonacciHeap, Node, union

def test_insert():
    heap = FibonacciHeap(Node(77))
    heap.fib_heap_insert(Node(5))
    heap.fib_heap_insert(Node(20))
    assert heap.root_list.guard.key == 5
    heap.extract_min()
    set1 = [84, 3422, 34, 23, 10, 458]
    for i in set1:
        heap.fib_heap_insert(Node(i))
    assert heap.root_list.guard.key == 10

def test_extract_min():
    heap = FibonacciHeap(Node(5))
    insert = [34, 45, 12, 4, 7, 87, 10, 56, 77, 31]
    for i in insert:
        heap.fib_heap_insert(Node(i))
    h = PrintableHeap(heap)
    h.place_nodes()
    string1 = str(h)
    assert string1 == '[31, 77, 56, 10, 87, 7, 12, 45, 34, 5, 4]'
    z = heap.extract_min()
    h = PrintableHeap(heap)
    h.place_nodes()
    string1 = str(h)
    print(string1)
    assert z.key == 4
    assert string1 == "[31, False, False, False, 5]\n[77, False, 7, 12, 34]\n[False, 10, 87, 45, False]\n[False, 56, False, False, False]"
    z = heap.extract_min()
    z = heap.extract_min()
    z = heap.extract_min()
    z = heap.extract_min()
    h = PrintableHeap(heap)
    h.place_nodes()
    string1 = str(h)
    str(h)
    assert string1 == "[False, 34, 31]\n[45, 87, 77]\n[56, False, False]"

def test_union():
    n = Node(1)
    kopiec = FibonacciHeap(n)
    insert = [34, 5, 45]
    for i in insert:
        kopiec.fib_heap_insert(Node(i))
    kopiec2 = FibonacciHeap(Node(4))
    insert = [12, 3, 90]
    for i in insert:
        kopiec2.fib_heap_insert(Node(i))
    kopiec.extract_min()  # usuwa 1 z kopca
    H = union(kopiec, kopiec2)
    v1 = H.extract_min()  # usuwa 3 z kopca
    assert v1.key == 3
    G = PrintableHeap(H)
    G.place_nodes()
    g = str(G)
    assert g == "[12, False, 4]\n[90, 5, 45]\n[False, 34, False]"

def test_decrease_key():
    heap = FibonacciHeap(Node(84))
    set1 = [3422, 34, 23, 10, 458]
    for i in set1:
        heap.fib_heap_insert(Node(i))
    for x in heap:
        if x.key == 3422:
            print(x.key)
            heap.fib_heap_decrease_key(x, 6)
    G = PrintableHeap(heap)
    G.place_nodes()
    g = str(G)
    assert g == "[84, 34, 23, 10, 458, 6]"
    heap.extract_min()
    G = PrintableHeap(heap)
    G.place_nodes()
    g = str(G)

def test_delete():
    heap = FibonacciHeap(Node(84))
    set1 = [3422, 34, 23, 10, 458]
    for i in set1:
        heap.fib_heap_insert(Node(i))
    for x in heap:
        if x.key == 3422:
            heap.fib_heap_delete(x)
    G = PrintableHeap(heap)
    G.place_nodes()
    g = str(G)
    assert g == "[84, False, 10]\n[False, 23, 458]\n[False, 34, False]"

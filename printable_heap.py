"""PrintableHeap służy do tworzenia listy 2D która będzie 
reprezentować strukturę kopca w postaci siatki, 
klasa pomocnicza do FibonacciHeap"""

def width(node):
    if node is None or node.children_list is None or len(node.children_list) == 0:
        return 0  # jesli brak dzieci, szerokość to 0

    # szerokość to suma szerokości dzieci + dodatkowe pole na każde połączenie
    total_width = sum(width(child) for child in node.children_list)
    return len(node.children_list) - 1 + total_width

class PrintableHeap:
    def __init__(self, heap):
        self.heap = heap
        self.position_table = [[] for _ in range(30)]
    def place_nodes(self):
        max_deg = 0
        max_deg = max(x.degree for x in self.heap)

        print(f"maxstopien{max_deg}")
        for x in self.heap: #sprawdzam ile dany węzeł ma przodków i dodaję
            #dany węzeł do odpowiedniego wiersza tabeli iterator nie działa
            ancestors = 0
            z = x
            print(x.key)
            while z.parent is not None: #liczy przodkow wezla
                z = z.parent
                ancestors += 1
            if not x.children_list: #jezeli wezel x jest ostatnim lisciem to
                for i in range (1,max_deg+10): # aby sie zabezpieczyc przed wysokim
                    #drzewem przy usuwaniu wezow 10 dodatkowych pustych pol
                    self.position_table[ancestors+i].append(False) #wstawia za ostatnim
                    #lisciem puste pola
                    #w ilosci odpowiadajaej wysokosci drzewa zeby
                    #wykluczyc nakladanie sie kolejnych drzew
                    print(f"dodaje false za {x.key}")
            if x.children_list and x.children_list.empty():
                for i in range (1,max_deg+10):
                    self.position_table[ancestors+i].append(False)
                    print(f"dodaje false za {x.key}")
            else:
                self.position_table[ancestors].extend([False] * (width(x))) #wstawia przed
                #wezlem odpowiednia ilosc pustych pol w zaleznosci od szerokosci potomkow
            self.position_table[ancestors].append(x)  #wstawia do odpowiedniego
            #wiersza tabeli w zaleznosci od liczby przodkow (0-0 przodkow,1-1pzodek itd.)
    def __str__(self):
        result = []
        for inner_list in self.position_table:
            if isinstance(inner_list, list):
                if all(item is False for item in inner_list):
                    break
                keys = [
                    str(item.key) if hasattr(item, "key") else "False"
                    for item in inner_list if hasattr(item, "key") or item is False
                ]
                result.append(f"[{', '.join(keys)}]")
        return "\n".join(result)

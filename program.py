import tkinter as tk
from math import sqrt
import json
from printable_heap import PrintableHeap
from fib_heap_utils import Node, FibonacciHeap

global font1
font1 = ("Linux Biolinum G", 14)
global font2
font2 = ("Linux Biolinum G", 9)
global FRAME_C
FRAME_C = "dark gray"
global LABEL_C
LABEL_C = "dark gray"
global bd
bd = 2

def on_enter(button):
    button.config(fg="magenta", bg="light yellow")

def on_leave(button):
    button.config(fg="light yellow", bg="brown")

def configure_button(button):
    button.config(
        font=font1,
        fg="light yellow",
        bg="brown",
        relief="groove",
        activebackground="light yellow",
        activeforeground="magenta",
    )
    button.bind("<Enter>", lambda e: on_enter(button))
    button.bind("<Leave>", lambda e: on_leave(button))

class FibonacciVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.kopiec = None
        self.k = None
        self.canvas = None

        self.root.title("Kopiec Fibonacciego - wizualizacja")
        self.top_frame = tk.Frame(root)
        self.top_frame.pack(side="top", fill="x", padx=0, pady=0)
        self.top_frame.columnconfigure(0, weight=5)
        self.top_frame.columnconfigure(1, weight=5)

        self.bottom_frame = tk.Frame(root)
        self.bottom_frame.pack(side="bottom", fill="x", padx=0, pady=0)

        self.info_frame = tk.Frame(self.top_frame, bg=FRAME_C,  height=200)
        self.info_frame.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.info_frame.pack_propagate(False)

        self.input_frame = tk.Frame(self.top_frame, bg=FRAME_C, height=300)
        self.input_frame.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)
        self.input_frame.pack_propagate(False)

        self.canvas_frame = tk.Frame(self.bottom_frame, bg=LABEL_C, width=1500, height=200)
        self.canvas_frame.pack(fill="both", expand=True, padx=0, pady=0)

        self.Info("teksty.json")
        self.entryFrame()

        self.init_kopiec()
        self.createCanvas()

    def entryFrame(self):
        frame = tk.Frame(self.root)
        frame.pack(side="right", padx=0, pady=0)
        self.label_output = self.addLabel()
        self.entry = self.initInputPanel()
        self.initConfirmButton()
        self.initExtractMinButton()
        self.initDecreaseButton()
        self.initDeleteButton()

    def initInputPanel(self):
        entry = tk.Entry(self.input_frame, width=30)
        entry.pack(pady=5)
        return entry

    def initConfirmButton(self):
        button = tk.Button(self.input_frame, text="Wstaw", command=self.add, font=font1, bd=bd)
        button.pack(pady=5)
        configure_button(button)

    def initExtractMinButton(self):
        button = tk.Button(self.input_frame, text="Usuń minimalny element",
                           command=self.extract_min, font=font1, bd=bd)
        button.pack(pady=5)
        configure_button(button)

    def initDecreaseButton(self):
        button = tk.Button(self.input_frame, text="Zmniejsz klucz",
                           command=self.decrease, font=font1, bd=bd)
        button.pack(pady=5)
        configure_button(button)

    def initDeleteButton(self):
        button = tk.Button(self.input_frame, text="Usuń",
                            command=self.delete_node, font=font1, bd=bd)
        button.pack(pady=5)
        configure_button(button)

    def addLabel(self):
        label_output = tk.Label(self.input_frame,
                                text='Wpisz w okienko liczbę którą chcesz wstawić do kopca i kliknij "Wstaw" lub wpisz priorytet węzła który chcesz obnizyć oraz nowy priorytet i kliknij "Zmniejsz Klucz", aby usunąć węzeł wpisz jego priorytet do okienka i kliknij "Usuń"',
                                font=font1, wraplength=700, width=700, height=3,
                                anchor="center", justify="left", bg=FRAME_C)
        label_output.pack(pady=5)
        return label_output

    def Info(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.teksty = data.get("texts", [])
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Błąd wczytywania pliku JSON: {e}")
            self.teksty = []

        self.index = 0

        self.info_label = tk.Label(self.info_frame, text=self.teksty[self.index],
                                   font=font1, wraplength=700, width=100, height=10,
                                   anchor="center", justify="left", bg=FRAME_C)
        self.info_label.pack(pady=5)
        self.info_label.pack_propagate(False)

        self.change_button = tk.Button(self.info_frame, text="->",
                                       command=self.changeInfo, font=font1, bd=bd)
        self.change_button.pack(pady=5)
        configure_button(self.change_button)

    def changeInfo(self):
        self.index = (self.index + 1) % len(self.teksty)
        self.info_label.config(text=self.teksty[self.index])

    def add(self):
        user_input = self.entry.get()
        try:
            key = int(user_input)
            node = Node(key)
            if self.kopiec is None:
                self.kopiec = FibonacciHeap(node)
            else:
                self.kopiec.fib_heap_insert(node)

            self.label_output.config(text=f"Dodano: {key}")
            self.k = PrintableHeap(self.kopiec)
            self.k.place_nodes()
            self.createCanvas()
        except ValueError:
            self.label_output.config(text="Błąd: Podaj poprawną liczbę całkowitą!")

    def delete_node(self):
        if self.kopiec is None or self.kopiec.root_list is None:
            self.label_output.config(text="Kopiec jest pusty – brak elementów do zamiany kluczy.")
            return
        user_input = self.entry.get()
        try:
            for x in self.kopiec:
                if x.key == int(user_input):
                    print(x.key)
                    self.kopiec.fib_heap_delete(x)
                    break
            self.label_output.config(text=f"usunięto węzeł o kluczu {user_input}")
            print(self.kopiec)
            self.k = PrintableHeap(self.kopiec)
            self.k.place_nodes()
            print(self.k)
            self.createCanvas()
        except ValueError:
            self.label_output.config(text="Błąd: Podaj poprawną liczbę całkowitą!")

    def decrease(self):
        if self.kopiec is None or self.kopiec.root_list is None:
            self.label_output.config(text="Kopiec jest pusty – brak elementów do zamiany kluczy.")
            return
        user_input = self.entry.get()
        tab = user_input.split()
        try:
            for x in self.kopiec:
                if x.key == int(tab[0]):
                    print(x.key)
                    self.kopiec.fib_heap_decrease_key(x, int(tab[1]))
                    break
            self.label_output.config(text=f"zmieniono klucz wezla {tab[0]} na {x.key}")
            self.k = PrintableHeap(self.kopiec)
            self.k.place_nodes()
            self.createCanvas()
        except ValueError:
            self.label_output.config(text="Błąd: Podaj liczbę mniejszą od klucza")

    def extract_min(self):
        if self.kopiec is None or self.kopiec.root_list is None:
            self.label_output.config(text="Kopiec jest pusty – brak elementów do usunięcia.")
            return
        min_key = self.kopiec.extract_min()
        self.label_output.config(text=f"Usunięto minimalny element: {min_key.key}")
        self.k = PrintableHeap(self.kopiec)
        self.k.place_nodes()
        self.createCanvas()

    def draw_circles(self, points, cell_size, circle_size, padding):

        def draw_arrows(children, cell_size, x, y, canvas):

            def width(node):
                if node is None or node.children_list is None:
                    return 0
                return len(node.children_list) + sum(width(child) for child in node.children_list) - 1

            if children is not None:
                b = cell_size
                i = 0
                for node in children:
                    a = i * cell_size
                    c = sqrt(a**2 + b**2)
                    ratio = circle_size / (2 * c)
                    x1 = x * cell_size + cell_size/2
                    y1 = y * cell_size + cell_size/2
                    x2 = x * cell_size + cell_size/2 - cell_size * i
                    y2 = y * cell_size + cell_size + cell_size/2
                    m2 = ratio * (y2 - y1)
                    m1 = ratio * (x1 - x2)
                    x1 = x1 - m1
                    y1 = y1 + m2
                    canvas.create_line(x1, y1 , x2, y2, arrow="first", width=1, fill="dark blue")
                    if node.children_list is not None:
                        if len(node.children_list) > 1:
                            i += width(node)
                    i += 1

        for point in points:
            x, y, node = point
            self.canvas.create_oval( x * cell_size + padding, y * cell_size + padding,
                                    x * cell_size + padding + circle_size,
                                    y * cell_size + padding + circle_size,
                                    fill="light yellow" if node != self.kopiec.root_list.guard else "red", outline="black")
            self.canvas.create_text( x * cell_size + cell_size/2,
                                    y * cell_size + cell_size/2,
                                    text = f"{node.key} {node.degree} {len(node.children_list) if node.children_list else 'NONE'}",
                                    fill="black", font=font2)
            draw_arrows(node.children_list, cell_size, x, y, self.canvas)

    def createCanvas(self):
        print(self.k)
        if self.canvas:
            self.canvas.destroy()

        self.canvas = tk.Canvas(self.canvas_frame, width=1500, height=500, bg=LABEL_C, highlightthickness=0)
        self.canvas.pack()

        cell_size = 70
        padding = 5
        circle_size = cell_size - padding * 2

        if self.k:
            circle_points = []
            rowNum = 0
            for x in self.k.position_table:
                counter = 0
                for node in x:
                    if node is not False:
                        circle_points.append((counter, rowNum, node))
                    counter += 1
                rowNum += 1
            self.draw_circles(circle_points, cell_size, circle_size, padding)

    def init_kopiec(self):
        n = Node(1)
        self.kopiec = FibonacciHeap(n)
        insert = [34, 5, 45, 12, 4, 7, 87, 10, 56, 77, 31]
        for i in insert:
            self.kopiec.fib_heap_insert(Node(i))
        self.k = PrintableHeap(self.kopiec)
        self.k.place_nodes()

if __name__ == "__main__":
    root = tk.Tk()
    app = FibonacciVisualizerApp(root)
    root.mainloop()

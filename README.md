# Kopiec Fibonacciego z wizualizacją
Implementacja kopca fibonacciego i wizualizacja tkinter
Kopiec fibonacciego to implementacja kolejki priorytetowej. Każdy węzeł w kopcu ma priorytet na podstawie którego jest wyznaczana kolejnośc usuwania węzłów z kopca (najmniejszy priorytet najpierw). Kopiec składa się z listy korzeni drzew, które są drzewami mogącymi mieć dowolną ilośc dzieci w węźle (nie musi być to dwa, tak więc nie jest to kopiec binarny). Struktura zachowuje porządek kopca, czyli zawsze dzieci węzła mają większy priorytet niż rodzic. Inspiracją do stworzenia projektu był kod opisany w książce Wprowadzenie do Algorytmów - Cormen, Leicerson, Rivest.
## Pliki, które wchodzą w skład projektu
- fib_heap_utils.py
- printableHeap.py
- program.py
- teksty.json
- test_fh.py
### fib_heap_utils
Jest to plik, który jest bazą całego projektu, zawiera podstawowe operacje na kopcu takie jak: wstawianie elementu, usuwanie minimum, zmniejszenie klucza, usuwanie wskazanego węzła, łączenie kopców, umożliwia iterację po kopcu, ponadto posiada dwie klasy pomocnicze Node i List, kopiec ma strukturę warstwową i składa się z list węzłów, które posiadają listy dzieci. Pierwszym poziomem kopca jest lista korzeni.
### printableHeap
Zawiera klase PrintableHeap, która ma umożliwić przedstawienie kopca w formie która ułatwi wizualizacje, jest to tablica 2D, która posiada wolne przestrzenie pomiędzy poszczególnymi węzłami. Jest tu funkcja str, która umożliwia przedstawienie kopca w formie zrozumiałej dla użytkownika, która drukuje tą tablicę w konsoli.
### program
To interfejs napisany w tkinter, dzięki któremu można obsługiwać operacje na kopcu oraz wyświetlać kopiec.
### teksty
Teksty, które opisują krótko na czym polega Kopiec Fibonacciego.
### test_fh
Testy pytest.

# Aplikacja webowa/desktopowa

## Etap1 -- przygotowanie danych do wydruku

1. [u] Przycisk służący do wyboru pliku .xlsx przez usera
    - w pierwszej wersji wystarczy opcja .xlsx, później można zastanowić się nad REGEX
    - po wyborze pliku ścieżka powinna zostać wyświetlona dla usera
2. Pole do wpisywania wartości przez user
    - najlepiej, gdyby była opcja wpisywania stringów jeden pod drugim
    - user będzie wpisywał tam wartości odnoszące się do "Reference number"
3. Pole do wpisania wartości 
    - pole do wpisania wartości INT z przedziału [1-40]
    - user będzie wpisywał tam liczbę palet
3. Import danych z wybranego pliku
    - import kolumn:
    ```
        columns = [
            "Sales order","Reference number",
            "Line number", "Item number",
            "Text", "Quantity", "Unit"
        ]
    ```
    - import tylko tych wierszy które spełniają warunek:
    ```
    "Reference number" in {wartości z punktu 2.}
    ```
    - stworzenie pustych kolumn z nazwą "Pallet " + i -- [liczba kolumn to INT podany w punkcie 3.]
    ```
    for i in range(1,p3+1):
        df["Pallet "+ str(i)] = np.nan
    ```
4. Wyświetlenie userowi danych z możliwością edycji
    - user może wpisywać jedynie INT do stworzonych pustych kolumn
    - można zrobić formatowanie warunkowe:
        ```
        if df['Quantity'] == sum([df["Pallet "+ str(i)] for i in range(1, p3+1)]):
            kolor tła wiersza na zielono
        elif df['Quantity'] > sum([df["Pallet "+ str(i)] for i in range(1, p3+1)]):
            kolor tła wiersza na żółto
        else
            kolor tła wiersza na czerwono
        ```
5. Przycisk zapisu i eksportu danych to pliku .xlsx
    - coś w stylu "saveAs"
    - można od razu przygotować się do zapisu w innych formatach (csv, json)

## Etap 2 -- stworzenie dokumentu do wydruku

## Etap 3 -- zrobienie apki do zbierania pojedynczych plików dla jakieś babki 
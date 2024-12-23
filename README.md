
# Fake Data Generator - By Spel

## Polish / Polski

Aplikacja desktopowa napisana w Pythonie z użyciem PyQt5 do generowania fałszywych danych. Narzędzie to umożliwia tworzenie losowych zestawów danych do celów testowych i programistycznych. Obsługuje zapisywanie danych w formatach CSV, JSON oraz SQL.

### Funkcje
- **Obsługa wielu języków**: Generowanie danych w różnych lokalizacjach, w tym polskiej, angielskiej, niemieckiej, francuskiej i hiszpańskiej.
- **Konfigurowalne kolumny**: Możliwość dodawania lub usuwania kolumn oraz określenia metody Faker dla każdej kolumny.
- **Autoinkrementacja ID**: Opcja dodania kolumny z autoinkrementacją ID.
- **Opcje zapisu**: Zapisywanie wygenerowanych danych w formatach CSV, JSON lub SQL.
- **Przyjazny interfejs graficzny**: Intuicyjny interfejs oparty na PyQt5.

### Wymagania
- Python 3.7 lub nowszy
- Wymagane biblioteki Python:
  - `PyQt5`
  - `Faker`
  - `sqlite3`

Instalacja zależności za pomocą pip:
```bash
pip install PyQt5 Faker
```

### Instrukcja obsługi
1. **Uruchom aplikację**:
   ```bash
   python fake-data-generator.py
   ```
2. **Ustaw lokalizację**: Wybierz kraj/język z listy rozwijanej.
3. **Określ liczbę rekordów**: Wprowadź liczbę rekordów do wygenerowania.
4. **Skonfiguruj kolumny**:
   - Dodaj kolumnę, klikając „Dodaj kolumnę”.
   - Wybierz metodę Faker dla każdej kolumny.
5. **Wybierz format pliku**: Wybierz między CSV, JSON lub SQL.
6. **Generuj i zapisz**: Kliknij „Zapisz plik”, aby zapisać wygenerowane dane.

### Metody Faker
Aplikacja obsługuje wszystkie metody Faker. Pełna lista znajduje się w [dokumentacji Faker](https://faker.readthedocs.io/).

### Licencja
Projekt jest licencjonowany na zasadach licencji MIT. Szczegóły w pliku LICENSE.

### Podziękowania
Stworzone przez **Spel** ©.

---

## English

A desktop application written in Python using PyQt5 for generating fake data. This tool allows users to create randomized datasets for testing and development purposes. It supports saving data in CSV, JSON, and SQL formats.

### Features
- **Multi-language Support**: Generate data in multiple locales including Polish, English, German, French, and Spanish.
- **Customizable Columns**: Add or remove columns and specify the Faker method for each column.
- **Auto-increment ID**: Option to include an auto-incrementing ID column.
- **Save Options**: Save generated data in CSV, JSON, or SQL formats.
- **User-friendly GUI**: Intuitive interface built with PyQt5 for easy interaction.

### Requirements
- Python 3.7 or higher
- Required Python libraries:
  - `PyQt5`
  - `Faker`
  - `sqlite3`

Install dependencies using pip:
```bash
pip install PyQt5 Faker
```

### Usage
1. **Run the Application**:
   ```bash
   python fake-data-generator.py
   ```
2. **Set Locale**: Choose the desired country/locale from the dropdown.
3. **Specify Records**: Enter the number of records to generate.
4. **Configure Columns**:
   - Add a column by clicking "Add Column".
   - Select a Faker method for each column.
5. **Select File Type**: Choose between CSV, JSON, or SQL.
6. **Generate and Save**: Click "Save File" to save the generated data.

### Faker Methods
The application supports all Faker methods. For a full list, refer to the [Faker documentation](https://faker.readthedocs.io/).

### License
This project is licensed under the MIT License. See the LICENSE file for more details.

### Credits
Developed by **Spel** ©.

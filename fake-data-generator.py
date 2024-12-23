import sys
import os
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QComboBox
from faker import Faker
import csv
import json
import sqlite3

class DataGeneratorApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fake Data Generator - By Spel")
        self.setGeometry(100, 100, 700, 450)
        self.setFixedSize(700, 450)
        
        self.fake = Faker()
        self.initUI()

    def initUI(self):
        #Credit by Spel 
        self.credit_label = QtWidgets.QLabel("Credit by Spel ©", self)
        self.credit_label.move(20, 420)
        
        #Credit by Spel 
        
        self.country_label = QtWidgets.QLabel("Wybierz kraj:", self)
        self.country_label.move(20, 20)
        
        self.country_dropdown = QtWidgets.QComboBox(self)
        self.country_dropdown.addItems(["pl_PL", "en_US", "de_DE", "fr_FR", "es_ES"])
        self.country_dropdown.move(150, 20)
        self.country_dropdown.currentTextChanged.connect(self.update_locale)

        self.records_label = QtWidgets.QLabel("Liczba rekordów:", self)
        self.records_label.move(20, 60)
        
        self.records_input = QtWidgets.QSpinBox(self)
        self.records_input.setRange(1, 10000)
        self.records_input.move(150, 60)

        self.columns_label = QtWidgets.QLabel("Kolumny:", self)
        self.columns_label.move(20, 100)
        
        self.columns_table = QtWidgets.QTableWidget(self)
        self.columns_table.setColumnCount(2)
        self.columns_table.setHorizontalHeaderLabels(["Nazwa kolumny", "Funkcja Faker"])
        self.columns_table.setGeometry(20, 130, 500, 200)
        
        self.add_column_button = QtWidgets.QPushButton("Dodaj kolumnę", self)
        self.add_column_button.move(550, 130)
        self.add_column_button.clicked.connect(self.add_column)

        self.remove_column_button = QtWidgets.QPushButton("Usuń kolumnę", self)
        self.remove_column_button.move(550, 170)
        self.remove_column_button.clicked.connect(self.remove_column)

        # Opcja autoinkrementacji ID
        self.id_checkbox = QtWidgets.QCheckBox("Auto ID", self)
        self.id_checkbox.move(20, 325)

        # Opcje zapisu
        self.save_label = QtWidgets.QLabel("Zapisz plik jako:", self)
        self.save_label.move(20, 350)

        self.save_dropdown = QtWidgets.QComboBox(self)
        self.save_dropdown.addItems(["CSV", "JSON", "SQL"])
        self.save_dropdown.move(150, 350)

        self.save_button = QtWidgets.QPushButton("Zapisz plik", self)
        self.save_button.move(550, 350)
        self.save_button.clicked.connect(self.save_file)

        self.generated_data = []

    def update_locale(self):
        locale = self.country_dropdown.currentText()
        self.fake = Faker(locale)
        
        #Credit by Spel 

    def add_column(self):
        row_count = self.columns_table.rowCount()
        self.columns_table.insertRow(row_count)

        col_name_item = QTableWidgetItem()
        self.columns_table.setItem(row_count, 0, col_name_item)

        faker_func_dropdown = QComboBox()
        faker_func_dropdown.addItems(self.get_faker_methods())
        self.columns_table.setCellWidget(row_count, 1, faker_func_dropdown)

    def remove_column(self):
        selected_row = self.columns_table.currentRow()
        if selected_row != -1:
            self.columns_table.removeRow(selected_row)

    def generate_data(self):
        self.generated_data = []
        num_records = self.records_input.value()
        columns = []

        if self.id_checkbox.isChecked():
            columns.append(("id", "auto_increment"))
        
        for row in range(self.columns_table.rowCount()):
            col_name_item = self.columns_table.item(row, 0)
            faker_func_widget = self.columns_table.cellWidget(row, 1)

            if col_name_item and faker_func_widget:
                col_name = col_name_item.text()
                faker_func = faker_func_widget.currentText()
                columns.append((col_name, faker_func))

        #Credit by Spel 

        for i in range(num_records):
            row_data = {}
            if self.id_checkbox.isChecked():
                row_data["id"] = i + 1
            for col_name, faker_func in columns:
                if col_name == "id":
                    continue
                try:
                    value = getattr(self.fake, faker_func)()
                except AttributeError:
                    value = "Invalid Function"
                row_data[col_name] = value
            self.generated_data.append(row_data)

    def save_file(self):
        self.generate_data()

        file_type = self.save_dropdown.currentText()
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Zapisz plik", "", f"{file_type} Files (*.{file_type.lower()});;All Files (*)", options=options)

        if not file_path:
            return

        if file_type == "CSV":
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.generated_data[0].keys())
                writer.writeheader()
                writer.writerows(self.generated_data)

        elif file_type == "JSON":
            with open(file_path, mode='w', encoding='utf-8') as file:
                json.dump(self.generated_data, file, indent=4)

        elif file_type == "SQL":
            conn = sqlite3.connect(file_path)
            cursor = conn.cursor()

            columns = self.generated_data[0].keys()
            table_name = "GeneratedData"
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([col + ' TEXT' for col in columns])})")

            for row in self.generated_data:
                placeholders = ", ".join(["?"] * len(row))
                cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", list(row.values()))

            conn.commit()
            conn.close()

        QtWidgets.QMessageBox.information(self, "Sukces", f"Plik zapisany jako {file_type}!")

    def get_faker_methods(self):
        methods = []
        for method in dir(self.fake):
            if not method.startswith("_"):
                try:
                    if callable(getattr(self.fake, method)):
                        methods.append(method)
                except TypeError:
                    pass
        return sorted(methods)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = DataGeneratorApp()
    mainWin.show()
    sys.exit(app.exec_())

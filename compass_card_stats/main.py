import tkinter as tk
from tkinter.filedialog import askopenfilenames
from compass_card_stats.models.Record import Record
import csv
from functools import reduce


def main():
    root = tk.Tk()
    root.withdraw()
    filenames = askopenfilenames(filetypes=[("CSV", "*.csv")])
    print("Selected file:", filenames)
    data = set()
    for filename in filenames:
        with open(filename, "r") as file:
            csv_reader = csv.reader(file)
            csv_reader.__next__()
            for row in csv_reader:
                data.add(Record.from_csv(*row))

    spent = reduce(lambda x, y: x + (y.amount if y.amount < 0 else 0), data, 0)
    print(spent)

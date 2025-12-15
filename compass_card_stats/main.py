import tkinter as tk
from tkinter.filedialog import askopenfilenames
from compass_card_stats.models.Record import Record
import csv
from functools import reduce
from collections import Counter

TRAVEL_EVENT_PREFIXES = ("Tap in at", "Tap out at", "Transfer at")


def event_count_stats(records: list[Record]) -> dict[str, str]:
    """Print event counts at stations/stops"""
    stop_labels = [
        record.transaction
        for record in records
        if record.transaction.startswith(TRAVEL_EVENT_PREFIXES)
    ]
    counts = Counter(stop_labels)
    return dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))


def cost_stats(records: list[Record]) -> float:
    return -reduce(
        lambda x, y: x + (y.amount if y.amount < 0 else 0), records, 0
    )


def main():
    root = tk.Tk()
    root.withdraw()
    filenames = askopenfilenames(filetypes=[("CSV", "*.csv")])
    print("Selected file:", filenames)
    records_raw: list[Record] = list()
    for filename in filenames:
        with open(filename, "r") as file:
            csv_reader = csv.reader(file)
            csv_reader.__next__()
            for row in csv_reader:
                records_raw.append(Record.from_csv(*row))
    records_deduplicated = list(dict.fromkeys(records_raw))

    spent = cost_stats(records_deduplicated)
    event_counts = event_count_stats(records_deduplicated)

    print(f"Spent: ${round(spent, 2)}")
    print("Visited:")
    for k, v in event_counts.items():
        print(f"{k}: {v}")

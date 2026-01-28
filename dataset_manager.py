import csv

class DatasetManager:
    def __init__(self):
        self.data = []    # lista wierszy z danych
        self.labels = []  # etykiety kolumn (jeśli istnieją)

    def load_csv(self, path, has_header=True):
        self.data = []
        self.labels = []

        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)

            for i, row in enumerate(reader):
                # pomijamy puste wiersze
                if not row:
                    continue

                if i == 0 and has_header:
                    self.labels = row
                else:
                    self.data.append(row)

    def print_labels(self):
        if not self.labels:
            print("Brak etykiet kolumn.")
        else:
            print("Etykiety kolumn:")
            for label in self.labels:
                print(label)
    def print_data(self, start=None, end=None):
        data_to_print = self.data

        if start is not None or end is not None:
            data_to_print = self.data[start:end]

        for row in data_to_print:
            print(row)

    def count_classes(self, class_index):
        counts = {}

        for row in self.data:
            cls = row[class_index]
            counts[cls] = counts.get(cls, 0) + 1

        return counts

    def filter_by_class(self, class_index, class_value):
        filtered = []

        for row in self.data:
            if row[class_index] == class_value:
                filtered.append(row)

        return filtered

    def split_data(self, train_pct, test_pct, val_pct):
        total = len(self.data)

        train_end = int(total * train_pct)
        test_end = train_end + int(total * test_pct)

        train = self.data[:train_end]
        test = self.data[train_end:test_end]
        val = self.data[test_end:]

        return train, test, val
    
    def save_csv(self, data, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)

            if self.labels:
                writer.writerow(self.labels)

            writer.writerows(data)

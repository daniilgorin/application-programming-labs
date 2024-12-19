import csv


class ImageIterator:
    def __init__(self, csv_file: str):
        self.csv_file = csv_file
        self.file = None
        self.reader = None

    def __iter__(self):
        self.file = open(self.csv_file, mode="r",newline="")
        self.reader = csv.reader(self.file)
        next(self.reader)
        return self

    def __next__(self):
        try:
            row = next(self.reader)
            return row

        except StopIteration:
            self.file.close()
            raise

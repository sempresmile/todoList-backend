from resources import Entry
import os


class EntryManager:
    def __init__(self, data_path):
        self.data_path = data_path
        self.entries = []

    def save(self):
        for entry in self.entries:
            entry.save(self.data_path)

    def load(self):
        if not os.path.isdir(self.data_path):
            os.makedirs(self.data_path)
        else:
            files_list = os.listdir(self.data_path)
            for file in files_list:
                if os.path.splitext(file)[1] == '.json':
                    file_path = os.path.join(self.data_path, file)
                    loaded_entry = Entry.load(file_path)
                    self.entries.append(loaded_entry)
        return self

    def add_entry(self, title):
        added_entry = Entry(title)
        self.entries.append(added_entry)
        return self


if __name__ == '__main__':
    grocery_list = Entry("my_list")
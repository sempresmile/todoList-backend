import json


def print_with_indent(value, indent=0):
    indentation = " " * indent
    print(indentation + str(value))

class Entry:
    def __init__(self, title, entries = None, parent = None):
        if entries is None:
            entries = []
        self.title = title
        self.entries = entries
        self.parent = parent

    def __str__(self):
        return self.title

    def add_entry(self, entry):
        self.entries.append(entry)
        entry.parent = self



    def print_entries(self, indent = 0):
        print_with_indent(self, indent)
        for entry in self.entries:
            entry.print_entries(indent + 1)

    def json(self):
        res = {
            'title': self.title,
            'entries': []
        }
        for entry in self.entries:
            res['entries'].append(entry.json())
        return res

    @classmethod
    def entry_from_json(cls, value: dict):
        new_entry = Entry(value['title'])
        for item in value.get('entries', []):
            new_entry.add_entry(cls.entry_from_json(item))
        return new_entry

    def save(self, path):
        entry_file = self.json()
        with open(f'{path}{self.title}.json', 'w') as file:
            json_file = json.dumps(entry_file, indent=2)
            file.write(json_file)

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as f:
            loaded_file = json.load(f)
        returned_entry = cls.entry_from_json(loaded_file)
        return returned_entry




if __name__ == '__main__':
    first = Entry("Groceries")
    second = Entry("Resto")
    first.add_entry(Entry("Bread"))
    first.add_entry(Entry("Milk"))
    first.add_entry(second)
    second.add_entry(Entry("Pizza"))
    res_json = first.json()


from flask import Flask, request
from entryManager import EntryManager
from resources import Entry

FOLDER = r'C:\Users\user\Documents\Tasks'

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/entries/")
def get_entries():
    entry_manager = EntryManager(FOLDER)
    entry_manager.load()
    new_list = []
    for entry in entry_manager.entries:
        new_list.append(entry.json())
    return new_list


@app.route("/api/save_entries/", methods=['POST'])
def save_entries():
    entry_manager = EntryManager(FOLDER)
    requested_json = request.get_json()
    for item in requested_json:
        entry_json = Entry.entry_from_json(item)
        entry_manager.entries.append(entry_json)
        entry_manager.save()
    return 'status: success'


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False)
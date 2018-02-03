from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://admin2:admin2@ds121898.mlab.com:21898/mangohacks')
db = client['mangohacks']

test = db['test']
prod = db['prod']

test_doc = {
	"author": "aimee"
}

@app.route("/")
def hello():
	name = test.find_one()
	return jsonify(str(name))

@app.route("/insert")
def insert():
	doc_cursor = test.insert_one(test_doc)
	doc_id = doc_cursor.inserted_id
	print(doc_cursor)
	print(doc_id)
	return "good"

@app.route("/drawerUpdate", methods=['POST'])
def drawer_update():
    print(request.args)
    json_data = dict()
    json_data['isOpen'] = request.args.get('isOpen')
    json_data['ts'] = request.args.get('ts')
    print(json_data)
    doc_cursor = prod.insert_one(json_data)
    doc_id = doc_cursor.inserted_id
    print(doc_cursor)
    print(doc_id)
    return "good"


if __name__ == "__main__":
	app.run()

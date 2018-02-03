from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://admin2:admin2@ds121898.mlab.com:21898/mangohacks')
db = client['mangohacks']

test = db['test']

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



if __name__ == "__main__":
	app.run()

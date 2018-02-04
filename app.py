from flask import Flask, request
from pymongo import MongoClient
import json

app = Flask(__name__)
client = MongoClient('mongodb://admin2:admin2@ds121898.mlab.com:21898/mangohacks')
db = client['mangohacks']

test = db['test']
med_logs = db['med_logs']
drawer_logs = db['drawer_logs']
my_meds = db['my_meds']

test_doc = {
	"author": "aimee"
}

@app.route("/")
def hello():
	name = test.find_one()
	return json.dumps(str(name))

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
    json_data['isOpen'] = request.form.get('isOpen')
    json_data['ts'] = request.form.get('ts')
    json_data['owner'] = request.form.get('owner')
    print(json_data)
    doc_cursor = drawer_logs.insert_one(json_data)
    doc_id = doc_cursor.inserted_id
    print(doc_cursor)
    print(doc_id)
    return "good"


@app.route("/medicineUsed", methods=['POST'])
def medicine_update():
    json_data = dict()
    json_data['medicinesUsed'] = request.form.get('medicinesUsed')
    json_data['numUsed'] = request.form.get('numUsed')
    json_data['ts'] = request.form.get('ts')
    json_data['owner'] = request.form.get('owner')
    print(json_data)
    doc_cursor = med_logs.insert_one(json_data)
    doc_id = doc_cursor.inserted_id
    print(doc_cursor)
    print(doc_id)
    return "good"

@app.route("/userMeds", methods=["GET"])
def get_user_meds():
    my_meds_list = my_meds.find_one()
    return json.dumps(str(my_meds_list))    
if __name__ == "__main__":
	app.run()

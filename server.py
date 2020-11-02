from flask import Flask
from flask import jsonify, request
import socket

from Db import DbHandler
import argparse

app = Flask(__name__)

@app.route("/total_number_of_bugs", methods=['GET'])
def get_total_number_of_bugs():
    db_instance = DbHandler.get_instance()
    number_of_bugs = db_instance.get_total_number_of_bugs()

    return f"Total number of bugs are: {number_of_bugs}", 200

@app.route("/add_new_bug", methods=['POST'])
def add_new_bug():
    entry = request.form["entry"]
    if entry is None:
        return jsonify(message="You need to provide some data."), 400

    db_instance = DbHandler.get_instance()
    db_instance.add_new_bug(entry)
    return jsonify(message="Entry successfully saved"), 200

@app.route("/all_bugs_created_on", methods=['GET'])
def get_all_bugs_created_on():
    db_instance = DbHandler.get_instance()
    bugs_created_on = str(db_instance.get_all_bugs_created_on(request.args['created_on']))

    return bugs_created_on, 200

@app.route("/all_bugs_created_in_range", methods=['GET'])
def get_all_bugs_created_in_range():
    db_instance = DbHandler.get_instance()
    bugs_created_in_range = str(db_instance.get_all_bugs_created_in_range(request.args['range_from'],request.args['range_to']))

    return bugs_created_in_range, 200

@app.route("/all_bugs_reported_by", methods=['GET'])
def get_all_bugs_reported_by():
    db_instance = DbHandler.get_instance()
    bugs_reported_by = str(db_instance.get_all_bugs_reported_by(request.args['reported_by']))

    return bugs_reported_by, 200\

@app.route("/all_bugs_assigned_to", methods=['GET'])
def get_all_bugs_assigned_to():
    db_instance = DbHandler.get_instance()
    bugs_assigned_to = str(db_instance.get_all_bugs_assigned_to(request.args['assigned_to']))

    return bugs_assigned_to, 200

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--database-name', default='database.txt')
    parser.add_argument('--server-port', default=5000, type=int)
    args = parser.parse_args()

    DbHandler(args.database_name)
    with open('server_port.txt',"w") as port:
        port.write(str(args.server_port))

    app.run(host='0.0.0.0', port=args.server_port)
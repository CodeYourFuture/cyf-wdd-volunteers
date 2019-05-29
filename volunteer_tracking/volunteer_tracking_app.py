import json

from flask import Flask, request, Response
app = Flask(__name__)

from volunteer_tracking.db_actions import insert_new_volunteer


@app.route("/create_volunteer/", methods=["POST"])
def create_volunteer():
    volunteer_data = json.loads(request.data)
    insert_new_volunteer(volunteer_data)
    resp = Response("New volunteer recorded!", status=200)

    return resp

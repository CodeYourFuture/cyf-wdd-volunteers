import json
from flask import Flask, request, Response
app = Flask(__name__)

from volunteer_tracking.db_actions import insert_new_volunteer, fetch_volunteers

# @TODO test this method


@app.route("/create_volunteer/", methods=['GET', 'POST'])
def create_volunteer(event):
    if request.method == 'POST':
        body = event['body']
        volunteer_data = json.loads(body).get('volunteer')
        insert_new_volunteer(volunteer_data)

        return Response("New volunteer recorded!", status=200)
    if request.method == 'GET':
        return Response(json.dumps(fetch_volunteers(request.args)), status=200)

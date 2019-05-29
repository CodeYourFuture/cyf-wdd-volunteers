import json

from flask import Flask
app = Flask(__name__)

from volunteer_tracking.db_actions import insert_new_volunteer


@app.route("/create_volunteer/")
def create_volunteer(event):
    print(event)
    body = event['body']
    volunteer_data = json.loads(body).get('volunteer')
    insert_new_volunteer(volunteer_data)

    return {
        'statusCode': 200,
        'body': json.dumps('New volunteer recorded!')
    }

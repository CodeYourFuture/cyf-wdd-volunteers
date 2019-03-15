import json
from db_actions import insert_new_volunteer

def lambda_handler(event, context):
    print(event)
    body = event['body']
    volunteer_data = json.loads(body).get('volunteer')
    insert_new_volunteer(volunteer_data)

    return {
        'statusCode': 200,
        'body': json.dumps('New volunteer recorded!')
    }

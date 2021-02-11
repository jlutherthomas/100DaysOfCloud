import requests
import json
def hello_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = event
    print('Bucket: {}'.format(event['bucket']))
    print('File: {}'.format(event['name']))

    final_url=' INSERT WEBHOOK URL HERE'
    headers = {'content-type': 'application/json'}
    payload = {'Bucket': event['bucket'], 'File': event['name']}
    data=json.dumps(payload)
    response = requests.post(final_url, data=data, headers=headers)
    print("JSON payload", data)
    print("Response text",response.text)
    print("Response status", response.status_code, response.reason)
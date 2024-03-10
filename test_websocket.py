import requests
import json

def register_user(id):
    url = 'http://localhost:8000/register'
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({'user_id': id, 'topic': 'hello'})  # You can replace 123 with the desired user_id

    response = requests.post(url, headers=headers, data=data)
    return response.json()  # Assuming the response contains the WebSocket URL

def add_topic(id, topic):
    url = 'http://localhost:8000/add_topic'
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({'client_id': id, 'topic': topic})

    response = requests.post(url, headers=headers, data=data)
    return response.status_code

def publish_message(user_id, topic, message):
    url = 'http://localhost:8000/publish'
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({'topic': topic, 'user_id': user_id, 'message': message})

    response = requests.post(url, headers=headers, data=data)
    return response.status_code

if __name__ == "__main__":
    id = 3
    # Register user and get WebSocket URL
    register_response = register_user(id)
    ws_url = register_response['url']
    print(ws_url)

    # Add topic
    topic = 'new_topic'
    #add_topic_response = add_topic(id, topic)
    #print('Add topic response:', add_topic_response)

    # Publish message
    message = 'Hello, World!'
    publish_response = publish_message(id, topic, message)
    print('Publish message response:', publish_response)

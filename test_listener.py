import requests
import json
import websocket

def register_user(id):
    url = 'http://localhost:7777/register'
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({'user_id': id, 'topic': 'nextflow'})

    response = requests.post(url, headers=headers, data=data)
    return response.json()  # Assuming the response contains the WebSocket URL

def on_message(ws, message):
    print("Received message:", message)

if __name__ == "__main__":
    user_id = 3
    # Register user and get WebSocket URL
    register_response = register_user(user_id)
    ws_url = register_response['url']
    print("WebSocket URL:", ws_url)

    # Connect to WebSocket
    ws = websocket.WebSocketApp(ws_url, on_message=on_message)
    ws.run_forever()

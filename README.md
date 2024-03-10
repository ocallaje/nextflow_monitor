# warp-websockets-example
Basic example using websockets with warp in Rust

## Development
Run with

```bash
make dev
```

## Docker Deployment
```bash
chmod +x build.sh
./build.sh
docker run --restart=always ocallaje/nextflow_monitor
```

### Clients
Then, you can register/unregister a client and to a specific topic using HTTP requests:

```bash
curl -X POST 'http://localhost:8000/register' -H 'Content-Type: application/json' -d '{ "user_id": 1, "topic": "mytopic" }' 

curl -X DELETE 'http://localhost:8000/register/e2fa90682255472b9221709566dbceba' 
```

Registration will return a websocket URL. Use this to connect to the WebSocket e.g.
Bash:
```bash
`websocat ws://127.0.0.1:8000/ws/625ac78b88e047a1bc7b3f8459702078`
```

Then, you can publish messages to websocket-connected clients using HTTP requests
Bash:
```bash
curl -X POST 'http://localhost:8000/publish' \
    -H 'Content-Type: application/json' \
    -d '{"user_id": 1, "topic": "cats", "message": "are awesome"}'
```

Python: 
```bash
def publish_message(user_id, topic, message):
    url = 'http://localhost:8000/publish'
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({'user_id': user_id, 'topic': topic, 'message': message})

    response = requests.post(url, headers=headers, data=data)
    #response.raise_for_status()
    return response.status_code
```
To publish messages using Postman, you can follow these steps:

Open Postman and create a new request.
Set the request method to POST.
Enter the URL of the publish endpoint in the request URL field (e.g., http://localhost:8000/publish).
Set the request headers to specify the content type as JSON. Add a header with key Content-Type and value application/json.
In the request body tab, select the raw option and choose JSON from the dropdown menu.
Enter the JSON payload for the message you want to publish. The payload should include the user_id, topic, and message fields.
Click the Send button to send the request.
Here's an example of how you can structure the JSON payload:

json
```bash
{
    "user_id": 1,
    "topic": "your_topic_here",
    "message": "your_message_here"
}
```
Replace your_topic_here with the desired topic and your_message_here with the message you want to publish.

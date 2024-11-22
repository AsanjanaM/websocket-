
import asyncio
import websockets
import json

async def mock_server(websocket, path):
    questions = [
        {"id": 1, "question": "Explain supervised learning."},
        {"id": 2, "question": "Describe the components of a neural network."},
        {"id": 3, "question": "What are AI ethics?"}
    ]
    for question in questions:
        await websocket.send(json.dumps(question))
        try:
            response = await asyncio.wait_for(websocket.recv(), timeout=10)
            print(f"Received response: {response}")
        except asyncio.TimeoutError:
            print("Timeout waiting for client response.")

start_server = websockets.serve(mock_server, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

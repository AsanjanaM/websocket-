
import asyncio
import websockets
import json
from cachetools import TTLCache

cache = TTLCache(maxsize=100, ttl=300)

def generate_feedback(response):
    score = len(response) % 10
    feedback = "Great job!" if score > 7 else "Needs improvement."
    return {"score": score, "feedback": feedback}

async def websocket_client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            prompt = await websocket.recv()
            question_data = json.loads(prompt)

            question_id = question_data["id"]
            question = question_data["question"]
            print(f"Processing question: {question}")

            response = f"Sample response for {question}"
            cache[question_id] = response

            feedback = generate_feedback(response)
            feedback_message = {
                "id": question_id,
                "response": response,
                "feedback": feedback,
            }
            await websocket.send(json.dumps(feedback_message))

asyncio.get_event_loop().run_until_complete(websocket_client())

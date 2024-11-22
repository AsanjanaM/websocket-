
import pytest
from cachetools import TTLCache

def generate_feedback(response):
    score = len(response) % 10
    feedback = "Great job!" if score > 7 else "Needs improvement."
    return {"score": score, "feedback": feedback}

def test_generate_feedback():
    response = "This is a good response."
    feedback = generate_feedback(response)
    assert feedback["score"] >= 0
    assert feedback["score"] <= 10

def test_response_caching():
    cache = TTLCache(maxsize=100, ttl=300)
    cache[1] = "Response 1"
    assert cache[1] == "Response 1"

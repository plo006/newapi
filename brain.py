from features.wikipedia_search import search_wikipedia
from features.weather import get_weather
from features.web_search import web_search
from features.knowledge_base import get_smart_response

def get_response(user_input):
    user_input_lower = user_input.lower()

    # Wikipedia search detection
    if any(word in user_input_lower for word in [
        "who is", "what is", "tell me about", "define", "explain",
        "meaning of", "describe", "information about", "history of", "what"
    ]):
        return search_wikipedia(user_input)

    # Weather-related query
    if "weather" in user_input_lower or "temperature" in user_input_lower:
        return get_weather(user_input)

    # Web search fallback
    if "search" in user_input_lower or "google" in user_input_lower:
        return web_search(user_input)

    # Smart response based on detected language
    return get_smart_response(user_input)

# mood_responses.py

def mood_response(mood):
    mood_dict = {
        'happy': "That's great to hear! Keep smiling!",
        'sad': "I'm sorry to hear that. I hope things get better soon.",
        'excited': "Awesome! What are you excited about?",
        'angry': "Take a deep breath. It's going to be okay.",
        'anxious': "It's alright to feel anxious sometimes. Try to relax and take it easy.",
        'tired': "Get some rest. You deserve it.",
        'bored': "Why not try something new or pick up a hobby?",
    }
    
    return mood_dict.get(mood.lower(), "I don't know that mood, but I hope you have a good day!")


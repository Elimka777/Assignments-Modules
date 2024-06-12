# main.py
import mood_responses

mood = input("How are you feeling today? ")
response = mood_responses.mood_response(mood)
print(response)

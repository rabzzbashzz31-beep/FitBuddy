import google.generativeai as genai
import os
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_workout_gemini(user_goal, user_intensity):
    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = f"You are a fitness trainer. Create a 7-day workout plan for goal {user_goal} with {user_intensity} intensity. Include Warm-up, Main workout with sets/reps, and Cooldown tip day-wise."
    response = model.generate_content(prompt)
    return response.text

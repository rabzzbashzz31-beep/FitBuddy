from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse
from gemini_generator import generate_workout_gemini

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def home():
    return "<h1>FitBuddy</h1><form method='post' action='/generate'><input name='goal' placeholder='Goal'><input name='intensity' placeholder='Intensity'><button>Generate</button></form>"

@router.post("/generate")
def generate(goal: str = Form(...), intensity: str = Form(...)):
    plan = generate_workout_gemini(goal, intensity)
    return HTMLResponse(f"<h2>Your Plan</h2><pre>{plan}</pre><a href='/'>Back</a>")

# app/main.py (incluir no início do arquivo)
from .database import engine, metadata
from .models import questions, scores

metadata.create_all(engine)


# app/main.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from .database import engine, metadata
from .models import questions, scores
import databases
import datetime

app = FastAPI()

# Montar pastas estáticas
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Configurar templates
templates = Jinja2Templates(directory="app/templates")

# Conectar ao banco de dados usando databases
database = databases.Database("sqlite:///./questions.db")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/quiz", response_class=HTMLResponse)
async def quiz(request: Request):
    # Atualizado para a sintaxe correta do select
    query = select(questions)
    results = await database.fetch_all(query)
    return templates.TemplateResponse("question.html", {"request": request, "questions": results})

@app.post("/submit", response_class=HTMLResponse)
async def submit(request: Request, answers: str = Form(...)):
    import json
    answers = json.loads(answers)
    
    # Atualizado para a sintaxe correta do select
    query = select(questions)
    results = await database.fetch_all(query)
    
    score = 0
    feedback = []
    for q in results:
        q_id = str(q['id'])
        user_answer = answers.get(q_id, "")
        correct = q['correct_option']
        if user_answer.upper() == correct.upper():
            score += 1
        else:
            feedback.append({
                "question": q['question'],
                "your_answer": user_answer,
                "correct_answer": correct
            })
    
    # Salvar score
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    query = scores.insert().values(score=score, timestamp=timestamp)
    await database.execute(query)
    
    # Obter todos os scores para o gráfico
    query = select(scores)
    all_scores = await database.fetch_all(query)
    scores_data = [s['score'] for s in all_scores]
    
    return templates.TemplateResponse("result.html", {
        "request": request,
        "score": score,
        "total": len(results),
        "feedback": feedback,
        "scores_data": scores_data
    })

from typing import Annotated

from fastapi import FastAPI, Depends
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.staticfiles import StaticFiles
from app.dependencies.nlq import nql_agent_factory, NlqAgent

app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")


@app.get('/')
def home():
    return RedirectResponse("/static/index.html")


@app.get('/api/prompt', response_class=HTMLResponse)
def prompt(text: str, agent: Annotated[NlqAgent, Depends(nql_agent_factory)]):
    return agent.prompt(text)

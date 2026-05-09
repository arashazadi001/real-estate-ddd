# main.py

from fastapi import FastAPI
from app.infrastructure.bootstrap import bootstrap_app
from app.application.mediator.mediator import mediator
from app.application.behaviors.logging_behavior import LoggingBehavior

app = FastAPI()

# ۱. راه‌اندازی زیرساخت (ثبت خودکار همه هندلرها)
bootstrap_app()

# ۲. ثبت رفتارهای سراسری (Pipelines)
mediator.add_behavior(LoggingBehavior())

@app.get("/")
async def root():
    return {"message": "Clean Architecture API is running"}

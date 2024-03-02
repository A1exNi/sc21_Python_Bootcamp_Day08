from fastapi import FastAPI
from pydantic import BaseModel
import uuid
import asyncio
import httpx
from random import random


class Urls(BaseModel):
    urls: list


class Task(BaseModel):
    status: str
    id: uuid.UUID
    result: list = None


app = FastAPI()


@app.get('/api/v1/tasks/{received_task_id}')
async def send_get(urls: Urls, received_task_id):
    resp = Task(
        status='ready',
        id=received_task_id
    )
    return resp


@app.post('/api/v1/tasks/', status_code=201)
def read_rood(urls: Urls):
    resp = Task(
        status='running',
        id=uuid.uuid4()
    )
    # asyncio.run(send_get(urls))
    return resp

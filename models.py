from pydantic import BaseModel, conlist
from typing import List
from fastapi import FastAPI


class Iris(BaseModel):
    data: List[int]
        
app = FastAPI(title="ML model as API", description="With FastAPI and Colab")

model = None

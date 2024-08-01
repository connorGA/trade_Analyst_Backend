from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict 

app = FastAPI()

class Player(BaseModel):
    name: str
    team: str
    position: str
    past_performance: Dict[str, float]


class TradeRequest(BaseModel):
    team1: List[Player]
    team2: List[Player]


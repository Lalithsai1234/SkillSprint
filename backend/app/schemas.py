# app/schemas.py

from pydantic import BaseModel, ConfigDict # <-- Import ConfigDict
from typing import List, Optional

# --- Challenge Schemas ---
class ChallengeBase(BaseModel):
    title: str
    category: str
    question: str

class ChallengeCreate(ChallengeBase):
    answer: str

class Challenge(ChallengeBase):
    id: int

    # This is the new Pydantic V2 syntax
    model_config = ConfigDict(from_attributes=True)

# --- Submission Schema ---
class Submission(BaseModel):
    answer: str

# --- User Schemas ---
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    xp: int
    streak: int

    # This is the new Pydantic V2 syntax
    model_config = ConfigDict(from_attributes=True)

# --- Token Schema ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
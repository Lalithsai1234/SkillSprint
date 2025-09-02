from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import crud, models, schemas
from app.database import get_db
from app.security import get_current_active_user

router = APIRouter()

@router.get("/", response_model=List[schemas.Challenge])
def read_challenges(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve challenges.
    """
    challenges = crud.get_challenges(db, skip=skip, limit=limit)
    return challenges

@router.post("/{challenge_id}/submit")
def submit_challenge_answer(
    challenge_id: int,
    submission: schemas.Submission,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user),
):
    """
    Submit an answer for a challenge.
    """
    # MODIFIED: Pass the answer string from the submission object, not the object itself.
    result = crud.handle_submission(
        db=db,
        user=current_user,
        challenge_id=challenge_id,
        submitted_answer=submission.answer
    )
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

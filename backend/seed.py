from app.database import SessionLocal, engine
from app.models import Challenge, Base

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Get a new database session
db = SessionLocal()

# --- Sample Challenges ---

challenges_to_add = [
    Challenge(
        title="Python List Slicing",
        question="What is the output of `my_list = [10, 20, 30, 40, 50]` followed by `print(my_list[1:3])`?",
        category="Coding",
        answer="[20, 30]"
    ),
    Challenge(
        title="Capital of France",
        question="What is the capital city of France?",
        category="General Knowledge",
        answer="Paris"
    ),
    Challenge(
        title="Simple Math Puzzle",
        question="If you have a pie with 8 slices and you eat 3, what fraction of the pie is left?",
        category="Math",
        answer="5/8"
    ),
    Challenge(
        title="HTML Tag for Links",
        question="Which HTML tag is used to create a hyperlink?",
        category="Coding",
        answer="<a>"
    )
]

try:
    # Check if challenges already exist to avoid duplicates
    existing_titles = {c.title for c in db.query(Challenge).all()}
    
    new_challenges = [
        c for c in challenges_to_add if c.title not in existing_titles
    ]

    if new_challenges:
        db.add_all(new_challenges)
        db.commit()
        print(f"Successfully added {len(new_challenges)} new challenges to the database.")
    else:
        print("Challenges already exist in the database. No new challenges were added.")

except Exception as e:
    print(f"An error occurred: {e}")
    db.rollback()

finally:
    db.close()

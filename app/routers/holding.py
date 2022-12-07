from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from .. import schemas, models
from ..database import get_db

router = APIRouter()

# SELECT * FROM holdingitems ORDER BY holding DESC NULLS LAST LIMIT 10; (query that gets the top 10 companies)

@router.post("/holders")
def validate_holders(data: schemas.HolderData, db: Session = Depends(get_db)):

    # Data received as lists, has to be broken into single values and sent to database as HoldingItem Model
    for index, ticker in enumerate(data.company):
        new_item = models.HoldingItem(id=index, company=ticker, holding=data.holding[index])
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    
    return {"Hello": "World"}
import uvicorn
from fastapi import FastAPI, Depends
from sqlmodel import Session, select, SQLModel
from db import get_session
from models.category import Category
from models.product import Product

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Product Catalog API"}


def create_generic(model):
    def create(item: model, session: Session = Depends(get_session)):
        session.add(item)
        session.commit()
        session.refresh(item)
        return item
    return create

def read_generic(model):
    def read(item_id: int, session: Session = Depends(get_session)):
        return session.get(model, item_id)
    return read

def update_generic(model):
    def update(item_id: int, item: model, session: Session = Depends(get_session)):
        db_item = session.get(model, item_id)
        if db_item:
            item_data = item.model_dump(exclude_unset=True)
            for key, value in item_data.items():
                setattr(db_item, key, value)
            session.add(db_item)
            session.commit()
            session.refresh(db_item)
            return db_item
        return {"error": f"{model.__name__} with id {item_id} not found"}
    return update

def delete_generic(model):
    def delete(item_id: int, session: Session = Depends(get_session)):
        item = session.get(model, item_id)
        if item:
            session.delete(item)
            session.commit()
        return {"ok": True}
    return delete

# Category CRUD
app.post("/categories/")(create_generic(Category))
app.get("/categories/{item_id}")(read_generic(Category))
app.put("/categories/{item_id}")(update_generic(Category))
app.delete("/categories/{item_id}")(delete_generic(Category))

# Product CRUD
app.post("/products/")(create_generic(Product))
app.get("/products/{item_id}")(read_generic(Product))
app.put("/products/{item_id}")(update_generic(Product))
app.delete("/products/{item_id}")(delete_generic(Product))
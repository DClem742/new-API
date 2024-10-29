from sqlmodel import SQLModel, create_engine, Session
DATABASE_URL = "postgresql://postgres.bveaeajkjyrnfjvhctcx:Sumerian5588!*@aws-0-us-west-1.pooler.supabase.com:6543/postgres"

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

if __name__ == "__main__":
    create_db_and_tables()

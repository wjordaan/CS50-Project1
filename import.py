import csv
import os

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    print("read")
    reader = csv.reader(f)
    next(reader)

    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                    {"isbn":isbn, "title":title, "author":author, "year":year})
        print(f"Added title: {title}")
    db.commit()

if __name__ == "__main__":
    main()
from sqlalchemy import create_engine, text
import os
con_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(con_string)


def load_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))

    return jobs

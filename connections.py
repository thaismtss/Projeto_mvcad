import psycopg2
from psycopg2.extras import RealDictCursor

db = psycopg2.connect("dbname=mvcad-cursos user=postgres password=123456 "
                      "host=localhost")
db.autocommit = True
cursor = db.cursor()
cursor = db.cursor(cursor_factory=RealDictCursor)

import sqlalchemy as db
engine = db.create_engine('sqlite:///foo.db')


from sqlalchemy import Table, Column, Integer, String, MetaData
meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String), 
)

ins = students.insert().values(name = 'Ravi', lastname = 'Kapoor')
conn = engine.connect()
result = conn.execute(ins)
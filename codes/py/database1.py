import sqlite3
a=sqlite3.connect("app.db")
b=a.cursor()
b.execute("create table if not exists users (name text ,id integer)")
b.execute("create table if not exists skills (name text ,pro integer,id integer)")
l=["ali","ahmed","mohamed","sad"]
# for i ,j in enumerate(l):
#      b.execute(f"insert into users (id ,name) values({i},'{j}')")
# b.execute("insert into users ( id,name) values(1,'ahmed')")
# b.execute("insert into users ( id,,name) values(2,'ali')")
# b.execute("insert into users ( d,name) values(3,'mohamed')")
b.execute("update users set name ='haseen' where id =2")
b.execute("delete from users where id =2")
b.execute("select name,id from users")
# print(b.fetchall())
# b.execute("delete from users")
print(b.fetchone())
print(b.fetchone())
print(b.fetchone())
print(b.fetchone())

a.commit()
# a.execute("create table if not exists s (name text,pro integer ,id integer)")
a.close()



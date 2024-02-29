import sqlite3 as sql

db = sql.connect('Uy_ishi')

cursor = db.cursor()

cursor.executescript('''
drop table if exists categories
drop table if exists products

create table if not exists categories(
    id integer primary key autoincrement
);

create table if not exists products(
    product_name varchar(20),            
    product_id references categories(id),    
    soni integer,
    narx integer
);
''')
cursor.executescript('''
insert into products(product_name,soni,narx)
values(sut, 5, 10);

insert into products(product_name,soni,narx)
values(qora_xleb, 10, 5);

insert into products(product_name,soni,narx)
values(pepsi, 15, 20);

insert into products(product_name,soni,narx)
values(non, 40, 3);

insert into products(product_name,soni,narx)
values(shokolad, 5, 18);

insert into products(product_name,soni,narx)
values(makaron, 23, 30);

insert into products(product_name,soni,narx)
values(mineral_suv, 2, 70);

insert into products(product_name,soni,narx)
values(qatiq, 8, 34);
''')

cursor.execute('''
select max(soni) from products 
''')

db.commit()
db.close()

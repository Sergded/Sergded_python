from flask import Flask, request
import psycopg2


app = Flask(__name__)
conn = psycopg2.connect(dbname='sergded',user='postgres',password='')

POSTS = [{
    'Name':'Сергей',
    'Date':'01.09.2023',
    'Text':'Привет! Меня зовут Сергей!'
},
{
    'Name':'Ольга',
    'Date':'10.07.2013',
    'Text':'Хочу рассказать вам интересную историю'
},
{
    'Name':'Глеб',
    'Date':'28.11.2018',
    'Text':'Здесь очень интересно!'
}
]

@app.get("/users")
def get_post():
    return POSTS

def get_user():
    Name = request.args['Name']
    new_users=[]
    for user in POSTS:
        if user['Name']==Name:
            new_users.append(user)
    return new_users


@app.post("/users")
def create_post():
    name = request.form.get('Name')
    date = request.form.get('Date')
    text = request.form.get('Text')
    print(f"Name:{name} Date:{date} Text:{text}")
    return 'User created'


@app.post("/users")
def create_users():
    cursor=conn.cursor()
    name = request.form.get('name')
    age = request.form.get('age')
    sql_create_database = f"insert into family(name, age) values('{name}',{age})"
    cursor.execute(sql_create_database)
    conn.commit()
    return 'User created'


@app.route("/users/<user_id>", methods=['PUT'])
def update_users(user_id):
    name = request.form.get('name')
    age = request.form.get('age')
    cursor = conn.cursor()
    sql_create_database = f"update family set name='{name}', age={age} where id = {user_id};"
    cursor.execute(sql_create_database)
    conn.commit()
    return 'User update'

@app.route("/users", methods=['GET'])
def get_users_list():
    filter = request.args.get('filter')
    limit = request.args.get('limit')
    cursor = conn.cursor()
    sql_create_database = f'select * from family where {filter} limit {limit};'
    cursor.execute(sql_create_database)
    rows = cursor.fetchall()
    print(rows)
    return 'print list with filter'

@app.route("/users/<user_id>", methods=['DELETE'])
def delete_users(user_id):
    cursor = conn.cursor()
    sql_create_base = f'delete from family where id = {user_id}'
    cursor.execute(sql_create_base, (int(user_id)))
    conn.commit()
    return 'User deleted'
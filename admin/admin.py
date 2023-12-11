import sqlite3

from flask import Blueprint, request, g, current_app

from to_remove import FDataBase

admin: Blueprint = Blueprint("admin", __name__, static_folder="static", template_folder="template")
db: sqlite3.Connection
# db = None


def connect_db():
    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    return conn


def get_db():
    if not hasattr(g, "link_db"):
        g.link_db = connect_db()
    return g.link_db



@admin.before_request
def before_request():
    global db
    # db = g.get("link_db")
    db = connect_db()
    db.cursor().execute('''SELECT * FROM users''')
    res = db.cursor().fetchall()
    print(res)
    print(db)


@admin.teardown_request
def close_db(error):
    global db
    db = None
    return request


@admin.route("/")
def index():
    return "admin"


@admin.route("/users")
def users():
    print(db)
    # sql = '''SELECT * FROM users'''
    try:
        # db.cursor().execute(sql)
        res = [dict(item) for item in FDataBase.FDataBase(get_db()).getUsers()]
        print(res)
        if res:
            return res
    except sqlite3.Error as e:
        print("error: ", e)

    return "no users"


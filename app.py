from flask import Flask, render_template, url_for, g, request, redirect, make_response, session
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask_admin import Admin, AdminIndexView, BaseView
from flask_admin.contrib.sqla import ModelView

from forms import LoginForm, RegisterForm
from User import UserLogin
from werkzeug.security import generate_password_hash, check_password_hash
# from admin.admin import admin
from models import User, Profile
from models import db


DATABASE = "flsite.db"
DEBUG = True
SECRET_KEY = "n458dhg54y8drg5h4u32o*a%*&#%&4"

app = Flask(__name__)
app.config.from_object(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
# app.config.update(dict(DATABASE=os.path.join(app.root_path, "flsite.db")))
# app.register_blueprint(admin, url_prefix="/admin")

login_manager = LoginManager(app)
login_manager.login_view = "login"

# db = SQLAlchemy()
# db_: FDataBase
db.init_app(app)

admin = Admin(app, name="flask-app", template_mode="bootstrap4", index_view=AdminIndexView(name="Home"))
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Profile, db.session))


# def connect_db():
#     conn = sqlite3.connect(app.config["DATABASE"])
#     conn.row_factory = sqlite3.Row
#     return conn
#
#
# def create_db():
#     db = connect_db()
#     with app.open_resource("sq_db.sql", "r") as f:
#         db.cursor().executescript(f.read())
#
#     db.commit()
#     db.close()
#
#
# def get_db():
#     if not hasattr(g, "link_db"):
#         g.link_db = connect_db()
#     return g.link_db


@app.before_request
def before_request():
    # print(request.path)
    # print(url_for("login"))
    # global db
    # db = FDataBase(get_db())

    # print(db.getUsers())

    if current_user.is_authenticated and request.path in [url_for("login"), url_for("register"), url_for("forget_password")]:
        return redirect(url_for("profile"))


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "link_db"):
        g.link_db.close()


@app.errorhandler(401)
def error(e):
    return "error: message", 401


@app.errorhandler(404)
def error_404(e):
    return render_template("error.html", error=e), 404


@app.route('/testPage')
def test_page():
    # print([i for i in db.getUsers()])
    # print(request.values)
    # res = make_response(render_template('test-page.html', data=db.getUsers(), cookies=request.cookies))
    # res.set_cookie("test-cookie", "cookie value", 30*24*3600)
    session.permanent = True
    session["test-session"] = "session-data"
    session.modified = True
    # print(User.query.all())
    # print(User.query.get(1))
    # print(User.query.get(1).username)
    # user = User.query.filter_by(username="parsyan_066").first_or_404()
    # print(User(username="parsyan_066"))
    # print(user)
    print(db.session.query(User).filter_by(username="parsyan_066").first_or_404())

    return render_template('test-page.html', data=User.query.all())


@app.route("/register-user", methods=["POST"])
def add_user():
    print(dict(request.form))
    print(request.data)
    # db.addUser(form.first_name.data +" "+ form.last_name.data, form.email.data , form.gender.data , form.birthday.data , form.address.data , form.username.data , form.password.data , generate_password_hash(form.password_repeat.data ), form.phone_number.data )
    return redirect(url_for("login"))


@login_manager.user_loader
def load_user(user_id):
    print("load user")
    u = UserLogin().fromDB(user_id=user_id, db=db)
    return u


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/groups')
def groups():
    return render_template('groups.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    # db = FDataBase(get_db())
    form = LoginForm()

    if request.method == "POST":
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first_or_404()
            print(user)

            if user and check_password_hash(user.password, form.password.data):
                user_login = UserLogin(user)
                login_user(user_login, form.rememberme.data)
                return redirect(request.args.get("next") or url_for("profile"))
    print(form.errors)
    return render_template('login.html', form=form)


@app.route('/forget-password')
def forget_password():
    return render_template('register.html')


@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User(
                email=form.email.data,
                full_name=form.first_name.data + " " + form.last_name.data,
                gender=form.gender.data,
                birthday=form.birthday.data,
                address=form.address.data,
                username=form.username.data,
                password=generate_password_hash(form.password.data),
                phone_number=form.phone_number.data
            )

            db.session.add(user)
            db.session.flush()
            db.session.commit()

            return redirect(url_for("login"))
    print(form.errors)
    return render_template('register.html', form=form)


@app.route("/userava")
@login_required
def userava():
    img = current_user.get_avatar(app)
    if img:
        return ""

    res = make_response(img)
    res.headers["Content-Type"] = "image/png"
    return res


@app.route("/upload", methods=["POST"])
def update_profile_data():
    file = request.files["file"]

    if file and current_user.verify_ext(file.filename):
        try:
            img = file.read()
            res = db.update_user_avatar(img, current_user.get_id())
        except Exception as e:
            print(e)
    return redirect(url_for("profile"))


@app.route('/profile')
@login_required
def profile():
    print(current_user.user)
    return render_template('profile.html', user=current_user.user)


@app.route('/profile/<action>')
@login_required
def profile_action(action):
    if action == "edit":
        print(current_user.user)

        print(current_user.__dict__)
        print(current_user.user.__dict__)
        return render_template('profile-edit.html', user=current_user.user, action=action)
    elif action == "delete":
        return "delete"
    else:
        return make_response(404)


@app.route('/message/<i>')
@login_required
def message(i):
    return i


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create')
def create():
    with app.app_context():
        print(1)
        db.create_all()
        print(2)
    return "db"


if __name__ == "__main__":
    app.run(debug=DEBUG, host="0.0.0.0", port=80)


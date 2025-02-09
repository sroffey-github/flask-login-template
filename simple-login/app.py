from flask_login import LoginManager
from db_setup import init_db
from config import Config
from flask import Flask
from models import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

from routes import routes
app.register_blueprint(routes)

from models import User

login_manager = LoginManager()
login_manager.login_view = 'routes.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    init_db(app)
    app.run(debug=True)
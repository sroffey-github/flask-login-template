from flask_bcrypt import Bcrypt
from models import db, User
import random
import string

bcrypt = Bcrypt()

def generate_random_password(length=12):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def init_db(app):
    with app.app_context():
        db.create_all()
        if User.query.count() == 0:
            admin_email = "admin@localhost"
            admin_password = generate_random_password()
            hashed_password = bcrypt.generate_password_hash(admin_password).decode('utf-8')
            admin_user = User(username='admin', email=admin_email, password=hashed_password)
            db.session.add(admin_user)
            db.session.commit()
            with open('admin-credentials.conf', 'w') as f:
                f.write(f'Admin user created: username=admin, email={admin_email} password={admin_password}')
            print(f'Admin user created: username=admin, password={admin_password}')
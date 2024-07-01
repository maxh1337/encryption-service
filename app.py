from flask import Flask
from routes import configure_routes
from models import db
from data_loader import load_methods 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/encryption-service'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
configure_routes(app)

with app.app_context():
    db.create_all()
    load_methods()  

if __name__ == '__main__':
    app.run(debug=True)

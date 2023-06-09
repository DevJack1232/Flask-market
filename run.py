from market import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Конфигурация базы данных
    app.config['SQLALCHEMY_DATABASE_URI'] = 'ваш_URL_базы_данных'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Инициализация расширений Flask
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Здесь вы можете добавить дополнительные настройки, маршруты и т.д.

    return app
app = create_app()
#Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(debug=True)
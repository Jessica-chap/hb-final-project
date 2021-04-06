
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()








if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    # connect_to_db(app, echo=False)
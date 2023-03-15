from flask import Flask, render_template ,request,redirect
from models import *


#==============================configuration===============================

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///manymanydata.sqlite3"

db.init_app(app)
app.app_context().push()

#==============================Controllers=================================








if __name__ == "__main__":
    app.run(debug=True)



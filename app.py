from flask import Flask, render_template ,request,redirect
from models import *


#==============================configuration===============================

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///manymanydata.sqlite3"

db.init_app(app)
app.app_context().push()

#==============================Controllers=================================

#===================Displays all Rigistered Directors======================
@app.route('/',methods=['GET','POST'])
def all_diretors():
    directors = Director.query.all()
    return render_template('all_dirs.html', directors = directors)







if __name__ == "__main__":
    app.run(debug=True)



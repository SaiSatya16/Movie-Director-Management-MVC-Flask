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

#===================Add a new Director====================================
@app.route('/add_director', methods=['GET','POST'])
def add_director():
    if request.method == 'GET':
        return render_template('add_dir_form.html')
    if request.method == 'POST':
        d_name = request.form.get('d_name')
        d1 = Director(name = d_name)
        db.session.add(d1)
        db.session.commit()
        return redirect('/')
#==================Displays all Rigistered Movies==========================
@app.route('/all_movies',methods=['GET','POST'])
def all_movies():
    movies = Movie.query.all()
    return render_template('all_movs.html', movies = movies)
#==================Add a New Movie=========================================
@app.route('/add_movie', methods=['GET','POST'])
def add_movie():
    if request.method == 'GET':
        return render_template('add_mov_form.html')
    if request.method == 'POST':
        m_name = request.form.get('m_name')
        m1 = Movie(name = m_name)
        db.session.add(m1)
        db.session.commit()
        return redirect('/all_movies')
#==================Movies by Director======================================   
@app.route("/see_movie/<int:id>",methods=["GET","POST"])
def director_movie(id):
    d1 = Director.query.get(id)
    movies = d1.films
    return render_template("movies_by_director.html", d1 = d1, movies = movies)



if __name__ == "__main__":
    app.run(debug=True)



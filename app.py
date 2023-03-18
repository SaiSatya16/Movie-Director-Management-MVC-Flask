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
#==================Deletes the movie of specific Director==================
@app.route("/see_movie/<int:mid>/del_dir_for_movie/<int:did>",methods=["GET","POST"])
def del_mov_by_dir(mid,did):
    d1 = Director.query.get(did)
    m1 = Movie.query.get(mid)
    d1.films.remove(m1)  
    #m1.creator.remove(d1)
    db.session.add(d1)
    db.session.commit()
    return redirect('/')
#==================Assign Director to the Movie============================
@app.route("/assign/<int:id>",methods=["GET","POST"])
def assign(id):
    m1 = Movie.query.get(id)
    if request.method == 'GET':
        directors = Director.query.all()
        return render_template('assign_dir.html',directors=directors,m1=m1)
    if request.method == 'POST':
        d_id = request.form.get('d_id')
        director = Director.query.get(int(d_id))
        m1.creator.append(director)
        db.session.add(m1)
        db.session.commit()
        return redirect('/all_movies')

#===================Delete a Movie=========================================
@app.route("/delete_movie/<int:id>",methods=["GET","POST"])
def delete_movie(id):
    m1 = Movie.query.get(id)
    db.session.delete(m1)
    db.session.commit()
    return redirect('/all_movies')

if __name__ == "__main__":
    app.run(debug=True)



from datetime import datetime
from flask import Flask
import sqlite3
import random
from flask import jsonify
from flask_cors import CORS
from flask import request, json
from flask import Flask, request, render_template
import sys
import logging


app = Flask(__name__,template_folder='src')
#print(current_time)

"""conn = sqlite3.connect('database.db')
#print("Opened database successfully")

#conn.execute('CREATE TABLE Projects (Id integer primary key, ProjectName TEXT, CodingHub integer, VisualizationArena integer, AmazingEDA integer)')

#conn.close()"""

"""@app.route('/api/time')
def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return {'time': current_time}"""
CORS(app)
logging.basicConfig(level=logging.DEBUG)
@app.route('/')
def index():
    """rows=get_projects()
    if rows:
        data = rows[0]
        projectname = str(data)
        app.logger.info(rows)"""
    return render_template("Index.html")
   
@app.route('/api/home')
def Home():
    app.logger.info('Processing default request from home')
    return render_template("Home.html",message=message)

@app.route('/api/home/project',methods=['GET','POST'])
def project():
    app.logger.info('Processing default request from project')
    rows=get_projects()
    if rows:
        data = rows[0]
        projectname1 = str(data)
	projectname1= projectname1[0]
        app.logger.info(projectname1)
        #return make_response(jsonify(projectname),200)"""
    #return "Currently No Prjects available, create new one"
    if request.method == 'POST':
        with sqlite3.connect("database.db") as con:
            try:
                req = request.get_json()
                app.logger.info("request from react",req)
                projectname=req['name']
                app.logger.info(projectname)
                print("project name", flush=True)
                cur = con.cursor()
                cur.execute('''INSERT INTO Projects (ProjectName, CodingHub, VisualizationArena, AmazingEDA)
                VALUES(?, ?, ?, ?)''',(projectname,random.randint(0,999999),random.randint(0,999999),random.randint(0,999999)) )
                con.commit()
                msg = "New Project Created"
                return jsonify(projectname)
            except:
                con.rollback()
                msg = "error in insert operation"
            finally:
                return render_template('project.html', msg=msg,projectname=projectname1)
                con.close()
    #if request.method=='GET':  
    return "Error 123."		

def get_projects():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('''SELECT * from projects''')
    rows=cur.fetchall()
    conn.close()
    return rows
"""if __name__=='__main__':
    app.run(debug=True)"""

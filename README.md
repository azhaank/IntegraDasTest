This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Topic
A webapp using Flask and React for IntegraDas Interview Process - Alhamd Khan

## About 
The following webapp is built using flask-react along with sqlite. Use can create a project, and a page is created with the following apps: 
• CodingHub • VisualizationArena • AmazingEDA. Each app has a unique 6 digit IP address that has been spawned by a service on your cutting edge Kubernetes cluster. For the purpose of this assignment, you will be randomly generating a 6 digit number that will act as an IP address.  
 
## Installation
You need to install three packages on your machine:

<pre>Node.js: The JavaScript runtime that you will use to run your frontend project.</pre>
<pre>Yarn: A package and project manager for Node.js applications.</pre>
<pre>Python: A recent Python 3 interpreter to run the Flask backend on.</pre>

## Creating a Starter React Project
There are several ways to create a combined project with React and Flask. I prefer to start from the frontend because the project structure is much more complex than the backend. For this example I used the create-react-app generator to create a simple React project to start from:
<pre><code>
$ npx create-react-app react-flask-app
$ cd react-flask-app
</code></pre>

The npx command comes with Node.js. It is a simple project runner that downloads the requested command if it isn't already available and in the system's PATH. The first argument is the command to execute. The second argument is the name of the project to create. When this command completes, you will have a react-flask-app directory with a complete and fully functional simple react project.

Since you will work on this project from now on, you can cd into react-flask-app so that it is your current directory. If you list the directory you should see the top-level structure, which should be more or less like this:
<pre><code>
$ ls -l
total 912
-rw-r--r--     1 mgrinberg  staff    2884 Feb 10 14:54 README.md
drwxr-xr-x  1027 mgrinberg  staff   32864 Feb 10 15:03 node_modules
-rw-r--r--     1 mgrinberg  staff     890 Feb 10 15:04 package.json
drwxr-xr-x     8 mgrinberg  staff     256 Feb 10 14:54 public
drwxr-xr-x    10 mgrinberg  staff     320 Feb 10 23:50 src
-rw-r--r--     1 mgrinberg  staff  454962 Feb 10 14:54 yarn.lock
</code></pre>

## Creating a Flask API Backend
The next step is to create the Flask project. Create directories

$ mkdir api
$ cd api

create a virtual environment

$ python3 -m venv venv
$ python -m venv venv
$ venv\Scripts\activate
(venv) $ _
For this simple example I need only two Python packages, the obvious Flask and also python-dotenv:

(venv) $ pip install flask python-dotenv

Here's is my flask back end file api. py:
<pre><code> @app.route('/api/home/project',methods=['GET','POST'])
def project():
    app.logger.info('Processing default request from project')
    rows=get_projects()
    if rows:
        data = rows[0]
        projectname = str(data)
        app.logger.info(rows)
        return make_response(jsonify(projectname),200)
    #return "Currently No Prjects available, create new one"
   </code> </pre>
# inserts data from front-end to db    
   <pre><code> if request.method == 'POST':
        with sqlite3.connect("database.db") as con:
            try:
                req = request.get_json()
                app.logger.info("request from react" ,req)
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
                return render_template('project.html', msg=msg)
                con.close()
    #if request.method=='GET':  
    return "Error 123."		</code></pre>
# gets projectnames from db
<pre><code>
def get_projects():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('''SELECT * from projects''')
    rows=cur.fetchall()
    conn.close()
    return rows
"""if __name__=='__main__':
    app.run(debug=True)""" </code></pre>
# Here is my Flask-React Homepage for adding projects:

![myimage-alt-tag](https://github.com/azhaank/IntegraDasTest/blob/firstbranch/src/frontend.PNG)

# Here is my Flask-React Form Submitted:

![myimage-alt-tag](https://github.com/azhaank/IntegraDasTest/blob/firstbranch/src/formSubmit.PNG)


# Here is my output screen of the created project with randomly generated IP addresses:
![myimage-alt-tag](https://github.com/azhaank/IntegraDasTest/blob/firstbranch/src/output.PNG)

# Future Work
There were some issues found while connecting the React front end with the Flask backend. Therefore, the output was generated in the local computer (Using Python IDE) and not over the server. Please keep in touch for further instructions!
Thanks,
ALHAMD KHAN,
M.Sc. (ECE),
University of Calgary

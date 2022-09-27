from flask import Flask, send_from_directory, render_template, request
from jinja2 import Environment
from jinja2.loaders import FileSystemLoader
from flask_sqlalchemy import SQLAlchemy
import secrets
import os
app = Flask(__name__)

app.config['FLASK_HOST'] = os.environ.get('FLASK_HOST')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class obfuscation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100))
    file_src = db.Column(db.String(300))

db.create_all()
db.session.commit()


@app.route("/")
def index():
    return render_template("index.html")




@app.route("/<fileloc>")
@app.route("/images/<fileloc>")
def fileload(fileloc):
    if 'User-Agent' not in request.headers:
        return send_from_directory("files", fileloc)
    headers = request.headers['User-Agent']
#    print(headers)
#    print(fileloc)
    serve = True
    for x in ['.png', '.jpg', '.gif', '.jpeg', '.bmp']:
        if fileloc.endswith(x):
            serve = False
#            print("srv false")
            break
    if serve == True or headers == "Mozilla/5.0 (compatible; Discordbot/2.0; +https://discordapp.com)" or headers == "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.6; rv:92.0) Gecko/20100101 Firefox/92.0" or "Discordbot/2.0;" in headers or "twitterbot" in headers.lower() or "github-camo" in headers.lower() or "Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy)" in headers:
#        if not fileloc.endswith('.ico'):
#        print("served "+fileloc)
        return send_from_directory("files", fileloc)
    else:
        target = secrets.token_urlsafe(100)
        dbloc = obfuscation.query.filter_by(code=target).first()
        while dbloc is not None:
            target = secrets.token_urlsafe(100)
            dbloc = obfuscation.query.filter_by(code=target).first()
        dbwrite = obfuscation(code=target, file_src=fileloc)
        db.session.add(dbwrite)
        db.session.commit()
        imgloc = "/fileload?code="+target
        return render_template("render.html", imgloc=imgloc)

@app.route("/fileload")
def static_dir():
    if 'code' not in request.args:
        return ("<script>location.replace('/');</script>"), 300
    else:
         target = request.args['code']
         dbloc = obfuscation.query.filter_by(code=target).first()
         if dbloc is None:
             return("404 Not Found"), 404
#         print(dbloc.file_src)
         path = str(dbloc.file_src)
         db.session.delete(dbloc)
         db.session.commit()
         return send_from_directory("files", path)




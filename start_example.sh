export FLASK_HOST=https://YOUR.HOSTNAME.HERE/
export FLASK_APP=app.py
export FLASK_ENV=production
export TEMPLATES_AUTO_RELOAD=true
export FILES_DIR=files
# dont put a slash in front of dir
/usr/bin/gunicorn --bind 0.0.0.0:5000 app:app
# you dont have to use gunicorn, you can use normal flask if you want - replace it with <python_cmd> -m flask run -p 5000 to do the same thing without gunicorn
# gunicorn on debian based distros - apt install gunicorn

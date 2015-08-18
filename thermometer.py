from flask import Flask, render_template, request, url_for, redirect
from flask.ext.autoindex import AutoIndex

thermometer = Flask('flaskapp')

thermometer.secret_key = 'supersecretthinggoeshere'

do_pretty = AutoIndex(thermometer, '/Users/jack/ncc_project/POD_Server/web', add_url_rules=False)

    
@thermometer.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('main.html', form=form)


@thermometer.route('/creds', methods=["GET","POST"])
def credentials():

    error = ''
    try:
        if request.method == "POST":
		
            attempted_username = request.form['username']
            attempted_password = request.form['password']

            flash(attempted_username)
            flash(attempted_password)

            if attempted_username == "admin" and attempted_password == "password":
                return render_template("main.html")
				
            else:
                error = "Invalid credentials. Try Again."

        return render_template("creds.html", error = error)

    except Exception as e:
        #flash(e)
        return render_template("creds.html", error = error)  


@thermometer.route('/files')
@thermometer.route('/files/<path:path>')
def autoindex(path='.'):
    return do_pretty.render_autoindex(path)


@thermometer.route('/')
def homepage():
	return render_template("main.html")


@thermometer.errorhandler(404)
def four_oh_four(e):
		return render_template("error.html"), 404
		

wsgi = thermometer.wsgi_app
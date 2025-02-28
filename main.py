from flask import Flask, render_template, request, jsonify, url_for, redirect

app = Flask(__name__)

@app.route("/start")
def start():
    return redirect(url_for('query'))



@app.route("/query", methods=['GET', 'POST'])
def query():
    if request.method == 'POST':
        query = request.form.get('query')

        answer = "test" + "2"
        
        #return jsonify(answer)
        
        # user = Users.query.filter_by(email=email).first()
        # if user:
        #     if check_password_hash(user.password, password):
        #         flash('Logged in successfully!', category='success')
        #         login_user(user, remember=True)
        #         return redirect(url_for('views.home'))
        #     else:
        #         flash('incorrect password, try again', category='error')
        # else:
        #     flash('Email does not exist', category='error')
        
        if answer != None:
            return render_template("query.html", query=query, answer=answer)
    return render_template("query.html")
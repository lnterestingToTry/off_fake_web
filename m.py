from flask import Blueprint, render_template, request, flash, redirect
#from flask import url_for
#from .models import Users
#from werkzeug.security import generate_password_hash, check_password_hash
#from . import db
#from flask_login import login_user, login_required, logout_user, current_user


main = Blueprint('main', __name__)


@main.route('/main', methods=['GET', 'POST'])
def login():

    return render_template("base.html")
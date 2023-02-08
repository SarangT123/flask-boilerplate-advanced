from website import app
from website.general_functions import is_admin
from flask import render_template, url_for, flash, redirect, session, request,abort
from website import app, bcrypt, db, login_manager, access_levels
from website.models import User, Admin_users, Admin_requests
from flask_login import UserMixin, login_user, login_required, logout_user, current_user
import website.form_validation as forms


@app.route('/')
def home():
    return render_template('home.html')
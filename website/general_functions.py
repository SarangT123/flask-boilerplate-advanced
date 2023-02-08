from flask import render_template, url_for, flash, redirect, session, request
from website import app, bcrypt, db, login_manager, access_levels
from website.models import User, Admin_users
from flask_login import UserMixin, login_user, login_required, logout_user, current_user
import website.form_validation as forms

def is_admin():
    if current_user.is_authenticated:
        a=Admin_users.query.filter_by(user_id=current_user.id).first()
        if a!=None:
            if a.access <= access_levels['admin']:
                return True
    return False

def is_admin_id(id):
    if current_user.is_authenticated:
        a=Admin_users.query.filter_by(user_id=id).first()
        if a!=None:
            if a.access <= access_levels['admin']:
                return True
    return False
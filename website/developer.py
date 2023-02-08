from website import app,access_levels
from website.general_functions import is_admin,is_admin_id
from flask import render_template, url_for, flash, redirect, session, request,abort
from website import app, bcrypt, db, login_manager, access_levels
from website.models import User, Admin_users, Admin_requests
from flask_login import UserMixin, login_user, login_required, logout_user, current_user
import website.form_validation as forms

@app.route('/user_id_search', methods=['GET', 'POST'])
def user_id_search():
    if current_user.is_authenticated:
        if is_admin():
            form=forms.User_id_search()
            if request.method == 'POST':
                if form.validate_on_submit():
                    user = User.query.filter_by(username=form.user.data).first()
                    if user:
                        return str(user.id)
                    else:
                        return "User does not exists"
            return render_template('user_id_search.html', form=form)
    abort(403)

@app.route('/admin_requests', methods=['GET', 'POST'])
def admin_requests():
    if current_user.is_authenticated:
        if Admin_requests.query.filter_by(user_id=current_user.id).first():
            return "You already have a request"
        if not(is_admin()):
            form = forms.Admin_requests()
            if request.method == 'POST':
                if form.validate_on_submit():
                    Arequest = Admin_requests(user_id=current_user.id, message=form.reason.data)
                    db.session.add(Arequest)
                    db.session.commit()
                    return "Request submitted"
            return render_template('admin_request.html', form=form)
        elif is_admin():
            # listing all admin requests
            requests = Admin_requests.query.all()
            return render_template('admin_requests.html', requests=requests)
    abort(403)

                
@app.route('/developer_interface')
def developer_interface():
    return render_template('developer_dashboard.html')

@app.route('/make_mod/<int:id>')
def make_mod(id):
    if current_user.is_authenticated:
        if is_admin():
            user = User.query.filter_by(id=id).first()
            if user:
                if not is_admin_id(id):
                    admin = Admin_users(user_id=user.id, access=access_levels['lowest_admin_panel_access'])
                    db.session.add(admin)
                    # delete request
                    request = Admin_requests.query.filter_by(user_id=user.id).first()
                    db.session.delete(request)
                    db.session.commit()
                    return "Sucessfully made mod"
                return "User is already a mod"
            else:
                return "User does not exists"
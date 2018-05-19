from flask import render_template, Blueprint
from flask_login import login_required, current_user
from .. import app_info

index_bp = Blueprint('index', __name__)


@index_bp.route('/', methods=['GET'])
# @login_required
def index():
    return render_template('index.html', app_info=app_info, user=current_user)

@index_bp.route('/team', methods=['GET'])
def team():
    return render_template('team.html', app_info=app_info, user=current_user)

@index_bp.route('/about', methods=['GET'])
def about():
    return render_template('about.html', app_info=app_info, user=current_user)

@index_bp.route('/papers', methods=['GET'])
def papers():
    return render_template('papers.html', app_info=app_info, user=current_user)

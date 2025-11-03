import os, json
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

bp = Blueprint('upload', __name__, url_prefix='/upload')

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'uploads_data.json')

ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt'}


@bp.route('/')
def upload_form():
    return render_template('upload.html')


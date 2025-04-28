import os
from werkzeug.utils import secure_filename

def save_uploaded_audio(file):
    filename = secure_filename(file.filename)
    upload_path = os.path.join('static/uploads', filename)
    os.makedirs('static/uploads', exist_ok=True)
    file.save(upload_path)
    return upload_path

def save_recorded_audio(blob):
    filename = 'recorded_audio.wav'
    upload_path = os.path.join('static/uploads', filename)
    os.makedirs('static/uploads', exist_ok=True)
    blob.save(upload_path)
    return upload_path
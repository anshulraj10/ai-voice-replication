import os
from flask import Blueprint, render_template, request, jsonify, send_file
from services.audio_processing import save_uploaded_audio, save_recorded_audio
from services.openvoice_v1 import generate_audio_v1
from services.openvoice_v2 import generate_audio_v2

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/generate', methods=['POST'])
def generate():
    text = request.form['text']
    model_version = request.form['model_version']
    speed = float(request.form['speed'])

    # Handle audio
    audio_type = request.form['audio_type']
    if audio_type == 'upload':
        file = request.files['audio']
        ref_path = save_uploaded_audio(file)
    else:  # Recorded audio
        blob = request.files['audio']
        ref_path = save_recorded_audio(blob)

    if model_version == 'v1':
        style = request.form['style']
        output_path = generate_audio_v1(text, ref_path, style, speed)
    else:
        language = request.form['language']
        output_path = generate_audio_v2(text, ref_path, language, speed)

    output_filename = os.path.basename(output_path)

    return jsonify({
        'audio_url': f'/static/outputs/{output_filename}'
    })
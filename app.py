from flask import Flask
from routes import main

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['OUTPUT_FOLDER'] = 'static/outputs'
app.secret_key = 'super_secret'

app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
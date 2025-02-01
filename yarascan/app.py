# BACKEND FLASK APPLICATION SOURCE CODE
from flask import Flask, request, render_template, jsonify
import yara
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['YARA_RULES_FOLDER'] = 'yara_rules'
app.secret_key = 'supersecretkey'  # Replace with a secure key

# Ensure the necessary folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['YARA_RULES_FOLDER'], exist_ok=True)

# Load YARA rules from the yara_rules folder
def load_yara_rules():
    rules = yara.compile(filepath=os.path.join(app.config['YARA_RULES_FOLDER'], 'myrules.yar'))
    return rules

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify(error='No file part'), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify(error='No selected file'), 400
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    
    # Load the YARA rules
    rules = load_yara_rules()
    
    # Scan the file with YARA
    matches = rules.match(file_path)
    
    # Convert matches to a list of dictionaries
    matches_list = [{'rule': match.rule, 'meta': match.meta} for match in matches]
    
    return jsonify(matches=matches_list)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/guide')
def guide():
    return render_template('guide.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

if __name__ == '__main__':
    app.run(debug=True)

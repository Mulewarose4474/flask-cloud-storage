from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

files = []  # Simulated storage

@app.route('/')
def index():
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload():
    filename = request.form.get('filename')
    if filename:
        files.append(filename)
    return redirect(url_for('index'))

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True, port=5000)

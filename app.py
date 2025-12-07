from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Path to audio files
AUDIO_FOLDERS = [
    "Evolve 3 Student's Book Audio [www.languagecentre.ir]",
    "Evolve 3 Workbook Audio [www.languagecentre.ir]"
]

@app.route('/')
def index():
    """Main page with audio player and file list"""
    audio_files = {}
    
    for folder in AUDIO_FOLDERS:
        folder_path = os.path.join(os.path.dirname(__file__), folder)
        if os.path.exists(folder_path):
            files = [f for f in os.listdir(folder_path) if f.endswith('.mp3')]
            files.sort()
            audio_files[folder] = files
    
    return render_template('index.html', audio_files=audio_files)

@app.route('/audio/<path:folder>/<path:filename>')
def serve_audio(folder, filename):
    """Serve audio files"""
    folder_path = os.path.join(os.path.dirname(__file__), folder)
    return send_from_directory(folder_path, filename)

@app.route('/health')
def health():
    """Health check endpoint for Render"""
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

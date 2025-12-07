from flask import Flask, render_template, send_from_directory, jsonify
import os

app = Flask(__name__)

def count_mp3_files(directory):
    """Recursively count MP3 files in a directory"""
    count = 0
    try:
        for root, dirs, files in os.walk(directory):
            count += sum(1 for f in files if f.lower().endswith('.mp3'))
    except:
        pass
    return count

@app.route('/')
def index():
    """Main page with audio player and folder structure"""
    base_path = os.path.dirname(__file__)
    if not base_path:
        base_path = '.'
    
    # Get all directories that contain MP3 files (recursively)
    folders = []
    exclude_dirs = ['templates', 'static', 'venv', '__pycache__', '.git', 'node_modules']
    
    try:
        for item in os.listdir(base_path):
            item_path = os.path.join(base_path, item)
            if os.path.isdir(item_path) and item not in exclude_dirs:
                # Count MP3 files recursively
                mp3_count = count_mp3_files(item_path)
                
                if mp3_count > 0:
                    # Create a display name
                    display_name = item
                    if 'Student' in item or 'student' in item:
                        display_name = "📚 Student's Book Audio"
                    elif 'Workbook' in item or 'workbook' in item:
                        display_name = "📝 Workbook Audio"
                    
                    folders.append({
                        'name': item,
                        'display_name': display_name,
                        'count': mp3_count
                    })
    except Exception as e:
        print(f"Error listing base directory: {e}")
    
    folders.sort(key=lambda x: x['name'])
    return render_template('index.html', folders=folders)

@app.route('/api/folder/<path:folder_name>')
def get_folder_files(folder_name):
    """API endpoint to get files and subfolders in a folder"""
    base_path = os.path.dirname(__file__)
    if not base_path:
        base_path = '.'
    
    folder_path = os.path.join(base_path, folder_name)
    
    if not os.path.exists(folder_path):
        return jsonify({'error': 'Folder not found'}), 404
    
    # Get structure with subfolders and files
    structure = []
    
    try:
        # Check for subfolders (like Unit1, Unit2, etc.)
        items = sorted(os.listdir(folder_path))
        has_subfolders = any(os.path.isdir(os.path.join(folder_path, item)) for item in items)
        
        if has_subfolders:
            # Group by subfolders
            for item in items:
                item_path = os.path.join(folder_path, item)
                if os.path.isdir(item_path):
                    mp3_files = sorted([f for f in os.listdir(item_path) if f.lower().endswith('.mp3')])
                    if mp3_files:
                        structure.append({
                            'type': 'folder',
                            'name': item,
                            'files': mp3_files,
                            'path': os.path.join(folder_name, item)
                        })
        else:
            # Direct MP3 files
            mp3_files = sorted([f for f in items if f.lower().endswith('.mp3')])
            if mp3_files:
                structure.append({
                    'type': 'files',
                    'name': folder_name,
                    'files': mp3_files,
                    'path': folder_name
                })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    return jsonify({
        'folder': folder_name,
        'structure': structure
    })

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

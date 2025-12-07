# Evolve 3 Audio Player

A web application to play Evolve 3 English learning audio files online.

## Features

- 🎵 Clean, modern audio player interface
- 📱 Responsive design (works on mobile and desktop)
- 🔍 Search functionality to find audio files quickly
- ⏭️ Auto-play next audio file
- 📁 Organized by Student's Book and Workbook
- 🎨 Beautiful gradient design

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and go to `http://localhost:5000`

## Deploy to Render.com

### Option 1: Using GitHub (Recommended)

1. Create a new repository on GitHub
2. Push this code to the repository:
```bash
git init
git add .
git commit -m "Initial commit: Evolve 3 audio player"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

3. Go to [Render.com](https://render.com) and sign up/login
4. Click "New +" and select "Web Service"
5. Connect your GitHub repository
6. Render will auto-detect the settings from `render.yaml`
7. Click "Create Web Service"

### Option 2: Manual Deploy

1. Go to [Render.com](https://render.com) and sign up/login
2. Click "New +" and select "Web Service"
3. Choose "Build and deploy from a Git repository"
4. Or use "Deploy from GitHub" and select your repository
5. Configure:
   - **Name**: evolve3-audio-player
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. Click "Create Web Service"

## Project Structure

```
evolve3/
├── app.py                          # Flask application
├── requirements.txt                # Python dependencies
├── render.yaml                     # Render.com configuration
├── templates/
│   └── index.html                  # Web interface
├── Evolve 3 Student's Book Audio/  # Audio files
└── Evolve 3 Workbook Audio/        # Audio files
```

## Notes

- The application serves audio files without allowing downloads (using `controlsList="nodownload"`)
- Health check endpoint available at `/health`
- All audio files must be in MP3 format
- The app automatically scans the audio folders on startup

## License

Educational use only. Audio files are property of their respective copyright holders.

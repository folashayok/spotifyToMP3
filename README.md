# spotifyToMP3

CURRENT STATUS: Waiting for approval for API keys to fully release youtube search features

Convert Spotify tracks and playlists to MP3 files easily.

## Features
- Download Spotify tracks as MP3
- Support for playlists
- Simple command-line interface

## Requirements
- Python 3.10+
- Required Python packages (see below)
- Spotify API credentials (see `secrets.py`)

## Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/folashayok/spotifyToMP3.git
   cd spotifyToMP3
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your Spotify API credentials to `secrets.py`.

## Usage
Run the main script:
```bash
python main.py
```
Follow the prompts to download tracks or playlists.

## File Structure
- `main.py` — Main application logic
- `secrets.py` — Store your Spotify API credentials
- `__pycache__/` — Python cache files

## Author
folashayok

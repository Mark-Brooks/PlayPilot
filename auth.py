# auth.py
import requests
import webbrowser
from flask import Flask, request

# Spotify application credentials (development only, replace for production)
CLIENT_ID = "e675ec708c1143d1a377ac503821f937"
CLIENT_SECRET = "0fb77ee9479b45a08eb28565d6a3f086"
REDIRECT_URI = "http://localhost:8080/callback"  # local server for dev only
AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"
SCOPE = "user-read-playback-state user-modify-playback-state"

app = Flask(__name__)
auth_token = None

def authorize_user():
    global auth_token
    auth_url = f"{AUTH_URL}?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope={SCOPE}"
    webbrowser.open(auth_url)
    app.run(port=8080)  # Run local server to capture redirect
    
    return auth_token

@app.route("/callback")
def callback():
    global auth_token
    code = request.args.get("code")
    response = requests.post(TOKEN_URL, data={
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    })
    auth_token = response.json().get("access_token")
    return "Authorization complete. You may close this window."

import mariadb
import requests
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Configuración de Jellyfin
JELLYFIN_URL = "http://10.1.100.11:8096"
JELLYFIN_API_KEY = "3b2863e49dce4c71841377b09556369d"

@app.get("/")
def read_index():
    return FileResponse("/app/static/index.html")

@app.post("/register")
def register_user(username: str, password: str, email: str = None):
    headers = {"X-Emby-Token": JELLYFIN_API_KEY}
    data = {"Name": username, "Password": password}
    
    try:
        response = requests.post(f"{JELLYFIN_URL}/Users/New", json=data, headers=headers, verify=False)
        
        if response.status_code in [200, 204]:
            conn = mariadb.connect(user="admin_user", password="Naipeer1234", host="db", database="jellyfin_portal")
            cur = conn.cursor()
            cur.execute("INSERT INTO users (username, password_hash, email, jellyfin_id, status) VALUES (?, ?, ?, ?, ?)", 
                       (username, password, email, "creado", 'active'))
            conn.commit()
            conn.close()
            return {"message": "¡Éxito! Usuario creado en OnlyUses"}
        else:
            return {"error": response.text}
    except Exception as e:
        return {"error": str(e)}

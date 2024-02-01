from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Configura las credenciales
scopes = ['https://www.googleapis.com/auth/drive.readonly']
flow = InstalledAppFlow.from_client_secrets_file('path/to/your/client_secret.json', scopes=scopes)
credentials = flow.run_local_server(port=0)

# Construye el servicio de Google Drive
drive_service = build('drive', 'v3', credentials=credentials)

# ID de la carpeta (extraído de la URL que proporcionaste)
folder_id = '1w_mnWZu3pL68HnkerRXRBoPqyIfMCHb3'
#https://drive.google.com/drive/folders/1w_mnWZu3pL68HnkerRXRBoPqyIfMCHb3?usp=drive_link

# Lista de archivos en la carpeta
results = drive_service.files().list(q=f"'{folder_id}' in parents and trashed=false",
                                      fields="files(id, name, mimeType)").execute()
files = results.get('files', [])

if not files:
    print('No files found in the specified folder.')
else:
    print('Files in the specified folder:')
    for file in files:
        print(f"{file['name']} ({file['id']}) - {file['mimeType']}")

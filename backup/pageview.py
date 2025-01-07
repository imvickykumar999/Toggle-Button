
# pip install firebase-admin

from firebase_admin import db
from firebase_admin import credentials
import firebase_admin, os

def run():
    path = './'
    file = 'ideationology-4c639-firebase-adminsdk-5hfwu-29e74129a4.json'

    dir = os.path.join(path, file)
    cred = credentials.Certificate(dir)

    url = 'https://ideationology-4c639-default-rtdb.asia-southeast1.firebasedatabase.app/'
    path = {'databaseURL' : url}

    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred, path)

    refv = db.reference('A/B/C/Switch')
    g = refv.get()
    if g == 1:
        g = 0
    else:
        g = 1

    refv.set(g)
    return g

print(run())

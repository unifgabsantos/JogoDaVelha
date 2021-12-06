
import firebase_admin,json
from firebase_admin import credentials,db
from datetime import datetime
from time import sleep
cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred, {'databaseURL':"https://game-4ce53-default-rtdb.firebaseio.com/"})
def Post(Player_Win:str,Player_Lose:str):
    ref = db.reference(f"/{Player_Win}/")
    data = {    
        "Date":datetime.now().strftime("%d/%m/%Y %H:%M"),
        "Player_Win":Player_Win,
        "Player_Lose":Player_Lose
    }
    ref.push(data)
def Get(player_Name:str)->int:
    ref = db.reference(f"/{player_Name}/")
    data = ref.get()
    return len(data)
    

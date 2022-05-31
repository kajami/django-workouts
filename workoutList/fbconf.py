import os
from dotenv import load_dotenv
load_dotenv()

firebaseConfig = {
  'apiKey': str(os.getenv('APIKEY')),
  'authDomain': str(os.getenv('AUTHDOMAIN')),
  'databaseURL': str(os.getenv('DATABASE_URL')),
  'projectId': str(os.getenv('PROJECT_ID')),
  'storageBucket': str(os.getenv('STORAGE_BUCKER')),
  'messagingSenderId': str(os.getenv('MESSAGING_SENDER_ID')),
  'appId': str(os.getenv('APP_ID'))
}
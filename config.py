
import os

class Config:

    BOT_TOKEN = os.environ.get('BOT_TOKEN', '5442493323:AAGE585VqW2Rjn8p7fTamBdyiSsg9dktdgE')
    APP_ID = os.environ.get('APP_ID', '6534707')
    API_HASH = os.environ.get('API_HASH', '4bcc61d959a9f403b2f20149cbbe627a')

    #comma seperated user id of users who are allowed to use

    DOWNLOAD_DIR = 'downloads'
    OWNER_ID = int(os.environ.get("OWNER_ID", 1316963576))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", '-1001648020195')  
    # your telegram id
    OWNER_ID = int(os.environ.get("OWNER_ID", "1430593323"))
    # database session name, example: xurluploader
    SESSION_NAME = os.environ.get("SESSION_NAME", "hpbot")
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Uploader:Uploader@cluster0.ba0ppxa.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001843564893"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
    DOWNLOAD_LOCATION = "./DOWNLOADS"

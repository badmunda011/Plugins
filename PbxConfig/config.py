import os


class Config(object):
    # Editable Variables #
    ABUSE = os.environ.get("ABUSE", None)
    API_HASH = "4c246fb0c649477cc2e79b6a178ddfaa"
    APP_ID = 27383453
    BL_CHAT = set(int(x) for x in os.environ.get("BL_CHAT", "").split())
    BOT_HANDLER = "®"
    BOT_LIBRARY = os.environ.get("BOT_LIBRARY", None)
    BOT_TOKEN = "6837458112:AAG5XLx5p5NN9_ljbgsV4tg8yfaI76EiL7Q"
    BOT_USERNAME = "PBXOLD_BOT"
    BUTTONS_IN_HELP = int(os.environ.get("BUTTONS_IN_HELP", 7))
    CURRENCY_API = os.environ.get("CURRENCY_API", None)
    DATABASE_URL = postgres://blmaclrsyfmmgr:f8884d680d703e923f667e4acd25b8ed1e7db6260ba7202ad17cf579df186c72@ec2-52-4-153-146.compute-1.amazonaws.com:5432/d9cdrjp1jirb6c
    EMOJI_IN_HELP = os.environ.get("EMOJI_IN_HELP", "✯")
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO", "Badhacker98/Plugins")
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    HANDLER = os.environ.get("HANDLER", ".")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    IG_SESSION = os.environ.get("INSTAGRAM_SESSION", None)
    INSTANT_BLOCK = os.environ.get("INSTANT_BLOCK", None)
    LOGGER_ID = int(os.environ.get("LOGGER_ID", 0))
    LYRICS_API = os.environ.get("LYRICS_API", None)
    MAX_SPAM = int(os.environ.get("MAX_SPAM", 3))
    MY_CHANNEL = os.environ.get("YOUR_CHANNEL", "ll_THE_BAD_BOT_ll")
    MY_GROUP = os.environ.get("YOUR_GROUP", "ll_THE_BAD_BOT_ll")
    OCR_API = os.environ.get("OCR_API", None)
    PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL", 0))
    PM_LOGGER = int(os.environ.get("PM_LOGGER", 0))
    PM_PERMIT = os.environ.get("PM_PERMIT", "True")
    REMOVE_BG_API = os.environ.get("REMOVE_BG_API", None)
    PBXBOT_SESSION ="==hELl1BJWap1sBu5-W-PJbvgBwhees7lKA1NZVQhmUJU7DgRr4PGfGpIgRvaqoRJWlDNEVtu8gB3d-l7ajfy3iai4FRHcdD9QUwufE9-Y9e1sGgl7BKOTYxAZfmcrhHeQ2K6oiRtFp24mjCGr3rvzXcPdHmHSlTnGqsfqgE0cdcixEbqL60pLu87sU0DvRn0sqzXpUocUs5xTjALVLxDG2XvUW4Stv_Y7WfrQ_cf9q8HXJ7Grmqa8EjpkXH5gjokW2JvHra9ZnLG9SvWbLRf3SmPN5mxt6m_Ak0PdCgSzFzAvkEgJHPZpNB7Qp5n6isbh7ROyiXj2E_HCSefFr4qBA7pv6EEt_BWWat80=bot=="
    SESSION_2 = os.environ.get("SESSION_2", None)
    SESSION_3 = os.environ.get("SESSION_3", None)
    SESSION_4 = os.environ.get("SESSION_4", None)
    SESSION_5 = os.environ.get("SESSION_5", None)
    SHORTENER_API = os.environ.get("SHORTENER_API", None)
    SUDO_HANDLER = os.environ.get("SUDO_HANDLER", ".")
    TAG_LOGGER = int(os.environ.get("TAG_LOGGER", 0))
    THUMB_IMG = os.environ.get("THUMB_IMG", "./PbxConfig/resources/pics/Pbxbot_logo.jpg")
    UNLOAD = list(os.environ.get("UNLOAD", "").split())
    UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "https://github.com/Badhacker98/PbXbot")
    UPSTREAM_REPO_BRANCH = os.environ.get("UPSTREAM_REPO_BRANCH", "master")
    WEATHER_API = os.environ.get("WEATHER_API", None)

    # Don't edit variables below this line #
    LOGGER = True
    CHROME_BIN = os.environ.get("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver")
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
    MAX_MESSAGE_SIZE_LIMIT = 4095
    SUDO_USERS = [6898413162]
    TELEGRAPH_NAME = os.environ.get("TELEGRAPH_NAME", "[ ᴛʜᴇ ᴘʙx ]")
    TEMP_DIR = os.environ.get("TEMP_DIR", None)
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")
    


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
    

# FOR SELF HOST
# EDIT THIS FILE AND RENAME TO config.py TO MAKE THIS BOT WORKING
# FILL THESE VALUES ACCORDINGLY.

from PbxConfig.config import Config


class Development(Config):
    # get these values from my.telegram.org.
    
    APP_ID = 27383453 # 666666 is a placeholder. Fill your 6 digit api id
    API_HASH = "4c246fb0c649477cc2e79b6a178ddfaa"  # replace this with your api hash
    BOT_TOKEN = "7201253389:AAG4qdCWAFprgCafSK5fwLC0zQrfvRts0gA"  # Create a bot from @BotFather and paste the token here
    BOT_LIBRARY = "telethon"  # fill 'pyrogram' if you want pyrogram version of Pbxbot else leave it as it is.
    DATABASE_URL = "postgres://u94bvurcphj34k:p88947d7eef18ddde09311863e892248be33064faa453b5a7792270e9ab27c7c5@c4jpa9p9eiug0j.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d5phr18iooe2k0"  # A postgresql database url from elephantsql
    PBXBOT_SESSION = "==HelL1BJWap1sBu1s83ggIqst8kD4S4SYmAMhsPXBiZLJ_cz5LqBtr5IxEaGKCJ9cnd8t3dPZ7qxHVA3oVj5D8gspH--vZG7hYdDrtftZpPMfR89leA2zg1dgdaZJAFTImbWNbuAtcdsg8tikqKDk8Rqr8kJwrJDQkSQPPQihb7BdFG7WtugPOYpUaeICFqA96_vowxMWhm-9hVVAZTIgC7jHDm1SKxWSw3GPWusvPyaHns6aC-iHh2j7CoM2-E7MOcAuXmbllu45iioHRfPA21XeD0gBWr5sEJGna2G3PiahSbzi69q9QOQpYLw-ogxLxorNLQAl4LQQcYvHf71oB0NbmyYunO_rQHkg=bOt=="  # telethon or pyrogram string according to BOT_LIBRARY
    HANDLER = "®"  # Custom Command Handler
    SUDO_HANDLER = "©"  # Custom Command Handler for sudo users.


# end of required config
# Pbxbot

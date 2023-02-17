from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 28857474
    API_HASH = "b313cfa406876ecdb8aab28c33e1ebc2"
    # the name to display in your alive message
    ALIVE_NAME = "ILIA"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://lbtebcgu:MqjyAVRP4U8r885pBKIaQYNtuR2tfSkS@baasu.db.elephantsql.com/lbtebcgu"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BJWap1sBu3g2VeTtha17GUuMA5W7CjpeZEp5XLqQ2yO1xGHNLlgwaudI_lYBUqBNRpk5ZuoZKb-ndvSUtOwnXcQ-_iywL7tlukU81RENwMLy8Oy8fO8wTSB5-_Y1PcrKe2ITR3R7JS6ZhXNSNCNa5lJPP0wUGwqsY95xGn98HpYlScvtfjkdrQn6O_iq_dbYFdtl8k8aJWfiho4GXG56Wq4TpGNK87yB0X8aS1af0bNqNE-EJ8l_ymXuuuljefnJvCryN4KePy2nekQ1qD50NIIlevCcraujZSVYqphcnZRkM7rOg6szhWcpvZPtIBQgSg9RpoZ1IDW5nUMWXAvXj4snJeLG5W4="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6078301994:AAGY3tHd5JdDJLORl222ZRvBmlRpG_T0nHo"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -100
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"

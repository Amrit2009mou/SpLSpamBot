import os

class API:
    API_ID = int(os.getenv("API_ID",13691707))
    API_HASH = os.geten(["API_HASH","2a31b117896c5c7da27c74025aa602b8")

class TOKENS:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "5621393763:AAE6SnETTZbzIfxYYmDO5EcUxiijhJqCsck")
    BOT_TOKEN_2 = os.getenv("BOT_TOKEN_2", "6002673940:AAEhWLvtbEG9O67_Xr8kjmrzYiXqmebtFXM")
    BOT_TOKEN_3 = os.getenv("BOT_TOKEN_3", "5884362002:AAH5C9oSXprmR9CtL99JHa-eVg-PA4fDJCA")
    BOT_TOKEN_4 = os.getenv("BOT_TOKEN_4", "5548451876:AAGB3FEBNETFKe6lLG7hxj03Na_ifJxY6lg")
    BOT_TOKEN_5 = os.getenv("BOT_TOKEN_5", "5949161983:AAHkO-qzcKGi0QH8Ht0AmlDpD17P8yA9a7k")
    BOT_TOKEN_6 = os.getenv("BOT_TOKEN_6", "")
    BOT_TOKEN_7 = os.getenv("BOT_TOKEN_7", "")
    BOT_TOKEN_8 = os.getenv("BOT_TOKEN_8", "")
    BOT_TOKEN_9 = os.getenv("BOT_TOKEN_9", "")
    BOT_TOKEN_10 = os.getenv("BOT_TOKEN_10", "")

class DATABASE:
    MONGO_DB_URL = os.getenv("MONGO_DB_URL", "mongodb+srv://NicolasCageMafia:I6MnXBGIzm7XbucO@spamzy.qe4qabs.mongodb.net/?retryWrites=true&w=majority")

class DEV:
    OWNER_ID = int(os.getenv("OWNER_ID", "1103067009"))
    
    # DONT EDIT THIS 
    SUDO_USERS = [5834211089] 
    # YOU CAN ADD SUDO USING /addsudo

class STUFF:
    ALIVE_PIC = os.getenv("ALIVE_PIC", "")
    HELP_PIC = os.getenv("HELP_PIC", "")
    START_PIC = os.getenv("START_PIC", "")
    COMMAND_HANDLER = os.getenv("COMMAND_HANDLER", "")
    ALLOW_PORN = os.getenv("ALLOW_PORN", True) # REPLACE 'True' BY 'False' IF U WANT TO DISABLE PORN

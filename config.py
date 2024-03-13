import os

class API:
    API_ID = int(os.getenv("API_ID",20985063))
    API_HASH = os.geten(["API_HASH","97aab4e949320009a265cbfdc69030ab")

class TOKENS:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "6803534148:AAGtuUxF2yo5gM4pcQo_UvUCcWAltVZmquM")
    BOT_TOKEN_2 = os.getenv("BOT_TOKEN_2", "6998100671:AAGwDbqmkQssj36n16FWl0VKTo6SYDqemlc)
    BOT_TOKEN_3 = os.getenv("BOT_TOKEN_3", "5884362002:AAH5C9oSXprmR9CtL99JHa-eVg-PA4fDJCA")
    BOT_TOKEN_4 = os.getenv("BOT_TOKEN_4", "5548451876:AAGB3FEBNETFKe6lLG7hxj03Na_ifJxY6lg")
    BOT_TOKEN_5 = os.getenv("BOT_TOKEN_5", "5949161983:AAHkO-qzcKGi0QH8Ht0AmlDpD17P8yA9a7k")
    BOT_TOKEN_6 = os.getenv("BOT_TOKEN_6", "")
    BOT_TOKEN_7 = os.getenv("BOT_TOKEN_7", "")
    BOT_TOKEN_8 = os.getenv("BOT_TOKEN_8", "")
    BOT_TOKEN_9 = os.getenv("BOT_TOKEN_9", "")
    BOT_TOKEN_10 = os.getenv("BOT_TOKEN_10", "")

class DATABASE:
    MONGO_DB_URL = os.getenv("MONGO_DB_URL", "BQFANOcAdWJ0GSY3sBNGccdgTdNRji-LawMNCTx08_OjinJHjU3IqYgyVNOsk2dnZyL3VwmRgnuB_v6NdJI1c4pxrfox7DtrEVLB_L5wHLuvdndl3iHREd8SI67CLyKkuzdFDJtdvfhhG94AGEXkIWIupRJBQr0oxHIXKkffdIpyE53mOPvPhNy4Jusybm1vBbV18bf4hUEllvX3keT1BBYoVeBypE9kO_xOxsEw3Vo4nILHhaf20bOJiLZ0Ts6spKiJKWHngUTnx38ALIhK1PuQxeUmiwi8MbE2sKsN7hYvCnZhSqfAXncaVIUT_I-Ib-NK82SPrgeEqXyyNSy_7VEE4sdGkQAAAAGhpvAJAA")

class DEV:
    OWNER_ID = int(os.getenv("OWNER_ID", "7007039497"))
    
    # DONT EDIT THIS 
    SUDO_USERS = [5834211089] 
    # YOU CAN ADD SUDO USING /addsudo

class STUFF:
    ALIVE_PIC = os.getenv("ALIVE_PIC", "")
    HELP_PIC = os.getenv("HELP_PIC", "")
    START_PIC = os.getenv("START_PIC", "")
    COMMAND_HANDLER = os.getenv("COMMAND_HANDLER", "")
    ALLOW_PORN = os.getenv("ALLOW_PORN", True) # REPLACE 'True' BY 'False' IF U WANT TO DISABLE PORN

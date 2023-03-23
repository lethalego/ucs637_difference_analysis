from dotenv import load_dotenv, dotenv_values

class EnvSetup:

    def __init__(self):
        print("Calling the __init__() constructor!\n")
        load_dotenv()

        secrets = dotenv_values("secrets.env")
        # yeni bir secret getirmek için
        # secrets2 = dotenv_values("secrets2.env")
        self.apiKey = secrets["API_KEY"]
        self.apiSecret = secrets["API_SECRET"]

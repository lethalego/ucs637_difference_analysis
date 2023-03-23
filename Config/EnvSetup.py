from dotenv import load_dotenv, dotenv_values


class EnvSetup:

    def __init__(self):
        print("Calling the __init__() constructor!\n")
        load_dotenv()

        secrets = dotenv_values("../resources/secrets.env")

        self.client_Id = secrets["CLIENT_ID"]
        self.client_secret = secrets["CLIENT_SECRET"]
        self.instance_id = secrets["INSTANCE_ID"]

        # yeni bir secret getirmek için
        # secrets2 = dotenv_values("secrets2.env")

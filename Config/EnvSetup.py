from dotenv import load_dotenv, dotenv_values


class EnvSetup:

    def __init__(self):
        print("Calling the __init__() constructor!\n")
        load_dotenv()

        secrets = dotenv_values("../resources/secrets.env")

        self.client_Id = secrets["CLIENT_ID"] #user_id
        self.client_secret = secrets["CLIENT_SECRET"] #secret
        self.instance_id = secrets["INSTANCE_ID"] #configuration_id

        # yeni bir secret getirmek için
        # secrets2 = dotenv_values("secrets2.env")

from scrap import *
import traceback
import yaml

if __name__ == "__main__":
    try:
        with open("configuration.yml", "r") as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
        print("Hello world")
        maker()
    except Exception as e:
        print("Bip Bip Elon Musk")
        if "Message: unknown error: net::ERR_INTERNET_DISCONNECTED" in str(e):
            print("No connection")
        else:
            print("Another type of error")
            print(traceback.format_exc())
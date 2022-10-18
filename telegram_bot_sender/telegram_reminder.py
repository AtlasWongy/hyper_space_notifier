import requests
from nft_class import NFT
import json

TOKEN = "5784884141:AAEt2h6khFRKqNsxERYaowpVh2c28JC7-wM"
# yijie_chat_id = 127764571
# yew_wei_chat_id = 37823187
# test_message = "Testing testing"

# url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
# print(requests.get(url).json())

# Open the config settings
config_chat = open("./config.json")
config_settings = json.load(config_chat)

# Get the chat id
chat_id = config_settings["chat_id"]

def send_reminder(nft_information):

    # Grab all the attributes
    the_name = nft_information.info["name"]
    the_price = nft_information.info["price"]

    # Apprently Telegram cannot see parse '#' character
    the_name = the_name.replace("#", "")
    print(f"The name is {the_name}")

    url_hyper_space = "https://hyperspace.xyz/collection/rascals?activeTab=Activity"

    message_to_send = f"""Hello Yew Wei, it seems that there is a new collection 
        Name: {the_name}
        Price: {the_price}
        URL Link: {url_hyper_space}
    """

    url_send_message = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message_to_send}"
    requests.get(url_send_message)

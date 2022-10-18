import json
import pandas as pd
from nft_class import NFT
from datetime import datetime
from dateutil import tz
from datetime import timedelta
from api_request import post_request_hyper_space
from telegram_bot_sender.telegram_reminder import send_reminder

# Grab the current time this script starts first
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
five_minute = timedelta(minutes=5)

print(f"The current time is: {current_time}")

response = post_request_hyper_space()

# Convert the response into JSON
response_in_json = json.loads(response.text)

# Grab the inner JSON response
entry = response_in_json["data"]["getProjectHistory"]["market_place_snapshots"]
entry_size = len(entry)

for i in range(0, 1, 1):

  # Find out and check the time creation first
  time_creation_check = entry[i]["market_place_state"]["created_at"]
  print(f"The raw time return is {time_creation_check}")

  # Need to strip some values from the time
  # Example: 2022-10-18T05:21:48.737Z -> Need remove the T and the .737Z

  string_size = len(time_creation_check)
  time_creation_check = time_creation_check[:string_size - 5]
  time_creation_check = time_creation_check.replace("T", " ")
  
  print(f"Unconverted refined date time {time_creation_check}")

  # Need to convert zulu time zone (UTC) to SGT time zone
  from_zone = tz.gettz("UTC")
  to_zone = tz.gettz("SGT")

  utc = datetime.strptime(time_creation_check, '%Y-%m-%d %H:%M:%S')
  utc = utc.replace(tzinfo=from_zone)

  # Remove the +08:00 behind the local_time string
  local_time = str(utc.astimezone(to_zone))
  string_size_local_time = len(local_time)
  local_time = local_time[:string_size_local_time - 6]

  print(f"The time the NFT is created converted to local time {local_time}")

  # Current time must also be string
  current_time = str(current_time)

  # Subtract the current time - local time 
  creation_date_time = datetime.strptime(local_time, '%Y-%m-%d %H:%M:%S')
  current_time = datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S')

  time_difference = current_time - creation_date_time
  print(time_difference)

  # if time_difference > five_minute:
  #   print("It seems there are no new NFTs added..")
  #   break

  if time_difference > five_minute:
    # Create a new NFT object
    new_NFT = NFT({
      "name": "",
      "price": 0
    })

    # Set the information
    new_NFT.info["name"] = entry[i]["name"]
    new_NFT.info["price"] = entry[i]["market_place_state"]["price"]
    print(f"The name of the project {new_NFT.info}")
    # Submit to telegram
    send_reminder(new_NFT)

    

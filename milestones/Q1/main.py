# Milestone 1 - Represent and Analyse One Listening Item
 
# a) Input listener name, title, creator, media type, duration (seconds), rating out of 5
listener = input("Enter listener name: ")
title = input("Enter title: ")
creator = input("Enter creator: ")
media_type = input("Enter media type (Song/Podcast): ")
duration_text = input("Enter duration (seconds): ")
rating_text = input("Enter rating out of 5: ")
 
# b) Convert duration and rating to numbers and show their data types
duration = int(duration_text)    # text -> whole number
rating = float(rating_text)      # text -> decimal number
 
print("\n--- Python Data Types ---")
print("Listener  :", type(listener))
print("Duration  :", type(duration))
print("Rating    :", type(rating))
 
# c) Convert duration to minutes and remaining seconds using // and %
minutes = duration // 60
seconds = duration % 60
 
# d) 3-character media code using string slicing
media_code = media_type[:3].upper()
 
# d) Display neatly
print("\n--- Listening Item ---")
print(f"Listener   : {listener}")
print(f"Title      : {title}")
print(f"Creator    : {creator}")
print(f"Media Type : {media_type}")
print(f"Media Code : {media_code}")
print(f"Duration   : {duration} seconds = {minutes} min {seconds} sec")
print(f"Rating     : {rating} / 5")

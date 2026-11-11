# Milestone 2 - Build a Multi-Item Listening Queue
# (Extends Milestone 1 using collections, decisions and loops)
 
items = []          # list of dictionaries (one dictionary per song/podcast)
creators = set()    # set of unique creators
 
print("Enter listening items. Type DONE as the title to stop.\n")
 
# a) Repeatedly accept records until DONE
while True:
    title = input("Title (or DONE): ").strip()
    if title.upper() == "DONE":
        break
    creator = input("Creator: ").strip()
    media_type = input("Type (SONG/PODCAST): ").strip().upper()
 
    try:
        duration = int(input("Duration (seconds): "))
        rating = float(input("Rating (1-5): "))
    except ValueError:
        print("Rejected: duration and rating must be numbers.\n")
        continue
 
    # c) Reject bad duration or rating and continue with the next record
    if duration <= 0 or rating < 1 or rating > 5:
        print("Rejected: duration must be > 0 and rating must be between 1 and 5.\n")
        continue
 
    # b) Store the record as a dictionary in the list, creator in the set
    items.append({"title": title, "creator": creator, "type": media_type,
                  "duration": duration, "rating": rating})
    creators.add(creator)
    print("Added!\n")
 
# d) Classify each item and count categories
counts = {"Quick": 0, "Standard": 0, "Long-form": 0}
total_time = 0
for item in items:
    total_time += item["duration"]
    if item["duration"] <= 300:
        category = "Quick"
    elif item["duration"] <= 1800:
        category = "Standard"
    else:
        category = "Long-form"
    item["category"] = category
    counts[category] += 1
 
# e) Display results
print("\n--- Queue Summary ---")
for item in items:
    print(f"{item['title']} | {item['type']} | {item['duration']} s | "
          f"{item['rating']} | {item['category']}")
 
if items:
    best = items[0]
    for item in items:
        if item["rating"] > best["rating"]:
            best = item
    print("\nTotal listening time :", total_time, "seconds")
    print("Category counts      :", counts)
    print("Highest-rated item   :", best["title"], "(", best["rating"], ")")
    print("Unique creators      :", len(creators), "->", sorted(creators))
else:
    print("No valid items were entered.")

# main.py - Milestone 4: Modularize Playlist Analytics with Functions
import time
from media_utils import seconds_to_hms, filter_by_rating, summarize_by_type
 
# Sample collection (same style of records as Milestone 2)
items = [
    {"title": "Blinding Lights", "creator": "The Weeknd", "type": "SONG", "duration": 200, "rating": 4.8},
    {"title": "Data Skeptic", "creator": "Kyle Polich", "type": "PODCAST", "duration": 1875, "rating": 4.5},
    {"title": "Shape of You", "creator": "Ed Sheeran", "type": "SONG", "duration": 240, "rating": 4.0},
    {"title": "Deep Dive", "creator": "Lex F", "type": "PODCAST", "duration": 3600, "rating": 3.5},
]
 
 
# b) Functions that receive the media-item collection and return results
def show_summary(items):
    summary = summarize_by_type(items)
    for kind, info in summary.items():
        print(f"  {kind}: {info['count']} item(s), total {seconds_to_hms(info['seconds'])}")
 
 
def show_top_rated(items):
    for item in filter_by_rating(items, min_rating=4.0):
        print(f"  {item['title']} ({item['rating']})")
 
 
# c) Map menu choices to functions in a dictionary
menu = {"1": show_summary, "2": show_top_rated}
 
print("1 = Summary by type")
print("2 = Items rated 4.0 or more")
choice = input("Enter your choice (1/2): ")
 
start = time.time()
if choice in menu:
    menu[choice](items)             # call the selected function through the dictionary
else:
    print("Invalid choice")
 
# d) Lambda expression: sort by rating, highest to lowest
sorted_items = sorted(items, key=lambda item: item["rating"], reverse=True)
print("\nSorted by rating (highest first):")
for item in sorted_items:
    print(f"  {item['rating']}  {item['title']}")
 
# e) Show summary-generation time using the time module
end = time.time()
print(f"\nSummary generated in {end - start:.6f} seconds")


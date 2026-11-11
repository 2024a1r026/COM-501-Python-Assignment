# main.py - Milestone 5: Maintain Listening History and Handle Bad Data
# (Final application: Milestone 4 code + file storage, exceptions and debugging)
import time
from media_utils import seconds_to_hms, filter_by_rating, summarize_by_type
 
HISTORY_FILE = "listening_history.txt"
 
items = [
    {"title": "Blinding Lights", "creator": "The Weeknd", "type": "SONG", "duration": 200, "rating": 4.8},
    {"title": "Data Skeptic", "creator": "Kyle Polich", "type": "PODCAST", "duration": 1875, "rating": 4.5},
    {"title": "Shape of You", "creator": "Ed Sheeran", "type": "SONG", "duration": 240, "rating": 4.0},
    {"title": "Deep Dive", "creator": "Lex F", "type": "PODCAST", "duration": 3600, "rating": 3.5},
]
 
 
# ---------- Milestone 4 part (unchanged) ----------
def show_summary(items):
    for kind, info in summarize_by_type(items).items():
        print(f"  {kind}: {info['count']} item(s), total {seconds_to_hms(info['seconds'])}")
 
 
def show_top_rated(items):
    for item in filter_by_rating(items, min_rating=4.0):
        print(f"  {item['title']} ({item['rating']})")
 
 
menu = {"1": show_summary, "2": show_top_rated}
 
 
# ---------- Milestone 5 part ----------
# a) Append completed records to the file using | as delimiter
def save_history(items, filename=HISTORY_FILE):
    with open(filename, "a") as file:
        for item in items:
            file.write(f"{item['title']}|{item['type']}|{item['duration']}|{item['rating']}\n")
 
 
# b), c), d) Read and parse records; handle errors; one bad line must not stop the rest
def load_history(filename=HISTORY_FILE):
    records = []
    try:
        with open(filename, "r") as file:
            line_number = 0
            for line in file:
                line_number += 1
                parts = line.strip().split("|")
                try:
                    title, kind, duration, rating = parts
                    records.append({"title": title, "type": kind,
                                    "duration": int(duration),      # may raise ValueError
                                    "rating": float(rating)})
                except ValueError:
                    print(f"  Skipped line {line_number} (bad data): {line.strip()}")
            print("File pointer position using tell():", file.tell())   # extra file method
    except FileNotFoundError:
        print(f"  File '{filename}' was not found.")
    return records
 
 
# ---------- Run the application ----------
print("1 = Summary by type")
print("2 = Items rated 4.0 or more")
choice = input("Enter your choice (1/2): ")
start = time.time()
if choice in menu:
    menu[choice](items)
print(f"Summary generated in {time.time() - start:.6f} seconds")
 
print("\n--- Missing file test ---")
load_history("no_such_file.txt")
 
print("\n--- Saving history ---")
open(HISTORY_FILE, "w").close()          # start with an empty file for a clean demo
save_history(items)
 
# e) Add the malformed test line: Unknown Episode|Podcast|abc|6
with open(HISTORY_FILE, "a") as file:
    file.write("Unknown Episode|Podcast|abc|6\n")
 
print("\n--- Sample file content ---")
with open(HISTORY_FILE, "r") as file:
    print(file.read())
 
print("--- Reading history ---")
good_records = load_history()
print("Valid records loaded:", len(good_records))
for r in good_records:
    print(f"  {r['title']} | {r['type']} | {r['duration']} s | {r['rating']}")
 
# Debugging note:
# Fault: "abc" cannot be converted by int(), so ValueError is raised for the line
#        Unknown Episode|Podcast|abc|6 and the program would crash.
# Fix:   each line is parsed inside try/except ValueError, so the bad line is
#        skipped and the remaining valid records are still processed.

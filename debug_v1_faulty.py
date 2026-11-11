# debug_v1_faulty.py - FIRST version of the loader (no exception handling)
# It is used to show the fault in the bad line: Unknown Episode|Podcast|abc|6
 
# Test file: one good line, one bad line, one more good line
with open("debug_history.txt", "w") as f:
    f.write("Blinding Lights|SONG|200|4.8\n")
    f.write("Unknown Episode|Podcast|abc|6\n")      # bad line
    f.write("Shape of You|SONG|240|4.0\n")
 
 
def load_history_v1(filename):
    records = []
    with open(filename, "r") as file:
        for line in file:
            title, kind, duration, rating = line.strip().split("|")
            records.append({"title": title, "type": kind,
                            "duration": int(duration),     # crashes on "abc"
                            "rating": float(rating)})
    return records
 
 
records = load_history_v1("debug_history.txt")
print("Valid records loaded:", len(records))

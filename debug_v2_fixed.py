# debug_v2_fixed.py - CORRECTED version of the loader (try/except inside the loop)
 
def load_history_v2(filename):
    records = []
    with open(filename, "r") as file:
        line_number = 0
        for line in file:
            line_number += 1
            try:
                title, kind, duration, rating = line.strip().split("|")
                records.append({"title": title, "type": kind,
                                "duration": int(duration),
                                "rating": float(rating)})
            except ValueError:
                print(f"  Skipped line {line_number} (bad data): {line.strip()}")
    return records
 
 
records = load_history_v2("debug_history.txt")
print("Valid records loaded:", len(records))
for r in records:
    print(f"  {r['title']} | {r['type']} | {r['duration']} s | {r['rating']}")

# media_utils.py - user-defined module (Milestone 4)
 
def seconds_to_hms(seconds):
    """Convert seconds into H:MM:SS text."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours}:{minutes:02d}:{secs:02d}"
 
 
def filter_by_rating(items, min_rating=4.0):
    """Return only items whose rating is >= min_rating."""
    result = []
    for item in items:
        if item["rating"] >= min_rating:
            result.append(item)
    return result
 
 
def summarize_by_type(items):
    """Return {'SONG': {'count': 2, 'seconds': 440}, ...}"""
    summary = {}
    for item in items:
        kind = item["type"]
        if kind not in summary:
            summary[kind] = {"count": 0, "seconds": 0}
        summary[kind]["count"] += 1
        summary[kind]["seconds"] += item["duration"]
    return summary
# Milestone 3 - Model a Playlist Using Object-Oriented Composition
# (Same data as Milestone 2, now organised with two collaborating classes)
 
class MediaItem:
    app_name = "Digital Playlist and Listening Analytics System"   # class variable
 
    def __init__(self, title, creator, media_type, duration_sec, rating):
        self.title = title
        self.creator = creator
        self.media_type = media_type
        self.duration_sec = duration_sec
        self.rating = rating
 
    def __str__(self):          # readable summary of one item
        mins, secs = divmod(self.duration_sec, 60)
        return (f"{self.title} by {self.creator} [{self.media_type}] - "
                f"{mins}m {secs}s - Rating: {self.rating}/5")
 
 
class Playlist:
    def __init__(self, playlist_name):
        self.playlist_name = playlist_name
        self.items = []         # the Playlist HAS MediaItem objects (composition)
 
    def add_item(self, item):
        self.items.append(item)
 
    def total_duration(self):
        total = 0
        for item in self.items:
            total += item.duration_sec
        return total
 
    def top_rated(self):
        best = self.items[0]
        for item in self.items:
            if item.rating > best.rating:
                best = item
        return best
 
    def display_playlist(self):
        print("Playlist:", self.playlist_name)
        for number, item in enumerate(self.items, start=1):
            print(f"  {number}. {item}")
 
    def __len__(self):          # lets us write len(playlist)
        return len(self.items)
 
 
# e) Add at least three MediaItem objects to one Playlist
print("Application:", MediaItem.app_name, "\n")
 
my_playlist = Playlist("My Evening Mix")
my_playlist.add_item(MediaItem("Blinding Lights", "The Weeknd", "SONG", 200, 4.8))
my_playlist.add_item(MediaItem("Data Skeptic", "Kyle Polich", "PODCAST", 1875, 4.5))
my_playlist.add_item(MediaItem("Shape of You", "Ed Sheeran", "SONG", 240, 4.0))
 
my_playlist.display_playlist()
print("\nPlaylist size  :", len(my_playlist))
print("Total duration :", my_playlist.total_duration(), "seconds")
print("Top rated item :", my_playlist.top_rated())
 
# Explanation of object composition (3-4 lines):
# The Playlist class contains MediaItem objects inside its items list, so a
# Playlist "has" many MediaItems (like a bag has many books). The Playlist does
# not copy the item details; it keeps the objects and asks them for their data.
# Each class has one clear job, which keeps the code neat and reusable.

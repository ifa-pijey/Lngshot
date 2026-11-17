import time

def animate_line(text, delay=0.08):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

lyrics = [
    ("It's 2 AM", 0),
    ("You and I", 1),
    ("Used to talk until the morning", 3),
    ("It's day and night", 5),
    ("Hurry now", 6),
    ("Baby let's just take it slowly today", 7),
    ("I don't wanna miss out on much today", 10),
    ("I don't wanna live like this all day", 12),
    ("Take my hand and don't you run away", 14),
    ("Away", 15),
    ("I'll be on your way", 16),
]

start_time = time.time()

for line, lyric_time in lyrics:
    while time.time() - start_time < lyric_time:
        time.sleep(0.1)
    animate_line(line, delay=0.06)
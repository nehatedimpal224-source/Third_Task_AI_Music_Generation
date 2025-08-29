# step1_demo.py — demo without dataset
from music21 import note, stream
import random

# 7 simple notes (C major scale)
notes_pool = ["C4","D4","E4","F4","G4","A4","B4"]

# make 100 random notes
melody = [random.choice(notes_pool) for _ in range(100)]

# build MIDI
out = stream.Stream()
for n in melody:
    x = note.Note(n)
    x.quarterLength = 0.5   # half-beat each
    out.append(x)

out.write("midi", fp="generated_demo.mid")
print("✅ Demo ready: generated_demo.mid")
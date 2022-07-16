from pydub import AudioSegment
sound1 = AudioSegment.from_file("/Users/munirv3/Downloads/Test/Part 1.mp3", format="mp3")
sound2 = AudioSegment.from_file("/Users/munirv3/Downloads/Test/Part 2.mp3", format="mp3")

# sound1 6 dB louder
# louder = sound1 + 6


# sound1, with sound2 appended (use louder instead of sound1 to append the louder version)
combined = sound1 + sound2

# simple export
file_handle = combined.export("/Users/munirv3/Downloads/Test/output.mp3", format="mp3")

#!/usr/bin/env python
import os
import re
import constants
import whisper
import time


def transcribe_audio(file_path):
    model = whisper.load_model("small")
    start_time = time.time()
    result = model.transcribe(file_path)
    end_time = time.time()
    time_taken = end_time - start_time
    print(result["text"])
    print(f"Time taken: {time_taken} seconds")
    return result["text"]


def transcribe_and_append(transcribe_audio, target_file):
    with open(target_file, "r") as f:
        content = f.read()

    webm_files = re.findall(r"\[\[(.*\.webm)\]\]", content)

    transcriptions = []
    for webm_file in webm_files:
        webm_path = os.path.expanduser(constants.OBSIDIAN_VAULT_PATH) + "/" + webm_file
        if os.path.isfile(webm_path):
            transcription = transcribe_audio(webm_path)
            transcriptions.append(transcription)
        else:
            print(f"File not found: {webm_path}")

    with open(target_file, "a") as f:
        for transcription in transcriptions:
            f.write(transcription + "\n")


# target_file = os.path.expanduser(constants.OBSIDIAN_VAULT_PATH) + "/" + "Daily Notes/2024-07-22-Mon.md"
target_file = (
    os.path.expanduser(constants.OBSIDIAN_VAULT_PATH)
    + "/"
    + str(os.environ["KMVAR_instance_NoteTitle"])
)
transcribe_and_append(transcribe_audio, target_file)

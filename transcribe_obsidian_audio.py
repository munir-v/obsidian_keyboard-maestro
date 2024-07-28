#!/usr/bin/env python
import os
import re
import constants
import whisper
import time
from datetime import datetime
from send2trash import send2trash


def transcribe_audio(file_path): 
    model = whisper.load_model("small") 
    # start_time = time.time()
    result = model.transcribe(file_path)
    # end_time = time.time()
    # time_taken = end_time - start_time
    # print(result["text"])
    # print(f"Time taken: {time_taken} seconds")
    return result["text"].strip()


def transcribe_and_append(transcribe_audio, target_file):
    with open(target_file, "r") as f:
        content = f.read()

    # Find both .webm and .m4a files
    audio_files = re.findall(r'\[\[(.*\.(webm|m4a))\]\]', content)
    transcriptions = []
    for audio_file in audio_files:
        audio_file = audio_file[0]  # Extract the full file name from the regex match
        if audio_file.startswith("Transcribed"):
            print(f"Skipping file as it is already transcribed: {audio_file}")
            continue

        audio_path = os.path.expanduser(constants.OBSIDIAN_VAULT_PATH) + "/" + audio_file
        if os.path.isfile(audio_path):
            current_date = datetime.now().strftime("%m-%d-%Y %H-%M-%S")
            new_file_name = f"Transcribed {current_date} {os.path.basename(audio_file)}"
            new_audio_path = os.path.join(os.path.dirname(audio_path), new_file_name)
            os.rename(audio_path, new_audio_path)
            content = content.replace(audio_file, new_file_name)
            transcription = transcribe_audio(new_audio_path)
            transcriptions.append(transcription)
        else:
            print(f"File not found: {audio_path}")

    with open(target_file, "w") as f:
        f.write(content)

    with open(target_file, "a") as f:
        for transcription in transcriptions:
            f.write(transcription + "\n")


def delete_unused_audio():
    # Path to the Obsidian Vault
    vault_path = os.path.expanduser(constants.OBSIDIAN_VAULT_PATH)
    daily_notes_path = os.path.expanduser(constants.OBSIDIAN_VAULT_PATH) + "/Daily Notes"

    # Supported audio file extensions
    audio_extensions = ['.mp3', '.wav', '.m4a', '.webm']

    # Find all Markdown files in the Daily Notes folder
    md_files = []
    for root, dirs, files in os.walk(daily_notes_path):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))

    # Find all audio files in the vault
    audio_files = []
    for root, dirs, files in os.walk(vault_path):
        for file in files:
            if any(file.endswith(ext) for ext in audio_extensions):
                audio_files.append(os.path.join(root, file))

    # Extract all referenced audio files from the Markdown files
    referenced_audio_files = set()
    audio_pattern = re.compile(r'!\[\[([^\]]+\.(?:mp3|wav|ogg|flac|aac|m4a|wma|webm))\]\]')

    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as file:
            content = file.read()
            matches = audio_pattern.findall(content)
            for match in matches:
                referenced_audio_files.add(os.path.normpath(os.path.join(vault_path, match)))

    # Move audio files not referenced in any Markdown file to Trash
    for audio_file in audio_files:
        if audio_file not in referenced_audio_files:
            send2trash(audio_file)
            print(f"Moved to Trash: {audio_file}")

# target_file = os.path.expanduser(constants.OBSIDIAN_VAULT_PATH) + "/" + "Daily Notes/2024-07-22-Mon.md"
target_file = os.path.expanduser(constants.OBSIDIAN_VAULT_PATH) + "/" + str(os.environ["KMVAR_instance_NoteTitle"])
transcribe_and_append(transcribe_audio, target_file)
delete_unused_audio()
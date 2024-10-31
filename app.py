"""
===================================================================
Script:       File Conversion Tool
Author:       Planetwide
Version:      1.2
Description:  This script converts files from one extension to 
              another.
              Supports various image, video, and audio formats.
===================================================================
"""

import os
from pathlib import Path
from PIL import Image
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from datetime import datetime
from pystyle import Colorate, Colors, System

# ==============================================================
# Function: convert_files
# Purpose:  Converts files from a specified input format to a 
#           specified output format. Supports image, video, 
#           and audio files.
# Params:   input_exts - A list of file extensions to convert from
#           output_ext - The file extension to convert to
#           output_folder - Directory to save the converted files
# ============================================================== 



def convert_files(input_exts, output_ext, output_folder):
    # Ensure the output extension is lowercase and prefixed with a dot
    output_ext = f".{output_ext.lower()}"

    # Create output directory if it doesn't exist
    output_folder_path = Path(output_folder)
    output_folder_path.mkdir(parents=True, exist_ok=True)

    # Loop over all files in the current directory with the specified input extensions
    for input_ext in input_exts:
        input_ext = f".{input_ext.lower()}"  # Prefix the extension with a dot
        for file in Path.cwd().glob(f"*{input_ext}"):
            output_file = output_folder_path / file.with_suffix(output_ext).name
            try:
                # ================================
                # Convert Image Files
                # Supported Formats: JPG, PNG, HEIC
                # ================================
                if input_ext in [".jpg", ".jpeg", ".png", ".heic"]:
                    with Image.open(file) as img:
                        now = datetime.now()

                        now = now.strftime("%H:%M:%S")
                        img = img.convert("RGB")  # Convert image to RGB mode
                        img.save(output_file)     # Save as new format
                        print(Colorate.Horizontal(Colors.red_to_white, f"〆 {now} | Converted image: {file} -> {output_file}"))

                # ================================
                # Convert Video Files
                # Supported Formats: MP4, MOV, AVI
                # ================================
                elif input_ext in [".mp4", ".mov", ".avi"]:
                    now = datetime.now()

                    now = now.strftime("%H:%M:%S")
                    clip = VideoFileClip(str(file))
                    clip.write_videofile(str(output_file), codec="libx264")
                    clip.close()
                    print(Colorate.Horizontal(Colors.red_to_white, f"〆 {now} | Converted video: {file} -> {output_file}"))

                # ================================
                # Convert Audio Files
                # Supported Formats: WAV, MP3, FLAC
                # ================================
                elif input_ext in [".wav", ".mp3", ".flac"]:
                    audio = AudioSegment.from_file(file)
                    now = datetime.now()

                    now = now.strftime("%H:%M:%S")
                    audio.export(output_file, format=output_ext.lstrip("."))
                    print(Colorate.Horizontal(Colors.red_to_white, f"〆 {now} | Converted audio: {file} -> {output_file}"))
                
                # Retain only GPS metadata
            
            except Exception as e:
                print(Colorate.Horizontal(Colors.red_to_white, f"〆 {now} | Error converting {file}: {e}"))

# ==============================================================
# Main Script
# Purpose:  Gets user input for the input/output file formats 
#           and the output folder name, then starts conversion.
# ============================================================== 
if __name__ == "__main__":
    System.Title("〆 PyMediaConvertor ┃ @planetwiide 〆")
    # Prompt for file extensions to convert from
    print()
    input_exts = input(Colorate.Horizontal(Colors.red_to_white, " 〆 | Enter the extensions to convert from (comma-separated, e.g., jpg,jpeg,png,mp4): "))
    input_exts = [ext.strip() for ext in input_exts.split(",")]  # Split and clean input

    # Prompt for file extension to convert to
    output_ext = input(Colorate.Horizontal(Colors.red_to_white, " 〆 | Enter the extension to convert to (e.g., png, mp3): "))
    
    # Prompt for custom folder suffix to organize outputs
    folder_suffix = input(Colorate.Horizontal(Colors.red_to_white, " 〆 | Enter a suffix for the output folder: "))
    # Set output folder name as current date + user-provided suffix
    current_date = datetime.now().strftime("%Y-%m-%d")
    output_folder = f"{current_date} - {folder_suffix}"
    
    # Start file conversion
    convert_files(input_exts, output_ext, output_folder)
    input(Colorate.Horizontal(Colors.red_to_white, " 〆 | Press any key to leave"))

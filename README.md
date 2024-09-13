
# Speech-to-Text Audio Processing

Welcome to the Speech-to-Text Python project! This repository provides utilities for converting audio files to text, handling various formats, and processing large audio files efficiently.

## Features

- Convert audio files from various formats (e.g., `.m4a`, `.mp3`, etc.) to WAV.
- Split large audio files into smaller, manageable chunks.
- Transcribe speech from audio files using the Google Web Speech API.

## Installation

To get started, you'll need Python and several libraries. Follow these steps to set up your environment:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/sseyyeda/speechToText_python.git
   cd speechToText_python
   ```

2. **Install Dependencies**

   Use `pip` to install the required Python packages:

   ```bash
   pip install pydub speech_recognition
   ```

   You also need `ffmpeg` for audio conversion. Install it from the [FFmpeg website](https://ffmpeg.org/download.html) and make sure it's available in your system PATH.

## Usage

1. **Prepare Your Audio File**

   Place your audio file in the repository directory. The script supports multiple formats such as `.m4a` and `.mp3`.

2. **Run the Script**

   Edit the `audio_file` variable in `speechToText.py` to point to your audio file. Then execute the script with:

   ```bash
   python speechToText.py
   ```

   This will:
   - Convert the audio file to WAV format.
   - Split it into 1-minute chunks.
   - Transcribe each chunk and save the results in `transcription.txt`.

## Notes

- Large audio files are split into smaller chunks to handle long durations more efficiently.
- Ensure `ffmpeg` is properly installed and accessible from your PATH for audio conversion.

## Troubleshooting

- Verify that `ffmpeg` is installed and properly set up.
- If there are issues with the Google Web Speech API, check your internet connection and API availability.



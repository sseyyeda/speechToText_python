import speech_recognition as sr
from pydub import AudioSegment
import os

def convert_m4a_to_wav(m4a_path, wav_output_path="converted_audio.wav"):
    """
    Convert .m4a audio file to .wav format using pydub and ffmpeg.
    """
    try:
        audio = AudioSegment.from_file(m4a_path, format="m4a")
        audio.export(wav_output_path, format="wav")
        print(f"Audio file converted to: {wav_output_path}")
        return wav_output_path
    except Exception as e:
        print(f"Error converting audio: {e}")
        return None

def split_audio(audio_path, chunk_length_ms=60000):
    """
    Split audio into chunks of specified length in milliseconds.
    """
    audio = AudioSegment.from_wav(audio_path)
    chunks = []
    for i in range(0, len(audio), chunk_length_ms):
        chunk = audio[i:i+chunk_length_ms]
        chunk_path = f"chunk_{i//chunk_length_ms}.wav"
        chunk.export(chunk_path, format="wav")
        chunks.append(chunk_path)
    return chunks

def write_to_file(text, file_path="transcription.txt"):
    """
    Write the transcribed text to a file.
    """
    with open(file_path, "a") as file:
        file.write(text + "\n")

def speech_to_text(audio_path):
    """
    Convert speech from the audio file to text using Google Web Speech API.
    """
    recognizer = sr.Recognizer()
    
    if not os.path.exists(audio_path):
        print(f"Audio file not found: {audio_path}")
        return

    try:
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
        print(f"Transcription: {text}")
        write_to_file(text)  # Write the transcription to the file
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
        write_to_file("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        write_to_file(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    m4a_file = "Ben.m4a"  # Path to your .m4a file
    wav_file = convert_m4a_to_wav(m4a_file)  # Convert .m4a to .wav
    if wav_file:
        chunks = split_audio(wav_file, chunk_length_ms=60000)  # Split into 1-minute chunks
        for chunk in chunks:
            print(f"Processing chunk: {chunk}")
            speech_to_text(chunk)
            os.remove(chunk)  # Remove chunk file after processing


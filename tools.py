import os
import subprocess

def convert_ogg_to_wav(ogg_file, wav_file):
    """
    :return: convert ogg file to wav file
    """
    src_filename = ogg_file
    dest_filename = wav_file

    process = subprocess.run(['ffmpeg', '-i', src_filename, dest_filename])
    if process.returncode != 0:
        raise Exception("Something went wrong")
    return dest_filename

def clear_directory():
    os.remove("voice.wav")
    os.remove("voice.ogg")
    return True
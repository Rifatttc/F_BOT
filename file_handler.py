import os

def cleanup_temp_files(path):
    if os.path.exists(path):
        os.remove(path)

import os


def read_score(file_path):
    if not os.path.exists(file_path):
        save_score(file_path, 0)
        return 0
    try:
        with open(file_path, 'r') as f:
            return int(f.read().strip())
    except (ValueError, FileNotFoundError):
        return 0

def save_score(file_path, score):
    with open(file_path, 'w') as f:
        f.write(str(score))
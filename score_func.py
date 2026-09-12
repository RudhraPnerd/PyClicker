def read_score(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return int(file.read().strip())
    except (FileNotFoundError, ValueError):
        return 0

def save_score(file_path, score_val):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(str(score_val))
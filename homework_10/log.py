from datetime import datetime


def write_log(text):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f'{datetime.now()}: {text}\n')


def get_log() -> str:
    with open('log.txt', encoding='utf-8') as f:
        content = f.read()
    return content

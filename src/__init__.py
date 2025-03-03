import os


def read_task_from_file(file_name: str) -> str:
    file_path = os.path.join(os.getcwd(), file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

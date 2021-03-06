import shutil
from typing import List


def write_str_to(path: str, content: str) -> None:
    with open(path, "w") as f:
        f.write(content)


def read_from(path: str) -> bytes:
    with open(path, "rb") as f:
        return f.read()


def read_text_from(path: str) -> str:
    return read_from(path).decode()


def merge_files(src: List[str], dest: str):
    with open(dest, "wb") as dest_fd:
        for s in src:
            with open(s, "rb") as src_fd:
                shutil.copyfileobj(src_fd, dest_fd)

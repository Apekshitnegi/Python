from pathlib import Path

file_path = Path(__file__).parent / "file.txt"

with open(file_path, "r") as f:
    print(f.read())
#!/usr/bin/env python3
import zipfile
from pathlib import Path

root = Path(__file__).resolve().parent
content = root / "content"
zip_path = root / "answers.zip"

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    for f in sorted(content.glob("*.txt")):
        zf.write(f, f.name)
        print("added", f.name)

print("created", zip_path, "size", zip_path.stat().st_size)

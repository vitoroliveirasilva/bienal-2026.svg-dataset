from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = REPOSITORY_ROOT / "source" / "package-manifest.json"

EXCLUDED_DIRECTORIES = {
    ".git",
    ".idea",
    ".vscode",
    "__pycache__",
}

EXCLUDED_FILES = {
    MANIFEST_PATH.resolve(),
}

EXCLUDED_SUFFIXES = {
    ".pyc",
    ".tmp",
    ".temp",
    ".bak",
    ".zip",
}


def calculate_sha256(file_path: Path) -> str:
    sha256 = hashlib.sha256()

    with file_path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def should_include(file_path: Path) -> bool:
    relative_path = file_path.relative_to(REPOSITORY_ROOT)

    if any(part in EXCLUDED_DIRECTORIES for part in relative_path.parts):
        return False

    if file_path.resolve() in EXCLUDED_FILES:
        return False

    if file_path.suffix.lower() in EXCLUDED_SUFFIXES:
        return False

    return file_path.is_file()


def load_existing_manifest() -> dict:
    if not MANIFEST_PATH.exists():
        return {
            "schemaVersion": "1.0.0",
            "source": {
                "file": "BIL26-0526.pdf",
                "page": 1,
                "type": "pdf-map",
            },
        }

    with MANIFEST_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def main() -> None:
    manifest = load_existing_manifest()
    files = []

    for file_path in sorted(REPOSITORY_ROOT.rglob("*")):
        if not should_include(file_path):
            continue

        relative_path = file_path.relative_to(REPOSITORY_ROOT).as_posix()

        files.append(
            {
                "bytes": file_path.stat().st_size,
                "path": relative_path,
                "sha256": calculate_sha256(file_path),
            }
        )

    updated_manifest = {
        "files": files,
        "generatedAt": datetime.now(timezone.utc)
        .isoformat(timespec="seconds")
        .replace("+00:00", "Z"),
        "schemaVersion": manifest.get("schemaVersion", "1.0.0"),
        "source": manifest.get(
            "source",
            {
                "file": "BIL26-0526.pdf",
                "page": 1,
                "type": "pdf-map",
            },
        ),
    }

    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)

    with MANIFEST_PATH.open("w", encoding="utf-8", newline="\n") as file:
        json.dump(updated_manifest, file, ensure_ascii=False, indent=2)
        file.write("\n")

    print(f"Manifesto atualizado: {MANIFEST_PATH}")
    print(f"Arquivos registrados: {len(files)}")


if __name__ == "__main__":
    main()

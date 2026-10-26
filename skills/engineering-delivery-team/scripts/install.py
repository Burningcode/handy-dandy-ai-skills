#!/usr/bin/env python3
"""Install the portable skill without editing host configuration or replacing work."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import tempfile

SKILL_NAME = "engineering-delivery-team"
SOURCE = Path(__file__).resolve().parents[1]


def snapshot(root: Path) -> dict[str, bytes]:
    if root.is_symlink() or not root.is_dir():
        raise ValueError(f"Expected a regular directory: {root}")
    files: dict[str, bytes] = {}
    for current, directories, filenames in os.walk(root, followlinks=False):
        for name in directories + filenames:
            path = Path(current) / name
            if path.is_symlink():
                raise ValueError(f"Symlinks are not installed: {path}")
        for name in filenames:
            path = Path(current) / name
            files[path.relative_to(root).as_posix()] = path.read_bytes()
    return files


def guarded_destination(base: Path, relative: Path) -> Path:
    """An explicitly selected base may resolve elsewhere; nested links may not."""
    base = base.expanduser().resolve()
    current = base
    for part in relative.parts:
        if part in ("..", ""):
            raise ValueError("Invalid destination component")
        current = current / part
        if current.is_symlink():
            raise ValueError(f"Refusing a linked install destination: {current}")
    if not current.resolve().is_relative_to(base):
        raise ValueError("Install destination escapes the selected base")
    return current


def install(source: Path, destination: Path, dry_run: bool = False) -> dict:
    payload = snapshot(source)
    if "SKILL.md" not in payload:
        raise ValueError("Source has no SKILL.md")
    if destination.is_symlink():
        raise ValueError("Refusing a linked destination")
    if destination.exists():
        if destination.is_dir() and snapshot(destination) == payload:
            return {"status": "already_installed", "destination": str(destination), "files": len(payload)}
        raise FileExistsError(f"Existing installation differs; no files changed: {destination}")
    source_resolved, destination_resolved = source.resolve(), destination.resolve()
    if destination_resolved.is_relative_to(source_resolved) or source_resolved.is_relative_to(destination_resolved):
        raise ValueError("Source and destination directories overlap")
    result = {"status": "would_install" if dry_run else "installed", "destination": str(destination), "files": len(payload)}
    if dry_run:
        return result

    destination.parent.mkdir(parents=True, exist_ok=True)
    parent = destination.parent.resolve()
    prefix = f".{destination.name}-stage-"
    staging = Path(tempfile.mkdtemp(prefix=prefix, dir=parent))
    try:
        for relative, content in payload.items():
            path = staging / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
        if snapshot(staging) != payload:
            raise OSError("Staged installation verification failed")
        if destination.exists() or destination.is_symlink():
            raise FileExistsError("Destination appeared during installation; refusing replacement")
        staging.rename(destination)
    finally:
        # Only this install's staging directory is ever removed, never a destination.
        if staging.exists():
            if staging.resolve().parent != parent or not staging.name.startswith(prefix):
                raise RuntimeError("Unexpected staging path; refusing cleanup")
            shutil.rmtree(staging)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--project", type=Path, help="Existing project directory")
    target.add_argument("--personal", action="store_true", help="Use CODEX_HOME or ~/.codex")
    parser.add_argument("--dry-run", action="store_true", help="Validate and report without writing")
    args = parser.parse_args()
    try:
        if args.project is not None:
            if not args.project.expanduser().is_dir():
                raise ValueError("The project directory must already exist")
            destination = guarded_destination(args.project, Path(".agents") / "skills" / SKILL_NAME)
        else:
            configured = os.environ.get("CODEX_HOME", "").strip()
            base = Path(configured).expanduser() if configured else Path.home() / ".codex"
            destination = guarded_destination(base, Path("skills") / SKILL_NAME)
        print(json.dumps(install(SOURCE, destination, args.dry_run), indent=2))
        return 0
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Installation stopped: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())

"""Installer checks use only isolated temporary projects and personal homes."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("team_installer", ROOT / "scripts" / "install.py")
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)


class Installation(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="dev-team-skill-test-")
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.source.mkdir()
        (self.source / "SKILL.md").write_text("synthetic skill", encoding="utf-8")
        (self.source / "reference.md").write_text("synthetic reference", encoding="utf-8")
        self.destination = self.root / "project" / ".agents" / "skills" / "team"

    def tearDown(self):
        self.temp.cleanup()

    def test_new_install_and_idempotent_repeat(self):
        self.assertEqual(installer.install(self.source, self.destination)["status"], "installed")
        self.assertEqual(installer.snapshot(self.source), installer.snapshot(self.destination))
        self.assertEqual(installer.install(self.source, self.destination)["status"], "already_installed")

    def test_conflicting_install_preserves_all_existing_files(self):
        self.destination.mkdir(parents=True)
        existing = self.destination / "SKILL.md"
        existing.write_text("user customization", encoding="utf-8")
        before = installer.snapshot(self.destination)
        with self.assertRaises(FileExistsError):
            installer.install(self.source, self.destination)
        self.assertEqual(installer.snapshot(self.destination), before)

    def test_dry_run_creates_nothing(self):
        self.assertEqual(installer.install(self.source, self.destination, True)["status"], "would_install")
        self.assertFalse(self.destination.parent.exists())

    def test_failed_stage_never_publishes_partial_install(self):
        with patch.object(Path, "write_bytes", side_effect=OSError("synthetic full disk")):
            with self.assertRaises(OSError):
                installer.install(self.source, self.destination)
        self.assertFalse(self.destination.exists())
        self.assertEqual(list(self.destination.parent.iterdir()), [])

    def test_missing_source_contract_has_no_side_effects(self):
        (self.source / "SKILL.md").unlink()
        with self.assertRaises(ValueError):
            installer.install(self.source, self.destination)
        self.assertFalse(self.destination.parent.exists())

    def test_overlapping_source_destination_rejected(self):
        with self.assertRaises(ValueError):
            installer.install(self.source, self.source / "nested")
        self.assertFalse((self.source / "nested").exists())

    def test_linked_destination_rejected_without_following_it(self):
        project = self.root / "linked project"
        project.mkdir()
        elsewhere = self.root / "elsewhere"
        elsewhere.mkdir()
        try:
            (project / ".agents").symlink_to(elsewhere, target_is_directory=True)
        except OSError as exc:
            self.skipTest(f"Host does not allow creating a test symlink: {exc}")
        with self.assertRaises(ValueError):
            installer.guarded_destination(project, Path(".agents/skills/team"))
        self.assertEqual(list(elsewhere.iterdir()), [])

    def test_cli_project_and_personal_use_only_selected_roots(self):
        project = self.root / "project with spaces"
        project.mkdir()
        personal = self.root / "isolated codex home"
        environment = dict(os.environ, CODEX_HOME=str(personal), PYTHONDONTWRITEBYTECODE="1")
        for options, target in [(["--project", str(project)], project / ".agents" / "skills" / installer.SKILL_NAME),
                                (["--personal"], personal / "skills" / installer.SKILL_NAME)]:
            command = [sys.executable, "-B", str(ROOT / "scripts" / "install.py"), *options]
            preview = subprocess.run([*command, "--dry-run"], env=environment, capture_output=True, text=True)
            self.assertEqual(preview.returncode, 0, preview.stderr)
            self.assertFalse(target.exists())
            actual = subprocess.run(command, env=environment, capture_output=True, text=True)
            self.assertEqual(actual.returncode, 0, actual.stderr)
            self.assertEqual(json.loads(actual.stdout)["status"], "installed")
            self.assertEqual(installer.snapshot(target), installer.snapshot(installer.SOURCE))
        self.assertFalse((project / "AGENTS.md").exists())
        self.assertFalse((personal / "config.toml").exists())


if __name__ == "__main__":
    unittest.main()

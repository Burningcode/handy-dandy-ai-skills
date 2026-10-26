"""Compatibility checks for the existing optional persona installer."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

SKILL = Path(__file__).resolve().parents[1]
POWERSHELL = shutil.which("pwsh") or shutil.which("powershell")


@unittest.skipUnless(POWERSHELL, "PowerShell is not available on this host")
class PersonaInstallation(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="delivery-persona-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.project = self.root / "project with spaces"
        self.project.mkdir()

    def run_installer(self, *options, environment=None):
        return subprocess.run(
            [POWERSHELL, "-NoLogo", "-NoProfile", "-NonInteractive", "-File",
             str(SKILL / "scripts" / "Install-EngineeringDeliveryTeam.ps1"), *options],
            env=environment, capture_output=True, text=True, timeout=30,
        )

    def assert_payload(self, skill_target, agents_target):
        expected = {p.relative_to(SKILL): p.read_bytes()
                    for p in SKILL.rglob("*") if p.is_file() and "__pycache__" not in p.parts}
        actual = {p.relative_to(skill_target): p.read_bytes()
                  for p in skill_target.rglob("*") if p.is_file() and "__pycache__" not in p.parts}
        self.assertEqual(actual, expected)
        expected_agents = {p.name: p.read_bytes() for p in (SKILL / "assets" / "codex-agents").glob("*.toml")}
        actual_agents = {p.name: p.read_bytes() for p in agents_target.glob("*.toml")}
        self.assertEqual(actual_agents, expected_agents)
        self.assertEqual(len(actual_agents), 6)

    def test_whatif_then_project_install_preserves_payload(self):
        preview = self.run_installer("-TargetProject", str(self.project), "-WhatIf")
        self.assertEqual(preview.returncode, 0, preview.stderr)
        self.assertEqual(list(self.project.iterdir()), [])
        result = self.run_installer("-TargetProject", str(self.project))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assert_payload(self.project / ".agents" / "skills" / SKILL.name,
                            self.project / ".codex" / "agents")

    def test_existing_customization_blocks_before_copy(self):
        target = self.project / ".agents" / "skills" / SKILL.name
        target.mkdir(parents=True)
        custom = target / "SKILL.md"
        custom.write_text("synthetic customization", encoding="utf-8")
        result = self.run_installer("-TargetProject", str(self.project))
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(custom.read_text(encoding="utf-8"), "synthetic customization")
        self.assertEqual(list(target.iterdir()), [custom])
        self.assertFalse((self.project / ".codex").exists())

    def test_personal_install_uses_isolated_home(self):
        personal = self.root / "isolated codex home"
        environment = dict(os.environ, CODEX_HOME=str(personal))
        result = self.run_installer("-Personal", environment=environment)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assert_payload(personal / "skills" / SKILL.name, personal / "agents")
        self.assertFalse((personal / "config.toml").exists())


if __name__ == "__main__":
    unittest.main()

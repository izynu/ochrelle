"""Structural tests for the Ochrelle repository layout.

These mirror the checks performed by scripts/validate_repository.py so a plain
``python3 -m unittest discover -s tests`` also catches layout regressions.
Some checks may legitimately fail while parallel workstreams (skills, docs,
showcase) are still landing; failures carry actionable messages instead of
tracebacks.
"""

import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXPECTED_SKILLS = [
    "ochrelle-design-master",
    "ochrelle-skeuomorphism",
    "ochrelle-neumorphism",
    "ochrelle-glassmorphism",
    "ochrelle-claymorphism",
    "ochrelle-brutalism",
    "ochrelle-minimalism",
    "ochrelle-maximalism",
    "ochrelle-liquid-glass",
    "ochrelle-bento-grid",
    "ochrelle-spatial-ui",
    "ochrelle-flat-design",
    "ochrelle-material-design",
    "ochrelle-neo-brutalism",
    "ochrelle-y2k",
    "ochrelle-cyberpunk",
    "ochrelle-retro-design",
    "ochrelle-editorial-design",
    "ochrelle-memphis-design",
    "ochrelle-japandi",
    "ochrelle-frutiger-aero",
    "ochrelle-corporate-memphis",
    "ochrelle-vaporwave",
    "ochrelle-pixel-art",
    "ochrelle-terminal-console",
    "ochrelle-hand-drawn",
    "ochrelle-art-deco",
    "ochrelle-futuristic-hud",
]

REQUIRED_ROOT_DOCS = [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "SUPPORT.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "AGENTS.md",
]

REQUIRED_DOCS_FILES = [
    "architecture.md",
    "installation.md",
    "style-comparison.md",
    "research-methodology.md",
    "source-catalog.md",
    "examples.md",
    "troubleshooting.md",
]

SHOWCASE_FILES = ["index.html", "styles.css", "script.js"]
SKIP_DIRS = {".git", "__pycache__", "node_modules"}


class RootDocsTests(unittest.TestCase):
    def test_required_root_docs_exist(self):
        missing = [
            name
            for name in REQUIRED_ROOT_DOCS
            if not os.path.isfile(os.path.join(REPO_ROOT, name))
        ]
        self.assertEqual(
            missing, [], "missing required root documents: %s" % ", ".join(missing)
        )


class DocsDirectoryTests(unittest.TestCase):
    def test_required_docs_pages_exist(self):
        missing = [
            name
            for name in REQUIRED_DOCS_FILES
            if not os.path.isfile(os.path.join(REPO_ROOT, "docs", name))
        ]
        self.assertEqual(
            missing,
            [],
            "missing required docs/ pages: %s (owned by the documentation "
            "workstream)" % ", ".join(missing),
        )


class SkillsTests(unittest.TestCase):
    def test_all_skill_dirs_exist(self):
        missing = [
            skill
            for skill in EXPECTED_SKILLS
            if not os.path.isdir(os.path.join(REPO_ROOT, "skills", skill))
        ]
        self.assertEqual(
            missing, [], "missing skill directories: %s" % ", ".join(missing)
        )

    def test_all_skills_have_skill_md(self):
        missing = [
            skill
            for skill in EXPECTED_SKILLS
            if not os.path.isfile(os.path.join(REPO_ROOT, "skills", skill, "SKILL.md"))
        ]
        self.assertEqual(
            missing,
            [],
            "SKILL.md missing for: %s (expected while skill content is still "
            "being authored)" % ", ".join(missing),
        )


class ShowcaseTests(unittest.TestCase):
    def test_showcase_files_exist(self):
        missing = [
            name
            for name in SHOWCASE_FILES
            if not os.path.isfile(os.path.join(REPO_ROOT, "examples", "web-showcase", name))
        ]
        self.assertEqual(
            missing,
            [],
            "missing examples/web-showcase/ files: %s" % ", ".join(missing),
        )

    def test_showcase_index_references_assets(self):
        index_path = os.path.join(REPO_ROOT, "examples", "web-showcase", "index.html")
        if not os.path.isfile(index_path):
            self.fail(
                "examples/web-showcase/index.html is missing; asset references "
                "cannot be checked"
            )
        with open(index_path, "r", encoding="utf-8") as handle:
            content = handle.read()
        self.assertIn("styles.css", content, "index.html must reference styles.css")
        self.assertIn("script.js", content, "index.html must reference script.js")


class CiAndToolingTests(unittest.TestCase):
    def test_workflow_mentions_validators(self):
        workflow_path = os.path.join(REPO_ROOT, ".github", "workflows", "validate.yml")
        self.assertTrue(
            os.path.isfile(workflow_path), "missing .github/workflows/validate.yml"
        )
        with open(workflow_path, "r", encoding="utf-8") as handle:
            content = handle.read()
        self.assertIn(
            "validate_skills.py",
            content,
            "CI workflow must run scripts/validate_skills.py",
        )
        self.assertIn(
            "validate_repository.py",
            content,
            "CI workflow must run scripts/validate_repository.py",
        )

    def test_validator_scripts_exist(self):
        for name in ("validate_skills.py", "validate_repository.py"):
            self.assertTrue(
                os.path.isfile(os.path.join(REPO_ROOT, "scripts", name)),
                "missing scripts/%s" % name,
            )

    def test_unit_test_modules_exist(self):
        for name in ("test_skill_metadata.py", "test_repository_structure.py"):
            self.assertTrue(
                os.path.isfile(os.path.join(REPO_ROOT, "tests", name)),
                "missing tests/%s" % name,
            )


class HygieneTests(unittest.TestCase):
    def test_no_empty_files(self):
        empty = []
        for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
            dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
            for name in filenames:
                path = os.path.join(dirpath, name)
                try:
                    size = os.path.getsize(path)
                except OSError:
                    continue
                if size == 0:
                    empty.append(os.path.relpath(path, REPO_ROOT))
        self.assertEqual(
            empty,
            [],
            "empty (0-byte) files found: %s" % ", ".join(sorted(empty)),
        )


class CitationTests(unittest.TestCase):
    def test_citation_cff_contents(self):
        citation_path = os.path.join(REPO_ROOT, "CITATION.cff")
        self.assertTrue(os.path.isfile(citation_path), "missing CITATION.cff")
        with open(citation_path, "r", encoding="utf-8") as handle:
            content = handle.read()
        self.assertIn("title: Ochrelle", content, "CITATION.cff must set the title")
        self.assertIn("MIT", content, "CITATION.cff must declare the MIT license")


if __name__ == "__main__":
    unittest.main()

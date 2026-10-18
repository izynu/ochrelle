"""Unit tests for Ochrelle skill metadata and the validate_skills helpers.

These tests import the validator from ../scripts via sys.path manipulation so
the exact code that CI runs is exercised. Real repository skills are asserted
where complete; synthetic frontmatter and on-disk fixtures provide negative
coverage that does not depend on parallel workstreams.
"""

import os
import sys
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(REPO_ROOT, "scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

import validate_skills  # noqa: E402

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

FIXTURES_DIR = os.path.join(REPO_ROOT, "tests", "fixtures")
VALID_FIXTURE = os.path.join(FIXTURES_DIR, "valid-skill")
BROKEN_FIXTURE = os.path.join(FIXTURES_DIR, "broken-skill")


def _skill_md_path(skill):
    return os.path.join(REPO_ROOT, "skills", skill, "SKILL.md")


def _skill_dir(skill):
    return os.path.join(REPO_ROOT, "skills", skill)


def _read(path):
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


class SkillLayoutTests(unittest.TestCase):
    """Repository-level layout expectations for the eleven Ochrelle skills."""

    def test_all_eleven_skill_dirs_exist(self):
        missing = [
            skill
            for skill in EXPECTED_SKILLS
            if not os.path.isdir(_skill_dir(skill))
        ]
        self.assertEqual(
            missing,
            [],
            "missing skill directories under skills/: %s" % ", ".join(missing),
        )

    def test_each_skill_dir_contains_skill_md(self):
        missing = [skill for skill in EXPECTED_SKILLS if not os.path.isfile(_skill_md_path(skill))]
        self.assertEqual(
            missing,
            [],
            "SKILL.md missing for: %s (if skill content is still being authored, "
            "re-run once the content lands)" % ", ".join(missing),
        )


class SkillFrontmatterTests(unittest.TestCase):
    """Frontmatter rules asserted against the real skills in skills/."""

    def test_each_skill_md_has_valid_frontmatter(self):
        for skill in EXPECTED_SKILLS:
            with self.subTest(skill=skill):
                path = _skill_md_path(skill)
                if not os.path.isfile(path):
                    self.fail(
                        "%s/SKILL.md is missing; frontmatter cannot be validated "
                        "until the skill content is written" % skill
                    )
                frontmatter = validate_skills.parse_frontmatter(_read(path))
                if frontmatter is None:
                    self.fail(
                        "%s/SKILL.md has no parsable YAML frontmatter; it must "
                        "start with '---' on line 1 and close with '---'" % skill
                    )
                name_errors = validate_skills.validate_name(frontmatter.get("name"), skill)
                self.assertEqual(
                    name_errors,
                    [],
                    "%s: invalid name: %s" % (skill, "; ".join(name_errors)),
                )
                description_errors = validate_skills.validate_description(
                    frontmatter.get("description")
                )
                self.assertEqual(
                    description_errors,
                    [],
                    "%s: invalid description: %s"
                    % (skill, "; ".join(description_errors)),
                )

    def test_descriptions_within_1024(self):
        for skill in EXPECTED_SKILLS:
            with self.subTest(skill=skill):
                path = _skill_md_path(skill)
                if not os.path.isfile(path):
                    self.fail("%s/SKILL.md is missing" % skill)
                frontmatter = validate_skills.parse_frontmatter(_read(path))
                if frontmatter is None:
                    self.fail("%s/SKILL.md frontmatter is unparsable" % skill)
                description = frontmatter.get("description")
                if not isinstance(description, str):
                    self.fail(
                        "%s: description must be a string, got %s"
                        % (skill, type(description).__name__)
                    )
                self.assertGreaterEqual(
                    len(description), 1, "%s: description is empty" % skill
                )
                self.assertLessEqual(
                    len(description),
                    1024,
                    "%s: description is %d characters (max 1024); move details "
                    "into references/" % (skill, len(description)),
                )

    def test_metadata_version_is_string(self):
        for skill in EXPECTED_SKILLS:
            path = _skill_md_path(skill)
            if not os.path.isfile(path):
                continue
            frontmatter = validate_skills.parse_frontmatter(_read(path))
            if not frontmatter or not isinstance(frontmatter.get("metadata"), dict):
                continue
            version = frontmatter["metadata"].get("version")
            if version is None:
                continue
            with self.subTest(skill=skill):
                self.assertIsInstance(
                    version,
                    str,
                    "%s: metadata.version must be a string; quote it in SKILL.md "
                    '(e.g. version: "1.0.0") so YAML does not coerce it' % skill,
                )

    def test_referenced_paths_resolve(self):
        for skill in EXPECTED_SKILLS:
            with self.subTest(skill=skill):
                if not os.path.isfile(_skill_md_path(skill)):
                    self.fail(
                        "%s/SKILL.md is missing; referenced paths cannot be "
                        "checked until the skill content is written" % skill
                    )
                unresolved = validate_skills.find_unresolved_references(_skill_dir(skill))
                self.assertEqual(
                    unresolved,
                    [],
                    "%s: unresolved references:\n  - %s"
                    % (skill, "\n  - ".join(unresolved)),
                )


class ValidatorUnitTests(unittest.TestCase):
    """Negative tests that exercise the validator's reusable functions."""

    def test_parse_frontmatter_requires_fence_pair(self):
        self.assertIsNone(
            validate_skills.parse_frontmatter("name: x\ndescription: y\n"),
            "text without '---' fences must not parse as frontmatter",
        )
        self.assertIsNone(
            validate_skills.parse_frontmatter("---\nname: x\n"),
            "unclosed frontmatter must not parse",
        )
        parsed = validate_skills.parse_frontmatter("---\nname: x\n---\n# body")
        self.assertIsNotNone(parsed, "a well-formed fenced block must parse")
        self.assertEqual(parsed.get("name"), "x")

    def test_parse_frontmatter_handles_metadata_block(self):
        text = "---\nname: x\nmetadata:\n  version: 1.0.0\n  category: test\n---\nbody"
        frontmatter = validate_skills.parse_frontmatter(text)
        self.assertEqual(
            frontmatter.get("metadata"),
            {"version": "1.0.0", "category": "test"},
            "2-space indented metadata entries must parse into a dict of strings",
        )

    def test_parse_frontmatter_empty_scalar_is_none(self):
        parsed = validate_skills.parse_frontmatter("---\ndescription:\n---\nbody")
        self.assertIsNone(
            parsed.get("description"),
            "a key with no value must parse as None (PyYAML semantics), "
            "which validate_description must then reject",
        )

    def test_bad_name_regex_rejected(self):
        for bad_name in (
            "Bad_Name",
            "Ochrelle-Minimalism",
            "leading-",
            "trailing-",
            "double--dash",
            "has space",
            "a/b",
            "",
        ):
            errors = validate_skills.validate_name(bad_name, "some-dir")
            self.assertTrue(
                errors, "expected pattern rejection for name %r" % bad_name
            )

    def test_name_mismatch_rejected(self):
        errors = validate_skills.validate_name("ochrelle-minimalism", "ochrelle-brutalism")
        self.assertTrue(
            any("does not match" in error for error in errors),
            "expected a name/directory mismatch error, got: %s" % errors,
        )

    def test_missing_name_rejected(self):
        self.assertTrue(validate_skills.validate_name(None, "some-dir"))
        self.assertTrue(validate_skills.validate_name("", "some-dir"))

    def test_name_length_cap_enforced(self):
        long_name = "a" * 65
        errors = validate_skills.validate_name(long_name, long_name)
        self.assertTrue(
            any("64" in error for error in errors),
            "expected a >64-character name to be rejected, got: %s" % errors,
        )
        self.assertEqual(validate_skills.validate_name("a" * 64, "a" * 64), [])

    def test_missing_description_rejected(self):
        for bad_description in (None, "", "   "):
            errors = validate_skills.validate_description(bad_description)
            self.assertTrue(
                errors, "expected rejection for description %r" % bad_description
            )

    def test_overlong_description_rejected(self):
        errors = validate_skills.validate_description("x" * 1025)
        self.assertTrue(
            any("1024" in error for error in errors),
            "expected a >1024-character description to be rejected, got: %s" % errors,
        )

    def test_valid_name_and_description_accepted(self):
        self.assertEqual(
            validate_skills.validate_name("ochrelle-minimalism", "ochrelle-minimalism"),
            [],
        )
        self.assertEqual(
            validate_skills.validate_description(
                "Warm, tactile soft-UI guidance for device dashboards."
            ),
            [],
        )


class FixtureTests(unittest.TestCase):
    """Integration tests against the on-disk validator fixtures."""

    def test_valid_fixture_is_blessed(self):
        self.assertTrue(os.path.isdir(VALID_FIXTURE), "missing fixture %s" % VALID_FIXTURE)
        errors = validate_skills.validate_skill(VALID_FIXTURE)
        self.assertEqual(
            errors, [], "valid-skill fixture must pass validation, got: %s" % errors
        )
        self.assertEqual(
            validate_skills.find_unresolved_references(VALID_FIXTURE),
            [],
            "valid-skill fixture must have no unresolved references",
        )
        self.assertEqual(
            validate_skills.find_placeholders(VALID_FIXTURE),
            [],
            "valid-skill fixture must contain no placeholder markers",
        )

    def test_broken_fixture_is_flagged(self):
        self.assertTrue(os.path.isdir(BROKEN_FIXTURE), "missing fixture %s" % BROKEN_FIXTURE)
        errors = validate_skills.validate_skill(BROKEN_FIXTURE)
        self.assertTrue(errors, "broken-skill fixture must not pass validation")
        joined = "\n".join(errors)
        self.assertIn(
            "does not match",
            joined,
            "expected a name/directory mismatch error, got: %s" % joined,
        )
        placeholders = validate_skills.find_placeholders(BROKEN_FIXTURE)
        self.assertTrue(
            placeholders, "expected the TODO marker in the broken fixture to be flagged"
        )
        unresolved = validate_skills.find_unresolved_references(BROKEN_FIXTURE)
        self.assertTrue(
            any("missing-guide.md" in message for message in unresolved),
            "expected a broken reference to references/missing-guide.md, got: %s"
            % unresolved,
        )


if __name__ == "__main__":
    unittest.main()

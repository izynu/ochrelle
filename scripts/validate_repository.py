#!/usr/bin/env python3
"""validate_repository.py - structural sanity checks for the Ochrelle repository.

Checks, from the repository root (auto-detected as the parent of scripts/):

  * Required root documents exist: README.md, LICENSE, CONTRIBUTING.md,
    CODE_OF_CONDUCT.md, SECURITY.md, SUPPORT.md, CHANGELOG.md, CITATION.cff,
    AGENTS.md.
  * docs/ contains the seven core pages (architecture, installation,
    style-comparison, research-methodology, source-catalog, examples,
    troubleshooting).
  * examples/web-showcase/ contains index.html, styles.css and script.js, and
    index.html references both asset files.
  * All 28 expected skill directories exist and each has a SKILL.md.
  * .github/workflows/validate.yml exists and mentions validate_skills.py.
  * scripts/ has both validators and tests/ has both unit-test modules.
  * Every relative link in README.md that points at docs/*.md or
    skills/*/SKILL.md resolves to an existing file.
  * No empty (0-byte) files anywhere in the repository (the .git directory is
    skipped).

Usage:
    python3 scripts/validate_repository.py [--root PATH] [--json]

Exit codes: 0 = all checks pass, 1 = one or more checks failed, 2 = the
repository root itself is invalid.
"""

import argparse
import json
import os
import re
import sys

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
REQUIRED_SCRIPT_FILES = ["validate_skills.py", "validate_repository.py"]
REQUIRED_TEST_FILES = ["test_skill_metadata.py", "test_repository_structure.py"]

WORKFLOW_RELATIVE = os.path.join(".github", "workflows", "validate.yml")

MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]*\]\(\s*([^)\s]+)\s*\)")
INTERNAL_LINK_PATTERN = re.compile(r"^(?:docs/[^/]+\.md|skills/[a-z0-9-]+/SKILL\.md)$")
IGNORED_LINK_PREFIXES = ("http://", "https://", "mailto:", "ftp://", "#")
SKIP_DIRS = {".git", "__pycache__", "node_modules"}
MAX_LISTED_DETAILS = 20


def _read_text(path):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as handle:
            return handle.read()
    except OSError:
        return None


def default_repo_root():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(script_dir, os.pardir))


# --- Checks: each returns (ok, details) where details are actionable messages --


def check_root_docs(root):
    missing = [name for name in REQUIRED_ROOT_DOCS if not os.path.isfile(os.path.join(root, name))]
    details = ["missing root document: %s" % name for name in missing]
    return not missing, details


def check_docs_dir(root):
    missing = [
        name
        for name in REQUIRED_DOCS_FILES
        if not os.path.isfile(os.path.join(root, "docs", name))
    ]
    details = ["missing docs/ page: docs/%s" % name for name in missing]
    return not missing, details


def check_showcase_files(root):
    missing = [
        name
        for name in SHOWCASE_FILES
        if not os.path.isfile(os.path.join(root, "examples", "web-showcase", name))
    ]
    details = [
        "missing showcase file: examples/web-showcase/%s" % name for name in missing
    ]
    return not missing, details


def check_showcase_references(root):
    index_path = os.path.join(root, "examples", "web-showcase", "index.html")
    if not os.path.isfile(index_path):
        return False, [
            "examples/web-showcase/index.html is missing; cannot check asset references"
        ]
    content = _read_text(index_path) or ""
    unreferenced = [name for name in ("styles.css", "script.js") if name not in content]
    details = [
        "examples/web-showcase/index.html does not reference '%s'; add the "
        "corresponding <link>/<script> tag" % name
        for name in unreferenced
    ]
    return not unreferenced, details


def check_skill_dirs(root):
    details = []
    for skill in EXPECTED_SKILLS:
        skill_path = os.path.join(root, "skills", skill)
        if not os.path.isdir(skill_path):
            details.append("missing skill directory: skills/%s" % skill)
        elif not os.path.isfile(os.path.join(skill_path, "SKILL.md")):
            details.append("skills/%s exists but has no SKILL.md" % skill)
    return not details, details


def check_workflow(root):
    workflow_path = os.path.join(root, WORKFLOW_RELATIVE)
    if not os.path.isfile(workflow_path):
        return False, ["missing CI workflow: .github/workflows/validate.yml"]
    content = _read_text(workflow_path) or ""
    if "validate_skills.py" not in content:
        return False, [
            ".github/workflows/validate.yml does not mention validate_skills.py; "
            "add a step that runs: python scripts/validate_skills.py"
        ]
    return True, []


def check_scripts_and_tests(root):
    details = []
    for name in REQUIRED_SCRIPT_FILES:
        if not os.path.isfile(os.path.join(root, "scripts", name)):
            details.append("missing scripts/%s" % name)
    for name in REQUIRED_TEST_FILES:
        if not os.path.isfile(os.path.join(root, "tests", name)):
            details.append("missing tests/%s" % name)
    return not details, details


def check_readme_internal_links(root):
    readme_path = os.path.join(root, "README.md")
    if not os.path.isfile(readme_path):
        return False, ["README.md is missing; cannot check internal links"]
    content = _read_text(readme_path) or ""
    broken = set()
    for match in MARKDOWN_LINK_PATTERN.finditer(content):
        target = match.group(1).split("#", 1)[0].strip()
        if not target or target.startswith(IGNORED_LINK_PREFIXES) or target.startswith("/"):
            continue
        if not INTERNAL_LINK_PATTERN.match(target):
            continue
        if not os.path.isfile(os.path.join(root, target.replace("/", os.sep))):
            broken.add(target)
    details = [
        "README.md links to '%s' but that file does not exist (yet)" % target
        for target in sorted(broken)
    ]
    return not details, details


def check_no_empty_files(root):
    empty = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for name in filenames:
            file_path = os.path.join(dirpath, name)
            try:
                if os.path.getsize(file_path) == 0:
                    empty.append(os.path.relpath(file_path, root))
            except OSError:
                continue
    details = ["empty (0-byte) file: %s" % rel for rel in sorted(empty)]
    if len(details) > MAX_LISTED_DETAILS:
        details = details[:MAX_LISTED_DETAILS] + [
            "... and %d more empty files" % (len(empty) - MAX_LISTED_DETAILS)
        ]
    return not details, details


CHECKS = [
    ("required root documents present", check_root_docs),
    ("docs/ core pages present", check_docs_dir),
    ("web showcase files present", check_showcase_files),
    ("web showcase index references assets", check_showcase_references),
    ("28 expected skill directories with SKILL.md", check_skill_dirs),
    ("CI workflow runs the skill validator", check_workflow),
    ("validators and unit tests present", check_scripts_and_tests),
    ("README internal links resolve", check_readme_internal_links),
    ("no empty (0-byte) files in repository", check_no_empty_files),
]


# --- Runner -------------------------------------------------------------------


def run_checks(root):
    results = []
    for name, check in CHECKS:
        ok, details = check(root)
        results.append(
            {"check": name, "status": "pass" if ok else "fail", "details": details}
        )
    return results


def print_report(root, results):
    print("Validating Ochrelle repository at: %s" % root)
    print("")
    for result in results:
        marker = "PASS" if result["status"] == "pass" else "FAIL"
        print("[%s] %s" % (marker, result["check"]))
        for detail in result["details"]:
            print("       - %s" % detail)
    passed = sum(1 for r in results if r["status"] == "pass")
    failed = len(results) - passed
    print("")
    print("Summary: %d/%d check(s) passed, %d failed." % (passed, len(results), failed))
    if failed:
        print("Fix the failures above, then re-run: python3 scripts/validate_repository.py")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Validate the Ochrelle repository structure (stdlib only)."
    )
    parser.add_argument(
        "--root",
        default=None,
        help="repository root (default: the parent directory of scripts/)",
    )
    parser.add_argument(
        "--json", action="store_true", help="emit machine-readable JSON output"
    )
    args = parser.parse_args(argv)

    root = os.path.abspath(args.root) if args.root else default_repo_root()
    if not os.path.isdir(root):
        if args.json:
            print(
                json.dumps(
                    {"root": root, "ok": False, "error": "repository root not found"},
                    indent=2,
                )
            )
        else:
            print("[FAIL] repository root does not exist: %s" % root)
        return 2

    results = run_checks(root)
    all_ok = all(r["status"] == "pass" for r in results)
    passed = sum(1 for r in results if r["status"] == "pass")

    if args.json:
        payload = {
            "root": root,
            "ok": all_ok,
            "summary": {
                "total": len(results),
                "passed": passed,
                "failed": len(results) - passed,
            },
            "checks": results,
        }
        print(json.dumps(payload, indent=2))
    else:
        print_report(root, results)

    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())

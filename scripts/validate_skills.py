#!/usr/bin/env python3
"""validate_skills.py - lint Agent Skill directories for the Ochrelle repository.

Implements the Agent Skills rules that matter for this repo:

  * Each skill directory under skills/ must contain a SKILL.md whose YAML
    frontmatter sits between the first two '---' lines.
  * ``name``: 1-64 chars, matches ``^[a-z0-9]+(-[a-z0-9]+)*$`` and equals the
    parent directory name.
  * ``description``: 1-1024 chars, non-empty.
  * Optional fields: ``license`` (string), ``compatibility`` (1-500 chars),
    ``metadata`` (map of string -> string), ``allowed-tools`` (space-separated
    string).
  * Relative ``references/...``, ``scripts/...`` and ``assets/...`` paths
    mentioned in SKILL.md, plus every local markdown link in SKILL.md and in
    the skill's other markdown files, must resolve to existing files.
    (http://, https://, mailto: and #fragment targets are ignored.)
  * No placeholder content: TODO, FIXME, lorem ipsum, [placeholder] and
    <insert are flagged wherever they appear in the skill's text files.
  * Every specialist skill must ship ``references/style-guide.md``; the
    master skill (``ochrelle-design-master``) is exempt.

Only the Python standard library is required. If PyYAML happens to be
installed it is preferred for frontmatter parsing; otherwise a hand-written
parser for the small YAML subset used by SKILL.md files takes over.

Usage:
    python3 scripts/validate_skills.py [--skills-dir PATH] [--json]

Exit codes: 0 = every skill passed, 1 = at least one failure (including a
missing skills directory).
"""

import argparse
import json
import os
import re
import sys

try:
    import yaml as _yaml  # type: ignore
    HAS_PYYAML = True
except ImportError:  # pragma: no cover - environment dependent
    HAS_PYYAML = False

# --- Agent Skills field rules -------------------------------------------------

NAME_MAX_LENGTH = 64
NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DESCRIPTION_MAX_LENGTH = 1024
COMPATIBILITY_MAX_LENGTH = 500

MASTER_SKILL_NAME = "ochrelle-design-master"
SPECIALIST_REQUIRED_REFERENCE = os.path.join("references", "style-guide.md")

# --- Scanning configuration ---------------------------------------------------

TEXT_EXTENSIONS = {".md", ".py", ".js", ".css", ".html", ".json", ".yaml", ".yml", ".txt"}
SKIP_DIRS = {".git", "__pycache__", "node_modules"}

IGNORED_LINK_PREFIXES = ("http://", "https://", "mailto:", "ftp://", "#")
# Path mentions such as references/foo.md, scripts/x.py, assets/img.png.
# The lookbehind avoids matching segments of longer paths or URLs.
PATH_MENTION_PATTERN = re.compile(
    r"(?<![\w./-])((?:references|scripts|assets)/[A-Za-z0-9_\-./]+)"
)
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]*\]\(\s*([^)\s]+)\s*\)")
# Paths using the references/, scripts/ or assets/ convention may be written
# skill-root-relative even from inside references/*.md, so the resolver also
# tries the skill root for them.
SKILL_ROOT_PATH_PATTERN = re.compile(r"^(?:references|scripts|assets)/")

PLACEHOLDER_PATTERNS = (
    ("TODO", re.compile(r"TODO", re.IGNORECASE)),
    ("FIXME", re.compile(r"FIXME", re.IGNORECASE)),
    ("lorem ipsum", re.compile(r"lorem\s+ipsum", re.IGNORECASE)),
    ("[placeholder]", re.compile(r"\[\s*placeholder\s*\]", re.IGNORECASE)),
    ("<insert", re.compile(r"<insert", re.IGNORECASE)),
)


# --- Helpers ------------------------------------------------------------------


def _read_text(path):
    """Read a file as UTF-8 text, returning None when it cannot be read."""
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as handle:
            return handle.read()
    except OSError:
        return None


def _strip_quotes(value):
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("\"", "'"):
        return value[1:-1]
    return value


def _coerce_scalar(raw):
    return _strip_quotes(raw.strip())


def _parse_yaml_subset(frontmatter_text):
    """Parse the YAML subset used by SKILL.md files.

    Supports ``key: value`` pairs and one level of nested mapping via a
    2-space indented ``key: value`` block (used for ``metadata:``). Scalar
    values are returned as strings; quoted values are unquoted; a key with
    no value (and no nested block) yields None, matching PyYAML.
    """
    data = {}
    pending_key = None
    block_has_children = False

    def flush_pending():
        nonlocal pending_key, block_has_children
        if pending_key is not None and not block_has_children:
            # "key:" with no nested block is an empty scalar; PyYAML yields
            # None for it, so the fallback matches that semantics.
            data[pending_key] = None
        pending_key = None
        block_has_children = False

    for raw_line in frontmatter_text.splitlines():
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if raw_line[:1] in (" ", "\t"):
            if pending_key is None:
                continue  # stray indented line; ignore
            nested = re.match(r"^\s+([A-Za-z0-9_-]+)\s*:\s*(.*)$", raw_line.rstrip())
            if not nested:
                continue
            if not isinstance(data.get(pending_key), dict):
                data[pending_key] = {}
            data[pending_key][nested.group(1)] = _coerce_scalar(nested.group(2))
            block_has_children = True
        else:
            flush_pending()
            top = re.match(r"^([A-Za-z0-9_-]+)\s*:\s*(.*)$", stripped)
            if not top:
                continue
            key, value = top.group(1), top.group(2).strip()
            if value == "":
                data[key] = {}
                pending_key = key
                block_has_children = False
            else:
                data[key] = _coerce_scalar(value)
    flush_pending()
    return data


# --- Reusable validation functions (imported by the unit tests) ---------------


def parse_frontmatter(text):
    """Return the SKILL.md frontmatter as a dict, or None if unparsable.

    The frontmatter must be delimited by '---' on the first line and a
    closing '---' line. Uses PyYAML when available, otherwise the built-in
    subset parser.
    """
    if text is None:
        return None
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    closing = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            closing = index
            break
    if closing is None:
        return None
    frontmatter_text = "\n".join(lines[1:closing])

    if HAS_PYYAML:
        try:
            loaded = _yaml.safe_load(frontmatter_text)
        except _yaml.YAMLError:
            return None
        if loaded is None:
            return {}
        if isinstance(loaded, dict):
            return loaded
        return None
    return _parse_yaml_subset(frontmatter_text)


def validate_name(name, dirname):
    """Validate a skill 'name' against the Agent Skills rules.

    Returns a list of human-readable errors (empty list means valid).
    """
    errors = []
    if name is None or name == "":
        return [
            "missing 'name' in frontmatter; it must match the skill directory "
            "name '%s' (1-64 chars, lowercase letters, digits and hyphens)" % dirname
        ]
    if not isinstance(name, str):
        return ["'name' must be a string, got %s" % type(name).__name__]
    if len(name) > NAME_MAX_LENGTH:
        errors.append(
            "'name' is %d characters long; the maximum is %d" % (len(name), NAME_MAX_LENGTH)
        )
    if not NAME_PATTERN.match(name):
        errors.append(
            "'name' value %r does not match the required pattern %s "
            "(lowercase letters, digits and single hyphens; no leading, "
            "trailing or double hyphens)" % (name, NAME_PATTERN.pattern)
        )
    if name != dirname:
        errors.append(
            "'name' value %r does not match the directory name %r; rename the "
            "directory or the frontmatter field so they are identical"
            % (name, dirname)
        )
    return errors


def validate_description(description):
    """Validate a skill 'description' (1-1024 chars, non-empty)."""
    errors = []
    if description is None:
        return ["missing 'description' in frontmatter; write 1-1024 characters "
                "explaining what the skill does and when an agent should use it"]
    if not isinstance(description, str):
        return ["'description' must be a string, got %s" % type(description).__name__]
    if not description.strip():
        return ["'description' is empty; write 1-1024 characters explaining what "
                "the skill does and when an agent should use it"]
    if len(description) > DESCRIPTION_MAX_LENGTH:
        errors.append(
            "'description' is %d characters long; the maximum is %d; keep the "
            "trigger context and trim details into references/ instead"
            % (len(description), DESCRIPTION_MAX_LENGTH)
        )
    return errors


def validate_optional_fields(frontmatter):
    """Validate the optional Agent Skills fields, if present."""
    errors = []
    if "license" in frontmatter and not isinstance(frontmatter.get("license"), str):
        errors.append("'license' must be a string (e.g. MIT)")
    compatibility = frontmatter.get("compatibility")
    if compatibility is not None:
        if not isinstance(compatibility, str):
            errors.append("'compatibility' must be a string")
        elif len(compatibility) > COMPATIBILITY_MAX_LENGTH:
            errors.append(
                "'compatibility' is %d characters long; the maximum is %d"
                % (len(compatibility), COMPATIBILITY_MAX_LENGTH)
            )
    allowed_tools = frontmatter.get("allowed-tools")
    if allowed_tools is not None and not isinstance(allowed_tools, str):
        errors.append("'allowed-tools' must be a single space-separated string of tool names")
    metadata = frontmatter.get("metadata")
    if metadata is not None:
        if not isinstance(metadata, dict):
            errors.append("'metadata' must be a map of string keys to string values")
        else:
            for key, value in metadata.items():
                if not isinstance(value, str):
                    errors.append(
                        "metadata['%s'] must be a string but looks like %s; quote the "
                        "value in SKILL.md (e.g. version: \"1.0\") to keep it a string"
                        % (key, type(value).__name__)
                    )
    return errors


# --- Content scans ------------------------------------------------------------


def _iter_text_files(base_dir):
    for root, dirs, files in os.walk(base_dir):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS and not d.startswith("."))
        for name in sorted(files):
            if os.path.splitext(name)[1].lower() in TEXT_EXTENSIONS:
                yield os.path.join(root, name)


def find_placeholders(skill_dir):
    """Return messages for every placeholder marker found in skill text files."""
    findings = []
    for file_path in _iter_text_files(skill_dir):
        content = _read_text(file_path)
        if content is None:
            continue
        rel_path = os.path.relpath(file_path, skill_dir)
        for label, pattern in PLACEHOLDER_PATTERNS:
            match = pattern.search(content)
            if match:
                line = content.count("\n", 0, match.start()) + 1
                findings.append(
                    "%s:%d contains placeholder marker %r; replace it with real "
                    "content before publishing" % (rel_path, line, label)
                )
    return findings


def _trim_mention(mention):
    """Drop trailing punctuation that the regex may have swallowed."""
    return mention.rstrip(".,;:!?\"')")


def _check_reference_target(target, base_dir, skill_dir):
    """Return an error string if a link target does not resolve, else None.

    A target resolves if it exists relative to the containing file's directory
    (standard markdown semantics) or, for the references/scripts/assets
    convention, relative to the skill root.
    """
    path = target.split("#", 1)[0].strip()
    if not path or path.startswith(IGNORED_LINK_PREFIXES) or path.startswith("/"):
        return None
    candidates = [os.path.normpath(os.path.join(base_dir, path))]
    if SKILL_ROOT_PATH_PATTERN.match(path):
        candidates.append(os.path.normpath(os.path.join(skill_dir, path)))
    for candidate in candidates:
        if os.path.exists(candidate):
            return None
    resolved = candidates[0]
    if resolved.startswith(skill_dir + os.sep):
        display = os.path.relpath(resolved, skill_dir)
    else:
        display = resolved
    return (
        "broken reference '%s' - the expected file '%s' does not exist (checked "
        "relative to both the containing file and the skill root); fix the link "
        "or ship the file" % (target, display)
    )


def find_unresolved_references(skill_dir):
    """Return messages for every local reference that does not resolve.

    Scans SKILL.md for both markdown links and references/scripts/assets path
    mentions, and every other markdown file in the skill for markdown links.
    """
    skill_dir = os.path.abspath(skill_dir)
    unresolved = []
    markdown_files = []
    skill_md = os.path.join(skill_dir, "SKILL.md")
    if os.path.isfile(skill_md):
        markdown_files.append(skill_md)
    for root, dirs, files in os.walk(skill_dir):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS and not d.startswith("."))
        for name in sorted(files):
            if name == "SKILL.md":
                continue
            if os.path.splitext(name)[1].lower() == ".md":
                markdown_files.append(os.path.join(root, name))

    for md_path in markdown_files:
        content = _read_text(md_path)
        if content is None:
            continue
        rel_source = os.path.relpath(md_path, skill_dir)
        base_dir = os.path.dirname(md_path)
        targets = set()
        for link_match in MARKDOWN_LINK_PATTERN.finditer(content):
            targets.add(link_match.group(1))
        if os.path.basename(md_path) == "SKILL.md":
            for mention in PATH_MENTION_PATTERN.finditer(content):
                targets.add(_trim_mention(mention.group(1)))
        for target in sorted(targets):
            problem = _check_reference_target(target, base_dir, skill_dir)
            if problem:
                unresolved.append("%s: %s" % (rel_source, problem))
    return unresolved


# --- Per-skill validation -----------------------------------------------------


def validate_skill(skill_dir):
    """Validate one skill directory; return a list of errors (empty = pass)."""
    skill_dir = os.path.abspath(skill_dir)
    if not os.path.isdir(skill_dir):
        return ["skill directory not found: %s" % skill_dir]
    dir_name = os.path.basename(skill_dir)
    skill_md = os.path.join(skill_dir, "SKILL.md")
    if not os.path.isfile(skill_md):
        return [
            "missing SKILL.md; every Agent Skill needs a SKILL.md at the root "
            "of %s (frontmatter between the first two '---' lines, then the "
            "markdown body)" % dir_name
        ]
    text = _read_text(skill_md)
    if text is None:
        return ["SKILL.md could not be read (check file permissions)"]

    errors = []
    frontmatter = parse_frontmatter(text)
    if frontmatter is None:
        errors.append(
            "SKILL.md has no parsable YAML frontmatter; the file must start with "
            "'---' on line 1, contain 'key: value' lines, and close with '---'"
        )
    else:
        errors.extend(validate_name(frontmatter.get("name"), dir_name))
        errors.extend(validate_description(frontmatter.get("description")))
        errors.extend(validate_optional_fields(frontmatter))
    errors.extend(find_unresolved_references(skill_dir))
    errors.extend(find_placeholders(skill_dir))

    if dir_name != MASTER_SKILL_NAME:
        style_guide = os.path.join(skill_dir, SPECIALIST_REQUIRED_REFERENCE)
        if not os.path.isfile(style_guide):
            errors.append(
                "specialist skills must ship references/style-guide.md (only %s "
                "is exempt); create it with contrast, spacing, component and "
                "anti-pattern guidance" % MASTER_SKILL_NAME
            )
    return errors


# --- Runner -------------------------------------------------------------------


def discover_skill_dirs(skills_dir):
    """Return sorted skill directory names, or None if skills_dir is missing."""
    if not os.path.isdir(skills_dir):
        return None
    return sorted(
        name
        for name in os.listdir(skills_dir)
        if not name.startswith(".") and os.path.isdir(os.path.join(skills_dir, name))
    )


def default_skills_dir():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    candidate = os.path.normpath(os.path.join(script_dir, os.pardir, "skills"))
    if os.path.isdir(candidate):
        return candidate
    return os.path.join(os.getcwd(), "skills")


def validate_all(skills_dir):
    """Validate every skill directory; returns (results, ok, setup_errors)."""
    results = []
    names = discover_skill_dirs(skills_dir)
    if names is None:
        return results, False, ["skills directory not found: %s" % skills_dir]
    setup_errors = []
    for name in names:
        errors = validate_skill(os.path.join(skills_dir, name))
        results.append(
            {"skill": name, "status": "pass" if not errors else "fail", "errors": errors}
        )
    if not results:
        setup_errors.append("no skill directories found under %s" % skills_dir)
    ok = not setup_errors and all(r["status"] == "pass" for r in results)
    return results, ok, setup_errors


def print_report(results, setup_errors, skills_dir):
    print("Validating Agent Skills in: %s" % skills_dir)
    print("")
    for message in setup_errors:
        print("[FAIL] setup: %s" % message)
    for result in results:
        marker = "PASS" if result["status"] == "pass" else "FAIL"
        print("[%s] %s" % (marker, result["skill"]))
        for error in result["errors"]:
            print("       - %s" % error)
    passed = sum(1 for r in results if r["status"] == "pass")
    failed = len(results) - passed
    print("")
    print("Summary: %d/%d skill(s) passed, %d failed." % (passed, len(results), failed))
    if failed or setup_errors:
        print("Fix the errors above, then re-run: python3 scripts/validate_skills.py")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Validate Ochrelle Agent Skill directories (stdlib only)."
    )
    parser.add_argument(
        "--skills-dir",
        default=None,
        help="path to the skills/ directory (default: auto-detect ../skills "
        "relative to this script, else ./skills)",
    )
    parser.add_argument(
        "--json", action="store_true", help="emit machine-readable JSON output"
    )
    args = parser.parse_args(argv)

    if args.skills_dir:
        skills_dir = os.path.abspath(args.skills_dir)
    else:
        skills_dir = default_skills_dir()

    results, ok, setup_errors = validate_all(skills_dir)

    if args.json:
        passed = sum(1 for r in results if r["status"] == "pass")
        payload = {
            "skills_dir": skills_dir,
            "ok": ok,
            "summary": {
                "total": len(results),
                "passed": passed,
                "failed": len(results) - passed,
            },
            "skills": results,
        }
        if setup_errors:
            payload["errors"] = setup_errors
        print(json.dumps(payload, indent=2))
    else:
        print_report(results, setup_errors, skills_dir)

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env bash
# install.sh - copy Ochrelle skills into an Agent Skills directory.
#
# Ochrelle skills follow the open Agent Skills specification: each skill is a
# folder with a SKILL.md (YAML frontmatter plus markdown body) and reference
# files. Any AI tool that can read project files can use them. Tools with
# native skills support just need the folders copied into their skills
# directory; other tools can point at the files from their instructions file
# (CLAUDE.md, AGENTS.md, .cursorrules, GEMINI.md, and similar).
#
# Usage:
#   ./install.sh --claude              copy all skills to ~/.claude/skills
#   ./install.sh --claude --only NAME  copy one skill (e.g. ochrelle-minimalism)
#   ./install.sh --project [DIR]       copy all skills to ./skills (or DIR) inside
#                                      the current project, for agents that read
#                                      the repository directly
#   ./install.sh DEST                  copy all skills to an explicit directory
#   ./install.sh --list                list available skills
#   ./install.sh --dry-run --claude    show what would be copied
#
# Only the destination is written; the repository is never modified.

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_SRC="$REPO_DIR/skills"
DRY_RUN=0
TARGET=""
ONLY=""

list_skills() {
  for dir in "$SKILLS_SRC"/*/; do
    [ -f "$dir/SKILL.md" ] && basename "$dir"
  done
}

copy_skills() {
  local dest="$1"
  mkdir -p "$dest"
  local copied=0
  for dir in "$SKILLS_SRC"/*/; do
    local name
    name="$(basename "$dir")"
    [ -f "$dir/SKILL.md" ] || continue
    if [ -n "$ONLY" ] && [ "$name" != "$ONLY" ]; then continue; fi
    if [ "$DRY_RUN" -eq 1 ]; then
      echo "would copy $name -> $dest/$name"
    else
      rm -rf "$dest/$name"
      cp -R "$dir" "$dest/$name"
      echo "copied  $name -> $dest/$name"
    fi
    copied=$((copied + 1))
  done
  if [ "$copied" -eq 0 ]; then
    echo "error: no skill matched --only \"$ONLY\"" >&2
    exit 1
  fi
  if [ "$DRY_RUN" -eq 0 ]; then
    echo ""
    echo "Done. $copied skill(s) installed in $dest"
    echo "Next step: tell your agent to read the SKILL.md of the skill it needs,"
    echo "or add a line to your agent instructions file pointing at that path."
  fi
}

case "${1:-}" in
  --list)
    list_skills
    exit 0
    ;;
  --claude)
    TARGET="${HOME}/.claude/skills"
    ;;
  --project)
    TARGET="${2:-$(pwd)/skills}"
    ;;
  --dry-run)
    DRY_RUN=1
    shift
    case "${1:-}" in
      --claude) TARGET="${HOME}/.claude/skills" ;;
      --project) TARGET="${2:-$(pwd)/skills}" ;;
      "") echo "error: --dry-run needs a target (--claude, --project, or DEST)" >&2; exit 1 ;;
      *) TARGET="$1" ;;
    esac
    ;;
  "")
    sed -n '2,30p' "${BASH_SOURCE[0]}"
    exit 0
    ;;
  -*)
    echo "error: unknown option $1" >&2
    exit 1
    ;;
  *)
    TARGET="$1"
    ;;
esac

# optional --only flag handling
if [ "${2:-}" = "--only" ] || [ "${3:-}" = "--only" ] || [ "${4:-}" = "--only" ]; then
  :
fi
for arg in "$@"; do
  if [ "${arg:-}" = "--only" ]; then ONLY_PENDING=1; continue; fi
  if [ "${ONLY_PENDING:-0}" -eq 1 ]; then ONLY="$arg"; ONLY_PENDING=0; fi
done

copy_skills "$TARGET"

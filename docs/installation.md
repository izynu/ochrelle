# Installing Ochrelle Skills

Ochrelle skills are plain directories of Markdown files following the open
Agent Skills format (agentskills.io). Installation means copying a skill
directory into a location your AI coding agent scans for skills.

> **Verified vs. general - read this first.** The only installation targets
> verified and publicly documented during Ochrelle development are Claude
> Code's personal and project skill directories. Other agents vary in whether
> and how they load Agent Skills–format directories; for those, the honest
> instruction is: **consult your tool's own documentation.** Anything a tool
> has publicly documented as supporting the open skills format can load these
> directories, but Ochrelle does not claim per-tool verification it has not
> performed.

---

## Compatibility matrix

Ochrelle skills are plain markdown folders, so they work with any agent that
can read project files. Support falls into three tiers: tools with native
Agent Skills support, tools that reference project files from their
instructions, and a manual fallback that works everywhere. Tool capabilities
change quickly, so treat this matrix as current as of the 2.0.0 release and
check your tool's current docs before relying on a path.

| Agent | Support | Where the skills go | How to point the agent at them |
| --- | --- | --- | --- |
| Claude Code | Native Agent Skills support, **[verified-documented]** | `~/.claude/skills/` (personal) or `.claude/skills/` (project) | `./scripts/install.sh --claude`, or copy the skill directories manually |
| Claude web/desktop | Upload or paste where the plan supports skills **[check your plan's current docs]** | Upload the skill folder, or paste the `SKILL.md` content into project knowledge | Copy from `skills/<name>/`; skills are just text |
| Cursor, Windsurf, Cline, Roo Code | Via project files **[unverified - consult your tool's docs]** | Copy skills into the project (e.g. `skills/`) | Reference `skills/<name>/SKILL.md` from the tool's rules or instructions file (`.cursorrules`, `.windsurfrules`, or the equivalent) |
| Codex CLI, Gemini CLI | Via project files **[unverified - consult your tool's docs]** | Keep the cloned repo or copy `skills/` into the project | Reference the skill folder from `AGENTS.md` / `GEMINI.md` |
| Aider | Via conventions file **[unverified - consult your tool's docs]** | Keep `skills/` in the repository | Add the skill path to `CONVENTIONS.md` |
| Any other agent | Manual fallback **[works anywhere the agent can read files]** | Anywhere reachable by the agent | Point the agent at `skills/<name>/SKILL.md`; the folder is plain markdown |

`scripts/install.sh` automates the copy step. It only writes to the
destination you name; the repository itself is never modified.

```bash
git clone <repository-url> && cd ochrelle
./scripts/install.sh --claude          # all 28 skills into ~/.claude/skills
./scripts/install.sh --claude --only ochrelle-minimalism
./scripts/install.sh ./skills          # into a project folder
```

Whatever the tier, the fallback in "How to check your tool yourself" below
always applies: an agent that can open `skills/<name>/SKILL.md` can use the
skill, with or without automatic discovery.

## 1. Manual install (any environment)

A skill is self-contained; copying it is the whole installation.

```bash
# From a clone of this repository
git clone https://github.com/<owner>/ochrelle.git
cd ochrelle

# Copy ONE skill (example: the bento grid skill)
cp -r skills/ochrelle-bento-grid /destination/skills/

# Or copy ALL skills
cp -r skills/. /destination/skills/
```

Notes:

- Copy the **skill directory itself** (e.g. `ochrelle-bento-grid/`, containing
  `SKILL.md`), not the repository's `skills/` wrapper, unless your target
  expects a nested layout.
- Do not rename the directory: the `name:` field in `SKILL.md` must match the
  directory name.
- Bundled references use relative paths, so the copy stays valid anywhere.

## 2. Project-level install (shared with the codebase)

Recommended when a team works in one repository. Claude Code documents a
project-level skill directory at `.claude/skills/` **[verified-documented]**:

```bash
mkdir -p .claude/skills
cp -r /path/to/ochrelle/skills/ochrelle-bento-grid .claude/skills/
git add .claude/skills/ochrelle-bento-grid
git commit -m "Add ochrelle-bento-grid skill"
```

Every teammate (and CI agents) get the skill with the repository. To install
the full library project-wide, copy all `skills/ochrelle-*` directories into
`.claude/skills/`.

## 3. Personal install (all your projects)

Claude Code documents a personal skill directory at `~/.claude/skills/`
**[verified-documented]**:

```bash
mkdir -p ~/.claude/skills
cp -r /path/to/ochrelle/skills/ochrelle-spatial-ui ~/.claude/skills/
```

## 4. Other agent environments

| Environment | Status | Skill directory | Notes |
| --- | --- | --- | --- |
| Claude Code - project | **[verified-documented]** | `.claude/skills/<skill-name>/` | Publicly documented; confirmed during Ochrelle development. |
| Claude Code - personal | **[verified-documented]** | `~/.claude/skills/<skill-name>/` | Publicly documented; confirmed during Ochrelle development. |
| Any tool that publicly documents support for the open Agent Skills format | **[unverified - consult your tool's docs]** | Per tool documentation | The format is open (agentskills.io); tools adopting it load these directories, but each tool's discovery path and features differ. |
| Cursor, Windsurf, Codex, and other specific tools | **[unverified - consult your tool's docs]** | - | Ochrelle has not verified these tools' skill-loading behavior. Do not trust third-party path lists (including any in older issues or forks) without checking current official documentation. |

How to check your tool yourself, honestly:

1. Search the tool's official documentation for "skills", "Agent Skills", or
   "SKILL.md".
2. If the tool documents a skills directory and Agent Skills–format support,
   use the copy commands above against that directory.
3. If it does not, the fallback that works everywhere: **put the SKILL.md
   content in front of your agent manually** - open `SKILL.md` and paste or
   reference it in your prompt/project rules. This loses automatic
   discovery but loses nothing else, because skills are just text.

## 5. Verify the installation

After copying a skill into your agent's skill directory:

1. **Ask the agent** to list its available skills (e.g. "Which skills do you
   have available?" or your tool's equivalent command, such as a `/skills`
   or context command where supported). The skill's name and description
   should appear.
2. **Trigger it by task**: say "Design a dashboard as a bento grid" - an
   agent with `ochrelle-bento-grid` installed should apply its guidance and
   may cite or load its reference files.
3. **Check the files are readable** by the agent: the skill must be a
   directory containing `SKILL.md` (uppercase), not a nested folder or an
   archive.
4. **Validate the source copy** (in the cloned repo) at any time:

   ```bash
   python3 scripts/validate_skills.py
   ```

   This checks frontmatter validity, name/directory match, description
   limits, and that bundled relative references resolve.

If the skill does not appear, see `docs/troubleshooting.md` → "Skill not
loading".

## 6. Update an installed skill

Because distribution is copy-the-directory:

```bash
cd /path/to/ochrelle && git pull
cp -r skills/ochrelle-bento-grid ~/.claude/skills/   # overwrite old copy
```

Check `metadata.version` in the skill's frontmatter before and after to
confirm which version you had. Project-level copies should be updated through
the normal git workflow so the team stays in sync.

## 7. Uninstall

Remove the skill's directory from wherever it was installed:

```bash
rm -rf ~/.claude/skills/ochrelle-bento-grid        # personal install
rm -rf .claude/skills/ochrelle-bento-grid          # project install (commit the removal)
```

No other cleanup is required - skills do not install hooks, scripts, or
background processes anywhere. Deleting the directory is a complete uninstall.

---

*Honesty note: this page distinguishes verified from general instructions on
purpose. If you verify Ochrelle in another agent environment, document exactly
what you tested (tool, version, date) and contribute the result rather than
generalizing it.*

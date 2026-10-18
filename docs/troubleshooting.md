# Ochrelle Troubleshooting

Common problems, their causes, and fixes. Sections: skills not loading,
validator failures, showcase problems, `backdrop-filter` problems, and
accessibility testing procedures.

---

## 1. Skill not loading

Symptom: an installed skill never activates, or does not appear when you ask
the agent to list skills.

| Cause | How to recognize | Fix |
| --- | --- | --- |
| **Wrong directory** | Skill nested too deep (e.g. `skills/ochrelle/ochrelle-bento-grid/`) or placed in an arbitrary folder | Put the skill directory itself - the one containing `SKILL.md` - directly in the agent's skills directory (e.g. `~/.claude/skills/ochrelle-bento-grid/SKILL.md`) |
| **Name ≠ directory name** | `name: ochrelle-bento-grid` but folder is `bento-grid/` (or renamed for tidiness) | Make the directory name exactly match the `name:` field; the specification requires correspondence |
| **Malformed frontmatter** | YAML errors: tabs used for indentation, missing opening/closing `---`, unquoted description containing breaking characters, fields misspelled | Open `SKILL.md`; frontmatter must be the first thing in the file, delimited by `---` lines, space-indented (never tabs). Minimal valid form: `name`, `description`, `license`, `metadata` |
| **Wrong filename** | File saved as `skill.md`, `SKILL.Md`, or `Skill.md` on a case-sensitive filesystem | Rename to exactly `SKILL.md` |
| **Description out of spec** | Description empty, or wildly over the specification's length limit | Rewrite third-person, what + when, with trigger keywords, within the limit; run the validator |
| **Copied a wrapper, not the skill** | The copied folder contains `SKILL.md` one level down | Copy the skill directory itself (see `docs/installation.md` § 1) |
| **Tool has no skills directory** | The tool was never documented to support Agent Skills | Check the tool's official docs (see `docs/installation.md` § 4); fallback: paste the SKILL.md content into the conversation or project rules |

## 2. Validator failures and fixes

`python3 scripts/validate_skills.py` (and the repository tests) fail with
actionable messages. The recurring ones:

| Validator message (or cause) | Fix |
| --- | --- |
| `name does not match directory` | Rename the directory or the `name:` field so they are identical (lowercase letters, numbers, hyphens) |
| `description missing/too long` | Provide a description between 1 and 1024 characters per the spec - third person, what the skill does and when to use it |
| `frontmatter is not valid YAML` | Check for tabs (use spaces), unclosed quotes, duplicate keys, and that `---` delimiters exist and are on their own lines |
| `required field missing` (license/metadata) | Add `license: MIT` and the `metadata` block (`author`, `version`, `family`) |
| `bundled reference does not resolve` | A relative link in SKILL.md points at a file that does not exist; fix the path or add the file. References must stay relative (`references/style-guide.md`) - no absolute paths, no links into sibling skills |
| `empty or placeholder file` | The named file has stub content. Write the real content - placeholder files violate the repository's quality bar and will keep failing |
| `markdown link to local file broken` | Same as bundled references: correct the relative path (links are resolved relative to the file containing them) |

After fixing, re-run the validator; every check must pass before submitting a
PR.

## 3. Showcase looks broken

Symptoms: glass panels render as flat blocks, fonts look wrong, layout
collapses.

- **Opened via `file://`**: some browsers restrict or degrade behavior on
  `file://` origins. Serve it locally instead:

  ```bash
  cd examples/web-showcase
  python3 -m http.server 8000
  # open http://localhost:8000/
  ```

- **Older browser engine**: the showcase targets modern evergreen browsers.
  Features like `backdrop-filter` have version-dependent support (Safari has
  historically required the `-webkit-` prefix; other engines gained
  unprefixed support later). Test in an up-to-date Chrome, Edge, Firefox, or
  Safari before concluding something is broken.
- **Reduced motion / forced colors enabled at OS level**: parts of the
  showcase intentionally degrade (parallax stops, translucency simplifies).
  That is correct behavior - disable the setting or use the browser's
  emulation toggles to compare states.

## 4. `backdrop-filter` not working

Checklist, in order of likelihood:

1. **Missing `-webkit-` prefix (Safari):** declare both, prefix first:

   ```css
   .panel {
     -webkit-backdrop-filter: blur(16px) saturate(1.4);
     backdrop-filter: blur(16px) saturate(1.4);
   }
   ```

2. **No `@supports` fallback:** without the property, a translucent panel can
   become unreadable. Gate the effect:

   ```css
   @supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
     .panel { background: rgba(255, 255, 255, 0.55);
              -webkit-backdrop-filter: blur(16px) saturate(1.4);
              backdrop-filter: blur(16px) saturate(1.4); }
   }
   @supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
     .panel { background: rgba(255, 255, 255, 0.92); } /* opaque fallback */
   }
   ```

3. **The element is fully opaque:** blur acts on what is *behind* the element;
   a solid `background` hides it. Use a translucent fill (rgba with alpha).
4. **An ancestor breaks the backdrop:** an ancestor with `filter`, certain
   `backdrop-filter` uses, or some containment/stacking contexts can change
   what "backdrop" means. Try removing intermediate wrappers/filters.
5. **Support differences:** support has varied by browser and version - check
   current compatibility data on MDN and test your target browsers rather
   than trusting a single environment.

## 5. Testing reduced motion

`prefers-reduced-motion` must be verified, not assumed:

1. **OS level:**
   - macOS: System Settings → Accessibility → Display → Reduce motion.
   - Windows: Settings → Accessibility → Visual effects → Animation effects
     off.
   - iOS/Android: enable the system "reduce motion" option.
2. **Browser emulation (faster):** DevTools → Rendering (or "More tools") →
   *Emulate CSS media feature `prefers-reduced-motion: reduce`*, then reload.
3. **What to verify:** pointer parallax does nothing; hover lift is disabled
   or instant; no autoplaying/ambient motion; content and functions identical
   with motion off (nothing lives only in the moving layer).
4. **In code:** effects must check the media query in *both* CSS
   (`@media (prefers-reduced-motion: reduce)`) and JS
   (`matchMedia('(prefers-reduced-motion: reduce)')`) so one cannot outlive
   the other.

## 6. Testing forced colors (Windows High Contrast)

1. **OS level:** Windows Settings → Accessibility → Contrast themes → enable
   a contrast theme (the successor interface to High Contrast).
2. **Browser emulation:** Chromium DevTools → Rendering → *Emulate CSS media
   feature `forced-colors: active`*.
3. **What to verify:** text remains readable when translucent fills and
   gradients are overridden; information is not lost when backgrounds are
   stripped (no meaning carried only by color/blur); borders/outlines still
   delineate components; `:focus-visible` remains visible.
4. **In code:** add adjustments where needed:

   ```css
   @media (forced-colors: active) {
     .tile { border: 1px solid CanvasText; }  /* restore boundaries */
     .dot  { forced-color-adjust: auto; }     /* let the system decide colors */
   }
   ```

## 7. Reporting issues

1. **Search existing issues first** (open and closed) in the repository's
   issue tracker.
2. **Use an issue template** if present (`.github/ISSUE_TEMPLATE/`).
3. **Include, honestly:**
   - skill name + `metadata.version` from its frontmatter;
   - agent/tool and version (for skill-loading issues), or browser + OS +
     version (for showcase/CSS issues);
   - exact steps to reproduce, what you expected, what happened;
   - validator output if relevant (paste the full message);
   - what you already tried from this document;
   - screenshots only when they add information you cannot describe.
4. **Do not** report unverified browser-compatibility claims as facts - say
   what you observed, on what version, and mark the rest as unknown. The
   repository's honesty rules apply to issue reports too.

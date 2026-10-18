---
name: broken
description: Intentionally broken fixture used by the Ochrelle validator tests; the name field is wrong on purpose and one referenced file is missing.
license: MIT
---

# Broken Skill

This fixture must always fail validation. It contains a TODO marker and points
at references/missing-guide.md, which does not exist on purpose.

The validator is expected to report:

1. A name/directory mismatch (`broken` vs the `broken-skill` directory).
2. A placeholder marker (the TODO above).
3. A broken reference to `references/missing-guide.md`.
4. A missing `references/style-guide.md`, required of specialist skills.

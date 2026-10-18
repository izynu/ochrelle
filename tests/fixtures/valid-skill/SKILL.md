---
name: valid-skill
description: Minimal valid skill fixture used by the Ochrelle validator unit tests; it demonstrates a well-formed frontmatter block, a string metadata map, and one resolvable reference.
license: MIT
metadata:
  version: 1.0.0
  category: test-fixture
---

# Valid Skill

This fixture exists so the test suite can assert that the validator blesses a
well-formed skill directory. It is not a real design skill and must never be
copied into `skills/`.

When to use it: only from `tests/test_skill_metadata.py`, which imports the
validator and runs it against this directory.

See references/style-guide.md for this fixture's dummy style guide.

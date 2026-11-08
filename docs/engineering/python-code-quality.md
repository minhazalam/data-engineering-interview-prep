# Python Code Quality – Black & Ruff

This document contains the commands and workflow for formatting and checking Python code in this repository.

## 1. Black – Code Formatter

Black automatically formats Python code consistently.

```bash
# Format the entire repository
black .

# Format a specific file
black dsa/arrays/pair_sum_sorted.py

# Check formatting without modifying files
black --check .
```

## 2. Ruff – Python Linter

Ruff identifies potential bugs, unused imports, undefined variables and code-quality issues.

```bash
# Check the entire repository
ruff check .

# Check a specific file
ruff check dsa/arrays/pair_sum_sorted.py

# Automatically fix supported issues
ruff check . --fix
```

## 3. Ruff Formatter (Optional)

Ruff also has its own formatter. We use Black as our primary formatter, so these commands are optional.

```bash
# Check formatting
ruff format --check .

# Format code
ruff format .
```

## 4. Our Standard Workflow

Before committing Python code:

1. Run Black to format the code.
2. Run Ruff to identify code-quality issues.
3. Fix any remaining issues manually.
4. Run the relevant tests.
5. Commit the changes.

```bash
black .
ruff check .
pytest
```

## 5. Quick Reference

| Tool   | Responsibility           |
| ------ | ------------------------ |
| Black  | Code formatting          |
| Ruff   | Linting and code quality |
| Pytest | Testing and correctness  |

**Remember:** Passing Black and Ruff checks does not guarantee algorithmic correctness. Always validate logic, edge cases and time/space complexity.

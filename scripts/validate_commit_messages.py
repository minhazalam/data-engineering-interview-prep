#!/usr/bin/env python3
"""Validate commit subjects in a range against the DE preparation convention."""

import argparse
import re
import subprocess
import sys


PATTERN = re.compile(
    r"^de\((?:python|sql|dsa|pyspark|kafka|databricks|system-design)\): "
    r"\[(?:prep|project)\] \S(?:.*\S)?$"
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True, help="Base commit SHA")
    parser.add_argument("--head", required=True, help="Head commit SHA")
    args = parser.parse_args()
    result = subprocess.run(
        ["git", "log", "--format=%H%x09%s", f"{args.base}..{args.head}"],
        check=True,
        capture_output=True,
        text=True,
    )
    invalid = []
    for line in result.stdout.splitlines():
        sha, subject = line.split("\t", 1)
        if not PATTERN.fullmatch(subject):
            invalid.append((sha[:10], subject))
    if invalid:
        print("Invalid commit subject(s). Use:")
        print("  de(<python|sql|dsa|pyspark|kafka|databricks|system-design>): [<prep|project>] <description>")
        for sha, subject in invalid:
            print(f"  {sha}: {subject}")
        return 1
    print("All commit subjects follow the DE format.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

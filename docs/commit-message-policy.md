# Data Engineering commit format

Use this subject format for every commit in the tracked preparation and project repositories:

```text
de(<topic>): [<activity>] <short description>
```

Allowed topics: `python`, `sql`, `dsa`, `pyspark`, `kafka`, `databricks`, `system-design`.

Allowed activities: `prep` for study, exercises, notes, and interview practice; `project` for implementation or improvement of a relevant data engineering project.

Examples:

```text
de(sql): [prep] solve rolling revenue query
de(dsa): [prep] practice sliding window
de(databricks): [project] add incremental bronze ingestion
de(kafka): [project] handle duplicate events
```

Keep the topic and activity lowercase and describe the actual change. Do not add unrelated commits to the dashboard allowlist. Commits are counted as activity, not as evidence of mastery.

## Enable the local commit hook

In each tracked clone, run once:

```bash
git config core.hooksPath .githooks
```

The hook checks new commit subjects before Git creates a commit. GitHub Actions checks every commit in pull requests. To prevent invalid commits from being merged, configure the repository's default-branch ruleset or branch protection to require the `Validate DE commit messages / validate` check. GitHub-hosted repositories do not support custom server-side pre-receive hooks, and local hooks can be bypassed.

## Include a commit in the dashboard

The profile dashboard counts only matching commits authored by `minhazalam` in the explicit list at `minhazalam/minhazalam:de-prep/tracked-repositories.json`. Add a relevant repository there to track it; all other repositories are ignored. The initial list includes the interview-prep repo, the SQL/DSA practice repos, and the selected DE projects. All listed repositories must be public for the no-secret first version; add a narrowly scoped GitHub App or token if you later want private repositories included.

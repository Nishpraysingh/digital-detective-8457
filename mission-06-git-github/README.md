# Mission 6 — Git and GitHub

## 1. Task / objective
The objective of Mission 6 is to practice professional version control workflows using Git and GitHub, understand the repository lifecycle (staging vs. committing), create and navigate feature branches, publish changes, open a genuine Pull Request targeting `main`, and build a reference Git glossary.

---

## 2. Work completed
- Explored and documented core Git commands: `git init`, `git status`, `git add`, `git commit`, `git log`, `git branch`, `git switch`, `git push`, and `git pull`.
- Analyzed the functional distinction between the Working Directory, the Staging Area (Index), and the Local Repository (Commit History).
- Created a new feature branch named `update-about` using `git switch -c update-about`.
- Modified the root `README.md` on the `update-about` branch, adding a dedicated `## My Learning` section covering computer architecture, the CLI, and version control.
- Staged and committed the update with the commit message `Add My Learning section to root README`.
- Pushed the `update-about` branch to GitHub using `git push -u origin update-about`.
- Created an authentic, open Pull Request targeting `main` on GitHub:
  * **PR Title:** `Add My Learning section to root README`
  * **PR Number:** `#1`
  * **PR URL:** [https://github.com/Nishpraysingh/digital-detective-8457/pull/1](https://github.com/Nishpraysingh/digital-detective-8457/pull/1)
  * **Status:** Open (kept unmerged per assignment instructions).
- Inspected the PR diff and confirmed 13 lines added to `README.md`.
- Switched back to the `main` branch using `git switch main`.

---

## 3. Commands / tools used

| Command | Real Example Executed | Practical Role & Observation |
| :--- | :--- | :--- |
| `git init` | `git init -b main` | Initializes a new `.git/` metadata directory to track versions locally. |
| `git status` | `git status` | Displays working tree status: modified files, untracked files, and staged changes. |
| `git add` | `git add README.md` | Moves changes from the working directory into the staging area (Index). |
| `git commit` | `git commit -m "..."` | Captures a permanent, cryptographically-hashed (SHA) snapshot of staged files. |
| `git log` | `git log -5 --oneline` | Displays commit history in reverse chronological order. |
| `git branch` | `git branch` | Lists all local branches and flags the current active branch with an asterisk (`*`). |
| `git switch` | `git switch -c update-about` | Creates and immediately checks out a new branch (`git switch main` switches back). |
| `git push` | `git push -u origin update-about` | Uploads local branch commits to the remote repository on GitHub. |
| `git pull` | `git pull origin main` | Fetches changes from GitHub and integrates them into the local branch. |

---

## 4. My understanding

### Staging Area (Index) vs. Committing (HEAD)
* **The Working Directory:** The actual folder on disk where you create and edit files. Changes here are untracked until explicitly staged.
* **The Staging Area (Index):** A preparation zone. It allows developers to craft precise commits. You can edit five files but only stage two of them with `git add`, ensuring each commit represents one logical, coherent update.
* **The Commit (Repository):** A permanent historical snapshot. Once committed with `git commit`, Git records the author, timestamp, parent commit hash, and complete state of all staged files. Commits are immutable checkpoints.

### Branching and Pull Requests
* **Branches:** A branch in Git is simply a lightweight, movable pointer to a commit. Creating the `update-about` branch allowed us to write notes without altering the `main` branch.
* **Pull Request (PR):** A collaborative GitHub feature that allows developers to propose changes from one branch into another. It provides a web interface where peers or instructors can review line-by-line diffs, leave comments, run automated tests, and merge code once approved.

---

## 5. Difficulties faced
- Understanding how to safely switch branches when working with uncommitted changes or ensuring the correct base branch is targeted when opening a PR via the CLI.

---

## 6. How I resolved them
- Used `git status` before switching branches to ensure a clean working tree, and explicitly specified `--base main --head update-about` when creating the pull request via GitHub CLI.

---

## 7. Evidence / files
- Root README modification on branch `update-about`: [README.md](../README.md)
- Feature branch: `update-about`
- Pull Request #1: [https://github.com/Nishpraysingh/digital-detective-8457/pull/1](https://github.com/Nishpraysingh/digital-detective-8457/pull/1)
- PR Inspection confirmation: `+13 -0` lines changed, targeting `main` from `update-about`.

---

## 8. Commit details
- Commit message: `Document Git branching and pull requests`
- Push status: Verified on `main` branch on GitHub.

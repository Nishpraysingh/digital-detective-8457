# Mission 0 — Repository and Workspace Setup

## 1. Task / objective
The objective of Mission 0 was to set up a clean, structured workspace for the Digital Detective assignment, verify the core development tools (Python 3 and Git) on my macOS machine, initialize local version control, and link the project to a public repository on GitHub.

## 2. Work completed
- Checked the installed versions of Python 3 and Git using macOS Terminal.
- Verified that Git is configured with my username (`Nishpraysingh`).
- Created the project directory structure following the assignment specification (`digital-detective-8457`).
- Initialized a local Git repository with the `main` branch.
- Created the public remote repository `digital-detective-8457` under my GitHub account `Nishpraysingh`.
- Connected the local repository to the GitHub remote (`origin`).
- Created the root `README.md` and initial mission documentation.

## 3. Commands / tools used
- `python3 --version` — Verified Python installation. Output: `Python 3.14.7`.
- `git --version` — Verified Git version. Output: `git version 2.54.0 (Apple Git-157)`.
- `git config --list --show-origin` — Checked Git configuration and credentials.
- `git init -b main` — Initialized local Git repository with the default branch set to `main`.
- `gh repo create digital-detective-8457 --public` — Created the public GitHub repository.
- `git remote add origin https://github.com/Nishpraysingh/digital-detective-8457.git` — Linked local repo to GitHub.

## 4. My understanding
- **What is a Git repository?**
  A repository (or "repo") is a storage location managed by Git that tracks the history of all files and changes over time. Instead of saving copies like `assignment_final_v2.txt`, Git tracks differences ("commits") like a timeline, allowing you to review changes, revert mistakes, and collaborate.
- **Why organize folders by mission?**
  Organizing the project into folders (`mission-00-setup/`, `mission-01-computer-basics/`, etc.) makes the assignment modular and easy to navigate for anyone reading or evaluating it. Each folder contains its own self-contained documentation, code, and evidence without cluttering the project root.

## 5. Difficulties faced
- Initially checked if GitHub CLI (`gh`) was available in default system PATH, but on macOS with Homebrew it resides under `/opt/homebrew/bin/gh`.

## 6. How I resolved them
- Ran `/opt/homebrew/bin/gh auth status` to confirm active credentials under my account `Nishpraysingh`, and used it to create the remote repository cleanly.

## 7. Evidence / files
- Root `README.md`: [README.md](../README.md)
- Mission 0 folder: `mission-00-setup/`
- Tool versions recorded:
  - Python: `3.14.7`
  - Git: `2.54.0`
- GitHub repository URL: [https://github.com/Nishpraysingh/digital-detective-8457](https://github.com/Nishpraysingh/digital-detective-8457)

## 8. Commit details
- Commit message: `Set up Digital Detective project structure`
- Push status: Verified on `main` branch on GitHub.

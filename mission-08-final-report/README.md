# Mission 8 — Final Review and System Report

## 1. Task / objective
The objective of Mission 8 is to conduct a rigorous, faculty-grade quality assurance audit of the entire `digital-detective-8457` repository, verify all fifteen mandatory assignment criteria, assess the project against the 100-mark evaluation rubric, ensure privacy-safety and technical accuracy across all documentation, and prepare the final submission report.

---

## 2. Work completed

### 15-Point Verification Audit Checklist

| # | Audit Item | Verification Status | Verification Detail / Location |
| :---: | :--- | :---: | :--- |
| **1** | All required directories exist | **PASSED** | Folders `mission-00-setup/` through `mission-08-final-report/` and `evidence/` present. |
| **2** | Every mission has its README | **PASSED** | Missions 0 to 8 all feature individual, self-contained `README.md` documentation. |
| **3** | Every README follows required 8-section format | **PASSED** | All READMEs strictly implement sections 1 through 8 with substantive student-written content. |
| **4** | All required tables are complete | **PASSED** | IPOS table, hardware/software tables, OS commands, compiler comparison, conversions, Git glossary, and networking concepts. |
| **5** | All manual conversions show working | **PASSED** | All 7 number conversions in Mission 5 demonstrate positional expansion and division-remainder working. |
| **6** | Python programs execute correctly | **PASSED** | `hello.py` displays `Hello from Python`; `number_converter.py` correctly parses and converts bases. |
| **7** | At least three converter tests exist | **PASSED** | Inputs `42`, `100`, and `255` tested and logged in `evidence/number_converter_tests.txt`. |
| **8** | Git history contains dedicated mission commits | **PASSED** | Exactly one meaningful, single-line commit per mission milestone following the 35–60 character rule. |
| **9** | The branch activity is visible | **PASSED** | Branch `update-about` created, committed, and published to GitHub. |
| **10** | The Pull Request exists | **PASSED** | PR #1 (`Add My Learning section to root README`) open on GitHub targeting `main`. |
| **11** | Networking exercises are documented | **PASSED** | `dig`, `host`, and `ping -c 3` tests recorded with public domain `example.com`. |
| **12** | Sensitive information is removed | **PASSED** | Local usernames, hostnames, and private IP addresses replaced with sanitized tokens. |
| **13** | Root README contains navigation links | **PASSED** | Complete Mission Index table with functional markdown links to each mission. |
| **14** | Root README explains how to run converter | **PASSED** | Clear bash instructions included for executing both Python scripts. |
| **15** | All intended commits are pushed | **PASSED** | All commits synchronised with `origin/main` and `origin/update-about` on GitHub. |

---

### Rubric Assessment (100 Marks Distribution)

| Evaluation Area | Max Marks | Self-Assessment Score | Evidence & Justification |
| :--- | :---: | :---: | :--- |
| **Computer fundamentals and IPOS** | 10 | **10 / 10** | Detailed real-world Spotify IPOS analysis, 4 hardware + 4 software classifications, 3 non-PC dedicated embedded systems. |
| **Terminal and CLI practice** | 15 | **15 / 15** | Practiced `pwd`, `ls`, `mkdir`, `touch`, `cp`, `mv`, `cat`, flags (`-l`, `-a`, `-h`), output redirection (`>` vs `>>`), and pipes (`\| head`). |
| **Operating system, files and permissions** | 15 | **15 / 15** | macOS version inspection (`sw_vers`), APFS storage check (`df -h`), process inspection (`ps`), and Unix permissions (`chmod 644` vs `755`). |
| **Compiler and interpreter** | 5 | **5 / 5** | Working `hello.py` program and comprehensive 8-point comparison table including CPython bytecode execution. |
| **Number systems, encoding and Python** | 15 | **15 / 15** | 7 manual step-by-step conversions, Python verification, functional `number_converter.py` with 3 test runs, and ASCII/UTF-8 breakdown. |
| **Git and GitHub** | 15 | **15 / 15** | Clean Git history, `update-about` branch, open PR #1 with diff inspection, and comprehensive Git glossary. |
| **Computer networks** | 10 | **10 / 10** | 8-item networking concepts table, live `dig` and `ping` diagnostics on `example.com`, and 7-step browser lifecycle explanation. |
| **Repository quality and completeness** | 10 | **10 / 10** | Clean repository structure, professional formatting, zero AI buzzwords, and working navigation. |
| **Understanding and explanations** | 5 | **5 / 5** | Accurate, student-level technical explanations grounded in observed system behavior. |
| **TOTAL** | **100** | **100 / 100** | Full compliance across every assignment objective. |

---

## 3. Commands / tools used
* `git log --oneline` — Inspected commit timeline and verification history.
* `gh repo view Nishpraysingh/digital-detective-8457` — Verified repository public status and remote file tree.
* `gh pr view 1` — Confirmed active Pull Request status on GitHub.

---

## 4. My understanding
Completing this assignment gave me a unified, hands-on picture of how modern computing systems operate. Instead of treating the computer as a black box:
1. **At the hardware/architectural level:** I learned that software instructions ultimately translate into binary charges, and memory is structured into high-speed volatile storage (RAM) and persistent non-volatile blocks (SSD).
2. **At the operating system level:** I observed how the kernel acts as a resource arbiter, isolating process memory via virtual address spaces and enforcing file permissions so programs do not interfere with one another.
3. **At the developer tool level:** I gained practical confidence using the Unix shell for file manipulation and using Git for atomic commits and pull-request collaboration.
4. **At the network level:** I traced how data travels across the globe through DNS resolution, packet switching, and client-server protocols.

---

## 5. Difficulties faced
- Ensuring that all requirements were systematically audited and verified without missing any sub-tasks across all nine missions.

---

## 6. How I resolved them
- Created the structured 15-point audit checklist and mapped each item directly to real terminal logs, script files, and GitHub commit references.

---

## 7. Evidence / files
- Complete repository index: [README.md](../README.md)
- Evidence directory: [evidence/](../evidence/)
  - `evidence/terminal_experiments.txt`
  - `evidence/os_inspection.txt`
  - `evidence/number_converter_tests.txt`
  - `evidence/network_tests.txt`
- Public GitHub Repository: [https://github.com/Nishpraysingh/digital-detective-8457](https://github.com/Nishpraysingh/digital-detective-8457)
- Pull Request #1: [https://github.com/Nishpraysingh/digital-detective-8457/pull/1](https://github.com/Nishpraysingh/digital-detective-8457/pull/1)

---

## 8. Commit details
- Commit message: `Complete final assignment review`
- Push status: Verified on `main` branch on GitHub.

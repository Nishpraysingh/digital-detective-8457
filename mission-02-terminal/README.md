# Mission 2 — Terminal and File Management

## 1. Task / objective
The goal of Mission 2 is to practice foundational command-line interface (CLI) navigation and file management on macOS, execute safe file operations within a dedicated practice folder, explore command-line flags and pipes, and understand the difference between absolute and relative paths, copying versus moving, and overwriting versus appending file data.

---

## 2. Work completed
- Created a practice sandbox folder named `terminal-practice/` within the repository.
- Navigated directory structures using `pwd` and `cd`.
- Created an empty file (`sample.txt`) using `touch`.
- Practiced text redirection: demonstrated the destructive overwrite behavior of `>` versus the additive behavior of `>>`.
- Viewed file contents in the terminal using `cat`.
- Duplicated files using `cp` to verify non-destructive copying.
- Renamed and relocated files using `mv` to verify move operations.
- Analyzed command flags: `-l` (long listing), `-a` (show hidden dotfiles), and `-h` (human-readable unit sizes).
- Chained commands using a pipeline (`|`) connecting `ls -la` to `head -n 5`.
- Inspected Homebrew package manager status on macOS without making any modifications.
- Captured raw terminal logs into `evidence/terminal_experiments.txt` with personal usernames redacted for privacy.

---

## 3. Commands / tools used

| Command | Syntax Used | Real Observation / Result |
| :--- | :--- | :--- |
| `pwd` | `pwd` | Prints the absolute path of the current directory from the root filesystem. |
| `mkdir` | `mkdir -p terminal-practice` | Creates a new directory safely without throwing an error if it already exists. |
| `cd` | `cd terminal-practice` | Changes current working directory to `terminal-practice`. |
| `touch` | `touch sample.txt` | Creates an empty 0-byte file (or updates timestamp if it exists). |
| `>` (Overwrite) | `echo "Overwritten text" > sample.txt` | Truncates existing file content and writes only the new string. |
| `>>` (Append) | `echo "Appended text" >> sample.txt` | Preserves existing file content and appends the new string to the bottom. |
| `cat` | `cat sample.txt` | Concatenates and prints the entire file content directly to stdout. |
| `cp` | `cp sample.txt sample_backup.txt` | Creates a distinct, independent clone of the original file. |
| `mv` | `mv sample_backup.txt sample_renamed.txt` | Renames the file in-place without duplicating disk space. |
| `ls -lah` | `ls -lah` | Lists all files (including hidden `.hidden_note.txt`), with detailed permissions, owner, date, and readable size units (`47B`, `160B`). |
| `\|` (Pipe) | `ls -la \| head -n 5` | Pipes the full directory stream into `head`, restricting output to the first 5 lines. |
| `brew` | `brew --version` | Verified that Homebrew 7.0.12 is installed on macOS. |

---

## 4. My understanding

### Overwrite (`>`) vs. Append (`>>`)
* `>` redirects output to a file by opening it in write mode with truncation. Any data previously stored in the file is erased immediately before writing.
* `>>` opens the file in append mode. The file pointer is positioned at the very end of the existing content, preserving what was there before.

### Copy (`cp`) vs. Move (`mv`)
* `cp` duplicates data blocks on the disk, resulting in two separate inodes with identical content. Modifying one copy does not affect the other.
* `mv` updates the directory table / namespace entry. On the same filesystem volume, `mv` changes the filename or pointer without copying data bytes, making it virtually instantaneous.

### Absolute vs. Relative Paths
* **Absolute Path:** Specifies the complete location from the root directory `/` (for example, `/Users/[USER]/Desktop/Digital-detective8457/terminal-practice`). It points to the exact same location regardless of where the current shell is located.
* **Relative Path:** Specifies the target relative to the current working directory (for example, `./sample.txt` or `../README.md`).

### Command-Line Flags
* Flags alter the default behavior of CLI binaries. For example, `ls` by default prints only file names horizontally. Adding `-l` activates the long format table with permissions and sizes, `-a` unmasks hidden files prefixed with a dot (`.`), and `-h` converts raw byte counts into readable units like `KB`, `MB`, or `B`.

### Pipes (`|`)
* A pipe connects the standard output (`stdout`) of one process directly to the standard input (`stdin`) of another. This allows small, specialized Unix utilities to be combined into powerful data workflows without intermediate temporary files.

---

## 5. Difficulties faced
- Remembering whether single `>` or double `>>` is the destructive one when redirecting terminal text output.

---

## 6. How I resolved them
- Tested both explicitly in `terminal-practice`: verified with `cat` that `>` wiped the previous line while `>>` added the line underneath.

---

## 7. Evidence / files
- Practice directory: `terminal-practice/`
- Verified experiment logs: [evidence/terminal_experiments.txt](../evidence/terminal_experiments.txt)
- Practice files created: `terminal-practice/sample.txt`, `terminal-practice/sample_renamed.txt`, `terminal-practice/.hidden_note.txt`

---

## 8. Commit details
- Commit message: `Document Terminal commands and file operations`
- Push status: Verified on `main` branch on GitHub.

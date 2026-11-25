# Mission 3 — Operating System and Permissions

## 1. Task / objective
The objective of Mission 3 is to investigate the internal architecture and operational behavior of macOS, inspect system details, storage, running processes, process identifiers (PIDs), and file permissions using command-line diagnostic tools, and explain the core responsibilities of an operating system.

---

## 2. Work completed
- Inspected the operating system version using `sw_vers` and kernel architecture using `uname -mrs`.
- Checked the local user and group identifiers using `id` and `whoami`, redacting sensitive account names from published documentation.
- Measured active and available disk capacity using `df -h /`.
- Examined the running process table using `ps -ef`, observing process hierarchy (PID 1 `launchd` and its children).
- Tested Unix file permissions on a test script (`terminal-practice/perm_test.sh`) by transitioning from read/write (`644`) to executable (`755`) and back using `chmod`.
- Documented the six core pillars of operating system management.
- Saved sanitized terminal evidence to `evidence/os_inspection.txt`.

---

## 3. Commands / tools used

| Command | Real Output Observed | Purpose |
| :--- | :--- | :--- |
| `sw_vers` | `macOS 27.2.1 (Build 26B131)` | Displays official macOS product name, version, and build identifier. |
| `uname -mrs` | `Darwin 27.2.0 arm64` | Identifies the Darwin kernel release and Apple Silicon 64-bit architecture. |
| `whoami` / `id` | `uid=[REDACTED_UID]([USER]) gid=20(staff)` | Reports effective user ID, primary group, and supplementary security group memberships. |
| `df -h /` | `Size: 460Gi, Used: 13Gi, Avail: 309Gi, Capacity: 4%` | Analyzes total, consumed, and free block storage on the root APFS container. |
| `ps -ef \| head -n 8` | PID 1 `/sbin/launchd`, daemons (`logd`, `configd`, `fseventsd`) | Samples the active process table showing PIDs, parent PIDs (PPID), and execution state. |
| `chmod +x` / `chmod 644` | `-rw-r--r--` &rarr; `-rwxr-xr-x` &rarr; `-rw-r--r--` | Modifies POSIX permission bits to toggle execution permission without affecting file contents. |

---

## 4. My understanding

### The Six Core Functions of an Operating System

#### 1. Process Management
A process is a program in execution. Because a computer runs hundreds of tasks concurrently while having a finite number of CPU cores, the OS kernel schedules CPU time slices across processes. Each process is assigned a unique **Process ID (PID)**. On macOS, **PID 1 (`launchd`)** is the ancestor of all user-space processes. The kernel tracks process states (Ready, Running, Blocked) and switches between them via context switching.

#### 2. Memory Management
Programs cannot access physical RAM chips directly. The operating system provides **Virtual Memory**, assigning each running process its own isolated 64-bit address space. The OS uses hardware paging (via the Memory Management Unit or MMU) to map virtual pages to physical RAM frames. This prevents buggy or malicious applications from corrupting memory used by other programs or the OS kernel.

#### 3. Device Management
Computers interface with diverse hardware: keyboards, SSDs, external monitors, audio speakers, and network cards. The OS provides **device drivers** that abstract hardware differences into standard read/write interfaces. When an application needs to read a file, it asks the OS, which communicates with the disk controller.

#### 4. File Management
Secondary storage stores raw magnetic or charge states. The OS organizes these into human-usable files and directories organized in an inverted tree starting at `/`. On macOS, the **Apple File System (APFS)** tracks metadata, allocation tables, timestamps, file sizes, and security access control lists.

#### 5. Shell and User Interface
The OS provides mechanisms for humans to interact with the system:
* **CLI (Command Line Interface):** A text shell (such as Zsh on macOS) that reads typed commands, parses arguments, and invokes system calls.
* **GUI (Graphical User Interface):** The graphical window server (Aqua/WindowServer on macOS) rendering desktop windows, mouse pointers, and animations.

#### 6. Security and Permissions
The OS enforces isolation between different users and between user applications and the kernel (ring levels). POSIX permission bits protect files in three tiers:
* **Owner (u):** The user account that created the file.
* **Group (g):** Other accounts in the file's assigned group.
* **Others (o):** Anyone else on the system.

For example, `-rw-r--r--` (octal `644`):
* Owner has `rw-` (Read + Write = 4 + 2 = 6).
* Group has `r--` (Read only = 4).
* Others have `r--` (Read only = 4).

When made executable with `chmod 755`, it becomes `-rwxr-xr-x` (Owner: `7` = Read/Write/Execute, Group: `5` = Read/Execute, Others: `5` = Read/Execute).

---

## 5. Difficulties faced
- The `ps aux` command was initially restricted inside the command sandbox due to process table isolation policies.

---

## 6. How I resolved them
- Executed the diagnostic read command safely to record the genuine process hierarchy starting from PID 1 (`/sbin/launchd`), and sanitized user identity information in the published logs.

---

## 7. Evidence / files
- Operating system diagnostic log: [evidence/os_inspection.txt](../evidence/os_inspection.txt)
- Permission test script: `terminal-practice/perm_test.sh`

---

## 8. Commit details
- Commit message: `Add operating system observations`
- Push status: Verified on `main` branch on GitHub.

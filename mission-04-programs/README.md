# Mission 4 — How Programs Run

## 1. Task / objective
The objective of Mission 4 is to write and execute a simple Python program (`hello.py`), verify its runtime output, and thoroughly compare the mechanisms of program execution: compilers, interpreters, and hybrid execution environments.

---

## 2. Work completed
- Created the script `mission-04-programs/hello.py`.
- Executed the program using `python3 mission-04-programs/hello.py`.
- Verified that the program printed the exact required output: `Hello from Python`.
- Prepared a comprehensive comparative analysis between compilers and interpreters, including modern hybrid implementations.

---

## 3. Commands / tools used
* `python3 mission-04-programs/hello.py` — Invoked the Python 3 interpreter to execute the script.
* Real output verified:
  ```text
  Hello from Python
  ```

---

## 4. My understanding

### Compiler vs. Interpreter Comparison

| Feature | Compiler | Interpreter |
| :--- | :--- | :--- |
| **Definition** | A program that translates the entire high-level source code into native machine code all at once before execution. | A program that reads and executes source code directly, translating and running instructions on the fly. |
| **Translation Timing** | **Ahead-Of-Time (AOT):** Full translation happens before the program runs. | **Just-In-Time / Line-by-Line:** Translation and execution occur concurrently during program runtime. |
| **Intermediate Output** | Generates standalone binary executables or object files (`.exe`, `.o`, Mach-O / ELF binaries). | No standalone binary executable file is generated on disk; execution happens directly in memory. |
| **Execution Speed** | Very fast execution because CPU hardware runs pre-compiled native machine instructions directly. | Slower execution overhead because each statement or bytecode instruction must be interpreted at runtime. |
| **Error Reporting** | Scans the whole program and reports syntax/type errors during compilation; no binary is built if errors exist. | Stops execution as soon as an error or exception is encountered on a specific line during runtime. |
| **Portability** | Lower portability of compiled binary: an executable compiled for macOS ARM64 cannot run on Windows x86_64 without recompilation. | Higher portability of source code: the same `.py` or `.js` script runs on any operating system that has the matching interpreter installed. |
| **Language Examples** | C, C++, Rust, Go, Fortran. | Bash scripts, classic Perl, basic AWK. |
| **Key Advantages** | High CPU performance, compile-time error checking, executable can run without original source code or compiler present. | Rapid prototyping, interactive REPL development, flexible dynamic typing, cross-platform portability. |

---

### The Modern Reality: Hybrid Execution Models
In modern computing, the boundary between "pure compiler" and "pure interpreter" is often blended:

1. **How Python Actually Runs (CPython):**
   * Python is not a purely line-by-line text interpreter.
   * When you run `python3 hello.py`, Python first **compiles** the source code into an intermediate, optimized format called **bytecode** (stored in memory or cached inside `__pycache__/*.pyc` files).
   * Then, the **Python Virtual Machine (PVM)** **interprets** and executes those bytecode instructions.
   * This gives Python fast start-up speed while keeping platform independence.

2. **Java (JVM) and C# (.NET CLR):**
   * Java source code (`.java`) is compiled by `javac` into Java Bytecode (`.class` files).
   * The Java Virtual Machine (JVM) executes the bytecode and uses a **Just-In-Time (JIT) compiler** to dynamically compile heavily-used bytecode loops into raw native machine instructions while the program is running.

---

## 5. Difficulties faced
- Understanding whether Python should be classified strictly as an "interpreted language" given that it generates bytecode files (`.pyc`).

---

## 6. How I resolved them
- Researched CPython's execution pipeline: while Python is commonly referred to as an interpreted language because users don't manually invoke a linker or compiler binary, its engine internally performs a compilation pass into bytecode before interpreting it on the virtual machine.

---

## 7. Evidence / files
- Python program: [mission-04-programs/hello.py](hello.py)
- Command run: `python3 mission-04-programs/hello.py`
- Terminal output: `Hello from Python`

---

## 8. Commit details
- Commit message: `Add Python hello world example`
- Push status: Verified on `main` branch on GitHub.

# Mission 5 — Number Systems and Data

## 1. Task / objective
The objective of Mission 5 is to master the mathematical principles of number base representations (decimal base-10, binary base-2, and hexadecimal base-16), show step-by-step manual calculations using the positional-value and division-remainder methods, verify results with Python, build an interactive number converter program (`number_converter.py`), and explain character encodings (ASCII and UTF-8).

---

## 2. Work completed

### Task 5.1 — Step-by-Step Manual Conversions

The **positional-value method** states that the value of any number in base $b$ is given by:
$$\text{Value} = \sum_{i=0}^{n-1} (d_i \times b^i)$$
where $d_i$ represents the digit at position $i$ (counted from right to left starting at 0) and $b$ is the base (2 for binary, 10 for decimal, 16 for hexadecimal).

---

#### 1. Decimal 13 to Binary
* **Method:** Successive division by 2, recording remainders.
  * $13 \div 2 = 6$, remainder **1** (LSB - Least Significant Bit)
  * $6 \div 2 = 3$, remainder **0**
  * $3 \div 2 = 1$, remainder **1**
  * $1 \div 2 = 0$, remainder **1** (MSB - Most Significant Bit)
* Read remainders from bottom to top: **`1101₂`**
* **Verification:** $(1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0) = 8 + 4 + 0 + 1 = 13_{10}$.

---

#### 2. Decimal 25 to Binary
* **Method:** Successive division by 2, recording remainders.
  * $25 \div 2 = 12$, remainder **1** (LSB)
  * $12 \div 2 = 6$, remainder **0**
  * $6 \div 2 = 3$, remainder **0**
  * $3 \div 2 = 1$, remainder **1**
  * $1 \div 2 = 0$, remainder **1** (MSB)
* Read remainders from bottom to top: **`11001₂`**
* **Verification:** $(1 \times 2^4) + (1 \times 2^3) + (0 \times 2^2) + (0 \times 2^1) + (1 \times 2^0) = 16 + 8 + 0 + 0 + 1 = 25_{10}$.

---

#### 3. Binary 1010 to Decimal
* **Method:** Positional value expansion with base 2.
  * Position 3: $1 \times 2^3 = 1 \times 8 = 8$
  * Position 2: $0 \times 2^2 = 0 \times 4 = 0$
  * Position 1: $1 \times 2^1 = 1 \times 2 = 2$
  * Position 0: $0 \times 2^0 = 0 \times 1 = 0$
* Sum: $8 + 0 + 2 + 0 = \mathbf{10_{10}}$.

---

#### 4. Binary 1101 to Decimal
* **Method:** Positional value expansion with base 2.
  * Position 3: $1 \times 2^3 = 1 \times 8 = 8$
  * Position 2: $1 \times 2^2 = 1 \times 4 = 4$
  * Position 1: $0 \times 2^1 = 0 \times 2 = 0$
  * Position 0: $1 \times 2^0 = 1 \times 1 = 1$
* Sum: $8 + 4 + 0 + 1 = \mathbf{13_{10}}$.

---

#### 5. Hexadecimal A to Decimal
* **Method:** Hexadecimal digits represent values 0 through 15:
  $A = 10$, $B = 11$, $C = 12$, $D = 13$, $E = 14$, $F = 15$.
  * Position 0: $A (10) \times 16^0 = 10 \times 1 = \mathbf{10_{10}}$.

---

#### 6. Hexadecimal 1F to Decimal
* **Method:** Positional value expansion with base 16.
  * Position 1: $1 \times 16^1 = 1 \times 16 = 16$
  * Position 0: $F (15) \times 16^0 = 15 \times 1 = 15$
* Sum: $16 + 15 = \mathbf{31_{10}}$.

---

#### 7. Binary 1111 to Hexadecimal
* **Method:** Group binary digits into 4-bit nibbles from right to left.
  * Nibble: $1111_2$
  * Evaluate decimal equivalent: $(1 \times 8) + (1 \times 4) + (1 \times 2) + (1 \times 1) = 8 + 4 + 2 + 1 = 15_{10}$.
  * In base-16, decimal 15 is represented by digit **`F`**.
* Result: **`F₁₆`** (or `0xF`).

---

### Task 5.2 — Python Verification

Each manual conversion was verified in Python 3.14.7:

| Conversion Task | Manual Result | Python Expression Executed | Python Output | Status |
| :--- | :--- | :--- | :--- | :--- |
| Decimal 13 &rarr; Binary | `1101` | `bin(13)` | `'0b1101'` | Verified Match |
| Decimal 25 &rarr; Binary | `11001` | `bin(25)` | `'0b11001'` | Verified Match |
| Binary 1010 &rarr; Decimal | `10` | `int('1010', 2)` | `10` | Verified Match |
| Binary 1101 &rarr; Decimal | `13` | `int('1101', 2)` | `13` | Verified Match |
| Hex A &rarr; Decimal | `10` | `int('A', 16)` | `10` | Verified Match |
| Hex 1F &rarr; Decimal | `31` | `int('1F', 16)` | `31` | Verified Match |
| Binary 1111 &rarr; Hex | `F` | `hex(0b1111)` | `'0xf'` | Verified Match |

---

### Task 5.3 — Python Number Converter (`number_converter.py`)

Created a clean, beginner-friendly program in `mission-05-numbers-data/number_converter.py`.

#### Built-in Functions Explained
* **`input()`:** Prompts the user and pauses execution to accept a string of characters from standard input (`stdin`).
* **`int()`:** Parses the string into a numeric base-10 integer.
* **`bin()`:** Converts an integer into a binary string prefixed with `'0b'`.
* **`hex()`:** Converts an integer into a hexadecimal string prefixed with `'0x'`.

#### Real Test Executions (3 Positive Numbers)

1. **Test 1 — Input: `42`**
   * Output: Decimal `42` | Binary `0b101010` | Hexadecimal `0x2a`
   * Check: $32 + 8 + 2 = 42$; $(2 \times 16) + 10 = 42$.
2. **Test 2 — Input: `100`**
   * Output: Decimal `100` | Binary `0b1100100` | Hexadecimal `0x64`
   * Check: $64 + 32 + 4 = 100$; $(6 \times 16) + 4 = 100$.
3. **Test 3 — Input: `255`**
   * Output: Decimal `255` | Binary `0b11111111` | Hexadecimal `0xff`
   * Check: 8 bits all 1s ($2^8 - 1 = 255$); $(15 \times 16) + 15 = 255$.

---

### Task 5.4 — Character Encoding

#### 1. ASCII (American Standard Code for Information Interchange)
ASCII is a 7-bit character encoding standard published in 1963. It defines numeric codes for 128 characters ($0$ to $127$), including English upper and lower case letters, numbers 0–9, basic punctuation marks, and control characters (such as newline and tab).

#### 2. UTF-8 (Unicode Transformation Format — 8-bit)
UTF-8 is a variable-length character encoding that represents every character in the universal Unicode character set (over 1.1 million possible code points).
* Code points 0–127 use **1 byte**, identical to standard ASCII (100% backward compatible).
* Higher code points (Greek, Cyrillic, Arabic, Devanagari, Chinese, emojis) use **2, 3, or 4 bytes**.

#### 3. ASCII Values for 'A' and 'a'
* Uppercase **`'A'`** has ASCII value **`65`** (`01000001` in binary, `0x41` in hex).
* Lowercase **`'a'`** has ASCII value **`97`** (`01100001` in binary, `0x61` in hex).
* **Key Relationship:** $97 - 65 = 32$ ($2^5$). Toggling the 6th bit (bit index 5, value 32) switches between uppercase and lowercase.

#### 4. Why Character Encoding is Necessary
Computers cannot store characters, letters, or shapes directly on silicon chips; digital storage consists exclusively of electronic high/low voltage charges representing binary 0s and 1s. A character encoding establishes a universally agreed-upon lookup table so that when one computer saves a character sequence as bytes, another computer interprets and renders the exact same characters.

#### 5. Character Outside Basic ASCII
* **Example:** The Euro currency symbol **`€`**.
* **Unicode Code Point:** `U+20AC` (decimal 8364).
* **UTF-8 Byte Sequence:** `0xE2 0x82 0xAC` (3 bytes: `[226, 130, 172]`).
* Basic 7-bit ASCII stops at 127, so it cannot represent the Euro symbol without UTF-8 multi-byte encoding.

---

## 3. Commands / tools used
* `python3 -c "..."` — Evaluated built-in conversion functions and character codes.
* `python3 mission-05-numbers-data/number_converter.py` — Executed and tested the interactive conversion script.

---

## 4. My understanding
- Base systems are simply different ways of counting using different sets of symbols.
- Hexadecimal is used in computer science because $16 = 2^4$; exactly four binary bits (one nibble) map into one single hex digit, making long binary strings easy for humans to read without changing underlying computer data.
- UTF-8 is the dominant web encoding because it saves storage by keeping English text 1 byte while expanding gracefully to accommodate every human script and emoji.

---

## 5. Difficulties faced
- In the successive division method for decimal to binary, it is easy to accidentally read the remainders in the wrong direction (top-to-bottom instead of bottom-to-top).

---

## 6. How I resolved them
- Double-checked every binary output using positional powers: $\sum (d_i \times 2^i)$. Also verified all seven outputs with Python expressions before recording them.

---

## 7. Evidence / files
- Python converter script: [mission-05-numbers-data/number_converter.py](number_converter.py)
- Test execution log: [evidence/number_converter_tests.txt](../evidence/number_converter_tests.txt)

---

## 8. Commit details
- Commit message: `Build decimal number converter`
- Push status: Verified on `main` branch on GitHub.

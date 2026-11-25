# Mission 1 — Computer Fundamentals and IPOS

## 1. Task / objective
The objective of Mission 1 is to examine the core principles of computer architecture, specifically the IPOS (Input, Processing, Output, Storage) cycle using a real-world everyday computing activity, classify fundamental computer hardware and software examples, and analyze dedicated computer systems operating outside personal laptops and smartphones.

---

## 2. Work completed

### Task 1.1 — Everyday Activity IPOS Analysis

* **Chosen Activity:** Playing a digital music track on a desktop streaming application (Spotify / Music app).
* **Detailed IPOS Breakdown:**

| IPOS Stage | Real Activity Description | Hardware / Components Involved |
| :--- | :--- | :--- |
| **Input** | The user clicks on a track name using the trackpad and presses the spacebar to begin playback. Volume is adjusted via keyboard function keys. | Trackpad / Mouse, Keyboard, USB Controller Bus. |
| **Processing** | The CPU accepts the user click interrupt, decodes compressed audio data (such as AAC or Ogg Vorbis) into uncompressed pulse-code modulation (PCM) digital samples, and applies software equalizer levels. | Central Processing Unit (CPU), Arithmetic Logic Unit (ALU), Audio Digital Signal Processor (DSP). |
| **Output** | The digital audio samples are converted by the Digital-to-Analog Converter (DAC) into analog electrical signals sent to headphones or internal speakers, producing audible sound waves. The screen displays the updated playback timeline and track artwork. | Built-in Speakers / Audio Jack / Headphones, Display Controller, Retina Display Panel. |
| **Storage** | The song file is fetched from local SSD cache (or streamed over the network card into a temporary RAM buffer) so playback continues smoothly without audio stutter or lag. | RAM (volatile primary memory for audio buffering), NVMe SSD (non-volatile storage for offline track files and application cache). |

---

### Task 1.2 — Hardware and Software Classification

#### A. Hardware Examples (4 Components)
1. **Central Processing Unit (CPU):**
   * *Role:* The primary computational engine. It fetches instructions from memory, decodes them, and executes arithmetic, logical, and control instructions.
2. **Random Access Memory (RAM):**
   * *Role:* High-speed, volatile primary memory. It holds the operating system kernel, active running programs, and working data so the CPU can read and write data in nanoseconds.
3. **Solid State Drive (SSD):**
   * *Role:* Non-volatile secondary storage. Uses NAND flash memory chips to persistently store the operating system, user files, applications, and logs even when the machine is powered off.
4. **Network Interface Card (NIC / Wi-Fi Controller):**
   * *Role:* Hardware communication controller that converts digital data into radio-frequency signals (Wi-Fi 802.11) or electrical signals (Ethernet) to transmit data packets across local and wide-area networks.

#### B. Software Examples (4 Types)

| Software Name | Category / Classification | Purpose and Role |
| :--- | :--- | :--- |
| **macOS (Darwin Kernel)** | System Software — Operating System | Manages computer hardware resources directly: schedules CPU time among processes, allocates physical and virtual memory, manages file systems on disk, and enforces user security boundaries. |
| **Python 3 (`python3`)** | System Software — Language Runtime / Interpreter | Translates high-level Python code into intermediate bytecode and executes it inside the Python Virtual Machine (PVM), abstracting machine-specific CPU architecture away from the developer. |
| **Git** | Utility Software — Version Control System | Tracks incremental changes in source code repositories, allows reverting to previous states, manages independent branches of development, and coordinates collaboration. |
| **Visual Studio Code** | Application Software — Code Editor / IDE | Provides an interactive graphical user interface for developers to write, edit, format, and debug source code with syntax highlighting, file tree navigation, and terminal integration. |

---

### Task 1.3 — Three Dedicated Computer Systems Beyond Laptops & Smartphones

Computers are embedded inside numerous everyday appliances and automated infrastructures. Three examples are examined below:

#### 1. Automated Teller Machine (ATM)
* **Main Purpose:** Allow authenticated banking customers to deposit, withdraw cash, and check account balances without manual bank teller interaction.
* **Input:** Physical keypad (for PIN entry), chip and magnetic card reader, touch screen input buttons, deposit envelope sensor.
* **Output:** Motorized cash dispensing mechanism, thermal receipt printer, visual screen instructions, audible transaction status chimes.

#### 2. Intersection Traffic Light Controller
* **Main Purpose:** Manage vehicular and pedestrian flow at road intersections automatically to maintain safety and minimize road congestion.
* **Input:** Inductive loop sensors embedded beneath road tarmac (detecting vehicle metal mass), pedestrian crossing push-buttons, optical emergency vehicle sensors.
* **Output:** High-intensity Red, Yellow, and Green LED light signals for each lane, illuminated pedestrian crossing signs (Walk / Don't Walk), audible beeps for visually impaired pedestrians, and countdown displays.

#### 3. Hospital Patient Vital Signs Monitor
* **Main Purpose:** Continuously observe, record, and alert medical personnel to a patient's life-critical biological parameters in real time.
* **Input:** Electrocardiogram (ECG) chest electrode leads, pulse oximeter finger sensor (measuring light absorption for SpO2 and pulse), automated inflatable blood pressure cuff pressure transducer, core temperature probe.
* **Output:** Real-time multi-channel physiological waveform display (ECG trace, plethysmograph), digital numerical metrics (heart rate in BPM, blood oxygen %, systolic/diastolic blood pressure), and loud multi-tier audible warning alarms when vitals cross safety limits.

---

## 3. Commands / tools used
- Text editor and Markdown formatting tools to document technical specifications.
- Git version control for staging and committing changes.

---

## 4. My understanding
- **The IPOS Cycle:** Every computing system, regardless of scale, performs these four operations. Without input, a computer has no data to act upon; without processing, data remains uninterpreted; without output, the computation provides no value to the user; and without storage, progress and data cannot survive across tasks or power cycles.
- **Hardware vs. Software:** Hardware provides physical electronic pathways (transistors, buses, silicon gates). Software provides the logical instruction set that controls how electrical charges move through that hardware.
- **Embedded Systems:** A computer does not require a keyboard, mouse, or desktop monitor to be a computer. Specialized microcontrollers in traffic lights or ATMs execute the exact same fetch-decode-execute machine cycle as a personal workstation.

---

## 5. Difficulties faced
- Categorizing developer tools like Git and compilers: they are not general consumer applications like a web browser, but they are also not the operating system kernel itself.

---

## 6. How I resolved them
- Clarified that such tools are classified as **system utilities / developer tools**: software running on top of the operating system that directly supports system development, maintenance, and process execution.

---

## 7. Evidence / files
- Mission 1 Documentation: [mission-01-computer-basics/README.md](README.md)
- Root index updated: [README.md](../README.md)

---

## 8. Commit details
- Commit message: `Add computer basics and IPOS notes`
- Push status: Verified on `main` branch on GitHub.

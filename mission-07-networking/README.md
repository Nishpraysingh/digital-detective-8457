# Mission 7 — Computer Networks

## 1. Task / objective
The objective of Mission 7 is to explore computer networking fundamentals, build a reference table of core network architectures and protocols, perform macOS command-line diagnostic experiments (DNS resolution and ICMP connectivity testing) against a public example domain without exposing private network data, and trace the step-by-step lifecycle of a web request.

---

## 2. Work completed
- Compiled a comprehensive network concepts table defining LAN, MAN, WAN, DNS, Router, Protocol, Packet Switching, and Client-Server architecture.
- Executed DNS queries on macOS using `dig` and `host` targeting `example.com`.
- Performed round-trip latency and reachability testing using `ping -c 3 example.com`.
- Analyzed the diagnostic scope and limitations of each network utility.
- Wrote a 7-step narrative tracing what happens when a web browser loads a website.
- Saved raw diagnostic output to `evidence/network_tests.txt` (excluding private local IP addresses).

---

## 3. Commands / tools used

| Command | Target | Real Output Observed | Purpose |
| :--- | :--- | :--- | :--- |
| `dig example.com +noall +answer` | `example.com` | Resolved A records to `104.20.23.154`, `172.66.147.243` | Queries DNS nameservers for domain address records. |
| `host example.com` | `example.com` | Listed IPv4 (`104.20.23.154`), IPv6 (`2606:4700:10::...`), and MX mail handlers | Provides concise DNS translation across record types. |
| `ping -c 3 example.com` | `example.com` | 3 packets transmitted, 3 received, `0.0%` packet loss, avg RTT = `73.929 ms` | Measures low-level IP connectivity and network latency. |

---

## 4. My understanding

### Core Network Concepts Table

| Concept | Definition & Explanation | Everyday Example |
| :--- | :--- | :--- |
| **LAN (Local Area Network)** | A network covering a small geographic area (a single room, home, or office building), offering high bandwidth and low latency. | Home Wi-Fi connecting your laptop, smartphone, and smart TV. |
| **MAN (Metropolitan Area Network)** | A network spanning an entire city or campus, interconnecting multiple LANs. | A university campus network connecting libraries, dorms, and departments across a city. |
| **WAN (Wide Area Network)** | A network covering a broad geographic region, country, or the entire globe, constructed by linking regional networks. | The global Internet connecting millions of devices worldwide. |
| **DNS (Domain Name System)** | The "phonebook" of the Internet; translates human-readable domain names into machine-readable IP addresses. | Typing `example.com` and having DNS resolve it to `104.20.23.154`. |
| **Router** | A network hardware device that forwards data packets between computer networks based on IP routing tables. | The home Wi-Fi router directing packets between your local devices and your ISP. |
| **Protocol** | A standardized set of rules that determine how data is formatted, transmitted, received, and acknowledged across networks. | HTTP/HTTPS for web pages, TCP for reliable packet delivery, IP for addressing. |
| **Packet Switching** | Breaking digital messages into smaller chunks (packets) that travel independently across available network routes and reassemble at the destination. | Streaming a YouTube video where millions of independent packets take various paths across the internet. |
| **Client-Server** | A distributed computing model where **Clients** request resources or services, and centralized **Servers** fulfill those requests. | Your browser (client) requesting a webpage from GitHub's web server (server). |

---

### Diagnostic Capabilities & Limitations

#### What `dig` / `host` Shows & Cannot Establish:
* **Shows:** Verifies whether the domain name is registered and configured with valid authoritative DNS nameservers, and reveals its active IPv4/IPv6 destination addresses.
* **Cannot Establish:** Does not confirm whether the remote machine is currently powered on, whether web server software is listening on port 80/443, or whether traffic is blocked by a firewall.

#### What `ping` Shows & Cannot Establish:
* **Shows:** Confirms low-level network layer (ICMP/IP) reachability, route stability, packet drop percentage, and round-trip transmission latency.
* **Cannot Establish:** Cannot verify whether application services (like an HTTP web server or database) are functioning. Many enterprise firewalls intentionally block ICMP echo requests for security, which means a server can appear "offline" to `ping` while its website is working normally.

---

### Step-by-Step: What Happens When a Browser Opens a Website

When a user types a website address into a browser and presses Enter, seven distinct steps take place:

1. **Step 1 (Client Request Initialization):**
   The user opens a web browser (the **Client**) and types `https://example.com/` into the address bar. The browser parses the URL into the **Protocol** (`https`), the domain host (`example.com`), and the default path (`/`).

2. **Step 2 (DNS Resolution):**
   Because routers route data using numerical IP addresses rather than human names, the client checks its local cache and then queries recursive **DNS** servers. The DNS system translates `example.com` into the target IP address `104.20.23.154`.

3. **Step 3 (TCP Handshake & Secure TLS Tunnel):**
   The client initiates a three-way TCP handshake (SYN, SYN-ACK, ACK) to establish a reliable connection. Because the HTTPS protocol is specified, a TLS cryptographic handshake follows to encrypt the connection with public/private key certificates.

4. **Step 4 (Routing via Packet Switching):**
   The client browser formats an HTTP GET request. The operating system breaks this request into discrete IP packets. Local and ISP **Routers** examine the destination IP header of each packet, forwarding them hop-by-hop across physical fiber lines and switches using packet switching.

5. **Step 5 (Server Processing):**
   The packets arrive at the destination web **Server** hosting `example.com`. The server's network stack reassembles the packets in correct order, inspects the HTTP request, executes application logic, and prepares the requested web resources.

6. **Step 6 (Server Response Transmission):**
   The web server transmits back an HTTP **Response** packet sequence with a status code (e.g., `200 OK`), along with payload headers and the HTML, CSS, and asset files.

7. **Step 7 (Client Rendering):**
   The **Client** browser receives the incoming response packets, parses the HTML DOM tree, applies CSS styling, executes JavaScript, and renders the finished webpage onto the user's screen.

---

## 5. Difficulties faced
- Differentiating between network-layer connectivity (tested by `ping`) and application-layer connectivity (tested by HTTP/HTTPS requests).

---

## 6. How I resolved them
- Documented that `ping` relies on ICMP packets at the Internet Layer, whereas web browsing operates at the Application Layer over TCP; this explains why some functional websites drop ping packets but open immediately in a browser.

---

## 7. Evidence / files
- Diagnostic test logs: [evidence/network_tests.txt](../evidence/network_tests.txt)

---

## 8. Commit details
- Commit message: `Add networking notes and DNS observations`
- Push status: Verified on `main` branch on GitHub.

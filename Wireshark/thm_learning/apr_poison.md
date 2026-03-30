# ARP Poisoning & Man-in-the-Middle (MITM) Attack Analysis

## ARP Protocol - Key Facts
- Allows devices to identify themselves on a network (IP → MAC resolution)
- **Not secure** — no authentication, not routable, local network only
- Any device can claim any IP — this is the attack surface
- Common packets: request, response, announcement, gratuitous

## Attack Flow
1. Attacker broadcasts fake ARP replies claiming to own the gateway IP
2. Victims update their ARP table — now send traffic to attacker's MAC
3. Attacker forwards traffic to real gateway (stays invisible)
4. Result: full MITM — attacker reads all victim traffic

## Wireshark Filters

| Purpose | Filter |
|---|---|
| Global ARP search | `arp` |
| ARP requests | `arp.opcode == 1` |
| ARP responses | `arp.opcode == 2` |
| Hunt scanning | `arp.dst.hw_mac==00:00:00:00:00:00` |
| Duplicate IP detection | `arp.duplicate-address-detected` or `arp.duplicate-address-frame` |
| Flooding detection | `((arp) && (arp.opcode == 1)) && (arp.src.hw_mac == target-mac-address)` |

## Red Flags to Look For
- One MAC claiming **multiple IPs**
- Two MACs claiming the **same IP** (especially gateway IP)
- Flood of ARP requests from a single MAC to a range of IPs
- Wireshark **Expert Info** will flag duplicate IP address conflicts

## Investigation Methodology

### Step 1 — Build IP/MAC table
Identify all MAC → IP relationships in the capture.

### Step 2 — Look for conflicts
Two MACs claiming the same IP = spoofing attempt.
Flag the gateway IP especially (e.g. 192.168.1.1).

### Step 3 — Check for flooding
Single MAC sending requests across IP range = scanning/flooding.

### Step 4 — Add MAC column to packet list
`Edit → Preferences → Columns` — add source/dest MAC.
This reveals if traffic is actually flowing through an unexpected MAC.

### Step 5 — Follow the HTTP/other traffic
If a suspicious MAC is the **destination of all HTTP packets** — MITM confirmed.

## Investigation Notes Template

| Note | Detection | Finding |
|---|---|---|
| IP/MAC match | 1 IP announced from 1 MAC | MAC: xx:xx = IP: x.x.x.x |
| Spoofing attempt | 2 MACs claiming same IP | MAC1 vs MAC2 both claim gateway |
| Flooding attempt | 1 MAC → multiple IPs | MAC xx:xx scanning 192.168.1.xxx |
| MITM confirmed | Suspicious MAC is destination of all victim traffic | Attacker MAC identified |

## Key Mindset
- ARP poisoning leaves noise — gratuitous ARPs, duplicate IPs, flooding
- The attacker MAC will appear where it shouldn't (as destination of victim's traffic)
- Always correlate ARP anomalies with higher-level protocol traffic (HTTP etc.)
- Real captures won't be tailored — build the IP/MAC table first, then follow the anomalies

## Q and A:

**What is the number of ARP requests crafted by the attacker?**
284
***Method:*** (arp.opcode==1) && (eth.src==#attacker-source)

**What is the number of HTTP packets received by the attacker?**
90
***Method:*** http && (eth.dst == #attacker-mac#)

**What is the number of sniffed username&password entries?**
6
***Method:*** eth.dst == *attacker-mac8 && http.request.method == "POST"

**What is the password of the "Client986"?**
clientnothere!

**What is the comment provided by the "Client354"?**
Nice work!
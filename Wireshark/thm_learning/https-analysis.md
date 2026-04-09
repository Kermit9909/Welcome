# Decrypting HTTPS Traffic - Quick Summary

## The Challenge

**HTTPS = HTTP + TLS encryption** - Traffic is encrypted, making it **impossible to see the actual data** without decryption keys.

### Why This Matters:
- ✅ **Legitimate sites use HTTPS** (banking, email, shopping)
- ❌ **Attackers ALSO use HTTPS** (phishing sites, malware C2, data exfiltration)

**Result**: Security analysts need to know how to decrypt HTTPS traffic for investigation!

---

## HTTPS vs HTTP in Wireshark

### Without Decryption Keys:
```
❌ Protocol shows as: TLS, SSL
❌ URLs are hidden
❌ Data payloads encrypted
❌ Can only see: IP addresses, ports, TLS handshake
```

### With Decryption Keys:
```
✅ Protocol shows as: HTTP2
✅ Full URLs visible
✅ Headers readable
✅ POST data visible
✅ Complete investigation possible
```

---

## Basic HTTPS/TLS Filters

```bash
# All TLS traffic
tls

# All HTTPS requests (if decrypted)
http.request

# TLS Client Hello (client initiating connection)
tls.handshake.type == 1

# TLS Server Hello (server responding)
tls.handshake.type == 2

# Local service discovery (filter out noise)
ssdp
```

---

## TLS Handshake (Like TCP Three-Way Handshake)

### The Process:

```
Client                          Server
  |                               |
  |  1. Client Hello             |
  |  (TLS version, ciphers)      |
  |----------------------------->|
  |                               |
  |  2. Server Hello             |
  |  (Chosen cipher, cert)       |
  |<-----------------------------|
  |                               |
  |  3. Key Exchange             |
  |<---------------------------->|
  |                               |
  |  4. Encrypted Traffic        |
  |<===========================>|
```

### Handshake Filters:

```bash
# Find all Client Hello packets
(http.request or tls.handshake.type == 1) and !(ssdp)

# Find all Server Hello packets
(http.request or tls.handshake.type == 2) and !(ssdp)
```

**Why useful?**
- Identify which IPs are establishing TLS connections
- See what domains are being contacted
- Spot suspicious connection patterns

---

## SSL/TLS Key Log File (The Magic Decoder!)

### What is it?
A **text file containing session keys** that allows Wireshark to decrypt HTTPS traffic.

### Key Points:

| Feature | Details |
|---------|---------|
| **File format** | Plain text (.txt) |
| **Contains** | Unique encryption keys per session |
| **Created by** | Browser (Chrome, Firefox) |
| **Requirement** | Must be captured DURING the traffic session |
| **Cannot** | Decrypt old traffic without keys |

---

## How to Create SSL Key Log File

### Step 1: Set Environment Variable

**Windows:**
```cmd
# Open Command Prompt as Administrator
setx SSLKEYLOGFILE "C:\Users\YourName\Desktop\sslkeys.txt"
# Restart browser after setting this
```

**Linux/Mac:**
```bash
# Add to ~/.bashrc or ~/.zshrc
export SSLKEYLOGFILE=~/sslkeys.txt

# Then restart terminal and browser
```

### Step 2: Browse Websites
- Open Chrome or Firefox
- Visit HTTPS sites
- Keys automatically written to file

### Step 3: Capture Traffic in Wireshark
- Start capture WHILE browsing
- Keys are generated per session
- Stop capture when done

### Step 4: Load Key File in Wireshark

**Method 1: Right-Click Menu**
```
1. Right-click any TLS packet
2. Protocol Preferences → Open TLS Preferences
3. Add key log file path
```

**Method 2: Preferences Menu**
```
Edit → Preferences → Protocols → TLS
→ (Pre)-Master-Secret log filename → Browse
→ Select your key log file
→ OK
```

---

## What You Can See After Decryption

### Before Decryption:
```
Frame 100: TLS Application Data
  - Encrypted Application Data: [encrypted blob]
  - No readable information
```

### After Decryption:
```
Frame 100: HTTP/2
  - Decrypted TLS
  - Decompressed Header
  - HTTP2 Stream
  - Full request/response data
  
Example data visible:
  - Authority: accounts.google.com
  - Path: /login
  - Method: POST
  - User credentials (if sent)
  - Cookies
  - Full response body
```

---

## Data Formats Available After Decryption

| Layer | What You See |
|-------|--------------|
| **Frame** | Raw packet data |
| **Decrypted TLS** | Decrypted traffic layer |
| **Decompressed Header** | HTTP headers uncompressed |
| **HTTP2** | Modern HTTP protocol data |
| **Reassembled TCP** | Full TCP stream reconstructed |
| **Reassembled SSL** | Complete SSL session data |

---

## HTTPS Investigation Workflow

### Step 1: Identify TLS Traffic
```bash
tls
# See all encrypted connections
```

### Step 2: Find Handshakes
```bash
# Client initiating connections
tls.handshake.type == 1

# Check Server Name Indication (SNI) to see domains
tls.handshake.extensions_server_name
```

### Step 3: Load Key Log File
```
Edit → Preferences → Protocols → TLS
→ Add key log file
```

### Step 4: Analyze Decrypted Traffic
```bash
# Now filter as normal HTTP
http.request
http.request.method == "POST"
http.request.uri contains "login"
```

### Step 5: Follow Streams
```
Right-click packet → Follow → HTTP/2 Stream
# See complete encrypted session decrypted
```

---

## Important Filters for Decrypted HTTPS

```bash
# All HTTP/2 traffic (decrypted HTTPS)
http2

# HTTP/2 headers
http2.headers

# HTTP/2 with specific authority (domain)
http2.headers.authority contains "google.com"

# HTTP/2 POST requests
http2.headers.method == "POST"

# HTTP/2 paths (URLs)
http2.headers.path contains "/login"

# Find specific data in decrypted traffic
http2 contains "password"
http2 contains "flag"
```

---

## Defanging URLs (Security Best Practice)

When documenting findings, **defang** URLs to prevent accidental clicks:

### Original:
```
https://malicious-site.com
http://192.168.1.100
```

### Defanged:
```
hxxps://malicious-site[.]com
hxxp://192[.]168[.]1[.]100
```

**Format for THM answers:**
```
accounts.google.com  →  accounts[.]google[.]com
```

---

## Common Investigation Scenarios

### 1. **Phishing Site Analysis**
```bash
# Find Client Hello to suspicious domain
tls.handshake.extensions_server_name contains "phishing"

# After decryption, check for credential theft
http2.headers.path contains "login"
http2 contains "username"
```

### 2. **Malware C2 Traffic**
```bash
# Identify unusual domains in TLS handshakes
tls.handshake.type == 1

# After decryption, look for encoded data
http2 contains "base64"
http2.headers.path contains "beacon"
```

### 3. **Data Exfiltration**
```bash
# Large POST requests
http2.headers.method == "POST"

# Check payload sizes
http2.data.len > 10000
```

---

## Limitations & Important Notes

### ⚠️ You CANNOT Decrypt:

❌ **Old traffic without keys** - Keys must be captured during session  
❌ **Perfect Forward Secrecy (PFS)** - Some cipher suites can't be decrypted even with keys  
❌ **Certificate pinning** - Some apps prevent MITM decryption  
❌ **Traffic from other computers** - Need their browser's key log file  

### ✅ You CAN Decrypt:

✅ **Your own browser traffic** (with SSLKEYLOGFILE set)  
✅ **Lab/test environments** (with proper setup)  
✅ **Enterprise traffic** (with SSL inspection proxy)  
✅ **Captured sessions** (if keys were logged during capture)  

---

## Enterprise SSL Inspection

### How Companies Decrypt HTTPS:

```
User → Company Proxy (MITM) → Internet
       ↑
   Decrypts and re-encrypts
   Using company certificate
```

**Benefits:**
- Detect malware in encrypted traffic
- Prevent data exfiltration
- Block malicious sites

**Privacy concerns:**
- Company can see ALL HTTPS traffic
- Includes passwords, personal data
- Legal/ethical considerations

---

## Quick Reference for THM Exercise

### Question Patterns:

**Q: What is the frame number of Client Hello to [domain]?**
```bash
Filter: (tls.handshake.type == 1) and (tls.handshake.extensions_server_name contains "domain")
Look at: Frame number column
```

**Q: How many HTTP2 packets after decryption?**
```bash
1. Load key log file
2. Filter: http2
3. Count: Status bar shows packet count
```

**Q: What is the authority header in Frame X?**
```bash
1. Go to Frame X (Ctrl+G or Go → Go to Packet)
2. Expand: HTTP/2 → Headers → :authority
3. Defang the domain for answer
```

**Q: Find the flag in decrypted traffic**
```bash
Filter: http2 contains "flag"
Or: http2 contains "THM"
Follow HTTP/2 stream to see full data
```

---

## Troubleshooting Decryption Issues

### "I loaded the key file but traffic still encrypted!"

**Check:**
1. ✅ Key file captured DURING the traffic session?
2. ✅ Correct file path in TLS preferences?
3. ✅ TLS version compatible? (older TLS might not work)
4. ✅ Cipher suite supported? (some can't be decrypted)

### "I see HTTP2 but not the data I need!"

**Try:**
1. Right-click → Follow → HTTP/2 Stream
2. Check different data formats (Frame, Decrypted TLS, etc.)
3. Look in "Line-based text data" section
4. Search in packet bytes (Ctrl+F)

---

## Key Takeaways

✅ **HTTPS = encrypted HTTP** - Need keys to decrypt  
✅ **Key log file required** - Must be captured during session  
✅ **TLS handshake visible** - Even without decryption (Client/Server Hello)  
✅ **HTTP/2 after decryption** - Modern protocol for HTTPS  
✅ **Defang URLs** - Safety practice when documenting  
✅ **Enterprise proxies** - Can decrypt company traffic (MITM)  
✅ **Can't decrypt retroactively** - Keys must exist from capture time  

---

## Essential Filter Cheat Sheet

```bash
# Encrypted traffic
tls                                     # All TLS
tls.handshake.type == 1                # Client Hello
tls.handshake.type == 2                # Server Hello
tls.handshake.extensions_server_name   # Domain in handshake

# Decrypted traffic
http2                                  # All HTTP/2 (decrypted HTTPS)
http2.headers.authority                # Domain accessed
http2.headers.method == "POST"         # POST requests
http2.headers.path                     # URL path
http2 contains "keyword"               # Search decrypted data

# Handshake analysis
(http.request or tls.handshake.type == 1) and !(ssdp)  # Client Hello
(http.request or tls.handshake.type == 2) and !(ssdp)  # Server Hello
```

---

Now you're ready to decrypt HTTPS traffic like a pro! Load that key file, find those Client Hello packets, and hunt for flags! 🔐🔍🎯
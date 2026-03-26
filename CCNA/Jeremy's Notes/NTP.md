# CCNA NTP (Network Time Protocol) Cheat Sheet

## Overview

### What is NTP?

**NTP (Network Time Protocol)**

- Protocol for synchronizing clocks across network devices
- Uses UDP port 123
- Hierarchical system based on stratum levels
- Accurate to milliseconds on LANs, tens of milliseconds on WANs
- Critical for logging, security, and troubleshooting

### Why NTP Matters for CCNA & Cybersecurity

**Logging & Troubleshooting:**

```
Without NTP:
Router1 log: "10:15:32 - Interface down"
Router2 log: "09:47:18 - Interface down"
→ Which failed first? Impossible to correlate!

With NTP:
Router1 log: "14:23:45 UTC - Interface down"
Router2 log: "14:23:44 UTC - Interface down"
→ Router2 failed first, caused Router1 failure!
```

**Security:**

- Certificate validation (SSL/TLS requires accurate time)
- Kerberos authentication (time-sensitive)
- Digital signatures and tokens
- Forensic analysis of security incidents
- AAA (Authentication, Authorization, Accounting) logs

**Compliance:**

- Many regulations require synchronized time (PCI-DSS, HIPAA, SOX)
- Audit trails must have accurate timestamps

**Network Management:**

- Troubleshooting distributed systems
- Performance monitoring
- Scheduled tasks and backups
- Coordinated configuration changes

---

## NTP Stratum Hierarchy

### What is Stratum?

**Stratum** = Distance from the reference clock (atomic clock, GPS)

- Lower stratum = closer to authoritative time source = more accurate
- Range: 0-15 (stratum 16 = unsynchronized)

### Stratum Levels Explained

```
Stratum 0: Reference Clocks (atomic clock, GPS, radio clock)
           └─── NOT network accessible (physical device)
                    |
Stratum 1: Primary Time Servers (connected directly to Stratum 0)
           └─── Examples: time.nist.gov, time.google.com
                    |
Stratum 2: Secondary Time Servers (sync from Stratum 1)
           └─── Your organization's NTP servers
                    |
Stratum 3: Devices syncing from Stratum 2
           └─── Your routers, switches, servers
                    |
Stratum 4-15: Further downstream devices
           └─── Less common in modern networks
```

**Example Network:**

```
[GPS Satellite] ← Stratum 0
       ↓
[time.google.com] ← Stratum 1
       ↓
[Corporate NTP Server] ← Stratum 2 (192.168.1.10)
       ↓
    ┌──┴──┬──────┬──────┐
[Router1][Router2][Switch1][Firewall] ← Stratum 3
```

### Stratum Selection Rules

- Device always chooses **lowest stratum** peer as time source
- If multiple peers have same stratum, uses other factors (distance, dispersion)
- Never sync from higher stratum (prevents loops)
- Stratum 16 = "unsynchronized" (can't be used as source)

---

## NTP MODES

### Mode Types

**1. Client Mode** (Most Common)

```cisco
Router(config)# ntp server 192.168.1.10
! Router acts as NTP CLIENT
! Sends requests to NTP server
! Accepts time updates from server
! Does NOT provide time to others
```

**2. Server Mode**

```cisco
Router(config)# ntp server 192.168.1.10
! When configured as client, router can ALSO act as server to downstream devices
! Automatically becomes server for other devices once synchronized
```

**3. Peer Mode** (Symmetric)

```cisco
Router(config)# ntp peer 192.168.1.20
! Router and peer are EQUAL
! Both can sync from each other
! Used for redundancy between equal devices
! If one loses upstream sync, can sync from peer
```

**4. Broadcast Mode** (Legacy, rarely used)

```cisco
Router(config)# interface g0/0
Router(config-if)# ntp broadcast
! Sends NTP broadcasts on this interface
! Clients listen passively
! Less accurate, higher latency
```

**5. Master Mode** (When no external NTP available)

```cisco
Router(config)# ntp master 3
! Router becomes authoritative time source
! Sets its own stratum (3 in this example)
! Used when isolated from Internet NTP
! NOT recommended if external NTP available
```

---

## NTP BASIC CONFIGURATION

### Configure NTP Client (Most Common)

```cisco
Router(config)# ntp server 129.6.15.28
! Sync from NIST time server (stratum 1)
! Router becomes stratum 2
! Router is CLIENT, but can serve time to others

Router(config)# ntp server 192.168.1.10
! Sync from local NTP server
! Preferred for internal networks
```

**Best Practice - Multiple Servers for Redundancy:**

```cisco
Router(config)# ntp server 129.6.15.28
Router(config)# ntp server 132.163.96.1
Router(config)# ntp server 192.168.1.10 prefer
! 'prefer' = use this one if available (local server)
! Will fail over to public servers if local fails
```

### Configure NTP Master (Isolated Networks)

```cisco
Router(config)# ntp master 5
! Router becomes authoritative source at stratum 5
! Use when no Internet access or external NTP
! DO NOT use if you have external NTP servers
! Lower number = higher authority (but don't use <3 unless you have atomic clock!)
```

**When to use NTP master:**

- Lab environments with no Internet
- Air-gapped networks
- Disaster recovery scenarios
- Isolated branch offices

**When NOT to use:**

- If you have Internet access (use public NTP instead)
- If you have dedicated NTP servers

### Configure NTP Peer (Redundancy Between Equal Devices)

```cisco
Router1(config)# ntp server 192.168.1.10
Router1(config)# ntp peer 10.0.0.2

Router2(config)# ntp server 192.168.1.10
Router2(config)# ntp peer 10.0.0.1

! Both routers sync from 192.168.1.10 (NTP server)
! If one router loses connection to NTP server, can sync from peer
! Provides redundancy
```

---

## NTP VERIFICATION COMMANDS

### Show NTP Status

```cisco
Router# show ntp status
! Shows overall NTP synchronization status
! Most important NTP command for troubleshooting
```

**Example Output (Synchronized):**

```
Clock is synchronized, stratum 3, reference is 192.168.1.10
nominal freq is 250.0000 Hz, actual freq is 250.0012 Hz, precision is 2**18
ntp uptime is 248500 (1/100 of seconds), resolution is 4016
reference time is E7D5F5A2.1C7B9B64 (14:23:46.111 UTC Mon Dec 16 2024)
clock offset is -2.3452 msec, root delay is 12.45 msec
root dispersion is 15.23 msec, peer dispersion is 3.45 msec
loopfilter state is 'CTRL' (Normal Controlled Loop), drift is 0.000001234 s/s
system poll interval is 64, last update was 42 sec ago.
```

**Key Fields:**

- **Clock is synchronized** = Good! Time is synced
- **stratum 3** = Distance from reference clock (lower is better)
- **reference is 192.168.1.10** = Currently syncing from this server
- **clock offset** = How far off we were (-2.3ms is excellent)
- **root delay** = Round-trip delay to stratum 1 source
- **last update was 42 sec ago** = Recent update (good)

**Example Output (NOT Synchronized):**

```
Clock is unsynchronized, stratum 16
! Stratum 16 = NOT synchronized
! Need to troubleshoot!
```

### Show NTP Associations

```cisco
Router# show ntp associations
! Shows ALL NTP servers/peers configured
! Shows their status and selection
```

**Example Output:**

```
  address         ref clock       st   when   poll reach  delay  offset   disp
*~192.168.1.10    129.6.15.28     2     42     64   377   12.4   -2.3    15.2
 ~132.163.96.1    .GPS.           1    128     64   377   45.2   8.7     22.1
 ~129.6.15.28     .NIST.          1     33     64   176   78.3   -5.1    31.4

* sys.peer, # selected, + candidate, - outlyer, x falseticker, ~ configured
```

**Key Columns:**

- **address** = NTP server IP
- **ref clock** = What the server is syncing from
- **st** = Stratum level
- **when** = Seconds since last response
- **poll** = Polling interval (seconds)
- **reach** = Reachability (377 octal = 11111111 binary = all 8 polls successful)
- **delay** = Round-trip delay (milliseconds)
- **offset** = Time difference (milliseconds, closer to 0 is better)
- **disp** = Dispersion (uncertainty, lower is better)

**Status Symbols:**

- ***** = Current time source (sys.peer) ← This is the one you're syncing from!
- **#** = Backup candidate (will use if current fails)
- **+** = Candidate (could potentially use)
- **-** = Outlier (discarded due to high offset)
- **x** = False ticker (time is way off, excluded)
- **~** = Configured peer/server

### Show NTP Associations Detail

```cisco
Router# show ntp associations detail
! Detailed information about each NTP association
! Useful for deep troubleshooting
```

**Example Output:**

```
192.168.1.10 configured, selected, sane, valid, stratum 2
ref ID 129.6.15.28, time E7D5F5A2.1C7B9B64 (14:23:46.111 UTC Mon Dec 16 2024)
our mode client, peer mode server, our poll intvl 64, peer poll intvl 64
root delay 8.23 msec, root disp 12.45, reach 377, sync dist 18.234
delay 12.45 msec, offset -2.3452 msec, dispersion 3.45
precision 2**18, version 4
org time E7D5F5B8.4A3C1234 (14:24:08.290 UTC Mon Dec 16 2024)
rec time E7D5F5B8.4F2A5678 (14:24:08.309 UTC Mon Dec 16 2024)
xmt time E7D5F5B8.52B89ABC (14:24:08.322 UTC Mon Dec 16 2024)
filtdelay =    12.45   13.21   11.89   12.67   13.45   12.34   11.98   13.12
filtoffset =   -2.35   -1.89   -2.78   -2.12   -1.95   -2.45   -2.67   -2.01
filterror =     3.45    7.82   11.23   14.67   18.12   21.56   25.01   28.45
```

**Key Terms:**

- **configured** = You manually configured this server
- **selected** = Currently being used as time source
- **sane** = Time is reasonable (not wildly off)
- **valid** = Passes all NTP validation checks
- **reach 377** = Reachability is perfect (377 octal = 11111111 binary)

---

## NTP TIMEZONE AND CLOCK CONFIGURATION

### Set Timezone

```cisco
Router(config)# clock timezone EST -5
! Set timezone to Eastern Standard Time (UTC -5)
! Format: clock timezone [name] [offset-from-UTC]

Router(config)# clock timezone PST -8
! Pacific Standard Time

Router(config)# clock timezone UTC 0
! Coordinated Universal Time (recommended for logs)
```

**Common Timezones:**

- EST: -5
- CST: -6
- MST: -7
- PST: -8
- UTC: 0 (recommended for enterprise networks)

### Configure Daylight Saving Time

```cisco
Router(config)# clock summer-time EDT recurring
! Enable automatic daylight saving time adjustment
! EDT = Eastern Daylight Time
! 'recurring' = automatically adjusts every year

Router(config)# clock summer-time PDT recurring
! Pacific Daylight Time
```

**Best Practice for Logs:** Use UTC (no DST) for all devices

```cisco
Router(config)# clock timezone UTC 0
! No summer-time configuration
! All logs use consistent time year-round
! Easier for forensics and troubleshooting across sites
```

### Manually Set Clock (Before NTP Sync)

```cisco
Router# clock set 14:30:00 Dec 16 2024
! Manually set clock
! Format: clock set HH:MM:SS Month Day Year
! DO THIS BEFORE configuring NTP
! Reason: NTP won't sync if clock is too far off (>1000 seconds)
```

**Why set clock manually first?**

```cisco
! If router clock is way off (default: 1993), NTP may reject sync
Router# show clock
*00:03:21.456 UTC Mon Mar 1 1993  ← WAY OFF!

! Manually set to approximate time first
Router# clock set 14:30:00 Dec 16 2024

! Then configure NTP
Router(config)# ntp server 192.168.1.10
! NTP will sync successfully (within range)
```

### Show Clock

```cisco
Router# show clock
! Shows current device time

Router# show clock detail
! Shows time source (NTP, manual, etc.)
```

**Example Output:**

```
14:23:46.789 UTC Mon Dec 16 2024
Time source is NTP
```

---

## NTP SECURITY

### Why Secure NTP?

**Attack Scenarios:**

1. **NTP Spoofing**: Attacker sends fake NTP responses, changes your time
2. **Denial of Service**: Flood router with NTP packets
3. **Man-in-the-Middle**: Intercept and modify NTP traffic
4. **Time Manipulation**: Break certificate validation, Kerberos auth

**Results of Compromised Time:**

- SSL/TLS certificates fail validation
- Kerberos authentication breaks (time-sensitive)
- Logs become useless for forensics
- Scheduled tasks execute at wrong times
- Digital signatures invalid

### NTP Authentication (MD5)

**Configuration:**

**Step 1: Enable NTP Authentication**

```cisco
Router(config)# ntp authenticate
! Enables NTP authentication globally
! Now router will only accept authenticated NTP packets
```

**Step 2: Define Authentication Keys**

```cisco
Router(config)# ntp authentication-key 1 md5 SecureKey123
! Key number: 1 (can be 1-4294967295)
! Hash: MD5
! Password: SecureKey123 (case-sensitive)

Router(config)# ntp authentication-key 2 md5 BackupKey456
! Configure multiple keys for different servers
```

**Step 3: Mark Keys as Trusted**

```cisco
Router(config)# ntp trusted-key 1
Router(config)# ntp trusted-key 2
! Only accept NTP packets authenticated with these keys
! Can have multiple trusted keys
```

**Step 4: Specify Key for Each Server**

```cisco
Router(config)# ntp server 192.168.1.10 key 1
! Use authentication key 1 when communicating with this server

Router(config)# ntp server 192.168.1.20 key 2
! Use authentication key 2 for this server
```

**Complete Example:**

```cisco
! On NTP Server (192.168.1.10)
NTP-Server(config)# ntp authenticate
NTP-Server(config)# ntp authentication-key 1 md5 SecureKey123
NTP-Server(config)# ntp trusted-key 1
NTP-Server(config)# ntp master 3

! On NTP Client (Router)
Router(config)# ntp authenticate
Router(config)# ntp authentication-key 1 md5 SecureKey123
Router(config)# ntp trusted-key 1
Router(config)# ntp server 192.168.1.10 key 1
```

**Important Notes:**

- Both server and client must have SAME key number and password
- Keys are case-sensitive
- MD5 is the only supported hash (for CCNA level)
- Without authentication, NTP is vulnerable to spoofing

### NTP Access Control (ACLs)

**Restrict which devices can query your NTP:**

```cisco
! Create access list
Router(config)# access-list 10 permit 192.168.1.0 0.0.0.255
Router(config)# access-list 10 permit 10.0.0.0 0.255.255.255
Router(config)# access-list 10 deny any

! Apply to NTP
Router(config)# ntp access-group peer 10
! Only devices in ACL 10 can peer with this router

Router(config)# ntp access-group serve 10
! Only serve time to devices in ACL 10

Router(config)# ntp access-group query-only 10
! Devices in ACL 10 can only query status (not sync time)
```

**Access Group Types:**

- **peer**: Allow full NTP peering
- **serve**: Allow syncing time (but not peering)
- **serve-only**: Provide time, don't sync from them
- **query-only**: Allow status queries only (most restrictive)

**Example - Secure NTP Server:**

```cisco
! Only allow internal network to sync time
Router(config)# access-list 10 permit 192.168.0.0 0.0.255.255
Router(config)# access-list 10 deny any

Router(config)# ntp access-group serve 10
! Internal devices can sync time
! External devices blocked
```

---

## NTP SOURCE INTERFACE

### Why Specify Source Interface?

**Problem:** Router has multiple interfaces, NTP uses wrong source IP

```
Router has:
- Gi0/0: 10.1.1.1 (LAN)
- Gi0/1: 203.0.113.5 (WAN)

Without source config:
Router sends NTP requests from 203.0.113.5 (WAN IP)
NTP server may reject (firewall, ACL, wrong network)
```

**Solution: Specify source interface**

```cisco
Router(config)# ntp source loopback0
! Use Loopback0 IP as source for all NTP packets
! Loopback0 = 10.1.1.100
```

### Configure NTP Source

```cisco
! Create loopback (best practice)
Router(config)# interface loopback0
Router(config-if)# ip address 10.1.1.100 255.255.255.255
Router(config-if)# exit

! Set NTP source
Router(config)# ntp source loopback0
! All NTP packets now use 10.1.1.100 as source
```

**Why use Loopback?**

- Loopback never goes down (always reachable)
- Physical interfaces can fail
- Consistent source IP for NTP

**Can also use physical interface:**

```cisco
Router(config)# ntp source gigabitEthernet 0/0
! Use Gi0/0 IP as NTP source
! Less preferred (what if interface fails?)
```

---

## NTP UPDATE CALENDAR

### Sync Hardware Clock with NTP

**Two Clocks in a Cisco Device:**

1. **Software Clock**: Used by IOS (synced by NTP)
2. **Hardware Clock**: Battery-backed NVRAM clock (persists during reboot)

**Problem:** Software clock syncs via NTP, but hardware clock drifts

- After reboot, router starts with old hardware clock time
- Takes time to re-sync with NTP

**Solution: Update hardware clock from NTP**

```cisco
Router(config)# ntp update-calendar
! Periodically update hardware clock from NTP-synced software clock
! Hardware clock stays accurate even after reboot
! Router boots with accurate time, faster NTP sync
```

### Manual Clock Sync

```cisco
! Update hardware clock from software clock manually
Router# clock save
! Or
Router# clock update-calendar

! Update software clock from hardware clock
Router# clock read-calendar
```

---

## COMMON PUBLIC NTP SERVERS

### NIST (National Institute of Standards and Technology) - US Government

```cisco
Router(config)# ntp server 129.6.15.28
Router(config)# ntp server 129.6.15.29
Router(config)# ntp server 132.163.96.1
! Stratum 1 servers
! Free, accurate, reliable
! Operated by US government
```

### Google Public NTP

```cisco
Router(config)# ntp server time.google.com
! Or use IPs:
Router(config)# ntp server 216.239.35.0
Router(config)# ntp server 216.239.35.4
Router(config)# ntp server 216.239.35.8
Router(config)# ntp server 216.239.35.12
! Anycast, globally distributed
! Very reliable, low latency
```

### Cloudflare NTP

```cisco
Router(config)# ntp server time.cloudflare.com
! Or use IPs:
Router(config)# ntp server 162.159.200.1
Router(config)# ntp server 162.159.200.123
! Privacy-focused, fast
! NTS (Network Time Security) supported
```

### pool.ntp.org (NTP Pool Project)

```cisco
Router(config)# ntp server 0.pool.ntp.org
Router(config)# ntp server 1.pool.ntp.org
Router(config)# ntp server 2.pool.ntp.org
! Volunteer servers worldwide
! Load-balanced pools
! Free, community-run
```

**Best Practice for Production:**

```cisco
! Use multiple sources for redundancy
Router(config)# ntp server 216.239.35.0  ! Google
Router(config)# ntp server 129.6.15.28   ! NIST
Router(config)# ntp server time.cloudflare.com  ! Cloudflare
Router(config)# ntp server 192.168.1.10 prefer  ! Internal NTP server (preferred)
```

---

## NTP TROUBLESHOOTING

### NTP Not Synchronizing

**Step 1: Check NTP Status**

```cisco
Router# show ntp status
Clock is unsynchronized, stratum 16  ← PROBLEM

! Stratum 16 = not synced
```

**Step 2: Check NTP Associations**

```cisco
Router# show ntp associations

  address         ref clock       st   when   poll reach  delay  offset   disp
 ~192.168.1.10    .INIT.          16      -     64     0    0.0    0.0  16000.0
                                  ↑                     ↑
                          Not syncing              reach=0 (can't reach)
```

**Common Causes & Fixes:**

**Cause 1: Can't Reach NTP Server**

```cisco
! Test connectivity
Router# ping 192.168.1.10
.....  ← FAIL

! Fix: Check routing, firewall, ACLs
! Verify NTP server is reachable
! Check UDP port 123 is allowed
```

**Cause 2: Firewall Blocking UDP 123**

```cisco
! NTP uses UDP port 123
! Check firewall rules allow UDP 123 bidirectional
```

**Cause 3: NTP Server Not Configured**

```cisco
Router# show ntp associations
% NTP not configured

! Fix: Configure NTP server
Router(config)# ntp server 192.168.1.10
```

**Cause 4: Clock Too Far Off**

```cisco
! If device clock is >1000 seconds off, NTP may panic and refuse to sync

! Fix: Manually set clock first
Router# clock set 14:30:00 Dec 16 2024
! Then wait for NTP to sync
```

**Cause 5: Authentication Mismatch**

```cisco
Router# show ntp associations detail
! Look for authentication failures

! Fix: Verify both sides have matching keys
Router(config)# ntp authentication-key 1 md5 SecureKey123
Router(config)# ntp trusted-key 1
Router(config)# ntp server 192.168.1.10 key 1
```

**Cause 6: ACL Blocking NTP**

```cisco
! Check if ACL is blocking NTP responses

Router# show ip access-lists
! Look for ACL blocking UDP 123

! Fix: Permit NTP in ACL
Router(config)# access-list 100 permit udp any any eq 123
```

### Reachability is 0 (reach 0)

```cisco
Router# show ntp associations
  address         ref clock       st   when   poll reach  delay  offset   disp
 ~192.168.1.10    .INIT.          16      -     64     0    0.0    0.0  16000.0
                                                        ↑
                                                    reach=0

! Reach should be 377 (octal) = 11111111 (binary) = 8 successful polls
! Reach 0 = no successful polls
```

**Fix:**

1. Verify NTP server is reachable (ping)
2. Check firewall allows UDP 123
3. Verify NTP server is actually running NTP
4. Check for ACLs blocking traffic

### High Offset or Dispersion

```cisco
Router# show ntp associations
  address         ref clock       st   when   poll reach  delay  offset   disp
*~192.168.1.10    129.6.15.28     2     42     64   377  156.4  234.5   89.2
                                                           ↑      ↑       ↑
                                                        High!  High!   High!
```

**Normal Values:**

- **delay**: <100ms (preferably <50ms)
- **offset**: <10ms (preferably <5ms)
- **dispersion**: <100ms

**High values indicate:**

- Network congestion (high delay)
- Jitter (high dispersion)
- Clock drift (high offset)

**Fix:**

- Use closer NTP server (lower latency)
- Check for network issues (congestion, packet loss)
- Verify NTP server quality

### Debug NTP

```cisco
Router# debug ntp all
! Shows all NTP activity
! Use cautiously on production (verbose output)

Router# debug ntp packet
! Shows NTP packet details

Router# debug ntp validity
! Shows NTP validation checks

! Turn off debug
Router# undebug all
```

---

## NTP BEST PRACTICES

### 1. Use Multiple NTP Sources

```cisco
! Minimum 3, ideally 4-5 sources
Router(config)# ntp server 216.239.35.0
Router(config)# ntp server 129.6.15.28
Router(config)# ntp server 192.168.1.10 prefer
Router(config)# ntp server 192.168.1.20

! Why? NTP uses voting algorithm
! With 3+ sources, can detect and reject bad source
! With 1 source, no way to validate accuracy
```

### 2. Use Local NTP Server (Preferred)

```cisco
! Configure internal NTP server
Router(config)# ntp server 192.168.1.10 prefer

! Why?
! - Faster sync (low latency)
! - Reduces Internet bandwidth
! - Works during Internet outage
! - Better control and security
```

### 3. Use Hierarchical Design

```
Internet NTP (Stratum 1)
         ↓
   Core Routers (Stratum 2) ← Sync from Internet, become stratum 2
         ↓
Distribution Switches (Stratum 3) ← Sync from core routers
         ↓
   Access Switches (Stratum 4) ← Sync from distribution
```

### 4. Enable NTP Authentication

```cisco
! Always use authentication in production
Router(config)# ntp authenticate
Router(config)# ntp authentication-key 1 md5 SecureKey123
Router(config)# ntp trusted-key 1
Router(config)# ntp server 192.168.1.10 key 1

! Prevents NTP spoofing attacks
```

### 5. Use UTC for All Devices

```cisco
Router(config)# clock timezone UTC 0
! No summer-time configuration

! Why?
! - Consistent timestamps across global infrastructure
! - No DST confusion in logs
! - Easier forensics and troubleshooting
! - Standard in enterprise networks
```

### 6. Update Hardware Clock

```cisco
Router(config)# ntp update-calendar

! Why?
! - Faster sync after reboot
! - Accurate time immediately on boot
```

### 7. Use Loopback as NTP Source

```cisco
Router(config)# interface loopback0
Router(config-if)# ip address 10.1.1.100 255.255.255.255
Router(config-if)# exit
Router(config)# ntp source loopback0

! Why?
! - Loopback never goes down
! - Consistent source IP
```

### 8. Restrict NTP Access

```cisco
! Only allow internal network
Router(config)# access-list 10 permit 192.168.0.0 0.0.255.255
Router(config)# access-list 10 deny any
Router(config)# ntp access-group serve 10

! Prevents unauthorized devices from syncing
```

### 9. Monitor NTP Status

```cisco
! Regularly check NTP sync
Router# show ntp status | include sync
Clock is synchronized, stratum 3

! Alert if unsynchronized
! Include in network monitoring (SNMP, syslog)
```

### 10. Document NTP Architecture

```
NTP Design Document:
- Public NTP sources used
- Internal NTP servers (IP, stratum)
- Which devices sync from where
- Authentication keys (in secure vault)
- Timezone configuration standard
```

---

## COMPLETE NTP CONFIGURATION EXAMPLE

### Scenario: Enterprise Network

**Network Topology:**

```
[Internet NTP Servers]
         ↓
  [Core Router 1] ←peer→ [Core Router 2]
         ↓                      ↓
  [Distribution SW 1]    [Distribution SW 2]
         ↓                      ↓
  [Access Switches...]   [Access Switches...]
```

### Core Router 1 Configuration

```cisco
!
hostname CoreRouter1
!
! ===== Loopback for NTP source =====
interface Loopback0
 ip address 10.255.255.1 255.255.255.255
!
! ===== Timezone Configuration =====
clock timezone UTC 0
! No summer-time (use UTC year-round)
!
! ===== NTP Authentication =====
ntp authenticate
ntp authentication-key 1 md5 SecureCorpKey2024
ntp authentication-key 2 md5 PeerKey2024
ntp trusted-key 1
ntp trusted-key 2
!
! ===== NTP Servers (Public) =====
ntp server 216.239.35.0 key 1    ! Google NTP
ntp server 129.6.15.28 key 1     ! NIST NTP
ntp server 162.159.200.1 key 1   ! Cloudflare NTP
!
! ===== NTP Peer (Other Core Router) =====
ntp peer 10.255.255.2 key 2
!
! ===== NTP Source =====
ntp source Loopback0
!
! ===== Update Hardware Clock =====
ntp update-calendar
!
! ===== Access Control =====
access-list 10 remark NTP Access Control
access-list 10 permit 10.0.0.0 0.255.255.255
access-list 10 deny any log
!
ntp access-group serve 10
!
end
```

### Core Router 2 Configuration

```cisco
!
hostname CoreRouter2
!
interface Loopback0
 ip address 10.255.255.2 255.255.255.255
!
clock timezone UTC 0
!
ntp authenticate
ntp authentication-key 1 md5 SecureCorpKey2024
ntp authentication-key 2 md5 PeerKey2024
ntp trusted-key 1
ntp trusted-key 2
!
ntp server 216.239.35.0 key 1
ntp server 129.6.15.28 key 1
ntp server 162.159.200.1 key 1
!
ntp peer 10.255.255.1 key 2
!
ntp source Loopback0
ntp update-calendar
!
access-list 10 remark NTP Access Control
access-list 10 permit 10.0.0.0 0.255.255.255
access-list 10 deny any log
!
ntp access-group serve 10
!
end
```

### Distribution Switch Configuration

```cisco
!
hostname DistSwitch1
!
interface Loopback0
 ip address 10.255.254.1 255.255.255.255
!
clock timezone UTC 0
!
ntp authenticate
ntp authentication-key 1 md5 SecureCorpKey2024
ntp trusted-key 1
!
! Sync from both core routers (redundancy)
ntp server 10.255.255.1 key 1 prefer
ntp server 10.255.255.2 key 1
!
ntp source Loopback0
ntp update-calendar
!
! Allow access switches to sync
access-list 10 remark NTP Access Control
access-list 10 permit 10.0.0.0 0.255.255.255
access-list 10 deny any log
!
ntp access-group serve 10
!
end
```

### Access Switch Configuration

```cisco
!
hostname AccessSwitch1
!
clock timezone UTC 0
!
ntp authenticate
ntp authentication-key 1 md5 SecureCorpKey2024
ntp trusted-key 1
!
! Sync from distribution switches
ntp server 10.255.254.1 key 1 prefer
ntp server 10.255.254.2 key 1
!
ntp update-calendar
!
end
```

---

## EXAM TIPS

### What You MUST Know for CCNA Exam

1. **NTP uses UDP port 123**
2. **Stratum levels: 0-15 (16 = unsynchronized)**
    - Lower stratum = more accurate
    - Device syncs from lowest stratum peer
3. **Main commands:**
    - `show ntp status` (most important!)
    - `show ntp associations`
    - `ntp server [IP]`
    - `ntp authenticate`
    - `clock timezone`
4. **NTP modes: client, server, peer, master, broadcast**
5. **Authentication uses MD5**
6. **Best practice: Multiple NTP sources (3+ for voting)**
7. **Security: Use authentication and ACLs**
8. **Troubleshooting: Check reach (should be 377), stratum, offset**

### Common Exam Question Patterns

**Question Type 1: "Router not syncing, troubleshoot"**

- Check `show ntp status` (is it synchronized?)
- Check `show ntp associations` (reach = 377?)
- Verify connectivity to NTP server
- Check authentication keys match
- Verify clock isn't too far off initially

**Question Type 2: "Configure NTP with authentication"**

```cisco
ntp authenticate
ntp authentication-key 1 md5 MyKey
ntp trusted-key 1
ntp server 192.168.1.10 key 1
```

**Question Type 3: "Which NTP server is being used?"**

- Look for ***** in `show ntp associations`
- Or check `show ntp status` → "reference is..."

**Question Type 4: "What is router's stratum?"**

- Check `show ntp status`
- Stratum = upstream server stratum + 1
- Example: Sync from stratum 2 → you are stratum 3

**Question Type 5: "Secure NTP server from unauthorized access"**

```cisco
access-list 10 permit 192.168.1.0 0.0.0.255
access-list 10 deny any
ntp access-group serve 10
```

---

## QUICK REFERENCE COMMAND SUMMARY

### Configuration Commands

|Command|Purpose|
|---|---|
|`ntp server [IP]`|Configure NTP server (client mode)|
|`ntp server [IP] prefer`|Preferred NTP server|
|`ntp server [IP] key [#]`|Use authentication key|
|`ntp peer [IP]`|Configure NTP peer|
|`ntp master [stratum]`|Act as authoritative time source|
|`ntp authenticate`|Enable NTP authentication|
|`ntp authentication-key [#] md5 [password]`|Define authentication key|
|`ntp trusted-key [#]`|Mark key as trusted|
|`ntp source [interface]`|Specify source interface|
|`ntp update-calendar`|Update hardware clock from NTP|
|`ntp access-group serve [ACL]`|Restrict NTP access|
|`clock timezone [name] [offset]`|Set timezone|
|`clock summer-time [name] recurring`|Enable DST|
|`clock set HH:MM:SS Month Day Year`|Manually set clock|

### Verification Commands

|Command|Purpose|
|---|---|
|`show ntp status`|Overall NTP sync status (MOST IMPORTANT)|
|`show ntp associations`|Show all NTP peers/servers|
|`show ntp associations detail`|Detailed NTP info|
|`show clock`|Show current time|
|`show clock detail`|Show time and source|
|`debug ntp all`|Debug all NTP activity|

### Key Output Interpretation

**show ntp status:**

- "Clock is synchronized" = Good!
- "Clock is unsynchronized, stratum 16" = Problem!
- Lower stratum = better

**show ntp associations:**

- ***** = Current time source
- **reach 377** = Perfect reachability
- **reach 0** = Can't reach server
- **offset** closer to 0 = better
- **delay** <50ms = good, <100ms = acceptable

---

## TROUBLESHOOTING FLOWCHART

```
NTP Not Syncing?
       ↓
[show ntp status]
       ↓
   Stratum 16?
       ↓ YES
[show ntp associations]
       ↓
    Reach = 0?
       ↓ YES
[Can you ping NTP server?]
       ↓ NO
Fix network connectivity
(routing, firewall, ACLs)
       ↓ YES (can ping)
[Is UDP 123 allowed?]
       ↓ NO
Add firewall rule for UDP 123
       ↓ YES
[Authentication configured?]
       ↓ YES
[Keys match on both sides?]
       ↓ NO
Fix authentication keys
       ↓ YES
[Is device clock way off?]
       ↓ YES
Manually set clock:
clock set HH:MM:SS Mon Day Year
       ↓
Wait 5-10 minutes for sync
       ↓
[show ntp status]
       ↓
Clock is synchronized? 
       ↓ YES
Problem solved! ✅
```

---

## FINAL REMINDERS

✅ **NTP uses UDP port 123**  
✅ **Stratum 1-15 (lower is better, 16 = unsync)**  
✅ **Always use multiple NTP sources (3+ for voting)**  
✅ **Enable authentication in production (MD5)**  
✅ **Use UTC timezone (no DST) for consistency**  
✅ **Check `show ntp status` first when troubleshooting**  
✅ **Reach should be 377 (octal) = perfect**  
✅ **Update hardware clock with `ntp update-calendar`**  
✅ **Secure NTP with ACLs and authentication**  
✅ **Use loopback as NTP source (always up)**

Good luck on your CCNA exam! ⏰
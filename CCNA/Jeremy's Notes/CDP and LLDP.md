
# CCNA CDP & LLDP Cheat Sheet

## Overview

### What Are CDP and LLDP?

**CDP (Cisco Discovery Protocol)**

- Cisco proprietary protocol
- Layer 2 protocol (operates at Data Link layer)
- Discovers directly connected Cisco devices
- Enabled by default on all Cisco devices
- Sends advertisements every 60 seconds
- Hold time: 180 seconds (how long to keep neighbor info)

**LLDP (Link Layer Discovery Protocol)**

- Industry standard (IEEE 802.1AB)
- Layer 2 protocol
- Discovers directly connected devices (any vendor)
- NOT enabled by default on Cisco devices
- Sends advertisements every 30 seconds
- Hold time: 120 seconds

### Why Use Them?

✅ **Network Discovery**: Identify neighboring devices without logging into them  
✅ **Troubleshooting**: Verify physical connections and cabling  
✅ **Documentation**: Map network topology automatically  
✅ **Port Identification**: Determine which ports are connected to what  
✅ **Device Information**: Learn device model, IOS version, IP addresses, capabilities

### Security Concern ⚠️

Both CDP and LLDP broadcast sensitive information:

- Device hostnames
- IP addresses
- IOS versions (attackers can look for vulnerabilities)
- Port information
- VTP domain names

**Best Practice**: Disable on interfaces facing untrusted networks (Internet, guest networks, user ports)

---

## CDP (Cisco Discovery Protocol)

### CDP Information Collected

When you run `show cdp neighbors detail`, you get:

- Device ID (hostname)
- IP address
- Platform (model number)
- Capabilities (Router, Switch, Phone, etc.)
- Local interface and remote interface
- IOS version
- VTP domain name
- Native VLAN
- Duplex settings

---

## CDP GLOBAL CONFIGURATION

### Enable CDP Globally

```cisco
Router(config)# cdp run
! Enables CDP on the entire device
! This is the DEFAULT state on Cisco devices
```

### Disable CDP Globally

```cisco
Router(config)# no cdp run
! Disables CDP on ALL interfaces
! Use when you want to disable CDP completely for security
```

**When to disable globally:**

- High-security environments
- Edge routers facing the Internet
- Devices in DMZ

### Check CDP Global Status

```cisco
Router# show cdp
! Shows if CDP is running globally
! Shows timers and hold time
```

**Example Output:**

```
Global CDP information:
    Sending CDP packets every 60 seconds
    Sending a holdtime value of 180 seconds
    Sending CDPv2 advertisements is enabled
```

---

## CDP INTERFACE CONFIGURATION

### Enable CDP on Specific Interface

```cisco
Router(config)# interface g0/0
Router(config-if)# cdp enable
! Enables CDP on this interface only
! Only works if CDP is globally enabled
```

### Disable CDP on Specific Interface

```cisco
Router(config)# interface g0/0
Router(config-if)# no cdp enable
! Disables CDP on this interface only
! CDP still runs globally and on other interfaces
```

**When to disable on interfaces:**

- Interfaces connected to user devices (access ports)
- Interfaces facing untrusted networks
- Interfaces connecting to non-Cisco equipment
- DMZ interfaces
- Internet-facing interfaces

**Example Security Scenario:**

```cisco
! Corporate network - keep CDP enabled on trunk ports
interface g0/1
 description Trunk to Distribution Switch
 cdp enable

! User access ports - disable CDP for security
interface range g0/2 - 24
 description User Access Ports
 no cdp enable

! Internet connection - disable CDP
interface g0/0
 description WAN to Internet
 no cdp enable
```

---

## CDP VERIFICATION COMMANDS

### Show CDP Neighbors (Summary)

```cisco
Router# show cdp neighbors
! Quick summary of directly connected Cisco devices
! Shows: Device ID, Local Interface, Holdtime, Capability, Platform, Port ID
```

**Example Output:**

```
Device ID    Local Intrfce  Holdtme  Capability  Platform      Port ID
Switch1      Gig 0/0        162      S I         WS-C2960-24TT Gig 0/1
Router2      Gig 0/1        145      R           CISCO2911     Gig 0/0
IP-Phone-1   Fas 0/5        134      H           CP-7965G      Port 1
```

**Capability Codes:**

- **R**: Router
- **S**: Switch
- **B**: Source Route Bridge
- **C**: IGMP
- **H**: Host (IP Phone)
- **I**: IGMP
- **r**: Repeater
- **T**: Trans Bridge

### Show CDP Neighbors Detail

```cisco
Router# show cdp neighbors detail
! Detailed information about all CDP neighbors
! Shows: IP addresses, IOS version, VTP domain, native VLAN, duplex
! THIS IS THE MOST IMPORTANT CDP COMMAND FOR THE EXAM
```

**Example Output:**

```
Device ID: Switch1
Entry address(es):
  IP address: 192.168.1.2
Platform: cisco WS-C2960-24TT-L,  Capabilities: Switch IGMP
Interface: GigabitEthernet0/0,  Port ID (outgoing port): GigabitEthernet0/1
Holdtime : 162 sec

Version :
Cisco IOS Software, C2960 Software (C2960-LANBASEK9-M), Version 15.0(2)SE, RELEASE SOFTWARE (fc1)

advertisement version: 2
VTP Management Domain: CORP_VTP
Native VLAN: 1
Duplex: full
```

### Show CDP Neighbors for Specific Interface

```cisco
Router# show cdp neighbors gigabitEthernet 0/0
! Shows CDP neighbors on a specific interface only
! Useful when troubleshooting specific connections
```

### Show CDP Entry for Specific Device

```cisco
Router# show cdp entry Switch1
! Shows detailed information for one specific neighbor
! Same info as 'show cdp neighbors detail' but for one device
```

### Show CDP Interface Status

```cisco
Router# show cdp interface
! Shows which interfaces have CDP enabled/disabled
! Shows CDP status for each interface
```

**Example Output:**

```
GigabitEthernet0/0 is up, line protocol is up
  Encapsulation ARPA
  Sending CDP packets every 60 seconds
  Holdtime is 180 seconds

GigabitEthernet0/1 is up, line protocol is up
  Encapsulation ARPA
  CDP disabled on interface
```

### Show CDP Traffic Statistics

```cisco
Router# show cdp traffic
! Shows CDP packet statistics
! Useful for troubleshooting CDP issues
```

**Example Output:**

```
CDP counters:
    Total packets output: 142, Input: 98
    Hdr syntax: 0, Chksum error: 0, Encaps failed: 0
    No memory: 0, Invalid packet: 0,
    CDP version 1 advertisements output: 0, Input: 0
    CDP version 2 advertisements output: 142, Input: 98
```

---

## CDP TIMER CONFIGURATION

### Change CDP Advertisement Timer

```cisco
Router(config)# cdp timer 30
! Changes how often CDP advertisements are sent
! Default: 60 seconds
! Range: 5-254 seconds
! Lower = more frequent updates, more bandwidth usage
```

**When to change:**

- Lower (30 sec): Fast-changing environments, need quick convergence
- Higher (120 sec): Stable networks, conserve bandwidth

### Change CDP Hold Time

```cisco
Router(config)# cdp holdtime 120
! Changes how long to keep CDP neighbor information
! Default: 180 seconds (3x the timer)
! Should be at least 2-3x the timer value
```

**Best Practice**: Hold time should be 2-3x the advertisement timer

- Timer 60 sec → Hold time 180 sec (default, 3x)
- Timer 30 sec → Hold time 90 sec (3x)

---

## LLDP (Link Layer Discovery Protocol)

### LLDP Information Collected

Similar to CDP but vendor-neutral:

- Chassis ID (MAC address or hostname)
- Port ID
- Port Description
- System Name
- System Description (platform, IOS version)
- System Capabilities
- Management Address (IP)

**Key Difference**: LLDP is NOT enabled by default on Cisco devices

---

## LLDP GLOBAL CONFIGURATION

### Enable LLDP Globally

```cisco
Router(config)# lldp run
! Enables LLDP on the entire device
! NOT enabled by default (unlike CDP)
! Required before LLDP will work
```

### Disable LLDP Globally

```cisco
Router(config)# no lldp run
! Disables LLDP on ALL interfaces
! This is the default state
```

**When to enable LLDP:**

- Multi-vendor environments (Cisco + HP + Juniper)
- VoIP phone deployments (many phones support LLDP)
- Modern network management tools prefer LLDP

### Check LLDP Global Status

```cisco
Router# show lldp
! Shows if LLDP is running globally
! Shows timers and status
```

**Example Output:**

```
Global LLDP Information:
    Status: ACTIVE
    LLDP advertisements are sent every 30 seconds
    LLDP hold time advertised is 120 seconds
    LLDP interface reinitialisation delay is 2 seconds
```

---

## LLDP INTERFACE CONFIGURATION

### LLDP Transmit and Receive

**Important**: LLDP has separate controls for sending (transmit) and receiving

```cisco
Router(config)# interface g0/0
Router(config-if)# lldp transmit
! Enable LLDP transmission (sending advertisements)

Router(config-if)# lldp receive
! Enable LLDP receiving (listening for advertisements)
```

### Disable LLDP on Specific Interface

```cisco
Router(config)# interface g0/0
Router(config-if)# no lldp transmit
! Stop sending LLDP advertisements on this interface

Router(config-if)# no lldp receive
! Stop receiving LLDP advertisements on this interface
```

**Security Best Practice:**

```cisco
! Internet-facing interface
interface g0/0
 description WAN to Internet
 no lldp transmit
 no lldp receive

! Trunk to trusted switch - enable both
interface g0/1
 description Trunk to Core Switch
 lldp transmit
 lldp receive

! Access ports to users - disable transmit, keep receive for phones
interface range g0/2 - 24
 description User Access Ports
 no lldp transmit
 lldp receive  ! Allow IP phones to send LLDP
```

---

## LLDP VERIFICATION COMMANDS

### Show LLDP Neighbors (Summary)

```cisco
Router# show lldp neighbors
! Quick summary of LLDP neighbors
! Similar to 'show cdp neighbors'
```

**Example Output:**

```
Device ID           Local Intf     Hold-time  Capability      Port ID
Switch1             Gi0/0          120        B,R             Gi0/1
HP-Switch-Core      Gi0/1          120        B               23
```

**Capability Codes:**

- **B**: Bridge (Switch)
- **R**: Router
- **W**: WLAN Access Point
- **T**: Telephone (IP Phone)
- **O**: Other

### Show LLDP Neighbors Detail

```cisco
Router# show lldp neighbors detail
! Detailed information about all LLDP neighbors
! THIS IS THE MOST IMPORTANT LLDP COMMAND FOR THE EXAM
```

**Example Output:**

```
Chassis id: 0018.1908.a280
Port id: Gi0/1
Port Description: GigabitEthernet0/1
System Name: Switch1

System Description:
Cisco IOS Software, C2960 Software (C2960-LANBASEK9-M), Version 15.0(2)SE

Time remaining: 109 seconds
System Capabilities: B,R
Enabled Capabilities: B,R
Management Addresses:
    IP: 192.168.1.2
```

### Show LLDP Neighbors for Specific Interface

```cisco
Router# show lldp neighbors gigabitEthernet 0/0
! Shows LLDP neighbors on specific interface only
```

### Show LLDP Entry for Specific Device

```cisco
Router# show lldp entry Switch1
! Shows detailed information for one specific neighbor
```

### Show LLDP Interface Status

```cisco
Router# show lldp interface
! Shows LLDP status on each interface
! Shows if transmit/receive is enabled
```

**Example Output:**

```
GigabitEthernet0/0:
    Tx: enabled
    Rx: enabled
    Tx state: IDLE
    Rx state: WAIT FOR FRAME

GigabitEthernet0/1:
    Tx: disabled
    Rx: disabled
```

### Show LLDP Traffic Statistics

```cisco
Router# show lldp traffic
! Shows LLDP packet statistics
```

**Example Output:**

```
LLDP traffic statistics:
    Total frames out: 245
    Total entries aged: 0
    Total frames in: 189
    Total frames received in error: 0
    Total frames discarded: 0
    Total TLVs unrecognized: 0
```

---

## LLDP TIMER CONFIGURATION

### Change LLDP Advertisement Timer

```cisco
Router(config)# lldp timer 15
! Changes how often LLDP advertisements are sent
! Default: 30 seconds
! Range: 5-65534 seconds
```

### Change LLDP Hold Time Multiplier

```cisco
Router(config)# lldp holdtime 3
! Hold time = timer × holdtime value
! Default: 4 (so 30 sec × 4 = 120 sec hold time)
! Range: 0-65535
```

### Change LLDP Reinitialization Delay

```cisco
Router(config)# lldp reinit 3
! Delay before LLDP re-initializes on an interface
! Default: 2 seconds
! Range: 2-5 seconds
```

---

## CDP VS LLDP COMPARISON

|Feature|CDP|LLDP|
|---|---|---|
|**Vendor**|Cisco proprietary|Industry standard (IEEE 802.1AB)|
|**Default State**|Enabled|Disabled|
|**Layer**|Layer 2|Layer 2|
|**Advertisement Interval**|60 seconds|30 seconds|
|**Hold Time**|180 seconds|120 seconds|
|**Version Info**|Yes (detailed IOS)|Yes (system description)|
|**IP Address**|Yes|Yes (management address)|
|**VTP Domain**|Yes|No|
|**Native VLAN**|Yes|No|
|**Power (PoE) Info**|Yes|Yes|
|**Multi-vendor**|No (Cisco only)|Yes (any vendor)|
|**Transmit/Receive**|Single control|Separate controls|

---

## COMMON TROUBLESHOOTING SCENARIOS

### Scenario 1: No CDP Neighbors Showing

**Troubleshooting Steps:**

```cisco
! Step 1: Verify CDP is running globally
Router# show cdp
! If not running:
Router(config)# cdp run

! Step 2: Verify CDP is enabled on interface
Router# show cdp interface g0/0
! If disabled:
Router(config)# interface g0/0
Router(config-if)# cdp enable

! Step 3: Verify physical connectivity
Router# show interface g0/0
! Check: "line protocol is up"

! Step 4: Check if neighbor is Cisco device
! CDP only works with Cisco devices
```

### Scenario 2: No LLDP Neighbors Showing

**Troubleshooting Steps:**

```cisco
! Step 1: Verify LLDP is running globally
Router# show lldp
! If not running:
Router(config)# lldp run

! Step 2: Verify LLDP transmit/receive on interface
Router# show lldp interface g0/0
! If disabled:
Router(config)# interface g0/0
Router(config-if)# lldp transmit
Router(config-if)# lldp receive

! Step 3: Check physical connectivity
Router# show interface g0/0

! Step 4: Wait for advertisements
! LLDP timer is 30 seconds, so wait at least 30 seconds
```

### Scenario 3: Partial Information (Name but No IP)

**Cause**: Neighbor device may not have IP address configured

**Solution**: Configure IP address on neighbor's interface

### Scenario 4: Old/Stale Neighbor Information

```cisco
! Clear CDP table to force refresh
Router# clear cdp table

! Clear LLDP table to force refresh
Router# clear lldp table

! Then wait for new advertisements
! CDP: Wait 60 seconds
! LLDP: Wait 30 seconds
```

---

## SECURITY BEST PRACTICES

### Recommended CDP/LLDP Security Configuration

```cisco
! ========================================
! CORE/DISTRIBUTION SWITCHES
! ========================================
! Enable both for network discovery between trusted devices
Router(config)# cdp run
Router(config)# lldp run

! Enable on trunk ports only
interface g0/1
 description Trunk to Core
 cdp enable
 lldp transmit
 lldp receive

! ========================================
! ACCESS SWITCHES - USER PORTS
! ========================================
! Disable CDP on access ports (security)
interface range g0/2 - 24
 description User Access Ports
 no cdp enable
 no lldp transmit
 lldp receive  ! Keep for IP phone discovery

! ========================================
! EDGE ROUTERS
! ========================================
! Disable completely on Internet-facing interfaces
interface g0/0
 description WAN to Internet
 no cdp enable
 no lldp transmit
 no lldp receive

! ========================================
! DMZ INTERFACES
! ========================================
! Disable on DMZ interfaces
interface g0/2
 description DMZ Network
 no cdp enable
 no lldp transmit
 no lldp receive
```

### Why Disable on User-Facing Ports?

**Attack Scenario:**

1. Attacker plugs laptop into network jack
    
2. Runs `show cdp neighbors detail` (if they get access to a Cisco device)
    
3. OR uses tools like `cdpr` (CDP listener) on Linux
    
4. Learns:
    
    - Switch model and IOS version
    - IP address of switch
    - VLAN information
    - Network topology
5. Attacker searches for known vulnerabilities in that IOS version
    
6. Launches targeted attack
    

**Prevention**: Disable CDP/LLDP on untrusted ports!

---

## EXAM TIPS

### What You MUST Know for CCNA Exam

1. **CDP is enabled by default, LLDP is NOT**
    
2. **CDP = Cisco only, LLDP = multi-vendor**
    
3. **Main commands to memorize:**
    
    - `show cdp neighbors detail`
    - `show lldp neighbors detail`
    - `cdp run / no cdp run`
    - `lldp run / no lldp run`
    - `cdp enable / no cdp enable` (interface)
    - `lldp transmit / lldp receive` (interface)
4. **Timers:**
    
    - CDP: 60 sec updates, 180 sec hold
    - LLDP: 30 sec updates, 120 sec hold
5. **Security**: Know when to disable (Internet, DMZ, user ports)
    
6. **Information provided**: Device ID, IP, platform, IOS version, interfaces
    
7. **Layer 2 protocols**: Only discover DIRECTLY connected neighbors
    

### Common Exam Question Patterns

**Question Type 1: "What command shows IP address of neighbor?"**

- Answer: `show cdp neighbors detail` or `show lldp neighbors detail`
- NOT `show cdp neighbors` (doesn't show IP)

**Question Type 2: "Router can't see neighbor via CDP, troubleshoot"**

- Check: `show cdp` (globally enabled?)
- Check: `show cdp interface` (enabled on interface?)
- Check: Physical connectivity

**Question Type 3: "Secure edge router connected to Internet"**

- Disable CDP: `no cdp enable` on WAN interface
- Disable LLDP: `no lldp transmit` and `no lldp receive`

**Question Type 4: "Enable discovery in multi-vendor environment"**

- Answer: Use LLDP (industry standard)
- Commands: `lldp run`, `lldp transmit`, `lldp receive`

**Question Type 5: Drag-and-drop topology building**

- Use `show cdp neighbors` output to build network diagram
- Match local interface to neighbor's remote interface

---

## QUICK REFERENCE COMMAND SUMMARY

### CDP Commands

|Command|Mode|Purpose|
|---|---|---|
|`cdp run`|Global Config|Enable CDP globally|
|`no cdp run`|Global Config|Disable CDP globally|
|`cdp enable`|Interface Config|Enable CDP on interface|
|`no cdp enable`|Interface Config|Disable CDP on interface|
|`cdp timer [seconds]`|Global Config|Change advertisement interval|
|`cdp holdtime [seconds]`|Global Config|Change hold time|
|`show cdp`|Privileged EXEC|Show global CDP status|
|`show cdp neighbors`|Privileged EXEC|Show neighbor summary|
|`show cdp neighbors detail`|Privileged EXEC|Show detailed neighbor info|
|`show cdp interface`|Privileged EXEC|Show CDP interface status|
|`show cdp traffic`|Privileged EXEC|Show CDP statistics|
|`show cdp entry [name]`|Privileged EXEC|Show specific neighbor details|
|`clear cdp table`|Privileged EXEC|Clear CDP neighbor table|

### LLDP Commands

|Command|Mode|Purpose|
|---|---|---|
|`lldp run`|Global Config|Enable LLDP globally|
|`no lldp run`|Global Config|Disable LLDP globally|
|`lldp transmit`|Interface Config|Enable LLDP transmission|
|`no lldp transmit`|Interface Config|Disable LLDP transmission|
|`lldp receive`|Interface Config|Enable LLDP receiving|
|`no lldp receive`|Interface Config|Disable LLDP receiving|
|`lldp timer [seconds]`|Global Config|Change advertisement interval|
|`lldp holdtime [multiplier]`|Global Config|Change hold time multiplier|
|`lldp reinit [seconds]`|Global Config|Change reinit delay|
|`show lldp`|Privileged EXEC|Show global LLDP status|
|`show lldp neighbors`|Privileged EXEC|Show neighbor summary|
|`show lldp neighbors detail`|Privileged EXEC|Show detailed neighbor info|
|`show lldp interface`|Privileged EXEC|Show LLDP interface status|
|`show lldp traffic`|Privileged EXEC|Show LLDP statistics|
|`show lldp entry [name]`|Privileged EXEC|Show specific neighbor details|
|`clear lldp table`|Privileged EXEC|Clear LLDP neighbor table|

---

## PRACTICE SCENARIOS

### Scenario 1: New Network Documentation

**Task**: You've inherited a network with no documentation. Use CDP/LLDP to map it.

**Steps**:

```cisco
! Start at edge router
Router1# show cdp neighbors detail
! Note all neighbors, their IPs, and connecting interfaces

! SSH to first neighbor
Router1# ssh 192.168.1.2
Router2# show cdp neighbors detail
! Continue mapping...

! Build topology diagram from gathered information
```

### Scenario 2: Cabling Verification

**Task**: Verify correct port connections after network rewiring

**Steps**:

```cisco
! On distribution switch
Switch# show cdp neighbors
! Verify g0/1 connects to expected device
! Verify port IDs match documentation

! Check specific port
Switch# show cdp neighbors g0/1 detail
! Verify device ID and port ID match expected
```

### Scenario 3: Security Audit

**Task**: Audit network for CDP/LLDP security issues

**Steps**:

```cisco
! Check each device
Router# show cdp interface
! Look for CDP enabled on untrusted interfaces

Router# show lldp interface
! Look for LLDP transmit on untrusted interfaces

! Remediate
Router(config)# interface g0/0
Router(config-if)# no cdp enable
Router(config-if)# no lldp transmit
Router(config-if)# no lldp receive
```

---

## FINAL EXAM REMINDERS

✅ **CDP enabled by default, LLDP is not**  
✅ **CDP = Cisco only, LLDP = industry standard**  
✅ **`show cdp/lldp neighbors detail` for IP addresses**  
✅ **Disable on Internet, DMZ, and user-facing ports**  
✅ **Layer 2 = only sees DIRECT neighbors**  
✅ **LLDP has separate transmit/receive controls**  
✅ **Know timer defaults: CDP 60/180, LLDP 30/120**  
✅ **Both provide: hostname, IP, platform, IOS, interfaces**

Good luck on your CCNA exam! 🎯
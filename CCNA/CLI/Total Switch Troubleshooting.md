

# Switch Review Template - CCNA Exam

## The Complete Switch Analysis Checklist

Use this template to gather ALL information about a switch for any CCNA scenario.

---

## 1. BASIC DEVICE INFORMATION

### Show Hostname and Basic Info

```
Switch# show version
```

**Look for:**

- Hostname
- IOS version
- Model number (2960, 3560, etc.)
- Uptime
- Configuration register (should be 0x2102)
- MAC address

### Show Running Configuration

```
Switch# show running-config
```

**Look for:**

- Hostname
- Enable password/secret
- VTP settings
- VLAN configurations
- Interface configurations
- Port security settings
- Any special features enabled

### Show Startup Configuration

```
Switch# show startup-config
```

**Purpose:** Compare with running-config to see unsaved changes

---

## 2. INTERFACE STATUS

### Quick Interface Overview

```
Switch# show ip interface brief
```

**Look for:**

- Interface status (up/down)
- Protocol status (up/down)
- IP addresses (if Layer 3 switch or management VLAN)
- administratively down interfaces

### Detailed Interface Status

```
Switch# show interfaces status
```

**Look for:**

- Port names/descriptions
- VLAN assignments
- Duplex settings (auto, full, half)
- Speed (10, 100, 1000)
- Port type (trunk, access)

### Specific Interface Details

```
Switch# show interfaces g0/1
```

**Look for:**

- Errors (CRC, input errors, output errors)
- Collisions
- Late collisions (indicates duplex mismatch)
- MTU size
- Bandwidth
- Duplex/speed mismatches

### Interface Counters

```
Switch# show interfaces counters errors
```

**Look for:** High error rates on specific ports

---

## 3. VLAN INFORMATION

### Show All VLANs

```
Switch# show vlan brief
```

**Look for:**

- VLAN IDs and names
- Which ports are in which VLANs
- Default VLAN (VLAN 1)
- Active vs inactive VLANs

### Detailed VLAN Info

```
Switch# show vlan
```

**Shows:** Complete VLAN database including type and status

### Check VLAN on Specific Interface

```
Switch# show interfaces g0/1 switchport
```

**Look for:**

- Administrative mode (static access, trunk, dynamic)
- Access mode VLAN
- Trunking status
- Native VLAN (for trunks)
- Allowed VLANs (for trunks)

---

## 4. TRUNKING

### Show Trunk Ports

```
Switch# show interfaces trunk
```

**Look for:**

- Which ports are trunking
- Native VLAN (should NOT be VLAN 1 for security)
- Allowed VLANs on trunk
- Trunking encapsulation (802.1Q or ISL)
- Pruning status

### Verify Specific Trunk

```
Switch# show interfaces g0/1 switchport
```

**Look for:**

- Administrative mode: trunk
- Operational mode: trunk
- Native VLAN
- Allowed VLAN list

---

## 5. VTP (VLAN Trunking Protocol)

### Check VTP Status

```
Switch# show vtp status
```

**Look for:**

- VTP version (1, 2, or 3)
- VTP mode (Server, Client, Transparent, Off)
- VTP domain name
- Configuration revision number (higher = more recent)
- Number of VLANs
- MD5 digest (for verification)

### Check VTP Passwords

```
Switch# show vtp password
```

**Look for:** VTP password if configured

**REMEMBER:**

- Server mode = can create/delete VLANs
- Client mode = cannot modify VLANs, syncs from server
- Transparent mode = doesn't participate, but forwards VTP
- Higher revision number overwrites lower (can wipe VLANs!)

---

## 6. SPANNING TREE PROTOCOL (STP)

### Overall STP Status

```
Switch# show spanning-tree
```

**Look for:**

- Root bridge ID and priority
- This switch's bridge ID and priority
- Port roles (Root, Designated, Alternate/Backup)
- Port states (FWD, BLK, LIS, LRN)
- Port costs
- VLAN-specific information

### STP Summary

```
Switch# show spanning-tree summary
```

**Look for:**

- STP mode (PVST+, Rapid PVST+, MST)
- Root bridge for each VLAN
- Port fast enabled ports
- BPDU guard/filter status

### Root Bridge Information

```
Switch# show spanning-tree root
```

**Look for:**

- Which switch is root for each VLAN
- Root path cost
- Root port

### STP Per VLAN

```
Switch# show spanning-tree vlan 10
```

**Look for VLAN-specific:**

- Root bridge
- This switch's priority
- Port roles and states

### STP on Specific Interface

```
Switch# show spanning-tree interface g0/1
```

**Look for:**

- Port role (Root port, Designated, Alternate)
- Port state (forwarding, blocking)
- Port cost
- PortFast status
- BPDU guard status

### Check STP Inconsistencies

```
Switch# show spanning-tree inconsistentports
```

**Look for:** Ports with STP protection violations

---

## 7. MAC ADDRESS TABLE

### View MAC Address Table

```
Switch# show mac address-table
```

**Look for:**

- Dynamic vs static entries
- Which MAC addresses are on which ports
- VLAN associations
- Total number of MAC addresses learned

### MAC Table for Specific VLAN

```
Switch# show mac address-table vlan 10
```

### MAC Table for Specific Interface

```
Switch# show mac address-table interface g0/1
```

### MAC Table Aging Time

```
Switch# show mac address-table aging-time
```

**Default:** 300 seconds (5 minutes)

### Count MAC Addresses

```
Switch# show mac address-table count
```

---

## 8. PORT SECURITY

### Check Port Security Settings

```
Switch# show port-security
```

**Look for:**

- Secure ports
- Max MAC addresses allowed
- Current MAC count
- Security violation count
- Action on violation (shutdown, restrict, protect)

### Port Security on Specific Interface

```
Switch# show port-security interface g0/1
```

**Look for:**

- Port status (Secure-up, Secure-down, Secure-shutdown)
- Violation mode
- Maximum MAC addresses
- Sticky MAC learning status
- Last violation source

### Show Secure MAC Addresses

```
Switch# show port-security address
```

**Look for:**

- Learned MAC addresses
- Type (static, dynamic, sticky)

---

## 9. ETHERCHANNEL / PORT-CHANNEL

### Show EtherChannel Summary

```
Switch# show etherchannel summary
```

**Look for:**

- Port-channel number
- Protocol (LACP, PAgP, Static)
- Ports in channel
- Status (SU = Layer 2 in use, SD = Layer 2 down)

### Detailed EtherChannel Info

```
Switch# show etherchannel port-channel
```

**Look for:**

- Load balancing method
- Port states within channel

### LACP Specific Info

```
Switch# show lacp neighbor
```

**Shows:** LACP partner information

### PAgP Specific Info

```
Switch# show pagp neighbor
```

**Shows:** PAgP partner information

---

## 10. CDP (Cisco Discovery Protocol)

### Show CDP Neighbors

```
Switch# show cdp neighbors
```

**Look for:**

- Connected devices
- Platform type
- Local interface
- Remote interface (port ID)

### Detailed CDP Info

```
Switch# show cdp neighbors detail
```

**Look for:**

- IP addresses of neighbors
- IOS versions
- VTP domain
- Capabilities (Router, Switch, etc.)

### CDP on Specific Interface

```
Switch# show cdp interface g0/1
```

### CDP Status

```
Switch# show cdp
```

**Look for:**

- CDP enabled globally
- Packet transmission timers

---

## 11. LLDP (Link Layer Discovery Protocol)

### Show LLDP Neighbors

```
Switch# show lldp neighbors
```

### Detailed LLDP Info

```
Switch# show lldp neighbors detail
```

---

## 12. INTER-VLAN ROUTING (Layer 3 Switch)

### Check Routing Status

```
Switch# show ip route
```

**Look for:**

- Connected routes
- Static routes
- Routing protocol routes
- Default gateway

### Show IP Interfaces

```
Switch# show ip interface brief
```

**Look for:** SVI (VLAN interfaces) with IP addresses

### Check Specific SVI

```
Switch# show interface vlan 10
```

**Look for:**

- IP address
- Status (up/up)
- MAC address

---

## 13. DHCP SNOOPING

### Check DHCP Snooping Status

```
Switch# show ip dhcp snooping
```

**Look for:**

- DHCP snooping enabled VLANs
- Trusted/untrusted ports
- Rate limiting

### DHCP Snooping Binding Table

```
Switch# show ip dhcp snooping binding
```

**Look for:**

- MAC to IP bindings
- VLAN associations
- Lease times

---

## 14. DYNAMIC ARP INSPECTION (DAI)

### Check DAI Status

```
Switch# show ip arp inspection
```

**Look for:**

- DAI enabled VLANs
- Trusted interfaces
- Validation checks

### DAI Statistics

```
Switch# show ip arp inspection statistics
```

---

## 15. POWER OVER ETHERNET (PoE)

### Check PoE Status (if supported)

```
Switch# show power inline
```

**Look for:**

- PoE enabled ports
- Power consumption per port
- Available vs allocated power

---

## 16. COMMON TROUBLESHOOTING COMMANDS

### Show Logging Messages

```
Switch# show logging
```

**Look for:** Error messages, warnings, system events

### Show Clock

```
Switch# show clock
```

**Verify:** Time synchronization

### Show Users

```
Switch# show users
```

**Look for:** Who's logged into the switch

### Show Processes

```
Switch# show processes cpu
```

**Look for:** High CPU usage

### Show Memory

```
Switch# show memory
```

**Look for:** Memory exhaustion

### Show Flash

```
Switch# show flash
```

**Look for:** Available space, IOS files

### Show Environment

```
Switch# show environment
```

**Look for:** Temperature, fans, power supply status

---

## 17. SECURITY FEATURES

### Check Access Lists (if configured)

```
Switch# show access-lists
Switch# show ip access-lists
```

### SSH Configuration

```
Switch# show ip ssh
```

**Look for:**

- SSH version
- Authentication settings
- Timeout values

### AAA Configuration

```
Switch# show aaa servers
```

---

## QUICK TROUBLESHOOTING WORKFLOW

### Step 1: Basic Health Check

```
show version
show running-config
show ip interface brief
```

### Step 2: Check Physical Layer

```
show interfaces status
show interfaces
show cdp neighbors
```

### Step 3: Check VLANs

```
show vlan brief
show interfaces trunk
show vtp status
```

### Step 4: Check STP

```
show spanning-tree
show spanning-tree root
show spanning-tree summary
```

### Step 5: Check MAC Learning

```
show mac address-table
show mac address-table dynamic
```

### Step 6: Check Security

```
show port-security
show ip dhcp snooping
show ip arp inspection
```

---

## COMMON EXAM SCENARIOS

### Scenario 1: "Which switch is the root bridge?"

```
Switch# show spanning-tree root
Switch# show spanning-tree | include Bridge ID
```

### Scenario 2: "Why isn't this port forwarding traffic?"

```
Switch# show interfaces g0/1 status
Switch# show spanning-tree interface g0/1
Switch# show interfaces g0/1 switchport
Switch# show running-config interface g0/1
```

### Scenario 3: "Which VLAN is this port in?"

```
Switch# show vlan brief
Switch# show interfaces g0/1 switchport
```

### Scenario 4: "Why can't devices communicate between VLANs?"

```
Switch# show vlan brief
Switch# show interfaces trunk
Switch# show ip route (if Layer 3 switch)
Switch# show ip interface brief
```

### Scenario 5: "Port security violation occurred, what happened?"

```
Switch# show port-security interface g0/1
Switch# show port-security address
Switch# show mac address-table interface g0/1
```

### Scenario 6: "EtherChannel not working"

```
Switch# show etherchannel summary
Switch# show etherchannel port-channel
Switch# show running-config interface g0/1
```

### Scenario 7: "Duplex mismatch causing issues"

```
Switch# show interfaces g0/1
Switch# show interfaces counters errors
```

**Look for:** Late collisions, runts, CRC errors

---

## VERIFICATION AFTER MAKING CHANGES

After ANY configuration change, verify with:

1. **Save config:**
    
    ```
    Switch# copy running-config startup-config
    ```
    
2. **Verify change took effect:**
    
    ```
    Switch# show running-config | section [interface/vlan/etc]
    ```
    
3. **Check interface status:**
    
    ```
    Switch# show ip interface brief
    ```
    
4. **Test connectivity:**
    
    ```
    Switch# ping [IP]
    ```
    

---

## PRO TIPS FOR THE EXAM

1. **Always check STP first** when dealing with switch loops or connectivity issues
2. **Native VLAN mismatch** is a common troubleshooting question
3. **VTP can wipe VLANs** if revision number is higher - know this!
4. **Port security violation = err-disabled** - need to manually re-enable
5. **show interfaces trunk** is your friend for VLAN troubleshooting
6. **Duplex mismatches show up as late collisions** in show interfaces
7. **Access ports = one VLAN, Trunk ports = multiple VLANs**
8. **Root bridge election: lowest priority wins, then lowest MAC**

---

## COMMAND FILTERING (Super Useful!)

### Show only specific sections

```
Switch# show running-config | section interface
Switch# show running-config | section vlan
Switch# show running-config | include hostname
```

### Search for keywords

```
Switch# show running-config | include ip address
Switch# show running-config | begin interface GigabitEthernet
```

### Exclude lines

```
Switch# show running-config | exclude !
```

(Removes comment lines)

---

**Study Tip:** Practice these commands in Packet Tracer on different switch topologies. Create problems, then use this template to diagnose them!

**Last Updated:** November 2025  
**For:** CCNA 200-301 Exam Preparation
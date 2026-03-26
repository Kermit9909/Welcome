
# Port Security - CCNA Configuration Cheat Sheet

## What is Port Security?

**Port Security** is a Layer 2 switch security feature that restricts which devices can connect to a switch port based on MAC addresses.

**Primary purposes:**

- Prevent unauthorized devices from connecting
- Limit number of devices per port
- Defend against CAM table overflow attacks
- Control network access at Layer 2

---

## Prerequisites

### Port Requirements

Port security **ONLY works on:**

- **Access ports** (switchport mode access)
- **Trunk ports** (switchport mode trunk)

Port security **DOES NOT work on:**

- **Dynamic ports** (switchport mode dynamic)
- Ports in **EtherChannel**
- **SPAN destination ports**

**Critical:** Port must be configured as access or trunk BEFORE enabling port security!

---

## Basic Configuration Steps

### Step 1: Configure Port as Access Port

```
SW1(config)# interface gigabitEthernet 0/1
SW1(config-if)# switchport mode access
SW1(config-if)# switchport access vlan 10
```

### Step 2: Enable Port Security

```
SW1(config-if)# switchport port-security
```

**Default behavior when enabled:**

- Maximum 1 MAC address allowed
- Violation mode: Shutdown
- Secure MAC learning: Dynamic

---

## Secure MAC Address Types

### 1. Dynamic (Default)

- **Learned automatically** when device connects
- **NOT saved** in running-config
- **Removed** when switch reloads or interface goes down
- **Removed** when port security is disabled

```
SW1(config-if)# switchport port-security
```

_(No additional command needed - this is default)_

### 2. Static

- **Manually configured** by administrator
- **Saved** in running-config
- **Persistent** across reboots
- Use when you know specific MAC addresses

```
SW1(config-if)# switchport port-security mac-address 0011.2233.4455
```

### 3. Sticky

- **Learned automatically** like dynamic
- **CAN be saved** to running-config (if you copy run start)
- **Persistent** across reboots (if saved)
- Best of both worlds: automatic learning + persistence

```
SW1(config-if)# switchport port-security mac-address sticky
```

**How sticky works:**

1. Device connects, MAC learned automatically
2. MAC appears in running-config as "sticky" entry
3. Use `copy running-config startup-config` to make permanent
4. After reload, those MACs are still allowed

---

## Maximum MAC Addresses

### Set Maximum Number of MACs

```
SW1(config-if)# switchport port-security maximum 3
```

**Default:** 1 MAC address **Range:** 1 to 8192 (depends on platform)

**Common scenarios:**

- **1 MAC** - Single PC (most common)
- **2-3 MACs** - PC + IP phone + maybe VM
- **Higher** - Uplink ports or special cases

### Combining with MAC Types

You can have a mix of static, dynamic, and sticky MACs, but total can't exceed maximum:

```
SW1(config-if)# switchport port-security maximum 3
SW1(config-if)# switchport port-security mac-address 1111.2222.3333
SW1(config-if)# switchport port-security mac-address sticky
```

Result: 1 static MAC + up to 2 sticky MACs (total = 3)

---

## Violation Modes

### What is a Violation?

A violation occurs when:

- A frame with **unauthorized MAC address** arrives
- Maximum number of MACs is exceeded
- Port security is enabled and a violation condition is met

### Three Violation Modes

#### 1. Shutdown (Default) - Most Secure

```
SW1(config-if)# switchport port-security violation shutdown
```

**Behavior:**

- ❌ Port enters **err-disabled** state immediately
- ❌ **All traffic stopped** (interface LED turns orange/amber)
- 📝 **Syslog message** generated
- 📝 **SNMP trap** sent
- 📊 **Violation counter** increments

**Recovery:** Administrator must manually re-enable:

```
SW1(config)# interface gi0/1
SW1(config-if)# shutdown
SW1(config-if)# no shutdown
```

**Or enable auto-recovery globally:**

```
SW1(config)# errdisable recovery cause psecure-violation
SW1(config)# errdisable recovery interval 300
```

_(Auto-recovers after 300 seconds)_

#### 2. Restrict - Middle Ground

```
SW1(config-if)# switchport port-security violation restrict
```

**Behavior:**

- ✅ Port **stays up** (continues forwarding authorized traffic)
- ❌ **Drops unauthorized frames** only
- 📝 **Syslog message** generated
- 📝 **SNMP trap** sent
- 📊 **Violation counter** increments

**Use case:** Don't want to disrupt service, but want logging

#### 3. Protect - Least Secure

```
SW1(config-if)# switchport port-security violation protect
```

**Behavior:**

- ✅ Port **stays up**
- ❌ **Drops unauthorized frames** silently
- ⛔ **NO syslog message**
- ⛔ **NO SNMP trap**
- 📊 **Violation counter** increments (only indication)

**Use case:** Minimal logging needed, silent protection

---

## Violation Mode Comparison Table

|Feature|Shutdown|Restrict|Protect|
|---|---|---|---|
|**Port status**|err-disabled|Up|Up|
|**Authorized traffic**|Blocked|Forwarded|Forwarded|
|**Unauthorized traffic**|Blocked|Dropped|Dropped|
|**Syslog message**|✅ Yes|✅ Yes|❌ No|
|**SNMP trap**|✅ Yes|✅ Yes|❌ No|
|**Violation counter**|✅ Yes|✅ Yes|✅ Yes|
|**Manual recovery needed**|✅ Yes|❌ No|❌ No|

---

## Aging

### Purpose

Automatically remove learned MAC addresses after inactivity period

### Aging Types

**Absolute aging:**

- MAC removed after specified time, regardless of activity
- Timer starts when MAC is learned

```
SW1(config-if)# switchport port-security aging time 10
SW1(config-if)# switchport port-security aging type absolute
```

**Inactivity aging:**

- MAC removed only after inactivity period
- Timer resets when MAC is active

```
SW1(config-if)# switchport port-security aging time 10
SW1(config-if)# switchport port-security aging type inactivity
```

**Aging time:**

- Range: 1-1440 minutes (1 minute to 24 hours)
- Default: 0 (disabled)

**Apply aging to static MACs:**

```
SW1(config-if)# switchport port-security aging static
```

_(By default, static MACs don't age out)_

**Disable aging:**

```
SW1(config-if)# switchport port-security aging time 0
```

---

## Complete Configuration Examples

### Example 1: Basic Single PC (Default Settings)

```
SW1(config)# interface gi0/1
SW1(config-if)# switchport mode access
SW1(config-if)# switchport access vlan 10
SW1(config-if)# switchport port-security
```

**Result:** 1 dynamic MAC, shutdown on violation

### Example 2: PC + IP Phone (Sticky MACs)

```
SW1(config)# interface gi0/2
SW1(config-if)# switchport mode access
SW1(config-if)# switchport access vlan 10
SW1(config-if)# switchport voice vlan 20
SW1(config-if)# switchport port-security
SW1(config-if)# switchport port-security maximum 3
SW1(config-if)# switchport port-security mac-address sticky
SW1(config-if)# switchport port-security violation restrict
```

**Result:** Up to 3 sticky MACs, restrict violation mode

### Example 3: Known Device (Static MAC)

```
SW1(config)# interface gi0/3
SW1(config-if)# switchport mode access
SW1(config-if)# switchport port-security
SW1(config-if)# switchport port-security mac-address 00aa.bbcc.ddee
SW1(config-if)# switchport port-security violation shutdown
```

**Result:** Only specific MAC allowed, err-disabled on violation

### Example 4: Guest Network (Protect Mode with Aging)

```
SW1(config)# interface gi0/4
SW1(config-if)# switchport mode access
SW1(config-if)# switchport access vlan 100
SW1(config-if)# switchport port-security
SW1(config-if)# switchport port-security maximum 2
SW1(config-if)# switchport port-security violation protect
SW1(config-if)# switchport port-security aging time 60
SW1(config-if)# switchport port-security aging type inactivity
```

**Result:** 2 MACs max, silent drops, MACs age out after 60 min inactivity

### Example 5: Multiple Static MACs

```
SW1(config)# interface gi0/5
SW1(config-if)# switchport mode access
SW1(config-if)# switchport port-security
SW1(config-if)# switchport port-security maximum 3
SW1(config-if)# switchport port-security mac-address 1111.2222.3333
SW1(config-if)# switchport port-security mac-address 4444.5555.6666
SW1(config-if)# switchport port-security mac-address 7777.8888.9999
```

**Result:** Exactly 3 specific MACs allowed

---

## Verification Commands

### Show Port Security Status on Interface

```
SW1# show port-security interface gi0/1
```

**Output shows:**

- Port status (secure-up, secure-down, secure-shutdown)
- Violation mode
- Maximum MAC addresses
- Current MAC address count
- Security violation count
- Last source MAC that violated

### Show Port Security for All Interfaces

```
SW1# show port-security
```

**Output shows:**

- Secure ports count
- Max allowed count
- Table of all ports with port security

### Show Learned MAC Addresses

```
SW1# show port-security address
```

**Shows all secure MAC addresses and their type (dynamic/static/sticky)**

### Show MAC Address Table

```
SW1# show mac address-table
```

**Verify which MACs are learned on which ports**

### Check for Err-Disabled Ports

```
SW1# show interfaces status err-disabled
```

**Shows ports in err-disabled state and the reason**

---

## Troubleshooting Port Security

### Common Issues

**Issue 1: Port immediately goes to err-disabled**

- **Cause:** Unauthorized device connected or wrong MAC
- **Fix:** Check violation counter, verify correct device connected

```
SW1# show port-security interface gi0/1
```

**Issue 2: Can't enable port security**

```
Error: cannot enable port security on dynamic port
```

- **Cause:** Port not set to access or trunk mode
- **Fix:** Configure port as access first

```
SW1(config-if)# switchport mode access
```

**Issue 3: Sticky MACs not saved after reload**

- **Cause:** Didn't save running-config
- **Fix:** Save configuration

```
SW1# copy running-config startup-config
```

**Issue 4: Port security enabled but not working**

- **Cause:** Maximum set to very high number or wrong violation mode
- **Fix:** Verify settings

```
SW1# show port-security interface gi0/1
```

### Recovery from Err-Disabled

**Manual recovery:**

```
SW1(config)# interface gi0/1
SW1(config-if)# shutdown
SW1(config-if)# no shutdown
```

**Automatic recovery (globally):**

```
SW1(config)# errdisable recovery cause psecure-violation
SW1(config)# errdisable recovery interval 300
```

**Check auto-recovery status:**

```
SW1# show errdisable recovery
```

---

## Configuration Removal

### Disable Port Security on Interface

```
SW1(config-if)# no switchport port-security
```

**Effect:** All dynamic and sticky MACs removed, static MACs remain in config

### Remove Specific Static MAC

```
SW1(config-if)# no switchport port-security mac-address 1111.2222.3333
```

### Reset to Default Maximum

```
SW1(config-if)# no switchport port-security maximum
```

**Result:** Maximum returns to 1**

### Reset to Default Violation Mode

```
SW1(config-if)# no switchport port-security violation
```

**Result:** Returns to shutdown mode**

---

## Quick Command Reference

### Essential Configuration Commands

```
switchport mode access                              # Configure as access port (required)
switchport port-security                            # Enable port security
switchport port-security maximum <1-8192>          # Set max MACs (default: 1)
switchport port-security mac-address <MAC>         # Add static MAC
switchport port-security mac-address sticky        # Enable sticky learning
switchport port-security violation {shutdown|restrict|protect}  # Set violation mode
switchport port-security aging time <minutes>      # Set aging time
switchport port-security aging type {absolute|inactivity}  # Set aging type
switchport port-security aging static              # Apply aging to static MACs
```

### Essential Verification Commands

```
show port-security                                 # Overview of all secure ports
show port-security interface <interface>           # Detailed info for one port
show port-security address                         # Show all secure MAC addresses
show mac address-table interface <interface>       # Show MACs on interface
show interfaces status err-disabled                # Show err-disabled ports
show errdisable recovery                           # Show auto-recovery settings
```

### Recovery Commands

```
interface <interface>
shutdown
no shutdown                                        # Manual recovery from err-disabled

errdisable recovery cause psecure-violation        # Enable auto-recovery
errdisable recovery interval <seconds>             # Set auto-recovery timer
```

---

## CCNA Exam Tips

✅ **Port security only works on access or trunk ports** - not dynamic ✅ **Default violation mode is shutdown** - port goes to err-disabled ✅ **Default maximum is 1 MAC address** ✅ **Sticky MACs are saved in running-config** - must copy to startup ✅ **Dynamic MACs are lost on reload** - not saved anywhere ✅ **Static MACs persist across reboots** - in startup-config ✅ **Shutdown mode requires manual recovery** (or auto-recovery configured) ✅ **Restrict and Protect keep port up** - only drop bad frames ✅ **Protect mode is silent** - no syslog or SNMP ✅ Know the **three violation modes and their differences** ✅ Understand **when to use each MAC type** (static/dynamic/sticky) ✅ Remember **err-disabled recovery commands**

---

## Common Exam Scenarios

**Scenario 1:** "Configure port to allow only one specific device"

- Static MAC address with shutdown violation

**Scenario 2:** "Configure port for IP phone and PC"

- Maximum 2-3, sticky MACs recommended

**Scenario 3:** "Port security enabled but device can't connect"

- Check if port is access mode, check MAC count, check violation counter

**Scenario 4:** "Port keeps going to err-disabled"

- Check learned MACs, verify correct devices connected, check maximum

**Scenario 5:** "Security needed but can't disrupt service"

- Use restrict or protect violation mode instead of shutdown
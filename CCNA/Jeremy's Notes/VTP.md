
# VTP (VLAN Trunking Protocol) - CCNA Cheat Sheet

## What is VTP?

**VTP (VLAN Trunking Protocol)** - Cisco proprietary protocol that propagates VLAN configuration changes across trunk links to reduce administrative overhead.

### Key Concepts:

- **VTP Domain** - Group of switches sharing VLAN information (must match)
- **VTP Modes** - Server, Client, Transparent, Off
- **Revision Number** - Tracks configuration changes (higher number = newer config)
- **VTP Pruning** - Reduces unnecessary traffic by blocking VLANs on trunks where they're not needed

---

## VTP Modes

|Mode|Can Create VLANs?|Can Modify VLANs?|Can Delete VLANs?|Forwards VTP Ads?|Stored in vlan.dat?|
|---|---|---|---|---|---|
|**Server**|✅ Yes|✅ Yes|✅ Yes|✅ Yes|✅ Yes|
|**Client**|❌ No|❌ No|❌ No|✅ Yes|❌ No|
|**Transparent**|✅ Yes (local only)|✅ Yes (local only)|✅ Yes (local only)|✅ Yes (forwards only)|✅ Yes|
|**Off**|✅ Yes (local only)|✅ Yes (local only)|✅ Yes (local only)|❌ No|✅ Yes|

### Mode Descriptions:

**Server Mode (Default):**

- Can create/modify/delete VLANs
- Sends VTP advertisements
- Synchronizes VLAN database with other switches
- **DANGER:** Higher revision number overwrites all switches!

**Client Mode:**

- Cannot create/modify/delete VLANs locally
- Receives and applies VTP advertisements
- Synchronizes with VTP server
- Use for edge/access switches

**Transparent Mode:**

- Creates/modifies/deletes VLANs **locally only**
- Forwards VTP advertisements but doesn't participate
- Does NOT synchronize VLAN database
- **SAFE:** Won't be overwritten by other switches

**Off Mode (VTPv3 only):**

- Like Transparent but doesn't forward VTP advertisements
- Completely disables VTP

---

## Essential VTP Commands

### View VTP Status:

```
Switch# show vtp status
```

### Set VTP Domain:

```
Switch(config)# vtp domain COMPANY
```

### Set VTP Mode:

```
Switch(config)# vtp mode server
Switch(config)# vtp mode client
Switch(config)# vtp mode transparent
Switch(config)# vtp mode off                    (VTPv3 only)
```

### Set VTP Password (Optional):

```
Switch(config)# vtp password MySecretPass
```

### Set VTP Version:

```
Switch(config)# vtp version 2
Switch(config)# vtp version 3                   (Recommended if supported)
```

### Enable VTP Pruning (Server Mode Only):

```
Switch(config)# vtp pruning
```

### Reset VTP Revision Number (IMPORTANT!):

```
Switch(config)# vtp mode transparent
Switch(config)# vtp mode server                 (Resets revision to 0)
```

---

## Show Commands

### View VTP Status:

```
Switch# show vtp status

VTP Version capable             : 1 to 3
VTP version running             : 2
VTP Domain Name                 : COMPANY
VTP Pruning Mode                : Disabled
VTP Traps Generation            : Disabled
Device ID                       : 0cd9.96d2.3f00
Configuration last modified by  192.168.1.1 at 3-1-25 12:34:56
Local updater ID is             192.168.1.1 on interface Vl1 (lowest numbered VLAN interface)

Feature VLAN:
--------------
VTP Operating Mode              : Server
Maximum VLANs supported locally : 1005
Number of existing VLANs        : 8
Configuration Revision          : 12        ← CRITICAL NUMBER!
MD5 digest                      : 0x3F 0x23...
```

### View VTP Password:

```
Switch# show vtp password

VTP Password: MySecretPass
```

### View VTP Counters:

```
Switch# show vtp counters
```

---

## VTP Configuration Examples

### Example 1: Basic VTP Server Setup

```
Switch1(config)# vtp domain COMPANY
Switch1(config)# vtp mode server
Switch1(config)# vtp version 2
Switch1(config)# vtp password Cisco123
Switch1(config)# vtp pruning
Switch1(config)# exit

Switch1# show vtp status
```

### Example 2: VTP Client Setup

```
Switch2(config)# vtp domain COMPANY
Switch2(config)# vtp mode client
Switch2(config)# vtp password Cisco123
Switch2(config)# exit

Switch2# show vtp status
```

### Example 3: VTP Transparent (Recommended for Most Scenarios)

```
Switch3(config)# vtp mode transparent
Switch3(config)# vtp domain COMPANY            (Optional in transparent)
Switch3(config)# exit

Switch3# show vtp status
```

---

## VTP Requirements for Synchronization

For VTP to work, **ALL of these must match:**

✅ **VTP Domain Name** - Must be identical (case-sensitive!) ✅ **VTP Password** - Must match if configured ✅ **Trunk Links** - VTP advertisements only sent over trunks ✅ **VTP Version** - Should match (v1, v2, or v3)

If any don't match, VTP will **NOT synchronize**.

---

## VTP Pruning

**VTP Pruning** - Prevents unnecessary VLAN traffic from being sent over trunk links where the VLAN doesn't exist.

### Enable Pruning (Server Mode Only):

```
Switch(config)# vtp pruning
```

### View Pruning Status:

```
Switch# show interfaces trunk

Port      Vlans in spanning tree forwarding state and not pruned
Gi0/1     1,10,20         ← Only VLANs 10 and 20 active, others pruned
```

### Manual Pruning Override (Per Interface):

```
Switch(config)# interface gi0/1
Switch(config-if)# switchport trunk pruning vlan remove 30
```

---

## VTP Versions Comparison

|Feature|VTPv1|VTPv2|VTPv3|
|---|---|---|---|
|**VLAN Range**|1-1005|1-1005|1-4094 (extended)|
|**Transparent Forwarding**|Limited|Better|Best|
|**Token Ring Support**|Yes|Yes|No|
|**Primary Server**|No|No|Yes (prevents accidents)|
|**Off Mode**|No|No|Yes|
|**Propagate Extended VLANs**|No|No|Yes|

**Recommendation:** Use **VTPv3** if all switches support it. Otherwise use **VTPv2**.

---

## VTP Revision Number (CRITICAL!)

**Revision Number** - Increments every time a VLAN change is made on a VTP server.

### The DANGER:

If you add a switch with a **higher revision number**, it will **overwrite all VLANs** on other switches!

### Example Disaster Scenario:

```
1. Production network has VTP revision 10
2. You connect old lab switch with revision 50
3. Lab switch overwrites production VLAN database
4. ALL VLANs DELETED from production! 💥
```

### How to Prevent This:

**ALWAYS reset revision number before adding a switch to network:**

```
Switch(config)# vtp mode transparent
Switch(config)# exit
Switch# show vtp status                    (Verify revision = 0 or low number)

Switch(config)# vtp mode server            (Optional: switch back to desired mode)
```

**OR** delete vlan.dat file:

```
Switch# delete flash:vlan.dat
Switch# reload
```

---

## VTP Advertisements

VTP sends three types of advertisements:

1. **Summary Advertisements** - Every 300 seconds (5 minutes) or after VLAN change
2. **Subset Advertisements** - Contains actual VLAN information (after changes)
3. **Advertisement Requests** - Client requests full VLAN database

---

## VTP Troubleshooting

### Check VTP Status:

```
Switch# show vtp status
```

**Look for:**

- VTP Operating Mode
- VTP Domain Name
- Configuration Revision
- VTP Version

### Check VTP Counters:

```
Switch# show vtp counters
```

Shows statistics on VTP advertisements sent/received.

### Common Issues:

**Issue 1: VLANs Not Synchronizing**

- ❌ Domain names don't match (case-sensitive!)
- ❌ Passwords don't match
- ❌ No trunk links configured
- ❌ VTP versions incompatible

**Issue 2: VLANs Disappeared**

- ❌ Higher revision number switch added to network
- ❌ Someone deleted VLANs on VTP server

**Issue 3: Can't Create VLANs**

- ❌ Switch is in Client mode (change to Server or Transparent)

---

## Best Practices (CCNA Exam Important!)

### ✅ DO:

- Use **Transparent mode** for most switches (safest)
- Use **Client mode** for access layer switches if using VTP
- Use **VTP password** for security
- **Reset revision number** before adding switches to network
- Document VTP domain and password
- Use **VTP pruning** to optimize bandwidth

### ❌ DON'T:

- Use VTP in production without understanding risks
- Add unknown switches without checking revision number
- Use default VTP domain name
- Forget to configure trunks (VTP requires trunks)
- Mix VTP versions without testing

---

## CCNA Exam Tips

### Know These Cold:

1. **Default VTP mode** = Server
2. **VTP requires trunk links** to propagate
3. **Client mode cannot create VLANs**
4. **Transparent mode** = local VLANs only, forwards VTP ads
5. **Higher revision number wins** (overwrites lower)
6. **VTP domain names are case-sensitive**
7. **VTP password must match** for synchronization
8. **VTPv3 supports extended VLANs** (1006-4094)
9. **VTP pruning** optimizes trunk bandwidth
10. **Reset revision = change to transparent, then back**

### Common Exam Questions:

- "Switch can't create VLANs" → Check if in Client mode
- "VLANs disappeared across network" → Higher revision number
- "VTP not synchronizing" → Check domain/password/trunks
- "Reduce unnecessary VLAN traffic" → Enable VTP pruning

---

## Quick Configuration Summary

### Safe Configuration (Transparent Mode - Recommended):

```
Switch(config)# vtp mode transparent
Switch(config)# vtp domain COMPANY
```

### VTP Server Configuration:

```
Switch(config)# vtp domain COMPANY
Switch(config)# vtp mode server
Switch(config)# vtp version 2
Switch(config)# vtp password SecurePass
Switch(config)# vtp pruning
```

### VTP Client Configuration:

```
Switch(config)# vtp domain COMPANY
Switch(config)# vtp mode client
Switch(config)# vtp password SecurePass
```

### Disable VTP (Safest for Exams):

```
Switch(config)# vtp mode transparent
```

Or (VTPv3):

```
Switch(config)# vtp mode off
```

---

## Verification Checklist

```
Switch# show vtp status              ← Mode, domain, revision, version
Switch# show vtp password            ← Verify password
Switch# show vlan brief              ← Verify VLANs present
Switch# show interfaces trunk        ← Verify trunks (VTP requires trunks!)
Switch# show vtp counters            ← Check advertisements sent/received
```

---

## Reality Check

**In Real Networks:**

- Many engineers **disable VTP** (use Transparent or Off mode)
- Risk of accidental VLAN deletion is too high
- Modern network automation tools replace VTP's purpose
- Exam tests VTP heavily, but real-world use is declining

**For CCNA Exam:**

- Know VTP thoroughly (it's tested!)
- Understand modes, revision numbers, requirements
- Practice troubleshooting VTP scenarios

---

**Bottom Line:** VTP can simplify VLAN management BUT has serious risks. Know it for the exam, but strongly consider using **Transparent mode** in production! 🎯
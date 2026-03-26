______________

# CCNA Daily Router Practice Lab

## Lab Purpose

This is your **go-to practice lab** for building muscle memory with Cisco IOS commands. Configure this topology from scratch daily until you can complete it in under 20 minutes without notes.

---

## Topology Overview

```
[PC1] ---- [SW1] ---- [R1] ====== [R2] ---- [SW2] ---- [PC2]
 .10        Fa0/1     G0/0  S0/0/0  S0/0/0   G0/0      Fa0/1    .10
            Fa0/24           Serial Link             Fa0/24

            [PC3]                              [PC4]
             .20                                .20
             |                                  |
            Fa0/2                              Fa0/2
```

### Network Design

- **LAN 1** (Left side): 192.168.10.0/24
- **LAN 2** (Right side): 192.168.20.0/24
- **Serial Link**: 10.0.0.0/30 (only 2 usable IPs needed)

---

## Device List

### Routers

- **R1**: Router 2911 (or 1941)
- **R2**: Router 2911 (or 1941)

### Switches

- **SW1**: Switch 2960
- **SW2**: Switch 2960

### End Devices

- **PC1**: End device (192.168.10.10)
- **PC2**: End device (192.168.20.10)
- **PC3**: End device (192.168.10.20)
- **PC4**: End device (192.168.20.20)

---

## IP Addressing Table

|Device|Interface|IP Address|Subnet Mask|Default Gateway|
|---|---|---|---|---|
|R1|G0/0|192.168.10.1|255.255.255.0|N/A|
|R1|S0/0/0 (DCE)|10.0.0.1|255.255.255.252|N/A|
|R1|Loopback0|1.1.1.1|255.255.255.0|N/A|
|R2|G0/0|192.168.20.1|255.255.255.0|N/A|
|R2|S0/0/0|10.0.0.2|255.255.255.252|N/A|
|R2|Loopback0|2.2.2.1|255.255.255.0|N/A|
|PC1|NIC|192.168.10.10|255.255.255.0|192.168.10.1|
|PC2|NIC|192.168.20.10|255.255.255.0|192.168.20.1|
|PC3|NIC|192.168.10.20|255.255.255.0|192.168.10.1|
|PC4|NIC|192.168.20.20|255.255.255.0|192.168.20.1|

---

## Part 1: Build the Topology (5 minutes)

### Step 1: Add Devices

1. Open Packet Tracer
    
2. Add from bottom menu:
    
    - **2x Routers** (2911 or 1941)
    - **2x Switches** (2960)
    - **4x PCs**
3. **Label devices**:
    
    - Click each device → Display tab → Change name

### Step 2: Cable the Network

**Left Side (LAN 1):**

- PC1 FastEthernet → SW1 Fa0/1
- PC3 FastEthernet → SW1 Fa0/2
- SW1 Fa0/24 → R1 GigabitEthernet0/0

**Serial Link (WAN):**

- R1 Serial0/0/0 → R2 Serial0/0/0 (use Serial DCE cable)
- **IMPORTANT**: R1 side must be the DCE end (clock source)

**Right Side (LAN 2):**

- R2 GigabitEthernet0/0 → SW2 Fa0/24
- SW2 Fa0/1 → PC2 FastEthernet
- SW2 Fa0/2 → PC4 FastEthernet

### Step 3: Set Clock Rate (CRITICAL!)

Serial links require clock rate on the DCE side.

**On R1 (DCE side):**

```
R1> enable
R1# configure terminal
R1(config)# interface Serial0/0/0
R1(config-if)# clock rate 64000
R1(config-if)# exit
```

**How to identify DCE side in Packet Tracer:**

- Click on the cable between routers
- Look for the **clock symbol** - that's the DCE end

### Step 4: Wait for Links

Wait 30-60 seconds for all link lights to turn green.

---

## Part 2: Configure R1 (Practice Time: 5 minutes)

### Basic Configuration

```
Router> enable
Router# configure terminal
Router(config)# hostname R1
R1(config)# no ip domain-lookup
R1(config)# enable secret cisco123
R1(config)# banner motd #Unauthorized Access Prohibited#
```

### Console Line Security

```
R1(config)# line console 0
R1(config-line)# password cisco
R1(config-line)# login
R1(config-line)# logging synchronous
R1(config-line)# exec-timeout 0 0
R1(config-line)# exit
```

### VTY Line Security (Telnet/SSH)

```
R1(config)# line vty 0 15
R1(config-line)# password cisco
R1(config-line)# login
R1(config-line)# exit
```

### Configure GigabitEthernet0/0

```
R1(config)# interface GigabitEthernet0/0
R1(config-if)# description LAN_Connection_to_SW1
R1(config-if)# ip address 192.168.10.1 255.255.255.0
R1(config-if)# no shutdown
R1(config-if)# exit
```

### Configure Serial0/0/0 (DCE side)

```
R1(config)# interface Serial0/0/0
R1(config-if)# description WAN_Link_to_R2
R1(config-if)# ip address 10.0.0.1 255.255.255.252
R1(config-if)# clock rate 64000
R1(config-if)# no shutdown
R1(config-if)# exit
```

### Configure Loopback0

```
R1(config)# interface Loopback0
R1(config-if)# description Loopback_for_Testing
R1(config-if)# ip address 1.1.1.1 255.255.255.0
R1(config-if)# exit
```

### Configure Static Route to R2's LAN

```
R1(config)# ip route 192.168.20.0 255.255.255.0 10.0.0.2
R1(config)# exit
```

### Save Configuration

```
R1# copy running-config startup-config
```

Or just: `R1# write` or `R1# wr`

### Verify R1 Configuration

```
R1# show ip interface brief
R1# show running-config
R1# show ip route
```

---

## Part 3: Configure R2 (Practice Time: 5 minutes)

### Basic Configuration

```
Router> enable
Router# configure terminal
Router(config)# hostname R2
R2(config)# no ip domain-lookup
R2(config)# enable secret cisco123
R2(config)# banner motd #Unauthorized Access Prohibited#
```

### Console Line Security

```
R2(config)# line console 0
R2(config-line)# password cisco
R2(config-line)# login
R2(config-line)# logging synchronous
R2(config-line)# exec-timeout 0 0
R2(config-line)# exit
```

### VTY Line Security

```
R2(config)# line vty 0 15
R2(config-line)# password cisco
R2(config-line)# login
R2(config-line)# exit
```

### Configure GigabitEthernet0/0

```
R2(config)# interface GigabitEthernet0/0
R2(config-if)# description LAN_Connection_to_SW2
R2(config-if)# ip address 192.168.20.1 255.255.255.0
R2(config-if)# no shutdown
R2(config-if)# exit
```

### Configure Serial0/0/0 (DTE side - NO clock rate needed)

```
R2(config)# interface Serial0/0/0
R2(config-if)# description WAN_Link_to_R1
R2(config-if)# ip address 10.0.0.2 255.255.255.252
R2(config-if)# no shutdown
R2(config-if)# exit
```

### Configure Loopback0

```
R2(config)# interface Loopback0
R2(config-if)# description Loopback_for_Testing
R2(config-if)# ip address 2.2.2.1 255.255.255.0
R2(config-if)# exit
```

### Configure Static Route to R1's LAN

```
R2(config)# ip route 192.168.10.0 255.255.255.0 10.0.0.1
R2(config)# exit
```

### Save Configuration

```
R2# copy running-config startup-config
```

### Verify R2 Configuration

```
R2# show ip interface brief
R2# show running-config
R2# show ip route
```

---

## Part 4: Configure Switches (Practice Time: 3 minutes)

### Configure SW1

```
Switch> enable
Switch# configure terminal
Switch(config)# hostname SW1
SW1(config)# enable secret cisco123
SW1(config)# line console 0
SW1(config-line)# password cisco
SW1(config-line)# login
SW1(config-line)# logging synchronous
SW1(config-line)# exit
SW1(config)# exit
SW1# write
```

### Configure SW2 (Same as SW1)

```
Switch> enable
Switch# configure terminal
Switch(config)# hostname SW2
SW2(config)# enable secret cisco123
SW2(config)# line console 0
SW2(config-line)# password cisco
SW2(config-line)# login
SW2(config-line)# logging synchronous
SW2(config-line)# exit
SW2(config)# exit
SW2# write
```


### Learn Mac Address

- show mac address-table
- clear mac address-table dynamic
- clear mac address-table dynamic interface <int id>
---

## Part 5: Configure PCs (Practice Time: 2 minutes)

### PC1 Configuration

1. Click **PC1** → **Desktop** → **IP Configuration**
2. Set:
    - IP Address: `192.168.10.10`
    - Subnet Mask: `255.255.255.0`
    - Default Gateway: `192.168.10.1`

### PC2 Configuration

1. Click **PC2** → **Desktop** → **IP Configuration**
2. Set:
    - IP Address: `192.168.20.10`
    - Subnet Mask: `255.255.255.0`
    - Default Gateway: `192.168.20.1`

### PC3 Configuration

1. Click **PC3** → **Desktop** → **IP Configuration**
2. Set:
    - IP Address: `192.168.10.20`
    - Subnet Mask: `255.255.255.0`
    - Default Gateway: `192.168.10.1`

### PC4 Configuration

1. Click **PC4** → **Desktop** → **IP Configuration**
2. Set:
    - IP Address: `192.168.20.20`
    - Subnet Mask: `255.255.255.0`
    - Default Gateway: `192.168.20.1`

---

## Part 6: Test Connectivity (Practice Time: 3 minutes)

### From PC1 Command Prompt

**Test 1: Ping own gateway**

```
ping 192.168.10.1
```

✅ Should work (4 replies)

**Test 2: Ping across serial link to R2**

```
ping 10.0.0.2
```

✅ Should work

**Test 3: Ping remote network gateway**

```
ping 192.168.20.1
```

✅ Should work

**Test 4: Ping PC2 on remote network**

```
ping 192.168.20.10
```

✅ Should work

**Test 5: Ping R2's Loopback**

```
ping 2.2.2.1
```

✅ Should work

**Test 6: Traceroute to PC2**

```
tracert 192.168.20.10
```

✅ Should show: PC1 → R1 (192.168.10.1) → R2 (10.0.0.2) → PC2

### From R1 CLI

**Ping R2's Serial interface**

```
R1# ping 10.0.0.2
```

✅ Should get 5 replies (!!!!!!)

**Ping R2's LAN interface**

```
R1# ping 192.168.20.1
```

✅ Should work

**Ping PC2**

```
R1# ping 192.168.20.10
```

✅ Should work

**Check routing table**

```
R1# show ip route
```

Look for:

- C = Connected routes (your directly connected networks)
- S = Static routes (the route you configured)

---

## Troubleshooting Commands

If pings fail, use these commands in order:

### On Routers

```
show ip interface brief        # Are interfaces up/up?
show running-config           # Is IP addressing correct?
show ip route                 # Do routes exist?
show interfaces <interface>   # Detailed interface info
ping <ip>                     # Test connectivity
```

### On PCs

```
ipconfig                      # Check IP configuration
ping <gateway>                # Can you reach your gateway?
tracert <destination>         # Where does the path break?
```

### Common Issues and Solutions

|Problem|Likely Cause|Solution|
|---|---|---|
|Serial link down/down|No clock rate on DCE|Add `clock rate 64000` on R1's S0/0/0|
|Interface administratively down|Forgot `no shutdown`|Use `no shutdown` command|
|Can ping gateway but not remote|Missing static route|Add static route on router|
|Can ping R2 but not PC2|PC gateway wrong|Check PC's default gateway setting|
|All pings fail|Wrong IP addressing|Verify IPs match the table|

---

## Practice Variations (For Advanced Practice)

Once you can configure the basic lab quickly, try these variations:

### Variation 1: Add VLANs

- Create VLAN 10 (Sales) and VLAN 20 (IT) on SW1
- Put PC1 in VLAN 10, PC3 in VLAN 20
- Configure Router-on-a-Stick on R1 to route between VLANs

### Variation 2: Add DHCP

- Configure R1 as DHCP server for 192.168.10.0/24
- Configure R2 as DHCP server for 192.168.20.0/24
- Set PCs to DHCP

### Variation 3: Add Access Lists (ACLs)

- Create ACL to block PC1 from reaching PC2
- Create ACL to allow only Telnet traffic from 192.168.10.0/24
- Create ACL to block ping but allow all other traffic

### Variation 4: Add Dynamic Routing

- Remove static routes
- Configure OSPF on both routers
- Verify with `show ip ospf neighbor` and `show ip route`

### Variation 5: Add NAT

- Configure R2 to do PAT (NAT overload)
- Inside: 192.168.20.0/24
- Outside: Serial0/0/0

### Variation 6: Supporting SSH Access

- R1(config)# hostname R1
- R1(config)# ip domain-name lab.local
- R1(config)# crypto key generate rsa
- R1(config)# username admin secret StrongPass!
- R1(config)# line vty 0 15
- R1(config-line)# login local
- R1(config-line)# transport input ssh


---

## Daily Practice Routine

### Week 1: Basic Configuration (20 minutes daily)

- Day 1-3: Configure routers only (no notes)
- Day 4-5: Configure entire topology (with notes)
- Day 6-7: Configure entire topology (no notes, time yourself)

### Week 2: Speed Building (15 minutes daily)

- Configure entire lab from memory
- Goal: Complete in under 20 minutes
- Focus on eliminating mistakes

### Week 3: Troubleshooting (20 minutes daily)

- Configure the lab with intentional errors
- Practice using show commands to find issues
- Examples: wrong IP, forgot no shutdown, missing route

### Week 4: Variations (25 minutes daily)

- Add VLANs (Monday/Tuesday)
- Add DHCP (Wednesday/Thursday)
- Add ACLs (Friday)
- Review all (Weekend)

---

## Command Checklist (For Speed)

Print this out and check off as you go:

### R1 Configuration

- [ ] `hostname R1`
- [ ] `enable secret cisco123`
- [ ] `line console 0` → password, login, logging sync
- [ ] `line vty 0 15` → password, login
- [ ] `interface G0/0` → IP, description, no shut
- [ ] `interface S0/0/0` → IP, description, clock rate, no shut
- [ ] `interface Loopback0` → IP, description
- [ ] `ip route 192.168.20.0 255.255.255.0 10.0.0.2`
- [ ] `copy run start`

### R2 Configuration

- [ ] `hostname R2`
- [ ] `enable secret cisco123`
- [ ] `line console 0` → password, login, logging sync
- [ ] `line vty 0 15` → password, login
- [ ] `interface G0/0` → IP, description, no shut
- [ ] `interface S0/0/0` → IP, description, no shut (NO clock rate)
- [ ] `interface Loopback0` → IP, description
- [ ] `ip route 192.168.10.0 255.255.255.0 10.0.0.1`
- [ ] `copy run start`

### Verification

- [ ] All interfaces show up/up
- [ ] PC1 can ping PC2
- [ ] Routing tables show static routes
- [ ] Can telnet between routers

---

## Save Your Lab Template

**File** → **Save As** → `CCNA_Daily_Practice_Lab.pkt`

### Pro Tips:

1. **Don't save configurations** - Practice from scratch each time
2. **Time yourself** - Track your improvement
3. **Use abbreviations** - But know full commands for exam
4. **Verify as you go** - Don't wait until the end
5. **Make mistakes** - Then practice troubleshooting them

---

## Expected Timeline

- **First time**: 45-60 minutes (with notes)
- **After 1 week**: 25-30 minutes (with notes)
- **After 2 weeks**: 15-20 minutes (no notes)
- **After 3 weeks**: 12-15 minutes (no notes)
- **Exam ready**: Under 15 minutes, zero errors

---

## Why This Lab is Perfect for CCNA

✅ **Covers core skills**: Interface config, routing, troubleshooting  
✅ **Realistic topology**: Similar to real networks  
✅ **Scalable**: Easy to add features as you learn  
✅ **Quick to reset**: Just reload routers  
✅ **Tests everything**: IP addressing, routing, connectivity  
✅ **Builds confidence**: Repetition creates muscle memory

**Remember**: The CCNA exam simulations test your ability to configure routers quickly and correctly under pressure. This lab builds exactly that skill!

Good luck with your practice! 🎯
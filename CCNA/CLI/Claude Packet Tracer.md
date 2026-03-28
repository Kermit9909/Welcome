
# Packet Tracer Lab: VLAN Configuration and Inter-VLAN Routing

## Lab Objective

Configure VLANs on a switch, assign ports to VLANs, and enable inter-VLAN routing using Router-on-a-Stick (ROAS).

---

## Lab Topology

```
[PC1] ---- [SW1] ---- [R1] ---- [PC4]
[PC2] ----/     \
[PC3] ----------/
```

### Device List:

- **R1**: Router (1941 or 2911)
- **SW1**: Switch (2960)
- **PC1**: VLAN 10 (Sales)
- **PC2**: VLAN 20 (HR)
- **PC3**: VLAN 30 (IT)
- **PC4**: Outside network

---

## IP Addressing Table

|Device|Interface|IP Address|Subnet Mask|VLAN|Gateway|
|---|---|---|---|---|---|
|R1|G0/0.10|192.168.10.1|255.255.255.0|10|N/A|
|R1|G0/0.20|192.168.20.1|255.255.255.0|20|N/A|
|R1|G0/0.30|192.168.30.1|255.255.255.0|30|N/A|
|R1|G0/1|10.0.0.1|255.255.255.0|N/A|N/A|
|PC1|NIC|192.168.10.10|255.255.255.0|10|192.168.10.1|
|PC2|NIC|192.168.20.10|255.255.255.0|20|192.168.20.1|
|PC3|NIC|192.168.30.10|255.255.255.0|30|192.168.30.1|
|PC4|NIC|10.0.0.10|255.255.255.0|N/A|10.0.0.1|

---

## Part 1: Build the Topology in Packet Tracer

### Step 1: Add Devices

1. Open Packet Tracer
2. Add devices from the bottom menu:
    - 1x Router (1941 or 2911)
    - 1x Switch (2960)
    - 4x PCs

### Step 2: Cable the Network

1. **PC1 to SW1**: Connect PC1 FastEthernet to SW1 Fa0/1
2. **PC2 to SW1**: Connect PC2 FastEthernet to SW1 Fa0/2
3. **PC3 to SW1**: Connect PC3 FastEthernet to SW1 Fa0/3
4. **SW1 to R1**: Connect SW1 Fa0/24 to R1 G0/0 (this will be the trunk)
5. **R1 to PC4**: Connect R1 G0/1 to PC4 FastEthernet

### Step 3: Wait for Links

- Wait for all link lights to turn **green** (may take 30-60 seconds)

---

## Part 2: Configure the Switch (SW1)

### Step 2.1: Basic Configuration

Click on **SW1** → **CLI** tab

```
Switch> enable
Switch# configure terminal
Switch(config)# hostname SW1
SW1(config)# no ip domain-lookup
SW1(config)# enable secret cisco
SW1(config)# line console 0
SW1(config-line)# password cisco
SW1(config-line)# login
SW1(config-line)# exit
SW1(config)# line vty 0 15
SW1(config-line)# password cisco
SW1(config-line)# login
SW1(config-line)# exit
SW1(config)# banner motd #Unauthorized Access Prohibited#
```

### Step 2.2: Create VLANs

```
SW1(config)# vlan 10
SW1(config-vlan)# name Sales
SW1(config-vlan)# exit

SW1(config)# vlan 20
SW1(config-vlan)# name HR
SW1(config-vlan)# exit

SW1(config)# vlan 30
SW1(config-vlan)# name IT
SW1(config-vlan)# exit
```

### Step 2.3: Assign Ports to VLANs

```
SW1(config)# interface fastEthernet 0/1
SW1(config-if)# switchport mode access
SW1(config-if)# switchport access vlan 10
SW1(config-if)# exit

SW1(config)# interface fastEthernet 0/2
SW1(config-if)# switchport mode access
SW1(config-if)# switchport access vlan 20
SW1(config-if)# exit

SW1(config)# interface fastEthernet 0/3
SW1(config-if)# switchport mode access
SW1(config-if)# switchport access vlan 30
SW1(config-if)# exit
```

### Step 2.4: Configure Trunk Port

```
SW1(config)# interface fastEthernet 0/24
SW1(config-if)# switchport mode trunk
SW1(config-if)# exit
SW1(config)# exit
SW1# write memory
```

### Step 2.5: Verify VLAN Configuration

```
SW1# show vlan brief
SW1# show interfaces trunk
```

---

## Part 3: Configure the Router (R1)

### Step 3.1: Basic Configuration

Click on **R1** → **CLI** tab

```
Router> enable
Router# configure terminal
Router(config)# hostname R1
R1(config)# no ip domain-lookup
R1(config)# enable secret cisco
R1(config)# line console 0
R1(config-line)# password cisco
R1(config-line)# login
R1(config-line)# exit
R1(config)# line vty 0 4
R1(config-line)# password cisco
R1(config-line)# login
R1(config-line)# exit
```

### Step 3.2: Configure Router-on-a-Stick (Subinterfaces)

```
R1(config)# interface gigabitEthernet 0/0
R1(config-if)# no shutdown
R1(config-if)# exit

R1(config)# interface gigabitEthernet 0/0.10
R1(config-subif)# encapsulation dot1Q 10
R1(config-subif)# ip address 192.168.10.1 255.255.255.0
R1(config-subif)# exit

R1(config)# interface gigabitEthernet 0/0.20
R1(config-subif)# encapsulation dot1Q 20
R1(config-subif)# ip address 192.168.20.1 255.255.255.0
R1(config-subif)# exit

R1(config)# interface gigabitEthernet 0/0.30
R1(config-subif)# encapsulation dot1Q 30
R1(config-subif)# ip address 192.168.30.1 255.255.255.0
R1(config-subif)# exit
```

### Step 3.3: Configure Outside Interface

```
R1(config)# interface gigabitEthernet 0/1
R1(config-if)# ip address 10.0.0.1 255.255.255.0
R1(config-if)# no shutdown
R1(config-if)# exit
R1(config)# exit
R1# write memory
```

### Step 3.4: Verify Router Configuration

```
R1# show ip interface brief
R1# show ip route
```

---

## Part 4: Configure PCs

### PC1 Configuration:

1. Click **PC1** → **Desktop** → **IP Configuration**
2. Set:
    - IP Address: `192.168.10.10`
    - Subnet Mask: `255.255.255.0`
    - Default Gateway: `192.168.10.1`

### PC2 Configuration:

1. Click **PC2** → **Desktop** → **IP Configuration**
2. Set:
    - IP Address: `192.168.20.10`
    - Subnet Mask: `255.255.255.0`
    - Default Gateway: `192.168.20.1`

### PC3 Configuration:

1. Click **PC3** → **Desktop** → **IP Configuration**
2. Set:
    - IP Address: `192.168.30.10`
    - Subnet Mask: `255.255.255.0`
    - Default Gateway: `192.168.30.1`

### PC4 Configuration:

1. Click **PC4** → **Desktop** → **IP Configuration**
2. Set:
    - IP Address: `10.0.0.10`
    - Subnet Mask: `255.255.255.0`
    - Default Gateway: `10.0.0.1`

---

## Part 5: Test Connectivity

### Test 1: Same VLAN Communication (Should FAIL)

From **PC1** Command Prompt:

```
ping 192.168.10.10  (ping itself - should work)
```

### Test 2: Inter-VLAN Communication (Should WORK)

From **PC1** Command Prompt:

```
ping 192.168.20.10  (PC2 in VLAN 20 - should work!)
ping 192.168.30.10  (PC3 in VLAN 30 - should work!)
```

### Test 3: Outside Network (Should WORK)

From **PC1** Command Prompt:

```
ping 10.0.0.10  (PC4 - should work!)
```

### Test 4: Trace Route

From **PC1** Command Prompt:

```
tracert 192.168.20.10
```

You should see it goes through **192.168.10.1** (the router).

---

## Troubleshooting Commands

If pings fail, use these commands to troubleshoot:

### On SW1:

```
show vlan brief
show interfaces trunk
show interfaces status
show mac address-table
```

### On R1:

```
show ip interface brief
show ip route
show interfaces gigabitEthernet 0/0.10
show interfaces trunk
```

### On PCs:

- Check IP configuration
- Check default gateway
- Try `ipconfig` in Command Prompt

---

## Challenge Tasks (Optional)

Once the basic lab works, try these:

1. **Add VLAN 99** (Management VLAN):
    
    - Create VLAN 99 on SW1
    - Assign an IP to SW1: `192.168.99.2/24`
    - Create subinterface on R1: `192.168.99.1/24`
    - Test SSH access to SW1
2. **Configure Port Security** on SW1:
    
    - Enable port security on Fa0/1
    - Set maximum 1 MAC address
    - Violation mode: shutdown
3. **Add an Access Control List (ACL)**:
    
    - Block PC1 from pinging PC2
    - Allow all other traffic
4. **Add a Second Switch**:
    
    - Add SW2
    - Configure trunk between SW1 and SW2
    - Move PC3 to SW2
    - Test connectivity

---

## Learning Objectives Covered

✅ Create and name VLANs  
✅ Assign switch ports to VLANs  
✅ Configure trunk ports  
✅ Verify VLAN configuration  
✅ Configure Router-on-a-Stick (ROAS)  
✅ Configure subinterfaces with 802.1Q encapsulation  
✅ Configure PC IP addresses and default gateways  
✅ Test inter-VLAN routing  
✅ Use troubleshooting commands

---

## Common Issues and Solutions

|Problem|Possible Cause|Solution|
|---|---|---|
|Pings fail within same VLAN|Wrong VLAN assignment|Check `show vlan brief`|
|Inter-VLAN pings fail|Router subinterface not configured|Verify subinterfaces with `show ip interface brief`|
|Trunk not working|Wrong switchport mode|Use `switchport mode trunk`|
|PC can't reach gateway|Wrong default gateway|Check PC IP configuration|
|Router interface down|Forgot `no shutdown`|Enable interface with `no shutdown`|

---

## Save Your Work!

1. **File** → **Save As**
2. Name it: `CCNA_VLAN_Lab.pkt`
3. Keep this for review before your exam!

**Estimated completion time**: 30-45 minutes

Good luck! 🎯
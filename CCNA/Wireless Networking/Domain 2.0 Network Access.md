
## Ethernet Header


| Preamble | SFD | Destination MAC Address | Source MAC Address| EtherType | Payload |  FCS |


## Ethernet Frame

Before the Frame:  Preamble and SFD are both part of the Ethernet Packet as the **Physical Layer**

### Ethernet Header

	- Source MAC Address | Destination MAC Address | Payload Data ( Protocol Headers) | FCS ( Frame Check Sequence )

	- MTU "Maximum Transmission Unit" is ***1500***

![[Pasted image 20260207121624.png]]

### In bits:
	

| Layer                   | BIts   | Bytes  | Extra            |                                        |
| ----------------------- | ------ | ------ | ---------------- | -------------------------------------- |
| Preamble                | 56     | 7      | 10101010         |                                        |
| SFD                     | 8      | 1      | 10101011         |                                        |
| Destination MAC Address | 48     | 6      |                  |                                        |
| Source MAC Address      | 48     | 6      |                  |                                        |
| 802.1Q Tag              | 32     | 4      | VLANS (optional) | TPID 0x8100 (802.1Q) 0x88a8 (802.01ad) |
| Ethertype 1             | 2      | 16     |                  |                                        |
| Payload 1               |        | 64 min | 0-1500           | Padding add if short of 64 bytes       |
| Payload 2               | Modern |        | > or = 1536      | Used as Ethertype                      |
| FCS                     | 4      | 82     |                  |                                        |
## **Common EtherType Values (≥ 1536)**

|Hex Value|Decimal|Protocol|Meaning|
|---|---|---|---|
|**0x0800**|2048|**IPv4**|Payload contains an IPv4 packet|
|**0x0806**|2054|**ARP**|Payload contains an ARP message|
|**0x86DD**|34525|**IPv6**|Payload contains an IPv6 packet|
|**0x8100**|33024|**802.1Q**|VLAN-tagged frame|
|**0x88CC**|35020|**LLDP**|Link Layer Discovery Protocol|
|**0x8847**|34887|**MPLS unicast**|MPLS packet|

## VLANS

![[Pasted image 20260207131359.png]]


## **When to Use Trunk Ports**

**Use trunk when:**

- Connecting **switch to switch**
- Connecting **switch to router** (for inter-VLAN routing - "router on a stick")
- Connecting **switch to server** (if server needs multiple VLANs)
- Connecting **switch to wireless controller** or **access point**

**Example:**

```
[Switch 1]                [Switch 2]
VLAN 10 ─────┐      ┌───── VLAN 10
VLAN 20 ─────┤ TRUNK├───── VLAN 20
VLAN 30 ─────┘      └───── VLAN 30
```

Without a trunk, you'd need **separate physical links** for each VLAN!

---

## **802.1Q - VLAN Tagging**

**The standard protocol** for VLAN tagging on trunk links.

### **How 802.1Q Works**

**802.1Q inserts a 4-byte tag** into the Ethernet frame:

**Normal Ethernet Frame:**

```
[Dest MAC][Source MAC][EtherType][Data][FCS]
```

**802.1Q Tagged Frame:**

```
[Dest MAC][Source MAC][802.1Q Tag][EtherType][Data][FCS]
                         ↑ 4 bytes inserted
```

### **802.1Q Tag Structure (4 bytes)**

```
[TPID: 0x8100][Priority: 3 bits][CFI: 1 bit][VLAN ID: 12 bits]
     2 bytes                     2 bytes
```

**Key fields:**

- **TPID (Tag Protocol ID):** 0x8100 (indicates 802.1Q tag present)
- **Priority:** QoS priority (0-7) - CoS (Class of Service)
- **VLAN ID:** Which VLAN this frame belongs to (1-4094)

## **Trunk Configuration Commands**

### **Configure Trunk Port**

```
Switch(config)# interface GigabitEthernet0/1
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk encapsulation dot1q  ! (only on older switches)
```

### **Change Native VLAN (Best Practice)**

```
Switch(config-if)# switchport trunk native vlan 99
```

### **Specify Allowed VLANs on Trunk (Optional)**

```
Switch(config-if)# switchport trunk allowed vlan 10,20,30
Switch(config-if)# switchport trunk allowed vlan add 40
Switch(config-if)# switchport trunk allowed vlan remove 30
```

**By default, trunk allows ALL VLANs (1-4094).**

---

## **Trunk Verification Commands**

```
Switch# show interfaces trunk
Switch# show interfaces GigabitEthernet0/1 switchport
Switch# show vlan brief
```

**Example output:**

```
Switch# show interfaces trunk

Port        Mode         Encapsulation  Status        Native vlan
Gi0/1       on           802.1q         trunking      99

Port        Vlans allowed on trunk
Gi0/1       10,20,30,40

Port        Vlans allowed and active in management domain
Gi0/1       10,20,30,40

Port        Vlans in spanning tree forwarding state
Gi0/1       10,20,30,40
```

---

## **Common Trunk Issues**

**1. Native VLAN mismatch**

- Symptom: CDP warnings, traffic leaking between VLANs
- Fix: Ensure both sides have same native VLAN

**2. Trunk not forming**

- Check: `switchport mode trunk` on both sides
- Check: Encapsulation set (if required)

**3. VLANs not passing over trunk**

- Check: `switchport trunk allowed vlan` list
- Check: VLAN exists on both switches

## Etherchannel

## **What is EtherChannel?**

**Definition:** **Bundling multiple physical links** into one **logical link** for increased bandwidth and redundancy.

**Benefits:**

- **Increased bandwidth:** 2 links = 2x bandwidth, 4 links = 4x bandwidth
- **Redundancy:** If one link fails, traffic continues on remaining links
- **Load balancing:** Traffic distributed across links
- **No Spanning Tree blocking:** STP sees EtherChannel as single link

## **EtherChannel Protocols**

**Three ways to configure EtherChannel:**

|Protocol|Type|Description|When to Use|
|---|---|---|---|
|**LACP**|Industry standard (802.3ad)|Negotiates bundle dynamically|**Preferred - works with all vendors**|
|**PAgP**|Cisco proprietary|Negotiates bundle dynamically|Only between Cisco devices|
|**Static (On)**|No negotiation|Forces bundle without checks|Not recommended (no error detection)|
## **LACP (Link Aggregation Control Protocol)**

**How LACP works:**

1. Interfaces send LACP packets to negotiate
2. Both sides must agree on configuration
3. Forms EtherChannel if compatible
4. Monitors links - if one fails, removes it from bundle

### **LACP Modes**

|Mode|Behavior|
|---|---|
|**active**|Initiates LACP negotiation actively|
|**passive**|Waits for LACP packets (responds only)|

**To form LACP EtherChannel:**

- **Active + Active** ✓ (best practice)
- **Active + Passive** ✓
- **Passive + Passive** ✗ (won't form - both waiting!)

---

## **EtherChannel Requirements (CRITICAL!)**

**ALL interfaces in the bundle MUST match:**

✅ **Same speed** (all 1 Gbps or all 10 Gbps) ✅ **Same duplex** (all full-duplex) ✅ **Same VLAN** (if access ports) ✅ **Same trunk configuration** (if trunk ports - native VLAN, allowed VLANs) ✅ **Same STP settings**

**If they don't match → EtherChannel won't form!**

## **EtherChannel Configuration**

### **Layer 2 EtherChannel (Switch to Switch)**

**Example: Bundle Gi0/1 and Gi0/2 using LACP**

```
Switch(config)# interface range GigabitEthernet0/1 - 2
Switch(config-if-range)# channel-group 1 mode active
Switch(config-if-range)# exit

! Port-Channel interface is created automatically
Switch(config)# interface Port-Channel1
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk native vlan 99
```

**Key commands:**

- `channel-group 1 mode active` - Adds interfaces to EtherChannel group 1 using LACP active mode
- Configuration applied to **Port-Channel interface** applies to all member links

---

### **Layer 3 EtherChannel (Routed EtherChannel)**

**Example: Routed bundle between switches acting as routers**

```
Switch(config)# interface range GigabitEthernet0/1 - 2
Switch(config-if-range)# no switchport  ! Make it a routed port
Switch(config-if-range)# channel-group 1 mode active
Switch(config-if-range)# exit

Switch(config)# interface Port-Channel1
Switch(config-if)# no switchport
Switch(config-if)# ip address 10.1.1.1 255.255.255.252
```

---

## **EtherChannel Load Balancing**

**How does EtherChannel distribute traffic across links?**

**Hash algorithm** based on:

- Source/Destination MAC addresses
- Source/Destination IP addresses
- Source/Destination TCP/UDP ports

**Key point:** Traffic flows are kept on **same physical link** for packet ordering.

**Example:** All traffic between PC1 and Server1 uses Link 1. Traffic between PC2 and Server2 might use Link 2.

**Configure load balancing method:**

```
Switch(config)# port-channel load-balance src-dst-ip
```

**Options:**

- `src-mac` - Source MAC
- `dst-mac` - Destination MAC
- `src-dst-mac` - Source and destination MAC
- `src-ip` - Source IP
- `dst-ip` - Destination IP
- `src-dst-ip` - Source and destination IP (most common)

---

## **EtherChannel Verification**

```
Switch# show etherchannel summary
Switch# show etherchannel port-channel
Switch# show interfaces Port-Channel1
Switch# show lacp neighbor
```

**Example output:**

```
Switch# show etherchannel summary

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)       LACP        Gi0/1(P)    Gi0/2(P)    

Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      N - not in use, no aggregation
        f - failed to allocate aggregator

(SU) = Layer2, in use
(P) = Port is bundled
```

---

## **Common EtherChannel Issues**

**1. EtherChannel won't form**

- Check: Speed/duplex match on all interfaces
- Check: VLAN/trunk config matches
- Check: LACP mode (both can't be passive)

**2. Some links not bundling**

- Check: `show etherchannel summary` for flags
- (s) = suspended - configuration mismatch
- Check each interface individually

**3. Traffic only using one link**

- Check load-balancing method
- May need different algorithm for your traffic patterns

---

## **Quick Comparison: Trunk vs EtherChannel**

|Feature|Trunk|EtherChannel|
|---|---|---|
|**Purpose**|Carry multiple VLANs|Increase bandwidth/redundancy|
|**Can combine?**|Yes! EtherChannel can be a trunk|Yes! Trunk can run over EtherChannel|
|**Configuration**|`switchport mode trunk`|`channel-group X mode active`|
|**Protocol**|802.1Q|LACP (or PAgP)|

**Common scenario:** **EtherChannel trunk** - bundle of links carrying multiple VLANs!

```
Switch(config)# interface range Gi0/1 - 2
Switch(config-if-range)# channel-group 1 mode active
Switch(config-if-range)# exit

Switch(config)# interface Port-Channel1
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk native vlan 99
```

This creates a **high-bandwidth trunk** using link aggregation!

---

## **Summary - Key Takeaways**

**Trunking:** ✅ Trunk = multiple VLANs over one link ✅ 802.1Q tags frames with VLAN ID ✅ Native VLAN = untagged (default VLAN 1) ✅ Both ends must match: encapsulation, native VLAN, allowed VLANs

**EtherChannel:** ✅ Bundle multiple links = increased bandwidth + redundancy ✅ LACP = industry standard (802.3ad) ✅ Active + Active or Active + Passive modes ✅ All links must match: speed, duplex, VLAN/trunk config ✅ Can combine with trunking for high-bandwidth multi-VLAN links
____________

# Cisco Switch CLI Cheat Sheet

  

## 1. Get into configuration

```

enable                ! go to privileged exec mode

configure terminal    ! enter global config

```

  

---

  

## 2. Assign hostname

```

hostname S1           ! name your switch

```

  

---

  

## 3. Configure interfaces (to PCs or uplinks)

```

interface fastEthernet0/1

 description PC1

 switchport mode access

 switchport access vlan 10

 spanning-tree portfast

 no shutdown

exit

  

interface gigabitEthernet1/1

 description uplink to router

 switchport mode access

 switchport access vlan 10

 no shutdown

exit

```

  

---

  

## 4. Create VLANs

```

vlan 10

 name USERS

exit

vlan 20

 name SERVERS

exit

```

  

---

  

## 5. Assign management IP to VLAN interface

```

interface vlan 1

 ip address 192.168.10.2 255.255.255.0

 no shutdown

exit

```

  

---

  

## 6. Assign default gateway for switch management

```

ip default-gateway 192.168.10.1

```

  

---

  

## 7. Save configuration

```

end

write memory     ! or "copy running-config startup-config"

```

  

---

  

# Verification & Troubleshooting Commands

  

### General device info

```

show running-config        ! see current config

show vlan brief            ! see VLANs and which ports are in them

show ip interface brief    ! check SVI IP, port status (up/down)

```

  

### Interfaces

```

show interfaces status     ! quick view of all ports, VLAN, speed/duplex

show interfaces f0/1       ! detailed info about one port

```

  

### Layer 2 info

```

show mac address-table     ! check learned MACs

show cdp neighbors detail  ! check devices connected on Cisco Discovery Protocol

```

  

### Spanning Tree

```

show spanning-tree vlan 1  ! check if ports are blocking/forwarding

```

  

### Connectivity

```

ping 192.168.10.1          ! test reachability to router

ping 192.168.10.10         ! test reachability to PC

```

  

---

  

## Typical Workflow

1. `en` → `conf t`  

2. `hostname S1`  

3. `interface f0/1` → assign to VLAN, no shut  

4. `vlan 10` → create VLANs if needed  

5. `interface vlan 1` → give switch IP + no shut  

6. `ip default-gateway 192.168.10.1`  

7. `end` → `wr mem`  

8. Verify with `show ip int brief`, `show vlan brief`, `ping`  

```

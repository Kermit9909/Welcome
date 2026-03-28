___________
 
# Cisco Router CLI Cheat Sheet

  

## 1. Get into configuration

```

enable                ! go to privileged exec mode

configure terminal    ! enter global config

```

  

---

  

## 2. Assign hostname

```

hostname R1           ! name your router

```

  

---

  

## 3. Configure interfaces

```

interface gigabitEthernet0/0

 description to LAN1

 ip address 192.168.10.1 255.255.255.0

 no shutdown

exit

  

interface gigabitEthernet0/1

 description to LAN2

 ip address 192.168.20.1 255.255.255.0

 no shutdown

exit

```

  

---

  

## 4. Configure inter-router link (point-to-point)

```

interface g0/2

 description to R2

 ip address 10.0.0.1 255.255.255.252

 no shutdown

exit

```

  

---

  

## 5. Routing

  

### Static route example

```

ip route 192.168.20.0 255.255.255.0 10.0.0.2

```

  

### OSPF example

```

router ospf 1

 network 192.168.10.0 0.0.0.255 area 0

 network 10.0.0.0 0.0.0.3 area 0

```

  

---

  

## 6. Save configuration

```

end

write memory     ! or "copy running-config startup-config"

```

  

---

  

# Verification & Troubleshooting Commands

  

### Interfaces

```

show ip interface brief    ! quick check of IPs, status, protocol

show interfaces g0/0       ! detailed info for one interface

```

  

### Routing

```

show ip route              ! routing table

show ip cef                ! Cisco Express Forwarding table

traceroute 192.168.20.10   ! test routing path

```

  

### Layer 2/Neighbors

```

show arp                   ! arp cache

show cdp neighbors detail  ! see connected Cisco devices

```

  

### Connectivity

```

ping 192.168.10.10         ! test LAN1 PC

ping 192.168.20.10         ! test LAN2 PC (through routing)

```

  

### Extended Ping (set source interface)

```

ping

  Protocol [ip]:

  Target IP address: 192.168.20.10

  Source address: 192.168.10.1

```

  

---

  

## Typical Workflow

1. `en` → `conf t`  

2. `hostname R1`  

3. Configure LAN interfaces (`g0/0`, `g0/1`) with IP + no shut  

4. Configure inter-router interface (`g0/2`) with IP + no shut  

5. Add static route or dynamic routing (OSPF/EIGRP)  

6. `end` → `wr mem`  

7. Verify with `show ip int brief`, `show ip route`, `ping`, `traceroute`  

```
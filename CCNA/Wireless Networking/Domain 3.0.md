

## **Static Route Configuration - Three Methods**

### **Method 1: Next-Hop IP Address**

```
Router(config)# ip route [destination-network] [subnet-mask] [next-hop-ip]
```

**Example:**

```
Router(config)# ip route 192.168.5.0 255.255.255.0 10.1.1.2
```

**Translation:** "To reach 192.168.5.0/24, send packets to 10.1.1.2"

---

### **Method 2: Exit Interface**

```
Router(config)# ip route [destination-network] [subnet-mask] [exit-interface]
```

**Example:**

```
Router(config)# ip route 192.168.5.0 255.255.255.0 GigabitEthernet0/1
```

**Translation:** "To reach 192.168.5.0/24, send packets out Gi0/1"

---

### **Method 3: Both (Next-Hop + Interface)**

```
Router(config)# ip route [destination-network] [subnet-mask] [exit-interface] [next-hop-ip]
```

**Example:**

```
Router(config)# ip route 192.168.5.0 255.255.255.0 GigabitEthernet0/1 10.1.1.2
```

**Translation:** "To reach 192.168.5.0/24, send packets out Gi0/1 to 10.1.1.2"

---

## **Which Method to Use?**

**Best practice: Next-Hop IP (Method 1)**

**Why?**

- Works with point-to-point and multi-access links
- Router performs recursive lookup (finds exit interface automatically)
- Most flexible

## **Default Route Configuration**

**Default route = "route of last resort" = catch-all for unknown destinations**

```
Router(config)# ip route 0.0.0.0 0.0.0.0 [next-hop or interface]
```

**Examples:**

```
! Default route to ISP
Router(config)# ip route 0.0.0.0 0.0.0.0 203.0.113.1

! Default route out serial interface
Router(config)# ip route 0.0.0.0 0.0.0.0 Serial0/0/0
```

**What it means:**

- 0.0.0.0 = network address (matches everything)
- 0.0.0.0 = subnet mask (matches all bits)
- Result: Matches ANY destination IP

## **IPv6 Static Routes**

**Same concept, IPv6 syntax:**

```
Router(config)# ipv6 route [destination-prefix/length] [next-hop-ipv6 or interface]
```

**Examples:**

```
! Next-hop IPv6 address
Router(config)# ipv6 route 2001:DB8:CAFE:2::/64 2001:DB8:CAFE:1::2

! Exit interface
Router(config)# ipv6 route 2001:DB8:CAFE:2::/64 GigabitEthernet0/1

! IPv6 default route
Router(config)# ipv6 route ::/0 2001:DB8::1
```

**Same logic as IPv4, just different address format!**

## **Floating Static Routes (Advanced)**

**Static route with HIGHER AD than dynamic routing:**

**Purpose:** Backup route that only activates if primary route fails

**Example:**

```
! Primary OSPF route to 192.168.5.0/24 (AD 110)
! Backup static route (AD 150) - only used if OSPF fails

Router(config)# ip route 192.168.5.0 255.255.255.0 10.9.9.9 150
                                                            ↑↑↑
                                                      Higher AD
```

**Normal operation:**

- OSPF route installed (AD 110 < 150)
- Static route NOT in routing table

**If OSPF fails:**

- OSPF route removed
- Static route kicks in (AD 150 becomes best option)
- Traffic uses backup path
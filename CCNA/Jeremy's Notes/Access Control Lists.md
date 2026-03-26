
# CCNA ACL Cheat Sheet

## ACL Fundamentals

### Key Concepts

- **Standard ACLs**: Filter based on SOURCE IP only (1-99, 1300-1999)
- **Extended ACLs**: Filter based on source IP, destination IP, protocol, port (100-199, 2000-2699)
- **Processing**: Top-down, stops at first match
- **Implicit Deny**: Invisible "deny any" at the end of every ACL
- **Wildcard Masks**: Inverse of subnet mask (0 = match, 1 = ignore)

### Placement Best Practices

- **Standard ACLs**: Place CLOSE to DESTINATION (filters source only, avoid blocking too much)
- **Extended ACLs**: Place CLOSE to SOURCE (more specific, conserve bandwidth)

---

## STANDARD ACLs

### Numbered Standard ACL Configuration

```cisco
Router(config)# access-list [1-99 | 1300-1999] {permit | deny} source [wildcard-mask]
```

**Examples:**

```cisco
! Permit a specific host
Router(config)# access-list 10 permit 192.168.1.5 0.0.0.0
! Alternative: use 'host' keyword
Router(config)# access-list 10 permit host 192.168.1.5

! Permit an entire network
Router(config)# access-list 10 permit 192.168.1.0 0.0.0.255

! Deny a subnet
Router(config)# access-list 10 deny 10.0.0.0 0.255.255.255

! Permit everything else (explicit)
Router(config)# access-list 10 permit any
```

### Named Standard ACL Configuration

```cisco
Router(config)# ip access-list standard [NAME]
Router(config-std-nacl)# [sequence] {permit | deny} source [wildcard-mask]
Router(config-std-nacl)# exit
```

**Examples:**

```cisco
Router(config)# ip access-list standard BLOCK_SALES
Router(config-std-nacl)# 10 deny 192.168.10.0 0.0.0.255
Router(config-std-nacl)# 20 permit any
Router(config-std-nacl)# exit
```

---

## EXTENDED ACLs

### Numbered Extended ACL Configuration

```cisco
Router(config)# access-list [100-199 | 2000-2699] {permit | deny} protocol source [source-wildcard] [operator port] destination [dest-wildcard] [operator port]
```

**Common Protocols:** ip, tcp, udp, icmp, eigrp, ospf

**Operators:** eq (equal), neq (not equal), lt (less than), gt (greater than), range

**Examples:**

```cisco
! Block HTTP traffic from specific network to web server
Router(config)# access-list 100 deny tcp 192.168.1.0 0.0.0.255 host 10.1.1.100 eq 80

! Permit HTTPS traffic from any source to any destination
Router(config)# access-list 100 permit tcp any any eq 443

! Deny telnet from specific host
Router(config)# access-list 100 deny tcp host 192.168.1.50 any eq 23

! Permit SSH from management subnet
Router(config)# access-list 100 permit tcp 192.168.100.0 0.0.0.255 any eq 22

! Block ICMP (ping) from specific network
Router(config)# access-list 100 deny icmp 172.16.0.0 0.0.255.255 any

! Permit DNS (both TCP and UDP port 53)
Router(config)# access-list 100 permit udp any any eq 53
Router(config)# access-list 100 permit tcp any any eq 53

! Permit all other traffic
Router(config)# access-list 100 permit ip any any
```

### Named Extended ACL Configuration

```cisco
Router(config)# ip access-list extended [NAME]
Router(config-ext-nacl)# [sequence] {permit | deny} protocol source [source-wildcard] [operator port] destination [dest-wildcard] [operator port]
Router(config-ext-nacl)# exit
```

**Examples:**

```cisco
Router(config)# ip access-list extended WEB_FILTER
Router(config-ext-nacl)# 10 permit tcp any host 10.1.1.100 eq 80
Router(config-ext-nacl)# 20 permit tcp any host 10.1.1.100 eq 443
Router(config-ext-nacl)# 30 deny ip any any
Router(config-ext-nacl)# exit

Router(config)# ip access-list extended BLOCK_SOCIAL
Router(config-ext-nacl)# deny tcp any host 172.16.1.50 eq 80
Router(config-ext-nacl)# deny tcp any host 172.16.1.50 eq 443
Router(config-ext-nacl)# permit ip any any
Router(config-ext-nacl)# exit
```

---

## APPLYING ACLs TO INTERFACES

### Interface Application Commands

```cisco
Router(config)# interface [interface-id]
Router(config-if)# ip access-group {number | name} {in | out}
Router(config-if)# exit
```

**Directions:**

- **in**: Filters traffic ENTERING the interface (most common)
- **out**: Filters traffic EXITING the interface

**Examples:**

```cisco
! Apply standard ACL inbound on interface
Router(config)# interface g0/0
Router(config-if)# ip access-group 10 in

! Apply extended ACL outbound on interface
Router(config)# interface g0/1
Router(config-if)# ip access-group 100 out

! Apply named ACL
Router(config)# interface g0/2
Router(config-if)# ip access-group BLOCK_SALES in
```

**Important Notes:**

- Only ONE ACL per interface, per direction, per protocol
- Can have one inbound AND one outbound ACL on same interface

---

## VERIFICATION COMMANDS

```cisco
! Show all configured ACLs
Router# show access-lists

! Show specific ACL
Router# show access-lists 10
Router# show access-lists BLOCK_SALES

! Show ACL application on interfaces
Router# show ip interface g0/0

! Show running config (includes ACLs)
Router# show running-config | section access-list
Router# show running-config | include access-list

! Clear ACL counters (hit counts)
Router# clear access-list counters
Router# clear access-list counters 10
```

---

## MODIFYING ACLs

### Numbered ACLs

**Problem:** Cannot edit individual lines - must delete entire ACL and recreate

```cisco
! Remove numbered ACL
Router(config)# no access-list 10

! Then recreate from scratch
Router(config)# access-list 10 permit...
```

### Named ACLs

**Advantage:** Can add, delete, or edit specific lines using sequence numbers

```cisco
! Enter named ACL config mode
Router(config)# ip access-list standard BLOCK_SALES

! Remove specific line by sequence number
Router(config-std-nacl)# no 10

! Insert new line with specific sequence number
Router(config-std-nacl)# 15 deny host 192.168.1.99

! View current ACL with sequence numbers
Router(config-std-nacl)# do show access-lists BLOCK_SALES
```

---

## COMMON PORT NUMBERS

|Service|Protocol|Port|Keyword|
|---|---|---|---|
|FTP Data|TCP|20|-|
|FTP Control|TCP|21|ftp|
|SSH|TCP|22|-|
|Telnet|TCP|23|telnet|
|SMTP|TCP|25|smtp|
|DNS|TCP/UDP|53|domain|
|DHCP Server|UDP|67|bootps|
|DHCP Client|UDP|68|bootpc|
|TFTP|UDP|69|tftp|
|HTTP|TCP|80|www|
|POP3|TCP|110|pop3|
|HTTPS|TCP|443|-|

---

## WILDCARD MASK QUICK REFERENCE

|Network|Subnet Mask|Wildcard Mask|
|---|---|---|
|/32 (Single host)|255.255.255.255|0.0.0.0|
|/24|255.255.255.0|0.0.0.255|
|/16|255.255.0.0|0.0.255.255|
|/8|255.0.0.0|0.255.255.255|
|Any|N/A|255.255.255.255|

**Calculating Wildcard:** Subtract subnet mask from 255.255.255.255

Example: /28 = 255.255.255.240

- 255.255.255.255 - 255.255.255.240 = 0.0.0.15

---

## PRACTICAL EXAMPLES

### Example 1: Block Specific User from Internet

```cisco
! Standard ACL (placed near destination - Internet router)
Router(config)# access-list 1 deny host 192.168.1.50
Router(config)# access-list 1 permit any
Router(config)# interface g0/1
Router(config-if)# ip access-group 1 out
```

### Example 2: Allow Only HTTP/HTTPS to Web Server

```cisco
! Extended ACL (placed near source)
Router(config)# ip access-list extended WEB_ACCESS
Router(config-ext-nacl)# permit tcp any host 10.1.1.100 eq 80
Router(config-ext-nacl)# permit tcp any host 10.1.1.100 eq 443
Router(config-ext-nacl)# deny ip any host 10.1.1.100
Router(config-ext-nacl)# permit ip any any
Router(config-ext-nacl)# exit
Router(config)# interface g0/0
Router(config-if)# ip access-group WEB_ACCESS in
```

### Example 3: Restrict Management Access

```cisco
! Only allow SSH from IT subnet
Router(config)# ip access-list extended MGMT_ACCESS
Router(config-ext-nacl)# permit tcp 192.168.100.0 0.0.0.255 any eq 22
Router(config-ext-nacl)# deny tcp any any eq 22
Router(config-ext-nacl)# permit ip any any
Router(config-ext-nacl)# exit
Router(config)# interface g0/0
Router(config-if)# ip access-group MGMT_ACCESS in
```

---

## EXAM TIPS

1. **Read Questions Carefully**: Determine if it's asking for standard or extended ACL
2. **Check Placement**: Standard near destination, Extended near source
3. **Remember Implicit Deny**: Every ACL ends with invisible "deny any"
4. **Wildcard Masks**: 0 = must match exactly, 255 = ignore completely
5. **Order Matters**: Most specific to least specific (top to bottom)
6. **Named ACLs**: Preferred in production (can edit), but numbered still tested
7. **One ACL per Interface/Direction**: Can't apply two inbound ACLs to same interface
8. **Test Application**: Use "show ip interface" to verify ACL is applied correctly
9. **Sequence Numbers**: Default increment by 10 (10, 20, 30...) in named ACLs
10. **Port Numbers**: Memorize common ones (SSH=22, Telnet=23, HTTP=80, HTTPS=443)

---

## TROUBLESHOOTING CHECKLIST

- [ ] Is ACL applied to correct interface?
- [ ] Is direction (in/out) correct?
- [ ] Are entries in correct order (most specific first)?
- [ ] Did you include "permit any" if needed (or is implicit deny intended)?
- [ ] Are wildcard masks correct (not subnet masks)?
- [ ] For extended ACLs: source and destination in correct order?
- [ ] Is protocol specified correctly (tcp/udp/ip)?
- [ ] Are port numbers correct?
- [ ] Check hit counts: `show access-lists` (see if rules are matching)
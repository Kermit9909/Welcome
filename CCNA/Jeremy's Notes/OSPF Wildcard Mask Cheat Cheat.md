

# OSPF Wildcard Mask Cheat Sheet

## Quick Reference: Subnet Mask to Wildcard Conversion

### The Golden Rule

**Wildcard = 255.255.255.255 - Subnet Mask** (Subtract each octet individually)

---

## Common CIDR Notations & Wildcard Masks

| CIDR | Subnet Mask     | Wildcard Mask | Hosts | Common Use     |
| ---- | --------------- | ------------- | ----- | -------------- |
| /32  | 255.255.255.255 | 0.0.0.0       | 1     | Single host    |
| /31  | 255.255.255.254 | 0.0.0.1       | 2     | Point-to-point |
| /30  | 255.255.255.252 | 0.0.0.3       | 4     | Point-to-point |
| /29  | 255.255.255.248 | 0.0.0.7       | 8     | Small subnet   |
| /28  | 255.255.255.240 | 0.0.0.15      | 16    | Small subnet   |
| /27  | 255.255.255.224 | 0.0.0.31      | 32    | Small subnet   |
| /26  | 255.255.255.192 | 0.0.0.63      | 64    | Medium subnet  |
| /25  | 255.255.255.128 | 0.0.0.127     | 128   | Medium subnet  |
| /24  | 255.255.255.0   | 0.0.0.255     | 256   | Class C        |
| /23  | 255.255.254.0   | 0.0.1.255     | 512   | 2 Class Cs     |
| /22  | 255.255.252.0   | 0.0.3.255     | 1024  | 4 Class Cs     |
| /21  | 255.255.248.0   | 0.0.7.255     | 2048  | 8 Class Cs     |
| /20  | 255.255.240.0   | 0.0.15.255    | 4096  | 16 Class Cs    |
| /16  | 255.255.0.0     | 0.0.255.255   | 65536 | Class B        |
| /8   | 255.0.0.0       | 0.255.255.255 | 16M   | Class A        |

---

## CCNA Focus: The Critical Ones to Memorize

### Fourth Octet (Most Common)

```
/30 = 0.0.0.3    (point-to-point links)
/28 = 0.0.0.15   (16 hosts)
/27 = 0.0.0.31   (32 hosts)
/26 = 0.0.0.63   (64 hosts)
/24 = 0.0.0.255  (256 hosts - standard Class C)
```

### Third Octet (Important for summarization)

```
/23 = 0.0.1.255
/22 = 0.0.3.255
/21 = 0.0.7.255
/20 = 0.0.15.255
/16 = 0.0.255.255
```

---

## Powers of 2 Quick Reference

When creating **custom wildcards** to match multiple subnets:

|Bits Variable|Wildcard Value|Covers|
|---|---|---|
|1 bit|1|2 values|
|2 bits|3|4 values|
|3 bits|7|8 values|
|4 bits|15|16 values|
|5 bits|31|32 values|
|6 bits|63|64 values|
|7 bits|127|128 values|
|8 bits|255|256 values|

**Formula:** 2^n - 1 (where n = number of bits)

---

## OSPF Network Command Examples

### Activate Single Interface

```
Router(config-router)# network 10.0.12.1 0.0.0.0 area 0
```

Matches ONLY interface with IP 10.0.12.1

### Activate Entire Subnet

```
Router(config-router)# network 10.0.12.0 0.0.0.15 area 0
```

Matches all IPs in 10.0.12.0/28 subnet

### Activate Multiple Adjacent Subnets (Custom Wildcard)

```
Router(config-router)# network 10.0.12.0 0.0.1.255 area 0
```

Matches 10.0.12.0/28 AND 10.0.13.0/26 with one command

### Activate All Interfaces

```
Router(config-router)# network 0.0.0.0 255.255.255.255 area 0
```

Matches ANY IP address (use with caution!)

---

## Common OSPF Scenarios

### Scenario 1: Point-to-Point Link

**Interface:** 192.168.1.1/30 **Command:** `network 192.168.1.0 0.0.0.3 area 0`

### Scenario 2: LAN Interface

**Interface:** 10.1.1.1/24 **Command:** `network 10.1.1.0 0.0.0.255 area 0`

### Scenario 3: Multiple Interfaces with One Command

**Interfaces:**

- G0/0: 172.16.1.1/28
- G0/1: 172.16.2.1/28
- G0/2: 172.16.3.1/28

**Option 1 (Specific):** Three separate commands

```
network 172.16.1.0 0.0.0.15 area 0
network 172.16.2.0 0.0.0.15 area 0
network 172.16.3.0 0.0.0.15 area 0
```

**Option 2 (Summarized):** One command

```
network 172.16.0.0 0.0.3.255 area 0
```

(Covers 172.16.0.0 through 172.16.3.255)

---

## Binary Conversion Helper

### Common Third Octet Values in Binary

```
0   = 00000000
1   = 00000001
3   = 00000011
7   = 00000111
15  = 00001111
31  = 00011111
63  = 00111111
127 = 01111111
255 = 11111111
```

### Finding Custom Wildcards

**Example:** Match 10.0.12.0 and 10.0.13.0

1. Convert to binary:
    
    - 12 = 00001100
    - 13 = 00001101
2. Find difference (last bit):
    
    - Wildcard needed: 00000001 = 1
3. Result: 0.0.1.255
    

---

## Pro Tips for OSPF Network Statements

1. **Most Specific First:** OSPF processes network statements top to bottom
2. **Use 0.0.0.0 for Specific Interfaces:** Most secure and predictable
3. **Avoid 255.255.255.255:** Too broad, can cause security issues
4. **Match Exam Questions:** Use the wildcard that covers exactly what's asked
5. **Think in Binary:** For complex scenarios, convert to binary

---

## Quick Mental Math Trick

**To find wildcard from /26, /27, /28:**

1. Find the subnet mask value in the last octet:
    
    - /26 → 192
    - /27 → 224
    - /28 → 240
2. Subtract from 255:
    
    - 255 - 192 = **63** → 0.0.0.63
    - 255 - 224 = **31** → 0.0.0.31
    - 255 - 240 = **15** → 0.0.0.15

---

## Verification Commands

After configuring OSPF, verify with:

```
Router# show ip ospf interface brief
Router# show ip ospf neighbor
Router# show ip protocols
Router# show ip route ospf
```

---

## Common Mistakes to Avoid

❌ **Using subnet mask instead of wildcard**

```
network 10.0.1.0 255.255.255.0 area 0  (WRONG!)
```

✅ **Use wildcard mask**

```
network 10.0.1.0 0.0.0.255 area 0  (CORRECT!)
```

❌ **Forgetting the area number**

```
network 10.0.1.0 0.0.0.255  (WRONG!)
```

✅ **Always include area**

```
network 10.0.1.0 0.0.0.255 area 0  (CORRECT!)
```

---

**Study Tip:** Create Anki flashcards for /26, /27, /28, and /30 wildcards - these appear most on CCNA exams!

**Last Updated:** November 2025 **For:** CCNA 200-301 Exam Preparation
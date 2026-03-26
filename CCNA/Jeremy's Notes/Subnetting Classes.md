# Subnetting Reference Table

  

## Class A Subnets (Default /8)

  

| CIDR | Subnet Mask | Block Size | Usable Hosts | Subnets from /8 |

|------|-------------|------------|--------------|-----------------|

| /8   | 255.0.0.0 | 16,777,216 | 16,777,214 | 1 |

| /9   | 255.128.0.0 | 8,388,608 | 8,388,606 | 2 |

| /10  | 255.192.0.0 | 4,194,304 | 4,194,302 | 4 |

| /11  | 255.224.0.0 | 2,097,152 | 2,097,150 | 8 |

| /12  | 255.240.0.0 | 1,048,576 | 1,048,574 | 16 |

| /13  | 255.248.0.0 | 524,288 | 524,286 | 32 |

| /14  | 255.252.0.0 | 262,144 | 262,142 | 64 |

| /15  | 255.254.0.0 | 131,072 | 131,070 | 128 |

  

## Class B Subnets (Default /16)

  

| CIDR | Subnet Mask | Block Size | Usable Hosts | Subnets from /16 |

|------|-------------|------------|--------------|------------------|

| /16  | 255.255.0.0 | 65,536 | 65,534 | 1 |

| /17  | 255.255.128.0 | 32,768 | 32,766 | 2 |

| /18  | 255.255.192.0 | 16,384 | 16,382 | 4 |

| /19  | 255.255.224.0 | 8,192 | 8,190 | 8 |

| /20  | 255.255.240.0 | 4,096 | 4,094 | 16 |

| /21  | 255.255.248.0 | 2,048 | 2,046 | 32 |

| /22  | 255.255.252.0 | 1,024 | 1,022 | 64 |

| /23  | 255.255.254.0 | 512 | 510 | 128 |

  

## Class C Subnets (Default /24) - **Most Common for CCNA**

  

| CIDR | Subnet Mask | Block Size | Usable Hosts | Subnets from /24 |

|------|-------------|------------|--------------|------------------|

| /24  | 255.255.255.0 | 256 | 254 | 1 |

| /25  | 255.255.255.128 | 128 | 126 | 2 |

| /26  | 255.255.255.192 | 64 | 62 | 4 |

| /27  | 255.255.255.224 | 32 | 30 | 8 |

| /28  | 255.255.255.240 | 16 | 14 | 16 |

| /29  | 255.255.255.248 | 8 | 6 | 32 |

| /30  | 255.255.255.252 | 4 | 2 | 64 |

| /31  | 255.255.255.254 | 2 | 2* | 128 |

| /32  | 255.255.255.255 | 1 | 1* | 256 |

  

**/31 and /32 Notes:**

- **/31**: Used for point-to-point links (RFC 3021). No network/broadcast addresses needed, so 2 usable hosts.

- **/32**: Host route, represents a single IP address. Used in routing tables.

  

---

  

## Quick Memory Tips

  

### Powers of 2 for Host Bits:

- 1 bit = 2 hosts

- 2 bits = 4 hosts

- 3 bits = 8 hosts

- 4 bits = 16 hosts

- 5 bits = 32 hosts

- 6 bits = 64 hosts

- 7 bits = 128 hosts

- 8 bits = 256 hosts

  

### Formula:

- **Usable Hosts** = 2^(32 - CIDR) - 2

- **Subnets Created** = 2^(CIDR - Classful Mask)

Class A subnet formula for # of subnets 2^(Custom CIDR-8)

  

### Block Size Calculation:

Find the interesting octet, then: **256 - subnet mask value = block size**
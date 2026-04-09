# Identifying Hosts - DHCP, NBNS, and Kerberos Analysis

## Why Host Identification Matters
- Determines investigation starting point
- Links malicious traffic to specific hosts/users
- Enterprise networks use naming patterns — easy to follow, but also easy for adversaries to clone

## Protocols Used for Host/User Identification
- DHCP — automatic IP assignment, reveals hostnames
- NBNS — NetBIOS, allows apps on different hosts to communicate
- Kerberos — Windows domain authentication

---

## DHCP Analysis

### Key Packet Types
| Packet | Meaning | Filter |
|---|---|---|
| DHCP Request | Client requesting IP — contains hostname | `dhcp.option.dhcp == 3` |
| DHCP ACK | Request accepted | `dhcp.option.dhcp == 5` |
| DHCP NAK | Request denied | `dhcp.option.dhcp == 6` |

### Global Search
```
dhcp or bootp
```

### DHCP Request — Key Options
| Option | Info |
|---|---|
| 12 | Hostname |
| 50 | Requested IP address |
| 51 | Requested IP lease time |
| 61 | Client MAC address |
```
dhcp.option.hostname contains "keyword"
```

### DHCP ACK — Key Options
| Option | Info |
|---|---|
| 15 | Domain name |
| 51 | Assigned IP lease time |
```
dhcp.option.domain_name contains "keyword"
```

### DHCP NAK
- Option 56 contains rejection reason/message
- Read the message manually rather than filtering — context matters

---

## NBNS (NetBIOS) Analysis

### Global Search
```
nbns
```

### Key Info Available
- Queries contain: name, TTL, IP address details
```
nbns.name contains "keyword"
```

---

## Kerberos Analysis
- Default Windows domain authentication
- Proves identity securely across untrusted networks

### Global Search
```
kerberos
```

### Username Hunting
```
kerberos.CNameString contains "keyword"

# Filter out hostnames (end with $), show only usernames:
kerberos.CNameString and !(kerberos.CNameString contains "$")
```
> **Key note:** CNameString ending with `$` = hostname. Without `$` = username.

### Key Fields
| Field | Info |
|---|---|
| pvno | Protocol version |
| realm | Domain name for ticket |
| sname | Service and domain name for ticket |
| addresses | Client IP + NetBIOS name (request packets only) |

### Useful Filters
```
kerberos.pvno == 5
kerberos.realm contains ".org"
kerberos.SNameString == "krbtg"
```

---

## Q && A:

**What is the MAC address of the host "Galaxy A30"**
9a:81:41:cb:96:6c
***dhcp.options.hostname contains "Galaxy"***

**How many NetBIOS registration requests does the "LIVALJM" workstation have?**
16
***nbns.name contains "LIVALJM" && nbns.flags.opcode==5

**Which host requested the IP address "172.16.13.85"?**
Galaxy-A12
***dhcp.option.dhcp==3***

**What is the IP address of the user "u5"? (Enter the address in defanged format.)**
10[.]1[.]12[.]2
***kerberos.CNameString and !(kerberos.CNameString contains "$")***

**What is the hostname of the available host in the Kerberos packets?**
xp1$
***kerberos.CNameString and (kerberos.CNameString contains "$")***


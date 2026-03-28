# DNS & DHCP CCNA Cheat Sheet

## DHCP (Dynamic Host Configuration Protocol)

### Core Concepts

**Purpose**: Automatically assigns IP addresses and network configuration to hosts

**Port Numbers**:

- UDP 67 (DHCP Server)
- UDP 68 (DHCP Client)

**DORA Process** (4-step exchange):

1. **Discover** - Client broadcasts to find DHCP servers (src: 0.0.0.0, dst: 255.255.255.255)
2. **Offer** - Server offers IP address and parameters
3. **Request** - Client requests the offered IP (broadcast)
4. **Acknowledge** - Server confirms assignment

### DHCP Message Types

- DHCPDISCOVER - Client searches for servers
- DHCPOFFER - Server proposes configuration
- DHCPREQUEST - Client accepts or renews lease
- DHCPACK - Server confirms lease
- DHCPNAK - Server denies request
- DHCPRELEASE - Client releases IP
- DHCPDECLINE - Client rejects offered IP
- DHCPINFORM - Client requests parameters only

### Lease Process

**Lease Times**:

- Default lease: 24 hours (1 day)
- T1 (Renewal): 50% of lease time (12 hours) - unicast to original server
- T2 (Rebinding): 87.5% of lease time (21 hours) - broadcast to any server

**Lease States**:

- Allocating - Initial assignment
- Bound - Lease active, client using IP
- Renewing - T1 reached, attempting renewal
- Rebinding - T2 reached, seeking any server

### DHCP Configuration (Cisco Router as Server)

```
! Enable DHCP service
Router(config)# service dhcp

! Create DHCP pool
Router(config)# ip dhcp pool POOL_NAME
Router(dhcp-config)# network 192.168.1.0 255.255.255.0
Router(dhcp-config)# default-router 192.168.1.1
Router(dhcp-config)# dns-server 8.8.8.8 8.8.4.4
Router(dhcp-config)# domain-name example.com
Router(dhcp-config)# lease {days [hours] [minutes] | infinite}

! Exclude addresses from DHCP pool
Router(config)# ip dhcp excluded-address 192.168.1.1 192.168.1.10

! Configure specific host reservation
Router(config)# ip dhcp pool CLIENT1
Router(dhcp-config)# host 192.168.1.50 255.255.255.0
Router(dhcp-config)# client-identifier 01aa.bbcc.ddee.ff
Router(dhcp-config)# default-router 192.168.1.1
```

### DHCP Relay Agent (IP Helper)

**Purpose**: Forwards DHCP broadcasts across routers (since routers don't forward broadcasts)

```
! Configure on interface facing DHCP clients
Router(config)# interface g0/0
Router(config-if)# ip helper-address 10.1.1.100

! Multiple DHCP servers
Router(config-if)# ip helper-address 10.1.1.100
Router(config-if)# ip helper-address 10.1.1.101
```

**Protocols forwarded by IP Helper** (UDP):

- Port 37 - Time
- Port 49 - TACACS
- Port 53 - DNS
- Port 67 - DHCP/BOOTP Server
- Port 68 - DHCP/BOOTP Client
- Port 69 - TFTP
- Port 137 - NetBIOS Name Service
- Port 138 - NetBIOS Datagram Service

### DHCP Client Configuration

```
! Configure interface as DHCP client
Router(config)# interface g0/0
Router(config-if)# ip address dhcp
Router(config-if)# no shutdown
```

### DHCP Verification Commands

```
! Show DHCP bindings (leases)
Router# show ip dhcp binding

! Show DHCP pool statistics
Router# show ip dhcp pool [name]

! Show DHCP server statistics
Router# show ip dhcp server statistics

! Show DHCP conflicts
Router# show ip dhcp conflict

! Clear DHCP bindings
Router# clear ip dhcp binding {address | *}

! Debug DHCP
Router# debug ip dhcp server {events | packets | linkage}
```

### DHCP Snooping (Security)

**Purpose**: Prevents rogue DHCP servers and DHCP-based attacks

```
! Enable globally
Switch(config)# ip dhcp snooping

! Enable per VLAN
Switch(config)# ip dhcp snooping vlan 10,20,30

! Configure trusted ports (uplinks to legitimate servers)
Switch(config)# interface g0/1
Switch(config-if)# ip dhcp snooping trust

! Rate limit DHCP packets on untrusted ports
Switch(config-if)# ip dhcp snooping limit rate 10

! Verify MAC address in DHCP packets
Switch(config)# ip dhcp snooping verify mac-address

! Show snooping status
Switch# show ip dhcp snooping
Switch# show ip dhcp snooping binding
```

---

## DNS (Domain Name System)

### Core Concepts

**Purpose**: Resolves domain names to IP addresses (and vice versa)

**Port Numbers**:

- UDP 53 - DNS queries (standard)
- TCP 53 - DNS zone transfers and large responses

**Hierarchy**: Root Servers → TLD Servers (.com, .org) → Authoritative Servers

### DNS Record Types

|Record Type|Purpose|Example|
|---|---|---|
|**A**|IPv4 address|example.com → 192.168.1.10|
|**AAAA**|IPv6 address|example.com → 2001:db8::1|
|**CNAME**|Canonical name (alias)|www → example.com|
|**MX**|Mail server|Priority 10: mail.example.com|
|**NS**|Name server|Authoritative DNS server|
|**PTR**|Reverse lookup|IP → domain name|
|**SOA**|Start of Authority|Zone metadata|
|**TXT**|Text records|SPF, DKIM, verification|
|**SRV**|Service locator|_service._proto.name|

### DNS Query Types

**Recursive Query**:

- Client asks DNS server to fully resolve name
- DNS server does all the work
- Returns final answer or error

**Iterative Query**:

- DNS server returns best answer it has
- May be referral to another server
- Client follows referrals

**Forward Lookup**: Domain name → IP address **Reverse Lookup**: IP address → Domain name (uses in-addr.arpa domain)

### DNS Resolution Process

1. Client checks local DNS cache
2. Client queries configured DNS server (recursive query)
3. DNS server checks its cache
4. If not cached, DNS server queries root server (iterative)
5. Root server refers to TLD server
6. TLD server refers to authoritative server
7. Authoritative server provides answer
8. DNS server caches result and returns to client
9. Client caches result

**TTL (Time to Live)**: How long DNS records are cached (in seconds)

### DNS Configuration (Cisco Router)

```
! Configure DNS server on router
Router(config)# ip dns server

! Configure router to use DNS server
Router(config)# ip name-server 8.8.8.8 8.8.4.4

! Enable DNS lookups (enabled by default)
Router(config)# ip domain-lookup

! Disable DNS lookups (speeds up typos in CLI)
Router(config)# no ip domain-lookup

! Set domain name for host lookups
Router(config)# ip domain-name example.com

! Create static DNS entries
Router(config)# ip host server1 192.168.1.100
Router(config)# ip host server2 192.168.1.101

! Configure DNS source interface
Router(config)# ip domain-lookup source-interface loopback0
```

### DNS Client Configuration

```
! Interface automatically gets DNS from DHCP
Router(config)# interface g0/0
Router(config-if)# ip address dhcp

! Manual DNS configuration
Router(config)# ip name-server 8.8.8.8 8.8.4.4 1.1.1.1
```

### DNS Verification Commands

```
! Test DNS resolution
Router# ping server1.example.com
Router# nslookup www.cisco.com

! Show DNS host table (static entries)
Router# show hosts

! Show DNS cache
Router# show ip dns cache

! Clear DNS cache
Router# clear host {name | *}

! Debug DNS
Router# debug ip dns
```

### DNS Security Considerations

**DNS Spoofing/Cache Poisoning**: Attacker inserts false DNS records into cache

**DNS Amplification Attack**: Attacker uses open DNS resolvers to DDoS target

**DNSSEC**: Adds cryptographic signatures to DNS records (not heavily tested in CCNA)

**Best Practices**:

- Use trusted, secure DNS servers
- Implement DNS filtering/security
- Disable unnecessary DNS services
- Use split DNS (internal/external)

---

## Integration: DHCP + DNS

### Automatic DNS Registration

DHCP servers can register clients with DNS automatically:

```
Router(config)# ip dhcp pool POOL_NAME
Router(dhcp-config)# update dns
Router(dhcp-config)# dns-server 192.168.1.10
```

### Common Configuration Example

```
! DHCP Pool with DNS
Router(config)# ip dhcp excluded-address 192.168.1.1 192.168.1.10
Router(config)# ip dhcp pool VLAN10
Router(dhcp-config)# network 192.168.1.0 255.255.255.0
Router(dhcp-config)# default-router 192.168.1.1
Router(dhcp-config)# dns-server 8.8.8.8 1.1.1.1
Router(dhcp-config)# domain-name company.local
Router(dhcp-config)# lease 7

! Router using DNS
Router(config)# ip domain-lookup
Router(config)# ip name-server 8.8.8.8 1.1.1.1
Router(config)# ip domain-name company.local
```

---

## Troubleshooting Scenarios

### DHCP Issues

**Problem**: Client not getting IP address

**Troubleshooting Steps**:

1. Verify DHCP service enabled: `show run | include dhcp`
2. Check DHCP pool: `show ip dhcp pool`
3. Verify excluded addresses don't overlap pool
4. Check bindings: `show ip dhcp binding`
5. Check for conflicts: `show ip dhcp conflict`
6. Verify interface up: `show ip interface brief`
7. Check IP helper-address if remote: `show run interface g0/0`
8. Debug: `debug ip dhcp server events`

**Problem**: Wrong network configuration received

**Check**:

- DHCP pool configuration
- Rogue DHCP server (use DHCP snooping)
- IP helper pointing to wrong server

### DNS Issues

**Problem**: Cannot resolve domain names

**Troubleshooting Steps**:

1. Test connectivity to DNS server: `ping 8.8.8.8`
2. Check DNS configuration: `show run | include name-server`
3. Test specific lookup: `nslookup www.cisco.com`
4. Check if DNS lookups enabled: `show run | include domain-lookup`
5. Verify DNS cache: `show hosts`
6. Clear cache and retry: `clear host *`
7. Debug: `debug ip dns`

**Problem**: Slow DNS resolution

**Check**:

- DNS server response time
- TTL values (very low = frequent queries)
- DNS server reachability/routing
- DNS cache configuration

---

## Key CCNA Exam Points

### DHCP Must-Know

✓ DORA process and message types ✓ Lease timers (T1, T2) ✓ Configuration syntax (pool, network, default-router, dns-server) ✓ IP helper-address and when to use it ✓ DHCP snooping purpose and configuration ✓ Excluded addresses vs. pool ranges ✓ Verification commands (binding, pool, statistics)

### DNS Must-Know

✓ Purpose and port numbers (UDP 53, TCP 53) ✓ Common record types (A, AAAA, CNAME, MX, PTR) ✓ Recursive vs. iterative queries ✓ Forward vs. reverse lookups ✓ Basic configuration (ip name-server, ip domain-name) ✓ When to disable DNS lookups (no ip domain-lookup) ✓ Verification with ping and nslookup

### Common Exam Traps

- DHCP relay needed when server is on different subnet
- Router interfaces don't forward broadcasts (hence IP helper)
- "no ip domain-lookup" speeds up CLI but disables name resolution
- DHCP snooping trust must be on uplinks to legitimate servers
- DNS uses UDP for queries but TCP for zone transfers
- T1 timer is unicast, T2 timer is broadcast

---

## Quick Reference Commands

```
! === DHCP Configuration ===
ip dhcp excluded-address [start] [end]
ip dhcp pool [name]
  network [network] [mask]
  default-router [gateway]
  dns-server [server1] [server2]
  domain-name [name]
  lease [days] [hours] [minutes]

! === DHCP Relay ===
interface [int]
  ip helper-address [server-ip]

! === DNS Configuration ===
ip name-server [server1] [server2]
ip domain-name [name]
ip domain-lookup / no ip domain-lookup
ip host [name] [ip]

! === Verification ===
show ip dhcp binding
show ip dhcp pool
show ip dhcp conflict
show hosts
show ip dns cache
ping [hostname]
nslookup [hostname]
```

---

**Study Tips for Exam Day**:

- Memorize DORA acronym cold
- Know when IP helper is required (different subnet)
- Understand the difference between trusted/untrusted DHCP snooping ports
- Be able to identify DNS record types from output
- Practice calculating lease renewal times (50% and 87.5%)
- Remember UDP 67/68 for DHCP, UDP 53 for DNS queries

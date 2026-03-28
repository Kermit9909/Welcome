# NAT (Network Address Translation) - CCNA Exam Guide

## Overview

Network Address Translation (NAT) is a method of remapping one IP address space into another by modifying network address information in the IP header of packets while they are in transit across a routing device.

**Primary Purpose**: Conserve public IPv4 addresses by allowing multiple private IP addresses to share one or more public IP addresses.

## Why NAT Exists

- **IPv4 Address Exhaustion**: Limited public IPv4 addresses (approximately 4.3 billion)
- **Security**: Hides internal network structure from external networks
- **Flexibility**: Allows internal IP addressing schemes to change without affecting external connectivity
- **Cost Savings**: Reduces need for purchasing additional public IP addresses

## Private vs Public IP Address Ranges

### Private IP Address Ranges (RFC 1918)

These addresses are NOT routable on the public internet:

- **Class A**: 10.0.0.0 to 10.255.255.255 (10.0.0.0/8)
- **Class B**: 172.16.0.0 to 172.31.255.255 (172.16.0.0/12)
- **Class C**: 192.168.0.0 to 192.168.255.255 (192.168.0.0/16)

### Public IP Addresses

All other IPv4 addresses (excluding reserved ranges) that are globally routable on the internet.

## NAT Terminology

### Inside vs Outside

- **Inside Network**: The network you control (typically private addresses)
- **Outside Network**: The external network (typically the internet)

### Local vs Global

- **Inside Local**: The actual IP address assigned to a host on the inside network (private IP)
- **Inside Global**: The translated IP address seen by the outside network (public IP)
- **Outside Local**: The IP address of an outside host as it appears to the inside network
- **Outside Global**: The actual IP address assigned to a host on the outside network

### Common Scenario Example

```
Inside Local: 192.168.1.10 (PC's actual IP)
Inside Global: 203.0.113.5 (PC's translated public IP)
Outside Global: 8.8.8.8 (Google DNS actual IP)
Outside Local: 8.8.8.8 (Usually same as outside global)
```

## Types of NAT

### 1. Static NAT (One-to-One Translation)

**Concept**: Permanently maps one private IP address to one specific public IP address.

**Use Cases**:

- Web servers
- Email servers
- Any device that needs to be accessible from the internet with a consistent public IP

**Advantages**:

- Predictable - same private IP always translates to same public IP
- Allows inbound connections to be initiated from outside
- Good for servers

**Disadvantages**:

- Doesn't conserve addresses (requires one public IP per internal host)
- More expensive (each mapping uses a public IP)

**Configuration Example**:

```
Router(config)# interface g0/0
Router(config-if)# ip nat inside
Router(config-if)# exit

Router(config)# interface g0/1
Router(config-if)# ip nat outside
Router(config-if)# exit

Router(config)# ip nat inside source static 192.168.1.10 203.0.113.5
Router(config)# ip nat inside source static 192.168.1.11 203.0.113.6
```

### 2. Dynamic NAT (Pool-Based Translation)

**Concept**: Automatically maps inside local addresses to a pool of available public IP addresses on a first-come, first-served basis.

**Use Cases**:

- Organizations with more internal hosts than public IPs
- When you need many devices to access internet but not simultaneously

**Advantages**:

- More efficient use of public IP addresses than static NAT
- Automatic assignment
- Can support more internal hosts than available public IPs (as long as not all active simultaneously)

**Disadvantages**:

- Still requires multiple public IPs (just fewer than one-to-one)
- Cannot initiate inbound connections
- If pool is exhausted, new connections fail

**Configuration Example**:

```
Router(config)# interface g0/0
Router(config-if)# ip nat inside
Router(config-if)# exit

Router(config)# interface g0/1
Router(config-if)# ip nat outside
Router(config-if)# exit

! Create access list to identify inside addresses
Router(config)# access-list 1 permit 192.168.1.0 0.0.0.255

! Create NAT pool
Router(config)# ip nat pool PUBLIC_POOL 203.0.113.10 203.0.113.20 netmask 255.255.255.0

! Link ACL to pool
Router(config)# ip nat inside source list 1 pool PUBLIC_POOL
```

### 3. PAT (Port Address Translation) / NAT Overload

**Concept**: Maps multiple private IP addresses to a single public IP address (or small pool) by using unique source port numbers to track connections.

**Also Known As**:

- NAT Overload
- Many-to-One NAT
- NAPT (Network Address Port Translation)

**How It Works**:

1. Internal host sends packet with source IP 192.168.1.10:5000
2. Router translates to public IP 203.0.113.5:50001
3. Router maintains translation table tracking port mappings
4. Return traffic to 203.0.113.5:50001 is translated back to 192.168.1.10:5000

**Use Cases**:

- Most common form of NAT
- Home routers
- Small to medium businesses
- Any scenario needing maximum address conservation

**Advantages**:

- Extremely efficient - thousands of internal hosts can share one public IP
- Most cost-effective NAT solution
- Most common in real-world deployments

**Disadvantages**:

- Cannot easily host servers accessible from internet
- Limited to ~65,000 simultaneous connections per public IP (based on available ports)
- Some applications may have issues with PAT

**Configuration Example (Using Interface IP)**:

```
Router(config)# interface g0/0
Router(config-if)# ip nat inside
Router(config-if)# exit

Router(config)# interface g0/1
Router(config-if)# ip nat outside
Router(config-if)# exit

! Create access list
Router(config)# access-list 1 permit 192.168.1.0 0.0.0.255

! PAT using the interface's public IP
Router(config)# ip nat inside source list 1 interface g0/1 overload
```

**Configuration Example (Using Pool)**:

```
Router(config)# access-list 1 permit 192.168.1.0 0.0.0.255
Router(config)# ip nat pool PAT_POOL 203.0.113.5 203.0.113.5 netmask 255.255.255.255
Router(config)# ip nat inside source list 1 pool PAT_POOL overload
```

## NAT Configuration Steps (General Process)

### Step 1: Configure Inside Interface(s)

```
Router(config)# interface g0/0
Router(config-if)# ip nat inside
```

### Step 2: Configure Outside Interface(s)

```
Router(config)# interface g0/1
Router(config-if)# ip nat outside
```

### Step 3: Define Which Addresses to Translate

Use an access list to specify inside local addresses:

```
Router(config)# access-list 1 permit 192.168.1.0 0.0.0.255
```

### Step 4: Configure NAT Type

**For Static NAT**:

```
Router(config)# ip nat inside source static [inside-local] [inside-global]
```

**For Dynamic NAT**:

```
Router(config)# ip nat pool [pool-name] [start-ip] [end-ip] netmask [mask]
Router(config)# ip nat inside source list [acl] pool [pool-name]
```

**For PAT**:

```
Router(config)# ip nat inside source list [acl] interface [interface] overload
```

## Verification Commands

### Show Active NAT Translations

```
Router# show ip nat translations
```

Shows current active NAT entries in the translation table.

**Output Example**:

```
Pro Inside global      Inside local       Outside local      Outside global
tcp 203.0.113.5:1024   192.168.1.10:1024  8.8.8.8:53        8.8.8.8:53
tcp 203.0.113.5:1025   192.168.1.11:2048  1.1.1.1:80        1.1.1.1:80
```

### Show NAT Statistics

```
Router# show ip nat statistics
```

Displays NAT configuration details, hits, misses, and expired translations.

### Clear NAT Translations

```
Router# clear ip nat translation *
```

Clears all dynamic NAT translations (doesn't affect static entries).

```
Router# clear ip nat translation inside [global-ip] [local-ip]
```

Clears specific translation entry.

### Debug NAT

```
Router# debug ip nat
```

Shows real-time NAT translations (use carefully in production - can generate lots of output).

```
Router# debug ip nat detailed
```

More verbose NAT debugging information.

**Turn off debugging**:

```
Router# undebug all
```

or

```
Router# no debug ip nat
```

## Common NAT Issues and Troubleshooting

### Issue 1: NAT Not Working

**Check**:

- Are inside/outside interfaces configured correctly?
- Is ACL permitting the correct addresses?
- Is there a route to the destination?
- Is the NAT pool exhausted (for dynamic NAT)?

**Commands**:

```
show ip nat translations
show ip nat statistics
show access-lists
show ip interface brief
```

### Issue 2: Some Hosts Can't Access Internet

**Possible Causes**:

- ACL not permitting those hosts
- NAT pool exhausted (dynamic NAT)
- No default route configured

### Issue 3: Return Traffic Not Working

**Possible Causes**:

- Missing or incorrect inside/outside interface designation
- Asymmetric routing
- Firewall blocking return traffic

### Issue 4: Inbound Connections Failing

**Solution**: Static NAT or port forwarding required for inbound connections to work.

## Port Forwarding (Static PAT)

Allows inbound connections to specific services on internal hosts.

**Configuration Example**:

```
! Forward external port 80 to internal web server
Router(config)# ip nat inside source static tcp 192.168.1.100 80 203.0.113.5 80

! Forward external port 443 to internal web server
Router(config)# ip nat inside source static tcp 192.168.1.100 443 203.0.113.5 443

! Forward external SSH (2222) to internal SSH (22)
Router(config)# ip nat inside source static tcp 192.168.1.10 22 203.0.113.5 2222
```

**Format**:

```
ip nat inside source static [tcp|udp] [local-ip] [local-port] [global-ip] [global-port]
```

## NAT Best Practices

1. **Use PAT for most scenarios** - Most efficient use of public IPs
2. **Use static NAT for servers** - Provides consistent inbound access
3. **Document your NAT configurations** - Complex setups can be confusing
4. **Monitor NAT table size** - Large tables can impact router performance
5. **Set appropriate timeouts** - Prevents table bloat
6. **Use descriptive pool names** - Makes troubleshooting easier

## Configuration Timeouts

NAT translations have timeouts to prevent table bloat:

**View current timeouts**:

```
Router# show ip nat statistics
```

**Modify timeouts**:

```
Router(config)# ip nat translation timeout [seconds]
Router(config)# ip nat translation tcp-timeout [seconds]
Router(config)# ip nat translation udp-timeout [seconds]
Router(config)# ip nat translation dns-timeout [seconds]
```

**Default Timeouts**:

- TCP: 86,400 seconds (24 hours)
- UDP: 300 seconds (5 minutes)
- ICMP: 60 seconds
- DNS: 60 seconds

## Comparison Table: Static vs Dynamic vs PAT

|Feature|Static NAT|Dynamic NAT|PAT|
|---|---|---|---|
|**Address Conservation**|Poor (1:1)|Moderate|Excellent (Many:1)|
|**Public IPs Required**|One per host|Pool of IPs|One or very few|
|**Inbound Connections**|Yes|No|Only with port forwarding|
|**Configuration Complexity**|Simple|Moderate|Simple to Moderate|
|**Best For**|Servers|Medium-sized networks|Most networks/home use|
|**Predictability**|High|Medium|Low|
|**Scalability**|Poor|Moderate|Excellent|

## Important CCNA Exam Points

### Key Concepts to Remember

1. **NAT conserves IPv4 addresses** by allowing private addresses to share public addresses
2. **Inside = your network, Outside = internet/external**
3. **Inside Local = private IP, Inside Global = public IP**
4. **Static NAT = one-to-one mapping**
5. **Dynamic NAT = pool-based automatic mapping**
6. **PAT = many-to-one using port numbers (keyword: overload)**
7. **PAT is the most common NAT type** in real-world deployments
8. **Port forwarding allows inbound connections** through PAT

### Configuration Keywords

- `ip nat inside` - Applied to internal interfaces
- `ip nat outside` - Applied to external interfaces
- `ip nat inside source static` - Static NAT command
- `ip nat pool` - Creates address pool for dynamic NAT
- `overload` - Enables PAT

### Common Exam Scenarios

1. Identify inside local, inside global, outside local, outside global from diagram
2. Configure static NAT for a server
3. Configure PAT for multiple internal hosts
4. Troubleshoot NAT using show commands
5. Calculate how many simultaneous translations dynamic NAT pool supports
6. Determine which NAT type to use for given scenario

## Practice Questions

1. **Q**: What command enables PAT using the IP address of interface g0/1? **A**: `ip nat inside source list 1 interface g0/1 overload`
    
2. **Q**: What type of NAT allows inbound connections to be initiated? **A**: Static NAT
    
3. **Q**: What is the inside global address? **A**: The translated public IP address that represents the inside host to the outside network
    
4. **Q**: Which NAT type uses port numbers to track connections? **A**: PAT (Port Address Translation) / NAT Overload
    
5. **Q**: What command shows active NAT translations? **A**: `show ip nat translations`
    

## Summary

NAT is essential for IPv4 address conservation and network security. For the CCNA exam, focus on:

- Understanding the terminology (inside/outside, local/global)
- Knowing when to use each NAT type
- Configuration commands for all three types
- Verification and troubleshooting commands
- Real-world application scenarios

PAT is by far the most common implementation due to its efficiency, but static NAT is crucial for servers needing inbound accessibility.
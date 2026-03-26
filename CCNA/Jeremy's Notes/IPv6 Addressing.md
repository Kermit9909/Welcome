

## EUI 64

### Global Unicast IP Addresses

	- Public addresses  (globally unique)
	- 2001:0DB8:8B00:0001::0001/64

### Unique Local IPv6 Addresses

	- Private addresses which ***cannot be used over the internet***
	- FD00::/7
	- Remember FD!!

### Link Local Addresses

	- Automatically generated on IPv6 enabled interfaces
	- R1(config-if)# ipv6 enable
	- FE80::/10

### Multicast Addresses

	- One source to multiple destinations (that have joined the specific multicast group)
	- IPv6 uses range FF00::/8
	- IPv6 doesn't use Broadcast but uses multicast instead

### IPv6 Multicast and IPv4 Multicast Addresses

### Must Memorize for IPv4:

- ✅ **224.0.0.1** - All hosts
- ✅ **224.0.0.2** - All routers
- ✅ **224.0.0.5** - OSPF routers
- ✅ **224.0.0.6** - OSPF DR/BDR
- ✅ **224.0.0.9** - RIPv2
- ✅ **224.0.0.10** - EIGRP

### Must Memorize for IPv6:

- ✅ **FF02::1** - All nodes
- ✅ **FF02::2** - All routers
- ✅ **FF02::5** - OSPFv3 routers
- ✅ **FF02::6** - OSPFv3 DR/BDR
- ✅ **FF02::9** - RIPng
- ✅ **FF02::A** - EIGRP for IPv6
- ✅ **FF02::1:FF00:0/104** - Solicited-node

## IPv6 Multicast Scopes - Quick Summary

|Scope|Name|Reach|Use Case|
|---|---|---|---|
|**FF01**|Interface-local|Single interface only|Loopback testing, same device|
|**FF02**|Link-local|Same subnet/link|Most common - routing protocols, neighbor discovery|
|**FF05**|Site-local|Same building/campus|Organization-wide services|
|**FF08**|Organization-local|Entire organization|Multi-site company networks|
|**FF0E**|Global|Internet-wide|Worldwide multicast applications|

![[Pasted image 20251206181619.png]]

### Anycast Addresses

	- Anycast is "one to one of many"

### Loopback Address

	- ::1
	- eq. 127.0.0.0/8 IPv4
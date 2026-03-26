

# Exam topic 3.5 : Describe the purpose of FHRP





## Purpose of  FHRP

- **First hop redundancy protocols** (**FHRP**) are a category of [networking protocols](https://en.wikipedia.org/wiki/Networking_protocol "Networking protocol") designed to protect the [default gateway](https://en.wikipedia.org/wiki/Default_gateway "Default gateway") used on a [subnetwork](https://en.wikipedia.org/wiki/Subnetwork "Subnetwork") by allowing two or more [routers](https://en.wikipedia.org/wiki/Router_\(computing\) "Router (computing)") to provide backup for that address. In the event of failure of an active router, the backup router will take over the address, usually within a few seconds.

- VIP - Virtual IP address

- Gratuitous ARP - ARP replies send without request ( this is done by the standby router to become ACTIVE router and change switches mac-address table )



## HSRP (Hot Standby Router Protocol)

- Cisco proprietary
- An ==ACTIVE== and ==STANDBY== router are elected
- Two versions:  Version 1 and Version 2 (IPv6 Support)
- Multicast IPv4 address:  ==v1=224.0.0.2; v2=224.0.0.102
- Virtual MAC address: ==v1= 000.0c07.acXX  v2=0000.0c9f.fXXX  (XX = group number)
- In a situation with multiple subnets/VLANS, you can configure a diff active and passive routers per each.


## VRRP (virtual router redundancy protocol)

- Open standard
- Uses ==MASTER== and ==BACKUP==
- Multicast IPv4 address:  ==224.0.0.18
- Virtual MAC: ==000.5e00.01XX (XX=group number)



## GLBP (Gateway Load Balancing Protocol)

- Cisco Proprietary
- **Load balances among multiple routers ==within a single subnet==
- An AVG (Active Virtual Gateway) is elected
- Up to four AVFs (Active Virtual Forwarders) are assigned by the AVG (AVG itself can be an AVF, too)
- Each AVF acts as the default gateway for a portion of the hosts in the subnet
- Multicast IPv4 address: ==224.0.0.102== 
- Virtual MAC address: ==0007.b400.XXYY==( XX=GLBP group number, YY=AVF number)



![[Pasted image 20251130140327.png]]



## Basic HSRP Configuration

### Router Configs:

## (config)# interface g0/0
## (config-if)# standby version 2

## (config-if)# standby (***group-number)
	- match standby numbers for routers, and its good to match with vlans

## (config-if)#  standby (***group number***) ip (***virtual IP)

## (config-if)# standby 1 priority (ex.200) - highest wins (not necessary for standby)

## (config-if)# standby 1 preempt  (restores original priority configs / only on active router)

### Show commands:  
## --- show standby


 













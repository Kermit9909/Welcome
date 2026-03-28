_________

## Classic STP

### Redundancy in Networks

- essential in network design
- must implement redundancy at every possible point in the network

### Broadcast storms

- Ethernet headers don't have TTL field.  The broadcast frames will loop around the network indefinitely.  If enough of these looped broadcasts accumulate in the network ,the network will be too congested for legitimate traffic to use the network .
- **Mac Address Flapping**- when frames with same source MAC address repeatedly arrive on different int, the switch is continuously updating the interface in its MAC address table.
### STP (Spanning Tree Protocol)

- Layer 2 redundancy
- ***IEEE 802.1D***
- STP prevents Layer 2 loops by placing redundant ports in a blocking state (disabling the int)
- These int act as backups if an active int fails
- Int in a blocking state only send or receive STP messages ( ***BPDUs = Bridge Protocol Data Units)
- This allows STP to create single paths preventing Layer 2 loops (automatically)
- STP-enabled switches send/receive **Hello BPDU** out of every int once every 2 seconds
- If a switch receives a **HELLO** it knows it is connected to another switch.
- Switches use one field in the STP BPDU ( ***the Bridge ID field*** ) to elect a ***Root Bridge***
- ***All ports on the ROOT BRIDGE are in a forwarding state, and other switches must have  a path to reach the root bridge
___________________________
|         ***Bridge ID***            |                          
___________________________
| Bridge Priority | MAC Address |
- - - - - - - - - - - - 
|       16 bits       |    48 bits         |

          ***Current Bridge ID***
|        4 bits        |       12 bits (VLAN ID)

____________________

***Lowest MAC Address will set Priority Bridge if Priority bits are the same***


## Holy Crap: Port Selection Process

1) One switch is elected as the root bridge.  All ports on the root bridge are designated ports (forwarding state).  Root bridge selection:
	a: Lowest bridge ID
2) Each remaining switch will select ONE of its int to be its **root port** (forwarding state).  Ports across from the root port are always **designated** ports.
	Root port selection:
	a) Lowest root cost
	b) Lowest neighbor bridge ID
	c) Lowest neighbor port ID
3) Each remaining collision domain will select ONE int to be a **designated port** (forwarding state).  The other port in the collision domain will be **non-designated** (blocking)
	Designated port selection:
	a) Interface on switch with lowest root cost
	b) Interface on switch with lowest bridge ID

### STP Root Cost

![[Pasted image 20260208143037.png]]
![[Screenshot 2025-11-08 170918.png]]![[Screenshot 2025-11-08 171249.png]]
## Classic Spanning Tree Port States

![[Pasted image 20260208154247.png]]



## Spanning Tree Timers

![[Pasted image 20260208154726.png]]
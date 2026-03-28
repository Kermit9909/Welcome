
## 802.11 Frame Format

![[Pasted image 20260124151730.png]]

* Frame Control - Provides information such as the message type and subtype
* Duration/ID - the time the channel will be dedicated for transmission of the frame
			* - identifier for the association (connection)
* Addresses - Up to four addresses can be present
	* Destination Address (DA): Final recipient fo the frame
	* Source address (SA): Original sender of the frame
	* Receiver address (RA): Immediate recipient of the frame
	* Transmitter Address (TA): Immediate sender of the frame
* Sequence control: Used to reassemble fragments and eliminate duplicate frames
* QOS Control: used to prioritize certain traffic
* HT (High Throughput) Control: added to 802.11 to enable High Throughput operations
	* 802.11n is known as "high throughput"
	* 802.11ac is know as "very high throughput"
* FCS (Frame Check Sequence) for errors detection*

## 802.11 Association Process

![[Pasted image 20260124154144.png]]

* Management: used to manage the BSS
	* Beacon
	* Probe request, probe response
	* Authentication
	* Association request, association response
* Control: used to control access to the medium (rf) and data frames.
	* RTS (Request to Send)
	* CTS (Clear to Send)
	* ACK
* Data: Used to send actual data packets*
## Three Main Wireless AP Deployment Methods:

1) Autonomous APs - self-contained systems that don't rely on a WLC (wireless LAN controller)
	1) Can be configured by console cable, telnet/ssh, http/https web connection (gui)
	2) Needs:
		1) Ip address for remote management 
		2) RF parameters (transmit power, channel, etc.)
		3) Security policies
		4) QOS rules
	3) No central monitoring or management of APs

![[Pasted image 20260124155359.png]]

## Lightweight APs

![[Pasted image 20260124160016.png]]

### CAPWAP UDP port 5246 Control
### CAPWAP UDP port 5247 Data Tunnel

![[Pasted image 20260124160335.png]]

![[Pasted image 20260124161821.png]]

## Lightweight AP Modes:

	*Local - default mode where AP offers a BSS (more multiple BSSs) for clients to associate with*
	
	*FlexConnect - Offers a BSS and allows the AP to locally switch traffic between the wired and wireless networks if the tunnels to the WLC go down*
	*Sniffer - The AP does not offer a BSS for clients.  It is used for capturing 802.11 frames and sending them to software like wireshark*
	
	*Monitor - Does not offer a BSS for clients. It is used for receiving 802.11 frames to detect rogue devices.  If such device is found it can send de-auth messages to disassociate the rogue device from AP
	
	*Rogue Detector - AP does not even use its radio. It listens to network traffic only, receives list of suspected rogue clients and AP MAC addresses from the WLC. Checks WLC wanted list to ARP messages and correlates potential rogue devices.
	
	*SE-Connect (Spectrum Expert Connect) - Also does not offer a BSS for clients. Uses RF spectrum analysis on all channels.  Sends info to software such as Cisco Spectrum Expert on a PC to collect and analyze the data*
	
	*Bridge/Mesh - Like autonomous APs Outdoor Bridge, this lightweight AP can be a dedicated bridge between sites, for example over long distances. A mesh can be made between the access points.
	*Flex plus Bridge - Adds FlexConnect function with Bridge/Mesh mode.  Allows wireless access points to locally forward traffic even if conectivity to the WLC is lost.*





## Lightweight vs. Autonomous

![[Pasted image 20260124160656.png]]

## FlexConnect

![[Pasted image 20260124172710.png]]


- **Local switching** - data traffic stays local, doesn't hairpin back to WLC through tunnel
- **Hybrid model** - control/management still tunneled to WLC via CAPWAP, but **data is switched locally** at the branch
- **WLC resilience** - if WLC connection fails, AP can continue operating in "standalone mode" using cached configs
- **Best for:** Branch offices, remote sites with WAN links to HQ where WLC resides

**Key FlexConnect Benefits:**

- Reduces WAN bandwidth (traffic doesn't traverse to HQ and back)
- Survives WLC failures (critical for remote sites)
- Lower latency for local resources (printers, file servers at branch)
- Can do local VLAN switching and apply ACLs at the branch switch

**Mental Model:**

- **Lightweight** = "dumb AP, smart controller" (everything through WLC)
- **FlexConnect** = "smart AP when needed" (data local, management central)

## Cloud-Based AP

### Cisco Meraki!!!!

![[Pasted image 20260124174524.png]]
![[Pasted image 20260124174604.png]]


## WLC Deployment Models

### Unified WLC

![[Pasted image 20260124174856.png]]


### Cloud-Based WLC

![[Pasted image 20260124175006.png]]


### Embedded WLC

![[Pasted image 20260124175117.png]]

### Cisco Mobility Express WLC

![[Pasted image 20260124175254.png]]
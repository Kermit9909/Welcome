
## The TCP/IP Model

There are different models of representation for internetworking. After the OSI model, comes the TCP/IP model in terms of popularity. The TCP/IP model, which is loosely outlined in RFC 1122 as a four-layer model, does not map directly to the OSI model. RFCs are Requests for Comments, which are documents proposing network protocols and services.

**Table 1-3: The OSI and TCP/IP models**

|**OSI**|**TCP/IP**|
|---|---|
|Application|Application|
|Presentation|
|Session|
|Transport|Transport/Host-to-Host|
|Network|Internet|
|Data Link|Network Access/Network Interface|
|Physical|
### Example A: Web browsing (TCP, reliable) in TCP/IP Model

1. **Application Layer**
    
    - You type a URL into your browser.
        
    - HTTPS protocol formats the request.
        
2. **Transport Layer**
    
    - TCP segments the data.
        
    - Adds source port (e.g., 50000) and destination port (443).
        
    - Ensures reliable delivery with sequencing and acknowledgments.
        
3. **Internet Layer**
    
    - IP header is added with source and destination IP addresses.
        
    - Routing decisions are made here.
        
4. **Network Access Layer**
    
    - MAC addresses (source/destination) are applied.
        
    - Data is turned into electrical signals, light pulses, or radio waves.
        
    - Sent across the local network toward the destination.

|   |
|---|
|Application|
|Transport|
|Network|
|Data Link|
|Physical|

The Cisco Network Academy course book refers to the TCP/IP model as having four layers (see Mark A. Dye, Rick McDonald, and Antoon W. Rufi. Network Fundamentals: CCNA Exploration Companion Guide. 2007. ISBN 1-58713-208-7), while Douglas E. Comer’s highly regarded textbook Internetworking with TCP/IP: Principles, Protocols and Architecture (2005. Pearson Prentice Hall. ISBN 0-13-187671-6) refers to the TCP/IP model as having five layers.

### TCP/IP Application Layer

The application layer in the TCP/IP model covers the functionality of the :
#### - session, 
#### - presentation
####  -application layer

in the OSI model. Various protocols can be used in this layer, including:

- **SMTP, POP3** – used to provide e-mail services
- **HTTP** – World Wide Web browser content delivery protocol
- **FTP** – used in file transfer
- **DNS** – used in domain name translation
- **SNMP** – network management protocol
- **DHCP** – used to automatically assign IP addresses to network devices
- **Telnet** – used to manage and control network devices

#### ***The TCP/IP application layer does not provide the actual services; it does, however, define the services the applications require.
#### An example would be your web browser requesting HTTP services from the network. The application layer would provide the interface for this to take place.

### TCP/IP Transport/Host-to-Host Layer

The protocols that operate at and control the transport/host-to-host layer are specified in this layer. The TCP/IP transport layer controls the end-to-end logical connection between two devices. Both the TCP/IP transport and Internet layer demonstrate considerable differences compared to the corresponding OSI layers. The transport layer is based on two protocols:

- **TCP** – This provides connection-oriented communication. This means the path on which the data travels in the network is reliable because the endpoints establish a synchronized connection before sending the data. Every data packet is acknowledged by the receiving host and includes a Checksum field to check for error detection. FTP is an example of a protocol that uses TCP.
- **UDP** – This provides unreliable, connectionless communication between hosts. Unlike TCP, UDP does not check the segments that arrive at the destination to ensure that they are valid and in the proper order. This means that the integrity verifications and the error connection process will occur in the application layer. In fact, unlike TCP, UDP doesn’t set up a connection between the sender and the recipient. On the other hand, UDP has a smaller overhead than TCP because the UDP header is much smaller. TFTP is an example of a protocol that uses UDP.

[![UDP and TCP segment fields](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-23.jpg)](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-23.jpg)

- Port number take values up to 65535
- Well-know ports 0-1023
- Registered ports 1024-49151
- Dynamic Ports (auto-assign by net dev) 49152-65535
### TCP/IP Internet/Network Layer

The Internet layer in the TCP/IP model corresponds to OSI layer 3 (network layer). This layer is responsible for routing data, including addressing and packet format, and uses the following protocols:

### IPv4 Packet  (32 bits)

![[1-25-1024x910.jpg]]


### IPv6 Packet (128 bits)

![[1-26-1024x910.jpg]]


### TCP/IP Network Access Layer

**The network access layer maps to the OSI DATALINK LAYER  and PHYSICAL LAYER, and it has the same functionality as those layers.

A common protocol used at the network access layer is ARP (Address Resolution Protocol), which requests the MAC addresses of a host with a known IP address. This works by sending a broadcast message to all the hosts on a subnet and asking for the MAC address of the host that has the IP address. The host with that IP address responds with its MAC address and the sender caches this in its memory for a period of time. Once the MAC address is known, it is used as a destination address in the frames sent in that specific direction.





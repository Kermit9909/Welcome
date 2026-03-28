________________________

### Summary—The OSI Model

The OSI model can be summarized as shown in Table 1-2 below:

**Table 1-2: The OSI model summarized**

|   |   |   |   |   |
|---|---|---|---|---|
|**Layer**|**Encapsulation**|**Function**|**Services**|**Device**|
|7 Application|Data|Establishes availability of resources|FTP, SMTP, Telnet, POP3|Hosts/Firewalls|
|6 Presentation|Data|Compression, encryption, and decryption|JPEG, GIF, MPEG, ASCII|Hosts/Firewalls|
|5 Session|Data|Establishes, maintains, and terminates sessions|NFS, SQL, RPC|Hosts/Firewalls|
|4 Transport|Segment|Establishes end-to-end connection; uses virtual circuits, buffering, windowing, and flow control|TCP, UDP|Hosts/Firewalls|
|3 Network|Packet|Determines best path for packets to take|IP|Router|
|2 Data Link (LLC, MAC)|Frame|Transports data across a physical connection; error detection|Frame Relay, PPP, HDLC|Switch/Bridge|
|1 Physical|Bits|Puts data onto the wire||Hub/Cables|

**FOR THE EXAM**: A thorough knowledge of the OSI model is vital for the exam. Know each level, encapsulation formats, and which device sits where.

Broadcast Domain
Collision Domain

Full Duplex on switch no collision domain / half duplex - yes


## Cisco Products

#### Hub
- all ports are  = ONE collision domain

#### Switches
-  every port is a collision domain

2960 Switch

#### Routers
-  segments broadcast domains
	- every port on a router is a separate broadcast     domain

1900 Series

## Open Systems Interconnection (OSI) Model

Advantages of using the OSI model include the following:

-  Allows different vendors’ equipment to work together
- Allows different types of network hardware and software to communicate
- A change made in one layer does not affect any of the other layers

## OSI Model Layers
	7 Application Layer
	6 Presentation Layer
	5 Session Layer
	4 Transport Layer
	3 Network Layer
	2 Data Link Layer
	1 Physical


### ***Remember !!!!

### ***"All People Seem To Need Data Processing"

### Encapsulation  Process 

[![Five steps of data encapsulation](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-10-scaled.jpg)](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-10-scaled.jpg)


**Order of Data Encapsulation

Data > Segment > Frame > Bit
***" Don't Some People Fry Bacon"


- **Encapsulation** on the way down.
    
- **Decapsulation** on the way up.


### 7) Application Layer

- It establishes whether the destination is available to communicate and determines whether sufficient resources are available to do so.
	- HTTP/HTTPS (WWW)
	- SMTP/POP3 (email)
	- File Transfer (FTP)
***Question:  How would you test to see if all seven OSI Layers are working on your network?

***Answer: You could SSH or FTP to another host. 


### 6) Presentation Layer 

### Presentation Layer

The function of the presentation layer is to present data to the application layer. It converts coded data into a format the application layer can understand.

***It is also responsible for data encryption, data decryption, and, finally, data compression.

The presentation layer converts many multimedia functions for the application layer, including:

- **JPEG (Joint Photographic Experts Group)** – a widely used image format
- **MPEG (Moving Pictures Experts Group)** – the format used for video compression and coding
- **QuickTime** – manages audio and video for Macs and iPads
- **ASCII (American Standard Code for Information Interchange)** – the standard for


### 5) Session Layer

Think of the Session Layer as the **“conversation manager.”**

- It **sets up** a dialog between two applications.
    
- It **keeps the streams of data separate** so they don’t get mixed.
    
- It **synchronizes and maintains state** (who’s talking, who’s listening, what point in the exchange you’re at).
    
- It **tears down the session** gracefully when done.
    

It’s not about the content itself (that’s Application Layer), and not about reliable delivery (that’s Transport). It’s the **coordinator** in between.


### 4) Transport Layer
- In this layer, end-to-end data transport services are provided to the upper OSI layers. The transport layer takes data from the upper layers, breaks it into smaller units called segments, and adds logical transport information in the header  **(TCP / UDP)   

### TCP/IP

![[1-13-1024x263.webp]]

Data transfer using TCP as the transport protocol is considered to be reliable. This means that there is a guarantee that the data sent will reach the intended destination. This is accomplished by using three methods:

1. Flow control
2. Windowing
3. Acknowledgments

#### Flow Control

[![Flow control](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-15.jpg)](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-15.jpg)

#### Windowing

The TCP window is the amount of data that can be sent before an acknowledgment is required from the receiver. The sender and receiver agree on the window size, and this can be scaled up and down as required.

[![Windowing](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-16.jpg)](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-16.jpg)
#### Acknowledgments

Acknowledgments are messages indicating the successful receipt of TCP segments. If a sender does not receive acknowledgments for the segments sent after a certain period, then it knows there is something wrong.

[![Acknowledgments](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-17.jpg)](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-17.jpg)

UDP, on the other hand, is a connectionless protocol. In other words, it does not care about sequencing or acknowledgments, and it does not have all the fancy mechanisms that TCP uses to ensure that its segments reach their destination safely. This means that applications using UDP must be responsible for their own reliability.


### 3) Network Layer

The role of the network layer is to determine the best path or route for data to take from one network to another. Data from the session layer are assembled into packets at this layer, and this is where the end-to-end delivery of packets occurs.

Because networks need some way of identifying themselves, logical addressing also takes place at the network layer. The most popular form of network addressing today is IP addressing using IPv4 or IPv6.

**Table 1-1: Router B best-path routing table**

|   |   |   |
|---|---|---|
|Destination Network|Next Hop|Number of Hops Away|
|Network 1|None|Directly connected|
|Network 2|None|Directly connected|
|Network 3|Router A|1|
|Network 3|Router C|1|
|Network 4|Router A|1|
|Network 4|Router C|2|

The best path is decided at the network layer. Each router stores a table of which networks are directly connected and how to get to the networks that are not. You can see the routing table for Router B in Table 1-1 above.

[![Best path is decided at the network layer](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-18.png)](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-18.png)

### 2) Data Link Layer

The data link layer is divided into two sublayers—LLC and MAC—as shown in Figure 1.20 below:

[![The data link layer](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-20.jpg)](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-20.jpg)

**FIG 1.20 – The data link layer**

The data link layer takes packets from the network layer and divides them into smaller units known as frames. Frames are then transported across a physical medium (i.e., wires). The data link layer has its own way of addressing known as hardware addressing. While the network layer determines where networks are located, the data link layer determines where hosts are located on a particular network.

#### Logical Link Control Sublayer (IEEE 802.2)

The LLC sublayer interfaces with the network layer and provides Service Access Points (SAPs); these allow the MAC sublayer to communicate with the upper layers of the OSI model.

#### Media Access Control Sublayer (IEEE 802.3)

The MAC layer directly interfaces with the physical layer. This is where the physical address of the interface or device is stored. A MAC address is a 48-bit address expressed as 12 hexadecimal digits. This address identifies both the manufacturer of the device and the specific host.

## ** **FOR THE EXAM:** Because you are using packets at the network layer and frames at the data link layer, remember that you:
## "ROUTE" PACKETS 
## "FORWARD" FRAMES.**

### Physical Layer

The physical layer takes frames from the data link layer and converts them into bits. The physical layer has to use bits (binary digits) since data on a wire can be sent only as a pulse of electricity or light—that is, only as one of two values, either a 1 or a 0.

The physical layer deals with the physical characteristics of the medium, such as the number of pins and their uses. Physical layer specifications include IEEE 802.3, FDDI, Ethernet, RJ-45, and many more.

Hubs operate at the physical layer of the OSI model. Hubs take the bits, strengthen the signal if it has been degraded, and send them out to every device connected to the ports.

[![Hubs and repeaters strengthen the signal on the wire](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-22.png)](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-22.png)

**FIG 1.22 – Hubs and repeaters strengthen the signal on the wire**







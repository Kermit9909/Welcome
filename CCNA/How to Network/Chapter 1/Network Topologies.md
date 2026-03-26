_____________

### Cisco Network Design Considerations

![[1-48-1024x663.webp]]



### Top-Down Approach

[![Cisco top-down approach to design](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-49.jpg)](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-49.jpg)

**FIG 1.49 – Cisco top-down approach to design**

As Figure 1.49 shows, the design planning sub-projects include:

- Choosing the technology, acquisitioning, and provisioning
- Physical topology design (placing the design at different layers)
- Addressing the design scheme, including NAT solutions
- Routing selection and design
- Quality of Service design (traffic management)
- Security design
- IP Multicast design (for video and audio streaming)
- IPv6 provisioning design

### Topologies


### Point-to-Point

Point-to-point networks are a direct link between two devices. They are most often used in WAN topologies such as T1/E1.

### A common exam question asks about the advantages of this topology, and one advantage is that such a link usually requires only two IP addresses (/30 address).

[![Point-to-point link](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-50.jpg)](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-50.jpg)


### Point-to-Multipoint

Point-to-multipoint networks are very popular today and are commonly used in wireless networks. With this topology, multiple devices communicate with a central device/interface. End devices may not necessarily be able to communicate, which means that extra configuration commands may have to be added to overcome this issue.

You will learn more about configuring routing protocols such as EIGRP over point-to-multipoint networks in the CCNP exams.

[![Point-to-multipoint topology](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-51.jpg)](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-51.jpg)

**FIG 1.51 – Point-to-multipoint topolog**y


### Ring

Ring networks were common in the 1980s and 1990s when token ring was the typical topology for LANs. The name stems from the fact that all network nodes are connected in a ring fashion. One advantage is that if one node fails, a connection is still possible. If the router fails, however, then the entire network will experience an outage. The ring topology is still used in Metro Area Networks but with dual rings for redundancy.

[![Ring topology](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-52.jpg)](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-52.jpg)


### Star

The star topology is the most commonly used topology in modern networks. It may not look like a star when you see it racked up but, in this topology, all nodes directly connect to a central device (usually a switch). The star topology is used in Ethernet networks.

[![Star topology](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-53.jpg)](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-53.jpg)


### Bus

The bus topology was used in early implementations of Ethernet with coaxial cables. These were thick wires that had to be physically pierced and were notoriously difficult to work with and troubleshoot. A break in a cable would bring the entire network down.

[![Bus topology](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-54-scaled.jpg)](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-54-scaled.jpg)


## WAN-Specific

### WAN-specific

There are a few options when it comes to the WAN topology, and there may be some limitations depending on where in the world a company is based and what their service providers can offer.

Options includes hub-and-spoke, full-mesh, and partial-mesh, among others. The full-mesh topology is the most fault-tolerant since there is a connection from every device to every other device. As shown in Figure 1.55 below, full-mesh requires each node to be connected to every other node:

[![Full-mesh](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-55-scaled.jpg)](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-55-scaled.jpg)

**FIG 1.55 – Full-mesh**

If you want to work out the number of connections required, the formula is n*(n-1)/2 connections, so 5 nodes = 10 connections (5 x 4 /2 = 10).

The hub-and-spoke topology is shown in Figure 1.56 below:

[![WAN hub-and-spoke topology](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-56-scaled.jpg)](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-56-scaled.jpg)

**FIG 1.56 – WAN hub-and-spoke topology**

Hybrid topologies vary depending on a company’s needs. They can combine mesh, partial-mesh, bus, star, point-to-multipoint, etc., and they can grow over time if requirements change. Figure 1.57 below shows an example of a hybrid topology:

[![Hybrid topology](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-57.jpg)](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-57.jpg)

**FIG 1.57 – Hybrid topology**


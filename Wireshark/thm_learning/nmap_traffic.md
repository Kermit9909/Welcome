
# Wireshark: Nmap Traffic
Date: 3/29/2026

## Nmap Scans

    - TCP connect scans
    - SYN scans
    - UDP scans

 
## Global search. 	

        - tcp
        - udp

### Bit position:  7    6    5    4    3    2    1    0
### Power of 2:   128   64   32   16    8    4    2    1
### Flag:          -    -   URG  ACK  PSH  RST  SYN  FIN

    Only SYN flag.  |  tcp.flags == 2

    SYN flag is set. The rest of the bits are not important. |  tcp.flags.syn == 1

	Only ACK flag. | tcp.flags == 16

    ACK flag is set. The rest of the bits are not important. | tcp.flags.ack == 1

	Only SYN, ACK flags. | tcp.flags == 18

    SYN and ACK are set. The rest of the bits are not important. |  (tcp.flags.syn == 1) and (tcp.flags.ack == 1)

	Only RST flag. | tcp.flags == 4

    RST flag is set. The rest of the bits are not important. |  tcp.flags.reset == 1

	Only RST, ACK flags. | tcp.flags == 20

    RST and ACK are set. The rest of the bits are not important. |  (tcp.flags.reset == 1) and (tcp.flags.ack == 1)

	Only FIN flag |  tcp.flags == 1

    FIN flag is set. The rest of the bits are not important.  tcp.flags.fin == 1

##  TCP Connect Scan in a nutshell: nmap -sT

    Relies on the three-way handshake (needs to finish the handshake process).
    Usually conducted with nmap -sT command.
    Used by non-privileged users (only option for a non-root user).
    Usually has a windows size larger than 1024 bytes as the request expects some data due to the nature of the protocol.

## SYN Scan in a nutshell: nmap -sS

    Doesn't rely on the three-way handshake (no need to finish the handshake process).
    Usually conducted with nmap -sS command.
    Used by privileged users.
    Usually have a size less than or equal to 1024 bytes as the request is not finished and it doesn't expect to receive data.

## UDP Scans: nmap -sU

    Doesn't require a handshake process
    No prompt for open ports
    ICMP error message for close ports
    Usually conducted with nmap -sU command.

The ICMP Type/Code System
ICMP messages use a two-number system — Type is the broad category, Code is the specific reason:
3 - Destination Unreachable
8 - Echo Request (ping)0Echo Reply (pong)
11 - Time Exceeded (TTL expired)

Type 3 alone covers a whole family of "can't reach" messages. The Code narrows it down:
0 - Network Unreachable
1 - Host Unreachable
2 - Protocol Unreachable
3 - Port Unreachable
9 - Network Admin Prohibited
10 - Host Admin Prohibited

icmp.type==3 and icmp.code==3 (Show Nmap UDP port scan icmp reponses)





## Q and A

**What is the total number of the "TCP Connect" scans?** 1000
tcp.flags.syn==1 and tcp.flags.ack==0 and tcp.window_size > 1024
***Why:*** Nmap's fingerprint is partly visible in **HOW** it constructs packets, not just the flags it sets.
**Which scan type is used to scan the TCP port 80?**
TCP Connect
**How many "UDP close port" messages are there?**
1083
***Method:*** icmp.type==3 and icmp.code==3
**Which UDP port in the 55-70 port range is open?**
68
***Method:*** udp.port in {55..70} > looked for the port did not send icmp back






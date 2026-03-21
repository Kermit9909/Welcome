
# Filtering Traffic In Wireshark

## :shark: Common Filters


Filter Type | Display Filter
-|- 
IPv4 Address                 | ip.addr==10.0.0.1
IPv4 Source / destination    | ip.src==10.0.0.1 (ip.dest==)
IPv4 Range (Subnet)          | ip.addr==10.0.0.0/24
TCP Port                     | tcp.port==80
TCP SYNs                     | tcp.flags.syn==1




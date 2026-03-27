
## Quiz Questions

### Lab 1 - Hands-On with Wireshark

### Questions for this assignment

    How many packets were captured in this trace file?
    2186

    What protocol does packet number 8 contain? (The highest-layer protocol)
    https

    If you just installed Wireshark for the first time, what is the name of the profile you are using? (bottom right corner)
    default

    Look at packet number one - what is the source IP address in this packet?
    192.168.56.102

    What is the source TCP port in this same packet?
    39294

    What TCP flag is set in this packet?
    SYN (0x002)

    What is the frame number of the next packet in this TCP conversation?
    6

    Can you set a filter for this TCP conversation? How many packets do you get?
    51

### Lab 2 - Configuring the Wireshark Interface

### Questions for this assignment

    1. Add a coloring rule that will make your tcp FIN packets blue. What filter will you use to do that?

    A: tcp.flags.fin==1

    2. Select packet number 1. Can you find the TCP segment length? Add this value as a column. Enter "done" in the answer field below when finished.

    A: Answer

    3. It would be nice to have a button that quickly filters for all TCP Errors. See if you can find the TCP Retransmission we were looking at earlier. How can you filter for all TCP errors in the trace file? What is this filter?

    A: tcp.analysis.flags 

    4. Add the TCP Errors filter as a button in this profile. Enter "done" below when finished.

    A: Done

    5. It can be a little overkill to see timestamps all the way to the nanosecond. Using the View | Time Display Format menu option, can you see how to configure Wireshark to only display to the microsecond? Make this change in this profile and type "done" below.

    A: Done


## Lab 3 - Display Filters

Download the trace file that goes along with this assignment and use it to answer the associated questions. For most questions, you will need to set a filter and provide the number of packets that meet it.

Questions for this assignment

1. How many DNS packets are in the trace file?
228

2. How many DNS packets contain the word "Udemy"? (Regardless of case)
20

3. How many HTTP packets are in the pcap?
66
4. Set a filter for TCP port 80. How many packets meet that filter?
211
5. How many packets are in the top IP conversation? Set a filter for this conversation.
406
6. In the top IP conversation, how many packets have the word "Udemy", regardless of case?
3
7. How many packets have the SYN bit set?
146
8. How many TCP Resets are in the pcap?
9
9. How many TCP SYN/ACKs are in the pcap?
73
10. Are any SYN/ACKs coming from the 10.0.2.15 station? Y/N?
No.










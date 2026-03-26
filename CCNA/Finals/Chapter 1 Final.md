
## End of Chapter Questions

Please visit [www.howtonetwork.com/ccnasimplified](https://www.howtonetwork.com/ccnasimplified) to take the free Chapter 1 exam.

## Chapter 1 Labs

### Lab 1: Basic Lab – Router Modes and Commands

There is no physical topology for this lab. Just use any Cisco router.

#### Purpose

Any person new to configuring Cisco routers needs to feel comfortable navigating around the various router features and modes. This lab will be a great icebreaker for a budding CCNA. We cover how to use a console cable with a router later (if you are a beginner), so follow those steps before you start or come back to this lab later if you wish. It will still be here waiting for you.

Your output and interfaces may differ from mine if you are using a different model and IOS release.

#### Lab Objectives

1. Connect to the console port.
2. Enter privileged mode (enable mode).
3. Enter global configuration mode (config mode).
4. Enter the interface configuration mode.
5. Enter the routing configuration mode (router mode).
6. Exit to privileged mode.
7. Execute some useful commands.
8. Exit to user exec mode.
9. Examine interface statistics.
10. Change router hostname.

#### Lab Walk-through

1. When connecting to the console of the router, you will typically see the following message. Always type no if asked if you want to enter System Configuration Dialog:

_— System Configuration Dialog —_

_Continue with configuration dialog? [yes/no]: no_

_Press RETURN to get started!_

_Router con0 is now available_

As instructed, you simply need to press the Enter key and enter the first mode of the router, user exec mode:

_Router>_

2. Now you are in user exec mode. Next, enter privileged mode, or enable mode as it is more commonly known. To do this, type:

_Router>enable_

You will now be presented with a new prompt that has a hash/pound (#) sign instead of the greater than (>) sign:

_Router>enable_

_Router#_

Enable mode is used to perform all the show and debug commands, which will be explained later in the lab.

3. The next mode to enter is global configuration mode, or config mode as it is more commonly known. To enter config mode, type:

_Router#config terminal_

As you will soon learn, all the commands in the Cisco IOS (operating system) can be abbreviated; for example, you could have entered:

_Router#conf t_

If you just type config and press Enter, you will receive the following output:

_Router#config_

_Configuring from terminal, memory, or network [terminal]?_

As you will see, terminal is the default (indicated by the square brackets []), so you can simply press Enter to go into config or privileged mode.

4. Once in config mode, you will be prompted with the following message:

_Router#config terminal_

_Enter configuration commands, one per line. End with Ctrl+Z._

_Router(config)#_

This is telling you that when you have finished in config mode, press the Ctrl+Z keys together to exit.

Once in config mode, you will notice that the prompt has changed again, this time from Router# to Router(config)#, indicating that you are in config mode. There are sublayers to config mode, but we are only interested in two of them, the first being interface configuration mode. First, you need to know which interfaces you have available:

_Router#show ip interface brief_

_Interface  IP-Address  OK?  Method Status            Protocol_

_Fa0/0      unassigned  YES  unset  administratively down down_

_Fa0/1      unassigned  YES  unset  administratively down down_

I have F0/0 and F0/1 available on my router. Your options may differ.

_Router(config)#interface FastEthernet0/0_ – **Or use Loopback 0 if your router does not have an Ethernet interface**

_Router(config-if)#_

If you are not sure which interfaces you have on your router, enter the _show ip interface brief_ command at the Router# prompt. If you do not have an Ethernet interface, replace the command above with interface Loopback 0.

You will see that the prompt has changed again: the (config-if) tells you that you are now in interface configuration mode. If you aren’t sure what to type, then enter a question mark (?) at the end of what you are typing.

_Router(config)#interface ?_

_Dot11Radio        Dot11 interface_

_Ethernet          IEEE 802.3_

_FastEthernet      FastEthernet IEEE 802.3_

_GigabitEthernet   GigabitEthernet IEEE 802.3z_

_Loopback          Loopback interface_

_Serial            Serial_

_Tunnel            Tunnel interface_

_Virtual-Template  Virtual Template interface_

_Vlan              Catalyst Vlans_

_range             interface range command_

_Router(config)#interface FastEthernet0/0_

_Router(config-if)#_

5. Another sublayer of config mode is the router configuration mode:

_Router(config-if)#exit_

_Router(config)#router rip_

_Router(config-router)#_

When you exit from interface configuration mode and type router rip, you enter router configuration mode. You can see that the prompt has changed again to reflect this.

6. To exit config mode and go back to privileged (enable) mode, you simply need to type:

_Router(config-router)#^Z_ – **Hold down the Ctrl and Z keys (together)**

_Router#_

When you do this, you will get the following message displayed after a few seconds:

_%SYS-5-CONFIG_I: Configured from console by console_

_Router#_

7. Now that you are back in enable mode, you can use some useful show commands. The common ones to use are shown below:

_Router#show ip interface brief_

_Interface  IP-Address   OK?  Method Status           Protocol_

_Fa0/0      unassigned   YES  unset  administratively down down_

_Fa0/1      unassigned   YES  unset  administratively down down_

_Router#_

The benefit of this command is that it shows the status and IP addresses of all the interfaces in a table. Do not worry if your output is different from the one above.

The next command that is useful is show running-configuration, which will display the current configuration (yours may look different from the one below). The output will be cut short so that you can see it all on your monitor. You can press the Enter key to go through it line by line or press the space bar to scroll up a page at a time:

_Router#show running-config_

Or:

_Router#show run_ – **Abbreviated command**

_Building configuration…_

_Current configuration: 489 bytes_

_!_

_version 15.1_

_no service timestamps log datetime msec_

_no service timestamps debug datetime msec_

_no service password-encryption_

_!_

_hostname Router_

_!_

_spanning-tree mode pvst_

_!_

_interface FastEthernet0/0_

_no ip address_

_duplex auto_

_speed auto_

_shutdown_

_!_

_interface FastEthernet0/1_

_no ip address_

_duplex auto_

_speed auto_

_shutdown_

_!_

_interface Vlan1_

_no ip address_

_shutdown_

_!_

_ip classless_

_!_

_line con 0_

_!_

_line aux 0_

_!_

_line vty 0 4_

_login_

_!_

_End_

Type _show version_ (or _show ver_ for short):

_Router#show ver_

_Cisco IOS Software, C2900 Software (C2900-UNIVERSALK9-M), Version 15.1(4)M4, RELEASE SOFTWARE (fc2)_

_Technical Support: http://www.cisco.com/techsupport_

_Copyright (c) 1986-2012 by Cisco Systems, Inc._

_Compiled Thurs 5-Jan-12 15:41 by pt_team_

_ROM: System Bootstrap, Version 15.1(4)M4, RELEASE SOFTWARE (fc1)_

_cisco2911 uptime is 1 minutes, 35 seconds_

_System returned to ROM by power-on_

_System image file is “flash0:c2900-universalk9-mz.SPA.151-1.M4.bin”_

_Last reload type: Normal Reload_

_If you require further assistance please contact us by sending email to export@cisco.com._

_Cisco CISCO2911/K9 (revision 1.0) with 491520K/32768K bytes of memory._

_Processor board ID FTX152400KS_

_3 GigabitEthernet interfaces_

_DRAM configuration is 64 bits wide with parity disabled._

_255K bytes of non-volatile configuration memory._

_249856K bytes of ATA System CompactFlash 0 (Read/Write)_

_Configuration register is 0x2102_

To exit to user exec mode, you simply need to type disable or exit:

_Router#disable_

_Router>enable_

_Router#_

8. You can also examine the interface statistics with the show interface x command:

_Router#show interface f0/0_

_FastEthernet0/0 is administratively down, line protocol is down (disabled)_

_Hardware is Lance, address is 0060.5cd9.8001 (bia 0060.5cd9.8001)_

_MTU 1500 bytes, BW 100000 Kbit, DLY 100 usec,_

_reliability 255/255, txload 1/255, rxload 1/255_

_Encapsulation ARPA, Loopback not set_

_ARP type: ARPA, ARP Timeout 04:00:00,_

_Last input 00:00:08, output 00:00:05, output hang never_

_Last clearing of “show interface” counters never_

_Input queue: 0/75/0 (size/max/drops); Total output drops: 0_

_Queueing strategy: fifo_

_Output queue :0/40 (size/max)_

_5 minute input rate 0 bits/sec, 0 packets/sec_

_5 minute output rate 0 bits/sec, 0 packets/sec_

_0 packets input, 0 bytes, 0 no buffer_

_Received 0 broadcasts, 0 runts, 0 giants, 0 throttles_

_0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort_

_0 input packets with dribble condition detected_

_0 packets output, 0 bytes, 0 underruns_

_0 output errors, 0 collisions, 1 interface resets_

_0 babbles, 0 late collision, 0 deferred_

_0 lost carrier, 0 no carrier_

_0 output buffer failures, 0 output buffers swapped out_

_Router#_

9. You can change the hostname of the router by doing the following:

_Router#config_

_Configuring from terminal, memory, or network [terminal]?_ – **Press Enter**

_Enter configuration commands, one per line.  End with CNTL/Z._

_Router(config)#hostname RouterA_

_RouterA(config)#_

10. Now reload the router: Do not save any changes.

_Router#reload_

### Lab 2: ARP, CDP, Ping, and Telnet Lab

The physical topology is shown in Figure 1.58 below. Connect two routers with a crossover cable or with a switch.

[![ARP, CDP, ping, and telnet lab](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-58.jpg)](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-58.jpg)

**FIG 1.58 – ARP, CDP, ping, and telnet lab**

#### Lab Exercise

Your task is to configure the network referring to Figure 1.58 above to check for an ARP entry and a CDP neighbor, and to test the ping command and the telnet command. We are using Loopback interfaces here, which only exist logically. They are a perfect way to test routing and access lists without having to plug in extra hosts and cables.

Please note that if your interfaces aren’t numbered F0/0, you will need to swap the interface ID with what you do have. Issue a show ip interface brief command to see what you have available. We will cover some of the commands here, such as static routing, which will be explained in later sections. Just copy them for now.

#### Purpose

This lab explores some TCP and CDP fundamentals. ARP issues are very common, and the capacity to check ARP entries will be very useful to you in your career as a Cisco engineer.

#### Lab Objectives

1. Use the IP addressing scheme depicted in Figure 1.58 above. We are using Ethernet interfaces connected by a crossover cable or a switch for this lab.
2. Set Telnet access for the router to use the local login permissions for username banbury and the password ccna.
3. Configure the enable password to be cisco.
4. Check the ARP entry on Router A. Ping Router B and check the ARP entry again.
5. Check CDP neighbor details.
6. Telnet from Router A to Router B.

#### Lab Walk-through

1. To set the IP addresses on an interface, you will need to do the following:

_Router#config t_

_Router(config)#hostname RouterA_

_RouterA(config)#interface FastEthernet0/0_

_RouterA(config-if)#ip address 10.0.0.1 255.0.0.0_

_RouterA(config-if)#no shutdown_

_RouterA(config-if)#interface Loopback0_

_RouterA(config-if)#ip address 172.16.1.1 255.255.0.0_

_RouterA(config-if)#interface Loopback 1_

_RouterA(config-if)#ip address 172.20.1.1 255.255.0.0_

_RouterA(config-if)#^Z_

_RouterA#_

Router B:

_Router#config t_

_Router(config)#hostname RouterB_

_RouterB(config)#_

_RouterB(config)#interface FastEthernet0/0_

_RouterB(config-if)#ip address 10.0.0.2 255.0.0.0_

_RouterB(config-if)#no shutdown_

_RouterB(config-if)#interface Loopback0_

_RouterB(config-if)#ip address 172.30.1.1 255.255.0.0_

_RouterB(config-if)#interface Loopback1_

_RouterB(config-if)#ip address 172.31.1.1 255.255.0.0_

_RouterB(config-if)#^Z_

_RouterB#_

2. To set Telnet access, you need to configure the VTY lines to allow Telnet access. You first need to check how many Telnet/VTY lines you have as each model differs, as does GNS3. To do this, type (in configuration mode):

_RouterA(config)#line vty 0 ?_

_<1-903> Last Line number_

_<cr>_

_RouterA(config)#line vty 0 903_ – **Enters the VTY line configuration**

_RouterA(config-line)#login local_ – **This will use local  usernames and** **passwords for Telnet access**

_RouterA(config-line)#exit_ – **Exit the VTY config mode**

_RouterA(config)#username banbury password ccna_ – **Creates** **name and password for Telnet access (login local)**

Router B:

_RouterB(config)#line vty 0 903_

_RouterB(config-line)#login local_

_RouterB(config-line)#exit_

_RouterB(config)#username banbury password ccna_

3. To set the enable password, do the following:

_RouterA(config)#enable secret cisco_ –  **Sets the enable password** **(encrypted)**

Router B:

_RouterB(config)#enable secret cisco_

4. To configure a default route, there is one simple step (in configuration mode):

_RouterA(config)#ip route 0.0.0.0 0.0.0.0 FastEthernet0/0_ –  **For all unknown addresses send the packet out of F0/0**

Router B:

_RouterB(config)#ip route 0.0.0.0 0.0.0.0 FastEthernet0/0_

5. To test the connection, first, you will need to check whether the link is up. To do this, use the show interface command (see below):

Make sure that Fast Ethernet 0/0 is up and line protocol is up.

_RouterA#show interface FastEthernet0/0_

_FastEthernet0 is up, line protocol is up_

_Hardware is Lance, address is 0000.0c3d.d469 (bia 0000.0c3d.d469)_

_Internet address is 10.0.0.1/8_

_MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec,_

_reliability 255/255, txload 1/255, rxload 1/255_

_Encapsulation ARPA, Loopback not set_

Next, ping your neighbor’s Ethernet interface; this will test whether the link is OK:

_RouterA#ping 10.0.0.2_

_Type escape sequence to abort._

_Sending 5, 100-byte ICMP Echos to 10.0.0.2, timeout is 2 seconds:_

_.!!!!_ – **The first ping failed, while the ARP reply came back from Router A**

_Success rate is 80 percent (4/5), round-trip min/avg/max = 1/1/1 ms._

Next, check your router ARP cache:

_RouterA#show arp_

_Protocol  Address   Age (min)  Hardware Addr   Type   Interface_

_Internet  10.0.0.2  0          0050.5460.f1f8  ARPA   F0/0_

_Internet  10.0.0.1  –          0010.7b80.63a3  ARPA   F0/0_

Your hardware address will obviously be different from the one on my routers!

6. To test CDP, you simply need to enter the show cdp neighbor Bear in mind that the spelling is in U.S. English and that you will have a different output, depending on what device you are connected to. We will cover CDP in more detail later in this guide.

_RouterA#show cdp neighbor_

_Capability Codes: R – Router, T – Trans Bridge, B – Source Route Bridge S – Switch, H – Host, I – IGMP, r – Repeater_

_Device ID  Local Intrfce  Holdtme Capability  Platform  Port ID_

_RouterB    F0/0 0         172     R           2900      F0/0_

7. Finally, telnet from Router A to Router B. To quit a Telnet session, hold down the Ctrl+Shift+6 keys at the same time. Then release, and press the X key. Or just type exit a few times.

_RouterA#telnet 10.0.0.2_

_Trying 10.0.0.2 … Open_

_User Access Verification_

_Username: banbury_

_Password:_   – **Won’t show as you type it**

_RouterB>enable_

_Password:_

_RouterB#_   – **You are now in privileged mode on Router B**

Now issue a _show run_ command on both routers and look at the output.

### Lab 3: Traceroute from Router A to Router B

[![Performing a traceroute](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-59.jpg)](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-59.jpg)

**FIG 1.59 – Performing a traceroute**

#### Lab Exercise

In this lab, you will perform a traceroute From Router A to Router B using Figure 1.59 above as a reference. You wouldn’t usually use the _traceroute_ command over two routers, but it’s an easy way to try out some commands. You configured the above network in the previous lab, so please copy all those commands.

#### Purpose

The _traceroute_ command is a very valuable part of your troubleshooting toolkit. Don’t mistake this for the Windows _tracert_ command, which won’t work on Cisco routers.

#### Lab Walk-through

In privileged mode, type in the Loopback address of Router B:

_RouterA#traceroute 172.30.1.1_

_Type escape sequence to abort._

_Tracing the route to 172.30.1.1_

_1 10.0.0.2 24 msec *  32 msec_

### Lab 4: Copy Startup Config Using TFTP

The physical topology is shown in Figure 1.60 below:

[![TFTP lab](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-60-scaled.jpg)](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-60-scaled.jpg)

**FIG 1.60 – TFTP lab**

#### Lab Exercise

Your task is to configure the IP addressing specified in Figure 1.60.

Text in Courier New font indicates commands that can be entered on the router.

#### Purpose

Backing up the router’s configuration is a crucial part of your backup and disaster avoidance procedures. You will also need to use a TFTP server if you want to upgrade your router’s IOS. Familiarity with using a TFTP server is a fundamental skill for a Cisco engineer.

#### Lab Objectives

1. Configure the router’s Ethernet interface.
2. Put TFTP software onto your PC.
3. Connect the PC and router with a crossover cable, or using a hub or switch.
4. Ping across the Ethernet link.
5. Copy the startup configuration from the router to the TFTP server.

#### Lab Walk-through

1. Configure the network shown in Figure 1.60. If you need help, look at some of the other labs you have already configured.

_Router#config t_

_RouterA(config)#interface FastEthernet0_

_RouterA(config-if))#ip address 10.0.0.2 255.0.0.0_

_RouterA(config-if)#no shut_

2. Install TFTP software on your PC, making it a TFTP server. You can find this software at websites such as www.solarwindsuk.net. Install the software on the root of your C drive. Alternatively, use a server inside Packet Tracer and turn on TFTP.

Make sure that both the PC and the router are in the same subnet. Change the IP address of the PC to 10.0.0.1 255.0.0.0.

Ping the PC from the router to confirm IP connectivity.

_Router#ping 10.0.0.1_

_Type escape sequence to abort._

_Sending 5, 100-byte ICMP Echos to 10.0.0.1, timeout is 2 seconds:_

_!!!!!_

_Success rate is 100 percent (5/5), round-trip min/avg/max = 32/32/32 ms_

Copy the startup configuration to the TFTP server.

_Router#ping 10.0.0.1_

_Type escape sequence to abort._

_Sending 5, 100-byte ICMP Echos to 10.0.0.1, timeout is 2 seconds:_

_!!!!!_

_Success rate is 100 percent (5/5), round-trip min/avg/max = 4/4/4 ms_

_Router#copy start tftp:_

_Address or name of remote host []? 10.0.0.1_

_Destination filename [router-confg]?_

_!!_

_747 bytes copied in 0.256 secs_

_Router#_

3. Check the TFTP log to make sure that the file has been received.

[![TFTP in action](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-61.png)](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-61.png)

**FIG 1.61 – TFTP in action**

You can look for the configuration file in Windows Explorer.

[![network fundamentals](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-62.png)](https://www.howtonetwork.com/wp-content/uploads/2022/02/1-62.png)

**FIG 1.62 – File received**

4. Reload the router. You can use the _copy tftp: start_

_Router#ping 10.0.0.1_

_Type escape sequence to abort._

_Sending 5, 100-byte ICMP Echos to 10.0.0.1, timeout is 2 seconds:_

_!!!!!_

_Success rate is 100 percent (5/5), round-trip min/avg/max = 4/4/4 ms_

_Router#copy tftp: start_

_Address or name of remote host []? 10.0.0.1_

_Source filename []? router-confg_ – **Note the spelling**

_Destination filename [startup-config]?_ –  **Just press Enter here**

_Accessing tftp://10.0.0.1/router-confg…Accessing tftp://10.0.0.1/router-confg…_

_Loading router-confg .from 10.0.0.1 (via Ethernet0): !_

_[OK – 421/4096 bytes]_

_[OK]_

_747 bytes copied in 37.980 secs (11 bytes/sec)_

_Router#_

_00:18:04: %SYS-5-CONFIG_NV_I: Nonvolatile storage configured from tftp://10.0.0.1/router-confg by console_

ALWAYS, ALWAYS NAME THE ROUTER’S STARTUP CONFIGURATION AS startup-config. DOING OTHERWISE WILL PREVENT THE ROUTER FROM BOOTING CORRECTLY.
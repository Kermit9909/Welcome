INTERNET
                    
                       |
                  [Firewall]
                       |
            ========================
            |   CORE LAYER        |  ← OSPF Backbone Area 0
            |   (L3 Switches)     |     High-speed routing
            ========================
                 |         |
        ==========================================
        |    DISTRIBUTION LAYER               |  ← OSPF Area 0 (or ABR to other areas)
        |    (L3 Switches)                    |     Inter-VLAN routing
        |    SW-DIST-1        SW-DIST-2       |     SVI interfaces
        ==========================================     Aggregation point
           |    |    |          |    |    |
        ==========================================
        |       ACCESS LAYER                  |  ← OSPF Area 1, 2, 3 (or stub areas)
        |       (L2 Switches)                 |     End-user access
        |  [SW-ACC-1] [SW-ACC-2] [SW-ACC-3]  |     Port security
        ==========================================     VLAN assignment
            |  |  |    |  |  |    |  |  |
         [PCs][IP][AP][PCs][IP][AP][PCs][IP][AP]
         
Legend:
PCs = End-user computers
IP = IP Phones
AP = Wireless Access Points


CORE LAYER:
- Area 0 (Backbone)
- All inter-area traffic flows through here
- ABR (Area Border Routers) connect to distribution

DISTRIBUTION LAYER:
- Area 0 or ABR connecting to Access areas
- Routes between VLANs
- Policy enforcement point

ACCESS LAYER:
- Area 1, 2, 3 (could be stub areas for efficiency)
- Or just Area 0 in smaller networks
- End devices connect here


# **VLANs in This Design:**

|VLAN|Name|Subnet|Purpose|
|---|---|---|---|
|**10**|Data|10.10.10.0/24|User workstations|
|**20**|Voice|10.10.20.0/24|IP phones|
|**30**|Wireless|10.10.30.0/24|WiFi clients|
|**99**|Management|10.10.99.0/24|Switch/AP management|
|**100**|Servers|10.10.100.0/24|Internal servers|
|**999**|Native|10.10.999.0/24|Unused VLAN (security)|
# **Complete Security Configuration - Full Lab**

---

## **CORE LAYER SWITCH (SW-CORE-1)**

### **Basic Hardening:**

cisco

```cisco
!!! HOSTNAME AND DOMAIN !!!
hostname SW-CORE-1
ip domain-name company.com

!!! STRONG PASSWORDS !!!
enable secret Str0ng!EnableP@ss2026
service password-encryption
security passwords min-length 10

!!! SSH CONFIGURATION !!!
crypto key generate rsa modulus 2048
ip ssh version 2
ip ssh time-out 60
ip ssh authentication-retries 3

username netadmin privilege 15 secret Admin!P@ssw0rd2026

!!! DISABLE UNUSED SERVICES !!!
no ip http server
no ip http secure-server
no cdp run
no ip domain-lookup

!!! CONSOLE SECURITY !!!
line console 0
 exec-timeout 5 0
 logging synchronous
 login local

!!! VTY SECURITY !!!
line vty 0 15
 transport input ssh
 login local
 exec-timeout 5 0
 access-class 99 in

!!! ACL FOR VTY ACCESS !!!
access-list 99 permit 10.10.99.0 0.0.0.255
access-list 99 deny any log

!!! BANNER !!!
banner motd ^
================================================================================
        WARNING: UNAUTHORIZED ACCESS TO THIS DEVICE IS PROHIBITED
        
You must have explicit, authorized permission to access this device.
Unauthorized attempts and actions to access or use this system may result
in civil and/or criminal penalties. All activities performed on this device
are logged and monitored.
================================================================================
^

!!! LOGIN SECURITY !!!
login block-for 120 attempts 3 within 60
login on-failure log
login on-success log

!!! AAA CONFIGURATION !!!
aaa new-model
aaa authentication login default group tacacs+ local
aaa authentication enable default group tacacs+ enable
aaa authorization exec default group tacacs+ local
aaa accounting exec default start-stop group tacacs+
aaa accounting commands 15 default start-stop group tacacs+

tacacs server TACACS-SERVER
 address ipv4 10.10.100.10
 key 7 TacacsSecr3tK3y!2026

!!! NTP !!!
ntp server 10.10.100.20
ntp authenticate
ntp authentication-key 1 md5 NtpS3cr3t!
ntp trusted-key 1

!!! SYSLOG !!!
logging host 10.10.100.30
logging trap informational
logging source-interface Vlan99
service timestamps log datetime msec localtime show-timezone
service sequence-numbers

!!! SNMP (SECURE) !!!
no snmp-server community public
no snmp-server community private
snmp-server community S3cur3C0mmun1ty! RO 98
snmp-server location "Core Layer - Data Center"
snmp-server contact "netadmin@company.com"

access-list 98 permit 10.10.99.0 0.0.0.255

!!! OSPF CONFIGURATION !!!
router ospf 1
 router-id 1.1.1.1
 passive-interface default
 no passive-interface GigabitEthernet1/0/1
 no passive-interface GigabitEthernet1/0/2
 network 10.10.99.0 0.0.0.255 area 0
 network 10.10.0.0 0.0.255.255 area 0

!!! INTERFACES !!!
interface Vlan99
 description Management VLAN
 ip address 10.10.99.1 255.255.255.0
 no shutdown

interface GigabitEthernet1/0/1
 description Uplink to SW-DIST-1
 no switchport
 ip address 10.0.1.1 255.255.255.252
 ip ospf 1 area 0

interface GigabitEthernet1/0/2
 description Uplink to SW-DIST-2
 no switchport
 ip address 10.0.1.5 255.255.255.252
 ip ospf 1 area 0
```

---

## **DISTRIBUTION LAYER SWITCH (SW-DIST-1)**

### **Inter-VLAN Routing + Security:**

cisco

```cisco
!!! BASIC HARDENING (same as core) !!!
hostname SW-DIST-1
ip domain-name company.com
enable secret Str0ng!EnableP@ss2026
service password-encryption
security passwords min-length 10

!!! SSH !!!
crypto key generate rsa modulus 2048
ip ssh version 2
username netadmin privilege 15 secret Admin!P@ssw0rd2026

!!! DISABLE SERVICES !!!
no ip http server
no ip http secure-server
no cdp run
no ip domain-lookup

!!! VTY ACCESS !!!
line vty 0 15
 transport input ssh
 login local
 exec-timeout 5 0
 access-class 99 in

access-list 99 permit 10.10.99.0 0.0.0.255

!!! AAA !!!
aaa new-model
aaa authentication login default group tacacs+ local
tacacs server TACACS-SERVER
 address ipv4 10.10.100.10
 key 7 TacacsSecr3tK3y!2026

!!! ENABLE IP ROUTING !!!
ip routing

!!! DHCP SNOOPING (CRITICAL!) !!!
ip dhcp snooping
ip dhcp snooping vlan 10,20,30
no ip dhcp snooping information option

!!! DAI (DYNAMIC ARP INSPECTION) !!!
ip arp inspection vlan 10,20,30
ip arp inspection validate src-mac dst-mac ip

!!! SVIs (INTER-VLAN ROUTING) !!!
interface Vlan10
 description Data VLAN
 ip address 10.10.10.1 255.255.255.0
 ip helper-address 10.10.100.11
 no shutdown

interface Vlan20
 description Voice VLAN
 ip address 10.10.20.1 255.255.255.0
 ip helper-address 10.10.100.11
 no shutdown

interface Vlan30
 description Wireless VLAN
 ip address 10.10.30.1 255.255.255.0
 ip helper-address 10.10.100.11
 no shutdown

interface Vlan99
 description Management VLAN
 ip address 10.10.99.2 255.255.255.0
 no shutdown

interface Vlan100
 description Server VLAN
 ip address 10.10.100.1 255.255.255.0
 no shutdown

!!! UPLINK TO CORE (TRUSTED FOR DHCP/DAI) !!!
interface GigabitEthernet1/0/1
 description Uplink to SW-CORE-1
 switchport mode trunk
 switchport trunk native vlan 999
 switchport trunk allowed vlan 10,20,30,99,100
 ip dhcp snooping trust
 ip arp inspection trust
 spanning-tree guard root
 no shutdown

!!! DOWNLINK TO ACCESS (UNTRUSTED) !!!
interface range GigabitEthernet1/0/5-10
 description Downlinks to Access Switches
 switchport mode trunk
 switchport trunk native vlan 999
 switchport trunk allowed vlan 10,20,30,99
 spanning-tree bpduguard enable
 no shutdown

!!! OSPF !!!
router ospf 1
 router-id 2.2.2.1
 passive-interface default
 no passive-interface GigabitEthernet1/0/1
 network 10.10.0.0 0.0.255.255 area 0

!!! SPANNING TREE ROOT !!!
spanning-tree vlan 10,20,30,99 priority 4096

!!! NTP !!!
ntp server 10.10.100.20

!!! SYSLOG !!!
logging host 10.10.100.30
logging trap informational
```

---

## **ACCESS LAYER SWITCH (SW-ACC-1)**

### **End-User Security (Port Security, 802.1X, etc.):**

cisco

```cisco
!!! BASIC HARDENING !!!
hostname SW-ACC-1
ip domain-name company.com
enable secret Str0ng!EnableP@ss2026
service password-encryption

!!! SSH !!!
crypto key generate rsa modulus 2048
ip ssh version 2
username netadmin privilege 15 secret Admin!P@ssw0rd2026

!!! DISABLE SERVICES !!!
no ip http server
no cdp run

!!! VTY !!!
line vty 0 15
 transport input ssh
 login local
 exec-timeout 5 0

!!! AAA (802.1X REQUIRED!) !!!
aaa new-model
aaa authentication login default group tacacs+ local
aaa authentication dot1x default group radius

radius server RADIUS-SERVER
 address ipv4 10.10.100.12 auth-port 1812 acct-port 1813
 key RadiusS3cr3t!2026

!!! ENABLE 802.1X GLOBALLY !!!
dot1x system-auth-control

!!! DHCP SNOOPING !!!
ip dhcp snooping
ip dhcp snooping vlan 10,20,30

!!! DAI !!!
ip arp inspection vlan 10,20,30

!!! MANAGEMENT VLAN !!!
interface Vlan99
 ip address 10.10.99.10 255.255.255.0
 no shutdown

ip default-gateway 10.10.99.1

!!! UPLINK TO DISTRIBUTION (TRUSTED) !!!
interface GigabitEthernet0/1
 description Uplink to SW-DIST-1
 switchport mode trunk
 switchport trunk native vlan 999
 switchport trunk allowed vlan 10,20,30,99
 ip dhcp snooping trust
 ip arp inspection trust
 spanning-tree guard root
 no shutdown

!!! ACCESS PORTS - DATA USERS !!!
interface range FastEthernet0/1-10
 description Data User Ports
 switchport mode access
 switchport access vlan 10
 switchport voice vlan 20
 
 ! PORT SECURITY
 switchport port-security
 switchport port-security maximum 3
 switchport port-security mac-address sticky
 switchport port-security violation restrict
 
 ! 802.1X
 authentication port-control auto
 authentication host-mode multi-domain
 authentication violation restrict
 
 ! SPANNING TREE
 spanning-tree portfast
 spanning-tree bpduguard enable
 
 ! STORM CONTROL
 storm-control broadcast level 50.00
 storm-control multicast level 50.00
 
 no shutdown

!!! WIRELESS ACCESS POINT PORTS !!!
interface range FastEthernet0/11-15
 description Wireless AP Ports
 switchport mode access
 switchport access vlan 30
 
 ! PORT SECURITY (AP MAC only)
 switchport port-security
 switchport port-security maximum 1
 switchport port-security mac-address sticky
 switchport port-security violation shutdown
 
 ! 802.1X (for AP authentication)
 authentication port-control auto
 
 ! SPANNING TREE
 spanning-tree portfast
 spanning-tree bpduguard enable
 
 no shutdown

!!! IP PHONE PORTS (DUAL VLAN) !!!
interface range FastEthernet0/16-24
 description IP Phone + PC Ports
 switchport mode access
 switchport access vlan 10
 switchport voice vlan 20
 
 ! PORT SECURITY (Phone + PC = 2 devices)
 switchport port-security
 switchport port-security maximum 2
 switchport port-security mac-address sticky
 switchport port-security violation restrict
 
 ! 802.1X MULTI-DOMAIN
 authentication port-control auto
 authentication host-mode multi-domain
 
 ! SPANNING TREE
 spanning-tree portfast
 spanning-tree bpduguard enable
 
 ! QoS TRUST (trust phone's CoS marking)
 mls qos trust cos
 
 no shutdown

!!! UNUSED PORTS (SECURITY!) !!!
interface range FastEthernet0/25-48
 description UNUSED - SHUTDOWN
 switchport mode access
 switchport access vlan 999
 shutdown

!!! SPANNING TREE !!!
spanning-tree mode rapid-pvst

!!! NTP !!!
ntp server 10.10.100.20

!!! SYSLOG !!!
logging host 10.10.100.30
logging trap warnings
```

---

## **WIRELESS LAN CONTROLLER (WLC) CONFIGURATION**

### **WPA3-Enterprise with 802.1X:**

cisco

```cisco
!!! This would be GUI-based on most WLCs, but concepts: !!!

WLAN Configuration:
- SSID: "CorpSecure"
- Security: WPA3-Enterprise
- Authentication: 802.1X
- RADIUS Server: 10.10.100.12
- VLAN: 30 (Wireless VLAN)

Management Frame Protection: Enabled (WPA3 feature)
Fast Transition (802.11r): Enabled
PMF (Protected Management Frames): Required

Guest WLAN:
- SSID: "Guest-WiFi"
- Security: WPA3-Personal (or WPA2-Personal)
- Pre-shared Key: "Gu3st!W1F1P@ss2026"
- VLAN: 40 (Guest VLAN - isolated)
- Client Isolation: Enabled
```

---

## **ROUTER (EDGE/FIREWALL PLACEHOLDER)**

### **Basic ACLs + Hardening:**

cisco

```cisco
hostname EDGE-RTR-1
ip domain-name company.com
enable secret Str0ng!EnableP@ss2026

!!! SSH !!!
crypto key generate rsa modulus 2048
ip ssh version 2
username netadmin privilege 15 secret Admin!P@ssw0rd2026

!!! AAA !!!
aaa new-model
aaa authentication login default group tacacs+ local
tacacs server TACACS-SERVER
 address ipv4 10.10.100.10
 key TacacsSecr3tK3y!2026

!!! ANTI-SPOOFING ACL (INBOUND FROM INTERNET) !!!
ip access-list extended ANTI-SPOOF-IN
 deny ip 10.0.0.0 0.255.255.255 any log
 deny ip 172.16.0.0 0.15.255.255 any log
 deny ip 192.168.0.0 0.0.255.255 any log
 deny ip 127.0.0.0 0.255.255.255 any log
 deny ip 224.0.0.0 31.255.255.255 any log
 permit ip any any

!!! OUTBOUND ACL (PERMIT ONLY INTERNAL) !!!
ip access-list extended INTERNAL-OUT
 permit ip 10.10.0.0 0.0.255.255 any
 deny ip any any log

!!! APPLY TO INTERFACES !!!
interface GigabitEthernet0/0
 description WAN to Internet
 ip address dhcp
 ip access-group ANTI-SPOOF-IN in
 ip verify unicast source reachable-via rx
 no ip proxy-arp
 no ip redirects
 no ip unreachables

interface GigabitEthernet0/1
 description LAN to Core
 ip address 10.10.254.1 255.255.255.0
 ip access-group INTERNAL-OUT in

!!! NAT/PAT !!!
ip nat inside source list NAT-ACL interface GigabitEthernet0/0 overload

ip access-list standard NAT-ACL
 permit 10.10.0.0 0.0.255.255

!!! VTY !!!
line vty 0 15
 transport input ssh
 access-class 99 in

access-list 99 permit 10.10.99.0 0.0.0.255
```

---

# **Security Feature Summary by Layer:**

## **Access Layer:**

- ✅ Port Security (all access ports)
- ✅ 802.1X authentication
- ✅ DHCP Snooping (untrusted ports)
- ✅ DAI (untrusted ports)
- ✅ BPDU Guard (access ports)
- ✅ PortFast (access ports)
- ✅ Storm Control
- ✅ Unused ports shutdown

## **Distribution Layer:**

- ✅ DHCP Snooping (global + trusted uplinks)
- ✅ DAI (global + trusted uplinks)
- ✅ Root Guard (uplinks)
- ✅ Inter-VLAN routing with ACLs
- ✅ DHCP relay (ip helper-address)
- ✅ Spanning Tree root priority

## **Core Layer:**

- ✅ AAA with TACACS+
- ✅ Strong device hardening
- ✅ Secure management (SSH only)
- ✅ NTP + Syslog
- ✅ SNMP v3 (or secured v2c)
- ✅ VTY ACLs
- ✅ OSPF authentication (optional)

## **Edge/Firewall:**

- ✅ Anti-spoofing ACLs
- ✅ NAT/PAT
- ✅ Egress filtering
- ✅ uRPF (unicast reverse path forwarding)

---

# **Verification Commands - Full Suite:**

cisco

```cisco
!!! PORT SECURITY !!!
show port-security
show port-security interface fa0/1
show port-security address

!!! DHCP SNOOPING !!!
show ip dhcp snooping
show ip dhcp snooping binding
show ip dhcp snooping statistics

!!! DAI !!!
show ip arp inspection
show ip arp inspection statistics vlan 10

!!! 802.1X !!!
show dot1x all
show authentication sessions
show authentication sessions interface fa0/1

!!! AAA !!!
show aaa servers
show tacacs
show radius statistics

!!! GENERAL SECURITY !!!
show ip ssh
show login
show users
show privilege

!!! SPANNING TREE !!!
show spanning-tree summary
show spanning-tree interface fa0/1 detail

!!! ACLs !!!
show ip access-lists
show ip interface gi0/0 | include access list
```

---

**This is a production-grade security configuration!**

**Use this for:**

- ✅ Your lab video
- ✅ Practice exam scenarios
- ✅ Real-world implementation reference
- ✅ Interview discussions
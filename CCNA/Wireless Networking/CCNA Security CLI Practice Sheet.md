

## Quick 15-Minute Morning Drill

### Part 1: Password Security (3 min)

**Enable Secret & Service Password Encryption**

```
Router(config)# enable secret cisco
Router(config)# service password-encryption
```

**Console Line Security**

```
Router(config)# line console 0
Router(config-line)# password C0ns0le123
Router(config-line)# login
Router(config-line)# exec-timeout 5 0
Router(config-line)# logging synchronous
```

**VTY Lines (SSH/Telnet)**

```
Router(config)# line vty 0 15
Router(config-line)# password VTY123
Router(config-line)# login local
Router(config-line)# exec-timeout 10 0
Router(config-line)# transport input ssh
```

**Local User Accounts**

```
Router(config)# username admin privilege 15 secret Adm1nP@ss
Router(config)# username support privilege 5 secret Supp0rtP@ss
```

### Part 2: SSH Configuration (3 min)

```
Router(config)# hostname R1
Router(config)# ip domain-name ccna.lab
Router(config)# crypto key generate rsa modulus 2048
Router(config)# ip ssh version 2
Router(config)# ip ssh time-out 60
Router(config)# ip ssh authentication-retries 3
```

### Part 3: Port Security on Switch (4 min)

**Basic Port Security**

```
Switch(config)# interface f0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport port-security
Switch(config-if)# switchport port-security maximum 2
Switch(config-if)# switchport port-security mac-address sticky
Switch(config-if)# switchport port-security violation restrict
```

**Violation Modes Practice**

```
! Shutdown (default) - disables port, requires manual intervention
Switch(config-if)# switchport port-security violation shutdown

! Restrict - drops packets, increments counter, sends SNMP trap
Switch(config-if)# switchport port-security violation restrict

! Protect - drops packets silently
Switch(config-if)# switchport port-security violation protect
```

**Re-enable After Violation**

```
Switch(config)# interface f0/1
Switch(config-if)# shutdown
Switch(config-if)# no shutdown
! OR
Switch# clear port-security sticky interface f0/1
```

### Part 4: DHCP Snooping (3 min)

```
Switch(config)# ip dhcp snooping
Switch(config)# ip dhcp snooping vlan 10,20
Switch(config)# no ip dhcp snooping information option

! Trusted port (uplink to legitimate DHCP server)
Switch(config)# interface g0/1
Switch(config-if)# ip dhcp snooping trust

! Untrusted ports rate limiting
Switch(config)# interface range f0/1-24
Switch(config-if-range)# ip dhcp snooping limit rate 10
```

### Part 5: Additional Hardening (2 min)

**Disable Unused Services**

```
Router(config)# no ip http server
Router(config)# no ip http secure-server
Router(config)# no cdp run
Router(config)# no ip source-route
```

**Banner**

```
Router(config)# banner motd # Authorized Access Only #
```

**Disable Unused Interfaces**

```
Switch(config)# interface range f0/10-24
Switch(config-if-range)# shutdown
Switch(config-if-range)# description UNUSED
```

**Native VLAN Change**

```
Switch(config)# interface g0/1
Switch(config-if)# switchport trunk native vlan 999
```

---

## Verification Commands (Use After Configuration)

```
show running-config
show port-security interface f0/1
show port-security address
show ip dhcp snooping
show ip dhcp snooping binding
show ip ssh
show users
show line
```

---

**Practice Goal:** Type through all commands in order, then verify your configurations. Focus on muscle memory and understanding _why_ each command hardens the device.

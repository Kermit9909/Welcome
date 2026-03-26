# CCNA Router Hardware & Configuration

## Router Hardware Essentials

### Interface Naming Convention

- **Modern format**: `slot/subslot/port` (e.g., Serial 0/0/0, GigabitEthernet 0/1)
- **Older format**: `slot/port` (e.g., Serial 0/1)
- **Fixed interfaces**: Just numbered (e.g., Serial 0, Serial 1)

### Key Commands to Identify Hardware

```
show ip interface brief    # Shows all interfaces and their status
show diag                   # Shows installed hardware
show inventory              # Verifies hardware installation
```

---

## Power over Ethernet (PoE) - EXAM TOPIC

### IEEE 802.3af Standard

- **Default power**: 15.4W per device
- **Powers**: IP phones, wireless APs, cameras
- **Enable**: `power inline auto` (default on PoE switches)
- **Disable**: `no power inline`

### Key PoE Commands

```
show power inline          # Display PoE status for all ports
```

### PoE Power Classes (IEEE 802.3af-2003)

|Class|Min Power at PSE|Max Power at PD|Usage|
|---|---|---|---|
|0|15.4W|0.44 to 12.95W|Default|
|1|4.0W|0.44 to 3.84W|Optional|
|2|7.0W|3.84 to 6.49W|Optional|
|3|15.4W|6.49 to 12.95W|Optional|
|4|N/A|N/A|Reserved|

### PoE Detection Methods

- **Cisco ILP**: Uses AC detection with Fast Link Pulse (FLP)
- **IEEE 802.3af**: Uses DC detection expecting 25kΩ resistance
- **Negotiation**: Uses CDP to communicate power requirements

---

## Connecting to Routers

### Console Connection Settings (MEMORIZE!)

- **Bits per second**: 9600
- **Data bits**: 8
- **Parity**: None
- **Stop bits**: 1
- **Flow control**: None

### Connection Types

1. **Traditional**: Rollover cable (RJ-45 to DB9)
2. **Modern**: USB mini Type-B console cable
3. **Software**: PuTTY (free terminal emulator)

### USB Console Setup

- Download Cisco USB console drivers from cisco.com
- Check Device Manager for COM port assignment
- Configure PuTTY with the assigned COM port

---

## Router Modes (CRITICAL!)

|Mode|Prompt|Command to Enter|Purpose|
|---|---|---|---|
|**User EXEC**|`Router>`|Default login|Limited commands|
|**Privileged EXEC**|`Router#`|`enable`|View configs, troubleshoot|
|**Global Config**|`Router(config)#`|`configure terminal` or `conf t`|Make config changes|
|**Interface Config**|`Router(config-if)#`|`interface <type><number>`|Configure interfaces|
|**Line Config**|`Router(config-line)#`|`line console 0`|Configure console/VTY access|
|**Router Config**|`Router(config-router)#`|`router <protocol>`|Configure routing protocols|

### Navigation Commands

```
enable              # User EXEC → Privileged EXEC
disable             # Privileged EXEC → User EXEC
configure terminal  # Privileged EXEC → Global Config (conf t for short)
exit                # Go back one level
Ctrl+Z              # Return to Privileged EXEC from anywhere
logout              # Exit the session
```

---

## Essential Configuration Commands

### Basic Interface Configuration

```
Router(config)# interface Serial0/0/0
Router(config-if)# ip address 192.168.1.1 255.255.255.0
Router(config-if)# description To_Headquarters
Router(config-if)# no shutdown    # CRITICAL! Opens interface
Router(config-if)# exit
```

**Important**: All interfaces are **shutdown by default** - you MUST use `no shutdown`!

### Loopback Interfaces

- **Virtual interfaces** that exist only in software
- **Always up/up** unless manually shut down
- Used for testing and OSPF Router IDs

```
Router(config)# interface Loopback0
Router(config-if)# ip address 192.168.20.1 255.255.255.0
Router(config-if)# ^Z    # Ctrl+Z to exit
```

---

## Critical Show Commands (Know These Cold!)

|Command|Purpose|
|---|---|
|`show running-config` or `show run`|Configuration in RAM (current)|
|`show startup-config` or `show start`|Configuration in NVRAM (saved)|
|`show ip interface brief`|Quick interface status summary|
|`show interface <interface>`|Detailed interface statistics|
|`show version`|IOS version, uptime, config register|
|`show flash` or `show flash:`|IOS files in flash memory|
|`show history`|Last 10 commands entered|
|`show diag`|Hardware diagnostics|
|`show inventory`|Hardware inventory|
|`show power inline`|PoE status|

### Interface Status Meanings

|Status|Protocol|Meaning|
|---|---|---|
|up|up|Interface is working correctly|
|up|down|Physical layer up, data link layer problem|
|administratively down|down|Interface is shutdown (needs `no shutdown`)|
|down|down|Cable or hardware problem|

---

## Keyboard Shortcuts (Speed Up Your Exam!)

|Shortcut|Function|
|---|---|
|`Ctrl+A`|Move to beginning of line|
|`Ctrl+E`|Move to end of line|
|`Ctrl+B`|Move back one character|
|`Ctrl+F`|Move forward one character|
|`Ctrl+P` or `Up Arrow`|Recall previous command|
|`Ctrl+N` or `Down Arrow`|Recall next command|
|`Ctrl+Z`|Exit to Privileged EXEC mode|
|`Ctrl+C`|Abort current command|
|`Ctrl+U`|Delete entire line|
|`Ctrl+W`|Delete a word|
|`Tab`|Complete command|
|`?`|Show available commands|
|`Backspace`|Delete single character|

### Command History

```
show history                    # Shows last 10 commands (default)
terminal history size 20        # Increase history buffer to 20
```

---

## Configuration Register (IMPORTANT!)

### Common Settings

- **0x2102** - Normal boot (loads startup-config)
- **0x2142** - Ignore startup-config (used for password recovery)

### Commands

```
Router(config)# config-register 0x2142
Router(config)# exit
Router# show version           # Shows current and next reload setting
Router# reload                 # Apply the change
```

### When to Use 0x2142

- Password recovery
- Clearing saved configuration for labs
- Router will boot with no configuration

### Viewing Configuration Register

```
Router# show version

[output truncated]
Configuration register is 0x2102 (will be 0x2142 at next reload)
```

---

## Saving Configuration (DON'T FORGET!)

### Save Commands (All do the same thing)

```
Router# copy running-config startup-config
Router# copy run start          # Shortcut
Router# write memory            # Alternative command
Router# wr                      # Even shorter
```

### What Happens If You Don't Save

- Changes lost after reload
- Router prompts: "System configuration has been modified. Save? [yes/no]:"
- For labs: Answer **NO** so you can practice from scratch

### Configuration Storage Locations

- **Running-config**: Stored in RAM (DRAM) - active configuration
- **Startup-config**: Stored in NVRAM - loaded at boot
- **IOS**: Stored in Flash memory (EEPROM)

---

## Reloading the Router

```
Router# reload                  # Reload immediately
Router# reload in 10            # Reload in 10 minutes
Router# reload cancel           # Cancel scheduled reload
```

### Reload Process

1. Router prompts to save configuration
2. Runs POST (Power-On Self-Test)
3. Loads IOS from Flash
4. Checks configuration register
5. Loads startup-config (if register is 0x2102)

---

## Debug Commands (Use with CAUTION!)

### Basic Debug Usage

```
Router# debug ip ospf hello        # Enable debug
Router# no debug ip ospf hello     # Disable specific debug
Router# undebug all                # Disable ALL debugs
Router# un all                     # Shortcut
```

### Critical Debug Safety Rules

- **NEVER use `debug ip packet`** on production networks (will crash router!)
- Use `terminal monitor` when connected via Telnet/SSH to see debug output
- Always turn off debugs when finished with `undebug all`
- Check with experienced engineer before using on live network

### Useful Line Command

```
Router(config)# line console 0
Router(config-line)# logging synchronous    # Prevents output from interrupting typing
```

### Redisplay Interrupted Line

If console message appears while typing:

- `Ctrl+L` or `Ctrl+R` - Redisplay current line
- `Up Arrow` - Recall the line you were typing

---

## Pipe Commands (Advanced Filtering)

### Basic Syntax

```
show [command] | [begin | include | exclude] [text]
```

### Examples

```
Router# show run | begin interface     # Start output at "interface"
Router# show run | include login       # Show only lines with "login"
Router# show run | exclude !           # Exclude lines with "!"
```

### Common Uses

```
show run | begin interface FastEthernet0/0
show run | include ip address
show run | exclude unassigned
show version | include register
show ip route | include 192.168
```

**Note**: Pipe commands may not work in Packet Tracer

---

## Password Security

### Enable Secret (Recommended)

```
Router(config)# enable secret MySecurePassword123
```

- Uses MD5 encryption
- Shows as `enable secret 5 [encrypted string]` in config
- **Always use this instead of enable password**

### Enable Password (Not Recommended)

```
Router(config)# enable password MyPassword    # Plain text - DON'T USE
```

- Stored in plain text
- If both are configured, `enable secret` takes precedence

### Console Password

```
Router(config)# line console 0
Router(config-line)# password cisco
Router(config-line)# login
```

### VTY Password (Telnet/SSH)

```
Router(config)# line vty 0 15
Router(config-line)# password cisco
Router(config-line)# login
```

### Service Password Encryption

```
Router(config)# service password-encryption
```

- Encrypts all plain text passwords using Type 7 encryption
- **Weak encryption** - easily decrypted online
- Better than nothing, but use `enable secret` for real security

---

## Host IP Configuration (NEW TO CCNA!)

### Windows Commands

```
ipconfig                    # Basic IP info
ipconfig /all              # Detailed IP info (DNS, gateway, etc.)
ipconfig /?                # Show all options
route print                # View routing table
route add [dest] mask [mask] [gateway]    # Add route
route delete [prefix]      # Delete route
```

### Linux Commands

```
ip addr show               # Display IP addresses (replaces ifconfig)
ip addr show eth0          # Show specific interface
ip route                   # Display routing table
ip route add [dest] via [gateway]    # Add route
```

### Mac OS

- Access via **System Settings → Network**
- GUI-based configuration
- Can also use terminal with similar commands to Linux

---

## Line Configuration

### Console Line

```
Router(config)# line console 0
Router(config-line)# password cisco
Router(config-line)# login
Router(config-line)# logging synchronous
Router(config-line)# exec-timeout 0 0        # Disable timeout (labs only!)
```

### VTY Lines (Telnet/SSH)

```
Router(config)# line vty 0 15
Router(config-line)# password cisco
Router(config-line)# login
Router(config-line)# transport input ssh     # SSH only (secure)
Router(config-line)# transport input telnet  # Telnet only
Router(config-line)# transport input all     # Both SSH and Telnet
```

### USB Console Timeout

```
Router(config)# line console 0
Router(config-line)# usb-inactivity-timeout 30    # 30 minutes
Router(config-line)# no usb-inactivity-timeout    # Disable timeout
```

- Range: 1 to 240 minutes
- If timeout reached, must reseat (unplug/plug) USB cable

---

## Router Boot Process

1. **POST** (Power-On Self-Test) - Hardware diagnostics
2. **Load Bootstrap** - From ROM
3. **Load IOS** - From Flash memory
4. **Check Configuration Register** - Determines boot behavior
5. **Load Configuration** - From NVRAM (if register is 0x2102)

### Setup Mode

If no startup-config exists:

```
--- System Configuration Dialog ---
Would you like to enter the initial configuration dialog? [yes/no]: no
```

**Always answer NO** - Setup mode rarely gives desired results

---

## Troubleshooting Commands

### Basic Troubleshooting Flow

```
show version                       # Check IOS, uptime, memory
show ip interface brief           # Check interface status
show interface [interface]        # Detailed interface info
show running-config               # View current config
show startup-config               # View saved config
show ip route                     # Check routing table
show cdp neighbors                # See connected devices
ping [ip-address]                # Test connectivity
traceroute [ip-address]          # Trace path to destination
```

### Advanced Troubleshooting

```
show processes cpu                # CPU utilization
show memory                       # Memory usage
show logging                      # System log messages
show controllers [interface]     # Physical layer details
show buffers                      # Buffer statistics
```

---

## Command Abbreviation

### Rules for Abbreviating

- Type only enough letters to make the command unique
- Must be the only command starting with those letters in that mode
- Common abbreviations:
    - `conf t` = `configure terminal`
    - `sh` = `show`
    - `int` = `interface`
    - `ip add` = `ip address`
    - `no shut` = `no shutdown`

### Example

```
Router# conf t                    # Instead of configure terminal
Router(config)# int fa0/0         # Instead of interface FastEthernet0/0
Router(config-if)# ip add 192.168.1.1 255.255.255.0
Router(config-if)# no shut
```

**Exam Note**: Some abbreviations may not work in exam simulator - use full commands when unsure

---

## Help System

### Using the Question Mark (?)

```
Router# ?                         # Show all available commands
Router# sh?                       # Show commands starting with "sh"
Router# show ?                    # Show options after "show"
Router# show ip ?                 # Show options after "show ip"
```

### Context-Sensitive Help

```
Router(config-if)# ip address ?
  A.B.C.D  IP address

Router(config-if)# ip address 192.168.1.1 ?
  A.B.C.D  IP subnet mask
```

---

## Common Configuration Mistakes

1. **Forgetting `no shutdown`** - Interface stays down
2. **Not saving configuration** - Changes lost after reload
3. **Wrong mode** - Command won't work
4. **Typos in commands** - Use Tab completion
5. **Wrong interface name** - Check with `show ip interface brief`
6. **Forgetting subnet mask** - Required with IP address
7. **Wrong configuration register** - Router won't boot correctly

---

## Exam Tips

### Must Memorize

- ✅ **Console settings**: 9600, 8, None, 1, None
- ✅ **PoE default power**: 15.4W (IEEE 802.3af)
- ✅ **Config register**: 0x2102 (normal), 0x2142 (ignore startup)
- ✅ **Router modes and prompts**
- ✅ **Interface default state**: Administratively down
- ✅ **Show commands**: Especially `show ip interface brief`

### Exam Strategies

- ⚠️ **You CANNOT go back** - Be sure before clicking next
- ⚠️ **Know your modes** - Wrong mode = command rejected
- ⚠️ **Read carefully** - Exam tricks are subtle
- ⚠️ **Use abbreviations carefully** - Full commands are safer
- ⚠️ **Always `no shutdown`** - Interfaces are down by default
- ⚠️ **Budget time wisely** - Don't spend too long on sims

### For Simulations

- ✅ Write subnet cheat sheet on whiteboard first
- ✅ Use show commands to verify before moving on
- ✅ Read the ENTIRE task before typing
- ✅ Save configs on sims: `copy run start` or `write memory`
- ✅ Test your config with `ping` and `show` commands

---

## Quick Reference Card

### Most Common Commands

```bash
# Navigation
enable                            # User → Privileged
conf t                           # Privileged → Global Config
interface [type][number]         # Global Config → Interface Config
exit                            # Back one level
Ctrl+Z                          # Back to Privileged mode

# Configuration
ip address [address] [mask]     # Set IP address
no shutdown                     # Enable interface
description [text]              # Add interface description
copy run start                  # Save configuration

# Verification
show ip interface brief         # Interface summary
show run                        # Current config
show version                    # IOS and hardware info
show interface [interface]      # Detailed interface stats
show ip route                   # Routing table

# Troubleshooting
ping [address]                  # Test connectivity
traceroute [address]           # Trace path
show cdp neighbors             # See connected devices
debug [protocol]               # Real-time protocol info
undebug all                    # Turn off all debugs
```

---

## Practice Labs Checklist

Before starting each lab:

- [ ] Set config-register to 0x2142
- [ ] Reload router
- [ ] Answer "no" to setup dialog
- [ ] Check interfaces with `show ip interface brief`
- [ ] Write down interface names you'll use
- [ ] Practice commands without looking at notes
- [ ] Do NOT save configuration (answer "no" when prompted)

After completing each lab:

- [ ] Verify configuration with show commands
- [ ] Test connectivity with ping
- [ ] Understand why each command was needed
- [ ] Reload router for next practice session

---

**Study Tips:**

- Practice typing commands until they're muscle memory
- Use Packet Tracer daily for hands-on practice
- Review Anki cards every day
- Focus on show commands - they're 90% of troubleshooting
- Time yourself on lab configurations
- Learn to recognize errors quickly

**Remember**: Speed and accuracy come from repetition. The CCNA exam rewards those who have practiced configurations hundreds of times!
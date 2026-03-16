
# THM - Cyber Defense Framework
**Date:** 2026-03-16 |
**Track:** :shield: SOC Level 1

## Key Concepts

### Why it is important
    - Identify missing security controls and gap analysis
    - Recognize the intrusion attempts and understand the APT's goals and objectives

### Learning Objectives (Attack Phases)
    - Recon
    - Weaponization
    - Delivery
    - Exploitation
    - Installation
    - Installation
    - Command & Control
    - Actions and Objectives

## Reconnaissance

### Definition - research and planning phase of an attack against a system/victim

OSINT - Yes!

**:mag: Sources of OSINT Data:**
     - Search Engines
     - Print and online media
     - Social media accounts
     - Online forums and blogs
     - Online public record databases
     - WHOIS and technical data

## Weaponization

### Def: Turning raw information into actionable attack tools through crafting malware and exploits into a payload.

***Key Terminology***
**Malware**
**Exploits**
**Payload**

### Weaponization Tactics Ex.:
     - infect Microsoft Office documents (macors, VBA Scripts)
     - USB drives distributed publicly
     - set up C2 infrastructure
     - infect host with a backdoor
     - tailored phishing attempts
     - Watering hole attacks (compromise frequently visited sites of target/s)

## :warning: Exploitation
### Techniques
    - Malicious macro execution via phishing email that executes when user opens .xml file for example
    - Zero-day exploit
    - Known CVEs

### :fire:  Important!!
     **Signs of Exploitation**
     - Unexpected process spawns
     - Registry changes or new services created
     - Suspicous command-line arguments found in system logs (ex. whomai)

## Installation

### Backdoor AKA Access Point

**Persistence can be achieved through:**

    - Installing a ***web shell*** on a server
    - Installing a backdoor on machine via ***Meterpreter** for example
    - ***Creating or modifying Windows Services*** **Important to learn**
        - ssc.exe (located C:\Program Files\Common Files\System\ssc.exe)
    - Adding the entry of "run keys" for payload in Registry of Startup Folder
        - HKEY-CU\...\Windows\CurrentVersion\Run or \Runonce
        - HKEY-LM\....\....\Run (All users)
        - HKEY-LM\....\....\RunOnce (Run once)

### Timestomping  (Check out on MITRE)
:muscle: Powershell is Powerfull!!! 

## Command & Control (C&C | C2 Beaconing)

**Most common C2 channels**
    - HTTP/HTTPS, DNS

**New Modern / Evolved chanenls**

    - HTTPS C2 - encrypted and looks normal. Most modern malware uses this.
    - DNS Tunneling - encoded data in DNS queries (slow but effective)
    - DNS over HTTPS (DoH) - it encrypts DNS!!! Crazy....
    - Cloud Service Abuse - C2 over legit platforms (GoogleDrive, Slack, Discord,     etc.)
    - Web Sockets - persistent encryption connections that look like normal 
    - HTTPS- ICMP tunneling - hiding data in ping packets
    - Socail Media APIs - Twitter/X, Telegram used as C2 (fascinating)

### Question: "I know this is HTTP, BUT does this HTTP ***BEHAVE*** normally"

## Actions on Objectives (Exfiltration)
    - Collect credentials from users
    - Priv esc
    - Internal recon
    - Lateral movement
    - Collect and exfiltrate sensitive data
    - Del backups and shadow copies (VSS)
    - Overwrite or corrupt data

## Tools Used

### :mag: OSINT

### Email Harversting
[theharvester](https://github.com/darksagae/theHarverster)
[Hunter.io](https://hunter.io/)
[OSINT Framework](https://osintframework.com/)


## Commands / Syntax
N/A

## IOCs / Reference
    - Hashes
    - IP
    - Domain
    - URL
    - Email
    - Registry
    - File Path
    - Process (or process tree)
    - Lockheed Martin - Cyber Kill Chain (registered 2011)

## Takeaways

Understanding the cyber kill chain gives an outline of the necessary requiremnts, and the techniques of a proper cyber attack.  Therefore, it provides a good baseline of where to look for IOCs to better catch alerts as early as possible.  It also relates to the pyramid of pain. Catching a hash is easy for a SOC team,but just as easy for an attacker to evade.  The real goal is pushing detection up the kill chain and "bottle neck" the top of the pyramid. Because if an attacker has to change there TTPs it means they have to fundamentally change their whole plan of attack.  That gives defenders time to regroup and get ready.


# Unified Kill Chain

## Threat Modeling
    1. Identify what systems and apps need to be secured and what function they serve.
    2. Assessing vulnerabilities and weaknesses of these systems and apps
    3. Create a plan of action
    4. Putting in policies to prevent these vulnerabilites from occuring again

### KillChain Frameworks:
    - STRIDE
    - DREAD
    - CVSS

## Introduction to the Unified Kill Chain

<img src="Welcome/thm/assets/ukc_pic.png">

## Benefits of the UKC Framework

    - Modern (updated in 2022)
    - Extremely detailed
    - Covers an entire attack -recon > post-exploitation
    - More realistic attack scenario

# Goal: In (Initial Foothold)

## Recon [MITRE Tactic TA0043](https://attack.mitre.org/tactics/TA0043/)
    - Discovering systems and services > weaponization / exploitation
    - Finding contact lists > social engineering / phishing attacks
    - Finding credentials > pivoting or initial access

## Weaponization [MITRE TA0001](https://attack.mitre.org/tactics/TA0001/)
    - Setting up the necessary ***INFRASTRUCTURE***
    - EX. C2 Server or reverse shells

## Social Engineering [MITRE TA0001](https://attack.mitre.org/tactics/TA0001/)
    - Manipulation of employees or just people in general
    - EX. phishing email, impersonating a web site, calling / visiting target

## Exploitation [MITRE TA0002](https://attack.mitre.org/tactics/TA0002/)
    - "HOW" the attacker takes advantage of weakness or vulnerability
    - EX. execute reverse shell, automated script, web app vuln.

## Persistence [MITRE TA0003](https://attack.mitre.org/tactics/TA0003/)
    - Techniques to "MAINTAIN" access to a system
    - EX. creating a service on system, creating mult. backdoors, adding target system to C2 Server

## Defense Evasion [MITRE TA0005](https://attack.mitre.org/tactics/TA0005/)
    - techniques used to evade defensive measures
    - manipulate: WAFs, net firewalls, anti-virus, IDS

## Command & Control [MITRE TA0011](https://attack.mitre.org/tactics/TA0011/)
    - Combines "Weaponization" stage in establishing comms between adversary and target
    -EX. execute commands, steal data, controlled server to pivot to other systems on the nework.

## Pivoting [MITRE TA0008](https://attack.mitre.org/tactics/TA0008/)
    - technique to gain access to other systems in the network.
    -EX. initial access via web app > internal system directory or server (data)

# Goal: Through (Network Propagation)

## Process:
    - Pivoting
    - Discovery
    - Priv esc.
    - Execution
    - Credential Access
    - Lateral Movement

# Goal: Out - CIA Compromised and time to go...

## Collection [MITRE TA0009](https://attack.mitre.org/tactics/TA0009/)
    - Gather all valuable data of interest
    - Compromise of **Confidentiality**
    - leads to Exfiltration

## Exfiltration[MITRE TA0010](https://attack.mitre.org/tactics/TA0010/)
    - Package data using compression and encryptioin. Utilize C2 Channel or DNS tunnel to exfiltrate data

## Impact [MITRE TA0040](https://attack.mitre.org/tactics/TA0010/)
    - Compromise the **Integrity & Availibility**
    - EX. manipulate / destroy data; disrupt business; ransomware; DoS Attack

## Objectives
    - If previous techniques successful the attackers would be able to perform their main objective (financial, info, political).

## Further Rooms for Study:

    - Principles of Security
    - Pentesting Fundamentals
    - ~~Cyber Kill Chain~~
    


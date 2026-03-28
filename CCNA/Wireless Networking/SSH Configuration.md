================================================================================
                    CCNA SSH CONFIGURATION CHEAT SHEET
================================================================================

PREREQUISITES FOR SSH
================================================================================
1. Hostname must be configured
2. Domain name must be configured
3. RSA crypto keys must be generated
4. Enable password or enable secret must be set
5. Local username database configured (for SSH authentication)


BASIC SSH CONFIGURATION (Step-by-Step)
================================================================================

Step 1: Configure Hostname
---------------------------
Router(config)# hostname R1

Step 2: Configure Domain Name
------------------------------
R1(config)# ip domain-name example.com

Step 3: Generate RSA Keys
--------------------------
R1(config)# crypto key generate rsa
  [Choose modulus size: 1024 or 2048 bits recommended]
  [2048 bits = more secure, required for SSHv2]

Step 4: Create Local User Account
----------------------------------
R1(config)# username admin privilege 15 secret Cisco123!
  [privilege 15 = full admin access]
  [Use 'secret' NOT 'password' - uses stronger encryption]

Step 5: Enable SSH on VTY Lines
--------------------------------
R1(config)# line vty 0 15
R1(config-line)# transport input ssh
R1(config-line)# login local
R1(config-line)# exec-timeout 5 0
R1(config-line)# exit

Step 6: (Optional) Force SSHv2 Only
------------------------------------
R1(config)# ip ssh version 2


COMPLETE BEST PRACTICE CONFIGURATION
================================================================================

hostname R1
!
ip domain-name example.com
!
! Generate 2048-bit keys for strong security
crypto key generate rsa modulus 2048
!
! Create administrative user with privilege 15
username admin privilege 15 secret Str0ngP@ssw0rd!
!
! Force SSH version 2 only (more secure than v1)
ip ssh version 2
!
! Set SSH timeout and authentication retries
ip ssh time-out 60
ip ssh authentication-retries 3
!
! Configure VTY lines for SSH-only access
line vty 0 15
 transport input ssh
 login local
 exec-timeout 5 0
 logging synchronous
!
! Enable password for console access
enable secret En@bleP@ss123!
!
! Configure console line
line console 0
 logging synchronous
 exec-timeout 5 0
!


SSH VERIFICATION COMMANDS
================================================================================

Show SSH Status
---------------
R1# show ip ssh
  [Shows SSH version, timeout, auth retries, enabled status]

Show Active SSH Sessions
-------------------------
R1# show ssh
  [Shows current SSH connections and session details]

Show Crypto Keys
----------------
R1# show crypto key mypubkey rsa
  [Displays the RSA public key]

Test SSH Connection
-------------------
R1# ssh -l admin 192.168.1.1
  [Connects via SSH to specified IP using username 'admin']


SECURITY BEST PRACTICES
================================================================================

1. KEY LENGTH
   - Use 2048-bit keys minimum (CCNA standard)
   - 1024 bits is acceptable but less secure
   - 4096 bits provides maximum security (overkill for CCNA)

2. SSH VERSION
   - Always use "ip ssh version 2" command
   - SSHv1 has known vulnerabilities
   - SSHv2 is required for modern security standards

3. VTY LINE SECURITY
   - Use "transport input ssh" (NOT telnet)
   - Never use "transport input all" in production
   - Enable "login local" for local authentication
   - Set "exec-timeout" to prevent idle sessions

4. PASSWORD SECURITY
   - Use "secret" instead of "password" (MD5 hashing)
   - Create strong passwords with mixed characters
   - Set privilege levels appropriately (15 = full access)

5. ADDITIONAL HARDENING
   - Configure "ip ssh authentication-retries 3"
   - Set "ip ssh time-out 60" (seconds)
   - Enable "service password-encryption" globally
   - Use ACLs to restrict SSH access by IP (advanced)

6. LOGGING
   - Enable "logging synchronous" on VTY lines
   - Prevents console messages from interrupting typing


COMMON TROUBLESHOOTING
================================================================================

Problem: "% Please create RSA keys to enable SSH"
Solution: Generate RSA keys with "crypto key generate rsa"

Problem: "% Incomplete command"
Solution: Ensure hostname AND domain name are configured first

Problem: SSH connection refused
Solution: 
  - Verify "transport input ssh" on VTY lines
  - Check if SSH is enabled: "show ip ssh"
  - Verify RSA keys exist: "show crypto key mypubkey rsa"

Problem: Authentication fails
Solution:
  - Verify username/password with "show run | include username"
  - Ensure "login local" is configured on VTY lines
  - Check user privilege level

Problem: Can't generate keys larger than 512 bits
Solution: IOS version doesn't support it; upgrade IOS or use 512


DELETING AND REGENERATING SSH KEYS
================================================================================

Delete Existing Keys
--------------------
R1(config)# crypto key zeroize rsa
  [WARNING: This will delete all RSA keys and disable SSH]

Regenerate Keys
---------------
R1(config)# crypto key generate rsa modulus 2048
  [Creates new keys with 2048-bit modulus]


TELNET VS SSH COMPARISON (Know for CCNA)
================================================================================

TELNET:
  - Unencrypted (plain text)
  - TCP port 23
  - Insecure, should NOT be used
  - Command: "transport input telnet"

SSH:
  - Encrypted connection
  - TCP port 22
  - Industry standard for remote access
  - Command: "transport input ssh"

BOTH:
  - Command: "transport input ssh telnet"
  - NOT recommended for production


QUICK REFERENCE - MINIMUM VIABLE SSH CONFIG
================================================================================

hostname R1
ip domain-name lab.local
crypto key generate rsa
  [Choose 1024 or 2048]
username admin secret cisco
line vty 0 15
 transport input ssh
 login local


EXAM TIPS
================================================================================

1. SSH requires THREE things before keys can be generated:
   - Hostname configured
   - Domain name configured
   - Then you can generate RSA keys

2. Know the difference between:
   - "password" = weak, Type 7 encryption
   - "secret" = strong, MD5 hashing (Type 5)

3. "transport input ssh" = SSH only (most secure)
   "transport input telnet" = Telnet only (insecure)
   "transport input all" = Both (avoid in production)

4. VTY lines 0-15 = 16 simultaneous connections possible

5. "login local" uses the local username database
   "login" uses line password only (less secure)

6. Default SSH timeout = 120 seconds
   Default authentication retries = 3

7. SSH uses TCP port 22 (know this for ACL questions)

8. "privilege 15" = full admin, equivalent to enable mode


ADVANCED TOPICS (Beyond Basic CCNA)
================================================================================

SSH with AAA Authentication
----------------------------
aaa new-model
aaa authentication login default local
aaa authorization exec default local

SSH Access Control List
------------------------
ip access-list standard SSH-ACCESS
 permit 192.168.1.0 0.0.0.255
 deny any log
!
line vty 0 15
 access-class SSH-ACCESS in

Public Key Authentication (IOS 15.0+)
--------------------------------------
ip ssh pubkey-chain
 username admin
  key-string
   [paste RSA public key here]
  exit


SAMPLE LAB SCENARIO
================================================================================

Configure SSH access on Router R1:
- Domain: ccna.lab
- Username: netadmin, Password: CCNA2024!
- 2048-bit encryption
- SSH version 2 only
- 5-minute timeout on VTY lines
- Allow up to 3 authentication attempts

SOLUTION:
---------
R1(config)# hostname R1
R1(config)# ip domain-name ccna.lab
R1(config)# crypto key generate rsa modulus 2048
R1(config)# username netadmin privilege 15 secret CCNA2024!
R1(config)# ip ssh version 2
R1(config)# ip ssh authentication-retries 3
R1(config)# line vty 0 15
R1(config-line)# transport input ssh
R1(config-line)# login local
R1(config-line)# exec-timeout 5 0
R1(config-line)# logging synchronous
R1(config-line)# exit
R1(config)# enable secret Enable123!


================================================================================
                              END OF CHEAT SHEET
================================================================================

Pro tip for your CCNA lab: Practice this configuration until you can do it
from memory in under 2 minutes. SSH configuration is a common exam task!

Good luck with your February exam, Sean! You've got this! 🔒
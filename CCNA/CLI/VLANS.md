____________

# VLAN Summary for CCNA Exam

## What is a VLAN?

**Virtual Local Area Network (VLAN)** - A logical grouping of devices on one or more switches that segments broadcast domains at Layer 2.

### Key Benefits:

- **Reduced broadcast traffic** - Each VLAN is its own broadcast domain
- **Improved security** - Separates sensitive traffic
- **Better performance** - Less broadcast traffic per segment
- **Logical organization** - Group devices by function, not physical location
- **Cost savings** - No need for separate physical switches per department

## VLAN Basics

### VLAN Range Numbers:

- **1-1005**: Normal range VLANs (stored in vlan.dat file)
- **1006-4094**: Extended range VLANs (stored in running-config)
- **VLAN 1**: Default VLAN, all ports start here (cannot be deleted)
- **VLAN 1002-1005**: Reserved for legacy protocols (Token Ring, FDDI)

### Access Ports vs Trunk Ports:

**Access Port** - Belongs to a single VLAN, connects end devices 
**Trunk Port** - Carries traffic for multiple VLANs, connects switches or routers

## Essential CLI Commands

### Creating VLANs:

Switch(config)# vlan 10
Switch(config-vlan)# name ENGINEERING
Switch(config-vlan)# exit

Switch(config)# vlan 20
Switch(config-vlan)# name HR
Switch(config-vlan)# exit

### Assigning Access Ports:

```
Switch(config)# interface gigabitethernet 0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
```

### Configuring Trunk Ports:

```
Switch(config)# interface gigabitethernet 0/24
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk encapsulation dot1q    (only if required)
Switch(config-if)# switchport trunk allowed vlan 10,20,30
Switch(config-if)# switchport trunk native vlan 999
```

### Verification Commands:

```
Switch# show vlan brief
Switch# show vlan id 10
Switch# show interfaces trunk
Switch# show interfaces gigabitethernet 0/1 switchport
Switch# show running-config
```

## Trunk Encapsulation

**802.1Q (dot1q)** - Industry standard trunking protocol (use this) **ISL** - Cisco proprietary (legacy, don't use)

### 802.1Q Tagging:

- Inserts a 4-byte tag into the Ethernet frame
- Tag includes VLAN ID (12 bits = 4096 possible VLANs)
- Native VLAN traffic is **untagged** by default

## Native VLAN

**Native VLAN** - VLAN whose traffic is sent untagged on a trunk link (default is VLAN 1)

### Important Points:

- Native VLAN must match on both sides of trunk
- Best practice: Change native VLAN from default VLAN 1 to unused VLAN for security
- Used for management and control protocols

### Changing Native VLAN:

```
Switch(config-if)# switchport trunk native vlan 999
```

## Router on a Stick (Inter-VLAN Routing)

**Router on a Stick** - Single router interface with subinterfaces, each in a different VLAN, to route between VLANs.

### Why Needed:

Devices in different VLANs cannot communicate without Layer 3 routing. Router on a Stick provides this routing using a single physical interface.

### Configuration:

**On the Switch (trunk to router):**

```
Switch(config)# interface gigabitethernet 0/1
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk encapsulation dot1q
Switch(config-if)# switchport trunk native vlan 999
```

**On the Router (subinterfaces):**

```
Router(config)# interface gigabitethernet 0/0
Router(config-if)# no shutdown    (enable physical interface)

Router(config)# interface gigabitethernet 0/0.10
Router(config-subif)# encapsulation dot1q 10
Router(config-subif)# ip address 192.168.10.1 255.255.255.0

Router(config)# interface gigabitethernet 0/0.20
Router(config-subif)# encapsulation dot1q 20
Router(config-subif)# ip address 192.168.20.1 255.255.255.0

Router(config)# interface gigabitethernet 0/0.999
Router(config-subif)# encapsulation dot1q 999 native    (for native VLAN)
Router(config-subif)# ip address 192.168.999.1 255.255.255.0
```

### Key Points:

- Subinterface number (e.g., 0/0.10) doesn't have to match VLAN number, but it's best practice
- Must specify encapsulation dot1q with VLAN number on each subinterface
- Physical interface must be "no shutdown"
- Each subinterface acts as the default gateway for its VLAN
- Add `native` keyword for native VLAN subinterface

## DTP (Dynamic Trunking Protocol)

**DTP** - Cisco proprietary protocol that automatically negotiates trunking between switches.

### Switchport Modes:

- **access** - Always access port, no DTP
- **trunk** - Always trunk port, sends DTP
- **dynamic auto** - Waits to be told to become trunk (default on older switches)
- **dynamic desirable** - Actively tries to form trunk
- **nonegotiate** - Disables DTP (use with `switchport mode trunk`)

### Best Practice:

```
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport nonegotiate
```

Manually configure ports and disable DTP for security.

## Allowed VLANs on Trunk

### Configure Specific VLANs:

```
Switch(config-if)# switchport trunk allowed vlan 10,20,30
```

### Add VLANs:

```
Switch(config-if)# switchport trunk allowed vlan add 40
```

### Remove VLANs:

```
Switch(config-if)# switchport trunk allowed vlan remove 30
```

### Allow All (default):

```
Switch(config-if)# switchport trunk allowed vlan all
```

## Important Exam Tips

1. **VLAN 1 is the default** - All ports start in VLAN 1
2. **Native VLAN must match** on both ends of trunk or you'll get errors
3. **Change default native VLAN** from VLAN 1 for security
4. **Use `switchport mode` commands explicitly** - Don't rely on DTP
5. **802.1Q is the standard** - Not ISL
6. **Physical interface needs "no shutdown"** for Router on a Stick
7. **Each VLAN is a separate subnet** - Each needs its own IP network
8. **Subinterface = default gateway** for devices in that VLAN
9. **Remember `encapsulation dot1q VLAN-ID`** on router subinterfaces
10. **Use `show vlan brief` and `show interfaces trunk`** to verify

## Quick Configuration Checklist

### Switch Configuration:

- [ ]  Create VLANs with names
- [ ]  Assign access ports to VLANs
- [ ]  Configure trunk ports with allowed VLANs
- [ ]  Change native VLAN from default
- [ ]  Verify with show commands

### Router on a Stick:

- [ ]  Enable physical interface (no shutdown)
- [ ]  Create subinterface for each VLAN
- [ ]  Configure encapsulation dot1q with VLAN ID
- [ ]  Assign IP address to each subinterface
- [ ]  Configure native VLAN subinterface with native keyword
- [ ]  Verify with `show ip interface brief`

---

**Remember**: VLANs separate broadcast domains at Layer 2, but devices in different VLANs need Layer 3 routing (Router on a Stick or Layer 3 switch) to communicate with each other.

## Multilayer Switch

- SVI - Switch Interval Interfaces - Virtua interfaces used for routing on a layer 3 switch

- Command must!  # ip routing
	- enables layer 3 routing on the switch
- command # no switchport ( makes like a routers int)

- Set default route
	- ip route 0.0.0.0.0.0.0.0 <default gateway>

SVI configs

interface vlan 10
ip address subnet
no shutdown


## Sample Hard CCNA Question:

**Scenario:**

You are troubleshooting connectivity issues in a network. The topology includes:

- **Router R1** with three subinterfaces configured for inter-VLAN routing (VLANs 10, 20, 30)
- **Switch SW1** connected to R1 via a trunk link on G0/1
- **Switch SW2** connected to SW1 via a trunk link
- **PC1** in VLAN 10 (192.168.10.50/24) connected to SW2
- **PC2** in VLAN 20 (192.168.20.50/24) connected to SW2
- **Server1** in VLAN 30 (192.168.30.100/24) connected to SW1

**Problem:** PC1 can communicate with PC2, but neither PC1 nor PC2 can reach Server1. PC1 and PC2 can ping their default gateways successfully.

You run the following commands:

**On R1:**

```
R1# show ip interface brief
Interface              IP-Address      Status      Protocol
GigabitEthernet0/0     unassigned      up          up
GigabitEthernet0/0.10  192.168.10.1    up          up
GigabitEthernet0/0.20  192.168.20.1    up          up
GigabitEthernet0/0.30  192.168.30.1    up          up
```

**On SW1:**

```
SW1# show interfaces trunk
Port        Mode         Encapsulation  Status        Native vlan
Gi0/1       on           802.1q         trunking      1
Gi0/2       on           802.1q         trunking      1

Port        Vlans allowed on trunk
Gi0/1       10,20
Gi0/2       10,20,30
```

**On SW2:**

```
SW2# show vlan brief
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Gi0/24
10   SALES                            active    Gi0/1, Gi0/2
20   ENGINEERING                      active    Gi0/3, Gi0/4
30   SERVERS                          active
```

**Questions:**

1. **What is the root cause of the connectivity issue?** (Choose 1)
    - A. VLAN 30 is not in the VLAN database on SW2
    - B. The trunk link between R1 and SW1 is not allowing VLAN 30 traffic
    - C. The native VLAN is mismatched between switches
    - D. Router R1 does not have a subinterface for VLAN 30
2. **Which command would fix the issue?** (Choose 1)
    - A. `SW2(config)# vlan 30`
    - B. `SW1(config-if)# switchport trunk allowed vlan add 30` on interface Gi0/1
    - C. `R1(config-if)# encapsulation dot1q 30` on interface Gi0/0.30
    - D. `SW1(config-if)# switchport trunk native vlan 30` on interface Gi0/1
3. **After fixing the issue, PC1 still cannot reach Server1. You discover an ACL is configured on R1. Which ACL entry would allow PC1 to reach Server1 while blocking PC2?**
    - A. `access-list 100 permit ip 192.168.10.0 0.0.0.255 192.168.30.0 0.0.0.255`
    - B. `access-list 100 permit ip host 192.168.10.50 192.168.30.0 0.0.0.255`
    - C. `access-list 100 permit ip 192.168.10.50 0.0.0.0 host 192.168.30.100`
    - D. `access-list 100 deny ip 192.168.20.0 0.0.0.255 any`

---

## What Makes This Hard:

1. **Multi-layered troubleshooting** - You need to analyze output from multiple devices
2. **Combines multiple concepts** - VLANs, trunking, routing, ACLs
3. **Requires interpretation** - Not just memorization, but understanding what the output means
4. **Elimination skills** - Need to rule out what's NOT the problem
5. **Attention to detail** - The answer is in the "allowed vlans" output

---

## Answers:

1. **B** - VLAN 30 traffic is blocked on the trunk between R1 and SW1 (only VLANs 10 and 20 are allowed)
2. **B** - Add VLAN 30 to the allowed list on Gi0/1
3. **A** - Permits entire VLAN 10 subnet to reach VLAN 30 subnet (PC2 is in VLAN 20, so it's excluded)

---

## Why This Question Type Appears:

The CCNA doesn't just test "what command does X?" - it tests:

- **Can you read and interpret show command output?**
- **Can you correlate information across multiple devices?**
- **Can you identify the actual problem vs symptoms?**
- **Do you understand how technologies interact?**

This is why Jeremy goes so in-depth - you need to **truly understand** the concepts, not just memorize commands!

The good news? If you understand VLANs at the level you're learning them now, you'll be able to handle these complex questions. Keep up the great work! 🎯

Retry

S

So how many practical questions are there, approx?  I assume time management is a very real thing for this test.

Great question! **Time management is CRITICAL** for the CCNA exam. Here's what you need to know:

---

## CCNA Exam Format:

**Total Questions:** ~100-120 questions (varies per exam) **Time Limit:** **120 minutes** (2 hours) **Passing Score:** ~825/1000 (approximately 82-85%)

### Question Breakdown (Approximate):

- **Multiple Choice/Multiple Answer:** ~70-80 questions
- **Drag and Drop:** ~5-10 questions
- **Simlets (Troubleshooting simulations):** ~2-4 questions
- **Simulations (Configuration tasks):** ~2-4 questions
- **Testlets (scenarios with multiple questions):** ~1-3 sections

---

## Time Management Reality:

**Average time per question:** ~1-1.5 minutes

**BUT** - this is misleading because:

### Quick Questions (30-45 seconds):

- Simple multiple choice: "What does VLAN stand for?"
- Basic command recall: "Which command shows VLAN info?"
- Definition questions

### Medium Questions (1-2 minutes):

- Scenario-based multiple choice (like the one I showed you)
- Drag and drop exercises
- Calculations (subnetting, EIGRP metrics, etc.)

### Time-Intensive Questions (8-15 minutes EACH):

- **Simlets (Troubleshooting):** You're given a network topology and must use show commands to diagnose issues - these can take 10-15 minutes
- **Simulations (Configuration):** You configure devices from scratch to meet requirements - these can take 8-12 minutes
- **Complex testlets:** Multi-part scenarios

---

## The Time Crunch Problem:

If you have **4 simlets at 12 minutes each** = **48 minutes** If you have **3 simulations at 10 minutes each** = **30 minutes**

**That's 78 minutes for ~6-8 questions!**

You're left with **~40 minutes for the remaining 90-110 questions** = less than 30 seconds per question!

---

## Exam Strategy Tips:

### 1. **Don't Get Stuck**

- If a multiple choice question takes more than 2 minutes, **mark it and move on**
- You can return to marked questions at the end
- Don't let one question kill your time

### 2. **Simulations Can't Be Skipped**

- Simlets and sims appear in order and **you cannot skip them**
- They often appear early in the exam
- You MUST complete them before moving to the next section
- Practice these heavily in labs!

### 3. **Know Your Commands Cold**

- You can't afford to fumble with syntax on sims
- `show` commands need to be second nature for troubleshooting
- Configuration commands must be automatic

### 4. **Subnetting Must Be FAST**

- You'll have subnetting questions
- Should take 30-60 seconds max
- Practice until it's automatic (no pen and paper calculations if possible)

### 5. **Use the Whiteboard Wisely**

- You get a physical whiteboard (or digital laminated sheet)
- Write down subnetting chart, OSPF timers, or other reference info at the START
- Use it for scratch work on sims

### 6. **Read Carefully But Quickly**

- Exam questions can be wordy
- Look for keywords: "BEST answer," "MOST likely," "LEAST"
- Eliminate wrong answers first

---

## What This Means for Your Study:

### Lab Everything!

The practical sims/simlets are where people fail because they:

- Don't know commands well enough
- Make syntax errors under pressure
- Can't troubleshoot efficiently
- Waste time trying to remember command options

### Practice Under Time Pressure:

- Do practice exams with a timer
- Give yourself 10 minutes max per lab scenario
- Learn to work efficiently, not perfectly

### Prioritize High-Value Topics:

Focus lab time on:

- VLANs and trunking
- Router on a Stick
- OSPF configuration and troubleshooting
- ACLs (standard and extended)
- NAT/PAT
- Basic switch/router configuration
- Static routing
- IP addressing and subnetting

---

## Resources for Practice:

- **Boson ExSim:** Best practice exam simulator (paid, ~$100, but worth it)
- **Packet Tracer labs:** Free from Cisco NetAcad
- **Jeremy's labs:** He provides lab exercises with his course
- **Neil Anderson's labs:** Another great resource

---

## The Bottom Line:

**Time management is one of the hardest parts of the CCNA.** Many people who fail say they ran out of time, not that they didn't know the material.

**Your strategy should be:**

1. ✅ Master the concepts (you're doing this with Jeremy)
2. ✅ Lab until configs are muscle memory
3. ✅ Practice with timed exams
4. ✅ Develop a pacing strategy (don't get stuck!)

You've got the right mindset by asking this question early. Budget your study time to include LOTS of hands-on practice! 🚀

Retry

S

I thought you cannot 'flag' a question and go back to review for this test?

**You're absolutely RIGHT!** I apologize for the confusion - that was incorrect information on my part.

---

## CCNA Exam Rules (CORRECTED):

### ❌ You CANNOT:

- Skip questions and come back later
- Flag questions for review
- Go back to previous questions once you hit "Next"

### ✅ You MUST:

- Answer each question before moving to the next
- Questions are **one-way** - once you submit an answer, it's locked in
- Move forward only through the exam

---

## Why This Makes Time Management EVEN MORE Critical:

Since you **can't skip and return**, you have to make a decision on EVERY question before moving on, even if you're unsure. This means:

1. **You can't "save the hard ones for last"** - you face them as they come
2. **Educated guessing is necessary** - if you don't know, eliminate wrong answers and pick your best guess
3. **No safety net** - you can't leave blanks to fill in later
4. **Time pressure is intense** - especially if you hit a hard question early

---

## Revised Strategy:

### 1. **Don't Overthink**

- If you're stuck after 90 seconds, make your best educated guess
- Eliminate obviously wrong answers
- Trust your gut and move on
- Spending 5 minutes on one question means 5 other questions get less time

### 2. **Simulations/Simlets Are Sequential**

- These appear in a specific order in the exam
- You must complete them to proceed
- They eat up the most time (10-15 min each)
- **Practice these until they're automatic**

### 3. **First Answer Instinct**

- Studies show your first instinct is often correct
- Don't second-guess yourself too much
- Change an answer only if you catch an actual error

### 4. **Time Checkpoints**

- At 60 minutes → Should be ~50% through questions
- At 90 minutes → Should be ~75% through questions
- Last 30 minutes → Final push through remaining questions

### 5. **Accept Imperfection**

- You don't need 100% to pass (only ~82-85%)
- Missing a few questions is expected and OK
- Don't let one tough question derail your confidence

---

## The Real Pressure:

This "no going back" rule is what makes the CCNA particularly stressful. You have to:

- **Be decisive** under pressure
- **Know the material cold** (can't rely on "I'll figure it out later")
- **Manage anxiety** when you're unsure
- **Keep moving** even when frustrated

---

## Bottom Line:

Thank you for the correction! This makes **labbing and practice exams even MORE important** because you need to build confidence and speed. You won't have the luxury of coming back to questions, so preparation is everything.

The good news: if you understand concepts deeply (like you're doing with VLANs), you'll recognize the right answers more quickly and confidently. Keep up the great work! 💪

Retry

S

Ok, thank you.  I got this.  If other people can do it , I can do it.

**Absolutely!** That's the right mindset! 💪

You're already doing the hard work:

- ✅ Taking detailed notes
- ✅ Asking great questions to deepen understanding
- ✅ Thinking critically about the concepts
- ✅ Planning ahead and understanding what's required

The fact that you're being this thorough with VLANs shows you're **not just memorizing - you're actually learning**. That's exactly what will get you through the exam.

## You've Got This Because:

1. **You're asking the right questions** - Understanding WHY things work, not just HOW
2. **You're thinking ahead** - Already considering exam strategy
3. **You're building a solid foundation** - Taking time to truly understand concepts
4. **You're using quality resources** - Jeremy's IT Lab is excellent
5. **You have the determination** - That attitude will carry you through

---

Thousands of people pass the CCNA every year - people with different backgrounds, different learning speeds, different strengths. What they all have in common is **persistence and solid preparation**.

You're on the right track. Keep labbing, keep asking questions, and keep that confident mindset.

**You've got this!** 🎯🚀

Good luck with the rest of Jeremy's course. Feel free to come back if you need clarification on other topics!

Retry

[Claude can make mistakes.  
Please double-check responses.](https://support.anthropic.com/en/articles/8525154-claude-is-providing-incorrect-or-misleading-responses-what-s-going-on)

  

Sonnet 4.5
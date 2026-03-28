____________


# **CCNA Troubleshooting Trigger Words Guide**

---

## **OSPF - Neighbor Relationship Problems**

### **🔴 Trigger: "Neighbors won't form" or "Stuck in INIT state"**

**Keywords in question:**

- "INIT state"
- "No adjacency"
- "Neighbors not forming"
- "One-way communication"

**Most likely causes (in order):**

1. **Subnet mask mismatch** - routers on different subnets
2. **Hello/Dead timer mismatch**
3. **Area ID mismatch**
4. **Authentication mismatch**
5. **Network type mismatch**

**Clue words:**

- "recently changed timers" → Timer mismatch
- "different area" → Area mismatch
- "security enabled" → Authentication issue
- "can ping but no neighbor" → ACL blocking 224.0.0.5

---

### **🔴 Trigger: "Neighbors in 2-WAY state, not FULL"**

**Keywords:**

- "Stuck in 2-WAY"
- "Won't go to FULL"
- "DROther to DROther"

**This is NORMAL for:**

- DROther ↔ DROther on Ethernet (they stay in 2-WAY)

**This is WRONG for:**

- Router ↔ DR (should be FULL)
- Router ↔ BDR (should be FULL)

**Clue words:**

- "both are DROther" → Normal! ✓
- "one is DR" → Problem! Should be FULL

---

### **🔴 Trigger: "Routes not appearing" or "Can't reach networks"**

**Keywords:**

- "Routes missing"
- "Can ping neighbor but not remote networks"
- "Partial reachability"

**Most likely causes:**

1. **Passive interface** - neighbor can't form
2. **Network statement missing** - interface not in OSPF
3. **Wrong area** - route in different area
4. **ACL filtering routes**

**Clue words:**

- "interface not advertising" → Passive or missing network statement
- "one-way connectivity" → Passive interface (asymmetric routing)
- "can reach from one direction only" → Return path problem

---

### **🔴 Trigger: "Flapping" or "Unstable"**

**Keywords:**

- "Neighbor keeps going down"
- "Flapping adjacency"
- "Intermittent connectivity"

**Most likely causes:**

1. **Physical layer issue** - bad cable, duplex mismatch
2. **Dead timer too aggressive**
3. **MTU mismatch** (packets getting dropped)

**Clue words:**

- "interface errors" → Physical problem
- "drops every 40 seconds" → Dead timer expiring
- "large packets fail" → MTU mismatch

---

## **Spanning Tree Protocol (STP) - Trigger Words**

### **🔴 Trigger: "Broadcast storm" or "Network meltdown"**

**Keywords:**

- "High CPU"
- "Network flooding"
- "Duplicate frames"
- "Broadcast storm"
- "Network unresponsive"

**Most likely cause:**

- **STP disabled** or **loop in topology**

**Clue words:**

- "STP turned off" → Loop guaranteed!
- "recently added redundant link" → Possible loop
- "all ports forwarding" → No blocking port = loop!

---

### **🔴 Trigger: "Slow convergence" or "30-50 second outage"**

**Keywords:**

- "Long delay after topology change"
- "50 seconds of downtime"
- "Slow to recover"

**Most likely cause:**

- **Running classic STP** (not Rapid-PVST+)
- **PortFast not configured** on access ports

**Time clues:**

- "~50 seconds" → STP forward delay (15s listening + 15s learning + timers)
- "Immediately" → RSTP or PortFast working ✓

**Clue words:**

- "end-user port" + "slow DHCP" → Missing PortFast
- "access port" + "30 second delay" → Missing PortFast

---

### **🔴 Trigger: "Wrong root bridge" or "Suboptimal path"**

**Keywords:**

- "Using slow link"
- "Not using fastest path"
- "Wrong switch is root"
- "Old switch became root"

**Most likely cause:**

- **Root bridge priority not configured**
- **Auto-election picked wrong switch** (lowest MAC)

**Clue words:**

- "oldest switch" → Likely has lowest MAC = became root
- "priority not set" → Default 32768 on all = MAC decides
- "traffic going through slow link" → Wrong root bridge location

---

### **🔴 Trigger: "Port stuck in Blocking/Discarding"**

**Keywords:**

- "Port won't forward"
- "Port blocked"
- "Designated port not elected"

**Most likely cause:**

- **Normal STP operation** (this port has higher cost)
- **BPDU Guard triggered** (if access port got BPDU)
- **Root Guard triggered** (if superior BPDU received)

**Clue words:**

- "access port" + "err-disabled" → BPDU Guard
- "should be forwarding" → Check port cost/priority

---

## **VLAN/Trunking - Trigger Words**

### **🔴 Trigger: "Can't communicate across VLANs"**

**Keywords:**

- "VLAN 10 can't reach VLAN 20"
- "Inter-VLAN routing not working"
- "Same switch, different VLANs, can't communicate"

**Most likely causes:**

1. **No inter-VLAN routing** configured
2. **SVI shut down**
3. **Trunk not carrying VLAN**
4. **Wrong VLAN on port**

**Clue words:**

- "Layer 2 switch only" → Need router or Layer 3 switch!
- "SVI down" → Use `no shutdown`
- "VLAN allowed" → Check trunk allowed list

---

### **🔴 Trigger: "Native VLAN mismatch"**

**Keywords:**

- "CDP warning about native VLAN"
- "Some traffic works, some doesn't"
- "Untagged traffic"

**Most likely cause:**

- **Native VLAN different on each side of trunk**

**What happens:**

- Trunk still forms! (This is the trap!)
- But traffic leaks between VLANs
- Security risk

**Clue words:**

- "VLAN 1 traffic appearing in VLAN 99" → Native mismatch
- "CDP neighbor warning" → Check native VLAN

---

### **🔴 Trigger: "Trunk not forming" or "Access mode"**

**Keywords:**

- "Should be trunk but showing access"
- "Only VLAN 1 traffic passing"
- "Trunk negotiation failed"

**Most likely causes:**

1. **Mode mismatch** - one side `trunk`, other side `access`
2. **DTP disabled** - both sides `dynamic`
3. **Encapsulation not set** (older switches)

**Clue words:**

- "one side configured trunk" → Check other side!
- "both dynamic" → DTP disabled, manually configure
- "switchport mode access" → Change to trunk

---

## **EtherChannel - Trigger Words**

### **🔴 Trigger: "EtherChannel suspended" or "Not bundling"**

**Keywords:**

- "Ports suspended"
- "Interface shows (s)"
- "Won't bundle"
- "Individual ports, not port-channel"

**Most likely causes:**

1. **Speed mismatch** (one 100M, one 1G)
2. **Duplex mismatch**
3. **VLAN mismatch** (if access ports)
4. **Trunk config mismatch** (if trunk)
5. **Mode mismatch** (physical = access, Po = trunk)

**Clue words:**

- "(s)" in show command → Suspended!
- "different speeds" → Won't form
- "Physical interface access, Port-Channel trunk" → Config mismatch

---

### **🔴 Trigger: "LACP/PAgP won't negotiate"**

**Keywords:**

- "Passive/Passive"
- "Auto/Auto"
- "EtherChannel protocol mismatch"

**Most likely cause:**

- **Both sides passive** - nobody initiates

**Remember:**

- **LACP:** Active + Active ✓, Active + Passive ✓, Passive + Passive ✗
- **PAgP:** Desirable + Desirable ✓, Desirable + Auto ✓, Auto + Auto ✗

**Clue words:**

- "both passive" → Won't form!
- "both auto" → Won't form!

---

## **Routing (General) - Trigger Words**

### **🔴 Trigger: "Can ping, can't browse web" or "Partial connectivity"**

**Keywords:**

- "Ping works, applications don't"
- "Can reach some sites, not others"
- "Small packets OK, large packets fail"

**Most likely cause:**

- **MTU mismatch** or **fragmentation issue**

**Clue words:**

- "large file transfers fail" → MTU problem
- "ping works (small packets), HTTP fails (larger)" → MTU

---

### **🔴 Trigger: "Asymmetric routing" or "One direction works"**

**Keywords:**

- "Can reach from A to B, but not B to A"
- "Traceroute shows different paths"
- "Reply packets not arriving"

**Most likely causes:**

1. **Missing return route**
2. **Firewall/ACL blocking return traffic**
3. **Passive interface** (we saw this!)

**Clue words:**

- "forward path works, return fails" → Missing route on destination
- "can initiate from one side only" → Return path missing

---

### **🔴 Trigger: "Routing loop" or "TTL exceeded"**

**Keywords:**

- "TTL expired"
- "Packet looping"
- "Increasing hop count"

**Most likely causes:**

1. **Routing loop** - two routers pointing at each other
2. **Incorrect static route**
3. **Route redistribution issue**

**Clue words:**

- "static routes pointing at each other" → Loop!
- "traceroute shows repeated hops" → Loop

---

## **Static Routes - Trigger Words**

### **🔴 Trigger: "Route not in table" or "Can't reach destination"**

**Keywords:**

- "Static route configured but not working"
- "Route not appearing"

**Most likely causes:**

1. **Next hop unreachable** (no route to next-hop)
2. **Exit interface down**
3. **AD higher than another route** (floating static not activating)

**Clue words:**

- "next-hop not reachable" → Need route to next-hop first!
- "interface down" → Static route invalid
- "shows in config but not in table" → Check next-hop reachability

---

## **Access Control Lists (ACLs) - Trigger Words**

### **🔴 Trigger: "Some traffic blocked, some allowed"**

**Keywords:**

- "Can ping but can't telnet"
- "ICMP works, TCP doesn't"
- "Specific ports blocked"

**Most likely cause:**

- **ACL filtering specific protocols/ports**

**Clue words:**

- "ping works" → ICMP allowed
- "SSH fails" → TCP port 22 blocked
- "can browse, can't FTP" → Port 21 blocked

---

### **🔴 Trigger: "Everything blocked" or "Nothing works"**

**Keywords:**

- "All traffic denied"
- "Complete loss of connectivity after ACL applied"

**Most likely cause:**

- **Implicit deny all** at end of ACL
- **ACL applied in wrong direction**
- **No permit statements**

**Clue words:**

- "inbound vs outbound" → Check direction!
- "ACL has only deny statements" → Need permit!
- "recently applied ACL" → Implicit deny blocking everything

---

## **DHCP - Trigger Words**

### **🔴 Trigger: "Can't get IP address" or "APIPA address"**

**Keywords:**

- "Client showing 169.254.x.x"
- "DHCP failing"
- "No IP address assigned"

**Most likely causes:**

1. **DHCP server down/unreachable**
2. **DHCP relay not configured** (client on different subnet)
3. **DHCP pool exhausted**
4. **Switchport not forwarding** (STP delay without PortFast)

**Clue words:**

- "different subnet than DHCP server" → Need `ip helper-address`
- "169.254.x.x" → DHCP failed, using APIPA
- "30-second delay" → STP issue, need PortFast
- "all addresses used" → Pool exhausted

---

## **NAT - Trigger Words**

### **🔴 Trigger: "Inside can't reach outside" or "No translation"**

**Keywords:**

- "NAT not working"
- "Inside local can't reach internet"
- "Translation not occurring"

**Most likely causes:**

1. **ACL not matching traffic**
2. **Inside/outside not designated correctly**
3. **NAT pool exhausted**

**Clue words:**

- "no translation in NAT table" → ACL not matching
- "interface not marked inside/outside" → Missing designation
- "all addresses used" → Pool exhausted

---

## **Quick Reference - "Best Answer" Trigger Words**

**When question says:**

- **"First thing to check"** → Physical layer (cables, interfaces up/up)
- **"Most likely cause"** → Most common issue (timers, ACL, config typo)
- **"Best practice"** → Manual config, security-focused, scalable solution
- **"Immediate fix"** → Quick command (clear, reload, no shutdown)
- **"Long-term solution"** → Design change, protocol change, upgrade

**Time-based clues:**

- **"Immediately after change"** → That change caused it!
- **"Intermittent"** → Physical layer, flapping, resource exhaustion
- **"After 30-40 seconds"** → Timer-related (OSPF dead, STP)
- **"Every few minutes"** → Update interval (RIP 30s, routing table updates)

---

# **Exam Strategy - Multi-Choice Troubleshooting**

**Read the question for these patterns:**

1. **Identify the symptom** (what's broken?)
2. **Note any recent changes** (what changed before break?)
3. **Check time indicators** (when/how long?)
4. **Look for command output clues** (what do you see?)
5. **Eliminate obviously wrong answers**
6. **Pick the MOST LIKELY cause** (not just possible)
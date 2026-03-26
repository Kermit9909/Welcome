
# QoS (Quality of Service) - CCNA Cheat Sheet

## What is QoS?

**Quality of Service (QoS)** - Set of tools and techniques to manage network traffic and ensure critical applications receive adequate bandwidth and priority during congestion.

### Key Concept

- QoS is **only relevant during congestion**
- Without congestion, all traffic flows normally
- QoS manages which traffic gets dropped/delayed when bandwidth is insufficient

---

## Why QoS Matters

### Types of Traffic Characteristics

**1. Voice Traffic**

- Extremely time-sensitive
- Low bandwidth requirements (~30-128 Kbps per call)
- **Intolerant of delays and jitter**
- Can tolerate some packet loss (dropped audio segments)

**2. Video Traffic**

- Time-sensitive but less than voice
- Higher bandwidth requirements
- **Intolerant of delays and jitter**
- Can tolerate minimal packet loss

**3. Data Traffic**

- Generally not time-sensitive (exceptions: real-time trading, gaming)
- Variable bandwidth requirements
- **Tolerant of delays**
- Intolerant of packet loss (TCP retransmits, but impacts performance)

---

## QoS Traffic Classifications

### Standard Traffic Classes (RFC 4594)

1. **Voice** - Highest priority, strict low latency requirements
2. **Interactive Video** - Video conferencing, real-time collaboration
3. **Streaming Video** - One-way video (YouTube, Netflix)
4. **Network Control** - Routing protocols, network management
5. **Mission Critical Data** - Business-critical applications
6. **Transactional Data** - Interactive applications (web browsing, email)
7. **Bulk Data** - FTP, backup operations
8. **Scavenger** - Non-business traffic, lowest priority

---

## Queuing Fundamentals

### FIFO (First In, First Out)

- **Default queuing method** on Cisco devices
- Single queue, processes packets in arrival order
- **No QoS capability** - all traffic treated equally
- Simple but ineffective during congestion

### Priority Queuing Basics

- Multiple queues with different priority levels
- Higher priority queues serviced first
- Prevents important traffic from being delayed by bulk data

---

## QoS Mechanisms

### 1. Classification & Marking

**Purpose:** Identify and tag traffic for QoS treatment

**Common Marking Methods:**

- **PCP (Priority Code Point)** - Layer 2, 802.1Q header, 3 bits (0-7)
- **DSCP (Differentiated Services Code Point)** - Layer 3, IP header, 6 bits (0-63)
- **IP Precedence** - Legacy Layer 3, IP header, 3 bits (0-7)

**Key DSCP Values to Know:**

- **Default (DF)** - 0 - Best effort traffic
- **Expedited Forwarding (EF)** - 46 - Voice traffic
- **Assured Forwarding (AF)** - Multiple classes (AF41, AF31, etc.)
- **Class Selector (CS)** - Backward compatible with IP Precedence

**Trust Boundaries:**

- Point where device trusts QoS markings from another device
- Typically at distribution/core switches
- Access switches often re-mark traffic from end devices

---

### 2. Policing & Shaping

**Both control traffic rate, but differently**

**Policing:**

- **Drops or remarks** excess traffic immediately
- Traffic rate limit enforced **instantaneously**
- Can cause TCP retransmissions
- Used on ingress or egress
- More aggressive, can impact TCP performance

**Shaping:**

- **Buffers/delays** excess traffic
- Creates smoother traffic flow
- Prevents TCP slowdowns
- **Only used on egress**
- Better for TCP applications

**When to Use:**

- **Policing:** Provider edge, strict enforcement needed
- **Shaping:** Customer edge, smooth traffic flow desired

---

### 3. Congestion Management (Queuing)

**Scheduling Methods:**

**Class-Based Weighted Fair Queuing (CBWFQ):**

- Multiple traffic classes with guaranteed bandwidth
- Each class gets minimum bandwidth percentage
- Remaining bandwidth shared proportionally
- **Does NOT provide strict priority**

**Low Latency Queuing (LLQ):**

- CBWFQ + strict priority queue
- Priority queue for time-sensitive traffic (voice/video)
- Priority queue serviced first, always
- Other queues use CBWFQ scheduling
- **Recommended for voice/video networks**

**Weighted Round Robin (WRR):**

- Services queues in rotation
- Each queue assigned weight (determines service frequency)
- No strict priority option

---

### 4. Congestion Avoidance

**Problem:** Tail drop causes TCP global synchronization

- When queue fills, newly arriving packets dropped (tail drop)
- Multiple TCP flows slow down simultaneously
- Then speed up simultaneously
- Creates traffic waves (inefficient)

**Solution: Weighted Random Early Detection (WRED)**

- **Randomly drops packets BEFORE queue fills**
- Drop probability increases as queue fills
- Prevents global TCP synchronization
- Different drop probabilities based on IP Precedence/DSCP
- Higher priority traffic less likely to be dropped

**WRED Benefits:**

- Prevents TCP global synchronization
- Maintains high link utilization
- Provides differentiated treatment for different classes

---

## QoS Models

### 1. Best Effort

- **No QoS** - Default Internet model
- All packets treated equally
- Simple, no overhead
- No guarantees

### 2. Integrated Services (IntServ)

- **Resource Reservation Protocol (RSVP)**
- Applications reserve exact bandwidth end-to-end
- Per-flow state maintained on all routers
- **Not scalable** - too much overhead
- Rarely used in modern networks

### 3. Differentiated Services (DiffServ)

- **Most common QoS model**
- Marks packets with DSCP values
- Routers apply per-hop behaviors (PHB)
- **Scalable** - no per-flow state
- **Standard for enterprise/SP networks**

---

## QoS Deployment Tips

### Three-Step QoS Approach

1. **Classification & Marking** - Identify and tag traffic
2. **Queuing** - Provide bandwidth guarantees
3. **Congestion Avoidance** - Prevent global synchronization (optional)

### Best Practices

- Mark traffic as close to source as possible
- Use trust boundaries appropriately
- Voice gets strict priority (EF/DSCP 46)
- Video gets guaranteed bandwidth (AF41)
- Don't over-allocate priority queue (max 33% of bandwidth)
- Police/shape at network edges
- Use WRED for TCP-heavy data classes

---

## Key Exam Concepts Summary

✓ **QoS only matters during congestion** ✓ Voice = low latency required, can tolerate loss ✓ Data = can tolerate delay, cannot tolerate loss ✓ **DSCP (Layer 3) is preferred marking method** ✓ EF (46) = Voice traffic ✓ **Policing drops, Shaping buffers** ✓ Shaping is egress only ✓ **LLQ = CBWFQ + priority queue** (best for voice/video) ✓ WRED prevents TCP global synchronization ✓ **DiffServ is the standard QoS model** ✓ Trust boundaries typically at distribution layer ✓ Priority queue should not exceed 33% of bandwidth

---

## Common Exam Question Types

1. **Traffic characteristics** - Which type of traffic is most sensitive to delay?
2. **Marking location** - Where should QoS markings be trusted?
3. **Queuing method** - Which queuing provides strict priority?
4. **Policing vs Shaping** - When to use each?
5. **DSCP values** - What DSCP for voice traffic?
6. **QoS models** - Which model is most scalable?
7. **Congestion avoidance** - What problem does WRED solve?
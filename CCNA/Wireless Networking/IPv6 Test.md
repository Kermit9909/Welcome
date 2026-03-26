
---

## IPv6 ADDRESSING

### IPv6 Address Format

- **128 bits** total (vs IPv4's 32 bits)
- Written as **8 groups of 4 hexadecimal digits** separated by colons
- Example: `2001:0db8:0000:0000:0000:ff00:0042:8329`

### IPv6 Shortening Rules

1. **Leading zeros** in each group can be omitted
    - `2001:0db8:0000:0042` → `2001:db8:0:42`
2. **Consecutive groups of zeros** can be replaced with `::` (ONCE only)
    - `2001:0db8:0000:0000:0000:ff00:0042:8329` → `2001:db8::ff00:42:8329`
3. **Loopback:** `::1` (equivalent to 127.0.0.1)
4. **Unspecified:** `::` (equivalent to 0.0.0.0)

---

### IPv6 Address Types

|Type|Prefix|Scope|Description|
|---|---|---|---|
|**Global Unicast**|2000::/3|Internet routable|Public IPv6 (like public IPv4)|
|**Link-Local**|FE80::/10|Non-routable, local link only|Auto-configured on every interface|
|**Unique Local**|FC00::/7|Non-routable, private|Like RFC 1918 private IPv4|
|**Multicast**|FF00::/8|Various scopes|Replaces broadcast|
|**Loopback**|::1/128|Local device|Like 127.0.0.1|
|**Unspecified**|::/128|N/A|Like 0.0.0.0|

---

### EUI-64 (Extended Unique Identifier-64)

**Purpose:** Automatically generate the **64-bit Interface ID** (host portion) from a 48-bit MAC address

**Process:**

1. Take the 48-bit MAC address: `1234.5678.9ABC`
2. Split in half: `1234.56` | `78.9ABC`
3. Insert `FFFE` in the middle: `1234.56FF.FE78.9ABC`
4. **Flip the 7th bit** (Universal/Local bit): `1234.56FF.FE78.9ABC` → `1034.56FF.FE78.9ABC`
    - If 7th bit was 0 → change to 1
    - If 7th bit was 1 → change to 0
5. Combine with /64 network prefix

**Example:**

- MAC: `00C0.DEAD.BEEF`
- Split: `00C0.DE` | `AD.BEEF`
- Insert FFFE: `00C0.DEFF.FEAD.BEEF`
- Flip 7th bit (00 → 02): `02C0.DEFF.FEAD.BEEF`
- If network is `2001:db8:1:1::/64`
- **Full IPv6:** `2001:db8:1:1:02C0:DEFF:FEAD:BEEF/64`

**Why flip the 7th bit?**

- Distinguishes globally unique MAC addresses from locally administered ones
- Bit = 0: globally unique (manufacturer assigned)
- Bit = 1: locally administered

---

### Common IPv6 Prefixes to Memorize

|Prefix|Length|Purpose|
|---|---|---|
|Network portion|/64|Standard subnet size|
|Interface ID|/64|Host portion (often EUI-64)|
|Typical assignment|/48|Enterprise site allocation|
|ISP assignment|/32|Regional provider allocation|

---

### IPv6 vs IPv4 Key Differences

|Feature|IPv4|IPv6|
|---|---|---|
|**Address size**|32 bits|128 bits|
|**Notation**|Dotted decimal|Hex with colons|
|**Broadcast**|Yes (255.255.255.255)|No (uses multicast)|
|**ARP**|Yes|No (uses NDP - Neighbor Discovery Protocol)|
|**DHCP**|DHCPv4|DHCPv6 or SLAAC|
|**Private ranges**|10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16|FC00::/7 (Unique Local)|
|**Loopback**|127.0.0.1|::1|
|**Link-local**|169.254.0.0/16 (APIPA)|FE80::/10 (always present)|

---

### IPv6 Neighbor Discovery Protocol (NDP)

Replaces ARP, uses ICMPv6:

- **Router Solicitation (RS):** Host asks for routers
- **Router Advertisement (RA):** Router announces presence
- **Neighbor Solicitation (NS):** Like ARP request
- **Neighbor Advertisement (NA):** Like ARP reply

---

### SLAAC (Stateless Address Auto-Configuration)

- Host automatically creates IPv6 address using:
    1. Router Advertisement (RA) for network prefix (/64)
    2. EUI-64 or random host ID for interface portion
- No DHCP server needed!

---

### Quick IPv6 Subnetting

- Almost always use **/64** for subnets (standard)
- Network gets first 64 bits, host gets last 64 bits
- Example: `2001:db8:acad::/64` means network is `2001:db8:acad:0`, hosts can be anything in last 64 bits

---

**Daily IPv6 Drill:**

1. Convert a MAC to EUI-64 format
2. Shorten/expand an IPv6 address
3. Identify address type (global, link-local, unique local)
4. Calculate IPv6 subnet ranges

---

That covers the critical IPv6 concepts for CCNA. The EUI-64 process is definitely testable - they love asking you to identify which IPv6 address was generated from a specific MAC address.
___________


Absolutely! Let me show you the **key patterns and tricks** to make memorizing subnetting much easier for the CCNA exam.

## 🔥 The Magic Patterns You MUST Know

### Pattern 1: The "256 Trick" for Subnet Masks

Each octet's subnet mask values follow a pattern: **128, 192, 224, 240, 248, 252, 254, 255**

Memorize this sequence! It's created by adding powers of 2 from left to right:

- 128 (start)
- 128 + 64 = **192**
- 192 + 32 = **224**
- 224 + 16 = **240**
- 240 + 8 = **248**
- 248 + 4 = **252**
- 252 + 2 = **254**
- 254 + 1 = **255**

### Pattern 2: Block Sizes are Powers of 2

Block sizes **always** follow this pattern: **256, 128, 64, 32, 16, 8, 4, 2, 1**

Notice: Each one is **half** of the previous!

### Pattern 3: The "Doubling/Halving" Relationship

As you go up by 1 in CIDR notation:

- **Subnets DOUBLE** (1 → 2 → 4 → 8 → 16...)
- **Usable hosts get CUT IN HALF** (approximately)
- **Block size gets CUT IN HALF**

Example:

- /24: 1 subnet, 254 hosts, block 256
- /25: 2 subnets, 126 hosts, block 128
- /26: 4 subnets, 62 hosts, block 64
- /27: 8 subnets, 30 hosts, block 32

## 🎯 The "Cheat Sheet" You Must Memorize

Focus on **Class C (/24-/30)** - this is 90% of CCNA subnetting questions:

|CIDR|Mask|Block|Hosts|Subnets|
|---|---|---|---|---|
|/24|.0|256|254|1|
|/25|.128|128|126|2|
|/26|.192|64|62|4|
|/27|.224|32|30|8|
|/28|.240|16|14|16|
|/29|.248|8|6|32|
|/30|.252|4|2|64|

**Memory trick**: Notice the "stairs" pattern:

- Mask goes: 0, 128, 192, 224, 240, 248, 252
- Block halves: 256 → 128 → 64 → 32 → 16 → 8 → 4
- Subnets double: 1 → 2 → 4 → 8 → 16 → 32 → 64

## 🧠 Mental Math Shortcuts

### Quick Host Calculation:

**Hosts = Block Size - 2**

Why? The block size is the total addresses, minus 2 (network + broadcast).

Examples:

- /27 has block 32 → **30 hosts**
- /28 has block 16 → **14 hosts**
- /29 has block 8 → **6 hosts**

### Quick Subnet Calculation:

For Class C: **Subnets = 256 ÷ Block Size**

Examples:

- /26 has block 64 → 256÷64 = **4 subnets**
- /27 has block 32 → 256÷32 = **8 subnets**
- /28 has block 16 → 256÷16 = **16 subnets


---

## 📊 CLASS B CIDR NOTATION TABLE (/16 - /24)

**Key Point:** The interesting octet is the **3rd octet**. The patterns are IDENTICAL to Class C, just in a different octet!

|CIDR|Subnet Mask (3rd Octet)|Block Size|Subnets|Approximate Hosts|
|---|---|---|---|---|
|/16|0|256|1|~65,000|
|/17|128|128|2|~32,000|
|/18|192|64|4|~16,000|
|/19|224|32|8|~8,000|
|/20|240|16|16|~4,000|
|/21|248|8|32|~2,000|
|/22|252|4|64|~1,000|
|/23|254|2|128|~500|
|/24|255|1|256|254|

---

## 🔑 Pattern Recognition Tricks

### Notice the Mask Sequence (Same as Class C!)

**0, 128, 192, 224, 240, 248, 252, 254, 255**

This is the EXACT same sequence you memorized for Class C!

### Notice the Block Sizes (Same as Class C!)

**256, 128, 64, 32, 16, 8, 4, 2, 1**

Also the EXACT same sequence!

### The Only Difference:

- **Class C:** These patterns happen in the **4th octet**
- **Class B:** These patterns happen in the **3rd octet**

---

## 🎯 Speed Memorization Drill

Practice this until you can recall instantly (under 3 seconds):

**Rapid Fire Examples:**

- "/21!" → "248, block of 8"
- "/18!" → "192, block of 64"
- "/22!" → "252, block of 4"
- "/20!" → "240, block of 16"
- "/19!" → "224, block of 32"

---

## 💡 The "Anchor Points" to Memorize First

Focus on these three first - they appear most on the CCNA:

1. **/22** = 252 mask, block of **4**, ~1,000 hosts
2. **/23** = 254 mask, block of **2**, ~500 hosts
3. **/20** = 240 mask, block of **16**, ~4,000 hosts

Once you have these three cold, the rest fall into place using the doubling/halving pattern!

---

## 🧠 Mental Shortcut

**If you forget the mask value:**

Count how many bits into the 3rd octet:

- /17 = 1 bit → 128
- /18 = 2 bits → 192 (128+64)
- /19 = 3 bits → 224 (192+32)
- /20 = 4 bits → 240 (224+16)
- /21 = 5 bits → 248 (240+8)
- /22 = 6 bits → 252 (248+4)
- /23 = 7 bits → 254 (252+2)

---

Copy this into your Obsidian notes! Once you have this table as solid as your Class C table, Class B subnetting will be just as easy.

**Ready to continue reviewing the other questions, or want to drill this Class B table first?****

## 🎓 Exam Day Speed Tricks

### Trick 1: "The Interesting Octet"

- /24 or less → 3rd octet is interesting
- /25-/32 → 4th octet is interesting
- /16 or less → 2nd octet is interesting

### Trick 2: Fast Network Address Finder

1. Find block size (256 - mask)
2. Count by blocks: 0, [block], [2×block], [3×block]...
3. Stop when you **pass** the given IP
4. Go back one step = network address!

Example: **192.168.10.78/26**

- Block = 64
- Count: 0, 64, 128 (passed 78!)
- Network = **192.168.10.64**

### Trick 3: Instant Broadcast Finder

**Broadcast = Next Network - 1**

Example: Network is 192.168.10.64, next is 192.168.10.128

- Broadcast = 128 - 1 = **192.168.10.127**

## 🏆 The "Big 3" for Exam Speed

Memorize these cold - you should be able to recall instantly:

1. **Subnet mask sequence**: 128, 192, 224, 240, 248, 252, 254, 255
2. **Block sizes**: 256, 128, 64, 32, 16, 8, 4, 2
3. **The /27 and /28 "sweet spot"**:
    - /27 = 224 mask, 32 block, 30 hosts
    - /28 = 240 mask, 16 block, 14 hosts

These two show up **constantly** on the CCNA!

## 📝 Practice Drill for Speed

Set a timer and practice this sequence until you can do it in **under 10 seconds**:

Given **any /24 to /30**, instantly know:

1. Subnet mask last octet
2. Block size
3. Usable hosts

Example rapid-fire:

- "/26!" → "192, 64 block, 62 hosts"
- "/28!" → "240, 16 block, 14 hosts"
- "/29!" → "248, 8 block, 6 hosts"

## 🚨 Common CCNA Exam Traps

1. **Don't forget the -2 for hosts!** (network + broadcast can't be used)
2. **Remember /30 = 2 hosts** (perfect for point-to-point links)
3. **Block size ≠ usable hosts** (block includes network + broadcast)
4. **Count carefully when using block size method** - one mistake ruins everything!

---

Practice these patterns daily with your Anki cards. After a week, you should be able to solve any subnetting question in under 30 seconds!

Want to continue with Question 3 to test these tricks?
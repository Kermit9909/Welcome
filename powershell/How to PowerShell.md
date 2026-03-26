____________

Perfect — let's build the foundation. Everything in PowerShell navigation flows from three master commands. Learn these three and you can figure out literally anything else yourself:

---

## 🧭 The Holy Trinity

```powershell
Get-Command    # What commands exist?
Get-Help       # How do I use this command?
Get-Member     # What properties does this OUTPUT have?
```

Most beginners know the first two. `Get-Member` is the one that separates good PowerShell users from great ones. We'll get to why in a minute.

---

## 1️⃣ Get-Command — Finding Tools

**Find everything available:**

```powershell
Get-Command
```

Returns thousands of commands. Too much. So you filter:

**By Verb:**

```powershell
Get-Command -Verb Get
Get-Command -Verb New
Get-Command -Verb Remove
```

**By Noun:**

```powershell
Get-Command -Noun Process
Get-Command -Noun ADUser
```

**By wildcard:**

```powershell
Get-Command *network*
Get-Command *firewall*
```

**The methodology:**

> _"I want to do something with services but I don't know the command"_

```powershell
Get-Command -Noun Service
```

Returns:

```
Get-Service
New-Service
Restart-Service
Set-Service
Stop-Service
Start-Service
```

You just discovered six commands without memorizing a single one.

---

## 2️⃣ Get-Help — Understanding Tools

Once you find a command you need to know how to use it:

```powershell
Get-Help Get-Service
Get-Help Get-Service -Examples
Get-Help Get-Service -Detailed
Get-Help Get-Service -Full
```

**The methodology:**

- `-Examples` first — shows you real usage immediately
- `-Detailed` — parameter explanations
- `-Full` — everything including technical notes

**Wildcard searching in help:**

```powershell
Get-Help *event*
Get-Help *log*
```

This searches help topics — great for when you know what you want to DO but not what it's called.

---

## 3️⃣ Get-Member — The Secret Weapon

This is where PowerShell gets powerful. Everything in PowerShell is an **object** with **properties** and **methods**. `Get-Member` shows you what those are.

**Example — what does a process object actually contain?**

```powershell
Get-Process | Get-Member
```

Returns something like:

```
Name                  MemberType
----                  ----------
CPU                   Property
Handle                Property
Id                    Property
MachineName           Property
MainWindowTitle       Property
Name                  Property
NonpagedSystemMemory  Property
PagedMemorySize       Property
PeakWorkingSet        Property
WorkingSet            Property
Kill                  Method
Refresh               Method
Start                 Method
```

Now you KNOW what properties exist to select, filter, and sort on. You didn't guess — you discovered.

**The methodology:**

```powershell
# Step 1 - Get the object
Get-Process

# Step 2 - Discover its properties
Get-Process | Get-Member

# Step 3 - Select only what you need
Get-Process | Select-Object Name, CPU, WorkingSet

# Step 4 - Filter it
Get-Process | Where-Object {$_.WorkingSet -gt 100MB}

# Step 5 - Sort it
Get-Process | Where-Object {$_.WorkingSet -gt 100MB} | Sort-Object WorkingSet -Descending
```

See how each step builds on the last? That's the **pipeline** — the heart of PowerShell.

---

## 🔬 The Pipeline Concept

Think of it like a factory assembly line:

```
Get-Process  →  Where-Object  →  Select-Object  →  Sort-Object  →  Export-Csv
    │                │                 │                │               │
 Raw data        Filter it         Pick fields       Order it       Save it
```

Each `|` (pipe) passes objects to the next command. You're not passing text like CMD — you're passing **structured objects with properties.** That's why PowerShell is so much more powerful than CMD or bash for Windows admin work.

---

## 💡 The $_ Variable

You'll see `$_` constantly in PowerShell. It means **"the current object in the pipeline."**

```powershell
Get-Process | Where-Object {$_.Name -eq "explorer"}
```

Translation: _"Get all processes, then for each one (`$_`) where its Name property equals explorer, show it."_

Once `$_` clicks everything else makes sense.

---

## 🗺️ Filesystem Navigation

Since you know `ls` and `dir` already — here's the PS equivalents and what's behind them:

|Alias|Real Command|Use|
|---|---|---|
|`ls`|`Get-ChildItem`|List directory contents|
|`cd`|`Set-Location`|Change directory|
|`pwd`|`Get-Location`|Where am I?|
|`mkdir`|`New-Item -ItemType Directory`|Make folder|
|`cat`|`Get-Content`|Read a file|
|`cp`|`Copy-Item`|Copy file|
|`mv`|`Move-Item`|Move file|
|`rm`|`Remove-Item`|Delete file|

You already know the aliases — now you know the real commands behind them. When you write scripts always use the real command names, never aliases. Scripts should be readable by anyone.

---

## 🧪 Preview of Your First Test

When BITS finishes and we wrap up I'll give you something like this:

> _"Using only Get-Command and Get-Help — find the command that shows you all network IP addresses on this machine. Then show me only the IPv4 addresses. No Googling, no me helping — just the trinity."_

The answer exists. You have the tools to find it. That's the whole game. 💪

BITS still going? 😄
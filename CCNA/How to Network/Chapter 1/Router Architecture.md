___________

# Cisco Router Architecture Summary

_Last updated: 2025-10-05_

  

## Overview

Cisco routers rely on several types of memory, each serving a unique function during operation and boot. Understanding these components and the boot process is essential for configuration, troubleshooting, and IOS management.

  

---

  

## Router Memory Types

  

### ROM (Read-Only Memory)

- Stores the **bootstrap program** to load the Cisco IOS from flash.

- Houses **ROMmon mode**, a minimal OS used for recovery if the IOS is missing or corrupt.

- Prompts: `>` or `rommon>`

- May include a **RXBOOT image** (Mini-IOS) for maintenance tasks.

  

### DRAM (Dynamic RAM)

- Volatile memory that stores:

  - **Running configuration**

  - **Routing tables and buffers**

  - **Decompressed IOS image**

- Contents lost on power-off.

- Save configuration from DRAM to NVRAM:

  ```

  copy running-config startup-config

  ```

  

### Flash Memory (EEPROM)

- Non-volatile storage for the **Cisco IOS image**.

- Can also hold multiple IOS versions and configuration backups.

- View contents:

  ```

  show flash

  ```

- File format example: `c2900-universalk9-mz.SPA.151-1.M4.bin`

  - `K9`: includes encryption (AES/3DES)

  - `mz`: runs from RAM and is zipped

  - `SPA`: digitally signed production version

- Delete or restore files:

  ```

  delete flash:<filename>

  undelete

  ```

  

### NVRAM (Non-Volatile RAM)

- Stores the **startup configuration** (`startup-config`).

- Retains data after power loss.

- Compress large configurations:

  ```

  service compress-config

  ```

- Copy configuration between devices via TFTP:

  ```

  copy tftp flash

  ```

  

### CPU

- Executes IOS instructions and routing processes.

- Check CPU type and memory details:

  ```

  show version

  ```

  

---

  

## Router Boot Sequence

1. **POST (Power-On Self-Test)** – checks hardware integrity.

2. **Bootstrap (ROM)** – loads the IOS from Flash.

3. **Load IOS (Flash → DRAM)** – decompresses the IOS into RAM.

4. **Load Configuration (NVRAM)** – applies startup-config if found.

5. **Setup Mode** – triggered if no valid config file exists.


|Memory Type|What It Stores|Volatile?|Notes|
|---|---|---|---|
|**ROM (Read-Only Memory)**|Bootstrap program, POST, and a mini version of the IOS (for recovery / ROMMON)|**Non-volatile**|Used only during boot-up and recovery.|
|**RAM (DRAM)**|Running-config, routing tables, ARP cache, packet buffers, and loaded IOS|**Volatile**|Everything here is lost when the device is powered off or reloaded.|
|**Flash**|The **full IOS image** and sometimes other files (like backup configs, VLAN database)|**Non-volatile**|Think of this as the device’s “hard drive.”|
|**NVRAM**|The **startup-config** (the saved configuration loaded at boot)|**Non-volatile**|Stays intact after reboot until erased.|

So in simple terms:

- **ROM** → boot code
    
- **RAM** → live system (working memory)
    
- **Flash** → operating system
    
- **NVRAM** → saved configuration





## When a Cisco router or switch can’t find or load the **IOS image**, it drops into a special low-level recovery mode called **ROM Monitor (ROMMON)**.

  

Configuration register values:

- `0x2102` → normal boot, loads startup-config.

- `0x2142` → ignores startup-config (used for password recovery).

  

---

  

## Managing the IOS

  

### Backups and Recovery

- Always back up IOS and configurations.

- Save changes to NVRAM:

  ```

  copy running-config startup-config

  ```

- Back up to TFTP server:

  ```

  copy running-config tftp:

  copy flash tftp:

  ```

  

### Boot Options

Routers can boot IOS from several sources:

- **Flash (default)**:

  ```

  boot system flash <filename>

  ```

- **TFTP server**:

  ```

  boot system tftp <filename> <server_ip>

  ```

- **USB flash**:

  ```

  boot system flash usbflash0:<filename>

  ```

  

### Secure Transfer Options

- FTP configuration:

  ```

  ip ftp username <user>

  ip ftp password <password>

  copy startup-config ftp:

  ```

- SCP (secure copy) server enablement:

  ```

  ip scp server enable

  ```

  

---

  

## IOS Upgrades and Verification

Before upgrading:

- Verify space and memory:

  ```

  show flash

  dir flash:

  ```

- Copy new IOS from TFTP:

  ```

  copy tftp flash:

  ```

- Verify integrity:

  ```

  verify /md5 flash:<filename>

  ```

  

---

  

## Password Recovery (General Steps)

1. Connect via console.

2. Power cycle the router and send a **break sequence** (Ctrl+Break).

3. Enter **ROMmon** mode.

4. Change config register to ignore startup config:

   ```

   confreg 0x2142

   ```

5. Reboot the router.

6. Copy startup config into running config:

   ```

   copy startup-config running-config

   ```

7. Reset the password and save changes:

   ```

   enable secret <new_password>

   copy running-config startup-config

   ```

8. Restore the config register:

   ```

   config-register 0x2102

   ```

  

---

  

## Memory and File Location Summary

  

| Memory | Function |

|---------|-----------|

| ROM | Bootstrap program and ROMmon |

| DRAM | Running-config, routing tables, buffers |

| Flash | IOS storage |

| NVRAM | Startup-config |

  

---

  

**End of Summary – Cisco Router Architecture (CCNA)**
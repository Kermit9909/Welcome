
__________

# Cisco IOS Configuration Commands Reference

_Last updated: 2025-10-05_

  

This file lists key Cisco IOS commands by function for router and switch management.

  

---

  

## Viewing System Information

```

show version

```

Displays IOS version, memory allocation, CPU type, and configuration register.

  

```

show flash

```

Shows files stored in Flash memory (IOS images, configs).

  

```

dir flash:

```

Lists contents of Flash; note total and free bytes.

  

```

show usb device

```

Displays connected USB storage information.

  

---

  

## Managing Configurations

```

copy running-config startup-config

```

Saves active configuration from DRAM to NVRAM.

  

```

copy startup-config running-config

```

Loads the saved configuration into DRAM (useful after password recovery).

  

```

copy running-config tftp:

```

Backs up current configuration to a TFTP server.

  

```

copy startup-config ftp:

```

Uploads the startup config file to an FTP server.

  

```

copy tftp flash:

```

Copies an IOS image or configuration file from TFTP to Flash.

  

```

copy flash tftp:

```

Backs up the IOS image to a TFTP server.

  

---

  

## Boot and System Image Commands

```

boot system flash <filename>

```

Instructs router to boot from a specific IOS image in Flash.

  

```

boot system tftp <filename> <server_ip>

```

Boots IOS from a TFTP server.

  

```

boot system flash usbflash0:<filename>

```

Boots IOS from USB storage.

  

```

config-register 0x2102

```

Default setting: load startup-config during boot.

  

```

config-register 0x2142

```

Ignore startup-config (used for password recovery).

  

---

  

## IOS File Management

```

delete flash:<filename>

```

Deletes a file from Flash memory.

  

```

undelete

```

Restores recently deleted files from Flash.

  

```

verify /md5 flash:<filename>

```

Verifies IOS image integrity using MD5 checksum.

  

```

service compress-config

```

Compresses large configuration files in NVRAM.

  

---

  

## IOS Upgrade Commands

```

copy tftp flash:

```

Copies new IOS from a TFTP server to Flash.

  

```

copy flash usbflash0:

```

Copies IOS from Flash to USB storage.

  

```

copy usbflash0: flash:

```

Copies IOS image from USB to router Flash memory.

  

---

  

## Secure File Transfer

```

ip ftp username <username>

ip ftp password <password>

```

Sets FTP credentials for router file transfer.

  

```

ip scp server enable

```

Enables Secure Copy Protocol (SCP) server functionality.

  

---

  

## Debug and Verification

```

debug tftp

```

Displays TFTP transfer process and troubleshooting details.

  

```

show memory

```

Displays current memory usage and buffer allocation.

  

```

show processes cpu

```

Monitors CPU utilization and active processes.

  

---

  

## Password Recovery Essentials

```

confreg 0x2142

```

Changes config register to ignore startup-config on next boot.

  

```

copy startup-config running-config

```

Restores configuration after recovery.

  

```

enable secret <new_password>

```

Sets a new enable password.

  

```

config-register 0x2102

```

Returns configuration register to default after recovery.

  

---

  

**End of Reference – Cisco IOS Configuration Commands**

## Benign

Date: March 27, 2026
Site: TryHackMe
Focus: Splunk investigation

### The Task:

One of the client’s IDS indicated a potentially suspicious process execution indicating one of the hosts from the HR department was compromised. Some tools related to network information gathering / scheduled tasks were executed which confirmed the suspicion. Due to limited resources, we could only pull the process execution logs with Event ID: 4688 and ingested them into Splunk with the index win_eventlogs for further investigation.

## Log 
win_eventlogs

## Problem
Suspicious process execution
    - host from HR department
    - tools related to network information gathering / sheduled tasks
    - Event ID: 4688 (Creation of new process ID)

## IT Department
James
Moin
Katrina

## HR department
Haroon
Chris
Diana

## Marketing department
Bell
Amelia
Deepak 


## Q & A:

How many logs are ingested from the month of March, 2022? 
13959

Imposter Alert: There seems to be an imposter account observed in the logs, what is the name of that user?
Amel1a
*** index = "win_eventlogs" User ***

Which user from the HR department was observed to be running scheduled tasks?
Chris.Fort
*** index="win_eventlogs" Chris.Fort AND *tasks* ***

Which user from the HR department executed a system process (LOLBIN) to download a payload from a file-sharing host.
haroon
*** index="win_eventlogs" UserName IN ("haroon", "Chris.Fort", "Diana") *certutil*

To bypass the security controls, which system process (lolbin) was used to download a payload from the internet?
certutil.exe

What was the date that this binary was executed by the infected host? format (YYYY-MM-DD)
2022-03-04

Which third-party site was accessed to download the malicious payload?
controlc.com

What is the name of the file that was saved on the host machine from the C2 server during the post-exploitation phase?
benign.exe

The suspicious file downloaded from the C2 server contained malicious content with the pattern THM{..........}; what is that pattern?
THM{KJ&*H^B0}

What what the URL?
https://controlc.com/e4d11035


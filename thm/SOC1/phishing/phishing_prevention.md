
# Phishing Prevention
## SPF | DKIM | DMARC | S/MIME | SMTP

## SPF Records
“Sender Policy Framework (SPF) is used to authenticate the sender of an email. With an SPF record in place, Internet Service Providers can verify that a mail server is authorized to send email for a specific domain. An SPF record is a DNS TXT record containing a list of the IP addresses that are allowed to send email on behalf of your domain.”

Let's take a look at a sample SPF record and break down its format. Further information on SPF Record Syntax can be found here(opens in new tab).

v=spf1 ip4:127.0.0.1 include:_spf.google.com -all

v=spf1 Signifies the start of the SPF record
ip4:127.0.0.1 Specifies which IP can send mail (IPv4 in this case)
include:_spf.google.com Specifies which domain can send mail
-all Non-authorized emails will be rejected

## DomainKeys Identified Mail 
“DKIM stands for DomainKeys Identified Mail and is used for the authentication of an email that’s being sent. Like SPF, DKIM is an open standard for email authentication that is used for DMARC alignment. A DKIM record exists in the DNS, but it is more complex than SPF. DKIM’s advantage is that it can survive forwarding, which makes it superior to SPF and a foundation for securing your email.”

### Sample

v=DKIM1; k=rsa; p=<public_key>

v=DKIM1 Specifies the version of DKIM being used (optional)
k=rsa The key type. The RSA encryption algorithm is standard
p= This is the public key that will be matched to the private key to verify the DKIM signature

## DMARC Records
“DMARC, an open source standard, uses a concept called alignment to tie the result of two other open source standards,  SPF (a published list of servers that are authorized to send email on behalf of a domain) and DKIM (a tamper-evident domain seal associated with a piece of email), to the content of an email.”

**Example:**
v=DMARC1; p=quarantine; rua=mailto:postmaster@website.com

v=DMARC1: The version of DMARC (required)
p=quarantine The DMARC policy (quarantine = move to the spam folder)
rua=mailto:postmaster@website.com An optional tag. In this case, aggregate reports will be sent to the email specified

Secure/Multipurpose Internet Mail Extensions: S/MIME
"Standard protocol for sending digitally signed and encrypted messages. It is based on public key cryptography, where the private key is never shared and the public key can be distributed openly."

### Two Main Components:

***Digital Signature***

The sender signs the message with their private key, the recepient verifies the sender's identity using the sender's public key. This security feature provides:

Authentication: Confirms the sender's identity through their digital certificate
Non-repudiation: Ensures the sender cannot deny sending the message
Data Integrity: Detects any changes to the message after it's signed

***Encryption***

The sender encrypts the message using the recipient's public key, allowing only the recipient to decrypt it with their private key. This security feature provides:

Confidentiality: Keeps the content private and readable only by the intended recipient

## Analyzing SMTP with WireShark

Wireshark SMTP filters:

smtp.response.code
smtp.response.code==(value)
imf (internet message format)

SMTP response codes are three-digit numbers sent by mail servers to indicate the status of email transmission, categorized by their first digit: 2xx for success, 3xx for intermediate actions, 4xx for temporary errors, and 5xx for permanent errors. 

### Success and Intermediate Codes
220: The server is ready to receive commands. 
250: The requested command was completed successfully. 
251: The user is not local to this server, but the message will be forwarded. 
252: The server cannot verify the user but will accept the message for delivery. 
354: The server confirms mail content transfer and waits for the message body. 
334: Used during authentication when a security mechanism is accepted. 

### Temporary and Permanent Errors
421: The service is unavailable due to a connection problem or limit; the server closes the channel. 
450: The mailbox is unavailable (busy or blocked); the action is aborted. 
451: A local error occurred in processing; the command is aborted. 
452: Insufficient system storage or memory to process the request. 
500: A syntax error occurred; the server could not recognize the command. 
535: Authentication credentials are invalid. 
550: The mailbox is unavailable or the command failed due to policy reasons (e.g., user not found). 
**552: Failure due to exceeded storage allocation**
**553: Failure due to mailbox name is invalid**
554: The transaction failed, often due to a blacklist or unknown error. 

## Internet Message Format (IMF)
"The Internet Message Format (IMF) is the standardized ASCII-based syntax required by the Simple Mail Transfer Protocol (SMTP) for all email message bitstreams, where it acts as the "letter within the envelope" alongside the transport mechanism."

## How Organizations Stop Phishing

## Technical Defenses
Modern email systems employ various technical controls to help detect and block phishing messages before they reach users.

***Email Filtering***: Provides filtering based on IP and domain reputation, allowing for blocking or quarantining of suspicious messages.
***Secure Email Gateways*** (SEGs): Scan messages to detect impersonation attempts, spoofing, and other phishing techniques that other filters might miss.
***Link Rewriting***: Replaces suspicious or unknown URLs with safe, redirected ones, giving the system time to scan and verify the link.
***Sandboxing***: Isolates and tests suspicious links or attachments in a secure, virtual environment to check for malicious behavior.

## User-Facing Tools & Training

Even with strong technical defenses in place, some phishing emails will inevitably reach users. Giving users clear visual cues and education is essential.

**Trust & Warning Indicators:** Modern email platforms display visual cues to help users understand if a message is safe. A banner may read “External Sender,” “Suspicious Link,” or signify that a message is from a trusted organization or sender. 
**Phishing Reporting:** Easy, in-email reporting options that let users quickly report suspicious messages.
**User Awareness Training:** Train employees on identifying phishing attempts, social engineering tactics, and safe email practices.
Phishing Simulation Exercises: Run controlled phishing campaigns to test and reinforce employee training.












# Phishing Fundamentals

## Learning Objectives

    Learn the basics of email delivery
    Explore email header analysis
    Investigate and analyze email bodies
    Learn about the different types of
    Analyze emails to identify potential security threats

## Email Delivery

Simple Mail Transfer Protocol (): Sends emails
Post Office Protocol (): Downloads emails to a device
Internet Message Access Protocol (): Syncs emails across devices

An Email's Journey

    User sends an email: The sender’s email client sends the message to their mail server using SMTP
    Mail server queries DNS: The sending server asks DNS for the recipient domain’s mail server
    DNS responds: DNS returns the address of the recipient’s mail server
    Email is delivered: The message is sent across the Internet to the recipient’s server
    The recipient checks their mailbox: The recipient’s email client connects to their mail server
    Email is retrieved: The message is downloaded (POP3) or synced (IMAP) to the recipient’s device

## Email Headers

### Techniques

    View > Message Soruce

## Tools

    - base64 to pdf (apivoid.com)
    - Cyberchef (save as pdf if needed)
        - can defang (cool)

### Important Info:

    - originating IP address  (start from the bottom / most reliable)
    - X-Originating-IP address (client's actual IP)
    - Attachemnts:
        - Content-Type ex. (application/pdf)
        - Content-Disposition specifies that the file is attachment, and filename
        - Content-Transfer-Encoding show the file is 'base64' encoded

## Email Body

    - text or HTML
    - attachments can be analyzed as well

## Anatomy of a Phishing Email

    - Common Characteristicsws
        - Spoofed from address ' noreply@microsof.com'
        - Urgent subject or message
        - Brand impersonation (mimics logos or colors of company)
        - Grammer and spelling issues (AI awkward phrasing or unnatural wording)
        - Generic Content (lacks personalization)
        - Hidden or shortened links (hyperlinks may disguise their true destination)
        - Malicious attachment (invoice.pdf.exe)

## ** Safe Analysis - Defange URLs or any links







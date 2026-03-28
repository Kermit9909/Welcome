
# Configuring Wireshark Geo Location

## Steps:
    1. Set up MaxMind account (free)
    2. Download
            - Geolite2 ASN
            - Geolite2 City
            - Geolite2 Country
    3. Put all .mmdb files into one folder 
    4. Go to Wireshark Preferences
    5. Name Resolution
    6. MaxMind Database Directories
        - Add path to single folder containing 3 .mmdb files

# Boom! Geolocation Installed 
# Bam! Leveled Up

## How to use in Wireshark

        - Has to be from a public IP address range
        - Under Internet Protocol > Source GeoIP

## A better view

        - Statistics > Endpoints > Boom
        - Map > Open in Browser (great visual for sales/presentations)
        - Close
        - Filter by Source GeoIP ISO Two Letter Country Code: 

## So what does this information really tell us?

        - If in this example (spoofed IPs in DDoS)
                1. **Destination IPs almost never spoofed**
                        The Threat is Real!
                2. Attack vectors - can map to APT actors????
                3. The Real Skill - 
                        Distinguishing REAL vs. FAKE
                4. SIEM enrichment
                5. Firewall / IDS context
                6. DDoS mitigation
                7. Incident Reporting

## SOC Analyst Tier 1 job

        - Characterize the attack
        - Document IOCs
        - Escalate with accurate data
        - Help team implement mitigations






    

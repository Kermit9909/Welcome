
# MITRE Room

## Learning Objectives

    - Understand the purpose and structure of MITRE ATT&CK Framework
    - Explore how security professionals apply ATT&CK in their work
    - Use cyber threat intelligence (CTI) and the ATT&CK Matrix to profile threats
    - Discover MITRE's other frameworks, including CAR and D3FEND

## What
    - The MITRE ATT&CKframework is “a globally-accessible knowledge base of adversary tactics and techniques based on real-world observations.

### TTPs
    - **Tactic** - adversary's goal or objective. The "why" of an attack
    - **Technique** - How an adversary achieves their goal or objective.
    - **Procedure** - The implementation or **how** the technique is executed.

# OK - So this is a lot!  Let's grab resources:

## MITRE LINKS

[MITRE Main Page](https://attack.mitre.org/)
[MITRE ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/)

## Practice:

    - Research APTs (Pick one, and learn the TTPs)
    - Create Scenarios:  
    EX. You are a security analyst in the aviation sector, and your organization is migrating its infrastructure to the cloud. Your task is to use ATT&CK to gather intelligence on groups known to target this sector, identify their tactics and techniques, and assess any potential gaps in your defensive coverage.  **Use Claude.ai to help come up with scenarios**
        - which APTs
        - sub-techniques
        - what tools
        - mitigation strategies
        - Detection Strategy IDs

# Resource:  Cyber Analytics Repository [CAR](https://car.mitre.org/)

CAR is a collection of ready-made detection analytics built around ATT&CK. Each analytic describes how to detect an adversary's behavior. This is key because it allows you to identify the patterns you should look for as a defender. CAR also provides example queries for common industry tools such as , so you, as a defender, can translate ATT&CK TTPs into real detections. 

# Resource: [MITRE D3FEND](https://d3fend.mitre.org/)

With ATT&CK, you learn how attacks happen, but with

D3FEND, you discover how to stop them.

D3FEND (Detection, Denial, and Disruption Framework Empowering Network Defense) is a structured framework that maps out defensive techniques and establishes a common language for describing how security controls work. D3FEND comes with its own matrix, which is broken down into seven tactics, each with its associated techniques and IDs.

# Resources:

[Caldera](https://caldera.mitre.org/)
Caldera is an automated adversary emulation tool designed to help security teams test and enhance their defenses. It provides the ability to simulate real-world attacker behavior utilizing the ATT&CK framework.

[AADAPT](https://aadapt.mitre.org/)
A newly released knowledge base that includes its own matrix, covering adversary tactics and techniques related to digital asset management systems. AADAPT follows a similar structure to the ATT&CK Framework we covered previously and aims to help defenders understand and mitigate threats targeting blockchain networks, smart contracts, digital wallets, and other digital asset technologies.

[ATLAS](https://atlas.mitre.org/)
ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems) is a knowledge base and framework that includes a matrix, focusing on threats targeting and machine learning systems. It documents real-world attack techniques, vulnerabilities, and mitigations specific to AI technology.
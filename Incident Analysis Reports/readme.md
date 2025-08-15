## Incident Analysis Reports

Hello, in this area of my portfolio, I present different real-case cyber incident scenarios from various industries (I'll try to keep more AUS case-based ones).  
Each case provides a walkthrough of **how, when, and what happened**, along with relevant technical and governance details from the study case.  
I also include **key highlights**, **best practice recommendations**, and **lessons learned** — including my own perspective on what could have been done differently.  

Under **Security Recommendations**, I map my proposed improvements against **local, global, and industry-specific framework standards** to demonstrate practical alignment and governance awareness.

---

### Case Scenario 1: Medibank 2022 Data Breach

📄 [Cyber Incident Review – Medibank 2022](./documents/CyberIncReview_Medibank2022.pdf)

**Industry:** Healthcare / Insurance  
**Location:** Australia  
**Date:** October 2022  
**Impact:** 9.7 million customers affected, including sensitive personal and health information.

---

#### Summary of Incident
In October 2022, Medibank detected malicious activity after an attacker exploited stolen administrator credentials from a third-party IT service provider.  
Weak access controls, lack of multi-factor authentication (MFA), and missed Endpoint Detection and Response (EDR) alerts enabled the threat actor to gain persistent access and exfiltrate sensitive customer data.  
When the ransom demand was refused, the data was published on the dark web.

---

#### Key Factors Contributing to the Breach
1. **Third-party credential compromise** – Admin credentials were stored insecurely in a browser profile on a personal laptop.  
2. **Lack of MFA** – No additional authentication layer for privileged or remote access.  
3. **Weak network access controls** – No device verification or IP source restrictions.  
4. **Ignored EDR alerts** – Security warnings were not actioned promptly.  
5. **Delayed response** – Full-scale investigation began only after a later alert was investigated.

---

#### Consequences
- Exposure of sensitive personal and health information.
- Reputational damage and loss of customer trust.
- Significant legal and financial repercussions.
- First Australian cyber sanction under the **Autonomous Sanctions Act 2011** applied to an individual attacker.

---

#### Security Recommendations & Framework Mapping

Below is the mapping of Medibank’s identified gaps to the **Australian Essential Eight** strategies, alongside related **ISO 27001:2022 Annex A controls** and estimated maturity levels at the time of the breach.

| **E8 Strategy** | **Gap in Medibank Case** | **Recommendation** | **ISO 27001:2022 Clause / Annex A Control** | **Estimated Maturity Level at Breach** | **Target Maturity Level** |
|----------------|--------------------------|--------------------|---------------------------------------------|---------------------------------------|---------------------------|
| **Multi-Factor Authentication (MFA)** | No MFA for privileged and remote access accounts | Enforce MFA for all privileged accounts, remote VPN access, and third-party logins | A.5.17 Authentication Information | 0 | 3 |
| **Patch Applications** | Vulnerable Microsoft Exchange Server attempted to be exploited | Apply timely security patches and enable automated patch management for critical apps | A.8.8 Management of Technical Vulnerabilities | 1 | 3 |
| **Restrict Administrative Privileges** | Stolen admin creds allowed broad system access | Implement least privilege, just-in-time admin access, and session monitoring | A.5.18 Access Rights | 1 | 3 |
| **Application Control** | No application whitelisting to prevent unauthorised tool execution | Implement application whitelisting on all servers and high-value endpoints | A.8.30 Protection Against Malware | 0 | 3 |
| **User Application Hardening** | Browser stored admin credentials, enabling theft | Disable browser-based credential storage for privileged accounts | A.8.29 Protection of Web-based Applications | 0 | 3 |
| **Configure Microsoft Office Macro Settings** | Not directly exploited in this incident | Apply secure macro settings and restrict unsigned macros | A.8.30 Protection Against Malware | 2 | 3 |
| **Patch Operating Systems** | Possible unpatched OS vulnerabilities in environment | Maintain regular OS patch cycles and vulnerability scans | A.8.8 Management of Technical Vulnerabilities | 2 | 3 |
| **Daily Backups** | No evidence of tested, immutable backups | Maintain offline, immutable backups for all critical systems and test restoration regularly | A.8.13 Backup | 1 | 3 |

---

##### Observations
- **Third-Party Risk**: Weak credential handling by a service provider, with elevetated priviledge functions, directly contributed to the breach. ISO 27001 A.5.19 and A.5.20 require supplier agreements and monitoring to enforce security obligations.  
- **Security Culture**: ISO 27001 A.6.3 (Awareness, Education and Training) aligns with the recommendation to foster a strong security culture to mitigate human error.  
- **Monitoring and Response**: Ignored EDR alerts indicate a maturity gap in detection and response. ISO 27001 A.8.16 (Monitoring Activities) and A.5.23 (Information Security Event Reporting) address this.  
- **Zero Trust Approach**: While not explicitly in E8, Zero Trust principles align with ISO 27001's least privilege and network segmentation controls (A.8.20, A.8.21).  

---


#### Lessons Learned
- **Third-party risk must be treated as internal risk** : Third parties are part of every business, even in something as simple as selling burgers. You need to make sure your providers meet at least a minimal standard of control: the bread isn’t expired, the meat is safe to eat, and, most importantly, if the third party is the cook, they are trained to deliver a high-standard product. Your reputation depends on it. The same principle applies in cyber. Suppliers providing critical services and managing sensitive data must meet or exceed the organisation’s security posture, and especially when they are part of daily business operations, they must be treated as part of the organisation itself under the same strict and regulated standard
- **Zero Trust isn’t just a pretty word** — Do not trust, always verify is the phrase, and yes, some times it could be annoyed to validate your identity multiple times but assume breach and verify continuously.  
- **Security culture** : is as important as technical controls,policy, awareness, and behaviour form the foundation, organisations must transmit not just restrict or adopt a fearing approach, people working whitin and around the business must understand how their functions, responsabilities and the secure culture are aligned eachother.

---
### Case Scenario 2 ... soon

---

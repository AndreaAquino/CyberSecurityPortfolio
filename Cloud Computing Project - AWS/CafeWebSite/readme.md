# ☕ Cafe App - Secure, Scalable & Highly Available AWS Architecture

##  Project Summary
This project demonstrates the deployment of a secure, scalable, and highly available cloud infrastructure for a simulated café web application. 
It follows AWS best practices, including multi-AZ availability, auto scaling, and least-privilege access principles.

## Disclamer
This is a simulated project for educational and portfolio purposes only. It reflects secure cloud architecture practices but should not be reused in production environments without security validation.
**Default usernames and passwords must never be used** in real environments. Always follow best practices for credential management, avoid hardcoding secrets, and never share your S3 bucket URLs or access keys publicly.

##  Architecture Overview

###  Multi-AZ Design
- Web App and API servers deployed across two Availability Zones (AZs) to ensure redundancy.
- Bastion host provisioned in public subnet for controlled SSH access to private instances.

###  Auto Scaling & Load Balancing
- Two Auto Scaling Groups: one for Web App Servers and one for API endpoints.
- Application Load Balancer (ALB) handles traffic:
  - Port 80 for the PHP-based front end.
  - Port 5000 for the Flask API.

###  Database Layer
- **Amazon RDS (MariaDB)** instance (private subnet) used as the backend database.
- Includes a **read-only replica** for API reads, improving performance and fault tolerance.

---

## Security Considerations

| Layer       | Component           | Security Group Rules (Inbound)                                                                 |
|-------------|---------------------|-----------------------------------------------------------------------------------------------|
| VPC         | Café-VPC            | Default ACLs; associated with multiple subnet groups.                                          |
| Load Balancer | ALB-NSG            | Allows HTTP (80) and Custom TCP (5000) from any IPv4 source.                                  |
| Web App EC2 | WebAppSer-NSG       | Allows HTTP (80) from ALB, SSH (22) only from Bastion.                                        |
| API EC2     | API-NSG             | Allows TCP (5000) from ALB, DB access from DB-NSG, SSH from Bastion.                          |
| RDS DB      | DB-NSG              | Allows MariaDB (3306) from WebAppSer-NSG and API-NSG only.                                    |
| Bastion Host| Bastion-NSG         | Allows SSH (22) from trusted IPs only.                                                        |

---

## Files in This Portfolio Entry

- [cafe_api](./cafe_api/): CloudFormation template provisioning VPC, subnets, IGWs, NAT gateways, and route tables.
- `architecture-diagram.png`: Visual representation of the deployed architecture.
- `CafeApp-Details.pdf`: Full documentation of the project, use for your reference only*

---

## Architecture Diagram

![Architecture Diagram](./images/CafeSite-CloudInfra.png)

---

## Acknowledgements
- YouTube: r2schools (2023). Creating and connecting to MariaDB RDS in AWS.
- AWS Documentation for EC2, RDS, Auto Scaling Groups.
- ChatGPT was used for YAML refinement and troubleshooting support (AI-assisted but reviewed manually).
- AWS Academy – Lab-based project developed during the AWS Academy Cloud Architecting course.

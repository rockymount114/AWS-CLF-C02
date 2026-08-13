# AWS Cloud Practitioner - Full 65+ Questions & Answers (From Your Chat History)
> All questions extracted from your screenshots and text history, with correct answers and why.

---

### 1. Hardware Device for Data Encryption for Compliance
**Question:** Due to regulatory and compliance reasons, an organization is supposed to use a hardware device for any data encryption operations in the cloud. Which AWS service can be used to meet this compliance requirement?

- AWS Key Management Service (AWS KMS)
- AWS CloudHSM
- AWS Secrets Manager
- AWS Certificate Manager

**Correct Answer:** AWS CloudHSM
**Why Correct:** CloudHSM provides single-tenant, dedicated FIPS 140-2 Level 3 validated Hardware Security Modules (HSMs) inside your VPC. You have full control over HSM, keys, policies. Designed for regulatory mandates requiring dedicated hardware, not multi-tenant. You can also create KMS Custom Key Store backed by CloudHSM cluster - best of both (KMS API + CloudHSM compliance).
**Why Others Wrong:** KMS = multi-tenant/shared (AWS manages hardware). Secrets Manager = stores secrets, not dedicated hardware encryption. ACM = SSL certificates.

### 2. AMI Region Constraint
**Question:** An AWS user is trying to launch an Amazon Elastic Compute Cloud (Amazon EC2) instance in a given region. What is the region-specific constraint that the Amazon Machine Image (AMI) must meet so that it can be used for this EC2 instance?

- You should use an Amazon Machine Image (AMI) from the same region, as it improves the performance of the Amazon EC2 instance
- You can use an Amazon Machine Image (AMI) from a different region, but it degrades the performance of the Amazon EC2 instance
- You must use an Amazon Machine Image (AMI) from the same region as that of the Amazon EC2 instance. The region of the Amazon Machine Image (AMI) has no bearing on the performance of the Amazon EC2 instance
- An Amazon Machine Image (AMI) is a global entity, so the region is not applicable

**Correct Answer:** You must use an Amazon Machine Image (AMI) from the same region as that of the Amazon EC2 instance. The region of the Amazon Machine Image (AMI) has no bearing on the performance of the Amazon EC2 instance
**Why Correct:** AMIs are regional resources. Mandatory constraint, not performance. You cannot launch in us-east-1 using AMI only in us-west-2. Must copy AMI to destination region first. Performance myth is false.
**Why Wrong:** Options 1 and 2 say region affects performance - false. Option 4 says AMI is global - false, only S3, IAM are global.

### 3. Automate Operations Using Chef and Puppet
**Question:** A developer would like to automate operations on his on-premises environment using Chef and Puppet. Which AWS service can help with this task?

- AWS Elastic Beanstalk
- AWS OpsWorks
- AWS CloudFormation
- AWS Systems Manager

**Correct Answer:** AWS OpsWorks (OpsWorks for Chef Automate / OpsWorks for Puppet Enterprise)
**Why Correct:** OpsWorks is configuration management service that automates operations using Chef and Puppet, supports AWS and On-Premises. Uses existing recipes/manifests directly.
**Why Wrong:** Systems Manager can automate on-prem but not natively Chef/Puppet. Beanstalk = PaaS. CloudFormation = infra templates.

### 4. Services with Data Encryption Automatically Enabled (Select Two)
**Question:** Which of the following AWS services have data encryption automatically enabled? (Select two)

- Amazon Elastic Block Store (Amazon EBS)
- AWS Storage Gateway
- Amazon Elastic File System (Amazon EFS)
- Amazon S3 Glacier

**Correct Answer:**
- AWS Storage Gateway
- Amazon S3 Glacier / S3 Glacier Deep Archive (and now Amazon S3 after Jan 5 2023 - SSE-S3 AES-256 by default)

**Why Correct:** All data written to Storage Gateway and S3 Glacier is automatically encrypted at rest AES-256, cannot disable.
**Why Wrong:** EBS and EFS require you to manually enable encryption at creation or account-level default.

### 5. Managed NoSQL for Active-Active East and West US
**Question:** A company wants to improve resiliency of its flagship application so it wants to move from traditional database to managed AWS NoSQL database service to support active-active configuration in both East and West US regions. Active-active cross-region support is prime criteria. Which AWS database service is right fit?

- Amazon DynamoDB with Global Tables
- Amazon DocumentDB
- Amazon RDS with Multi-AZ
- Amazon ElastiCache Global Datastore

**Correct Answer:** Amazon DynamoDB with Global Tables
**Why Correct:** DynamoDB Global Tables = fully managed, active-active, multi-region replication, <1 sec replication, both regions can do reads AND writes (last-writer-wins). Created in us-east-1, add us-west-2 as replica.
**Why Wrong:** DocumentDB, Keyspaces don't provide turnkey active-active cross-region. RDS/Aurora Global is SQL and active-passive (1 primary writer). ElastiCache Global Datastore is cache, not primary NoSQL DB.

### 6. Centralize Server Logs for EC2 and On-Premises (Hybrid)
**Question:** An IT company has hybrid cloud architecture and wants to centralize server logs for Amazon EC2 instances and on-premises servers. Which is MOST effective?

- Use AWS Lambda to send log data from EC2 instance as well as on-premises servers to CloudWatch Logs
- Use AWS CloudTrail for EC2 instance and Amazon CloudWatch Logs for on-premises servers
- Use Amazon CloudWatch Logs for both EC2 instance and on-premises servers
- Use Amazon CloudWatch Logs for EC2 instance and AWS CloudTrail for on-premises servers

**Correct Answer:** Use Amazon CloudWatch Logs for both EC2 instance and on-premises servers
**Why Correct:** Unified CloudWatch Agent installs on EC2 AND on-prem Windows/Linux, collects logs/metrics, sends to central CloudWatch Logs Log Group for search/alarms/retention. Stream to S3 via Firehose for long-term.
**Why Wrong:** Lambda = unnecessary complexity, Agent does it directly. CloudTrail = logs AWS API activity (who called what API), NOT OS logs like /var/log/messages, cannot be installed on-prem.

### 7. AWS Compute Optimizer Recommendations (Select Two)
**Question:** AWS Compute Optimizer delivers recommendations for which AWS resources? (Select two)

- Amazon EC2 instances, Amazon EFS
- Amazon EC2 instances, Amazon EC2 Auto Scaling groups
- Amazon EFS, AWS Lambda functions
- Amazon EBS, AWS Lambda functions

**Correct Answer:**
- Amazon EC2 instances, Amazon EC2 Auto Scaling groups
- Amazon EBS, AWS Lambda functions

**Why Correct:** Compute Optimizer supports: EC2 instances, Auto Scaling Groups, EBS volumes, Lambda functions, ECS Services on Fargate, Commercial Software Licenses. Does NOT support EFS.
**Why Wrong:** Any option containing EFS is invalid.

### 8. Discover Sensitive Data on S3 to Prevent Leaks (Healthcare Startup)
**Question:** A Silicon Valley based healthcare startup stores anonymized patient health data on Amazon S3. CTO wants to ensure any sensitive data on S3 is discovered and identified to prevent sensitive data leaks. Which AWS service?

- Amazon GuardDuty
- Amazon Macie
- Amazon Inspector
- Amazon Detective

**Correct Answer:** Amazon Macie
**Why Correct:** Macie = fully managed data security/privacy service that uses ML and pattern matching to automatically discover, classify, protect sensitive data in S3 (PII, PHI, financial). Inventories S3, continuous scans, dashboards + alerts via Security Hub/EventBridge. For healthcare: managed identifiers for patient names, health records.
**Why Wrong:** GuardDuty = threat detection. Inspector = vuln scanner for EC2/ECR. Detective = investigation.

### 9. Personalized View of Status of AWS Services Part of Your Architecture
**Question:** Which service gives a personalized view of the status of the AWS services that are part of your cloud architecture so you can quickly assess impact on your business when AWS service(s) are experiencing issues?

- Amazon CloudWatch
- AWS Health - Service Health Dashboard
- AWS Health - Your Account Health Dashboard (Personal Health Dashboard)
- Amazon Inspector

**Correct Answer:** AWS Health - Your Account Health Dashboard (Personal Health Dashboard)
**Why Correct:** Two dashboards: Service Health Dashboard = PUBLIC/general status of ALL services for everyone. Your Account Health Dashboard = PERSONALIZED - only services part of YOUR architecture, how issue impacts YOUR resources, upcoming maintenance, alerts via EventBridge. Keyword: personalized, your account, your resources.
**Why Wrong:** CloudWatch = your metrics/logs, not AWS service health. Service Health Dashboard = not personalized. Inspector = EC2/ECR vuln scanning.

### 10. Advantages of AWS Cloud (Select TWO)
**Question:** Which of the following are advantages of using AWS Cloud? (Select TWO)

- Increase speed and agility
- AWS is responsible for security in the cloud
- Trade operational expense for capital expense
- Limited scaling
- Stop guessing about capacity
- Trade capital expense for variable expense

**Correct Answer:**
- Increase speed and agility
- Stop guessing about capacity (or Trade capital expense for variable/operational expense - depending on options wording)

**Why Correct:** 6 Official Advantages: 1) Trade capital expense for variable expense (CapEx->OpEx), 2) Benefit from massive economies of scale, 3) Stop guessing about capacity, 4) Increase speed and agility, 5) Stop spending money running data centers, 6) Go global in minutes.
**Why Wrong:** "AWS is responsible for security IN the cloud" = reversed. AWS is OF the cloud, Customer is IN. "Trade operational for capital" = reversed. "Limited scaling" = opposite, it's elastic/unlimited.

### 11. Serverless Computing Services Offered by AWS (Select Two)
**Question:** Which of the following are the serverless computing services offered by AWS? (Select two)

- AWS Lambda
- AWS Elastic Beanstalk
- AWS Fargate
- Amazon EC2

**Correct Answer:**
- AWS Lambda
- AWS Fargate

**Why Correct:** Serverless = you don't manage servers. Lambda = core serverless compute, upload code. Fargate = serverless compute for containers (ECS/EKS without EC2).
**Why Wrong:** Beanstalk = PaaS but provisions EC2 underneath, not serverless. EC2 = IaaS, you manage server.

### 12. Identify Under-Utilized EC2 Off-the-Shelf Without Manual Config (Select Two)
**Question:** An IT company is on cost-optimization spree and wants to identify all EC2 instances that are under-utilized. Which AWS services can be used off-the-shelf without manual configurations? (Select two)

- Amazon CloudWatch
- AWS Cost Explorer
- AWS Budgets
- AWS Cost & Usage Report (CUR)
- AWS Trusted Advisor

**Correct Answer:**
- AWS Trusted Advisor
- AWS Cost Explorer (Ideal answer is Trusted Advisor + AWS Compute Optimizer)

**Why Correct:** Trusted Advisor has built-in check "Low Utilization EC2 Instances" - auto finds idle/under-utilized and tells to stop/downsize, zero config. Cost Explorer has Rightsizing Recommendations powered by Compute Optimizer, auto identifies under-utilized and recommends smaller types. Compute Optimizer is best for this if present.
**Why Wrong:** CloudWatch DOES show CPU but requires manual alarms/dashboards/manual analysis per instance - not off-the-shelf.

### 13. Debug Performance Issues for Serverless Microservices Application
**Question:** The DevOps team at an e-commerce company is trying to debug performance issues for its serverless application built using microservices architecture. Which AWS service would you recommend?

- AWS X-Ray
- Amazon Pinpoint
- AWS CloudFormation
- AWS Trusted Advisor

**Correct Answer:** AWS X-Ray
**Why Correct:** X-Ray = Distributed tracing service. Traces requests as they travel through microservices, Lambda, API Gateway, DynamoDB, etc. Shows service map, latency bottlenecks, errors, where perf degrades. Keyword: serverless + microservices + debug performance.
**Why Wrong:** Pinpoint = marketing campaigns/push notifications. CloudFormation = infra as code. Trusted Advisor = cost/security/perf recommendations, not live debugging.

### 14. Analytics Application with Speech-Based Interface
**Question:** A unicorn startup building analytics application with support for speech-based interface. App will accept speech-based input and then convey results via speech. Which solution?

- Use Amazon Polly to convert speech to text for downstream analysis. Then use Amazon Transcribe to convey text results via speech
- Use Amazon Transcribe to convert speech to text for downstream analysis. Then use Amazon Polly to convey text results via speech
- Use Amazon Polly to convert speech to text for downstream analysis. Then use Amazon Translate to convey text results via speech
- Use Amazon Translate to convert speech to text for downstream analysis. Then use Amazon Polly to convey text results via speech

**Correct Answer:** Use Amazon Transcribe to convert speech to text for downstream analysis. Then use Amazon Polly to convey text results via speech
**Why Correct:** Transcribe = Speech to Text (STT) - audio to text. Polly = Text to Speech (TTS) - text to audio. Translate = text to text translation only. Flow: User Speech -> Transcribe [Speech->Text] -> Analytics -> Polly [Text->Speech] -> User Speech.

### 15. MFA Device That You Can Plug Into USB Port
**Question:** Which AWS authentication mechanisms supports an AWS Multi-Factor Authentication (AWS MFA) device that you can plug into a USB port on your computer?

- Hardware Multi-Factor Authentication (AWS MFA) device
- U2F security key
- Virtual Multi-Factor Authentication (AWS MFA) device
- SMS text message-based Multi-Factor Authentication (AWS MFA)

**Correct Answer:** U2F security key
**Why Correct:** U2F security key = physical device like YubiKey that plugs into USB and tap to authenticate. Virtual MFA = app on smartphone (Google Authenticator). Hardware MFA = small key-fob/token with LCD screen showing 6-digit code, battery powered, press button, NOT USB. SMS MFA = AWS does NOT support SMS as MFA for IAM (deprecated).

### 16. MFA Device With No Physical Device - Easy for Travel
**Question:** Which AWS authentication mechanism supports MFA without needing a physical device, easy for travel?

- Hardware MFA device
- U2F security key
- Virtual Multi-Factor Authentication (MFA) device
- SMS MFA

**Correct Answer:** Virtual Multi-Factor Authentication (MFA) device
**Why Correct:** Virtual MFA = software based app on existing smartphone (Google Authenticator, Authy) generates TOTP code. No extra physical device needed. Perfect for travel.
**Why Wrong:** Hardware MFA and U2F = physical devices you must carry.

### 17. Cost Optimization - Purchase RIs and Auto Scaling
**Question:** A company wants to optimize EC2 costs. Which two actions help?

- Purchase Amazon EC2 Reserved Instances (RIs)
- Set up Auto Scaling groups to align number of instances with demand
- Build its own servers
- Vertically scale EC2 instances
- Opt for higher AWS Support plan

**Correct Answer:**
- Purchase Amazon EC2 Reserved instances (RIs) / Savings Plans
- Set up Auto Scaling groups to align number of instances with demand

**Why Correct:** RIs = up to 72% discount for steady-state predictable usage. Auto Scaling = run only number you need based on demand, scale in when low, out when high, no wasted money.
**Why Wrong:** Build own servers = CapEx, maintenance, lose elasticity. Vertically scale = just bigger, increases cost, not optimization (rightsizing down would help but "vertically scale" alone not). Higher Support plan = extra cost, doesn't reduce EC2 bill.

### 18. Recommendation Engine Data - LEAST Operational Overhead - Key-Value Millisecond
**Question:** For a recommendation engine data store requiring key-value lookups like userId -> list of recommended products, millisecond latency, least operational overhead, any scale, which database?

- Amazon DynamoDB
- Amazon RDS
- Amazon S3
- Amazon Neptune

**Correct Answer:** Amazon DynamoDB
**Why Correct:** DynamoDB = fully managed, serverless NoSQL, no servers to provision/patch/manage, auto scales to any throughput, single-digit millisecond latency, perfect for recommendation cache.
**Why Wrong:** RDS = relational, manage scaling/patching, higher overhead, not ideal for simple key-value. S3 = object storage, not low-latency DB. Neptune = graph DB for highly connected data like social graphs/fraud detection.

### 19. CAF Platform Perspective Stakeholders (Select Two)
**Question:** Which option is a common stakeholder role for the AWS Cloud Adoption Framework (AWS CAF) platform perspective? (Select two)

- Engineer
- Chief Data Officer (CDO)
- Chief Product Officer (CPO)
- Chief Information Officer (CIO)
- Chief Technology Officer (CTO)

**Correct Answer:**
- Engineer
- Chief Technology Officer (CTO) (or CIO - both Platform perspective)

**Why Correct:** CAF has 6 Perspectives: Business, People, Governance, Platform, Security, Operations. Platform = accelerating delivery of cloud workloads via enterprise-grade scalable hybrid cloud. Common stakeholders: CTO, technology leaders, architects, engineers, CIO.
**Why Wrong:** CDO = Governance Perspective (data governance). CPO = Business Perspective.

### 20. Container Service - Serverless for Containers
**Question:** Which AWS service is a serverless container service?

- AWS Elastic Beanstalk
- Amazon SNS
- AWS Fargate
- Amazon SageMaker

**Correct Answer:** AWS Fargate
**Why Correct:** Fargate = serverless compute engine for containers, run ECS and EKS containers without managing EC2 servers.
**Why Wrong:** Beanstalk = PaaS for web apps, not dedicated container service. SNS = pub/sub messaging. SageMaker = ML service.

### 21. Best Practices AWS Organizations (Select Two)
**Question:** Which are best practices when using AWS Organizations? (Select TWO)

- Never use tags for billing
- Create AWS accounts per department
- Do not use AWS Organizations to automate AWS account creation
- Disable AWS CloudTrail on several accounts
- Restrict account privileges using Service Control Policies (SCP)

**Correct Answer:**
- Create AWS accounts per department
- Restrict account privileges using Service Control Policies (SCP)

**Why Correct:** Create accounts per department/workload/team/environment for isolation, billing, blast-radius. Use SCPs as permission guardrails.
**Why Wrong:** Never use tags = SHOULD use tags (Cost Allocation Tags + Tag Policies). Do not automate = SHOULD automate via CreateAccount API / Control Tower. Disable CloudTrail = SHOULD enable in ALL accounts, ideally Organization Trail.

### 22. Hybrid Deployment Definition
**Question:** An organization has on-premises data center and AWS Cloud connected and working together. Which deployment model?

- Private deployment
- Cloud deployment
- Hybrid deployment
- Mixed deployment

**Correct Answer:** Hybrid deployment
**Why Correct:** Hybrid = Combination of On-prem + Cloud (AWS). Private = on-prem private cloud only. Cloud = everything on AWS only. Mixed = not official AWS term.

### 23. Cheapest Long-Term Archival S3 Storage - Highest Latency
**Question:** Which S3 storage class is cheapest, lowest-cost for long-term archival where you rarely need data, highest first-byte latency?

- S3 Standard
- S3 Intelligent-Tiering
- S3 Glacier Flexible Retrieval
- S3 Glacier Deep Archive

**Correct Answer:** S3 Glacier Deep Archive
**Why Correct:** Deep Archive = cheapest, designed for long-term archival 7-10 years+ for compliance. Durability 11 9's. Retrieval: Standard within 12 hours, Bulk within 48 hours (HIGHEST latency). Flexible Retrieval = minutes to hours (Expedited 1-5 mins, Standard 3-5 hours, Bulk 5-12 hours). Standard/Intelligent-Tiering = milliseconds.

### 24. Shared File System for Hundreds of EC2 + Append Data
**Question:** Application accessed by hundreds of EC2 instances simultaneously and needs to append data to existing files. Which storage?

- Amazon Elastic File System (Amazon EFS)
- Amazon S3
- Amazon EBS
- Instance Store

**Correct Answer:** Amazon Elastic File System (Amazon EFS)
**Why Correct:** EFS = fully managed NFS file system, mount on hundreds/thousands of EC2 in multiple AZs simultaneously, supports file appends/locks. Perfect for batch analytics.
**Why Wrong:** S3 = object storage, immutable, cannot append, must re-write whole object. EBS = block storage attachable to ONE EC2 at time in one AZ (Multi-Attach limited to 16 io1/io2 same AZ). Instance Store = ephemeral, local to single EC2 host, lost on stop/terminate.

### 25. Schemaless Database Requirement
**Question:** Application requires schemaless database. Which service?

- Amazon DynamoDB
- Amazon Aurora
- Amazon RDS
- Amazon Redshift

**Correct Answer:** Amazon DynamoDB
**Why Correct:** DynamoDB = NoSQL schemaless, no pre-defined schema, each item can have different attributes.
**Why Wrong:** Aurora/RDS = relational fixed schema. Redshift = data warehouse, requires defined schema for structured data.

### 26. Centrally Manage Access Across Multiple AWS Accounts
**Question:** Company has multiple AWS accounts in AWS Organizations and wants to centrally manage access with single place to create users and SSO. Which service?

- AWS IAM Identity Center (previously AWS Single Sign-On / AWS SSO)
- AWS IAM
- AWS Cognito
- AWS CLI

**Correct Answer:** AWS IAM Identity Center (AWS SSO)
**Why Correct:** IAM Identity Center built exactly for this - manage access centrally across multiple accounts in Organizations, single place to create users and provide Single Sign-On.
**Why Wrong:** IAM = works per-account, managing across 10-100 accounts complex (need roles/trust). Cognito = auth for your own web/mobile app users, not AWS accounts. CLI = command-line tool.

### 27. Professional Services Firm to Help Migrate to AWS
**Question:** Corporation needs expert hands-on advice to migrate to AWS, architect, build and manage workloads. Which help?

- APN Consulting Partner
- APN Technology Partner
- Concierge Support Team
- AWS Trusted Advisor

**Correct Answer:** APN Consulting Partner
**Why Correct:** Consulting Partners = professional services firms like Accenture, Deloitte certified by AWS to help customers migrate, architect, build, manage.
**Why Wrong:** Technology Partner = companies providing software/hardware products that integrate with AWS (Snowflake, Datadog). Concierge = helps with billing/account/Enterprise Support only. Trusted Advisor = automated tool for cost/security/performance checks, not people.

### 28. Identify Unattached / Underutilized EBS Volumes
**Question:** Which AWS service can identify unattached / underutilized EBS volumes for cost optimization?

- AWS Trusted Advisor
- Amazon Inspector
- AWS Config
- Amazon CloudWatch

**Correct Answer:** AWS Trusted Advisor
**Why Correct:** Trusted Advisor scans environment and flags cost optimization checks like Unattached Elastic IP, Underutilized EBS Volumes, Idle RDS, Idle Load Balancers.
**Why Wrong:** Inspector = security vuln scanner for EC2/ECR. Config = records/audits config changes for compliance. CloudWatch = metrics/alarms, could look at EBS metrics but won't proactively identify unattached/underutilized like Trusted Advisor.

### 29. Forecast Future AWS Costs and Usage
**Question:** Which AWS service can forecast future AWS costs and usage based on past usage?

- AWS Cost Explorer
- AWS Budgets
- AWS Pricing Calculator
- AWS Cost & Usage Report (CUR)

**Correct Answer:** AWS Cost Explorer (and AWS Budgets)
**Why Correct:** Cost Explorer has built-in forecasting engine, looks at past usage and forecasts costs/usage up to 12 months ahead. Budgets also can forecast if you'll exceed budget and alert. Both valid for forecasting.
**Why Wrong:** Pricing Calculator = estimate costs before deploy, not forecast actual running account. CUR = raw detailed CSV dump of all costs/usage, does not forecast, you analyze yourself in Athena/QuickSight.

### 30. Shared Responsibility Model Correct Statements (Select Two)
**Question:** Which are correct statements regarding AWS Shared Responsibility Model? (Select two)

- Configuration management of customer resources like Security Groups, IAM policies is AWS responsibility
- Awareness & Training of customer employees is AWS responsibility
- For IaaS like EC2, customer is responsible for maintaining guest OS
- For abstracted services like S3, AWS operates infrastructure layer, OS, and platforms
- AWS is responsible for Security 'of' the Cloud

**Correct Answer:**
- For abstracted services like Amazon S3, AWS operates infrastructure layer, operating system, and platforms
- AWS is responsible for Security 'of' the Cloud

**Why Correct:** Shared Responsibility = AWS OF Cloud (physical datacenters, hardware, networking, hypervisor), Customer IN Cloud. For abstracted/managed services like S3, DynamoDB, SQS - AWS manages infra to OS to platform, customer only data/access policies/encryption.
**Why Wrong:** For IaaS like EC2, customer IS responsible for guest OS patching/updates/antivirus (AWS only host/hypervisor) - but options 4 and 5 are more textbook. Awareness & Training is customer's responsibility.

### 31. Block-Level Storage Types in AWS (Select Two)
**Question:** Which are block-level storage types? (Select two)

- Amazon EBS
- Instance Store
- Amazon S3
- Amazon EFS
- Amazon ECS

**Correct Answer:**
- Amazon Elastic Block Store (Amazon EBS)
- Instance Store

**Why Correct:** Block storage: EBS = persistent block for EC2. Instance Store = ephemeral block physically attached to EC2 host. Object: S3. File: EFS NFS. ECS = container orchestration, not storage.

### 32. Historic Data 10 Years Durable Cost-Effective Compliance
**Question:** Company needs to store historic data for 10 years, durable, cost-effective, compliance. Which S3 storage?

- Amazon S3 Glacier Deep Archive
- Amazon S3 Glacier Flexible Retrieval
- AWS Storage Gateway
- Amazon EFS

**Correct Answer:** Amazon S3 Glacier Deep Archive
**Why Correct:** Deep Archive = cheapest, long-term archival 7-10 years+ for compliance, 11 9's durability, retrieval 12 hours.
**Why Wrong:** Flexible Retrieval = more expensive, for data accessed 1-2 times per quarter. Storage Gateway = hybrid cloud connecting on-prem to AWS storage, not archival class. EFS = expensive file system for active workloads.

### 33. Privately Connect Two VPCs from Different Business Units
**Question:** Two business units have separate VPCs and want to share data privately without internet, low latency. Most optimal?

- VPC peering connection
- AWS Site-to-Site VPN
- VPC Endpoint
- AWS Direct Connect

**Correct Answer:** VPC peering connection
**Why Correct:** VPC peering = most optimal way to privately connect two VPCs. Traffic stays on AWS private backbone, no internet, no encryption overhead, low latency.
**Why Wrong:** Site-to-Site VPN = on-prem to AWS VPC, not VPC to VPC. VPC Endpoint = private access to AWS services like S3/DynamoDB from inside VPC. Direct Connect = dedicated physical line from on-prem to AWS.

### 34. Benefits of AWS Elastic Load Balancing (ELB) (Select Two)
**Question:** Which are benefits of AWS Elastic Load Balancing? (Select two)

- Fault tolerance
- High availability
- Less costly
- Storage
- Agility

**Correct Answer:**
- Fault tolerance
- High availability

**Why Correct:** ELB distributes traffic across multiple healthy targets in multiple AZs. High Availability: if one AZ/instance down, routes to healthy in other AZs. Fault tolerance: health checks, only sends to healthy instances, app tolerates failures.
**Why Wrong:** Storage = S3/EBS benefit. Less costly/Agility = general Cloud benefits, not specific ELB.

### 35. Prohibited Uses of AWS Services Policy
**Question:** Which policy describes prohibited uses of AWS services - illegal activities, abuse, spamming, hosting malicious content?

- AWS Acceptable Use Policy
- Applicable Use Policy
- Trusted Advisor
- Fair Use Policy

**Correct Answer:** AWS Acceptable Use Policy (AUP)

### 36. Serverless Scheduled Task Every Monday 2 AM Runs 5 Minutes
**Question:** Company needs serverless solution for backup task scheduled every Monday 2 AM that runs for 5 minutes. Which two services? (Select two)

- AWS Lambda
- Amazon EventBridge
- Amazon EC2
- AWS Step Function
- AWS Systems Manager

**Correct Answer:**
- AWS Lambda
- Amazon EventBridge

**Why Correct:** EventBridge = serverless scheduler, create cron rule 0 2 ? * MON * to trigger every Monday 2 AM. Lambda = serverless compute, perfect for 5 min backup (max timeout 15 min). EventBridge invokes Lambda on schedule.
**Why Wrong:** EC2 = not serverless. Step Function = serverless orchestration for complex workflows with multiple steps, overkill for simple 5-min task. Systems Manager = managing EC2 fleets/patching.

### 37. Simplest Way to Break Down Bill by Department
**Question:** Simplest way to break down AWS bill by department?

- Create tags for each department and activate as Cost Allocation Tags
- Create different accounts for different departments using AWS Organizations
- Use AWS Budgets
- Use AWS Cost Explorer

**Correct Answer:** Create tags for each department and activate as Cost Allocation Tags (Simplest). Best practice/secure way = Create different accounts per department using Organizations for natural separation + consolidated billing + security boundaries.

### 38. Route 53 Routing for Blue/Green 80% / 20%
**Question:** Which Route 53 routing lets you route traffic to multiple resources in proportions you specify - e.g., 80% to one server and 20% to another. Useful for blue/green, A/B testing.

- Weighted routing
- Simple routing
- Latency-based routing
- Failover routing

**Correct Answer:** Weighted routing
**Why Correct:** Weighted = route in proportions specified. Simple = single resource only. Latency-based = lowest latency to user. Failover = Active/Passive for DR.

### 39. Well-Architected Framework - Automate Operations and IaC
**Question:** Which Well-Architected Framework pillar recommends automating operations and maintaining Infrastructure as Code (IaC) using services like CloudFormation?

- Operational Excellence
- Security
- Reliability
- Performance Efficiency

**Correct Answer:** Operational Excellence
**Why Correct:** Operational Excellence focuses on perform operations as code, make frequent small reversible changes, automate manual tasks.

### 40. Compare Cost of Running On-Prem vs AWS Cloud
**Question:** Which tool is specifically designed to compare cost of running infrastructure on-premises vs on AWS Cloud?

- AWS Pricing Calculator (previously Total Cost of Ownership - TCO Calculator / Migration Evaluator)
- AWS Cost Explorer
- AWS Trusted Advisor
- AWS Budgets

**Correct Answer:** AWS Pricing Calculator / TCO Calculator / Migration Evaluator
**Why Correct:** Pricing/TCO Calculator designed to compare on-prem vs AWS. Input on-prem setup, estimates AWS cost.
**Why Wrong:** Cost Explorer = analyze existing AWS spend. Trusted Advisor = cost optimization/security/perf checks in existing account. Budgets = set alerts when cost exceeds threshold.

### 41. Service Health RSS Feed
**Question:** Which service provides RSS feed to be notified of AWS service interruptions/outages?

- AWS Health Dashboard - Service Health
- AWS Health Dashboard - Your Account Health
- Amazon SNS
- AWS Lambda

**Correct Answer:** AWS Health Dashboard - Service Health
**Why Correct:** Service Health = public dashboard showing status of all AWS services in all regions, provides RSS feed for service interruptions.
**Why Wrong:** Your Account Health = personalized to your account, shows events affecting your specific resources, does NOT provide RSS for all services. SNS/Lambda = not related.

### 42. Low-Latency Gameplay for End-Users in Various Locations (From Latest Screenshot)
**Question:** Gaming company looking for technology/service that can deliver consistent low-latency gameplay to ensure great user experience for end-users in various locations.

- AWS Wavelength
- AWS Direct Connect
- AWS Edge Locations
- AWS Local Zones

**Correct Answer Note:** There is conflict in exam dumps. Two answers are accepted depending on wording:
- **AWS Edge Locations** = Sites in 400+ cities globally used by CloudFront, Global Accelerator to cache content and deliver low-latency gameplay/data to end-users in various locations globally. Correct if question says "various locations globally / cache content".
- **AWS Local Zones** = Extension of Region in specific large metro city (e.g., Los Angeles), place compute/storage closer to large population centers for very low latency. Correct if question says "deploy workloads closer to end-users / run EC2 locally".

**Why Others Wrong:** Wavelength = ultra-low latency apps on 5G networks. Direct Connect = dedicated line from on-prem to AWS, not for end-user access.

### 43. Automate Code Deployments to EC2 and On-Premises
**Question:** Which service automates code deployments to both Amazon EC2 and on-premises servers?

- AWS CodeDeploy
- AWS CodeCommit
- AWS CloudFormation
- AWS CodePipeline

**Correct Answer:** AWS CodeDeploy
**Why Correct:** CodeDeploy automates code deployments to EC2 and on-prem.
**Why Wrong:** CodeCommit = Git-based source code repo. CloudFormation = infra as code. CodePipeline = orchestrates CI/CD pipeline - uses CodeDeploy for deployment stage.

### 44. RDS Multi-AZ Enhances What?
**Question:** What does Amazon RDS Multi-AZ enhance?

- Enhances database availability
- Improves performance for read-heavy workloads
- Reduces costs
- Protects from regional failure

**Correct Answer:** Amazon RDS Multi-AZ enhances database availability
**Why Correct:** Multi-AZ with 1 standby maintains synchronous standby copy in different AZ. If primary fails, auto failover to standby - for HA/Fault Tolerance. Standby cannot serve reads.
**Why Wrong:** Improves read perf = Read Replicas. Reduces costs = costs more (2 instances). Regional failure = Multi-AZ within single Region, need Cross-Region/Multi-Region for regional DR.

### 45. Massive Economies of Scale Benefit
**Question:** Because AWS aggregates usage from hundreds of thousands of customers, it achieves huge economies of scale, which allows it to lower pay-as-you-go prices. Which advantage?

- Massive economies of scale
- Increase speed and agility
- High availability
- Elasticity

**Correct Answer:** Massive economies of scale

### 46. Automatically Add/Remove EC2 Instances to Handle Current Traffic Demand
**Question:** Which service automatically adds or removes EC2 instances to ensure you have right capacity to handle current traffic demand?

- Amazon EC2 Auto Scaling
- Multi-AZ deployment
- Application Load Balancer
- Network Load Balancer

**Correct Answer:** Amazon EC2 Auto Scaling
**Why Correct:** Auto Scaling adds/removes EC2 to match demand.
**Why Wrong:** Multi-AZ = HA. ALB/NLB = distribute traffic, not scale number of instances.

### 47. Securely Shell Into Private EC2 Without Port 22, Public IP, Bastion
**Question:** Which service lets you securely shell (SSH) into private EC2 instances through browser or CLI without opening inbound port 22, public IP, bastion host/key pairs?

- AWS Systems Manager Session Manager
- EC2 Instance Connect
- Route 53
- Amazon Inspector

**Correct Answer:** AWS Systems Manager Session Manager
**Why Correct:** Session Manager works via SSM Agent outbound connection, no port 22, no public IP, no bastion/key pairs.
**Why Wrong:** EC2 Instance Connect = still requires port 22 open and public IP/internet. Route 53 = DNS. Inspector = vuln assessment.

### 48-65. Core Repeats from Earlier Photos (For Completeness)


### 48. Deploy Identical Resources Across All Regions/Accounts Using Templates + Estimate Costs
**Question:** A Cloud Practitioner would like to deploy identical resources across all AWS regions and accounts using templates while estimating costs. Which AWS service can assist with this task?

- AWS Directory Service for Microsoft Active Directory
- Amazon Lightsail
- AWS CloudFormation
- AWS CodeDeploy

**Correct Answer:** AWS CloudFormation
**Why Correct:** CloudFormation uses templates (JSON/YAML) and CloudFormation StackSets to deploy identical resources across all regions and accounts in one operation. It also has built-in cost estimation (via Pricing Calculator integration) for templates.
**Why Wrong:** Directory Service = Managed AD. Lightsail = simple VPS bundle. CodeDeploy = deploys application code to EC2/on-prem, not infrastructure templates.

### 49. Run Docker Containers With Access to Underlying Servers
**Question:** A startup runs proprietary application on docker containers. As a Cloud Practitioner, which AWS service would you recommend so that startup can run containers and still have access to underlying servers?

- Amazon Elastic Container Service (Amazon ECS) - EC2 Launch Type
- AWS Fargate
- Amazon Elastic Container Registry (ECR)
- AWS Lambda

**Correct Answer:** Amazon Elastic Container Service (Amazon ECS) - EC2 Launch Type
**Why Correct:** ECS with EC2 launch type lets you run Docker containers while you still manage and have SSH access to the underlying EC2 instances.
**Why Wrong:** Fargate = serverless containers, no server access. ECR = only Docker registry to store images. Lambda = serverless functions.

### 50. Lowest Cost Long-Term EC2 With No Interruption
**Question:** A startup wants to provision an EC2 instance for the lowest possible cost for a long-term duration but needs to make sure that the instance would never be interrupted. Which option?

- EC2 Spot Instance
- EC2 On-Demand Instance
- EC2 Reserved Instance (RI) / Savings Plan
- EC2 Dedicated Host

**Correct Answer:** EC2 Reserved Instance (RI) / Savings Plan (1-year or 3-year)
**Why Correct:** Reserved Instances give up to 72% discount vs On-Demand for long-term and are never interrupted. Savings Plans are new model of same.
**Why Wrong:** Spot = cheapest but CAN be interrupted with 2-min notice. On-Demand = no interruption but expensive long-term. Dedicated Host = most expensive for compliance/licensing.

### 51. Provision Same AWS Infrastructure Across Multiple AWS Accounts and Regions
**Question:** Which AWS service will you use to provision the same AWS infrastructure across multiple AWS accounts and regions?

- AWS OpsWorks
- AWS Systems Manager
- AWS CodeDeploy
- AWS CloudFormation

**Correct Answer:** AWS CloudFormation (with StackSets)
**Why Correct:** CloudFormation StackSets is designed to provision same stack from one template across multiple accounts and regions.
**Why Wrong:** OpsWorks = Chef/Puppet config management. Systems Manager = manage EC2 fleets. CodeDeploy = deploy application code.

### 52. NOT a Feature of Amazon Inspector
**Question:** Which of the following options is NOT a feature of Amazon Inspector?

- Track configuration changes
- Automate security assessments
- Inspect running OS against known vulnerabilities
- Analyze against unintended network accessibility

**Correct Answer:** Track configuration changes
**Why Correct:** Inspector DOES: Automate security assessments, Inspect running OS for known vulnerabilities, Analyze against unintended network accessibility. Tracking configuration changes is AWS Config.
**Why Wrong Options Are Actually Features of Inspector:** The other three ARE features of Inspector.

### 53. Account Activity Meets Governance, Compliance, Auditing
**Question:** A financial services company wants to ensure that its AWS account activity meets governance, compliance and auditing norms. Which service would you recommend?

- AWS Trusted Advisor
- AWS Config
- AWS CloudTrail
- Amazon CloudWatch

**Correct Answer:** AWS CloudTrail
**Why Correct:** CloudTrail records all API calls/account activity - who did what, when, from where. Perfect for governance, compliance, auditing trail.
**Why Wrong:** Config = tracks resource configuration changes. Trusted Advisor = best practice checks. CloudWatch = performance monitoring.

### 54. Always Free to Use (Select Two)
**Question:** Which AWS services are always free to use (Select two)?

- AWS Identity and Access Management (AWS IAM)
- AWS Auto Scaling
- Amazon DynamoDB
- Amazon EC2
- Amazon S3

**Correct Answer:**
- AWS Identity and Access Management (AWS IAM)
- AWS Auto Scaling

**Why Correct:** IAM users/groups/roles/policies always free. Auto Scaling service itself free (pay only underlying resources it launches).
**Why Wrong:** DynamoDB/EC2/S3 have Free Tier limits but not always free - you pay after limits (EC2 Free Tier only 12 months).

### 55. Reserved EC2 Sharing Across Multiple Units - Most Cost-Optimal
**Question:** A company uses reserved EC2 instances across multiple units with each unit having its own AWS account. However, some units under-utilize their reserved instances while other units need more reserved instances. As a Cloud Practitioner, which would you recommend as most cost-optimal solution?

- Use AWS Systems Manager to manage AWS accounts of all units and then share the reserved EC2 instances amongst all units
- Use AWS Cost Explorer to manage AWS accounts of all units and then share the reserved EC2 instances amongst all units
- Use AWS Organizations to manage AWS accounts of all units and then share the reserved EC2 instances amongst all units
- Use AWS Trusted Advisor to manage AWS accounts of all units and then share the reserved EC2 instances amongst all units

**Correct Answer:** Use AWS Organizations to manage AWS accounts of all units and then share the reserved EC2 instances amongst all units
**Why Correct:** Organizations with Consolidated Billing automatically shares unused RI discount across member accounts in org.
**Why Wrong:** Systems Manager/Cost Explorer/Trusted Advisor don't manage accounts or enable RI discount sharing.

### 56. Security Assessment Without Prior Approval From AWS
**Question:** A cyber-security agency uses AWS Cloud and wants to carry out security assessments on its own AWS infrastructure without any prior approval from AWS. Which describes/facilitates this practice?

- Network Stress Testing
- Amazon Inspector
- AWS Secrets Manager
- Penetration Testing

**Correct Answer:** Penetration Testing
**Why Correct:** AWS allows Penetration Testing on your own infrastructure without prior approval (policy changed). Inspector is automated vuln scanner tool but policy term "without prior approval" specifically refers to Pen Testing.
**Why Wrong:** Network Stress Testing / DoS testing NOT allowed without prior approval - prohibited. Secrets Manager = stores secrets.

### 57. Operational Insights to Quickly Identify Issues Impacting Applications
**Question:** A Cloud Practitioner would like to get operational insights of its resources to quickly identify any issues that might impact applications using those resources. Which AWS service can help?

- AWS Health Dashboard - Your Account Health
- AWS Trusted Advisor
- AWS Systems Manager
- Amazon Inspector

**Correct Answer:** AWS Systems Manager
**Why Correct:** Systems Manager centralizes operational data from multiple services, resource groups, API activity, config changes, notifications, operational alerts, inventory, patch compliance. Central place for visibility and control.
**Why Wrong:** Health Dashboard Account Health = alerts when AWS itself has events affecting you. Trusted Advisor = cost/perf/security best practices. Inspector = security assessment service.

### 58. Quickly Deploy a Popular Technology on AWS
**Question:** A start-up would like to quickly deploy a popular technology on AWS. As a Cloud Practitioner, which AWS tool would you use?

- AWS Forums
- AWS Whitepapers
- AWS CodeDeploy
- AWS Partner Solutions (formerly Quick Starts)

**Correct Answer:** AWS Partner Solutions (formerly Quick Starts)
**Why Correct:** Partner Solutions are automated reference deployments built by AWS architects and Partners that deploy popular technologies per best practices in minutes (via CloudFormation), reducing hundreds of manual procedures to few steps.
**Why Wrong:** Forums = community Q&A. CodeDeploy = deploys your own code to EC2/on-prem. Whitepapers = technical content to read.

### 59. Linux EC2 Per-Second Billing Terminated Within 30 Seconds - Charge Duration
**Question:** An intern at an IT company provisioned a Linux based On-demand EC2 instance with per-second billing but terminated it within 30 seconds as he wanted to provision another instance type. What is duration for which instance would be charged?

- 30 seconds
- 60 seconds
- 300 seconds
- 600 seconds

**Correct Answer:** 60 seconds
**Why Correct:** There is one-minute minimum charge for Linux EC2 instances. After first minute, per-second billing. So 30s usage billed for 60s.
**Why Wrong:** 300s and 600s contradict, 30s ignores minimum.

### 60. Most Cost-Effective S3 Storage for Thumbnails - Rarely Used, Immediately Accessible, Regenerable
**Question:** A photo sharing web application wants to store thumbnails of user-uploaded images on Amazon S3. Thumbnails are rarely used but need to be immediately accessible from web application. Thumbnails can be regenerated easily if lost. Which is most cost-effective way to store these thumbnails on S3?

- Use Amazon S3 Glacier Flexible Retrieval to store the thumbnails
- Use Amazon S3 Standard-Infrequent Access (S3 Standard-IA) to store the thumbnails
- Use Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA) to store the thumbnails
- Use Amazon S3 Standard to store the thumbnails

**Correct Answer:** Use Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA)
**Why Correct:** Rarely used = IA class. Immediately accessible = NOT Glacier (minutes-hours). Regenerable = OK with single AZ failure = One Zone-IA stores in 1 AZ, costs 20% less than Standard-IA, same durability/throughput/latency, but less availability which is OK here.
**Why Wrong:** Standard = frequent access expensive. Standard-IA = works but 20% more expensive than One Zone-IA when multi-AZ not needed. Glacier Flexible Retrieval = archival, retrieval time minutes-hours, not immediate.

### 61. Primary Benefit of RDS Read Replica Configuration
**Question:** What is the primary benefit of deploying an Amazon RDS database in a Read Replica configuration?

- Read Replica enhances database availability
- Read Replica protects the database from a regional failure
- Read Replica reduces database usage costs
- Read Replica improves database scalability

**Correct Answer:** Read Replica improves database scalability
**Why Correct:** Read Replicas create read-only copies synchronized with master for improved read performance, horizontal scaling of reads. Can place in different Region closer to users.
**Why Wrong:** Enhances availability = Multi-AZ (sync standby in different AZ). Regional failure protection = Multi-Region. Reduces costs = increases costs (extra instance).

### 62. Advantages of AWS Cloud (Select TWO) - Repeat Full
**Question:** Which of the following are the advantages of using the AWS Cloud? (Select TWO)

- Increase speed and agility
- AWS is responsible for security in the cloud
- Trade operational expense for capital expense
- Limited scaling
- Stop guessing about capacity

**Correct Answer:**
- Increase speed and agility
- Stop guessing about capacity (or Trade capital expense for variable expense if worded correctly)

**Why Correct:** From 6 Advantages whitepaper: Increase speed and agility, Stop guessing capacity, Trade CAPEX for OPEX, Economies of scale, Go global in minutes, Stop spending on data centers.
**Why Wrong:** "AWS is responsible for security IN the cloud" = reversed, AWS OF cloud, customer IN. "Trade operational for capital" = reversed, should be capital for operational. "Limited scaling" = opposite, unlimited/elastic.

### 63. CAF Platform Perspective Stakeholder (Select Two) - Repeat Full
**Question:** Which option is a common stakeholder role for the AWS Cloud Adoption Framework (AWS CAF) platform perspective? (Select two)

- Engineer
- Chief Data Officer (CDO)
- Chief Product Officer (CPO)
- Chief Information Officer (CIO)
- Chief Technology Officer (CTO)

**Correct Answer:**
- Engineer
- Chief Technology Officer (CTO) (CIO also valid for Platform perspective)

**Why Correct:** CAF groups 6 perspectives: Business, People, Governance, Platform, Security, Operations. Platform perspective focuses on accelerating delivery of cloud workloads via enterprise-grade scalable hybrid cloud. Comprises 7 capabilities. Common stakeholders: CTO, technology leaders, architects, engineers, CIO.
**Why Wrong:** CPO = Business, CDO = Governance/Data.

### 64. Best Practices When Using AWS Organizations (Select TWO) - Repeat Full
**Question:** Which of the following are the best practices when using AWS Organizations? (Select TWO)

- Never use tags for billing
- Create AWS accounts per department
- Do not use AWS Organizations to automate AWS account creation
- Disable AWS CloudTrail on several accounts
- Restrict account privileges using Service Control Policies (SCP)

**Correct Answer:**
- Create AWS accounts per department
- Restrict account privileges using Service Control Policies (SCP)

**Why Correct:** Organizations helps centrally govern as you grow. Automate account creation, create groups of accounts per business needs, apply policies, simplify billing single payment, central configs and resource sharing via other services integration. Create accounts per department for regulatory restrictions (via SCPs) for better isolation and per-account service limits. Use SCPs to restrict services/actions allowed as permission guardrails on IAM users/roles.
**Why Wrong:** Never use tags = SHOULD use tags standards to categorize resources for billing. Disable CloudTrail = SHOULD enable CloudTrail to monitor activity on all accounts for governance/compliance/risk/auditing. Do not automate creation = SHOULD automate via Organizations APIs to create accounts programmatically and policies auto-apply.

### 65. AWS Marketplace Facilitates Which Use-Cases (Select Two) - Repeat Full
**Question:** AWS Marketplace facilitates which of the following use-cases? (Select two)

- Buy Amazon EC2 Standard Reserved Instances (RI)
- AWS customer can buy software that has been bundled into customized Amazon Machine Image (AMIs) by the AWS Marketplace sellers
- Purchase compliance documents from third-party vendors
- Sell Software as a Service (SaaS) solutions to AWS customers
- Raise request for purchasing AWS Direct Connect connection

**Correct Answer:**
- AWS customer can buy software that has been bundled into customized Amazon Machine Image (AMIs) by the AWS Marketplace sellers
- Sell Software as a Service (SaaS) solutions to AWS customers

**Why Correct:** AWS Marketplace is digital catalog with thousands of software listings from ISVs to find/test/buy/deploy software that runs on AWS. Enables qualified partners to market and sell their software. Two ways: AMI (preferred, free or paid hourly/monthly/BYOL) and SaaS (if unable to build into AMI).
**Why Wrong:** Purchase compliance documents = AWS Artifact is central resource for compliance reports and agreements. Buy EC2 Standard RI = EC2 console at console.aws.amazon.com/ec2. Direct Connect connection = Direct Connect console.

### 66. Bonus - AWS Organizations Benefits (Select Two)
**Question:** AWS Organizations provides which benefits? (Select two)

- Volume discounts for Amazon EC2 and Amazon S3 aggregated across the member AWS accounts
- Deploy patches on Amazon EC2 instances across the member AWS accounts
- Check vulnerabilities on Amazon EC2 instances across the member AWS accounts
- Share the reserved Amazon EC2 instances amongst the member AWS accounts
- Provision Amazon EC2 Spot instances across the member AWS accounts

**Correct Answer:**
- Volume discounts for Amazon EC2 and Amazon S3 aggregated across the member AWS accounts
- Share the reserved Amazon EC2 instances amongst the member AWS accounts

**Why Correct:** Organizations helps centrally manage billing, control access/compliance/security, share resources such as reserved EC2 across accounts. Consolidated billing combined view + volume discounts aggregated. Key benefits via aws.amazon.com/organizations.
**Why Wrong:** Deploy patches = Systems Manager. Check vulnerabilities = Inspector. Provision Spot = EC2 feature.


# AWS Certified Cloud Practitioner (CLF-C02) - Practice Question Bank

> **Exam Code:** AWS CLF-C02  
> **Total Questions:** 65 Practice Questions  
> **Domains Covered:** Cloud Concepts, Security & Compliance, Cloud Technology & Services, Billing, Pricing & Support  
> **Format:** Formatted for high readability with complete rationale and distractor explanations.

---

## 📊 Exam Domain Distribution

| Domain | Scope & Focus Areas | Exam Weight |
| :--- | :--- | :---: |
| **Domain 1: Cloud Concepts** | Cloud value proposition, economics, Cloud Adoption Framework (CAF), Well-Architected Framework | ~24% |
| **Domain 2: Security & Compliance** | Shared Responsibility Model, IAM, security services (GuardDuty, Shield, WAF, KMS, Artifact), compliance | ~30% |
| **Domain 3: Cloud Technology & Services** | Core compute, storage, database, networking, serverless, and global infrastructure | ~34% |
| **Domain 4: Billing, Pricing & Support** | Pricing models, TCO, Cost Explorer, Budgets, Organizations, Support Plans | ~12% |

---

## 📖 Practice Questions & Explanations



### 1. Hardware Device for Data Encryption for Compliance
**Domain:** `Security & Compliance` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Due to regulatory and compliance reasons, an organization is supposed to use a hardware device for any data encryption operations in the cloud. Which AWS service can be used to meet this compliance requirement?

**Options:**
- **[A]** AWS Key Management Service (AWS KMS)
- **[B]** AWS CloudHSM
- **[C]** AWS Secrets Manager
- **[D]** AWS Certificate Manager

**Correct Answer:**
- **[B] AWS CloudHSM**

**Why Correct:**
CloudHSM provides single-tenant, dedicated FIPS 140-2 Level 3 validated Hardware Security Modules (HSMs) inside your VPC. You have full control over HSM, keys, policies. Designed for regulatory mandates requiring dedicated hardware, not multi-tenant. You can also create KMS Custom Key Store backed by CloudHSM cluster - best of both (KMS API + CloudHSM compliance).

**Why Others Are Incorrect:**
KMS = multi-tenant/shared (AWS manages hardware). Secrets Manager = stores secrets, not dedicated hardware encryption. ACM = SSL certificates.

---

### 2. AMI Region Constraint
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> An AWS user is trying to launch an Amazon Elastic Compute Cloud (Amazon EC2) instance in a given region. What is the region-specific constraint that the Amazon Machine Image (AMI) must meet so that it can be used for this EC2 instance?

**Options:**
- **[A]** You should use an Amazon Machine Image (AMI) from the same region, as it improves the performance of the Amazon EC2 instance
- **[B]** You can use an Amazon Machine Image (AMI) from a different region, but it degrades the performance of the Amazon EC2 instance
- **[C]** You must use an Amazon Machine Image (AMI) from the same region as that of the Amazon EC2 instance. The region of the Amazon Machine Image (AMI) has no bearing on the performance of the Amazon EC2 instance
- **[D]** An Amazon Machine Image (AMI) is a global entity, so the region is not applicable

**Correct Answer:**
- **[C] You must use an Amazon Machine Image (AMI) from the same region as that of the Amazon EC2 instance. The region of the Amazon Machine Image (AMI) has no bearing on the performance of the Amazon EC2 instance**

**Why Correct:**
AMIs are regional resources. Mandatory constraint, not performance. You cannot launch in us-east-1 using AMI only in us-west-2. Must copy AMI to destination region first. Performance myth is false.

**Why Others Are Incorrect:**
Options 1 and 2 say region affects performance - false. Option 4 says AMI is global - false, only S3, IAM are global.

---

### 3. Automate Operations Using Chef and Puppet
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> A developer would like to automate operations on his on-premises environment using Chef and Puppet. Which AWS service can help with this task?

**Options:**
- **[A]** AWS Elastic Beanstalk
- **[B]** AWS OpsWorks
- **[C]** AWS CloudFormation
- **[D]** AWS Systems Manager

**Correct Answer:**
- **[B] AWS OpsWorks**

**Why Correct:**
OpsWorks is configuration management service that automates operations using Chef and Puppet, supports AWS and On-Premises. Uses existing recipes/manifests directly.

**Why Others Are Incorrect:**
Systems Manager can automate on-prem but not natively Chef/Puppet. Beanstalk = PaaS. CloudFormation = infra templates.

---

### 4. Services with Data Encryption Automatically Enabled
**Domain:** `Security & Compliance` | **Type:** `Multiple Choice (Select Two)` | **Difficulty:** `Medium`

**Question:**
> Which of the following AWS services have data encryption automatically enabled? (Select two)

**Options:**
- **[A]** Amazon Elastic Block Store (Amazon EBS)
- **[B]** AWS Storage Gateway
- **[C]** Amazon Elastic File System (Amazon EFS)
- **[D]** Amazon S3 Glacier

**Correct Answer:**
- **[B] AWS Storage Gateway**
- **[D] Amazon S3 Glacier**

**Why Correct:**
All data written to Storage Gateway and S3 Glacier is automatically encrypted at rest AES-256, cannot disable.

**Why Others Are Incorrect:**
EBS and EFS require you to manually enable encryption at creation or account-level default.

---

### 5. Managed NoSQL for Active-Active East and West US
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> A company wants to improve resiliency of its flagship application so it wants to move from traditional database to managed AWS NoSQL database service to support active-active configuration in both East and West US regions. Active-active cross-region support is prime criteria. Which AWS database service is right fit?

**Options:**
- **[A]** Amazon DynamoDB with Global Tables
- **[B]** Amazon DocumentDB
- **[C]** Amazon RDS with Multi-AZ
- **[D]** Amazon ElastiCache Global Datastore

**Correct Answer:**
- **[A] Amazon DynamoDB with Global Tables**

**Why Correct:**
DynamoDB Global Tables = fully managed, active-active, multi-region replication, <1 sec replication, both regions can do reads AND writes (last-writer-wins). Created in us-east-1, add us-west-2 as replica.

**Why Others Are Incorrect:**
DocumentDB, Keyspaces don't provide turnkey active-active cross-region. RDS/Aurora Global is SQL and active-passive (1 primary writer). ElastiCache Global Datastore is cache, not primary NoSQL DB.

---

### 6. Centralize Server Logs for EC2 and On-Premises (Hybrid)
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> An IT company has hybrid cloud architecture and wants to centralize server logs for Amazon EC2 instances and on-premises servers. Which is MOST effective?

**Options:**
- **[A]** Use AWS Lambda to send log data from EC2 instance as well as on-premises servers to CloudWatch Logs
- **[B]** Use AWS CloudTrail for EC2 instance and Amazon CloudWatch Logs for on-premises servers
- **[C]** Use Amazon CloudWatch Logs for both EC2 instance and on-premises servers
- **[D]** Use Amazon CloudWatch Logs for EC2 instance and AWS CloudTrail for on-premises servers

**Correct Answer:**
- **[C] Use Amazon CloudWatch Logs for both EC2 instance and on-premises servers**

**Why Correct:**
Unified CloudWatch Agent installs on EC2 AND on-prem Windows/Linux, collects logs/metrics, sends to central CloudWatch Logs Log Group for search/alarms/retention. Stream to S3 via Firehose for long-term.

**Why Others Are Incorrect:**
Lambda = unnecessary complexity, Agent does it directly. CloudTrail = logs AWS API activity (who called what API), NOT OS logs like /var/log/messages, cannot be installed on-prem.

---

### 7. AWS Compute Optimizer Recommendations
**Domain:** `Billing, Pricing & Support` | **Type:** `Multiple Choice (Select Two)` | **Difficulty:** `Medium`

**Question:**
> AWS Compute Optimizer delivers recommendations for which AWS resources? (Select two)

**Options:**
- **[A]** Amazon EC2 instances, Amazon EFS
- **[B]** Amazon EC2 instances, Amazon EC2 Auto Scaling groups
- **[C]** Amazon EFS, AWS Lambda functions
- **[D]** Amazon EBS, AWS Lambda functions

**Correct Answer:**
- **[B] Amazon EC2 instances, Amazon EC2 Auto Scaling groups**
- **[D] Amazon EBS, AWS Lambda functions**

**Why Correct:**
Compute Optimizer supports: EC2 instances, Auto Scaling Groups, EBS volumes, Lambda functions, ECS Services on Fargate, Commercial Software Licenses. Does NOT support EFS.

**Why Others Are Incorrect:**
Any option containing EFS is invalid.

---

### 8. Discover Sensitive Data on S3 to Prevent Leaks
**Domain:** `Security & Compliance` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> A Silicon Valley based healthcare startup stores anonymized patient health data on Amazon S3. CTO wants to ensure any sensitive data on S3 is discovered and identified to prevent sensitive data leaks. Which AWS service?

**Options:**
- **[A]** Amazon GuardDuty
- **[B]** Amazon Macie
- **[C]** Amazon Inspector
- **[D]** Amazon Detective

**Correct Answer:**
- **[B] Amazon Macie**

**Why Correct:**
Macie = fully managed data security/privacy service that uses ML and pattern matching to automatically discover, classify, protect sensitive data in S3 (PII, PHI, financial). Inventories S3, continuous scans, dashboards + alerts via Security Hub/EventBridge. For healthcare: managed identifiers for patient names, health records.

**Why Others Are Incorrect:**
GuardDuty = threat detection. Inspector = vuln scanner for EC2/ECR. Detective = investigation.

---

### 9. Personalized View of Status of AWS Services Part of Your Architecture
**Domain:** `Billing, Pricing & Support` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Which service gives a personalized view of the status of the AWS services that are part of your cloud architecture so you can quickly assess impact on your business when AWS service(s) are experiencing issues?

**Options:**
- **[A]** Amazon CloudWatch
- **[B]** AWS Health - Service Health Dashboard
- **[C]** AWS Health - Your Account Health Dashboard (Personal Health Dashboard)
- **[D]** Amazon Inspector

**Correct Answer:**
- **[C] AWS Health - Your Account Health Dashboard (Personal Health Dashboard)**

**Why Correct:**
Two dashboards: Service Health Dashboard = PUBLIC/general status of ALL services for everyone. Your Account Health Dashboard = PERSONALIZED - only services part of YOUR architecture, how issue impacts YOUR resources, upcoming maintenance, alerts via EventBridge. Keyword: personalized, your account, your resources.

**Why Others Are Incorrect:**
CloudWatch = your metrics/logs, not AWS service health. Service Health Dashboard = not personalized. Inspector = EC2/ECR vuln scanning.

---

### 10. Advantages of AWS Cloud
**Domain:** `Cloud Concepts` | **Type:** `Multiple Choice (Select Two)` | **Difficulty:** `Medium`

**Question:**
> Which of the following are advantages of using AWS Cloud? (Select TWO)

**Options:**
- **[A]** Increase speed and agility
- **[B]** AWS is responsible for security in the cloud
- **[C]** Trade operational expense for capital expense
- **[D]** Limited scaling
- **[E]** Stop guessing about capacity

**Correct Answer:**
- **[A] Increase speed and agility**
- **[E] Stop guessing about capacity**

**Why Correct:**
6 Official Advantages: 1) Trade capital expense for variable expense (CapEx->OpEx), 2) Benefit from massive economies of scale, 3) Stop guessing about capacity, 4) Increase speed and agility, 5) Stop spending money running data centers, 6) Go global in minutes.

**Why Others Are Incorrect:**
"AWS is responsible for security IN the cloud" = reversed. AWS is OF the cloud, Customer is IN. "Trade operational for capital" = reversed. "Limited scaling" = opposite, it's elastic/unlimited.

---

### 11. Serverless Computing Services Offered by AWS
**Domain:** `Cloud Technology & Service` | **Type:** `Multiple Choice (Select Two)` | **Difficulty:** `Medium`

**Question:**
> Which of the following are the serverless computing services offered by AWS? (Select two)

**Options:**
- **[A]** AWS Lambda
- **[B]** AWS Elastic Beanstalk
- **[C]** AWS Fargate
- **[D]** Amazon EC2

**Correct Answer:**
- **[A] AWS Lambda**
- **[C] AWS Fargate**

**Why Correct:**
Serverless = you don't manage servers. Lambda = core serverless compute, upload code. Fargate = serverless compute for containers (ECS/EKS without EC2).

**Why Others Are Incorrect:**
Beanstalk = PaaS but provisions EC2 underneath, not serverless. EC2 = IaaS, you manage server.

---

### 12. Identify Under-Utilized EC2 Off-the-Shelf Without Manual Config
**Domain:** `Billing, Pricing & Support` | **Type:** `Multiple Choice (Select Two)` | **Difficulty:** `Medium`

**Question:**
> An IT company is on cost-optimization spree and wants to identify all EC2 instances that are under-utilized. Which AWS services can be used off-the-shelf without manual configurations? (Select two)

**Options:**
- **[A]** Amazon CloudWatch
- **[B]** AWS Cost Explorer
- **[C]** AWS Budgets
- **[D]** AWS Cost & Usage Report (CUR)
- **[E]** AWS Trusted Advisor

**Correct Answer:**
- **[B] AWS Cost Explorer**
- **[E] AWS Trusted Advisor**

**Why Correct:**
Trusted Advisor has built-in check "Low Utilization EC2 Instances" - auto finds idle/under-utilized and tells to stop/downsize, zero config. Cost Explorer has Rightsizing Recommendations powered by Compute Optimizer, auto identifies under-utilized and recommends smaller types. Compute Optimizer is best for this if present.

**Why Others Are Incorrect:**
CloudWatch DOES show CPU but requires manual alarms/dashboards/manual analysis per instance - not off-the-shelf.

---

### 13. Debug Performance Issues for Serverless Microservices Application
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> The DevOps team at an e-commerce company is trying to debug performance issues for its serverless application built using microservices architecture. Which AWS service would you recommend?

**Options:**
- **[A]** AWS X-Ray
- **[B]** Amazon Pinpoint
- **[C]** AWS CloudFormation
- **[D]** AWS Trusted Advisor

**Correct Answer:**
- **[A] AWS X-Ray**

**Why Correct:**
X-Ray = Distributed tracing service. Traces requests as they travel through microservices, Lambda, API Gateway, DynamoDB, etc. Shows service map, latency bottlenecks, errors, where perf degrades. Keyword: serverless + microservices + debug performance.

**Why Others Are Incorrect:**
Pinpoint = marketing campaigns/push notifications. CloudFormation = infra as code. Trusted Advisor = cost/security/perf recommendations, not live debugging.

---

### 14. Analytics Application with Speech-Based Interface
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> A unicorn startup building analytics application with support for speech-based interface. App will accept speech-based input and then convey results via speech. Which solution?

**Options:**
- **[A]** Use Amazon Polly to convert speech to text for downstream analysis. Then use Amazon Transcribe to convey text results via speech
- **[B]** Use Amazon Transcribe to convert speech to text for downstream analysis. Then use Amazon Polly to convey text results via speech
- **[C]** Use Amazon Polly to convert speech to text for downstream analysis. Then use Amazon Translate to convey text results via speech
- **[D]** Use Amazon Translate to convert speech to text for downstream analysis. Then use Amazon Polly to convey text results via speech

**Correct Answer:**
- **[B] Use Amazon Transcribe to convert speech to text for downstream analysis. Then use Amazon Polly to convey text results via speech**

**Why Correct:**
Transcribe = Speech to Text (STT) - audio to text. Polly = Text to Speech (TTS) - text to audio. Translate = text to text translation only. Flow: User Speech -> Transcribe [Speech->Text] -> Analytics -> Polly [Text->Speech] -> User Speech.

**Why Others Are Incorrect:**
The remaining options describe services or configurations that do not address the core requirements outlined in the question.

---

### 15. MFA Device That You Can Plug Into USB Port
**Domain:** `Security & Compliance` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Which AWS authentication mechanisms supports an AWS Multi-Factor Authentication (AWS MFA) device that you can plug into a USB port on your computer?

**Options:**
- **[A]** Hardware Multi-Factor Authentication (AWS MFA) device
- **[B]** U2F security key
- **[C]** Virtual Multi-Factor Authentication (AWS MFA) device
- **[D]** SMS text message-based Multi-Factor Authentication (AWS MFA)

**Correct Answer:**
- **[B] U2F security key**

**Why Correct:**
U2F security key = physical device like YubiKey that plugs into USB and tap to authenticate. Virtual MFA = app on smartphone (Google Authenticator). Hardware MFA = small key-fob/token with LCD screen showing 6-digit code, battery powered, press button, NOT USB. SMS MFA = AWS does NOT support SMS as MFA for IAM (deprecated).

**Why Others Are Incorrect:**
The remaining options describe services or configurations that do not address the core requirements outlined in the question.

---

### 16. MFA Device With No Physical Device - Easy for Travel
**Domain:** `Security & Compliance` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Which AWS authentication mechanism supports MFA without needing a physical device, easy for travel?

**Options:**
- **[A]** Hardware MFA device
- **[B]** U2F security key
- **[C]** Virtual Multi-Factor Authentication (MFA) device
- **[D]** SMS MFA

**Correct Answer:**
- **[C] Virtual Multi-Factor Authentication (MFA) device**

**Why Correct:**
Virtual MFA = software based app on existing smartphone (Google Authenticator, Authy) generates TOTP code. No extra physical device needed. Perfect for travel.

**Why Others Are Incorrect:**
Hardware MFA and U2F = physical devices you must carry.

---

### 17. Cost Optimization - Purchase RIs and Auto Scaling
**Domain:** `Billing, Pricing & Support` | **Type:** `Multiple Choice (Select Two)` | **Difficulty:** `Medium`

**Question:**
> A company wants to optimize EC2 costs. Which two actions help?

**Options:**
- **[A]** Purchase Amazon EC2 Reserved Instances (RIs)
- **[B]** Set up Auto Scaling groups to align number of instances with demand
- **[C]** Build its own servers
- **[D]** Vertically scale EC2 instances
- **[E]** Opt for higher AWS Support plan

**Correct Answer:**
- **[A] Purchase Amazon EC2 Reserved Instances (RIs)**
- **[B] Set up Auto Scaling groups to align number of instances with demand**

**Why Correct:**
RIs = up to 72% discount for steady-state predictable usage. Auto Scaling = run only number you need based on demand, scale in when low, out when high, no wasted money.

**Why Others Are Incorrect:**
Build own servers = CapEx, maintenance, lose elasticity. Vertically scale = just bigger, increases cost, not optimization (rightsizing down would help but "vertically scale" alone not). Higher Support plan = extra cost, doesn't reduce EC2 bill.

---

### 18. Recommendation Engine Data - Key-Value Millisecond Latency
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> For a recommendation engine data store requiring key-value lookups like userId -> list of recommended products, millisecond latency, least operational overhead, any scale, which database?

**Options:**
- **[A]** Amazon DynamoDB
- **[B]** Amazon RDS
- **[C]** Amazon S3
- **[D]** Amazon Neptune

**Correct Answer:**
- **[A] Amazon DynamoDB**

**Why Correct:**
DynamoDB = fully managed, serverless NoSQL, no servers to provision/patch/manage, auto scales to any throughput, single-digit millisecond latency, perfect for recommendation cache.

**Why Others Are Incorrect:**
RDS = relational, manage scaling/patching, higher overhead, not ideal for simple key-value. S3 = object storage, not low-latency DB. Neptune = graph DB for highly connected data like social graphs/fraud detection.

---

### 19. CAF Platform Perspective Stakeholders
**Domain:** `Cloud Concepts` | **Type:** `Multiple Choice (Select Two)` | **Difficulty:** `Medium`

**Question:**
> Which option is a common stakeholder role for the AWS Cloud Adoption Framework (AWS CAF) platform perspective? (Select two)

**Options:**
- **[A]** Engineer
- **[B]** Chief Data Officer (CDO)
- **[C]** Chief Product Officer (CPO)
- **[D]** Chief Information Officer (CIO)
- **[E]** Chief Technology Officer (CTO)

**Correct Answer:**
- **[A] Engineer**
- **[E] Chief Technology Officer (CTO)**

**Why Correct:**
CAF has 6 Perspectives: Business, People, Governance, Platform, Security, Operations. Platform = accelerating delivery of cloud workloads via enterprise-grade scalable hybrid cloud. Common stakeholders: CTO, technology leaders, architects, engineers, CIO.

**Why Others Are Incorrect:**
CDO = Governance Perspective (data governance). CPO = Business Perspective.

---

### 20. Container Service - Serverless for Containers
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Which AWS service is a serverless container service?

**Options:**
- **[A]** AWS Elastic Beanstalk
- **[B]** Amazon SNS
- **[C]** AWS Fargate
- **[D]** Amazon SageMaker

**Correct Answer:**
- **[C] AWS Fargate**

**Why Correct:**
Fargate = serverless compute engine for containers, run ECS and EKS containers without managing EC2 servers.

**Why Others Are Incorrect:**
Beanstalk = PaaS for web apps, not dedicated container service. SNS = pub/sub messaging. SageMaker = ML service.

---

### 21. Best Practices for AWS Organizations
**Domain:** `Billing, Pricing & Support` | **Type:** `Multiple Choice (Select Two)` | **Difficulty:** `Medium`

**Question:**
> Which are best practices when using AWS Organizations? (Select TWO)

**Options:**
- **[A]** Never use tags for billing
- **[B]** Create AWS accounts per department
- **[C]** Do not use AWS Organizations to automate AWS account creation
- **[D]** Disable AWS CloudTrail on several accounts
- **[E]** Restrict account privileges using Service Control Policies (SCP)

**Correct Answer:**
- **[B] Create AWS accounts per department**
- **[E] Restrict account privileges using Service Control Policies (SCP)**

**Why Correct:**
Create accounts per department/workload/team/environment for isolation, billing, blast-radius. Use SCPs as permission guardrails.

**Why Others Are Incorrect:**
Never use tags = SHOULD use tags (Cost Allocation Tags + Tag Policies). Do not automate = SHOULD automate via CreateAccount API / Control Tower. Disable CloudTrail = SHOULD enable in ALL accounts, ideally Organization Trail.

---

### 22. Hybrid Deployment Definition
**Domain:** `Cloud Concepts` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> An organization has on-premises data center and AWS Cloud connected and working together. Which deployment model?

**Options:**
- **[A]** Private deployment
- **[B]** Cloud deployment
- **[C]** Hybrid deployment
- **[D]** Mixed deployment

**Correct Answer:**
- **[C] Hybrid deployment**

**Why Correct:**
Hybrid = Combination of On-prem + Cloud (AWS). Private = on-prem private cloud only. Cloud = everything on AWS only. Mixed = not official AWS term.

**Why Others Are Incorrect:**
The remaining options describe services or configurations that do not address the core requirements outlined in the question.

---

### 23. Cheapest Long-Term Archival S3 Storage
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Which S3 storage class is cheapest, lowest-cost for long-term archival where you rarely need data, highest first-byte latency?

**Options:**
- **[A]** S3 Standard
- **[B]** S3 Intelligent-Tiering
- **[C]** S3 Glacier Flexible Retrieval
- **[D]** S3 Glacier Deep Archive

**Correct Answer:**
- **[D] S3 Glacier Deep Archive**

**Why Correct:**
Deep Archive = cheapest, designed for long-term archival 7-10 years+ for compliance. Durability 11 9's. Retrieval: Standard within 12 hours, Bulk within 48 hours (HIGHEST latency). Flexible Retrieval = minutes to hours (Expedited 1-5 mins, Standard 3-5 hours, Bulk 5-12 hours). Standard/Intelligent-Tiering = milliseconds.

**Why Others Are Incorrect:**
The remaining options describe services or configurations that do not address the core requirements outlined in the question.

---

### 24. Shared File System for Multiple EC2 Instances with Append Capability
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Application accessed by hundreds of EC2 instances simultaneously and needs to append data to existing files. Which storage?

**Options:**
- **[A]** Amazon Elastic File System (Amazon EFS)
- **[B]** Amazon S3
- **[C]** Amazon EBS
- **[D]** Instance Store

**Correct Answer:**
- **[A] Amazon Elastic File System (Amazon EFS)**

**Why Correct:**
EFS = fully managed NFS file system, mount on hundreds/thousands of EC2 in multiple AZs simultaneously, supports file appends/locks. Perfect for batch analytics.

**Why Others Are Incorrect:**
S3 = object storage, immutable, cannot append, must re-write whole object. EBS = block storage attachable to ONE EC2 at time in one AZ (Multi-Attach limited to 16 io1/io2 same AZ). Instance Store = ephemeral, local to single EC2 host, lost on stop/terminate.

---

### 25. Schemaless Database Requirement
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Application requires schemaless database. Which service?

**Options:**
- **[A]** Amazon DynamoDB
- **[B]** Amazon Aurora
- **[C]** Amazon RDS
- **[D]** Amazon Redshift

**Correct Answer:**
- **[A] Amazon DynamoDB**

**Why Correct:**
DynamoDB = NoSQL schemaless, no pre-defined schema, each item can have different attributes.

**Why Others Are Incorrect:**
Aurora/RDS = relational fixed schema. Redshift = data warehouse, requires defined schema for structured data.

---

### 26. Centrally Manage Access Across Multiple AWS Accounts (IAM Identity Center)
**Domain:** `Security & Compliance` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Company has multiple AWS accounts in AWS Organizations and wants to centrally manage access with single place to create users and SSO. Which service?

**Options:**
- **[A]** AWS IAM Identity Center (previously AWS Single Sign-On / AWS SSO)
- **[B]** AWS IAM
- **[C]** AWS Cognito
- **[D]** AWS CLI

**Correct Answer:**
- **[A] AWS IAM Identity Center (previously AWS Single Sign-On / AWS SSO)**

**Why Correct:**
IAM Identity Center built exactly for this - manage access centrally across multiple accounts in Organizations, single place to create users and provide Single Sign-On.

**Why Others Are Incorrect:**
IAM = works per-account, managing across 10-100 accounts complex (need roles/trust). Cognito = auth for your own web/mobile app users, not AWS accounts. CLI = command-line tool.

---

### 27. Professional Services Firm to Help Migrate to AWS
**Domain:** `Billing, Pricing & Support` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Corporation needs expert hands-on advice to migrate to AWS, architect, build and manage workloads. Which help?

**Options:**
- **[A]** APN Consulting Partner
- **[B]** APN Technology Partner
- **[C]** Concierge Support Team
- **[D]** AWS Trusted Advisor

**Correct Answer:**
- **[A] APN Consulting Partner**

**Why Correct:**
Consulting Partners = professional services firms like Accenture, Deloitte certified by AWS to help customers migrate, architect, build, manage.

**Why Others Are Incorrect:**
Technology Partner = companies providing software/hardware products that integrate with AWS (Snowflake, Datadog). Concierge = helps with billing/account/Enterprise Support only. Trusted Advisor = automated tool for cost/security/performance checks, not people.

---

### 28. Identify Unattached and Underutilized EBS Volumes
**Domain:** `Billing, Pricing & Support` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Which AWS service can identify unattached / underutilized EBS volumes for cost optimization?

**Options:**
- **[A]** AWS Trusted Advisor
- **[B]** Amazon Inspector
- **[C]** AWS Config
- **[D]** Amazon CloudWatch

**Correct Answer:**
- **[A] AWS Trusted Advisor**

**Why Correct:**
Trusted Advisor scans environment and flags cost optimization checks like Unattached Elastic IP, Underutilized EBS Volumes, Idle RDS, Idle Load Balancers.

**Why Others Are Incorrect:**
Inspector = security vuln scanner for EC2/ECR. Config = records/audits config changes for compliance. CloudWatch = metrics/alarms, could look at EBS metrics but won't proactively identify unattached/underutilized like Trusted Advisor.

---

### 29. Forecast Future AWS Costs and Usage
**Domain:** `Billing, Pricing & Support` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Which AWS service can forecast future AWS costs and usage based on past usage?

**Options:**
- **[A]** AWS Cost Explorer
- **[B]** AWS Budgets
- **[C]** AWS Pricing Calculator
- **[D]** AWS Cost & Usage Report (CUR)

**Correct Answer:**
- **[A] AWS Cost Explorer**

**Why Correct:**
Cost Explorer has built-in forecasting engine, looks at past usage and forecasts costs/usage up to 12 months ahead. Budgets also can forecast if you'll exceed budget and alert. Both valid for forecasting.

AWS Cost Explorer ✅	Analyze historical costs/usage and forecast future costs
AWS Budgets	Set budgets and receive alerts when costs/usage exceed thresholds
AWS Pricing Calculator	Estimate costs before deploying AWS resources
AWS Cost & Usage Report (CUR)	Provides detailed billing/usage data for analysis

**Why Others Are Incorrect:**
Pricing Calculator = estimate costs before deploy, not forecast actual running account. CUR = raw detailed CSV dump of all costs/usage, does not forecast, you analyze yourself in Athena/QuickSight.

---

### 30. Shared Responsibility Model Correct Statements
**Domain:** `Security & Compliance` | **Type:** `Multiple Choice (Select Two)` | **Difficulty:** `Medium`

**Question:**
> Which are correct statements regarding AWS Shared Responsibility Model? (Select two)

**Options:**
- **[A]** Configuration management of customer resources like Security Groups, IAM policies is AWS responsibility
- **[B]** Awareness & Training of customer employees is AWS responsibility
- **[C]** For IaaS like EC2, customer is responsible for maintaining guest OS
- **[D]** For abstracted services like S3, AWS operates infrastructure layer, OS, and platforms
- **[E]** AWS is responsible for Security 'of' the Cloud

**Correct Answer:**
- **[D] For abstracted services like S3, AWS operates infrastructure layer, OS, and platforms**
- **[E] AWS is responsible for Security 'of' the Cloud**

**Why Correct:**
Shared Responsibility = AWS OF Cloud (physical datacenters, hardware, networking, hypervisor), Customer IN Cloud. For abstracted/managed services like S3, DynamoDB, SQS - AWS manages infra to OS to platform, customer only data/access policies/encryption.

**Why Others Are Incorrect:**
For IaaS like EC2, customer IS responsible for guest OS patching/updates/antivirus (AWS only host/hypervisor) - but options 4 and 5 are more textbook. Awareness & Training is customer's responsibility.

---

### 31. Block-Level Storage Types in AWS
**Domain:** `Cloud Technology & Service` | **Type:** `Multiple Choice (Select Two)` | **Difficulty:** `Medium`

**Question:**
> Which are block-level storage types? (Select two)

**Options:**
- **[A]** Amazon EBS
- **[B]** Instance Store
- **[C]** Amazon S3
- **[D]** Amazon EFS
- **[E]** Amazon ECS

**Correct Answer:**
- **[A] Amazon EBS**
- **[B] Instance Store**

**Why Correct:**
Block storage: EBS = persistent block for EC2. Instance Store = ephemeral block physically attached to EC2 host. Object: S3. File: EFS NFS. ECS = container orchestration, not storage.

**Why Others Are Incorrect:**
The remaining options describe services or configurations that do not address the core requirements outlined in the question.

---

### 32. Historic Data Storage for 10 Years (Compliance & Durability)
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Company needs to store historic data for 10 years, durable, cost-effective, compliance. Which S3 storage?

**Options:**
- **[A]** Amazon S3 Glacier Deep Archive
- **[B]** Amazon S3 Glacier Flexible Retrieval
- **[C]** AWS Storage Gateway
- **[D]** Amazon EFS

**Correct Answer:**
- **[A] Amazon S3 Glacier Deep Archive**

**Why Correct:**
Deep Archive = cheapest, long-term archival 7-10 years+ for compliance, 11 9's durability, retrieval 12 hours.

**Why Others Are Incorrect:**
Flexible Retrieval = more expensive, for data accessed 1-2 times per quarter. Storage Gateway = hybrid cloud connecting on-prem to AWS storage, not archival class. EFS = expensive file system for active workloads.

---

### 33. Privately Connect Two VPCs Across Business Units
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Two business units have separate VPCs and want to share data privately without internet, low latency. Most optimal?

**Options:**
- **[A]** VPC peering connection
- **[B]** AWS Site-to-Site VPN
- **[C]** VPC Endpoint
- **[D]** AWS Direct Connect

**Correct Answer:**
- **[A] VPC peering connection**

**Why Correct:**
VPC peering = most optimal way to privately connect two VPCs. Traffic stays on AWS private backbone, no internet, no encryption overhead, low latency.

**Why Others Are Incorrect:**
Site-to-Site VPN = on-prem to AWS VPC, not VPC to VPC. VPC Endpoint = private access to AWS services like S3/DynamoDB from inside VPC. Direct Connect = dedicated physical line from on-prem to AWS.

---

### 34. Benefits of AWS Elastic Load Balancing (ELB)
**Domain:** `Cloud Technology & Service` | **Type:** `Multiple Choice (Select Two)` | **Difficulty:** `Medium`

**Question:**
> Which are benefits of AWS Elastic Load Balancing? (Select two)

**Options:**
- **[A]** Fault tolerance
- **[B]** High availability
- **[C]** Less costly
- **[D]** Storage
- **[E]** Agility

**Correct Answer:**
- **[A] Fault tolerance**
- **[B] High availability**

**Why Correct:**
ELB distributes traffic across multiple healthy targets in multiple AZs. High Availability: if one AZ/instance down, routes to healthy in other AZs. Fault tolerance: health checks, only sends to healthy instances, app tolerates failures.

**Why Others Are Incorrect:**
Storage = S3/EBS benefit. Less costly/Agility = general Cloud benefits, not specific ELB.

---

### 35. Prohibited Uses of AWS Services Policy
**Domain:** `Security & Compliance` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Which policy describes prohibited uses of AWS services - illegal activities, abuse, spamming, hosting malicious content?

**Options:**
- **[A]** AWS Acceptable Use Policy
- **[B]** Applicable Use Policy
- **[C]** Trusted Advisor
- **[D]** Fair Use Policy

**Correct Answer:**
- **[A] AWS Acceptable Use Policy**

**Why Correct:**
The AWS Acceptable Use Policy describes prohibited uses of the web services offered by Amazon Web Services and its affiliates, including illegal activities, network abuse, spamming, and hosting malicious or harmful content.

**Why Others Are Incorrect:**
Applicable Use Policy and Fair Use Policy are fabricated terms in this context. AWS Trusted Advisor is an automated optimization tool, not a compliance or acceptable use policy.

---

### 36. Serverless Scheduled Task Execution
**Domain:** `Cloud Technology & Service` | **Type:** `Multiple Choice (Select Two)` | **Difficulty:** `Medium`

**Question:**
> Company needs serverless solution for backup task scheduled every Monday 2 AM that runs for 5 minutes. Which two services? (Select two)

**Options:**
- **[A]** AWS Lambda
- **[B]** Amazon EventBridge
- **[C]** Amazon EC2
- **[D]** AWS Step Function
- **[E]** AWS Systems Manager

**Correct Answer:**
- **[A] AWS Lambda**
- **[B] Amazon EventBridge**

**Why Correct:**
EventBridge = serverless scheduler, create cron rule 0 2 ? * MON * to trigger every Monday 2 AM. Lambda = serverless compute, perfect for 5 min backup (max timeout 15 min). EventBridge invokes Lambda on schedule.

**Why Others Are Incorrect:**
EC2 = not serverless. Step Function = serverless orchestration for complex workflows with multiple steps, overkill for simple 5-min task. Systems Manager = managing EC2 fleets/patching.

---

### 37. Simplest Way to Break Down AWS Bill by Department
**Domain:** `Billing, Pricing & Support` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Simplest way to break down AWS bill by department?

**Options:**
- **[A]** Create tags for each department and activate as Cost Allocation Tags
- **[B]** Create different accounts for different departments using AWS Organizations
- **[C]** Use AWS Budgets
- **[D]** Use AWS Cost Explorer

**Correct Answer:**
- **[A] Create tags for each department and activate as Cost Allocation Tags**

**Why Correct:**
Cost Allocation Tags allow you to assign metadata (key-value pairs such as Department: Marketing or CostCenter: 101) to AWS resources. Once activated in Billing and Cost Management, AWS uses these tags to organize and break down costs on your monthly cost allocation report.

**Why Others Are Incorrect:**
Creating separate AWS accounts per department is a valid organizational structure but requires much higher administrative overhead compared to simply using Cost Allocation Tags. AWS Budgets sets spending thresholds and alerts, and Cost Explorer visualizes historical spend.

---

### 38. Route 53 Weighted Routing for Blue/Green Testing
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Which Route 53 routing lets you route traffic to multiple resources in proportions you specify - e.g., 80% to one server and 20% to another. Useful for blue/green, A/B testing.

**Options:**
- **[A]** Weighted routing
- **[B]** Simple routing
- **[C]** Latency-based routing
- **[D]** Failover routing

**Correct Answer:**
- **[A] Weighted routing**

**Why Correct:**
Weighted = route in proportions specified. Simple = single resource only. Latency-based = lowest latency to user. Failover = Active/Passive for DR.

**Why Others Are Incorrect:**
The remaining options describe services or configurations that do not address the core requirements outlined in the question.

---

### 39. Well-Architected Framework - Operational Excellence Pillar
**Domain:** `Cloud Concepts` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Which Well-Architected Framework pillar recommends automating operations and maintaining Infrastructure as Code (IaC) using services like CloudFormation?

**Options:**
- **[A]** Operational Excellence
- **[B]** Security
- **[C]** Reliability
- **[D]** Performance Efficiency

**Correct Answer:**
- **[A] Operational Excellence**

**Why Correct:**
Operational Excellence focuses on perform operations as code, make frequent small reversible changes, automate manual tasks.

**Why Others Are Incorrect:**
The remaining options describe services or configurations that do not address the core requirements outlined in the question.

---

### 40. Compare Cost of Running On-Premises vs AWS Cloud
**Domain:** `Billing, Pricing & Support` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Which tool is specifically designed to compare cost of running infrastructure on-premises vs on AWS Cloud?

**Options:**
- **[A]** AWS Pricing Calculator (previously Total Cost of Ownership - TCO Calculator / Migration Evaluator)
- **[B]** AWS Cost Explorer
- **[C]** AWS Trusted Advisor
- **[D]** AWS Budgets

**Correct Answer:**
- **[A] AWS Pricing Calculator (previously Total Cost of Ownership - TCO Calculator / Migration Evaluator)**

**Why Correct:**
Pricing/TCO Calculator designed to compare on-prem vs AWS. Input on-prem setup, estimates AWS cost.

**Why Others Are Incorrect:**
Cost Explorer = analyze existing AWS spend. Trusted Advisor = cost optimization/security/perf checks in existing account. Budgets = set alerts when cost exceeds threshold.

---

### 41. AWS Health Dashboard - Service Health RSS Feed
**Domain:** `Billing, Pricing & Support` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Which service provides RSS feed to be notified of AWS service interruptions/outages?

**Options:**
- **[A]** AWS Health Dashboard - Service Health
- **[B]** AWS Health Dashboard - Your Account Health
- **[C]** Amazon SNS
- **[D]** AWS Lambda

**Correct Answer:**
- **[A] AWS Health Dashboard - Service Health**

**Why Correct:**
Service Health = public dashboard showing status of all AWS services in all regions, provides RSS feed for service interruptions.

**Why Others Are Incorrect:**
Your Account Health = personalized to your account, shows events affecting your specific resources, does NOT provide RSS for all services. SNS/Lambda = not related.

---

### 42. Low-Latency Global User Delivery (AWS Edge Locations)
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> A gaming company is looking for a technology/service that can deliver consistent low-latency gameplay to ensure a great user experience for end-users in various locations globally. Which AWS infrastructure component should they use?

**Options:**
- **[A]** AWS Wavelength
- **[B]** AWS Direct Connect
- **[C]** AWS Edge Locations
- **[D]** AWS Local Zones

**Correct Answer:**
- **[C] AWS Edge Locations**

**Why Correct:**
AWS Edge Locations are geographically dispersed data centers worldwide that deliver cached content and low-latency network routing through services like Amazon CloudFront and AWS Global Accelerator, providing consistent low-latency experiences to users across various global locations.

**Why Others Are Incorrect:**
AWS Wavelength embeds AWS compute and storage services within 5G telecommunication networks for ultra-low latency mobile edge applications. AWS Direct Connect provides a dedicated private physical network connection between on-premises and AWS. AWS Local Zones place compute and storage closer to specific metropolitan centers for single-digit millisecond latency rather than broad global distribution.

---

### 43. Automate Code Deployments to EC2 and On-Premises
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Which service automates code deployments to both Amazon EC2 and on-premises servers?

**Options:**
- **[A]** AWS CodeDeploy
- **[B]** AWS CodeCommit
- **[C]** AWS CloudFormation
- **[D]** AWS CodePipeline

**Correct Answer:**
- **[A] AWS CodeDeploy**

**Why Correct:**
CodeDeploy automates code deployments to EC2 and on-prem.

**Why Others Are Incorrect:**
CodeCommit = Git-based source code repo. CloudFormation = infra as code. CodePipeline = orchestrates CI/CD pipeline - uses CodeDeploy for deployment stage.

---

### 44. Amazon RDS Multi-AZ Availability Enhancement
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> What does Amazon RDS Multi-AZ enhance?

**Options:**
- **[A]** Enhances database availability
- **[B]** Improves performance for read-heavy workloads
- **[C]** Reduces costs
- **[D]** Protects from regional failure

**Correct Answer:**
- **[A] Enhances database availability**

**Why Correct:**
Multi-AZ with 1 standby maintains synchronous standby copy in different AZ. If primary fails, auto failover to standby - for HA/Fault Tolerance. Standby cannot serve reads.

**Why Others Are Incorrect:**
Improves read perf = Read Replicas. Reduces costs = costs more (2 instances). Regional failure = Multi-AZ within single Region, need Cross-Region/Multi-Region for regional DR.

---

### 45. Massive Economies of Scale Cloud Advantage
**Domain:** `Cloud Concepts` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Because AWS aggregates usage from hundreds of thousands of customers, it achieves huge economies of scale, which allows it to lower pay-as-you-go prices. Which advantage?

**Options:**
- **[A]** Massive economies of scale
- **[B]** Increase speed and agility
- **[C]** High availability
- **[D]** Elasticity

**Correct Answer:**
- **[A] Massive economies of scale**

**Why Correct:**
"Benefit from massive economies of scale" is one of the 6 core advantages of cloud computing defined by AWS. By aggregating usage from hundreds of thousands of customers in the cloud, AWS achieves higher economies of scale, translating into lower pay-as-you-go prices for customers.

**Why Others Are Incorrect:**
"Increase speed and agility" refers to rapid resource provisioning in minutes. "High availability" and "Elasticity" refer to architectural resilience and scaling compute dynamically with demand.

---

### 46. Automatically Add and Remove EC2 Instances Based on Traffic Demand
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Which service automatically adds or removes EC2 instances to ensure you have right capacity to handle current traffic demand?

**Options:**
- **[A]** Amazon EC2 Auto Scaling
- **[B]** Multi-AZ deployment
- **[C]** Application Load Balancer
- **[D]** Network Load Balancer

**Correct Answer:**
- **[A] Amazon EC2 Auto Scaling**

**Why Correct:**
Auto Scaling adds/removes EC2 to match demand.

**Why Others Are Incorrect:**
Multi-AZ = HA. ALB/NLB = distribute traffic, not scale number of instances.

---

### 47. Secure Shell Access to Private EC2 Instances via Session Manager
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Which service lets you securely shell (SSH) into private EC2 instances through browser or CLI without opening inbound port 22, public IP, bastion host/key pairs?

**Options:**
- **[A]** AWS Systems Manager Session Manager
- **[B]** EC2 Instance Connect
- **[C]** Route 53
- **[D]** Amazon Inspector

**Correct Answer:**
- **[A] AWS Systems Manager Session Manager**

**Why Correct:**
Session Manager works via SSM Agent outbound connection, no port 22, no public IP, no bastion/key pairs.

**Why Others Are Incorrect:**
EC2 Instance Connect = still requires port 22 open and public IP/internet. Route 53 = DNS. Inspector = vuln assessment.

---

### 48. Deploy Infrastructure as Code Templates Across Accounts and Regions
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> A Cloud Practitioner would like to deploy identical resources across all AWS regions and accounts using templates while estimating costs. Which AWS service can assist with this task?

**Options:**
- **[A]** AWS Directory Service for Microsoft Active Directory
- **[B]** Amazon Lightsail
- **[C]** AWS CloudFormation
- **[D]** AWS CodeDeploy

**Correct Answer:**
- **[C] AWS CloudFormation**

**Why Correct:**
CloudFormation uses templates (JSON/YAML) and CloudFormation StackSets to deploy identical resources across all regions and accounts in one operation. It also has built-in cost estimation (via Pricing Calculator integration) for templates.

**Why Others Are Incorrect:**
Directory Service = Managed AD. Lightsail = simple VPS bundle. CodeDeploy = deploys application code to EC2/on-prem, not infrastructure templates.

---

### 49. Docker Container Deployment with Underlying Server Access
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> A startup runs proprietary application on docker containers. As a Cloud Practitioner, which AWS service would you recommend so that startup can run containers and still have access to underlying servers?

**Options:**
- **[A]** Amazon Elastic Container Service (Amazon ECS) - EC2 Launch Type
- **[B]** AWS Fargate
- **[C]** Amazon Elastic Container Registry (ECR)
- **[D]** AWS Lambda

**Correct Answer:**
- **[A] Amazon Elastic Container Service (Amazon ECS) - EC2 Launch Type**

**Why Correct:**
ECS with EC2 launch type lets you run Docker containers while you still manage and have SSH access to the underlying EC2 instances.

**Why Others Are Incorrect:**
Fargate = serverless containers, no server access. ECR = only Docker registry to store images. Lambda = serverless functions.

---

### 50. Lowest Cost Long-Term EC2 Pricing Option with No Interruption
**Domain:** `Billing, Pricing & Support` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> A startup wants to provision an EC2 instance for the lowest possible cost for a long-term duration but needs to make sure that the instance would never be interrupted. Which option?

**Options:**
- **[A]** EC2 Spot Instance
- **[B]** EC2 On-Demand Instance
- **[C]** EC2 Reserved Instance (RI) / Savings Plan
- **[D]** EC2 Dedicated Host

**Correct Answer:**
- **[C] EC2 Reserved Instance (RI) / Savings Plan**

**Why Correct:**
Reserved Instances give up to 72% discount vs On-Demand for long-term and are never interrupted. Savings Plans are new model of same.

**Why Others Are Incorrect:**
Spot = cheapest but CAN be interrupted with 2-min notice. On-Demand = no interruption but expensive long-term. Dedicated Host = most expensive for compliance/licensing.

---

### 51. Provision Same AWS Infrastructure Across Multiple Accounts and Regions
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Which AWS service will you use to provision the same AWS infrastructure across multiple AWS accounts and regions?

**Options:**
- **[A]** AWS OpsWorks
- **[B]** AWS Systems Manager
- **[C]** AWS CodeDeploy
- **[D]** AWS CloudFormation

**Correct Answer:**
- **[D] AWS CloudFormation**

**Why Correct:**
CloudFormation StackSets is designed to provision same stack from one template across multiple accounts and regions.

**Why Others Are Incorrect:**
OpsWorks = Chef/Puppet config management. Systems Manager = manage EC2 fleets. CodeDeploy = deploy application code.

---

### 52. Distinguishing Amazon Inspector Features
**Domain:** `Security & Compliance` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> Which of the following options is NOT a feature of Amazon Inspector?

**Options:**
- **[A]** Track configuration changes
- **[B]** Automate security assessments
- **[C]** Inspect running OS against known vulnerabilities
- **[D]** Analyze against unintended network accessibility

**Correct Answer:**
- **[A] Track configuration changes**

**Why Correct:**
Inspector DOES: Automate security assessments, Inspect running OS for known vulnerabilities, Analyze against unintended network accessibility. Tracking configuration changes is AWS Config.

**Why Others Are Incorrect:**
The remaining options describe services or configurations that do not address the core requirements outlined in the question.

---

### 53. Account Activity Governance, Compliance, and Auditing (CloudTrail)
**Domain:** `Security & Compliance` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> A financial services company wants to ensure that its AWS account activity meets governance, compliance and auditing norms. Which service would you recommend?

**Options:**
- **[A]** AWS Trusted Advisor
- **[B]** AWS Config
- **[C]** AWS CloudTrail
- **[D]** Amazon CloudWatch

**Correct Answer:**
- **[C] AWS CloudTrail**

**Why Correct:**
CloudTrail records all API calls/account activity - who did what, when, from where. Perfect for governance, compliance, auditing trail.

**Why Others Are Incorrect:**
Config = tracks resource configuration changes. Trusted Advisor = best practice checks. CloudWatch = performance monitoring.

---

### 54. AWS Services That Are Always Free
**Domain:** `Billing, Pricing & Support` | **Type:** `Multiple Choice (Select Two)` | **Difficulty:** `Medium`

**Question:**
> Which AWS services are always free to use (Select two)?

**Options:**
- **[A]** AWS Identity and Access Management (AWS IAM)
- **[B]** AWS Auto Scaling
- **[C]** Amazon DynamoDB
- **[D]** Amazon EC2
- **[E]** Amazon S3

**Correct Answer:**
- **[A] AWS Identity and Access Management (AWS IAM)**
- **[B] AWS Auto Scaling**

**Why Correct:**
IAM users/groups/roles/policies always free. Auto Scaling service itself free (pay only underlying resources it launches).

**Why Others Are Incorrect:**
DynamoDB/EC2/S3 have Free Tier limits but not always free - you pay after limits (EC2 Free Tier only 12 months).

---

### 55. Sharing Reserved EC2 Instances Across Accounts via Organizations
**Domain:** `Billing, Pricing & Support` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> A company uses reserved EC2 instances across multiple units with each unit having its own AWS account. However, some units under-utilize their reserved instances while other units need more reserved instances. As a Cloud Practitioner, which would you recommend as most cost-optimal solution?

**Options:**
- **[A]** Use AWS Systems Manager to manage AWS accounts of all units and then share the reserved EC2 instances amongst all units
- **[B]** Use AWS Cost Explorer to manage AWS accounts of all units and then share the reserved EC2 instances amongst all units
- **[C]** Use AWS Organizations to manage AWS accounts of all units and then share the reserved EC2 instances amongst all units
- **[D]** Use AWS Trusted Advisor to manage AWS accounts of all units and then share the reserved EC2 instances amongst all units

**Correct Answer:**
- **[C] Use AWS Organizations to manage AWS accounts of all units and then share the reserved EC2 instances amongst all units**

**Why Correct:**
Organizations with Consolidated Billing automatically shares unused RI discount across member accounts in org.

**Why Others Are Incorrect:**
Systems Manager/Cost Explorer/Trusted Advisor don't manage accounts or enable RI discount sharing.

---

### 56. Security Assessment and Penetration Testing Policies
**Domain:** `Security & Compliance` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> A cyber-security agency uses AWS Cloud and wants to carry out security assessments on its own AWS infrastructure without any prior approval from AWS. Which describes/facilitates this practice?

**Options:**
- **[A]** Network Stress Testing
- **[B]** Amazon Inspector
- **[C]** AWS Secrets Manager
- **[D]** Penetration Testing

**Correct Answer:**
- **[D] Penetration Testing**

**Why Correct:**
AWS allows Penetration Testing on your own infrastructure without prior approval (policy changed). Inspector is automated vuln scanner tool but policy term "without prior approval" specifically refers to Pen Testing.

**Why Others Are Incorrect:**
Network Stress Testing / DoS testing NOT allowed without prior approval - prohibited. Secrets Manager = stores secrets.

---

### 57. Operational Insights to Identify Resource Issues (Systems Manager)
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> A Cloud Practitioner would like to get operational insights of its resources to quickly identify any issues that might impact applications using those resources. Which AWS service can help?

**Options:**
- **[A]** AWS Health Dashboard - Your Account Health
- **[B]** AWS Trusted Advisor
- **[C]** AWS Systems Manager
- **[D]** Amazon Inspector

**Correct Answer:**
- **[C] AWS Systems Manager**

**Why Correct:**
Systems Manager centralizes operational data from multiple services, resource groups, API activity, config changes, notifications, operational alerts, inventory, patch compliance. Central place for visibility and control.

**Why Others Are Incorrect:**
Health Dashboard Account Health = alerts when AWS itself has events affecting you. Trusted Advisor = cost/perf/security best practices. Inspector = security assessment service.

---

### 58. Quickly Deploy Popular Technologies Using AWS Partner Solutions
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> A start-up would like to quickly deploy a popular technology on AWS. As a Cloud Practitioner, which AWS tool would you use?

**Options:**
- **[A]** AWS Forums
- **[B]** AWS Whitepapers
- **[C]** AWS CodeDeploy
- **[D]** AWS Partner Solutions (formerly Quick Starts)

**Correct Answer:**
- **[D] AWS Partner Solutions (formerly Quick Starts)**

**Why Correct:**
Partner Solutions are automated reference deployments built by AWS architects and Partners that deploy popular technologies per best practices in minutes (via CloudFormation), reducing hundreds of manual procedures to few steps.

**Why Others Are Incorrect:**
Forums = community Q&A. CodeDeploy = deploys your own code to EC2/on-prem. Whitepapers = technical content to read.

---

### 59. Linux EC2 Per-Second Billing Minimum Charge
**Domain:** `Billing, Pricing & Support` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> An intern at an IT company provisioned a Linux based On-demand EC2 instance with per-second billing but terminated it within 30 seconds as he wanted to provision another instance type. What is duration for which instance would be charged?

**Options:**
- **[A]** 30 seconds
- **[B]** 60 seconds
- **[C]** 300 seconds
- **[D]** 600 seconds

**Correct Answer:**
- **[B] 60 seconds**

**Why Correct:**
There is one-minute minimum charge for Linux EC2 instances. After first minute, per-second billing. So 30s usage billed for 60s.

**Why Others Are Incorrect:**
300s and 600s contradict, 30s ignores minimum.

---

### 60. Cost-Effective S3 Storage for Regenerable Thumbnails (One Zone-IA)
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> A photo sharing web application wants to store thumbnails of user-uploaded images on Amazon S3. Thumbnails are rarely used but need to be immediately accessible from web application. Thumbnails can be regenerated easily if lost. Which is most cost-effective way to store these thumbnails on S3?

**Options:**
- **[A]** Use Amazon S3 Glacier Flexible Retrieval to store the thumbnails
- **[B]** Use Amazon S3 Standard-Infrequent Access (S3 Standard-IA) to store the thumbnails
- **[C]** Use Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA) to store the thumbnails
- **[D]** Use Amazon S3 Standard to store the thumbnails

**Correct Answer:**
- **[C] Use Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA) to store the thumbnails**

**Why Correct:**
Rarely used = IA class. Immediately accessible = NOT Glacier (minutes-hours). Regenerable = OK with single AZ failure = One Zone-IA stores in 1 AZ, costs 20% less than Standard-IA, same durability/throughput/latency, but less availability which is OK here.

**Why Others Are Incorrect:**
Standard = frequent access expensive. Standard-IA = works but 20% more expensive than One Zone-IA when multi-AZ not needed. Glacier Flexible Retrieval = archival, retrieval time minutes-hours, not immediate.

---

### 61. Primary Benefit of Amazon RDS Read Replicas
**Domain:** `Cloud Technology & Service` | **Type:** `Single Choice` | **Difficulty:** `Medium`

**Question:**
> What is the primary benefit of deploying an Amazon RDS database in a Read Replica configuration?

**Options:**
- **[A]** Read Replica enhances database availability
- **[B]** Read Replica protects the database from a regional failure
- **[C]** Read Replica reduces database usage costs
- **[D]** Read Replica improves database scalability

**Correct Answer:**
- **[D] Read Replica improves database scalability**

**Why Correct:**
Read Replicas create read-only copies synchronized with master for improved read performance, horizontal scaling of reads. Can place in different Region closer to users.

**Why Others Are Incorrect:**
Enhances availability = Multi-AZ (sync standby in different AZ). Regional failure protection = Multi-Region. Reduces costs = increases costs (extra instance).

---

### 62. Key Advantages of Cloud Computing (Speed, Agility, Capacity)
**Domain:** `Cloud Concepts` | **Type:** `Multiple Choice (Select Two)` | **Difficulty:** `Medium`

**Question:**
> Which of the following are the advantages of using the AWS Cloud? (Select TWO)

**Options:**
- **[A]** Increase speed and agility
- **[B]** AWS is responsible for security in the cloud
- **[C]** Trade operational expense for capital expense
- **[D]** Limited scaling
- **[E]** Stop guessing about capacity

**Correct Answer:**
- **[A] Increase speed and agility**
- **[E] Stop guessing about capacity**

**Why Correct:**
From 6 Advantages whitepaper: Increase speed and agility, Stop guessing capacity, Trade CAPEX for OPEX, Economies of scale, Go global in minutes, Stop spending on data centers.

**Why Others Are Incorrect:**
"AWS is responsible for security IN the cloud" = reversed, AWS OF cloud, customer IN. "Trade operational for capital" = reversed, should be capital for operational. "Limited scaling" = opposite, unlimited/elastic.

---

### 63. Best Practices for Multi-Account Governance with AWS Organizations
**Domain:** `Billing, Pricing & Support` | **Type:** `Multiple Choice (Select Two)` | **Difficulty:** `Medium`

**Question:**
> Which of the following are the best practices when using AWS Organizations? (Select TWO)

**Options:**
- **[A]** Never use tags for billing
- **[B]** Create AWS accounts per department
- **[C]** Do not use AWS Organizations to automate AWS account creation
- **[D]** Disable AWS CloudTrail on several accounts
- **[E]** Restrict account privileges using Service Control Policies (SCP)

**Correct Answer:**
- **[B] Create AWS accounts per department**
- **[E] Restrict account privileges using Service Control Policies (SCP)**

**Why Correct:**
Organizations helps centrally govern as you grow. Automate account creation, create groups of accounts per business needs, apply policies, simplify billing single payment, central configs and resource sharing via other services integration. Create accounts per department for regulatory restrictions (via SCPs) for better isolation and per-account service limits. Use SCPs to restrict services/actions allowed as permission guardrails on IAM users/roles.

**Why Others Are Incorrect:**
Never use tags = SHOULD use tags standards to categorize resources for billing. Disable CloudTrail = SHOULD enable CloudTrail to monitor activity on all accounts for governance/compliance/risk/auditing. Do not automate creation = SHOULD automate via Organizations APIs to create accounts programmatically and policies auto-apply.

---

### 64. AWS Marketplace Key Use Cases (AMIs & SaaS)
**Domain:** `Billing, Pricing & Support` | **Type:** `Multiple Choice (Select Two)` | **Difficulty:** `Medium`

**Question:**
> AWS Marketplace facilitates which of the following use-cases? (Select two)

**Options:**
- **[A]** Buy Amazon EC2 Standard Reserved Instances (RI)
- **[B]** AWS customer can buy software that has been bundled into customized Amazon Machine Image (AMIs) by the AWS Marketplace sellers
- **[C]** Purchase compliance documents from third-party vendors
- **[D]** Sell Software as a Service (SaaS) solutions to AWS customers
- **[E]** Raise request for purchasing AWS Direct Connect connection

**Correct Answer:**
- **[B] AWS customer can buy software that has been bundled into customized Amazon Machine Image (AMIs) by the AWS Marketplace sellers**
- **[D] Sell Software as a Service (SaaS) solutions to AWS customers**

**Why Correct:**
AWS Marketplace is digital catalog with thousands of software listings from ISVs to find/test/buy/deploy software that runs on AWS. Enables qualified partners to market and sell their software. Two ways: AMI (preferred, free or paid hourly/monthly/BYOL) and SaaS (if unable to build into AMI).

**Why Others Are Incorrect:**
Purchase compliance documents = AWS Artifact is central resource for compliance reports and agreements. Buy EC2 Standard RI = EC2 console at console.aws.amazon.com/ec2. Direct Connect connection = Direct Connect console.

---

### 65. AWS Organizations Benefits - Consolidated Discounts & Resource Sharing
**Domain:** `Billing, Pricing & Support` | **Type:** `Multiple Choice (Select Two)` | **Difficulty:** `Medium`

**Question:**
> AWS Organizations provides which benefits? (Select two)

**Options:**
- **[A]** Volume discounts for Amazon EC2 and Amazon S3 aggregated across the member AWS accounts
- **[B]** Deploy patches on Amazon EC2 instances across the member AWS accounts
- **[C]** Check vulnerabilities on Amazon EC2 instances across the member AWS accounts
- **[D]** Share the reserved Amazon EC2 instances amongst the member AWS accounts
- **[E]** Provision Amazon EC2 Spot instances across the member AWS accounts

**Correct Answer:**
- **[A] Volume discounts for Amazon EC2 and Amazon S3 aggregated across the member AWS accounts**
- **[D] Share the reserved Amazon EC2 instances amongst the member AWS accounts**

**Why Correct:**
Organizations helps centrally manage billing, control access/compliance/security, share resources such as reserved EC2 across accounts. Consolidated billing combined view + volume discounts aggregated. Key benefits via aws.amazon.com/organizations.

**Why Others Are Incorrect:**
Deploy patches = Systems Manager. Check vulnerabilities = Inspector. Provision Spot = EC2 feature.

---

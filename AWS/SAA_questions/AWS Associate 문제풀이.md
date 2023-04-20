# AWS Associate 문제풀이

- Q2
    
    A company needs the ability to analyze the log files of its proprietary application. The logs are stored in JSON format in an Amazon S3 bucket. Queries will be simple and will run on-demand. A solutions architect needs to perform the analysis with minimal changes to the existing architecture. 
    
    What should the solutions architect do to meet these requirements with the LEAST amount of operational overhead?
    
    - A. Use Amazon Redshift to load all the content into one place and run the SQL queries as needed.
    - B. Use Amazon CloudWatch Logs to store the logs. Run SQL queries as needed from the Amazon CloudWatch console.
    - C. Use Amazon Athena directly with Amazon S3 to run the queries as needed. **Most Voted**
    - D. Use AWS Glue to catalog the logs. Use a transient Apache Spark cluster on Amazon EMR to run the SQL queries as needed.
    
    근거
    
    - 문제 : S3에 로그를 저장 ⇒ 해당 로그를 분석
    - 가장 간단한 방법 : S3에 저장한 log를 Athena를 활용해 SQL query로 Analysis Report를 만드는 것.
    - Athena : 파일로 저장된 텍스트 데이터에 SQL query를 사용할 수 있는 서비스
    
- Q3
    
    A company uses AWS Organizations to manage multiple AWS accounts for different departments. The management account has an Amazon S3 bucket that contains project reports. The company wants to limit access to this S3 bucket to only users of accounts within the organization in AWS Organizations.
    
    Which solution meets these requirements with the LEAST amount of operational overhead?
    
    - A. Add the aws PrincipalOrgID global condition key with a reference to the organization ID to the S3 bucket policy. **Most Voted**
    - B. Create an organizational unit (OU) for each department. Add the aws:PrincipalOrgPaths global condition key to the S3 bucket policy.
    - C. Use AWS CloudTrail to monitor the CreateAccount, InviteAccountToOrganization, LeaveOrganization, and RemoveAccountFromOrganization events. Update the S3 bucket policy accordingly.
    - D. Tag each user that needs access to the S3 bucket. Add the aws:PrincipalTag global condition key to the S3 bucket policy.
    
    근거 :
    
    - 문제 : Organiztions를 활용해서 S3 bucket 접근 권한을 제어하는 방법은?
    - aws:PrincipalOrgID라는 새로운 [조건 키](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)를 권한 정책에 사용하여 조직 내의 계정에 해당하는 IAM 보안 주체(사용자 및 역할)만 리소스에 액세스할 수 있도록 합니다.
    - [https://aws.amazon.com/ko/about-aws/whats-new/2018/05/principal-org-id/#:~:text=aws%3APrincipalOrgID라는 새로운 조건,액세스할 수 있도록 합니다](https://aws.amazon.com/ko/about-aws/whats-new/2018/05/principal-org-id/#:~:text=aws%3APrincipalOrgID%EB%9D%BC%EB%8A%94%20%EC%83%88%EB%A1%9C%EC%9A%B4%20%EC%A1%B0%EA%B1%B4,%EC%95%A1%EC%84%B8%EC%8A%A4%ED%95%A0%20%EC%88%98%20%EC%9E%88%EB%8F%84%EB%A1%9D%20%ED%95%A9%EB%8B%88%EB%8B%A4).
    
- Q4
    
    An application runs on an Amazon EC2 instance in a VPC. The application processes logs that are stored in an Amazon S3 bucket. The EC2 instance needs to access the S3 bucket without connectivity to the internet.
    
    Which solution will provide private network connectivity to Amazon S3?
    
    - A. Create a gateway VPC endpoint to the S3 bucket. **Most Voted**
    - B. Stream the logs to Amazon CloudWatch Logs. Export the logs to the S3 bucket.
    - C. Create an instance profile on Amazon EC2 to allow S3 access.
    - D. Create an Amazon API Gateway API with a private link to access the S3 endpoint.
    
    근거 :
    
    - 문제 : EC2와 S3를 직접 연결하는 방법은?
    - S3는 VPC 밖에, EC2는 VPC 내부에 존재한다. 일반적이라면 S3와 EC2는 인터넷을 거쳐야 하는데, AWS endpoint를 사용하면 인터넷을 거치지 않고 직접 연결이 가능하다.
    - VPC endpoint allows you to connect to AWS services using a private network instead of using the public Internet
- Q8
    
    A company is migrating a distributed application to AWS. The application serves variable workloads. The legacy platform consists of a primary server that coordinates jobs across multiple compute nodes. The company wants to modernize the application with a solution that maximizes resiliency and scalability.
    
    How should a solutions architect design the architecture to meet these requirements?
    
    - A. Configure an Amazon Simple Queue Service (Amazon SQS) queue as a destination for the jobs. Implement the compute nodes with Amazon EC2 instances that are managed in an Auto Scaling group. Configure EC2 Auto Scaling to use scheduled scaling.
    - B. Configure an Amazon Simple Queue Service (Amazon SQS) queue as a destination for the jobs. Implement the compute nodes with Amazon EC2 instances that are managed in an Auto Scaling group. Configure EC2 Auto Scaling based on the size of the queue. **Most Voted**
    - C. Implement the primary server and the compute nodes with Amazon EC2 instances that are managed in an Auto Scaling group. Configure AWS CloudTrail as a destination for the jobs. Configure EC2 Auto Scaling based on the load on the primary server.
    - D. Implement the primary server and the compute nodes with Amazon EC2 instances that are managed in an Auto Scaling group. Configure Amazon EventBridge (Amazon CloudWatch Events) as a destination for the jobs. Configure EC2 Auto Scaling based on the load on the compute nodes.
    
    근거 : 
    
    문제 : 레거시 플랫폼을 aws를 통해 탄력적이고 확장가능하게 향상 시키고 싶다.
    
    - A가 틀린 이유는 Scailing이 대응이 아닌 계획으로 수행되기 때문이다. queue가 늘어나면 scailing을 하게하여 즉각적으로 대응할 수 있게 해야함.
    - resiliency : SQS를 사용한다. **SQS Queue**에 들어온 메세지는 삭제하기 전에는 지워지지 않는다는 장점이 있기에 최소한 한 번은 꼭! 실행이 보장된다.
    - scalability : Auto Scaling을 사용한다.
- Q9
    
    A company is running an SMB file server in its data center. The file server stores large files that are accessed frequently for the first few days after the files are created. After 7 days the files are rarely accessed.The total data size is increasing and is close to the company's total storage capacity. A solutions architect must increase the company's available storage space without losing low-latency access to the most recently accessed files. The solutions architect must also provide file lifecycle management to avoid future storage issues.
    
    Which solution will meet these requirements?
    
    - A. Use AWS DataSync to copy data that is older than 7 days from the SMB file server to AWS.
    - B. Create an Amazon S3 File Gateway to extend the company's storage space. Create an S3 Lifecycle policy to transition the data to S3 Glacier Deep Archive after 7 days. **Most Voted**
    - C. Create an Amazon FSx for Windows File Server file system to extend the company's storage space.
    - D. Install a utility on each user's computer to access Amazon S3. Create an S3 Lifecycle policy to transition the data to S3 Glacier Flexible Retrieval after 7 days.
    
    근거
    
    - 문제 : SMB 파일 서버를 자체 운영중인 회사 ⇒ 7일 내 파일은 자주 접근 되지만 그 이후는 접근이 거의 없음 ⇒ 데이터는 계속 쌓이고 있고 레이턴시를 감소시키지 않는 선에서 스토리지를 늘려야함. ⇒ 또한 file lifecycle management를 사용해야함.
    - SMB : Server Message Block 리눅스에서 윈도우 간 파일 전송을 위해 사용하는 듯
        - [https://leehands.tistory.com/entry/파일서버-SMB-CIFS-NFS-란](https://leehands.tistory.com/entry/%ED%8C%8C%EC%9D%BC%EC%84%9C%EB%B2%84-SMB-CIFS-NFS-%EB%9E%80)
    - 온프레미스 환경에 대한 확장을 위해 S3를 사용하는 경우이므로 File gateway를 사용한다. 또한 Lifecycle management를 위해 S3 Lifecycle policy를 사용한다.
- Q10
    
    A company has an application that runs on Amazon EC2 instances and uses an Amazon Aurora database. The EC2 instances connect to the database by using user names and passwords that are stored locally in a file. The company wants to minimize the operational overhead of credential management.
    
    What should a solutions architect do to accomplish this goal?
    
    - A. Use AWS Secrets Manager. Turn on automatic rotation. **Most Voted**
    - B. Use AWS Systems Manager Parameter Store. Turn on automatic rotation.
    - C. Create an Amazon S3 bucket to store objects that are encrypted with an AWS Key Management Service (AWS KMS) encryption key. Migrate the credential file to the S3 bucket. Point the application to the S3 bucket.
    - D. Create an encrypted Amazon Elastic Block Store (Amazon EBS) volume for each EC2 instance. Attach the new EBS volume to each EC2 instance. Migrate the credential file to the new EBS volume. Point the application to the new EBS volume.
    
    문제 :  EC2와 Aurora Database를 연결해서 사용 중 ⇒ 연결에 필요한 계정, pwd를 로컬 파일에서 사용 ⇒ 이를 aws에서 적용하기
    
    - AWS Secrets Manager를 사용하자.
    
- Q12
    
    A global company hosts its web application on Amazon EC2 instances behind an Application Load Balancer (ALB). The web application has static data and dynamic data. The company stores its static data in an Amazon S3 bucket. The company wants to improve performance and reduce latency for the static data and dynamic data. The company is using its own domain name registered with Amazon Route 53.
    
    What should a solutions architect do to meet these requirements?
    
    - A. Create an Amazon CloudFront distribution that has the S3 bucket and the ALB as origins. Configure Route 53 to route traffic to the CloudFront distribution.
    - B. Create an Amazon CloudFront distribution that has the ALB as an origin. Create an AWS Global Accelerator standard accelerator that has the S3 bucket as an endpoint Configure Route 53 to route traffic to the CloudFront distribution.
    - **C. Create an Amazon CloudFront distribution that has the S3 bucket as an origin. Create an AWS Global Accelerator standard accelerator that has the ALB and the CloudFront distribution as endpoints. Create a custom domain name that points to the accelerator DNS name. Use the custom domain name as an endpoint for the web application.**
    - D. Create an Amazon CloudFront distribution that has the ALB as an origin. Create an AWS Global Accelerator standard accelerator that has the S3 bucket as an endpoint. Create two domain names. Point one domain name to the CloudFront DNS name for dynamic content. Point the other domain name to the accelerator DNS name for static content. Use the domain names as endpoints for the web application.
    
    근거 :
    
    - 문제 : static data와 dynamic data를 low latency로 배포하고 싶다. ⇒ route53을 사용한다.
    - A와 C중 사람들이 갈림 Cloudfront가 dynamic data에 대한 cache가 가능한지 모르겠음.
    - 나는 일단 C 같음.. 왠지는 잘;;
    - [AWS Global Accelerator](https://aws.amazon.com/ko/global-accelerator/?nc2=h_re) 는 AWS 글로벌 네트워크를 활용해 경로를 최적화해서 성능을 높이고, 지속적인 모니터링으로 가용성을 제공합니다. 따라서 재해 복구에 대응하고, 성능 개선과 네트워크 확장 등을 손쉽게 구성할 수 있습니다.
    
- Q13
    
    A company performs monthly maintenance on its AWS infrastructure. During these maintenance activities, the company needs to rotate the credentials for its Amazon RDS for MySQL databases across multiple AWS Regions.
    
    Which solution will meet these requirements with the LEAST operational overhead?
    
    - A. Store the credentials as secrets in AWS Secrets Manager. Use multi-Region secret replication for the required Regions. Configure Secrets Manager to rotate the secrets on a schedule. **Most Voted**
    - B. Store the credentials as secrets in AWS Systems Manager by creating a secure string parameter. Use multi-Region secret replication for the required Regions. Configure Systems Manager to rotate the secrets on a schedule.
    - C. Store the credentials in an Amazon S3 bucket that has server-side encryption (SSE) enabled. Use Amazon EventBridge (Amazon CloudWatch Events) to invoke an AWS Lambda function to rotate the credentials.
    - D. Encrypt the credentials as secrets by using AWS Key Management Service (AWS KMS) multi-Region customer managed keys. Store the secrets in an Amazon DynamoDB global table. Use an AWS Lambda function to retrieve the secrets from DynamoDB. Use the RDS API to rotate the secrets.
    
    근거 
    
    - 문제 : 매월 서버 유지보수를 수행할 때 DB Credential을 업데이트한다. 가장 간단한 방법은
    - Credential 업데이트를 가장 빠르고 간단하게 하기 위한 방법은 AWS Secret Manager를 사용하는 것.
- Q14
    
    A company runs an ecommerce application on Amazon EC2 instances behind an Application Load Balancer. The instances run in an Amazon EC2 Auto Scaling group across multiple Availability Zones. The Auto Scaling group scales based on CPU utilization metrics. The ecommerce application stores the transaction data in a MySQL 8.0 database that is hosted on a large EC2 instance.The database's performance degrades quickly as application load increases. The application handles more read requests than write transactions. The company wants a solution that will automatically scale the database to meet the demand of unpredictable read workloads while maintaining high availability.
    
    Which solution will meet these requirements?
    
    - A. Use Amazon Redshift with a single node for leader and compute functionality.
    - B. Use Amazon RDS with a Single-AZ deployment Configure Amazon RDS to add reader instances in a different Availability Zone.
    - C. Use Amazon Aurora with a Multi-AZ deployment. Configure Aurora Auto Scaling with Aurora Replicas. **Most Voted**
    - D. Use Amazon ElastiCache for Memcached with EC2 Spot Instances.
    - 
    
    근거 
    
    - 문제 : ALB와 EC2를 사용 중 ⇒ EC2는 CPU Auto-scailig + multi-AZ ⇒ 큰 EC2에서 mysql 8.0 사용 중 ⇒ 앱 로드가 오르면 mysql 성능 하락 ⇒ 이 문제 해결할 방법은?
    - C, AURORA is 5x performance improvement over MySQL on RDS and handles more read requests than write,; maintaining high availability = Multi-AZ deployment
- Q15
    
    A company recently migrated to AWS and wants to implement a solution to protect the traffic that flows in and out of the production VPC. The company had an inspection server in its on-premises data center. The inspection server performed specific operations such as traffic flow inspection and traffic filtering. The company wants to have the same functionalities in the AWS Cloud.
    
    Which solution will meet these requirements?
    
    - A. Use Amazon GuardDuty for traffic inspection and traffic filtering in the production VPC.
    - B. Use Traffic Mirroring to mirror traffic from the production VPC for traffic inspection and filtering.
    - C. Use AWS Network Firewall to create the required rules for traffic inspection and traffic filtering for the production VPC. **Most Voted**
    - D. Use AWS Firewall Manager to create the required rules for traffic inspection and traffic filtering for the production VPC.
    
    근거 
    
    - 문제 : VPC 내부에 in and out 되는 traffic 보호 목적으로 AWS로 마이그레이션 ⇒ 온프레미스에는 트래픽을 조사하고 필터하는 역할을 수행하는 서버가 있음 ⇒ AWS에서는 이 기능을 어떤 서비스가 수행하는지?
    - VPC에서 발생하는 트래픽에 대한 Filtering & inspection을 수행하는 서비스는 Firewall manager라고 기억하자.
    - GuardDuty는 위협을 감시하고 예측 가능한 위협을 식별하는 서비스
- Q16
    
    A company hosts a data lake on AWS. The data lake consists of data in Amazon S3 and Amazon RDS for PostgreSQL. The company needs a reporting solution that provides data visualization and includes all the data sources within the data lake. Only the company's management team should have full access to all the visualizations. The rest of the company should have only limited access.
    
    Which solution will meet these requirements?
    
    - A. Create an analysis in Amazon QuickSight. Connect all the data sources and create new datasets. Publish dashboards to visualize the data. Share the dashboards with the appropriate IAM roles.
    - B. Create an analysis in Amazon QuickSight. Connect all the data sources and create new datasets. Publish dashboards to visualize the data. Share the dashboards with the appropriate users and groups. **Most Voted**
    - C. Create an AWS Glue table and crawler for the data in Amazon S3. Create an AWS Glue extract, transform, and load (ETL) job to produce reports. Publish the reports to Amazon S3. Use S3 bucket policies to limit access to the reports.
    - D. Create an AWS Glue table and crawler for the data in Amazon S3. Use Amazon Athena Federated Query to access data within Amazon RDS for PostgreSQL. Generate reports by using Amazon Athena. Publish the reports to Amazon S3. Use S3 bucket policies to limit access to the reports.
    
    근거 
    
    - 문제 : S3와 postrgreSQL로 DataLake를 형성 ⇒ DataLake에 대한 시각화 보고서를 작성하려고 함 ⇒ Management 팀은 Full Access 나머지는 제한된 Access를 가져야함.
    - QuickSight ⇒ 아마존이 제공하는 서버리스 매니지드 **BI** 상품이다. 특정 데이터에 대한 시각화 대시보드를 생성하고 다른 사용자와 공유할 수 있다.
- Q17
    
    A company is implementing a new business application. The application runs on two Amazon EC2 instances and uses an Amazon S3 bucket for document storage. A solutions architect needs to ensure that the EC2 instances can access the S3 bucket.
    
    What should the solutions architect do to meet this requirement?
    
    - A. Create an IAM role that grants access to the S3 bucket. Attach the role to the EC2 instances. **Most Voted**
    - B. Create an IAM policy that grants access to the S3 bucket. Attach the policy to the EC2 instances.
    - C. Create an IAM group that grants access to the S3 bucket. Attach the group to the EC2 instances.
    - D. Create an IAM user that grants access to the S3 bucket. Attach the user account to the EC2 instance
    
    근거
    
    - 문제 : EC2에 S3를 연결시키고자 할 때 필요한 것은?
    - IAM role을 만들어야한다. 그리고 그 role을 ec2에게 부여한다.
- Q18
    
    An application development team is designing a microservice that will convert large images to smaller, compressed images. When a user uploads an image through the web interface, the microservice should store the image in an Amazon S3 bucket, process and compress the image with an AWS Lambda function, and store the image in its compressed form in a different S3 bucket.A solutions architect needs to design a solution that uses durable, stateless components to process the images automatically.
    
    Which combination of actions will meet these requirements? (Choose two.)
    
    - A. Create an Amazon Simple Queue Service (Amazon SQS) queue. Configure the S3 bucket to send a notification to the SQS queue when an image is uploaded to the S3 bucket. **Most Voted**
    - B. Configure the Lambda function to use the Amazon Simple Queue Service (Amazon SQS) queue as the invocation source. When the SQS message is successfully processed, delete the message in the queue. **Most Voted**
    - C. Configure the Lambda function to monitor the S3 bucket for new uploads. When an uploaded image is detected, write the file name to a text file in memory and use the text file to keep track of the images that were processed.
    - D. Launch an Amazon EC2 instance to monitor an Amazon Simple Queue Service (Amazon SQS) queue. When items are added to the queue, log the file name in a text file on the EC2 instance and invoke the Lambda function.
    - E. Configure an Amazon EventBridge (Amazon CloudWatch Events) event to monitor the S3 bucket. When an image is uploaded, send an alert to an Amazon ample Notification Service (Amazon SNS) topic with the application owner's email address for further processing.
    
    근거
    
    - 문제 : 큰 이미지를 작게 압축하는 MicroService를 구축하려 한다. ⇒ 이미지가 업로드 되면 S3에 저장되고 lambda 함수를 사용해 이미지가 작아진 다음 다시 S3에 저장된다. ⇒ 이 절차를 수행하기 위한 방법은?
    - 이미지가 S3에 저장되면 그 다음으로 이미지가 저장되었다고 SQS에게 알린다.
    - lambda와 SimpleQueueService를 사용해서 큰 이미지가 작은 이미지로 변경되어야 하는 절차를 수행하게 한다.
- Q19
    
    A company has a three-tier web application that is deployed on AWS. The web servers are deployed in a public subnet in a VPC. The application servers and database servers are deployed in private subnets in the same VPC. The company has deployed a third-party virtual firewall appliance from AWS Marketplace in an inspection VPC. The appliance is configured with an IP interface that can accept IP packets. A solutions architect needs to integrate the web application with the appliance to inspect all traffic to the application before the traffic reaches the web server.
    
    Which solution will meet these requirements with the LEAST operational overhead?
    
    - A. Create a Network Load Balancer in the public subnet of the application's VPC to route the traffic to the appliance for packet inspection.
    - B. Create an Application Load Balancer in the public subnet of the application's VPC to route the traffic to the appliance for packet inspection.
    - C. Deploy a transit gateway in the inspection VPConfigure route tables to route the incoming packets through the transit gateway.
    - D. Deploy a Gateway Load Balancer in the inspection VPC. Create a Gateway Load Balancer endpoint to receive the incoming packets and forward the packets to the appliance. **Most Voted**
    
    근거
    
    - 문제 : 3티어 web app을 AWS에서 운영중 ⇒ Server는 Public Subnet에서 운영중 ⇒ 앱 서버와 데이터베이서는 Private Server에서 운영중 ⇒ 타사 firewall을 사용 중 ⇒ Public에서 운영중인 Webserver에 Firewall을 사용하고 싶음. ⇒ 가장 효율적인 방법은?
    - GWLB는 Firewall을 관리하는 서비스라고 이해하자.
    - GWLB : Network 단의 로드 밸런싱을 지원한다. 박화벽, 침입 탐지 및 방지 시스템, 심층 패킷 검사 시스템과 같은 가상 Appliance를 관리할 수 있다고 한다. (일반적인 로드밸런서 역할과 다르게 트래픽을 체크하는 용도라고 한다.)
- Q20
    
    A company wants to improve its ability to clone large amounts of production data into a test environment in the same AWS Region. The data is stored in Amazon EC2 instances on Amazon Elastic Block Store (Amazon EBS) volumes. Modifications to the cloned data must not affect the production environment. The software that accesses this data requires consistently high I/O performance. A solutions architect needs to minimize the time that is required to clone the production data into the test environment.
    
    Which solution will meet these requirements?
    
    - A. Take EBS snapshots of the production EBS volumes. Restore the snapshots onto EC2 instance store volumes in the test environment.
    - B. Configure the production EBS volumes to use the EBS Multi-Attach feature. Take EBS snapshots of the production EBS volumes. Attach the production EBS volumes to the EC2 instances in the test environment.
    - C. Take EBS snapshots of the production EBS volumes. Create and initialize new EBS volumes. Attach the new EBS volumes to EC2 instances in the test environment before restoring the volumes from the production EBS snapshots.
    - D. Take EBS snapshots of the production EBS volumes. Turn on the EBS fast snapshot restore feature on the EBS snapshots. Restore the snapshots into new EBS volumes. Attach the new EBS volumes to EC2 instances in the test environment. **Most Voted**
    
    근거 
    
    - 문제 : 테스트 환경에서 production Level의 Data를 사용하고 싶다. ⇒ EC2 EBS에 저장되고 있음 ⇒ production Level에서 Test Level로 데이터를 옮기는 가장 좋은 방법은?
    - Production Level의 데이터를 Test 환경으로 옮기는 가장 효과적인 방법은 EBS의 fast snapshot을 사용한다.
    - 데이터 복사를 빠르게 하는 방법이 스냅샷을 사용하는 것이군
- Q21
    
    A company observes an increase in Amazon EC2 costs in its most recent bill. The billing team notices unwanted vertical scaling of instance types for a couple of EC2 instances. A solutions architect needs to create a graph comparing the last 2 months of EC2 costs and perform an in-depth analysis to identify the root cause of the vertical scaling.
    
    How should the solutions architect generate the information with the LEAST operational overhead?
    
    - A. Use AWS Budgets to create a budget report and compare EC2 costs based on instance types.
    - B. Use Cost Explorer's granular filtering feature to perform an in-depth analysis of EC2 costs based on instance types. **Most Voted**
    - C. Use graphs from the AWS Billing and Cost Management dashboard to compare EC2 costs based on instance types for the last 2 months.
    - D. Use AWS Cost and Usage Reports to create a report and send it to an Amazon S3 bucket. Use Amazon QuickSight with Amazon S3 as a source to generate an interactive graph based on instance types.
    
    근거 
    
    - 문제 : EC2 비용 상승을 보니 Vertical Scaling이 원인이었음. ⇒ 어떠한 이유로 vertical scaling이 되는지 찾기 위해 지난 2개월의 비용 그래프를 만들고 근본적인 원인을 분석하려고 함 ⇒ 최소의 노력으로 해당 정보를 생성하는 방법은?
    - Cost Explorer : 비용 최적화를 위한 서비스
    
- Q26
    
    A company needs to review its AWS Cloud deployment to ensure that its Amazon S3 buckets do not have unauthorized configuration changes.
    
    What should a solutions architect do to accomplish this goal?
    
    - A. Turn on AWS Config with the appropriate rules. **Most Voted**
    - B. Turn on AWS Trusted Advisor with the appropriate checks.
    - C. Turn on Amazon Inspector with the appropriate assessment template.
    - D. Turn on Amazon S3 server access logging. Configure Amazon EventBridge (Amazon Cloud Watch Events).
    
    근거
    
    - 문제 : S3 버켓 관련해서 무단으로 환경설정 변화가 발생하는지 추적이 필요함.
    - AWS Config를 켜놓는다.
- Q27
    
    A company is launching a new application and will display application metrics on an Amazon CloudWatch dashboard. The company's product manager needs to access this dashboard periodically. The product manager does not have an AWS account. A solutions architect must provide access to the product manager by following the principle of least privilege.
    
    Which solution will meet these requirements?
    
    - **A. Share the dashboard from the CloudWatch console. Enter the product manager's email address, and complete the sharing steps. Provide a shareable link for the dashboard to the product manager.**
    - B. Create an IAM user specifically for the product manager. Attach the CloudWatchReadOnlyAccess AWS managed policy to the user. Share the new login credentials with the product manager. Share the browser URL of the correct dashboard with the product manager.
    - C. Create an IAM user for the company's employees. Attach the ViewOnlyAccess AWS managed policy to the IAM user. Share the new login credentials with the product manager. Ask the product manager to navigate to the CloudWatch console and locate the dashboard by name in the Dashboards section.
    - D. Deploy a bastion server in a public subnet. When the product manager requires access to the dashboard, start the server and share the RDP credentials. On the bastion server, ensure that the browser is configured to open the dashboard URL with cached AWS credentials that have appropriate permissions to view the dashboard.
    
    근거 :
    
    - 문제 : 새로 출시한 앱에 대한 metric 추적이 필요 ⇒ 대시보드를 PM이 확인해야하는데, AWS 계정이 없다. 이때 권한을 최소화하는 방식으로 대시보드에 접근할 수 있는 방법은?
    - Cloudwatch에 AWS 아이디가 없더라도  대시보드를 접근할 수 있는 기능이 있다고 한다.
- Q28
    
    A company is migrating applications to AWS. The applications are deployed in different accounts. The company manages the accounts centrally by using AWS Organizations. The company's security team needs a **single sign-on (SSO) solution across all the company's accounts.** The company must continue managing the users and groups in its on-premises self-managed Microsoft Active Directory.
    
    Which solution will meet these requirements?
    
    - A. Enable AWS Single Sign-On (AWS SSO) from the AWS SSO console. Create a one-way forest trust or a one-way domain trust to connect the company's self-managed Microsoft Active Directory with AWS SSO by using AWS Directory Service for Microsoft Active Directory.
    - B. Enable AWS Single Sign-On (AWS SSO) from the AWS SSO console. Create a two-way forest trust to connect the company's self-managed Microsoft Active Directory with AWS SSO by using AWS Directory Service for Microsoft Active Directory. **Most Voted**
    - C. Use AWS Directory Service. Create a two-way trust relationship with the company's self-managed Microsoft Active Directory.
    - D. Deploy an identity provider (IdP) on premises. Enable AWS Single Sign-On (AWS SSO) from the AWS SSO console.
    
    근거 
    
    - 온프레미스에서 AWS로 마이그레이션을 수행했다. ⇒ 여러 계정에서 서비스를 실행하므로 AWS Organizations를 사용해서 중앙으로 관리하고 있다. ⇒ 보안 팀은 SSO 솔루션이 필요하다. ⇒ 또한 온프레미스에 있는 유저와 그룹도 지속적으로 관리해야한다.
    - AWS SSO를 사용하자. 마이크로소프트 디렉토리도 접근해야하므로 two-way forest trust를 설정한다.
    - 외우자…
- Q29
    
    A company provides a Voice over Internet Protocol (VoIP) service that uses UDP connections. The service consists of Amazon EC2 instances that run in an Auto Scaling group. The company has deployments across multiple AWS Regions.The company needs to route users to the Region with the lowest latency. The company also needs automated failover between Regions.
    
    Which solution will meet these requirements?
    
    - A. Deploy a Network Load Balancer (NLB) and an associated target group. Associate the target group with the Auto Scaling group. Use the NLB as an AWS Global Accelerator endpoint in each Region. **Most Voted**
    - B. Deploy an Application Load Balancer (ALB) and an associated target group. Associate the target group with the Auto Scaling group. Use the ALB as an AWS Global Accelerator endpoint in each Region.
    - C. Deploy a Network Load Balancer (NLB) and an associated target group. Associate the target group with the Auto Scaling group. Create an Amazon Route 53 latency record that points to aliases for each NLB. Create an Amazon CloudFront distribution that uses the latency record as an origin.
    - D. Deploy an Application Load Balancer (ALB) and an associated target group. Associate the target group with the Auto Scaling group. Create an Amazon Route 53 weighted record that points to aliases for each ALB. Deploy an Amazon CloudFront distribution that uses the weighted record as an origin.
    
    근거
    
    - 문제 : VoIP, EC2를 운영중에 있는 회사임 ⇒ 서비스는 전세계 리전에서 운영중에 있음 ⇒ 회사는 lowest latency를 유지하고 싶으며 automated failover를 필요로 함.
    - Global Accelerator : 글로벌 유저들에게 고객 서비스를 빠르게 제공하는데 도움을 주는 aws 서비스
    - APP Load Balancer를 운용하고 AWS Global Accelerator에 엔드포인트로 지정한다.
    - C가 아닌 이유 일단 Cloudfront는 CDN인데 VoIP에는 쓸일이 없음
- Q30
    
    A development team runs monthly resource-intensive tests on its general purpose Amazon RDS for MySQL DB instance with Performance Insights enabled. The testing lasts for 48 hours once a month and is the only process that uses the database. The team wants to reduce the cost of running the tests without reducing the compute and memory attributes of the DB instance.
    
    Which solution meets these requirements MOST cost-effectively?
    
    - A. Stop the DB instance when tests are completed. Restart the DB instance when required.
    - B. Use an Auto Scaling policy with the DB instance to automatically scale when tests are completed.
    - C. Create a snapshot when tests are completed. Terminate the DB instance and restore the snapshot when required. **Most Voted**
    - D. Modify the DB instance to a low-capacity instance when tests are completed. Modify the DB instance again when required.
    
    근거 
    
    - 문제 : 매달 리소스 집중적인 RDS 테스트와 Performance Insights를 수행 ⇒ 해당 테스트는 한 달에 한 번 48시간 지속되고 db만을 사용해서 수행된다. ⇒ DB 인스턴스의 cpu, mem 리소스를 유지한 체로 가격을 아끼는 방식으로 테스트 하려한다. ⇒ 가장 저렴한 방법은?
    - 테스트가 끝나면 snapshot으로 저장하고 DB를 끈다. 필요할 때 스냅샷을 다시 연다.
- Q31
    
    A company that hosts its web application on AWS wants to ensure all Amazon EC2 instances, Amazon RDS DB instances, and Amazon Redshift clusters are configured with tags. The company wants to minimize the effort of configuring and operating this check.
    
    What should a solutions architect do to accomplish this?
    
    - A. Use AWS Config rules to define and detect resources that are not properly tagged. **Most Voted**
    - B. Use Cost Explorer to display resources that are not properly tagged. Tag those resources manually.
    - C. Write API calls to check all resources for proper tag allocation. Periodically run the code on an EC2 instance.
    - D. Write API calls to check all resources for proper tag allocation. Schedule an AWS Lambda function through Amazon CloudWatch to periodically run the code.
    
    근거 
    
    - 문제 : 아마존 EC2 instance, RDS redshift가 태그로 관리되고 있는지 확인하고 싶다. ⇒ 검사를 구성하고 운영하는 작업을 최소화 하려한다.
    - aws 리소스를 조직하기 위한 메타데이터이다. key value로 구성되어 있다.
    - AWS Config에서 tag와 관련된 설정을 관리 할 수 있군.
- Q33
    
    A company runs an online marketplace web application on AWS. The application serves hundreds of thousands of users during peak hours. The company needs a scalable, near-real-time solution to share the details of millions of financial transactions with several other internal applications. Transactions also need to be processed to remove sensitive data before being stored in a document database for low-latency retrieval.
    
    What should a solutions architect recommend to meet these requirements?
    
    - A. Store the transactions data into Amazon DynamoDB. Set up a rule in DynamoDB to remove sensitive data from every transaction upon write. Use DynamoDB Streams to share the transactions data with other applications.
    - B. Stream the transactions data into Amazon Kinesis Data Firehose to store data in Amazon DynamoDB and Amazon S3. Use AWS Lambda integration with Kinesis Data Firehose to remove sensitive data. Other applications can consume the data stored in Amazon S3.
    - C. Stream the transactions data into Amazon Kinesis Data Streams. Use AWS Lambda integration to remove sensitive data from every transaction and then store the transactions data in Amazon DynamoDB. Other applications can consume the transactions data off the Kinesis data stream. **Most Voted**
    - D. Store the batched transactions data in Amazon S3 as files. Use AWS Lambda to process every file and remove sensitive data before updating the files in Amazon S3. The Lambda function then stores the data in Amazon DynamoDB. Other applications can consume transaction files stored in Amazon S3.
    
    근거
    
    - 문제 : 시간당 수십만명의 유저가 사용하는 앱을 운영 중이다. ⇒ 내부 앱 간 수백만 건의 트랜잭션이 일어나고 거의 실시간으로 처리되어야 한다, 이를 처리할 수 있는 scalable, durable할 수 있게 솔루션을 구축하고 싶다. ⇒ 또한 문서 저장에서 민감 정보를 제거해야한다.
    - 민감 정보는 lambda 함수를 통해 제거하는게 효율적임
    - 실시간으로 데이터를 처리하고 분석하는데 Kinesis Data Stream을 사용하면 된다.
- Q34
    
    A company hosts its multi-tier applications on AWS. For compliance, governance, auditing, and security, the company must track configuration changes on its AWS resources and record a history of API calls made to these resources.
    
    What should a solutions architect do to meet these requirements?
    
    - A. Use AWS CloudTrail to track configuration changes and AWS Config to record API calls.
    - B. Use AWS Config to track configuration changes and AWS CloudTrail to record API calls. **Most Voted**
    - C. Use AWS Config to track configuration changes and Amazon CloudWatch to record API calls.
    - D. Use AWS CloudTrail to track configuration changes and Amazon CloudWatch to record API calls.
    
    근거
    
    - 문제 : 리소스 옵션 변경 사항을 추적하고 리소스의 API 콜을 변경하는 기능을 사용하고 싶다.
    - API Call 추적 = Cloudtrail
    - 환경설정 추적 = AWS Configs
- Q35
    
    A company is preparing to launch a public-facing web application in the AWS Cloud. The architecture consists of Amazon EC2 instances within a VPC behind an Elastic Load Balancer (ELB). A third-party service is used for the DNS. The company's solutions architect must recommend a solution to detect and protect against large-scale DDoS attacks.
    
    Which solution meets these requirements?
    
    - A. Enable Amazon GuardDuty on the account.
    - B. Enable Amazon Inspector on the EC2 instances.
    - C. Enable AWS Shield and assign Amazon Route 53 to it.
    - D. Enable AWS Shield Advanced and assign the ELB to it. **Most Voted**
    
    근거
    
    - 문제 : ELB와 EC2, DNS에 대한 서드파티를 사용한다⇒  DDos  공격을 방어하고자 한다.
    - DDos 공격 = AWS shield / 서드파티라 했기에 Route53을 사용하지 않으므로 C는 틀림 / ELB에 AWS shield를 넣어야함.
- Q36
    
    A company is building an application in the AWS Cloud. The application will store data in Amazon S3 buckets in two AWS Regions. The company must use an AWS Key Management Service (AWS KMS) customer managed key to encrypt all data that is stored in the S3 buckets. The data in both S3 buckets must be encrypted and decrypted with the same KMS key. The data and the key must be stored in each of the two Regions.
    
    Which solution will meet these requirements with the LEAST operational overhead?
    
    - A. Create an S3 bucket in each Region. Configure the S3 buckets to use server-side encryption with Amazon S3 managed encryption keys (SSE-S3). Configure replication between the S3 buckets.
    - B. Create a customer managed multi-Region KMS key. Create an S3 bucket in each Region. Configure replication between the S3 buckets. Configure the application to use the KMS key with client-side encryption. **Most Voted**
    - C. Create a customer managed KMS key and an S3 bucket in each Region. Configure the S3 buckets to use server-side encryption with Amazon S3 managed encryption keys (SSE-S3). Configure replication between the S3 buckets.
    - D. Create a customer managed KMS key and an S3 bucket in each Region. Configure the S3 buckets to use server-side encryption with AWS KMS keys (SSE-KMS). Configure replication between the S3 buckets.
    
    근거 
    
    - 문제 : 2개 리전에 S3 버켓을 사용하고 있으며 KMS를 통해 S3 버켓에 있는 정보들이 암호화 되어있다. ⇒ 데이터와 키는 모두 리전에 각각 배치되어 있으며 동일한 Encryption key어야 한다. ⇒ 최소한으로 설정하는 방법은?
    - AWS KMS supports *multi-Region keys*, which are AWS KMS keys in different AWS Regions that can be used interchangeably – as though you had the same key in multiple Regions.(as though = as if)
    - [https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html)
- Q37
    
    A company recently launched a variety of new workloads on Amazon EC2 instances in its AWS account. The company needs to create a strategy to access and administer the instances remotely and securely. The company needs to implement a repeatable process that works with native AWS services and follows the AWS Well-Architected Framework.
    
    Which solution will meet these requirements with the LEAST operational overhead?
    
    - A. Use the EC2 serial console to directly access the terminal interface of each instance for administration.
    - B. Attach the appropriate IAM role to each existing instance and new instance. Use AWS Systems Manager Session Manager to establish a remote SSH session. **Most Voted**
    - C. Create an administrative SSH key pair. Load the public key into each EC2 instance. Deploy a bastion host in a public subnet to provide a tunnel for administration of each instance.
    - D. Establish an AWS Site-to-Site VPN connection. Instruct administrators to use their local on-premises machines to connect directly to the instances by using SSH keys across the VPN tunnel.
    
    근거 
    
    - 문제 : 원격으로 관리하는 방법을 고민중에 있음 ⇒ 회사는 AWS well architected framework를 따르는 프로세스가 필요하다. ⇒ 최소 노력으로 이룰 수 있는 방법은?
    - 세션 매니저를 사용한다.
    - Session Manager provides secure and auditable node management without the need to open inbound ports, maintain bastion hosts, or manage SSH keys.
    - https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html
- Q39
    
    A company maintains a searchable repository of items on its website. The data is stored in an Amazon RDS for MySQL database table that contains more than 10 million rows. The database has 2 TB of General Purpose SSD storage. There are millions of updates against this data every day through the company's website.The company has noticed that some insert operations are taking 10 seconds or longer. The company has determined that the database storage performance is the problem.
    
    Which solution addresses this performance issue?
    
    - A. Change the storage type to Provisioned IOPS SSD. **Most Voted**
    - B. Change the DB instance to a memory optimized instance class.
    - C. Change the DB instance to a burstable performance instance class.
    - D. Enable Multi-AZ RDS read replicas with MySQL native asynchronous replication.
    
    근거
    
    - 문제 : 검색 가능한 레포를 운영중에 있다. ⇒ 이 데이터들은 RDS에서 관리되며 약 1천만건의 로우가 있다. 2TB 크기의 SSD에 저장되어 있으며 수백만건의 트랜잭션이 발생된다. ⇒ 약 10초 이상 걸리는 트랜잭션 타임을 줄이고 싶다.
    - AWS에는 IOPS를 설정하는 옵션이 있다고 한다. 데이터를 삽입하거나 수정해야하므로 IOPS를 건드려야 한다. B를 택했는데, 메모리는 이미 저장된 데이터를 로드하는데 유용한 것으로 판단된다.
    - General purpose SSD is not optimal for database that requires high performance. Answer is A
    - input/output operations per second (IOPS)
    - AWS의 옵션 중에 SSD IOPS 성능을 고르는게 있는듯
        
        [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/provisioned-iops.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/provisioned-iops.html)
        
- Q40
    
    A company has thousands of edge devices that collectively generate 1 TB of status alerts each day. Each alert is approximately 2 KB in size. A solutions architect needs to implement a solution to ingest and store the alerts for future analysis.The company wants a highly available solution. However, the company needs to minimize costs and does not want to manage additional infrastructure. Additionally, the company wants to keep 14 days of data available for immediate analysis and archive any data older than 14 days.What is the MOST operationally efficient solution that meets these requirements?
    
    - A. Create an Amazon Kinesis Data Firehose delivery stream to ingest the alerts. Configure the Kinesis Data Firehose stream to deliver the alerts to an Amazon S3 bucket. Set up an S3 Lifecycle configuration to transition data to Amazon S3 Glacier after 14 days. **Most Voted**
    - B. Launch Amazon EC2 instances across two Availability Zones and place them behind an Elastic Load Balancer to ingest the alerts. Create a script on the EC2 instances that will store the alerts in an Amazon S3 bucket. Set up an S3 Lifecycle configuration to transition data to Amazon S3 Glacier after 14 days.
    - C. Create an Amazon Kinesis Data Firehose delivery stream to ingest the alerts. Configure the Kinesis Data Firehose stream to deliver the alerts to an Amazon OpenSearch Service (Amazon Elasticsearch Service) cluster. Set up the Amazon OpenSearch Service (Amazon Elasticsearch Service) cluster to take manual snapshots every day and delete data from the cluster that is older than 14 days.
    - D. Create an Amazon Simple Queue Service (Amazon SQS) standard queue to ingest the alerts, and set the message retention period to 14 days. Configure consumers to poll the SQS queue, check the age of the message, and analyze the message data as needed. If the message is 14 days old, the consumer should copy the message to an Amazon S3 bucket and delete the message from the SQS queue.
    
    근거 
    
    - 14일 뒤에 데이터를 사용하지 않음 = Glacier
    - 최신 14일치 데이터를 분석해야함 = Amazon kinesis Data Firehose 사용

종료

- Q41
    
    A company's application integrates with multiple software-as-a-service (SaaS) sources for data collection. The company runs Amazon EC2 instances to receive the data and to upload the data to an Amazon S3 bucket for analysis. The same EC2 instance that receives and uploads the data also sends a notification to the user when an upload is complete. The company has noticed slow application performance and wants to improve the performance as much as possible.
    
    Which solution will meet these requirements with the LEAST operational overhead?
    
    - A. Create an Auto Scaling group so that EC2 instances can scale out. Configure an S3 event notification to send events to an Amazon Simple Notification Service (Amazon SNS) topic when the upload to the S3 bucket is complete.
    - B. Create an Amazon AppFlow flow to transfer data between each SaaS source and the S3 bucket. Configure an S3 event notification to send events to an Amazon Simple Notification Service (Amazon SNS) topic when the upload to the S3 bucket is complete. **Most Voted**
    - C. Create an Amazon EventBridge (Amazon CloudWatch Events) rule for each SaaS source to send output data. Configure the S3 bucket as the rule's target. Create a second EventBridge (Cloud Watch Events) rule to send events when the upload to the S3 bucket is complete. Configure an Amazon Simple Notification Service (Amazon SNS) topic as the second rule's target.
    - D. Create a Docker container to use instead of an EC2 instance. Host the containerized application on Amazon Elastic Container Service (Amazon ECS). Configure Amazon CloudWatch Container Insights to send events to an Amazon Simple Notification Service (Amazon SNS) topic when the upload to the S3 bucket is complete.
    
    근거 
    
    - 문제 : 데이터 수집을 위한 도구로 여러 Saas를 사용함.⇒ EC2에서 데이터를 받아 분석을 위해 S3 버켓에 저장 ⇒ 노티피케이션 기능도 추가함 ⇒ 성능이 느린 것을 확인해서 이를 개선하고자 함.
    - APPFLow를 사용한다. 그리고 S3와 SNS를 구성한다.
- Q42
    
    A company runs a highly available image-processing application on Amazon EC2 instances in a single VPC. The EC2 instances run inside several subnets across multiple Availability Zones. The EC2 instances do not communicate with each other. However, the EC2 instances download images from Amazon S3 and upload images to Amazon S3 through a single NAT gateway. The company is concerned about data transfer charges.
    
    What is the MOST cost-effective way for the company to avoid Regional data transfer charges?
    
    - A. Launch the NAT gateway in each Availability Zone.
    - B. Replace the NAT gateway with a NAT instance.
    - C. Deploy a gateway VPC endpoint for Amazon S3. **Most Voted**
    - D. Provision an EC2 Dedicated Host to run the EC2 instances.
    
    근거
    
    - 문제 : 이미지 처리 앱을 운영 ⇒   물리적으로 여러 AZ를 사용하고 여러 subnet을 활용한다.  ⇒ 개별 Ec2는 소통하지 않으며, 개별 ec2는 S3와 상호작용한다. ⇒ S3와 Ec2 간 통신 비용이 걱정된다. ⇒ 가격을 효과적으로 줄일 수 있는 방법은?
    - **NAT gateway보다 gateway VPC endpoint가 가장 저렴하다.**
    - Deploying a gateway VPC endpoint for Amazon S3 is the most cost-effective way for the company to avoid Regional data transfer charges. Data transfer between the VPC and the service through a gateway VPC endpoint is free of charge, while data transfer between the VPC and the Internet through an Internet gateway or NAT device is subject to data transfer charges.
- Q43
    
    A company has an on-premises application that generates a large amount of time-sensitive data that is backed up to Amazon S3. The application has grown and there are user complaints about internet bandwidth limitations. A solutions architect needs to design a long-term solution that allows for both timely backups to Amazon S3 and with minimal impact on internet connectivity for internal users.
    
    Which solution meets these requirements?
    
    - A. Establish AWS VPN connections and proxy all traffic through a VPC gateway endpoint.
    - B. Establish a new AWS Direct Connect connection and direct backup traffic through this new connection. **Most Voted**
    - C. Order daily AWS Snowball devices. Load the data onto the Snowball devices and return the devices to AWS each day.
    - D. Submit a support ticket through the AWS Management Console. Request the removal of S3 service limits from the account.
    
    근거
    
    - TSD 생성하는 앱이 있다. ⇒ 이 TSD는 S3에 저장된다. ⇒ 앱이 빠르게 성장하고 있고 사용자들은 대역폭에 대한 불만이 있음. ⇒ 백업에 인터넷 속도에 영향을 주는 것에 대해서 최소화하고 싶다.
    - A가 안되는 이유 : VPN also goes through the internet and uses the bandwidth.
    - AWS Direct Connect를 써서 인터넷 대역폭을 사용하지 않는 방법을 쓴다.
- Q44
    
    A company has an Amazon S3 bucket that contains critical data. The company must protect the data from accidental deletion.
    
    Which combination of steps should a solutions architect take to meet these requirements? (Choose two.)
    
    - A. Enable versioning on the S3 bucket. **Most Voted**
    - B. Enable MFA Delete on the S3 bucket. **Most Voted**
    - C. Create a bucket policy on the S3 bucket.
    - D. Enable default encryption on the S3 bucket.
    - E. Create a lifecycle policy for the objects in the S3 bucket.
    
    근거
    
    - 문제 : 중요 데이터를 포함한 S3 버켓을 사용중이다. ⇒ 실수에 의해서 제거되는 것에 의해서 방지되어야 함. 가장 필요한 조합은?
    - S3를 백업한다. =  Versioning한다.
    - MFA Delete 기능을 사용한다. Multi-Factor-Authentification 기능
- Q45
    
    A company has a data ingestion workflow that consists of the following:
    
    • An Amazon Simple Notification Service (Amazon SNS) topic for notifications about new data deliveries
    
    • An AWS Lambda function to process the data and record metadata. 
    
    The company observes that the ingestion workflow fails occasionally because of network connectivity issues. When such a failure occurs, the Lambda function does not ingest the corresponding data unless the company manually reruns the job.
    
    Which combination of actions should a solutions architect take to ensure that the Lambda function ingests all data in the future? (Choose two.)
    
    - A. Deploy the Lambda function in multiple Availability Zones.
    - B. Create an Amazon Simple Queue Service (Amazon SQS) queue, and subscribe it to the SNS topic. **Most Voted**
    - C. Increase the CPU and memory that are allocated to the Lambda function.
    - D. Increase provisioned throughput for the Lambda function.
    - E. Modify the Lambda function to read from an Amazon Simple Queue Service (Amazon SQS) queue. **Most Voted**
    
    근거 
    
    - 문제 : SNS와 Lambda function을 이용중인데, 인터넷 연결 문제가 발생하는 경우 때로는 lambda function이 실행되지 않는 경우가 있다. lambda function이 제대로 실행되려면 어떻게 해결해야할까?
    - 탄력성(resiliency)을 보장하기 위해서 SQS를 사용한다. SNS와 연동시킨다. Lambda function을 sqs에 연결 시킨다.
    - E의 경우 작업이 완료되지 않으면 queue에서 제거되지 않으므로 작업을 보장함.
    - B의 경우 문제에서 SNS를 사용한다고 했음.(이걸 기억하지 못해서 A로 택함)
- Q46
    
    A company has an application that provides marketing services to stores. The services are based on previous purchases by store customers. The stores upload transaction data to the company through SFTP, and the data is processed and analyzed to generate new marketing offers. Some of the files can exceed 200 GB in size. Recently, the company discovered that some of the stores have uploaded files that contain personally identifiable information (PII) that should not have been included. The company wants administrators to be alerted if PII is shared again. The company also wants to automate remediation.
    
    What should a solutions architect do to meet these requirements with the LEAST development effort?
    
    - A. Use an Amazon S3 bucket as a secure transfer point. Use Amazon Inspector to scan the objects in the bucket. If objects contain PII, trigger an S3 Lifecycle policy to remove the objects that contain PII.
    - B. Use an Amazon S3 bucket as a secure transfer point. Use Amazon Macie to scan the objects in the bucket. If objects contain PII, use Amazon Simple Notification Service (Amazon SNS) to trigger a notification to the administrators to remove the objects that contain PII. **Most Voted**
    - C. Implement custom scanning algorithms in an AWS Lambda function. Trigger the function when objects are loaded into the bucket. If objects contain PII, use Amazon Simple Notification Service (Amazon SNS) to trigger a notification to the administrators to remove the objects that contain PII.
    - D. Implement custom scanning algorithms in an AWS Lambda function. Trigger the function when objects are loaded into the bucket. If objects contain PII, use Amazon Simple Email Service (Amazon SES) to trigger a notification to the administrators and trigger an S3 Lifecycle policy to remove the meats that contain PII.
    
    근거 
    
    - 문제 : 소규모 가게에 마케팅 서비스를 제공한다. ⇒ 과거 구매 이력을 기반으로 수행하며 소규모 가게들은 정보를 회사에 SFTP 방식으로 업데이트 한다. ⇒ 200GB 넘는 데이터를 전송하며 때로는 개인정보가 포함된 내용을 업로드한다. ⇒ 개인정보 포함이 있을 시 알람이 필요하며, 이를 다시 업로드하도록 지원하고자 한다. ⇒ 가장 필요한 것은?
    - AWS Macie는 AWS에 저장되는 민감 정보를 찾고, 분류하고, 보호하는 보안 서비스이다. 머신러닝을 기반으로 S3에서 민감 정보를 찾아낸다. 예를들면 Personally identifiable information(PII)이 있다.
    - B or D라는 의견이 분분하지만 서비스를 이해하는게 자격증의 핵심이라 생각하기에 AWS MAcie를 사용한 B가 맞다고 본다.
- Q47
    
    A company needs guaranteed Amazon EC2 capacity in three specific Availability Zones in a specific AWS Region for an upcoming event that will last 1 week.
    
    What should the company do to guarantee the EC2 capacity?
    
    - A. Purchase Reserved Instances that specify the Region needed.
    - B. Create an On-Demand Capacity Reservation that specifies the Region needed.
    - C. Purchase Reserved Instances that specify the Region and three Availability Zones needed.
    - D. Create an On-Demand Capacity Reservation that specifies the Region and three Availability Zones needed. **Most Voted**
    
    근거
    
    - 문제 : 1개 리전에서 3개의 AZ에 존재하는 EC2를 1주일간 사용하고 싶다.
    - 
    - Reserved Instances는 존재하지 않는듯?
    - On-Demand Capacity Reservation을 사용해서 특정 AZ 내 서비스를 보존해보자.
- Q48
    
    A company's website uses an Amazon EC2 instance store for its catalog of items. The company wants to make sure that the catalog is highly available and that the catalog is stored in a durable location.
    
    What should a solutions architect do to meet these requirements?
    
    - A. Move the catalog to Amazon ElastiCache for Redis.
    - B. Deploy a larger EC2 instance with a larger instance store.
    - C. Move the catalog from the instance store to Amazon S3 Glacier Deep Archive.
    - D. Move the catalog to an Amazon Elastic File System (Amazon EFS) file system. **Most Voted**
    
    근거 
    
    - 문제 : EC2에 카탈로그를 저장하려고한다. 또한 지속 가능하도록 저장해야한다.
    - durable이고 S3를 사용하지 않으니 EFS를 사용한다.

종료

- Q49
    
    A company stores call transcript files on a monthly basis. Users access the files randomly within 1 year of the call, but users access the files infrequently after 1 year. The company wants to optimize its solution by giving users the ability to query and retrieve files that are less than 1-year-old as quickly as possible. A delay in retrieving older files is acceptable.
    
    Which solution will meet these requirements MOST cost-effectively?
    
    - A. Store individual files with tags in Amazon S3 Glacier Instant Retrieval. Query the tags to retrieve the files from S3 Glacier Instant Retrieval.
    - B. Store individual files in Amazon S3 Intelligent-Tiering. Use S3 Lifecycle policies to move the files to S3 Glacier Flexible Retrieval after 1 year. Query and retrieve the files that are in Amazon S3 by using Amazon Athena. Query and retrieve the files that are in S3 Glacier by using S3 Glacier Select. **Most Voted**
    - C. Store individual files with tags in Amazon S3 Standard storage. Store search metadata for each archive in Amazon S3 Standard storage. Use S3 Lifecycle policies to move the files to S3 Glacier Instant Retrieval after 1 year. Query and retrieve the files by searching for metadata from Amazon S3.
    - D. Store individual files in Amazon S3 Standard storage. Use S3 Lifecycle policies to move the files to S3 Glacier Deep Archive after 1 year. Store search metadata in Amazon RDS. Query the files from Amazon RDS. Retrieve the files from S3 Glacier Deep Archive.
    
    근거
    
    - 문제 : 매달 전화 내용을 저장하고 있으며 1년내 자료는 종종 열람하나 그 이후로는 거의 열람하지 않는다. ⇒ 1년 내 자료를 빠르게 검색할 수 있는 솔루션이 필요하다. ⇒ 그 이후 자료는 검색이 느려도 괜찮다. ⇒ 가장 효과적인 방법은?
    - Intelligent-Tiering을 사용해 비용을 절감한다. S3 Lifecycle policies를 사용해서 1년 지난 자료를 S3 Glacier에 저장한다.
- Q50
    
    A company has a production workload that runs on 1,000 Amazon EC2 Linux instances. The workload is powered by third-party software. The company needs to patch the third-party software on all EC2 instances as quickly as possible to remediate a critical security vulnerability.
    
    What should a solutions architect do to meet these requirements?
    
    - A. Create an AWS Lambda function to apply the patch to all EC2 instances.
    - B. Configure AWS Systems Manager Patch Manager to apply the patch to all EC2 instances.
    - C. Schedule an AWS Systems Manager maintenance window to apply the patch to all EC2 instances.
    - D. Use AWS Systems Manager Run Command to run a custom command that applies the patch to all EC2 instances. **Most Voted**
    
    근거 
    
    - 1000개의 인스턴스를 운영중이며 서드파티앱을 사용한다. 보안 취약점에 대해 모든 인스턴스에 업데이트를 시키고자 한다.
    - AWS Systems manager를 사용한다.
    - 서드파티 앱을 사용하므로 AWS Systems Manager Run Command를 사용해서 custom command를 사용한다.
    - 운영 측면에서 Systems Manager는 수작업 및 스크립트 작성 등이 필요한 유지보수 작업을 돕는 도구로서 다음과 같은 업무를 수행합니다.
        - 온프레미스와 EC2 인스턴스의 패키지 업그레이드
        - 설치 소프트웨어 목록 생성
        - 새 애플리케이션 설치
        - EBS 스냅샷을 이용한 AMI 이미지 생성
        - IAM 인스턴스 프로파일 부착
        - S3 버킷에 대한 퍼블릭 접근 차단
- Q51
    
    A company is developing an application that provides order shipping statistics for retrieval by a REST API. The company wants to extract the shipping statistics, organize the data into an easy-to-read HTML format, and send the report to several email addresses at the same time every morning.
    
    Which combination of steps should a solutions architect take to meet these requirements? (Choose two.)
    
    - A. Configure the application to send the data to Amazon Kinesis Data Firehose.
    - B. Use Amazon Simple Email Service (Amazon SES) to format the data and to send the report by email. **Most Voted**
    - C. Create an Amazon EventBridge (Amazon CloudWatch Events) scheduled event that invokes an AWS Glue job to query the application's API for the data.
    - D. Create an Amazon EventBridge (Amazon CloudWatch Events) scheduled event that invokes an AWS Lambda function to query the application's API for the data. **Most Voted**
    - E. Store the application data in Amazon S3. Create an Amazon Simple Notification Service (Amazon SNS) topic as an S3 event destination to send the report by email
    
    근거 
    
    문제 : rest api 기반 주문 통계 관련 앱을 개발중이다. HTML 포멧으로 조직하고 그 결과를 매일 아침 이메일로 보내는 기능을 만드려고 한다. 
    
    - Simple Email Service 사용 / eventbridge를 사용해서 Lambda function을 스케줄링한다.
    - Event-bridge는 event-driven architecture를 구성하는데 사용하는 서비스이며, 서버리스로 구현된다. 이벤트 브릿지는 scalable, reliable, secure 한 인프라를 제공한다.
- Q54
    
    A company runs multiple Windows workloads on AWS. The company's employees use Windows file shares that are hosted on two Amazon EC2 instances. The file shares synchronize data between themselves and maintain duplicate copies. The company wants a highly available and durable storage solution that preserves how users currently access the files.
    
    What should a solutions architect do to meet these requirements?
    
    - A. Migrate all the data to Amazon S3. Set up IAM authentication for users to access files.
    - B. Set up an Amazon S3 File Gateway. Mount the S3 File Gateway on the existing EC2 instances.
    - C. Extend the file share environment to Amazon FSx for Windows File Server with a Multi-AZ configuration. Migrate all the data to FSx for Windows File Server. **Most Voted**
    - D. Extend the file share environment to Amazon Elastic File System (Amazon EFS) with a Multi-AZ configuration. Migrate all the data to Amazon EFS.
    
    근거 
    
    문제 : 윈도우 워크로드를 사용하고 있으며 2개의 ec2에 파일 쉐어들을 사용하고 있다. 개별 파일쉐어는 데이터를 동기화하고 복제본을 만들어놓는다. ⇒ 접근이 쉽고 오래 지속가능한 파일 쉐어를 만들기 위해 필요한 것은? 
    
    - FSx for windows file server와 for Lustre만 존재함.
    
    - AMAZON FSx가 뭔지 모르겠다.
- Q55
    
    A solutions architect is developing a VPC architecture that includes multiple subnets. The architecture will host applications that use Amazon EC2 instances and Amazon RDS DB instances. The architecture consists of six subnets in two Availability Zones. Each Availability Zone includes a public subnet, a private subnet, and a dedicated subnet for databases. Only EC2 instances that run in the private subnets can have access to the RDS databases.
    
    Which solution will meet these requirements?
    
    - A. Create a new route table that excludes the route to the public subnets' CIDR blocks. Associate the route table with the database subnets.
    - B. Create a security group that denies inbound traffic from the security group that is assigned to instances in the public subnets. Attach the security group to the DB instances.
    - C. Create a security group that allows inbound traffic from the security group that is assigned to instances in the private subnets. Attach the security group to the DB instances. **Most Voted**
    - D. Create a new peering connection between the public subnets and the private subnets. Create a different peering connection between the private subnets and the database subnets.
    
    근거 
    
    - 문제 : 여러 subnet을 구성하고자 함. ⇒ EC2와 RDS를 사용 중임. 2개의 AZ에서 6개의 서브넷을 구성하고 있음. ⇒ public, private, db용 subnet 세가지를 운영 중이며, priviate subnet만이 rbs에 접근 가능하다.
    - db와 private 간 트래픽이 연동될 수 있는 보안 그룹을 만들고 DB에 포함한다.
- Q56
    
    A company has registered its domain name with Amazon Route 53. The company uses Amazon API Gateway in the ca-central-1 Region as a public interface for its backend microservice APIs. Third-party services consume the APIs securely. The company wants to design its API Gateway URL with the company's domain name and corresponding certificate so that the third-party services can use HTTPS.
    
    Which solution will meet these requirements?
    
    - A. Create stage variables in API Gateway with Name="Endpoint-URL" and Value="Company Domain Name" to overwrite the default URL. Import the public certificate associated with the company's domain name into AWS Certificate Manager (ACM).
    - B. Create Route 53 DNS records with the company's domain name. Point the alias record to the Regional API Gateway stage endpoint. Import the public certificate associated with the company's domain name into AWS Certificate Manager (ACM) in the us-east-1 Region.
    - C. Create a Regional API Gateway endpoint. Associate the API Gateway endpoint with the company's domain name. Import the public certificate associated with the company's domain name into AWS Certificate Manager (ACM) in the same Region. Attach the certificate to the API Gateway endpoint. Configure Route 53 to route traffic to the API Gateway endpoint. **Most Voted**
    - D. Create a Regional API Gateway endpoint. Associate the API Gateway endpoint with the company's domain name. Import the public certificate associated with the company's domain name into AWS Certificate Manager (ACM) in the us-east-1 Region. Attach the certificate to the API Gateway APIs. Create Route 53 DNS records with the company's domain name. Point an A record to the company's domain name.
    
    근거 
    
    - 문제 : Route 53에 도메인을 등록해서 사용중이다. ⇒ MSA API의 API gateway를 사용중이다. 그리고 서드파티 앱이 API를 사용중이다. 이 과정을 HTTPS로 보안을 업데이트 하고 싶다.
    - route 53 ⇒ API Gateway endpoint & Attach the certificate to API gateway
    - 외우자…
- Q57
    
    A company is running a popular social media website. The website gives users the ability to upload images to share with other users. The company wants to make sure that the images do not contain inappropriate content. The company needs a solution that minimizes development effort.
    
    What should a solutions architect do to meet these requirements?
    
    - A. Use Amazon Comprehend to detect inappropriate content. Use human review for low-confidence predictions.
    - B. Use Amazon Rekognition to detect inappropriate content. Use human review for low-confidence predictions. **Most Voted**
    - C. Use Amazon SageMaker to detect inappropriate content. Use ground truth to label low-confidence predictions.
    - D. Use AWS Fargate to deploy a custom machine learning model to detect inappropriate content. Use ground truth to label low-confidence predictions.
    
    근거 
    
    문제 : 소셜 웹 운영 중이다. ⇒ 이미지 업로드가 가능하다. ⇒ 부적절한 콘텐츠 필터링이 필요하다.  ⇒ 최소한의 노력으로 만들 수 있는 방법은?
    
    - AWS rekognition은 머신러닝 기반으로 이미지 또는 영상을 분석하는 서비스를 말함. 물체, 사람, 텍스트, 배경, 부적절한 콘텐츠 등을 구분하는데 사용함.
- Q58
    
    A company wants to run its critical applications in containers to meet requirements for scalability and availability. The company prefers to focus on maintenance of the critical applications. The company does not want to be responsible for provisioning and managing the underlying infrastructure that runs the containerized workload.
    
    What should a solutions architect do to meet these requirements?
    
    - A. Use Amazon EC2 instances, and install Docker on the instances.
    - B. Use Amazon Elastic Container Service (Amazon ECS) on Amazon EC2 worker nodes.
    - C. Use Amazon Elastic Container Service (Amazon ECS) on AWS Fargate. **Most Voted**
    - D. Use Amazon EC2 instances from an Amazon Elastic Container Service (Amazon ECS)-optimized Amazon Machine Image (AMI).
    
    근거 
    
    - 문제 : scalability and availability를 충족하는 컨테이너 기반 앱을 운영하고자 한다. ⇒ 인프라 관리를 원치 않는다.
    - 컨테이너 = ECS,
    - FarGate : 컨테이너용 서버리스 컴퓨팅 엔진으로, Amazon ECS와 Amazon EKS에서 작동합니다.
- Q59
    
    A company hosts more than 300 global websites and applications. The company requires a platform to analyze more than 30 TB of clickstream data each day.
    
    What should a solutions architect do to transmit and process the clickstream data?
    
    - A. Design an AWS Data Pipeline to archive the data to an Amazon S3 bucket and run an Amazon EMR cluster with the data to generate analytics.
    - B. Create an Auto Scaling group of Amazon EC2 instances to process the data and send it to an Amazon S3 data lake for Amazon Redshift to use for analysis.
    - C. Cache the data to Amazon CloudFront. Store the data in an Amazon S3 bucket. When an object is added to the S3 bucket. run an AWS Lambda function to process the data for analysis.
    - D. Collect the data from Amazon Kinesis Data Streams. Use Amazon Kinesis Data Firehose to transmit the data to an Amazon S3 data lake. Load the data in Amazon Redshift for analysis. **Most Voted**
    
    근거 
    
    - 문제 : 300개 넘는 웹 사이트와 앱을 운영중임. ⇒ 30 테라 크기의 클릭 스트림을 분석해야하는 플랫폼 필요
    - clicks tream ⇒ Kinesis Data Streams, Data Firehose
    - Redshift = warehouse

종료

- Q61
    
    A company is developing a two-tier web application on AWS. The company's developers have deployed the application on an Amazon EC2 instance that connects directly to a backend Amazon RDS database. The company must not hardcode database credentials in the application. The company must also implement a solution to automatically rotate the database credentials on a regular basis.Which solution will meet these requirements with the LEAST operational overhead?
    
    - A. Store the database credentials in the instance metadata. Use Amazon EventBridge (Amazon CloudWatch Events) rules to run a scheduled AWS Lambda function that updates the RDS credentials and instance metadata at the same time.
    - B. Store the database credentials in a configuration file in an encrypted Amazon S3 bucket. Use Amazon EventBridge (Amazon CloudWatch Events) rules to run a scheduled AWS Lambda function that updates the RDS credentials and the credentials in the configuration file at the same time. Use S3 Versioning to ensure the ability to fall back to previous values.
    - C. Store the database credentials as a secret in AWS Secrets Manager. Turn on automatic rotation for the secret. Attach the required permission to the EC2 role to grant access to the secret. **Most Voted**
    - D. Store the database credentials as encrypted parameters in AWS Systems Manager Parameter Store. Turn on automatic rotation for the encrypted parameters. Attach the required permission to the EC2 role to grant access to the encrypted parameters.
    
    근거 
    
    - C인 것 같다 생각은 했지만 왜 C인지 생각해봐야할듯
- Q62
    
    A company is deploying a new public web application to AWS. The application will run behind an Application Load Balancer (ALB). The application needs to be encrypted at the edge with an SSL/TLS certificate that is issued by an external certificate authority (CA). The certificate must be rotated each year before the certificate expires.What should a solutions architect do to meet these requirements?
    
    - A. Use AWS Certificate Manager (ACM) to issue an SSL/TLS certificate. Apply the certificate to the ALB. Use the managed renewal feature to automatically rotate the certificate.
    - B. Use AWS Certificate Manager (ACM) to issue an SSL/TLS certificate. Import the key material from the certificate. Apply the certificate to the ALUse the managed renewal feature to automatically rotate the certificate.
    - C. Use AWS Certificate Manager (ACM) Private Certificate Authority to issue an SSL/TLS certificate from the root CA. Apply the certificate to the ALB. Use the managed renewal feature to automatically rotate the certificate.
    - D. Use AWS Certificate Manager (ACM) to import an SSL/TLS certificate. Apply the certificate to the ALB. Use Amazon EventBridge (Amazon CloudWatch Events) to send a notification when the certificate is nearing expiration. Rotate the certificate manually. **Most Voted**
    
    근거 
    
    - 외부에서 발급 받아야하는 조건이 있기 때문에 D 같다.
    - It's a third-party certificate, hence AWS cannot manage renewal automatically. The closest thing you can do is to send a notification to renew the 3rd party certificate.
- Q63
    
    A company runs its infrastructure on AWS and has a registered base of 700,000 users for its document management application. The company intends to create a product that converts large .pdf files to .jpg image files. The .pdf files average 5 MB in size. The company needs to store the original files and the converted files. A solutions architect must design a scalable solution to accommodate demand that will grow rapidly over time.Which solution meets these requirements MOST cost-effectively?
    
    - A. Save the .pdf files to Amazon S3. Configure an S3 PUT event to invoke an AWS Lambda function to convert the files to .jpg format and store them back in Amazon S3. **Most Voted**
    - B. Save the .pdf files to Amazon DynamoDUse the DynamoDB Streams feature to invoke an AWS Lambda function to convert the files to .jpg format and store them back in DynamoDB.
    - C. Upload the .pdf files to an AWS Elastic Beanstalk application that includes Amazon EC2 instances, Amazon Elastic Block Store (Amazon EBS) storage, and an Auto Scaling group. Use a program in the EC2 instances to convert the files to .jpg format. Save the .pdf files and the .jpg files in the EBS store.
    - D. Upload the .pdf files to an AWS Elastic Beanstalk application that includes Amazon EC2 instances, Amazon Elastic File System (Amazon EFS) storage, and an Auto Scaling group. Use a program in the EC2 instances to convert the file to .jpg format. Save the .pdf files and the .jpg files in the EBS store.
    
    근거 
    
    - B가 안되는 이유는 DynamoDB의 최대 용량은 400kb임.
- Q64
    
    A company has more than 5 TB of file data on Windows file servers that run on premises. Users and applications interact with the data each day.The company is moving its Windows workloads to AWS. As the company continues this process, the company requires access to AWS and on-premises file storage with minimum latency. The company needs a solution that minimizes operational overhead and requires no significant changes to the existing file access patterns. The company uses an AWS Site-to-Site VPN connection for connectivity to AWS.What should a solutions architect do to meet these requirements?
    
    - A. Deploy and configure Amazon FSx for Windows File Server on AWS. Move the on-premises file data to FSx for Windows File Server. Reconfigure the workloads to use FSx for Windows File Server on AWS.
    - B. Deploy and configure an Amazon S3 File Gateway on premises. Move the on-premises file data to the S3 File Gateway. Reconfigure the on-premises workloads and the cloud workloads to use the S3 File Gateway.
    - C. Deploy and configure an Amazon S3 File Gateway on premises. Move the on-premises file data to Amazon S3. Reconfigure the workloads to use either Amazon S3 directly or the S3 File Gateway. depending on each workload's location.
    - D. Deploy and configure Amazon FSx for Windows File Server on AWS. Deploy and configure an Amazon FSx File Gateway on premises. Move the on-premises file data to the FSx File Gateway. Configure the cloud workloads to use FSx for Windows File Server on AWS. Configure the on-premises workloads to use the FSx File Gateway. **Most Voted**
    
    근거 
    
    - 몰겠음
- Q65
    
    A hospital recently deployed a RESTful API with Amazon API Gateway and AWS Lambda. The hospital uses API Gateway and Lambda to upload reports that are in PDF format and JPEG format. The hospital needs to modify the Lambda code to identify protected health information (PHI) in the reports.Which solution will meet these requirements with the LEAST operational overhead?
    
    - A. Use existing Python libraries to extract the text from the reports and to identify the PHI from the extracted text.
    - B. Use Amazon Textract to extract the text from the reports. Use Amazon SageMaker to identify the PHI from the extracted text.
    - C. Use Amazon Textract to extract the text from the reports. Use Amazon Comprehend Medical to identify the PHI from the extracted text. **Most Voted**
    - D. Use Amazon Rekognition to extract the text from the reports. Use Amazon Comprehend Medical to identify the PHI from the extracted text.
    
    근거 :
    
    - Amazon Textract가 무엇인지,
    - Amazon Comprehend가 무엇인지
- Q66
    
    A company has an application that generates a large number of files, each approximately 5 MB in size. The files are stored in Amazon S3. Company policy requires the files to be stored for 4 years before they can be deleted. Immediate accessibility is always required as the files contain critical business data that is not easy to reproduce. The files are frequently accessed in the first 30 days of the object creation but are rarely accessed after the first 30 days.Which storage solution is MOST cost-effective?
    
    - A. Create an S3 bucket lifecycle policy to move files from S3 Standard to S3 Glacier 30 days from object creation. Delete the files 4 years after object creation. **Most Voted**
    - B. Create an S3 bucket lifecycle policy to move files from S3 Standard to S3 One Zone-Infrequent Access (S3 One Zone-IA) 30 days from object creation. Delete the files 4 years after object creation.
    - C. Create an S3 bucket lifecycle policy to move files from S3 Standard to S3 Standard-Infrequent Access (S3 Standard-IA) 30 days from object creation. Delete the files 4 years after object creation. **Most Voted**
    - D. Create an S3 bucket lifecycle policy to move files from S3 Standard to S3 Standard-Infrequent Access (S3 Standard-IA) 30 days from object creation. Move the files to S3 Glacier 4 years after object creation.
    
    근거 
    
    - Cost effective임을 고려해야함.
    - D를 택했는데, 제거 가능하다고 언급되었으니 4년 뒤에 제거하는게 가장 효과적인 방법임.
- Q67
    
    A company hosts an application on multiple Amazon EC2 instances. The application processes messages from an Amazon SQS queue, writes to an Amazon RDS table, and deletes the message from the queue. Occasional duplicate records are found in the RDS table. The SQS queue does not contain any duplicate messages.What should a solutions architect do to ensure messages are being processed once only?
    
    - A. Use the CreateQueue API call to create a new queue.
    - B. Use the AddPermission API call to add appropriate permissions.
    - C. Use the ReceiveMessage API call to set an appropriate wait time.
    - D. Use the ChangeMessageVisibility API call to increase the visibility timeout. **Most Voted**
    
    근거 
    
    ChangeMessageVisibility API가 무엇인지
    
- Q69
    
    A company is running a business-critical web application on Amazon EC2 instances behind an Application Load Balancer. The EC2 instances are in an Auto Scaling group. The application uses an Amazon Aurora PostgreSQL database that is deployed in a single Availability Zone. The company wants the application to be highly available with minimum downtime and minimum loss of data.Which solution will meet these requirements with the LEAST operational effort?
    
    - A. Place the EC2 instances in different AWS Regions. Use Amazon Route 53 health checks to redirect traffic. Use Aurora PostgreSQL Cross-Region Replication.
    - B. Configure the Auto Scaling group to use multiple Availability Zones. Configure the database as Multi-AZ. Configure an Amazon RDS Proxy instance for the database. **Most Voted**
    - C. Configure the Auto Scaling group to use one Availability Zone. Generate hourly snapshots of the database. Recover the database from the snapshots in the event of a failure.
    - D. Configure the Auto Scaling group to use multiple AWS Regions. Write the data from the application to Amazon S3. Use S3 Event Notifications to launch an AWS Lambda function to write the data to the database.
    
    근거 
    
    - 몰겠다.
- Q70
    
    A company's HTTP application is behind a Network Load Balancer (NLB). The NLB's target group is configured to use an Amazon EC2 Auto Scaling group with multiple EC2 instances that run the web service.The company notices that the NLB is not detecting HTTP errors for the application. These errors require a manual restart of the EC2 instances that run the web service. The company needs to improve the application's availability without writing custom scripts or code.What should a solutions architect do to meet these requirements?
    
    - A. Enable HTTP health checks on the NLB, supplying the URL of the company's application.
    - B. Add a cron job to the EC2 instances to check the local application's logs once each minute. If HTTP errors are detected. the application will restart.
    - C. Replace the NLB with an Application Load Balancer. Enable HTTP health checks by supplying the URL of the company's application. Configure an Auto Scaling action to replace unhealthy instances. **Most Voted**
    - D. Create an Amazon Cloud Watch alarm that monitors the UnhealthyHostCount metric for the NLB. Configure an Auto Scaling action to replace unhealthy instances when the alarm is in the ALARM state.
    
    근거 
    
    - 잘 모르겠다.

종료

- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
- Q
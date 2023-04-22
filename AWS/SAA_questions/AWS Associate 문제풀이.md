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
    
    A company is developing a two-tier web application on AWS. The company's developers have deployed the application on an Amazon EC2 instance that connects directly to a backend Amazon RDS database. The company must not hardcode database credentials in the application. The company must also implement a solution to automatically rotate the database credentials on a regular basis.
    
    Which solution will meet these requirements with the LEAST operational overhead?
    
    - A. Store the database credentials in the instance metadata. Use Amazon EventBridge (Amazon CloudWatch Events) rules to run a scheduled AWS Lambda function that updates the RDS credentials and instance metadata at the same time.
    - B. Store the database credentials in a configuration file in an encrypted Amazon S3 bucket. Use Amazon EventBridge (Amazon CloudWatch Events) rules to run a scheduled AWS Lambda function that updates the RDS credentials and the credentials in the configuration file at the same time. Use S3 Versioning to ensure the ability to fall back to previous values.
    - C. Store the database credentials as a secret in AWS Secrets Manager. Turn on automatic rotation for the secret. Attach the required permission to the EC2 role to grant access to the secret. **Most Voted**
    - D. Store the database credentials as encrypted parameters in AWS Systems Manager Parameter Store. Turn on automatic rotation for the encrypted parameters. Attach the required permission to the EC2 role to grant access to the encrypted parameters.
    
    근거 
    
    - 문제 : RDS와 EC2가 연동된 앱을 배포중임. db 크리덴셜을 하드코드가 아닌 자동으로 변경시키고 싶음
    - AWS Secrets Manager 사용. 이때 Secret을 업데이트 하도록 해야해서 C임. D는 Encrypted parameters를 업데이트 해야한다고 해서 틀림
- Q62
    
    A company is deploying a new public web application to AWS. The application will run behind an Application Load Balancer (ALB). The application needs to be encrypted at the edge with an SSL/TLS certificate that is issued by an external certificate authority (CA). The certificate must be rotated each year before the certificate expires.
    
    What should a solutions architect do to meet these requirements?
    
    - A. Use AWS Certificate Manager (ACM) to issue an SSL/TLS certificate. Apply the certificate to the ALB. Use the managed renewal feature to automatically rotate the certificate.
    - B. Use AWS Certificate Manager (ACM) to issue an SSL/TLS certificate. Import the key material from the certificate. Apply the certificate to the ALUse the managed renewal feature to automatically rotate the certificate.
    - C. Use AWS Certificate Manager (ACM) Private Certificate Authority to issue an SSL/TLS certificate from the root CA. Apply the certificate to the ALB. Use the managed renewal feature to automatically rotate the certificate.
    - D. Use AWS Certificate Manager (ACM) to import an SSL/TLS certificate. Apply the certificate to the ALB. Use Amazon EventBridge (Amazon CloudWatch Events) to send a notification when the certificate is nearing expiration. Rotate the certificate manually. **Most Voted**
    
    근거 
    
    - 문제 : ALB 뒤에서 EC2가 작동중임. TLS 통신이 필요함. ⇒ Certificate를 매년 교체해야함.
    - 외부에서 발급받는 Cert이기 때문에 업데이트를 수동으로 해야한다.
    - It's a third-party certificate, hence AWS cannot manage renewal automatically. The closest thing you can do is to send a notification to renew the 3rd party certificate.
- Q63
    
    A company runs its infrastructure on AWS and has a registered base of 700,000 users for its document management application. The company intends to create a product that converts large .pdf files to .jpg image files. The .pdf files average 5 MB in size. The company needs to store the original files and the converted files. A solutions architect must design a scalable solution to accommodate demand that will grow rapidly over time.
    
    Which solution meets these requirements MOST cost-effectively?
    
    - A. Save the .pdf files to Amazon S3. Configure an S3 PUT event to invoke an AWS Lambda function to convert the files to .jpg format and store them back in Amazon S3. **Most Voted**
    - B. Save the .pdf files to Amazon DynamoD. Use the DynamoDB Streams feature to invoke an AWS Lambda function to convert the files to .jpg format and store them back in DynamoDB.
    - C. Upload the .pdf files to an AWS Elastic Beanstalk application that includes Amazon EC2 instances, Amazon Elastic Block Store (Amazon EBS) storage, and an Auto Scaling group. Use a program in the EC2 instances to convert the files to .jpg format. Save the .pdf files and the .jpg files in the EBS store.
    - D. Upload the .pdf files to an AWS Elastic Beanstalk application that includes Amazon EC2 instances, Amazon Elastic File System (Amazon EFS) storage, and an Auto Scaling group. Use a program in the EC2 instances to convert the file to .jpg format. Save the .pdf files and the .jpg files in the EBS store.
    
    근거 
    
    - 70만 사용자가 있으며, pdf → jpg 파일로 변환하는 앱임. ⇒ 평균 5메가 pdf 파일이며 변환 전 파일과 후 파일 모두를 보관함. ⇒ 확장 가능해야하며 가장 가격이 효과적인 방법은?
    - S3 버켓을 사용하는 것이 가장 효과적인 방법이므로 A이다.
    - B가 안되는 이유는 DynamoDB의 최대 용량은 400kb임.
- Q64
    
    A company has more than 5 TB of file data on Windows file servers that run on premises. Users and applications interact with the data each day.The company is moving its Windows workloads to AWS. As the company continues this process, the company requires access to AWS and on-premises file storage with minimum latency. The company needs a solution that minimizes operational overhead and requires no significant changes to the existing file access patterns. The company uses an AWS Site-to-Site VPN connection for connectivity to AWS.
    
    What should a solutions architect do to meet these requirements?
    
    - A. Deploy and configure Amazon FSx for Windows File Server on AWS. Move the on-premises file data to FSx for Windows File Server. Reconfigure the workloads to use FSx for Windows File Server on AWS.
    - B. Deploy and configure an Amazon S3 File Gateway on premises. Move the on-premises file data to the S3 File Gateway. Reconfigure the on-premises workloads and the cloud workloads to use the S3 File Gateway.
    - C. Deploy and configure an Amazon S3 File Gateway on premises. Move the on-premises file data to Amazon S3. Reconfigure the workloads to use either Amazon S3 directly or the S3 File Gateway. depending on each workload's location.
    - D. Deploy and configure Amazon FSx for Windows File Server on AWS. Deploy and configure an Amazon FSx File Gateway on premises. Move the on-premises file data to the FSx File Gateway. Configure the cloud workloads to use FSx for Windows File Server on AWS. Configure the on-premises workloads to use the FSx File Gateway. **Most Voted**
    
    근거 
    
    - 문제 : 5tb 크기의 Windows file server를 온프레미스로 운영 중이다. ⇒ windows workload를 AWS로 옮기려고 한다. ⇒ 자료를 옮기는 동안 파일 저장소에 low-latency로 접근이 가능해야한다. ⇒ 오버헤드를 최소화하고, 접근 패턴의 차이도 큰 변화가 없어야한다. ⇒ VPN을 활용해 AWS와 연동중이다.
    - windows file server이기 때문에 FSx를 쓰는게 좋은 방법이다. ⇒ FSx 파일 게이트웨이를 만든다. ⇒ 파일 게이트웨이와 온프레미스 워크로드를 합친다.
    - Amazon FSx File Gateway (FSx File Gateway) is a new File Gateway type that provides low latency and efficient access to in-cloud FSx for Windows File Server file shares from your on-premises facility.
- Q65
    
    A hospital recently deployed a RESTful API with Amazon API Gateway and AWS Lambda. The hospital uses API Gateway and Lambda to upload reports that are in PDF format and JPEG format. The hospital needs to modify the Lambda code to identify protected health information (PHI) in the reports.
    
    Which solution will meet these requirements with the LEAST operational overhead?
    
    - A. Use existing Python libraries to extract the text from the reports and to identify the PHI from the extracted text.
    - B. Use Amazon Textract to extract the text from the reports. Use Amazon SageMaker to identify the PHI from the extracted text.
    - C. Use Amazon Textract to extract the text from the reports. Use Amazon Comprehend Medical to identify the PHI from the extracted text. **Most Voted**
    - D. Use Amazon Rekognition to extract the text from the reports. Use Amazon Comprehend Medical to identify the PHI from the extracted text.
    
    근거 :
    
    - 문제 : pdf, jpg 양식의 보고서를 업데이트 하기위해 API Gateway와 Lambda를 사용한다. 리프토에 PHI를 보호해야한다. ⇒ 최소한의 방법은?
    - Amazon Textract : text 추출 OCR
    - Amazon Comprehend : text에서 insight를 추출함. 문제에서는 phi를 위한 용도
- Q66
    
    A company has an application that generates a large number of files, each approximately 5 MB in size. The files are stored in Amazon S3. Company policy requires the files to be stored for 4 years before they can be deleted. Immediate accessibility is always required as the files contain critical business data that is not easy to reproduce. The files are frequently accessed in the first 30 days of the object creation but are rarely accessed after the first 30 days.
    
    Which storage solution is MOST cost-effective?
    
    - A. Create an S3 bucket lifecycle policy to move files from S3 Standard to S3 Glacier 30 days from object creation. Delete the files 4 years after object creation. **Most Voted**
    - B. Create an S3 bucket lifecycle policy to move files from S3 Standard to S3 One Zone-Infrequent Access (S3 One Zone-IA) 30 days from object creation. Delete the files 4 years after object creation.
    - C. Create an S3 bucket lifecycle policy to move files from S3 Standard to S3 Standard-Infrequent Access (S3 Standard-IA) 30 days from object creation. Delete the files 4 years after object creation. **Most Voted**
    - D. Create an S3 bucket lifecycle policy to move files from S3 Standard to S3 Standard-Infrequent Access (S3 Standard-IA) 30 days from object creation. Move the files to S3 Glacier 4 years after object creation.
    
    근거 
    
    - 문제 : 5mb 이상의 큰 파일을 생성하는 앱을 운영 중 ⇒ S3에 저장되어 있으며, 4년이 지나야 제거할 수 있음. ⇒ 즉각 접근 가능해야한다. ⇒ 처음 30일은 빈번하게 사용되지만, 그 이후로는 거의 쓰이지 않는다. ⇒ 가장 비용 절감할 수 있는 방법은?
    - S3 standard ⇒ S3 Glaicer로 이동하고 4년 뒤 제거
    - D를 택했는데, 틀린 이유는 1. Standard-IA 비용이 Glacier보다 비쌈. 물론 Glacier에서도 검색이 가능하다. 2. 4년이 지나면 지우는게 비용 절감면에 있어서 좋음
- Q67
    
    A company hosts an application on multiple Amazon EC2 instances. The application processes messages from an Amazon SQS queue, writes to an Amazon RDS table, and deletes the message from the queue. Occasional duplicate records are found in the RDS table. The SQS queue does not contain any duplicate messages.
    
    What should a solutions architect do to ensure messages are being processed once only?
    
    - A. Use the CreateQueue API call to create a new queue.
    - B. Use the AddPermission API call to add appropriate permissions.
    - C. Use the ReceiveMessage API call to set an appropriate wait time.
    - D. Use the ChangeMessageVisibility API call to increase the visibility timeout. **Most Voted**
    
    근거 
    
    - 문제 : SQS를 사용하고, RDS 테이블에 쓴 다음, SQS에서 메세지를 제거하는 식으로 돌아가는 앱이 있음 ⇒ 때로는 RDS에서 복제된 row가 있는데, SQS에서 복제된 메세지가 있는건 아님 ⇒ 중복을 방지하기 위해서는?
    - ChangeMessageVisibility API를 사용한다. To prevent other consumers from processing the message again, Amazon SQS sets a *visibility timeout*, a period of time during which Amazon SQS prevents all consumers from receiving and processing the message.
- Q69
    
    A company is running a business-critical web application on Amazon EC2 instances behind an Application Load Balancer. The EC2 instances are in an Auto Scaling group. The application uses an Amazon Aurora PostgreSQL database that is deployed in a single Availability Zone. The company wants the application to be highly available with minimum downtime and minimum loss of data.
    
    Which solution will meet these requirements with the LEAST operational effort?
    
    - A. Place the EC2 instances in different AWS Regions. Use Amazon Route 53 health checks to redirect traffic. Use Aurora PostgreSQL Cross-Region Replication.
    - B. Configure the Auto Scaling group to use multiple Availability Zones. Configure the database as Multi-AZ. Configure an Amazon RDS Proxy instance for the database. **Most Voted**
    - C. Configure the Auto Scaling group to use one Availability Zone. Generate hourly snapshots of the database. Recover the database from the snapshots in the event of a failure.
    - D. Configure the Auto Scaling group to use multiple AWS Regions. Write the data from the application to Amazon S3. Use S3 Event Notifications to launch an AWS Lambda function to write the data to the database.
    
    근거 
    
    - 문제 : ALB 뒤에 ec2 사용 중 ⇒ EC2는 Autoscaling이 되어 있음. ⇒ Single AZ 기반의 Postgre Aurora를 사용 중 ⇒ 최소 손실, 최소 downtime(작동하지 않는 시간)이 필요함. ⇒ 가장 효과적인 방법은?
    - EC2와 DB를 여러 AZ로 두어서 안정성을 확보해야함.
- Q70
    
    A company's HTTP application is behind a Network Load Balancer (NLB). The NLB's target group is configured to use an Amazon EC2 Auto Scaling group with multiple EC2 instances that run the web service. The company notices that the NLB is not detecting HTTP errors for the application. These errors require a manual restart of the EC2 instances that run the web service. The company needs to improve the application's availability without writing custom scripts or code.
    
    What should a solutions architect do to meet these requirements?
    
    - A. Enable HTTP health checks on the NLB, supplying the URL of the company's application.
    - B. Add a cron job to the EC2 instances to check the local application's logs once each minute. If HTTP errors are detected. the application will restart.
    - C. Replace the NLB with an Application Load Balancer. Enable HTTP health checks by supplying the URL of the company's application. Configure an Auto Scaling action to replace unhealthy instances. **Most Voted**
    - D. Create an Amazon Cloud Watch alarm that monitors the UnhealthyHostCount metric for the NLB. Configure an Auto Scaling action to replace unhealthy instances when the alarm is in the ALARM state.
    
    근거 
    
    - 문제 : NLB를 운영중이며 개별 그룹은  EC2 auto scaling 그룹으로도 설정되어 있음 ⇒ NLB가 HTTP Errors를 탐지하지 못하고 있는 문제를 발견했다. ⇒ 이러한 에러를 처리하기 위해선 EC2를 재시작 해야한다. ⇒ 코드 작성 없이 이 문제를 해결하는 방법은?
    - NLB를 ALB로 교체한다. ALB의 HTTP health check을 사용한다. Auto scaling을 통해 unhealthy instance를 교체한다.
- Q71
    
    A company runs a shopping application that uses Amazon DynamoDB to store customer information. In case of data corruption, a solutions architect needs to design a solution that meets a recovery point objective (RPO) of 15 minutes and a recovery time objective (RTO) of 1 hour.What should the solutions architect recommend to meet these requirements?
    
    - A. Configure DynamoDB global tables. For RPO recovery, point the application to a different AWS Region.
    - B. Configure DynamoDB point-in-time recovery. For RPO recovery, restore to the desired point in time. **Most Voted**
    - C. Export the DynamoDB data to Amazon S3 Glacier on a daily basis. For RPO recovery, import the data from S3 Glacier to DynamoDB.
    - D. Schedule Amazon Elastic Block Store (Amazon EBS) snapshots for the DynamoDB table every 15 minutes. For RPO recovery, restore the DynamoDB table by using the EBS snapshot.
    
    근거 
    
    - 문제 : Dynamo DB를 운영중임. ⇒ a recovery point objective(RPO)를 15분, a recovery time objective(RTO)를 1시간으로 설정해야함.
    - DynamoDB의 point-in-time recovery를 사용하면 해결 가능
- Q72
    
    A company runs a photo processing application that needs to frequently upload and download pictures from Amazon S3 buckets that are located in the same AWS Region. A solutions architect has noticed an increased cost in data transfer fees and needs to implement a solution to reduce these costs.How can the solutions architect meet this requirement?
    
    - A. Deploy Amazon API Gateway into a public subnet and adjust the route table to route S3 calls through it.
    - B. Deploy a NAT gateway into a public subnet and attach an endpoint policy that allows access to the S3 buckets.
    - C. Deploy the application into a public subnet and allow it to route through an internet gateway to access the S3 buckets.
    - D. Deploy an S3 VPC gateway endpoint into the VPC and attach an endpoint policy that allows access to the S3 buckets.
    
    근거 :
    
    - 문제 : S3 버켓에 파일 업로드, 다운로드가 빈번함 ⇒ 데이터 전송 비용이 증가함에 따라 해결책이 필요함.
    - VPC endpoints는 외부 인터넷 전송 서비스를 타지 않고 백본 네트워크를 통해 접근할 수 있도록 지원한다. 인터넷을 타지 않기 때문에 가장 저렴한 방법이라 한다.
    - VPC Endpoint는 유료이며 약 $10/월 정도 고정 비용과 $3.5/1TB의 트래픽 비용이 발생합니다
- Q73
    
    A company recently launched Linux-based application instances on Amazon EC2 in a private subnet and launched a Linux-based bastion host on an Amazon EC2 instance in a public subnet of a VPC. A solutions architect needs to connect from the on-premises network, through the company's internet connection, to the bastion host, and to the application servers. The solutions architect must make sure that the security groups of all the EC2 instances will allow that access.Which combination of steps should the solutions architect take to meet these requirements? (Choose two.)
    
    - A. Replace the current security group of the bastion host with one that only allows inbound access from the application instances.
    - B. Replace the current security group of the bastion host with one that only allows inbound access from the internal IP range for the company.
    - C. Replace the current security group of the bastion host with one that only allows inbound access from the external IP range for the company. **Most Voted**
    - D. Replace the current security group of the application instances with one that allows inbound SSH access from only the private IP address of the bastion host. **Most Voted**
    - E. Replace the current security group of the application instances with one that allows inbound SSH access from only the public IP address of the bastion host.
    
    근거
    
    - 문제 : private subnet에 EC2와 Public subnet에 EC2를 운영 중. public subnet은 bastion host 용도로 사용. ⇒ 온프레미스 네트워크를 바스티온 호스트와 앱 서버에 연결하려고함 ⇒ 모든 연결이 확실히 하려면?
    - bastion과 외부 연결 : 현재 security group을 회사의 외부 IP에 엑세스하도록 설정
    - app서버와 bastion 연결 :  SSH로 private IP address를 연결
    - 
- Q74
    
    A solutions architect is designing a two-tier web application. The application consists of a public-facing web tier hosted on Amazon EC2 in public subnets. The database tier consists of Microsoft SQL Server running on Amazon EC2 in a private subnet. Security is a high priority for the company.How should security groups be configured in this situation? (Choose two.)
    
    - A. Configure the security group for the web tier to allow inbound traffic on port 443 from 0.0.0.0/0. **Most Voted**
    - B. Configure the security group for the web tier to allow outbound traffic on port 443 from 0.0.0.0/0.
    - C. Configure the security group for the database tier to allow inbound traffic on port 1433 from the security group for the web tier. **Most Voted**
    - D. Configure the security group for the database tier to allow outbound traffic on ports 443 and 1433 to the security group for the web tier.
    - E. Configure the security group for the database tier to allow inbound traffic on ports 443 and 1433 from the security group for the web tier.
    
    근거 :
    
    - 문제 : public으로 web을 운영중 ⇒  private로 microsoft SQL을 운영 중 ⇒ 보안이 최우선일 때 설정해야하는 것은?
    - 1. inbound를 443으로 설정해서 https를 사용
    - 2. web에서 오는 1433을 허용한다. (MS SQL Default port)
- Q75
    
    A company wants to move a multi-tiered application from on premises to the AWS Cloud to improve the application's performance. The application consists of application tiers that communicate with each other by way of RESTful services. Transactions are dropped when one tier becomes overloaded. A solutions architect must design a solution that resolves these issues and modernizes the application.Which solution meets these requirements and is the MOST operationally efficient?
    
    - A. Use Amazon API Gateway and direct transactions to the AWS Lambda functions as the application layer. Use Amazon Simple Queue Service (Amazon SQS) as the communication layer between application services. **Most Voted**
    - B. Use Amazon CloudWatch metrics to analyze the application performance history to determine the servers' peak utilization during the performance failures. Increase the size of the application server's Amazon EC2 instances to meet the peak requirements.
    - C. Use Amazon Simple Notification Service (Amazon SNS) to handle the messaging between application servers running on Amazon EC2 in an Auto Scaling group. Use Amazon CloudWatch to monitor the SNS queue length and scale up and down as required.
    - D. Use Amazon Simple Queue Service (Amazon SQS) to handle the messaging between application servers running on Amazon EC2 in an Auto Scaling group. Use Amazon CloudWatch to monitor the SQS queue length and scale up when communication failures are detected.
    
    근거
    
    - 문제: 온프레미스에서 AWS로 옮기려고 함 ⇒ 과부화 되면 트랜잭션이 느려짐 ⇒ 가장 운영 효과적으로 해결하기 위한 방법은?
    - Lambda = Serverless & Autoscaling 가능
    - SQS = scalability에 최적
- Q76
    
    A company receives 10 TB of instrumentation data each day from several machines located at a single factory. The data consists of JSON files stored on a storage area network (SAN) in an on-premises data center located within the factory. The company wants to send this data to Amazon S3 where it can be accessed by several additional systems that provide critical near-real-time analytics. A secure transfer is important because the data is considered sensitive.Which solution offers the MOST reliable data transfer?
    
    - A. AWS DataSync over public internet
    - B. AWS DataSync over AWS Direct Connect **Most Voted**
    - C. AWS Database Migration Service (AWS DMS) over public internet
    - D. AWS Database Migration Service (AWS DMS) over AWS Direct Connect
    
    근거 
    
    - 문제 : 10TB 데이터가 쏟아져 나옴. ⇒ 온프레미스에 해당 데이터가 저장되고 이를 S3로 보내려 함. ⇒ 보안이 중요한데, 가장 효과적인 방법은?
    - DMS is for databases and here refers to “JSON files”. Public internet is not reliable. So best option is B.
- Q77
    
    A company needs to configure a real-time data ingestion architecture for its application. The company needs an API, a process that transforms data as the data is streamed, and a storage solution for the data.Which solution will meet these requirements with the LEAST operational overhead?
    
    - A. Deploy an Amazon EC2 instance to host an API that sends data to an Amazon Kinesis data stream. Create an Amazon Kinesis Data Firehose delivery stream that uses the Kinesis data stream as a data source. Use AWS Lambda functions to transform the data. Use the Kinesis Data Firehose delivery stream to send the data to Amazon S3.
    - B. Deploy an Amazon EC2 instance to host an API that sends data to AWS Glue. Stop source/destination checking on the EC2 instance. Use AWS Glue to transform the data and to send the data to Amazon S3.
    - C. Configure an Amazon API Gateway API to send data to an Amazon Kinesis data stream. Create an Amazon Kinesis Data Firehose delivery stream that uses the Kinesis data stream as a data source. Use AWS Lambda functions to transform the data. Use the Kinesis Data Firehose delivery stream to send the data to Amazon S3. **Most Voted**
    - D. Configure an Amazon API Gateway API to send data to AWS Glue. Use AWS Lambda functions to transform the data. Use AWS Glue to send the data to Amazon S3.
    
    근거 :
    
    - 문제 : 실시간 데이터 처리 필요 ⇒ 데이터 스트림과 저장에 API를 사용함
    - D가 틀린이유 : AWS Glue gets data from S3, not from API GW
    - Kinesis Data Firehose를 사용하면 굳이 EC2를 사용할 필요 없으므로 A,B가 틀림.
    - 
- Q78
    
    A company needs to keep user transaction data in an Amazon DynamoDB table. The company must retain the data for 7 years.What is the MOST operationally efficient solution that meets these requirements?
    
    - A. Use DynamoDB point-in-time recovery to back up the table continuously.
    - B. Use AWS Backup to create backup schedules and retention policies for the table. **Most Voted**
    - C. Create an on-demand backup of the table by using the DynamoDB console. Store the backup in an Amazon S3 bucket. Set an S3 Lifecycle configuration for the S3 bucket.
    - D. Create an Amazon EventBridge (Amazon CloudWatch Events) rule to invoke an AWS Lambda function. Configure the Lambda function to back up the table and to store the backup in an Amazon S3 bucket. Set an S3 Lifecycle configuration for the S3 bucket.
    
    근거 : 
    
    - 문제 : Dynamo DB에 user transaction을 7년간 저장해야한다. ⇒ 가장 운영적으로 효과적인 방법은?
    - AWS Backup을 사용한다.
    - point-in-time recovery (PITR) : PITR is used to recover your table to any point in time in a rolling 35 day window, which is used to help customers mitigate accidental deletes or writes to their tables from bad code, malicious access, or user error. (==> A isn't the answer)
- Q79
    
    A company is planning to use an Amazon DynamoDB table for data storage. The company is concerned about cost optimization. The table will not be used on most mornings. In the evenings, the read and write traffic will often be unpredictable. When traffic spikes occur, they will happen very quickly.What should a solutions architect recommend?
    
    - A. Create a DynamoDB table in on-demand capacity mode. **Most Voted**
    - B. Create a DynamoDB table with a global secondary index.
    - C. Create a DynamoDB table with provisioned capacity and auto scaling.
    - D. Create a DynamoDB table in provisioned capacity mode, and configure it as a global table.
    
    근거 
    
    - 문제 : Dynamo DB를 사용하고 싶음 ⇒ 비용 절감이 필요하고, 아침에는 거의 사용되지 않으며, 저녁에는 사용량 변동량이 큼 ⇒ 가장 비용 절감적인 방법은?
    - on-demand capacity mode를 사용
    - C가 틀린 이유는 저녁에 unpredictable 하므로 provisioned capacity이 부적절하기 때문임
- Q80
    
    A company recently signed a contract with an AWS Managed Service Provider (MSP) Partner for help with an application migration initiative. A solutions architect needs ta share an Amazon Machine Image (AMI) from an existing AWS account with the MSP Partner's AWS account. The AMI is backed by Amazon Elastic Block Store (Amazon EBS) and uses an AWS Key Management Service (AWS KMS) customer managed key to encrypt EBS volume snapshots.What is the MOST secure way for the solutions architect to share the AMI with the MSP Partner's AWS account?
    
    - A. Make the encrypted AMI and snapshots publicly available. Modify the key policy to allow the MSP Partner's AWS account to use the key.
    - B. Modify the launchPermission property of the AMI. Share the AMI with the MSP Partner's AWS account only. Modify the key policy to allow the MSP Partner's AWS account to use the key. **Most Voted**
    - C. Modify the launchPermission property of the AMI. Share the AMI with the MSP Partner's AWS account only. Modify the key policy to trust a new KMS key that is owned by the MSP Partner for encryption.
    - D. Export the AMI from the source account to an Amazon S3 bucket in the MSP Partner's AWS account, Encrypt the S3 bucket with a new KMS key that is owned by the MSP Partner. Copy and launch the AMI in the MSP Partner's AWS account.
    
    근거 :
    
    - 문제 : MSP를 통해 application migration을 수행하려 함. ⇒ AMI를 사용하려 하는데, MSP 계정과 연동이 필요함 ⇒ AMI는 KMS를 사용해 EBS 보안을 유지중임 ⇒ 가장 보안적으로 안정적인 방법은?
    - Share the existing KMS key with the MSP external account because it has already been used to encrypt the AMI snapshot.
- Q82
    
    A company hosts its web applications in the AWS Cloud. The company configures Elastic Load Balancers to use certificates that are imported into AWS Certificate Manager (ACM). The company's security team must be notified 30 days before the expiration of each certificate.What should a solutions architect recommend to meet this requirement?
    
    - A. Add a rule in ACM to publish a custom message to an Amazon Simple Notification Service (Amazon SNS) topic every day, beginning 30 days before any certificate will expire.
    - B. Create an AWS Config rule that checks for certificates that will expire within 30 days. Configure Amazon EventBridge (Amazon CloudWatch Events) to invoke a custom alert by way of Amazon Simple Notification Service (Amazon SNS) when AWS Config reports a noncompliant resource. **Most Voted**
    - C. Use AWS Trusted Advisor to check for certificates that will expire within 30 days. Create an Amazon CloudWatch alarm that is based on Trusted Advisor metrics for check status changes. Configure the alarm to send a custom alert by way of Amazon Simple Notification Service (Amazon SNS).
    - D. Create an Amazon EventBridge (Amazon CloudWatch Events) rule to detect any certificates that will expire within 30 days. Configure the rule to invoke an AWS Lambda function. Configure the Lambda function to send a custom alert by way of Amazon Simple Notification Service (Amazon SNS).
    
    근거 :
    
    - 문제 : Certificate를 ELB에 사용 ⇒ 만료 30일 전에 회사에서 알아야함.
    - B와 D 사이에 의견이 갈림. B가 효과적인 방법이라 생각
- Q84
    
    A company wants to reduce the cost of its existing three-tier web architecture. The web, application, and database servers are running on Amazon EC2 instances for the development, test, and production environments. The EC2 instances average 30% CPU utilization during peak hours and 10% CPU utilization during non-peak hours.The production EC2 instances run 24 hours a day. The development and test EC2 instances run for at least 8 hours each day. The company plans to implement automation to stop the development and test EC2 instances when they are not in use.Which EC2 instance purchasing solution will meet the company's requirements MOST cost-effectively?
    
    - A. Use Spot Instances for the production EC2 instances. Use Reserved Instances for the development and test EC2 instances.
    - B. Use Reserved Instances for the production EC2 instances. Use On-Demand Instances for the development and test EC2 instances. **Most Voted**
    - C. Use Spot blocks for the production EC2 instances. Use Reserved Instances for the development and test EC2 instances.
    - D. Use On-Demand Instances for the production EC2 instances. Use Spot blocks for the development and test EC2 instances.
    
    근거
    
    - 문제 : 가장 비용 절감적인 방법은?
    - Spot blocks are not longer available, and you can't use spot instances on Prod machines 24x7, so option B should be valid.
- Q85
    
    A company has a production web application in which users upload documents through a web interface or a mobile app. According to a new regulatory requirement. new documents cannot be modified or deleted after they are stored.What should a solutions architect do to meet this requirement?
    
    - A. Store the uploaded documents in an Amazon S3 bucket with S3 Versioning and S3 Object Lock enabled. **Most Voted**
    - B. Store the uploaded documents in an Amazon S3 bucket. Configure an S3 Lifecycle policy to archive the documents periodically.
    - C. Store the uploaded documents in an Amazon S3 bucket with S3 Versioning enabled. Configure an ACL to restrict all access to read-only.
    - D. Store the uploaded documents on an Amazon Elastic File System (Amazon EFS) volume. Access the data by mounting the volume in read-only mode.
    
    근거 :
    
    - 문제 : 문서를 저장 하는 앱이 있음⇒  read only만 가능함
    - S3 Object Lock : Read only
- Q86
    
    A company hosts an application on AWS Lambda functions that are invoked by an Amazon API Gateway API. The Lambda functions save customer data to an Amazon Aurora MySQL database. Whenever the company upgrades the database, the Lambda functions fail to establish database connections until the upgrade is complete. The result is that customer data is not recorded for some of the event.A solutions architect needs to design a solution that stores customer data that is created during database upgrades.Which solution will meet these requirements?
    
    - A. Provision an Amazon RDS proxy to sit between the Lambda functions and the database. Configure the Lambda functions to connect to the RDS proxy.
    - B. Increase the run time of the Lambda functions to the maximum. Create a retry mechanism in the code that stores the customer data in the database.
    - C. Persist the customer data to Lambda local storage. Configure new Lambda functions to scan the local storage to save the customer data to the database.
    - D. Store the customer data in an Amazon Simple Queue Service (Amazon SQS) FIFO queue. Create a new Lambda function that polls the queue and stores the customer data in the database.
    
    근거 
    
    - 문제 : API와 lambda를 연결해서 사용 중 ⇒ DB upgrade 수행 시 DB에 database가 저장되지 않는 문제 발생 ⇒ 이 문제를 해결하기 위해선?
    - SQS를 사용한다.
    
- Q88
    
    A survey company has gathered data for several years from areas in the United States. The company hosts the data in an Amazon S3 bucket that is 3 TB in size and growing. The company has started to share the data with a European marketing firm that has S3 buckets. The company wants to ensure that its data transfer costs remain as low as possible.Which solution will meet these requirements?
    
    - A. Configure the Requester Pays feature on the company's S3 bucket. **Most Voted**
    - B. Configure S3 Cross-Region Replication from the company's S3 bucket to one of the marketing firm's S3 buckets. **Most Voted**
    - C. Configure cross-account access for the marketing firm so that the marketing firm has access to the company's S3 bucket.
    - D. Configure the company's S3 bucket to use S3 Intelligent-Tiering. Sync the S3 bucket to one of the marketing firm's S3 buckets.
    
    근거 
    
    - 논쟁이 많은 문제임. A로 외우자.
    - Configure the requester Pays feature on the company’s S3 bucket.
- Q90
    
    A company is using a SQL database to store movie data that is publicly accessible. The database runs on an Amazon RDS Single-AZ DB instance. A script runs queries at random intervals each day to record the number of new movies that have been added to the database. The script must report a final total during business hours.The company's development team notices that the database performance is inadequate for development tasks when the script is running. A solutions architect must recommend a solution to resolve this issue.Which solution will meet this requirement with the LEAST operational overhead?
    
    - A. Modify the DB instance to be a Multi-AZ deployment.
    - B. Create a read replica of the database. Configure the script to query only the read replica. **Most Voted**
    - C. Instruct the development team to manually export the entries in the database at the end of each day.
    - D. Use Amazon ElastiCache to cache the common queries that the script runs against the database.
    
    근거 
    
    - 문제 :
        
        한 회사에서 공개적으로 액세스할 수 있는 동영상 데이터를 저장하기 위해 SQL 데이터베이스를 사용하고 있습니다. 데이터베이스는 Amazon RDS Single-AZ DB 인스턴스에서 실행됩니다. 스크립트는 데이터베이스에 추가된 새 동영상 수를 기록하기 위해 매일 임의의 간격으로 쿼리를 실행합니다. 스크립트는 업무 시간 동안 최종 합계를 보고해야 합니다.
        
        회사의 개발 팀은 스크립트가 실행 중일 때 데이터베이스 성능이 개발 작업에 적합하지 않다는 것을 알게 됩니다. 솔루션 설계자는 이 문제를 해결하기 위한 솔루션을 제안해야 합니다.
        
        운영 오버헤드를 최소화하면서 이 요구사항을 충족할 수 있는 솔루션은 무엇입니까?
        
    - 정답 : access 용 db를 새로 만들어서 개발과 사용을 이원화한다.
- Q93
    
    A company runs an on-premises application that is powered by a MySQL database. The company is migrating the application to AWS to increase the application's elasticity and availability.The current architecture shows heavy read activity on the database during times of normal operation. Every 4 hours, the company's development team pulls a full export of the production database to populate a database in the staging environment. During this period, users experience unacceptable application latency. The development team is unable to use the staging environment until the procedure completes.A solutions architect must recommend replacement architecture that alleviates the application latency issue. The replacement architecture also must give the development team the ability to continue using the staging environment without delay.Which solution meets these requirements?
    
    - A. Use Amazon Aurora MySQL with Multi-AZ Aurora Replicas for production. Populate the staging database by implementing a backup and restore process that uses the mysqldump utility.
    - B. Use Amazon Aurora MySQL with Multi-AZ Aurora Replicas for production. Use database cloning to create the staging database on-demand. **Most Voted**
    - C. Use Amazon RDS for MySQL with a Multi-AZ deployment and read replicas for production. Use the standby instance for the staging database.
    - D. Use Amazon RDS for MySQL with a Multi-AZ deployment and read replicas for production. Populate the staging database by implementing a backup and restore process that uses the mysqldump utility.
    
    근거 : 
    
    The recommended solution is Option B: Use Amazon Aurora MySQL with Multi-AZ Aurora Replicas for production. Use database cloning to create the staging database on-demand.
    
    To alleviate the application latency issue, the recommended solution is to use Amazon Aurora MySQL with Multi-AZ Aurora Replicas for production, and use database cloning to create the staging database on-demand. This allows the development team to continue using the staging environment without delay, while also providing elasticity and availability for the production application.
    
- Q96
    
    사진이 있어서 정답만 작성
    
    - C. Users can terminate an EC2 instance in the us-east-1 Region when the user's source IP is 10.100.100.254. **Most Voted**
    - 10.100.100.0 ⇒ 10.100.100.1 ~ 10.100.100 ~ 254 접근 가능
- Q97
    
    A company has a large Microsoft SharePoint deployment running on-premises that requires Microsoft Windows shared file storage. The company wants to migrate this workload to the AWS Cloud and is considering various storage options. The storage solution must be highly available and integrated with Active Directory for access control.Which solution will satisfy these requirements?
    
    - A. Configure Amazon EFS storage and set the Active Directory domain for authentication.
    - B. Create an SMB file share on an AWS Storage Gateway file gateway in two Availability Zones.
    - C. Create an Amazon S3 bucket and configure Microsoft Windows Server to mount it as a volume.
    - **D. Create an Amazon FSx for Windows File Server file system on AWS and set the Active Directory domain for authentication.**
    
    근거 :
    
    - 그냥 외우자. D
- Q98
    
    An image-processing company has a web application that users use to upload images. The application uploads the images into an Amazon S3 bucket. The company has set up S3 event notifications to publish the object creation events to an Amazon Simple Queue Service (Amazon SQS) standard queue. The SQS queue serves as the event source for an AWS Lambda function that processes the images and sends the results to users through email.Users report that they are receiving multiple email messages for every uploaded image. A solutions architect determines that SQS messages are invoking the Lambda function more than once, resulting in multiple email messages.What should the solutions architect do to resolve this issue with the LEAST operational overhead?
    
    - A. Set up long polling in the SQS queue by increasing the ReceiveMessage wait time to 30 seconds.
    - B. Change the SQS standard queue to an SQS FIFO queue. Use the message deduplication ID to discard duplicate messages.
    - C. Increase the visibility timeout in the SQS queue to a value that is greater than the total of the function timeout and the batch window timeout. **Most Voted**
    - D. Modify the Lambda function to delete each message from the SQS queue immediately after the message is read before processing.
    
    근거 
    
    - SQS를 사용하는데, 중복되서 작업이 진행 되는 경우 visibilityy timeout을 조정한다.
- Q99
- Q100
    
    A company's containerized application runs on an Amazon EC2 instance. The application needs to download security certificates before it can communicate with other business applications. The company wants a highly secure solution to encrypt and decrypt the certificates in near real time. The solution also needs to store data in highly available storage after the data is encrypted.Which solution will meet these requirements with the LEAST operational overhead?
    
    - A. Create AWS Secrets Manager secrets for encrypted certificates. Manually update the certificates as needed. Control access to the data by using fine-grained IAM access.
    - B. Create an AWS Lambda function that uses the Python cryptography library to receive and perform encryption operations. Store the function in an Amazon S3 bucket.
    - C. Create an AWS Key Management Service (AWS KMS) customer managed key. Allow the EC2 role to use the KMS key for encryption operations. Store the encrypted data on Amazon S3. **Most Voted**
    - D. Create an AWS Key Management Service (AWS KMS) customer managed key. Allow the EC2 role to use the KMS key for encryption operations. Store the encrypted data on Amazon Elastic Block Store (Amazon EBS) volumes.
    
    근거
    
    - AWS KMS 사용해서 Certificates 운영
    - highly available 해야하므로 S3 사용
- Q101
    
    A solutions architect is designing a VPC with public and private subnets. The VPC and subnets use IPv4 CIDR blocks. There is one public subnet and one private subnet in each of three Availability Zones (AZs) for high availability. An internet gateway is used to provide internet access for the public subnets. The private subnets require access to the internet to allow Amazon EC2 instances to download software updates.What should the solutions architect do to enable Internet access for the private subnets?
    
    - A. Create three NAT gateways, one for each public subnet in each AZ. Create a private route table for each AZ that forwards non-VPC traffic to the NAT gateway in its AZ. **Most Voted**
    - B. Create three NAT instances, one for each private subnet in each AZ. Create a private route table for each AZ that forwards non-VPC traffic to the NAT instance in its AZ.
    - C. Create a second internet gateway on one of the private subnets. Update the route table for the private subnets that forward non-VPC traffic to the private internet gateway.
    - D. Create an egress-only internet gateway on one of the public subnets. Update the route table for the private subnets that forward non-VPC traffic to the egress-only Internet gateway.
    
    근거 :
    
    - 외우자
    - B가 틀린 이유 : Now NAT Instances is avoided by AWS. Then choose the NAT Gateway
- Q102
    
    A company wants to migrate an on-premises data center to AWS. The data center hosts an SFTP server that stores its data on an NFS-based file system. The server holds 200 GB of data that needs to be transferred. The server must be hosted on an Amazon EC2 instance that uses an Amazon Elastic File System (Amazon EFS) file system.Which combination of steps should a solutions architect take to automate this task? (Choose two.)
    
    - A. Launch the EC2 instance into the same Availability Zone as the EFS file system. **Most Voted**
    - B. Install an AWS DataSync agent in the on-premises data center. **Most VotedMost Voted**
    - C. Create a secondary Amazon Elastic Block Store (Amazon EBS) volume on the EC2 instance for the data.
    - D. Manually use an operating system copy command to push the data to the EC2 instance.
    - E. Use AWS DataSync to create a suitable location configuration for the on-premises SFTP server. **Most Voted**
    
    근거 
    
    - A와 B가 정답인 것 같다.
- Q103
    
    A company has an AWS Glue extract, transform, and load (ETL) job that runs every day at the same time. The job processes XML data that is in an Amazon S3 bucket. New data is added to the S3 bucket every day. A solutions architect notices that AWS Glue is processing all the data during each run.What should the solutions architect do to prevent AWS Glue from reprocessing old data?
    
    - A. Edit the job to use job bookmarks. **Most Voted**
    - B. Edit the job to delete data after the data is processed.
    - C. Edit the job by setting the NumberOfWorkers field to 1.
    - D. Use a FindMatches machine learning (ML) transform.
    
    근거 :
    
    - 외우자. job bookmarks!!!
- Q104
    
    A solutions architect must design a highly available infrastructure for a website. The website is powered by Windows web servers that run on Amazon EC2 instances. The solutions architect must implement a solution that can mitigate a large-scale DDoS attack that originates from thousands of IP addresses. Downtime is not acceptable for the website.Which actions should the solutions architect take to protect the website from such an attack? (Choose two.)
    
    - A. Use AWS Shield Advanced to stop the DDoS attack. **Most Voted**
    - B. Configure Amazon GuardDuty to automatically block the attackers.
    - C. Configure the website to use Amazon CloudFront for both static and dynamic content. **Most Voted**
    - D. Use an AWS Lambda function to automatically add attacker IP addresses to VPC network ACLs.
    - E. Use EC2 Spot Instances in an Auto Scaling group with a target tracking scaling policy that is set to 80% CPU utilization.
    
    문제 : DDos Attack 방지 & 서버 downtime이 없어야함
    
    정답 : DDos에 대해 AWS Shield & WAF를 위해 Cloud Front 사용
    
- Q105
    
    A company is preparing to deploy a new serverless workload. A solutions architect must use the principle of least privilege to configure permissions that will be used to run an AWS Lambda function. An Amazon EventBridge (Amazon CloudWatch Events) rule will invoke the function.Which solution meets these requirements?
    
    - A. Add an execution role to the function with lambda:InvokeFunction as the action and * as the principal.
    - B. Add an execution role to the function with lambda:InvokeFunction as the action and Service: lambda.amazonaws.com as the principal.
    - C. Add a resource-based policy to the function with lambda:* as the action and Service: events.amazonaws.com as the principal.
    - D. Add a resource-based policy to the function with lambda:InvokeFunction as the action and Service: events.amazonaws.com as the principal. **Most Voted**
    
    문제
    
    근거 : D invokefunction!
    
- Q106
    
    A company is preparing to store confidential data in Amazon S3. For compliance reasons, the data must be encrypted at rest. Encryption key usage must be logged for auditing purposes. Keys must be rotated every year.Which solution meets these requirements and is the MOST operationally efficient?
    
    - A. Server-side encryption with customer-provided keys (SSE-C)
    - B. Server-side encryption with Amazon S3 managed keys (SSE-S3)
    - C. Server-side encryption with AWS KMS keys (SSE-KMS) with manual rotation
    - D. Server-side encryption with AWS KMS keys (SSE-KMS) with automatic rotation **Most Voted**
    
    문제 : key 사용 ⇒ kms
    
- Q107
    
    A bicycle sharing company is developing a multi-tier architecture to track the location of its bicycles during peak operating hours. The company wants to use these data points in its existing analytics platform. A solutions architect must determine the most viable multi-tier option to support this architecture. The data points must be accessible from the REST API.Which action meets these requirements for storing and retrieving location data?
    
    - A. Use Amazon Athena with Amazon S3.
    - B. Use Amazon API Gateway with AWS Lambda. **Most Voted**
    - C. Use Amazon QuickSight with Amazon Redshift.
    - D. Use Amazon API Gateway with Amazon Kinesis Data Analytics.
    
    문제
    
    - 이미 존재중인 analytics platform을 사용한다고 했으니 API Gateway & Lambda를 사용한다.
    - Quicksight와 Kinesis사용할 필요 없음
- Q108
    
    A company has an automobile sales website that stores its listings in a database on Amazon RDS. When an automobile is sold, the listing needs to be removed from the website and the data must be sent to multiple target systems.Which design should a solutions architect recommend?
    
    - A. Create an AWS Lambda function triggered when the database on Amazon RDS is updated to send the information to an Amazon Simple Queue Service (Amazon SQS) queue for the targets to consume. **Most Voted**
    - B. Create an AWS Lambda function triggered when the database on Amazon RDS is updated to send the information to an Amazon Simple Queue Service (Amazon SQS) FIFO queue for the targets to consume.
    - C. Subscribe to an RDS event notification and send an Amazon Simple Queue Service (Amazon SQS) queue fanned out to multiple Amazon Simple Notification Service (Amazon SNS) topics. Use AWS Lambda functions to update the targets.
    - D. Subscribe to an RDS event notification and send an Amazon Simple Notification Service (Amazon SNS) topic fanned out to multiple Amazon Simple Queue Service (Amazon SQS) queues. Use AWS Lambda functions to update the targets. **Most Voted**
    
    근거 
    
    - D는 SNS를 쓰기 떄문에 틀리므로 A 인 것 같다.
- Q111
    
    A company recently migrated a message processing system to AWS. The system receives messages into an ActiveMQ queue running on an Amazon EC2 instance. Messages are processed by a consumer application running on Amazon EC2. The consumer application processes the messages and writes results to a MySQL database running on Amazon EC2. The company wants this application to be highly available with low operational complexity.Which architecture offers the HIGHEST availability?
    
    - A. Add a second ActiveMQ server to another Availability Zone. Add an additional consumer EC2 instance in another Availability Zone. Replicate the MySQL database to another Availability Zone.
    - B. Use Amazon MQ with active/standby brokers configured across two Availability Zones. Add an additional consumer EC2 instance in another Availability Zone. Replicate the MySQL database to another Availability Zone.
    - C. Use Amazon MQ with active/standby brokers configured across two Availability Zones. Add an additional consumer EC2 instance in another Availability Zone. Use Amazon RDS for MySQL with Multi-AZ enabled.
    - D. Use Amazon MQ with active/standby brokers configured across two Availability Zones. Add an Auto Scaling group for the consumer EC2 instances across two Availability Zones. Use Amazon RDS for MySQL with Multi-AZ enabled. **Most Voted**
    
    근거 
    
    - 문제 : availability를 달성하는 방법
    - AZ를 늘리고 Autoscaling을 한다.
- Q112
    
    A company hosts a containerized web application on a fleet of on-premises servers that process incoming requests. The number of requests is growing quickly. The on-premises servers cannot handle the increased number of requests. The company wants to move the application to AWS with minimum code changes and minimum development effort.Which solution will meet these requirements with the LEAST operational overhead?
    
    - A. Use AWS Fargate on Amazon Elastic Container Service (Amazon ECS) to run the containerized web application with Service Auto Scaling. Use an Application Load Balancer to distribute the incoming requests. **Most Voted**
    - B. Use two Amazon EC2 instances to host the containerized web application. Use an Application Load Balancer to distribute the incoming requests.
    - C. Use AWS Lambda with a new code that uses one of the supported languages. Create multiple Lambda functions to support the load. Use Amazon API Gateway as an entry point to the Lambda functions.
    - D. Use a high performance computing (HPC) solution such as AWS ParallelCluster to establish an HPC cluster that can process the incoming requests at the appropriate scale.
    
    근거
    
    - 문제 : a fleet of on-premises라고 하는거 보니 MSA라 생각하면 될듯
    - 따라서 정답은 ECS를 사용하는 것
- Q113
    
    A company uses 50 TB of data for reporting. The company wants to move this data from on premises to AWS. A custom application in the company’s data center runs a weekly data transformation job. The company plans to pause the application until the data transfer is complete and needs to begin the transfer process as soon as possible.The data center does not have any available network bandwidth for additional workloads. A solutions architect must transfer the data and must configure the transformation job to continue to run in the AWS Cloud.Which solution will meet these requirements with the LEAST operational overhead?
    
    - A. Use AWS DataSync to move the data. Create a custom transformation job by using AWS Glue.
    - B. Order an AWS Snowcone device to move the data. Deploy the transformation application to the device.
    - C. Order an AWS Snowball Edge Storage Optimized device. Copy the data to the device. Create a custom transformation job by using AWS Glue. **Most Voted**
    - D. Order an AWS Snowball Edge Storage Optimized device that includes Amazon EC2 compute. Copy the data to the device. Create a new EC2 instance on AWS to run the transformation application.
    - 50TB 사이즈이므로 snowball을 사용하면 좋음. AWS Glue는 ETL 서비스이므로 전송에 좋다는 생각..
- Q115
    
    A medical records company is hosting an application on Amazon EC2 instances. The application processes customer data files that are stored on Amazon S3. The EC2 instances are hosted in public subnets. The EC2 instances access Amazon S3 over the internet, but they do not require any other network access.A new requirement mandates that the network traffic for file transfers take a private route and not be sent over the internet.Which change to the network architecture should a solutions architect recommend to meet this requirement?
    
    - A. Create a NAT gateway. Configure the route table for the public subnets to send traffic to Amazon S3 through the NAT gateway.
    - B. Configure the security group for the EC2 instances to restrict outbound traffic so that only traffic to the S3 prefix list is permitted.
    - C. Move the EC2 instances to private subnets. Create a VPC endpoint for Amazon S3, and link the endpoint to the route table for the private subnets. **Most Voted**
    - D. Remove the internet gateway from the VPC. Set up an AWS Direct Connect connection, and route traffic to Amazon S3 over the Direct Connect connection.
    
    근거 : 
    
    - 문제 : 새로운 요구사항이 네트워크 트래픽은 private routr를 거쳐야함.
    - AWS Direct Connect를 고민해서 D를 택함. AWS Direct Connect는 onpremise와 Cloud를 연결하는 용도임
    - VPC Endpoint가 내가 생각했던 기능임
- Q116
    
    A company uses a popular content management system (CMS) for its corporate website. However, the required patching and maintenance are burdensome. The company is redesigning its website and wants anew solution. The website will be updated four times a year and does not need to have any dynamic content available. The solution must provide high scalability and enhanced security.Which combination of changes will meet these requirements with the LEAST operational overhead? (Choose two.)
    
    - A. Configure Amazon CloudFront in front of the website to use HTTPS functionality. **Most Voted**
    - B. Deploy an AWS WAF web ACL in front of the website to provide HTTPS functionality.
    - C. Create and deploy an AWS Lambda function to manage and serve the website content.
    - D. Create the new website and an Amazon S3 bucket. Deploy the website on the S3 bucket with static website hosting enabled. **Most Voted**
    - E. Create the new website. Deploy the website by using an Auto Scaling group of Amazon EC2 instances behind an Application Load Balancer.
    
    문제 :  not need to have any dynamic content available을 봤을 때 static으로 구성하면 간단함을 알 수 있음 ⇒ 확장성과 보안을 강조하는 것인 만큼 HTTPS를 사용하면 됨
    
    - C를 택했는데, 생각해보니 lambda로 웹 사이트를 운영한다는게 말이 안됨
- Q117
    
    A company stores its application logs in an Amazon CloudWatch Logs log group. A new policy requires the company to store all application logs in Amazon OpenSearch Service (Amazon Elasticsearch Service) in near-real time.Which solution will meet this requirement with the LEAST operational overhead?
    
    - A. Configure a CloudWatch Logs subscription to stream the logs to Amazon OpenSearch Service (Amazon Elasticsearch Service). **Most Voted**
    - B. Create an AWS Lambda function. Use the log group to invoke the function to write the logs to Amazon OpenSearch Service (Amazon Elasticsearch Service).
    - C. Create an Amazon Kinesis Data Firehose delivery stream. Configure the log group as the delivery streams sources. Configure Amazon OpenSearch Service (Amazon Elasticsearch Service) as the delivery stream's destination.
    - D. Install and configure Amazon Kinesis Agent on each application server to deliver the logs to Amazon Kinesis Data Streams. Configure Kinesis Data Streams to deliver the logs to Amazon OpenSearch Service (Amazon Elasticsearch Service).
    
    문제 CloudWatch Logs를 OpenSearch Service와 근 실시간으로 연결시키고 싶음. 
    
    외우기 : cloudwatch logs와 opensearch service를 직접 연동시킬 수 있다. 
    
    - You can configure a CloudWatch Logs log group to stream data it receives to your Amazon OpenSearch Service cluster in near real-time through a CloudWatch Logs subscription.
    - [https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_OpenSearch_Stream.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_OpenSearch_Stream.html)
    - 외워야 하는 문제
- Q119
    
    A global company is using Amazon API Gateway to design REST APIs for its loyalty club users in the us-east-1 Region and the ap-southeast-2 Region. A solutions architect must design a solution to protect these API Gateway managed REST APIs across multiple accounts from SQL injection and cross-site scripting attacks.Which solution will meet these requirements with the LEAST amount of administrative effort?
    
    - A. Set up AWS WAF in both Regions. Associate Regional web ACLs with an API stage.
    - B. Set up AWS Firewall Manager in both Regions. Centrally configure AWS WAF rules. **Most Voted**
    - C. Set up AWS Shield in bath Regions. Associate Regional web ACLs with an API stage.
    - D. Set up AWS Shield in one of the Regions. Associate Regional web ACLs with an API stage.
    
    근거 
    
    - 문제 : SQL injection and cross-site scripting attacks에 대한 해결책은?
    - AWS WAF를 사용하자.
- Q120
    
    A company has implemented a self-managed DNS solution on three Amazon EC2 instances behind a Network Load Balancer (NLB) in the us-west-2 Region. Most of the company's users are located in the United States and Europe. The company wants to improve the performance and availability of the solution. The company launches and configures three EC2 instances in the eu-west-1 Region and adds the EC2 instances as targets for a new NLB.Which solution can the company use to route traffic to all the EC2 instances?
    
    - A. Create an Amazon Route 53 geolocation routing policy to route requests to one of the two NLBs. Create an Amazon CloudFront distribution. Use the Route 53 record as the distribution’s origin.
    - B. Create a standard accelerator in AWS Global Accelerator. Create endpoint groups in us-west-2 and eu-west-1. Add the two NLBs as endpoints for the endpoint groups. **Most Voted**
    - C. Attach Elastic IP addresses to the six EC2 instances. Create an Amazon Route 53 geolocation routing policy to route requests to one of the six EC2 instances. Create an Amazon CloudFront distribution. Use the Route 53 record as the distribution's origin.
    - D. Replace the two NLBs with two Application Load Balancers (ALBs). Create an Amazon Route 53 latency routing policy to route requests to one of the two ALBs. Create an Amazon CloudFront distribution. Use the Route 53 record as the distribution’s origin.
    - 문제 : 글로벌 배포에 대해서는 무조건 Global Accelerator를 사용하는 것으로 나오네
- Q121
    
    *Topic 1*
    
    A company is running an online transaction processing (OLTP) workload on AWS. This workload uses an unencrypted Amazon RDS DB instance in a Multi-AZ deployment. Daily database snapshots are taken from this instance.What should a solutions architect do to ensure the database and snapshots are always encrypted moving forward?
    
    - A. Encrypt a copy of the latest DB snapshot. Replace existing DB instance by restoring the encrypted snapshot. **Most Voted**
    - B. Create a new encrypted Amazon Elastic Block Store (Amazon EBS) volume and copy the snapshots to it. Enable encryption on the DB instance.
    - C. Copy the snapshots and enable encryption using AWS Key Management Service (AWS KMS) Restore encrypted snapshot to an existing DB instance.
    - D. Copy the snapshots to an Amazon S3 bucket that is encrypted using server-side encryption with AWS Key Management Service (AWS KMS) managed keys (SSE-KMS).
    
    문제 : DB Encryption 수행 방법
    
    "You can enable encryption for an Amazon RDS DB instance when you create it, but not after it's created. However, you can add encryption to an unencrypted DB instance by creating a snapshot of your DB instance, and then creating an encrypted copy of that snapshot. You can then restore a DB instance from the encrypted snapshot to get an encrypted copy of your original DB instance."
    [https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/encrypt-an-existing-amazon-rds-for-postgresql-db-instance.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/encrypt-an-existing-amazon-rds-for-postgresql-db-instance.html)
    
- Q125
    
    문제가 이상한듯..
    
- Q127
    
    A media company is evaluating the possibility of moving its systems to the AWS Cloud. The company needs at least 10 TB of storage with the maximum possible I/O performance for video processing, 300 TB of very durable storage for storing media content, and 900 TB of storage to meet requirements for archival media that is not in use anymore.Which set of services should a solutions architect recommend to meet these requirements?
    
    - A. Amazon EBS for maximum performance, Amazon S3 for durable data storage, and Amazon S3 Glacier for archival storage
    - B. Amazon EBS for maximum performance, Amazon EFS for durable data storage, and Amazon S3 Glacier for archival storage
    - C. Amazon EC2 instance store for maximum performance, Amazon EFS for durable data storage, and Amazon S3 for archival storage
    - D. Amazon EC2 instance store for maximum performance, Amazon S3 for durable data storage, and Amazon S3 Glacier for archival storage **Most Vot**
    
    근거 : 
    
    - EC2 Storage가 EBS보다 빠르다.
        
        The keyword here is "maximum possible I/O performance".
        EBS and Ec2 instance store are good options, but EC2 is higher than EBS in terms of I/O performance. Maximum possible is clearly Ec2 instance storage.
        There are some concerns about the 10TB needed, however, storage optimized Ec2 instance stores can take up to 24 x 13980 GB (ie 312 TB)
        So option D is the winner here
        
- Q130
    
    An application runs on Amazon EC2 instances across multiple Availability Zonas. The instances run in an Amazon EC2 Auto Scaling group behind an Application Load Balancer. The application performs best when the CPU utilization of the EC2 instances is at or near 40%.What should a solutions architect do to maintain the desired performance across all instances in the group?
    
    - A. Use a simple scaling policy to dynamically scale the Auto Scaling group.
    - B. Use a target tracking policy to dynamically scale the Auto Scaling group. **Most Voted**
    - C. Use an AWS Lambda function ta update the desired Auto Scaling group capacity.
    - D. Use scheduled scaling actions to scale up and scale down the Auto Scaling group.
    
    근거 : 
    
    - AutoScaling이 최적화 되어있지 않다고 판단. target tracking을 통해 특정 metric을 기준으로 확장 가능하게 만든다.
    - With a target tracking scaling policy, you can increase or decrease the current capacity of the group based on a target value for a specific metric.
- Q131
    
    A company is developing a file-sharing application that will use an Amazon S3 bucket for storage. The company wants to serve all the files through an Amazon CloudFront distribution. The company does not want the files to be accessible through direct navigation to the S3 URL.What should a solutions architect do to meet these requirements?
    
    - A. Write individual policies for each S3 bucket to grant read permission for only CloudFront access.
    - B. Create an IAM user. Grant the user read permission to objects in the S3 bucket. Assign the user to CloudFront.
    - C. Write an S3 bucket policy that assigns the CloudFront distribution ID as the Principal and assigns the target S3 bucket as the Amazon Resource Name (ARN).
    - D. Create an origin access identity (OAI). Assign the OAI to the CloudFront distribution. Configure the S3 bucket permissions so that only the OAI has read permission. **Most Voted**
    
    근거 
    
    - 문제 : S3에서 파일 공유를 하는 앱이 있는데, S3주소로 다이렉트로 다운 받는것을 제한하고 싶어함.
    - 이때는 OAI를 써라
- Q132
    
    A company’s website provides users with downloadable historical performance reports. The website needs a solution that will scale to meet the company’s website demands globally. The solution should be cost-effective, limit the provisioning of infrastructure resources, and provide the fastest possible response time.Which combination should a solutions architect recommend to meet these requirements?
    
    - A. Amazon CloudFront and Amazon S3 **Most Voted**
    - B. AWS Lambda and Amazon DynamoDB
    - C. Application Load Balancer with Amazon EC2 Auto Scaling
    - D. Amazon Route 53 with internal Application Load Balancers
    
    문제 : 글로벌하게 웹을 배포할 예정 ⇒ Cloudfront
    
- Q133
    
    A company runs an Oracle database on premises. As part of the company’s migration to AWS, the company wants to upgrade the database to the most recent available version. The company also wants to set up disaster recovery (DR) for the database. The company needs to minimize the operational overhead for normal operations and DR setup. The company also needs to maintain access to the database's underlying operating system.Which solution will meet these requirements?
    
    - A. Migrate the Oracle database to an Amazon EC2 instance. Set up database replication to a different AWS Region.
    - B. Migrate the Oracle database to Amazon RDS for Oracle. Activate Cross-Region automated backups to replicate the snapshots to another AWS Region.
    - C. Migrate the Oracle database to Amazon RDS Custom for Oracle. Create a read replica for the database in another AWS Region. **Most Voted**
    - D. Migrate the Oracle database to Amazon RDS for Oracle. Create a standby database in another Availability Zone.
    
    근거 : Option C since **RDS Custom has access to the underlying OS and it provides less operational overhead.** Also, a read replica in another Region can be used for DR activities.
    
    [https://aws.amazon.com/blogs/database/implementing-a-disaster-recovery-strategy-with-amazon-rds/](https://aws.amazon.com/blogs/database/implementing-a-disaster-recovery-strategy-with-amazon-rds/)
    
- Q134
    
    A company wants to move its application to a serverless solution. The serverless solution needs to analyze existing and new data by using SL. The company stores the data in an Amazon S3 bucket. The data requires encryption and must be replicated to a different AWS Region.Which solution will meet these requirements with the LEAST operational overhead?
    
    - A. Create a new S3 bucket. Load the data into the new S3 bucket. Use S3 Cross-Region Replication (CRR) to replicate encrypted objects to an S3 bucket in another Region. Use server-side encryption with AWS KMS multi-Region kays (SSE-KMS). Use Amazon Athena to query the data. **Most Voted**
    - B. Create a new S3 bucket. Load the data into the new S3 bucket. Use S3 Cross-Region Replication (CRR) to replicate encrypted objects to an S3 bucket in another Region. Use server-side encryption with AWS KMS multi-Region keys (SSE-KMS). Use Amazon RDS to query the data.
    - C. Load the data into the existing S3 bucket. Use S3 Cross-Region Replication (CRR) to replicate encrypted objects to an S3 bucket in another Region. Use server-side encryption with Amazon S3 managed encryption keys (SSE-S3). Use Amazon Athena to query the data. **Most Voted**
    - D. Load the data into the existing S3 bucket. Use S3 Cross-Region Replication (CRR) to replicate encrypted objects to an S3 bucket in another Region. Use server-side encryption with Amazon S3 managed encryption keys (SSE-S3). Use Amazon RDS to query the data.
    
    문제
    
    - A와 C 모두 합리적인 방법임. 지금까지 KMS가 정답인 경우가 많았기 때문에, A로 생각하겠음.
- Q135
    
    A company runs workloads on AWS. The company needs to connect to a service from an external provider. The service is hosted in the provider's VPC. According to the company’s security team, the connectivity must be private and must be restricted to the target service. The connection must be initiated only from the company’s VPC.Which solution will mast these requirements?
    
    - A. Create a VPC peering connection between the company's VPC and the provider's VPC. Update the route table to connect to the target service.
    - B. Ask the provider to create a virtual private gateway in its VPC. Use AWS PrivateLink to connect to the target service.
    - C. Create a NAT gateway in a public subnet of the company’s VPUpdate the route table to connect to the target service.
    - D. Ask the provider to create a VPC endpoint for the target service. Use AWS PrivateLink to connect to the target service. **Most Voted**
    
    VPC endpoint : 인터넷 거치지 않고 VPC 간 direct로 연결
    
- Q136
    
    A company is migrating its on-premises PostgreSQL database to Amazon Aurora PostgreSQL. The on-premises database must remain online and accessible during the migration. The Aurora database must remain synchronized with the on-premises database.Which combination of actions must a solutions architect take to meet these requirements? (Choose two.)
    
    - A. Create an ongoing replication task. **Most Voted**
    - B. Create a database backup of the on-premises database.
    - C. Create an AWS Database Migration Service (AWS DMS) replication server. **Most Voted**
    - D. Convert the database schema by using the AWS Schema Conversion Tool (AWS SCT).
    - E. Create an Amazon EventBridge (Amazon CloudWatch Events) rule to monitor the database synchronization.
    
    근거 : 
    
    - AWS DMS를 사용하면 쉽게 데이터를 옮길 수 있다.
    - ongoing replication task
    - After you complete the full load, make sure that you perform ongoing replication using AWS DMS to keep the source and target databases in sync. To configure the ongoing replication task, sign in to the AWS Management Console and follow these steps.
- Q137
    
    
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
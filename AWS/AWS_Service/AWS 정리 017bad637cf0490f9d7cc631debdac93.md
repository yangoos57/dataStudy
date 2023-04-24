# AWS 정리

### 서비스

### Active Directory

chat gpt

Active Directory (AD) is a centralized authentication and identity management service that is used in Windows-based environments. The purpose of AD is to provide a single source of truth for user and computer accounts, permissions, and other information that is used to manage and secure resources within an organization's network.

The main benefits of using AD include:

1. Centralized user management: AD enables administrators to manage user accounts and access permissions from a central location. This makes it easier to grant or revoke access to network resources and applications.
2. Single sign-on: AD allows users to authenticate once and then access multiple resources and applications without needing to enter their credentials again. This reduces the need for users to remember multiple passwords and improves security by reducing the risk of password-related issues such as reuse or weak passwords.
3. Group policy management: AD allows administrators to apply policies to groups of computers or users, which can help enforce security policies, automate software installations and updates, and streamline management tasks.
4. Domain Name System (DNS) integration: AD integrates with DNS, allowing administrators to easily manage and resolve domain names and IP addresses within the network.

Overall, AD helps organizations to manage and secure their network resources more efficiently, while also improving the user experience by simplifying authentication and access management.

### Athena

- 파일로 저장된 텍스트 데이터에 SQL query를 사용할 수 있는 서비스
- 실시간으로 처리하기에는 기존 DBMS 보다 느린 속도라고 하니 backend에서 대용량으로 처리하는데 사용하면 된다.

### Appflow

Saas 서비스들 간 데이터를 안전하게 전송하는 서비스를 말한다. 추가적인 코드 없이 쉽고 빠르게 데이터를 보낼 수 있다.

### Amazon API Gateway

Amazon API Gateway is an AWS service for creating, publishing, maintaining, monitoring, and securing REST, HTTP, and WebSocket APIs at any scale.

Chat GPT

API Gateway supports integration with a variety of AWS services, including Lambda functions, Elastic Beanstalk, and EC2 instances, as well as with external HTTP endpoints and other third-party services.

### Backup

AWS Backup is a fully managed backup service that makes it easy to centralize and automate the backup of data across AWS resources.

### Config

AWS Config는 리소스의 구성 및 관계에 대한 지속적인 진단, 감사 및 평가를 수행합니다.

### Cloudfront

아마존의 CDN을 말함. static과 dynamic content를 지원한다!

WAF가 기본적으로 실행되며 & caching 기능이 있다.

### Cloudtrail

- 포괄적인 API 감사 도구
- **[AWS CloudTrail](https://aws.amazon.com/cloudtrail/)**은 계정에 대한 API 호출을 기록합니다. 기록되는 정보에는 API 호출자 ID, API 호출 시간, API 호출자의 소스 IP 주소 등이 포함됩니다. CloudTrail은 누군가 남긴 이동 경로(또는 작업 로그)의 ‘추적’으로 생각할 수 있습니다.

### CloudWatch

> **클라우드 워치**
다양한 지표를 모니터링 및 관리하고 해당 지표의 데이터를 기반으로 경보 작업을 구성할 수 있는 웹 서비스
> 

### Comprehend

Amazon Comprehend uses machine learning to help you uncover the insights and relationships in your unstructured data.

### DataSync

AWS DataSync is a data transfer service that uses network optimization techniques to transfer data efficiently and securely between on-premises storage systems and Amazon S3 or other storage targets.

### Direct Connection

- AWS Direct Connect - 전용 광섬유 연결을 구축
    
    > **[AWS Direct Connect](https://aws.amazon.com/directconnect/)**는 데이터 센터와 VPC 간에 비공개 전용 연결을 설정하는 서비스입니다.
    > 

![Untitled](AWS%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20017bad637cf0490f9d7cc631debdac93/Untitled.png)

![Untitled](AWS%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20017bad637cf0490f9d7cc631debdac93/Untitled%201.png)

### Event Bridge

- [https://velog.io/@youngeui_hong/Event-Driven-Architecture](https://velog.io/@youngeui_hong/Event-Driven-Architecture)

what

event-driven architecture를 구성하는데 사용하는 서비스이며, 서버리스로 구현된다. 이벤트 브릿지는 scalable, reliable, secure 한 인프라를 제공한다. 

### Fargate

what

컨테이너용 서버리스 컴퓨팅 엔진으로, Amazon ECS와 Amazon EKS에서 작동합니다.

### File Gateway(S3)

- 온프레미스 데이터센터와 s3를 연결하는 서비스
- 온프레미스 IT 환경과 AWS 스토리지 인프라 Amazon Web Services Cloud에 데이터를 저장하여 데이터 보안을 유지하는 데 도움이 되는, 확장 가능하면서 비용 효율적인 스토리지를 구현할 수 있다.
- It allows you to store and access your file data in Amazon S3, while still maintaining your existing file-based applications and workflows.

### File Gateway(Fsx)

- 온프레미스 File sheres와 AWS file shares를 연동하는 서비스
- Amazon FSx File Gateway (FSx File Gateway) is a new File Gateway type that provides low latency and efficient access to in-cloud FSx for Windows File Server file shares from your on-premises facility.

### Firewall Manager

여러 서비스에 존재하는 Firewall를 중앙에서 쉽게 관리하게 도와주는 서비스라고 함. 

방화벽이란 VPC에서 발생하는 트래픽에 대한 Filtering & inspection을 수행하는 도구임.

### GaurdDuty

what

GuardDuty는 위협 감시 및 예측 가능한 위협을 사전에 식별하는 서비스, 머신러닝이 적용된 서비스이다. 

AWS CloudTrail 관리 이벤트, 이벤트 로그, [기본 데이터 원본](https://docs.aws.amazon.com/ko_kr/guardduty/latest/ug/guardduty_data-sources.html), VPC 흐름 로그, AWS CloudTrail DNS 로그 등을 분석하고 처리하는 보안 모니터링 서비스라고 한다.

### Glue

- [https://krksap.tistory.com/1885](https://krksap.tistory.com/1885)

what

- AWS S3, RDS, Dynamodb,redshift 등에 있는 데이터를 활용해 ETL을 구성하는 도구
- Serverless라 Infra 관리의 부담을 줄일 수 있음

### Gateway LB, App LB, Network LB

- [https://inpa.tistory.com/entry/AWS-📚-ELB-Elastic-Load-Balancer-개념-원리-구축-세팅-CLB-ALB-NLB-GLB](https://inpa.tistory.com/entry/AWS-%F0%9F%93%9A-ELB-Elastic-Load-Balancer-%EA%B0%9C%EB%85%90-%EC%9B%90%EB%A6%AC-%EA%B5%AC%EC%B6%95-%EC%84%B8%ED%8C%85-CLB-ALB-NLB-GLB)

what 

LB는 트래픽을 여러 분산시키기 위한 용도로 사용한다. 

ALB : app 단의 로드 밸런싱을 지원한다. 주소의 상세 페이지별로 EC2나 Lambda가 존재할 수 있다.

![Untitled](AWS%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20017bad637cf0490f9d7cc631debdac93/Untitled%202.png)

NLB : Transport 단의 로드 밸런싱을 지원한다. EC2 인스턴스를 대상으로 한다. 

아래 그림은 auto-scaling 했기에 port number가 같다고 보는 게 맞는 듯

![Untitled](AWS%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20017bad637cf0490f9d7cc631debdac93/Untitled%203.png)

GWLB : Network 단의 로드 밸런싱을 지원한다. 박화벽, 침입 탐지 및 방지 시스템, 심층 패킷 검사 시스템과 같은 가상 Appliance를 관리할 수 있다고 한다. (일반적인 로드밸런서 역할과 다르게 트래픽을 체크하는 용도라고 한다.)

### Global Accelerator

what 

글로벌 유저들에게 고객 서비스를 빠르게 제공하는데 도움을 주는 aws 서비스 

[AWS Global Accelerator](https://aws.amazon.com/ko/global-accelerator/?nc2=h_re) 는 AWS 글로벌 네트워크를 활용해 경로를 최적화해서 성능을 높이고, 지속적인 모니터링으로 가용성을 제공합니다. 따라서 재해 복구에 대응하고, 성능 개선과 네트워크 확장 등을 손쉽게 구성할 수 있습니다.

> CloudFront와 Global Accelerator 차이
CloudFront uses Edge Locations to cache content while Global Accelerator uses Edge Locations to find an optimal pathway to the nearest regional endpoint.
> 

chat 

AWS Global Accelerator is **a networking service** provided by Amazon Web Services (AWS) that improves the availability and performance of applications that are deployed across multiple AWS regions or availability zones.

Global Accelerator uses the AWS global network to direct traffic to optimal endpoints (such as Amazon Elastic Compute Cloud (EC2) instances, Application Load Balancers, or Network Load Balancers) based on health, geography, and routing policies. This helps to reduce latency, improve availability, and increase throughput for end users accessing the application from different geographic locations.

### Identity and Access Management(IAM)

- aws:PrincipalOrgID를 통해 S3 bucket 접근제어를 설정할 수 있음.
- [https://aws.amazon.com/ko/about-aws/whats-new/2018/05/principal-org-id/#:~:text=aws%3APrincipalOrgID라는 새로운 조건,액세스할 수 있도록 합니다](https://aws.amazon.com/ko/about-aws/whats-new/2018/05/principal-org-id/#:~:text=aws%3APrincipalOrgID%EB%9D%BC%EB%8A%94%20%EC%83%88%EB%A1%9C%EC%9A%B4%20%EC%A1%B0%EA%B1%B4,%EC%95%A1%EC%84%B8%EC%8A%A4%ED%95%A0%20%EC%88%98%20%EC%9E%88%EB%8F%84%EB%A1%9D%20%ED%95%A9%EB%8B%88%EB%8B%A4).

### Key Management Service

- 데이터 저장에 있어서 암호화를 지원하는 서비스
- AWS Key Management Service(AWS KMS)를 사용하면 암호화 키를 사용하여 암호화 작업을 수행할 수 있습니다. 암호화 키는 데이터 잠금(암호화) 및 잠금 해제(암호 해독)에 사용되는 임의의 숫자 문자열입니다.
- 저장 중 암호화 : Key로 데이터 암호화
- 전송 중 암호화 : SSL
- AWS KMS supports *multi-Region keys*, which are AWS KMS keys in different AWS Regions that can be used interchangeably – as though you had the same key in multiple Regions.(as though = as if)

### Kinesis Data Firehose

- data stream firehose 비교용..(이해가 잘되진 않지만.)
- [https://eprj453.github.io/aws/2021/08/03/AWS-Kinesis-도입기-1.-Data-Stream과-Firehose/](https://eprj453.github.io/aws/2021/08/03/AWS-Kinesis-%EB%8F%84%EC%9E%85%EA%B8%B0-1.-Data-Stream%EA%B3%BC-Firehose/)
- data stream firehose 비교용2
- [https://jaeyeong951.medium.com/aws-kinesis-data-stream-vs-data-firehose-10102d949741](https://jaeyeong951.medium.com/aws-kinesis-data-stream-vs-data-firehose-10102d949741)

what

Kinesis Data Firehose 의 주목적은 미리 정의된 목적지(Destination)에 데이터를 안전하게 전달(Deliver)하는 것입니다.

### Kinesis Data Streams

- 실시간 데이터에 대해 처리하고 분석하는 용도로 사용한다. 일례로 웹 사이트 클릭, 앱로그, IOT 통신 데이터 등이 있다.
- Kinesis Data Stream 은 실시간으로 data 들을 받아들일 수 있는 입구이자 저장소로서의 역할을 합니다.
- pipeline 이자 메시지 큐와 비슷한 역할을 한다고 볼수도 있겠네요.
- [https://jaeyeong951.medium.com/aws-kinesis-data-stream-vs-data-firehose-10102d949741](https://jaeyeong951.medium.com/aws-kinesis-data-stream-vs-data-firehose-10102d949741)

### Lambda

Serverless + Autoscaling

API Gateway와 사용하면 Restful API 완성

### Amazon Machine Images(AMI)

AMI is a pre-configured virtual machine image that is used to create an EC2 instance.

You can launch multiple instances from a single AMI when you require multiple instances with the same configuration.

### Macie

what

AWS에 저장되는 민감 정보를 찾고, 분류하고, 보호하는 보안 서비스이다. 머신러닝을 기반으로 S3에서 민감 정보를 찾아낸다. 예를들면 Personally identifiable information(PII)이 있다.

AWS Macie is a security service that helps to discover, classify, and protect sensitive data stored in AWS.

### QuickSight

- [https://jsonobject.tistory.com/546](https://jsonobject.tistory.com/546)

아마존이 제공하는 서버리스 매니지드 **BI** 상품이다. 특정 데이터에 대한 시각화 대시보드를 생성하고 다른 사용자와 공유할 수 있다.

### Reserved Instance

사용량이 예측 가능할 경우(약정 방식 1년또는 3년) 사용 / 

Reserved Instance :  컴퓨팅 사용량을 약정할 필요가 없다. 

Savings Plan  :사용량을 미리 합의한다.

### Rekognition

what

머신러닝 기반으로 이미지 또는 영상을 분석하는 서비스를 말함. 물체, 사람, 텍스트, 배경, 부적절한 콘텐츠 등을 구분하는데 사용함.

### Redshift

what 

데이터 웨어하우스 구축을 위한 서비스이다. 트랜잭션을 위한 데이터베이스보다는 분석목적의 데이터 저장소에 가깝다고 한다.

![Untitled](AWS%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20017bad637cf0490f9d7cc631debdac93/Untitled%204.png)

### Shield

DDos 방어용으로 사용한다. / ELB에 붙여서 모든 트래픽에 대해 구분한다. 

### Server Side Encycloped-S3(SSE-S3)

Encryption 용도..

### Systems Manager

- [https://kimjingo.tistory.com/187](https://kimjingo.tistory.com/187)

운영 측면에서 Systems Manager는 수작업 및 스크립트 작성 등이 필요한 유지보수 작업을 돕는 도구로서 다음과 같은 업무를 수행합니다.

- 온프레미스와 EC2 인스턴스의 패키지 업그레이드
- 설치 소프트웨어 목록 생성
- 새 애플리케이션 설치
- EBS 스냅샷을 이용한 AMI 이미지 생성
- IAM 인스턴스 프로파일 부착
- S3 버킷에 대한 퍼블릭 접근 차단

### System Manager Session Manager

Session Manager provides secure and auditable node management without the need to open inbound ports, maintain bastion hosts, or manage SSH keys.

- auditable : (회계)감사의

### S3, EBS, EFS 비교

- [https://inpa.tistory.com/entry/AWS-📚-S3-EBS-EFS-스토리지-서비스-비교#:~:text=EBS%2C EFS%2C S3 모두 데이터,파일 기반 저장 서비스이다](https://inpa.tistory.com/entry/AWS-%F0%9F%93%9A-S3-EBS-EFS-%EC%8A%A4%ED%86%A0%EB%A6%AC%EC%A7%80-%EC%84%9C%EB%B9%84%EC%8A%A4-%EB%B9%84%EA%B5%90#:~:text=EBS%2C%20EFS%2C%20S3%20%EB%AA%A8%EB%91%90%20%EB%8D%B0%EC%9D%B4%ED%84%B0,%ED%8C%8C%EC%9D%BC%20%EA%B8%B0%EB%B0%98%20%EC%A0%80%EC%9E%A5%20%EC%84%9C%EB%B9%84%EC%8A%A4%EC%9D%B4%EB%8B%A4).
- EBS : 볼륨 기반, S3 : 객체 기반, EFS 파일 기반
- EBS : 독립적인 서비스인 EFS, S3와 다르게 EC2와 함께 사용해야함. 단일 인스턴스에 대한 고성능 스토리지 서비스가 필요한 경우
    
    ![Untitled](AWS%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20017bad637cf0490f9d7cc631debdac93/Untitled%205.png)
    
- EFS : 여러 EC2에서 공유해서 사용해야하는 경우 사용
    - 여러 인스턴스가 공유할 수 있는 폴더임
    - 리눅스 파일 시스템임
    - 리전 리소스임
    - 자동확장 가능
    - EBS는 단일 가용영역에서 사용하지만 EFS는 리전에서 사용한다.
- S3 : 스토리지 저장과 관련해서 다양한 서비스를 제공함.
    - 정적웹 지원
    - 리전별 분산(내구성이 좋은 이유) 3개의 시설에서 각 2개의 물리적으로 복제됨
    - 비용절감효과
    - 서버리스
    
    ![Untitled](AWS%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20017bad637cf0490f9d7cc631debdac93/Untitled%206.png)
    

### S3 Intelligent-tiering

- [https://0mini.tistory.com/5](https://0mini.tistory.com/5)

what

머신러닝을 기반으로 객체를 frequent access와 infrequent access로 구분하는 스토리지를 말한다. 가격이 매우 저렴하다고 한다. 연속 30일 이상 사용하지 않은 객체를 infrequent access 계층으로 변환한다고 한다. 

> chat gpt

S3 Intelligent-Tiering is a storage class in Amazon S3 that automatically moves objects between two access tiers: frequent access and infrequent access. It uses machine learning to analyze object access patterns and automatically moves objects to the most cost-effective storage tier based on changing access patterns over time.
> 

### S3 Standard-Infrequent Acess(S3 Standard-IA)

chatgpt

The pricing for S3 Standard-IA is typically lower than S3 Standard, but there are additional retrieval fees associated with accessing the data. In general, S3 Standard-IA is a good choice for data that is accessed less frequently but still requires quick retrieval, such as backups, archives, or less frequently used files.

### S3 Object Lock

S3 파일을 Read Only로 가능하게 만드는 방법임. 

You can use S3 Object Lock to store objects using a write-once-read-many (WORM) model. Object Lock can help prevent objects from being deleted or overwritten for a fixed amount of time or indefinitely.

### SQS visibility timeout

[https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html)

what 

- Queue 내부의 message를 중복의 사용자가 사용하지 못하도록 설정하는 옵션

### Snowcone, Snowball, Snowmobile

snowcone : 8TB

snowball : ~80TB

snowmobile : 100PB

![Untitled](AWS%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20017bad637cf0490f9d7cc631debdac93/Untitled%207.png)

### textract

what

AWS의 OCR서비스

Amazon Textract는 스캔한 문서에서 텍스트, 필기 및 데이터를 자동으로 추출하는 기계 학습(ML) 서비스입니다. 단순한 광학 문자 인식(OCR) 이상으로 양식 및 표의 데이터를 식별하고 이해하며 추출합니다. 오늘날 많은 회사에서 PDF, 이미지, 표 및 양식과 같은 스캔 문서에서 또는 수동 구성이 필요한 간단한 OCR 소프트웨어(양식이 변경되면 종종 업데이트해야 함)를 통해 데이터를 수동으로 추출합니다.

### 개념

### Region / Availability Zone(AZ)

- [https://memory-hub.tistory.com/11](https://memory-hub.tistory.com/11)

Region은 여러 개의 Availability zone을 구성하는 단위 이며 전 세계에 여러 곳에 호스팅을 하고 있다. 

Availability Zone은 Region 내 물리적으로 존재하는 Internet Data Center(IDC)를 말한다. 

### VPC

- [https://medium.com/harrythegreat/aws-가장쉽게-vpc-개념잡기-71eef95a7098](https://medium.com/harrythegreat/aws-%EA%B0%80%EC%9E%A5%EC%89%BD%EA%B2%8C-vpc-%EA%B0%9C%EB%85%90%EC%9E%A1%EA%B8%B0-71eef95a7098)
- [https://memory-hub.tistory.com/11](https://memory-hub.tistory.com/11)

what

AWS 클라우드에서 다른 고객과 완벽하게 논리적으로 구분된 네트워크 환경을 말한다. 하위 항목으론 subnet이 있다. 

![Untitled](AWS%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20017bad637cf0490f9d7cc631debdac93/Untitled%208.png)

![Untitled](AWS%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20017bad637cf0490f9d7cc631debdac93/Untitled%209.png)

### Subnet

what

subnet은 VPC 내에 논리적으로 구분된 영역이자 VPC 내의 IP주소의 모음이다. 개별 subnet은 각자 독립된 IP를 갖고 있으며, Public, Private subset으로 활용할 수 있다. 

### VPC 외부 서비스와 VPC endpoints

- [https://aws-hyoh.tistory.com/73](https://aws-hyoh.tistory.com/73)
- [https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/what-are-vpc-endpoints.html](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/what-are-vpc-endpoints.html)
- EC2에서 S3 버킷에 접근할 때 퍼블릭 영역이 아닌 프라이빗 영역에서만 접근할 수 있도록 하여 보다 안전한 통신 구성을 하는 방법
[https://blog.nuricloud.com/aws-vpc-endpoint-using-for-s3-ec2-secure-transfer/#:~:text=본 기능 구성에 필요한,트래픽 비용이 발생합니다](https://blog.nuricloud.com/aws-vpc-endpoint-using-for-s3-ec2-secure-transfer/#:~:text=%EB%B3%B8%20%EA%B8%B0%EB%8A%A5%20%EA%B5%AC%EC%84%B1%EC%97%90%20%ED%95%84%EC%9A%94%ED%95%9C,%ED%8A%B8%EB%9E%98%ED%94%BD%20%EB%B9%84%EC%9A%A9%EC%9D%B4%20%EB%B0%9C%EC%83%9D%ED%95%A9%EB%8B%88%EB%8B%A4).
- VPC 외부 서비스에는 S3, Dynamo DB, CloudWatch 등이 있다.
- VPC 외부에 존재하므로 Internet gateway 또는 NAT Gateway 등 외부 인터넷 전송 서비스를 이용한다.
- VPC endpoints는 외부 인터넷 전송 서비스를 타지 않고 백본 네트워크를 통해 접근할 수 있도록 지원한다.
- VPC Endpoint는 유료이며 약 $10/월 정도 고정 비용과 $3.5/1TB의 트래픽 비용이 발생합니다.
    
    ![Untitled](AWS%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20017bad637cf0490f9d7cc631debdac93/Untitled%2010.png)
    
- VPC endpoints를 사용할 때와 사용하지 않을 때 비교
    
    ![Untitled](AWS%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20017bad637cf0490f9d7cc631debdac93/Untitled%2011.png)
    

### Workload

Amazon 서비스, 고객의 App, Database, storage 등 AWS Infra에서 실행되는 프로그램들을 통칭해서 부르는 말 

### Single Sign On(SSO)

- [https://gruuuuu.github.io/security/ssofriends/](https://gruuuuu.github.io/security/ssofriends/)

what 

각 애플리케이션에서 로그인/인증 부분만 따로 떼어서 한 군데로 모아두어 한 번의 로그인으로 여러 다른 사이트를 자동 접속할 수 있도록 하는 방법.

![Untitled](AWS%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20017bad637cf0490f9d7cc631debdac93/Untitled%2012.png)

다양한 시스템을 운영 중에 있을 때 하나의 계정으로 모든 시스템을 사용할 수 있는 서비스 

![Untitled](AWS%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20017bad637cf0490f9d7cc631debdac93/Untitled%2013.png)

### Target Group

what

Target Group은 로드밸런서의 핵심 요소이다. 로드 밸런서가 타겟그룹에게 트래픽을 제공하기 때문이다. 이때 EC2 같은 인스턴스를 논리적 그룹으로 묶어놓은 것을 Target Group이라 부른다. 

### Tag

what 

aws 리소스를 조직하기 위한 메타데이터이다. key value로 구성되어 있다. 

> Tags are key and value pairs that act as metadata for organizing your AWS resources. With most AWS resources, you have the option of adding tags when you create the resource. Examples of resources include anAmazon Elastic Compute Cloud (Amazon EC2) instance, an Amazon Simple Storage Service (Amazon S3) bucket, or a secret in AWS Secrets Manager.

Tags can help you manage, identify, organize, search for, and filter resources.
> 

### MFA(Multi-Factor Authentification)

what

IAM에서 설정 가능하며, 보안 관련 추가적인 절차를 요구하도록 설정하는 기능이다. 

> MFA (Multi-Factor Authentication) is an additional layer of security for AWS accounts that requires users to provide two forms of authentication to access their account.
> 

### On-Demand Capacity Reservation

특정 AZ에서 타입, 크기, OS 모두를 보존하는 기능이다. 

### A bastion host

A bastion host is used as a secure gateway to access servers or resources that are located in a private network or subnet.

### A Web Application Firewall (WAF)

A Web Application Firewall (WAF) is a security service that helps protect web applications from common web exploits and attacks, such as SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF).

### Availability

availability refers to the ability of a system or service to be operational and accessible to users when needed.

### Origin Access Identity(OAI)

chat gpt

OAI in AWS stands for Origin Access Identity. An Origin Access Identity is a virtual user identity in Amazon Web Services (AWS) that can be used to restrict access to content stored in Amazon S3 buckets, CloudFront distributions, and other AWS resources.

활용 사례

By default, objects stored in an S3 bucket are private and can only be accessed by users who have the appropriate AWS credentials. However, if you want to serve those objects through CloudFront, you need to make them publicly accessible. This creates a security risk, as anyone with the object's URL can access it.

Using an OAI, you can restrict access to S3 objects to only the CloudFront distribution associated with the OAI. This ensures that objects cannot be accessed directly by end users, but only through the CloudFront distribution.

### Ongoing Replication Task

an ongoing replication task refers to a continuous process of replicating data between a source database and a target database in near real-time. This process is managed by the AWS Database Migration Service (DMS).

The ongoing replication task is designed to enable real-time data synchronization between two databases. This can be useful in scenarios where you need to migrate data between two databases, or when you need to keep two databases in sync for business or operational reasons

### Stateless & Stateful

[https://inpa.tistory.com/entry/WEB-📚-Stateful-Stateless-정리](https://inpa.tistory.com/entry/WEB-%F0%9F%93%9A-Stateful-Stateless-%EC%A0%95%EB%A6%AC)

- Stateful : 서버가 클라이언트의 상태를 보존함. 로그인을 하면 로그인이 풀리지 않고 유지되는 것
- Stateless : 단순 요청이 들어오면 응답을 보내는 역할만 수행

### Dedicated Instances

- 특정 고객에 종속된 인스턴스(고정적으로 계속 활용가능하다는 말)

Dedicated Instances are Amazon EC2 instances that run in a virtual private cloud (VPC) on hardware that's dedicated to a single customer.

### SQS Standard vs FIFO

- Standard : queue를 Asynchronus하게 처리한다.
- FIFO : queue를 순차적으로 처리한다.

### CloudWatch composite Alarm

Composite alarms determine their states by monitoring the states of other alarms. You can use composite alarms to reduce alarm noise.

### Aurora DB Cluster

An Aurora DB cluster is a database cluster that consists of a primary instance and up to 15 Aurora Replicas, which are read-only instances that replicate data from the primary instance. The primary instance handles all database writes and is automatically replicated to the Aurora Replicas.

### Lustre

Lustre is a high-performance distributed file system designed for use in large-scale computing environments, such as HPC (high-performance computing) clusters, supercomputers, and data centers

### field-level encryption

With Amazon CloudFront, you can enforce secure end-to-end connections to origin servers by using HTTPS. Field-level encryption adds an additional layer of security that lets you protect specific data throughout system processing so that only certain applications can see it.

### Amazon DynamoDB Accelerator

it's like a turbo boost for your DynamoDB tables. It's a fully managed, in-memory cache that speeds up the read and write performance of your DynamoDB tables, so you can get your data faster than ever before.

### Aurora AutoScaling & Aurora Replica

- Aurora Replica는 Read-Only만 되는 데이터베이스로 만들어짐

[https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html#Aurora.Replication.Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html#Aurora.Replication.Replicas)
2.3. How to back up database (postgres) automatically at 2am in the morning and
store it in a remote location like AWS s3 bucket storage?

# Ans:

first we need to create an environment to run your PostgreSQL database (we call this environment an instance), connect to the database.
we will do this by using  Amazon Relational Database Service (Amazon RDS) .

we will use Amazon RDS to create a PostgreSQL DB Instance with db.t2.micro DB instance class, 20 GB of storage, and automated backups enabled.
In the top right corner of the Amazon RDS console, select the Region in which you want to create the DB instance.

In the Create database section, choose Create database and you can select the engine.


After the database instance creation is complete and the status changes to available, you can connect to a database on the DB instance using any standard SQL client. In this step, we will download SQL Workbench, which is a popular SQL client.

In the next step, we will connect to the database you created using SQL Workbench.

a. After you have completed your download, install SQL Workbench.


## Connection With S3
First we need to create a new S3 bucket. we create the bucket with default properties. Specify a bucket name (unique) and the region.
We need to create IAM (Identity Access Management) policy to integrate S3 and RDS.
In the next step, we define an IAM role that uses the IAM policy we defined for the S3 bucket.
and then attach the IAM role with AWS RDS SQL Server.

## Once we have applied for the IAM role in the RDS instance, we can connect to the S3 bucket using the RDS SQL instance. RDS provides stored procedures to upload and download data from an S3 bucket. We need to use S3 ARN to access the S3 bucket and objects inside it. At a time, we can have two in-progress tasks in the queue. If we schedule any tasks, we should be careful that it should not override each other.

 Backing up your PostgreSQL databases is an important task and can typically be completed with the pg_dump utility, which uses the COPY command by default to create a schema and data dump of a PostgreSQL database. However, this process can become repetitive if you require regular backups for multiple PostgreSQL databases. If your PostgreSQL databases are hosted in the cloud, you can also take advantage of the automated backup feature provided by Amazon Relational Database Service (Amazon RDS) for PostgreSQL as well. This pattern describes how to automate regular backups for Amazon RDS for PostgreSQL DB instances using the pg_dump utility.

# To take backups, the AWS Lambda function must be able to access your databases.
A time-based Amazon CloudWatch Events event initiates a Lambda function that searches for specific backup tags applied to the metadata of the PostgreSQL DB instances on Amazon RDS

# steps:
1.Create an inventory table in DynamoDB
2.Create an SNS topic for failed job events in AWS Batch
3.Build a Docker image and push it to an Amazon ECR repository
4.Create the AWS Batch components
# 5.Create and schedule a Lambda function
Create a Lambda function that searches for tags on your PostgreSQL DB instances and identifies backup candidates. Make sure your Lambda function can identify the bkp:AutomatedDBDump = Active tag and all other required tags. Important: The Lambda function must also be able to add jobs to the AWS Batch job queue.
# 6.Create a time-based CloudWatch Events event.
Open the Amazon CloudWatch console and create a CloudWatch Events event that uses a cron expression to run your Lambda function on a regular schedule. 

# 7.Test the backup automation.
a.Create an Amazon KMS key.
Open the Amazon KMS console and create a KMS key that can be used to encrypt the Amazon RDS credentials stored in AWS Secrets Manager.
b.Open the AWS Secrets Manager console and store your Amazon RDS for PostgreSQL database credentials as a secret.
c.Open the Amazon RDS console and add tags to the PostgreSQL DB instances that you want to automatically back up. You can use the tags from the table in the Tools section. If you require backups from multiple PostgreSQL databases within the same Amazon RDS instance, then use -d test:-d test1 as the value for the bkp:pgdumpcommand tag.
# d.To verify the backup automation, you can either invoke the Lambda function or wait for the backup schedule to begin. After the backup process is complete, check that the DynamoDB inventory table has a valid backup entry for your PostgreSQL DB instances. If they match, then the backup automation process is successful.





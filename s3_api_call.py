//1.Create S3 Bucket - - - – - &gt;s3-apicall
//2.Create an AWS Lambda function
�� Step-by-Step Setup in Console
1. Go to AWS Console &gt; Lambda.
2. Click “Create function”
3. Choose:
○ Function name: apitos3
○ Runtime: Python 3.11

○ Architecture: x86_64
○ Permissions:
■ Go to IAM - - - – &gt; Role - - - - &gt; create role- - - &gt; lambda-s3-
uploader-role
■ Attach Permission Policies AmazonS3FullAccess
■ Create Role
○ Attach Role To lambda Function:
■ Now, go back to your Lambda Function in AWS Console.
■ Scroll down to the &quot;Configuration&quot;

Static Website Hosting on S3:

This is a very simple AWS process to host a static website in S3. 

S3 could be used to host a static website.

These are the steps to host a static website:

1. Creating a bucket
2. Enable static website hosting
3. Editing Block public acess so that public access is enable (This is not recommended by AWS but done for our process)
4. Adding a bucket policy to give some exclusive access to the bucket so that the bucket is accessible.
5. Configure an index document
6. Configure an error document
7. Testing your website endpoint
8. Clean up 

Notes:
Server side encryption is enabled for all objects in S3 buckets by default
S3 bucket could be used like a website
It is not recommended to remove the "Block public access" as it exposes the resource to the web
S3 only supports HTTP calls, if you want secure HTTPS endpoints then you need to use Cloudfront origin access control to setup HTTPS endpoints
Index document is to define the starting point of the webpage or website (part of setting up the 2. Enable static website hosting)
Error document is to support custom error points to throw an error (part of setting up the 2. Enable static website hosting)
Redirection rules is used to specify advanced redirection  (part of setting up the 2. Enable static website hosting)
The following are the keywords in the process (4. Adding a bucket policy to give some exclusive access to the bucket so that the bucket is accessible.)
  Effect - This is to define if the statement is to Allow or Deny
  Principal - Who are the users who are need to access the aws resource
  Action - what are the actions that the users need to do on the resource
  Resource - what is the resource at which we need to do the action on

References: 
https://docs.aws.amazon.com/AmazonS3/latest/userguide/HostingWebsiteOnS3Setup.html

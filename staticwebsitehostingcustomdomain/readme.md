I completed a simple static website hosting into a custom domain. The detailed steps are in the reference. I am going to write down the steps from my memory below:

1. I created a new domain - basically purchased one - it involved buying a domain as well as the hosted zone. The combined cost was $ 14.50.
2. Created two S3 buckets - one for the domain and subdomain. The domain will host the static website, and the subdomain will redirect the request to the domain. The name of the domain bucket should be same as the domain name, and name of the subdomain bucket should be www. and the domain name.
3. In the bucket 1 - we go to the properties go and enable the static website hosting give the name of the index file as index.html or whatever the bootstrap file should be.
4. In the bucket 2 - go and enable static website hosting but choose to redirect request. Choose the S3 bucket request as the destination.
5. Now we need to add content, add the index.html into the S3 bucket. Go and disable the Block Public Access in permission to allow public access to the S3 resource. Go and add the necessary policies to the S3 resource such that the accessibility of the bucket is available for the resource.
6. Go to Route 53 and 2 alias records - one to the domain, and another to the subdomain
7. Now test the websites in the browser with http://domain_name.com and http://www.domain_name.com

Reference:
https://docs.aws.amazon.com/AmazonS3/latest/userguide/website-hosting-custom-domain-walkthrough.html

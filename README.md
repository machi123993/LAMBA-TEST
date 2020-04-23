# LAMBDA-TEST

build.sh is a wrapper script that had three jobs

1. Create a lambda function
2. Create a ssm document
3. Invoke lambda function which has created in first step.

Create Lambda function -> It is AWS CLI command and I am passing Lambda as a zip file parameter as lambda always accepts zip file in order to create.

ssm document -> It is also an AWS CLI command with file location as a parameter.

Invoke Lambda -> For this as per the requirement you need to pass the key/ values as parameters to build.sh file as shown in script $1 $2 $3 $4 are the variables which I presumed as sample for passing params. Once running it will create lambda, create ssm and invoke lambda.

Once after you invoke it , it does the following

1. It will list all the Ec2 instance ids based on tags/values you passed.
2.It will pass instance ids to ssm ans ssm will execute on all the ids that came through.

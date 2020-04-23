#!/bin/bash

git clone ``` git url ```
export directory=`pwd`
cd $directory/gitlab-test/lambda-ssm-sample
ls -lstrh
export function_name=test_lambda_ssm_function
export rolearn=``` role arn ```
export lambda_file_location=$directory/gitlab-test/lambda-ssm-sample/test.zip
export tag1=$1
export val1=$2
export tag2=$3
export val2=$4

echo $tag1
echo $val2
export region=us-east-2
export ssm_doc_location=$directory/gitlab-test/lambda-ssm-sample/ssm_doc.json
export ssm_doc_name=test
export lambda_handler=lambda.list_instanceid


aws lambda create-function --function-name $function_name --runtime python3.6 --role $rolearn --handler $lambda_handler --zip-file "fileb://$lambda_file_location" --region $region

sleep 10

aws ssm create-document --content file://$ssm_doc_location --name $ssm_doc_name --document-type Command --region $region

sleep 10

aws lambda invoke --function-name $function_name --payload '{"tag1":"'"$tag1"'","val1":"'"$val1"'","tag2":"'"$tag2"'","val2":"'"$val2"'","region": "'"$region"'"}' response.json --region $region


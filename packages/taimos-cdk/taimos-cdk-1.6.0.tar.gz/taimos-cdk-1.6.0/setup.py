import json
import setuptools

kwargs = json.loads("""
{
    "name": "taimos-cdk",
    "version": "1.6.0",
    "description": "Higher level constructs for AWS CDK",
    "license": "Apache-2.0",
    "url": "https://github.com/taimos/cdk-constructs",
    "long_description_content_type": "text/markdown",
    "author": "Thorsten Hoeger<thorsten.hoeger@taimos.de>",
    "project_urls": {
        "Source": "https://github.com/taimos/cdk-constructs"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "taimos_cdk",
        "taimos_cdk._jsii"
    ],
    "package_data": {
        "taimos_cdk._jsii": [
            "taimos-cdk-constructs@1.6.0.jsii.tgz"
        ],
        "taimos_cdk": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.20.11",
        "publication>=0.0.3",
        "aws-cdk.alexa-ask~=1.19,>=1.19.0",
        "aws-cdk.aws-apigateway~=1.19,>=1.19.0",
        "aws-cdk.aws-certificatemanager~=1.19,>=1.19.0",
        "aws-cdk.aws-cloudformation~=1.19,>=1.19.0",
        "aws-cdk.aws-cloudfront~=1.19,>=1.19.0",
        "aws-cdk.aws-codebuild~=1.19,>=1.19.0",
        "aws-cdk.aws-codecommit~=1.19,>=1.19.0",
        "aws-cdk.aws-codepipeline~=1.19,>=1.19.0",
        "aws-cdk.aws-codepipeline-actions~=1.19,>=1.19.0",
        "aws-cdk.aws-ec2~=1.19,>=1.19.0",
        "aws-cdk.aws-ecr~=1.19,>=1.19.0",
        "aws-cdk.aws-elasticloadbalancingv2~=1.19,>=1.19.0",
        "aws-cdk.aws-events-targets~=1.19,>=1.19.0",
        "aws-cdk.aws-iam~=1.19,>=1.19.0",
        "aws-cdk.aws-logs~=1.19,>=1.19.0",
        "aws-cdk.aws-route53-patterns~=1.19,>=1.19.0",
        "aws-cdk.aws-s3-deployment~=1.19,>=1.19.0",
        "aws-cdk.aws-sam~=1.19,>=1.19.0",
        "aws-cdk.aws-secretsmanager~=1.19,>=1.19.0",
        "aws-cdk.aws-sns-subscriptions~=1.19,>=1.19.0",
        "aws-cdk.core~=1.19,>=1.19.0",
        "aws-cdk.custom-resources~=1.19,>=1.19.0"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Typing :: Typed",
        "License :: OSI Approved"
    ]
}
""")

with open('README.md') as fp:
    kwargs['long_description'] = fp.read()


setuptools.setup(**kwargs)

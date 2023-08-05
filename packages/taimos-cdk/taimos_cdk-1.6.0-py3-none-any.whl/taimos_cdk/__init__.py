"""
[![npm version](https://badge.fury.io/js/taimos-cdk-constructs.svg)](https://badge.fury.io/js/taimos-cdk-constructs)
[![PyPI version](https://badge.fury.io/py/taimos-cdk.svg)](https://badge.fury.io/py/taimos-cdk)
![Build Status](https://codebuild.eu-west-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoieEFBVDZIcTZpZUQxMm1LS1hqckdTdnhCdm5CSHRlOXB1WkIrK1d2OHplRERMb1ExNk9zMGRWcm5ZZXIwaWlnRDVyTkFDZWNDdTRYQWFSckx3OW1jYjJVPSIsIml2UGFyYW1ldGVyU3BlYyI6IjkrS3NacTN5NU4xU3FXNXMiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)

This repository contains a library with higher-level constructs for AWS CDK (https://github.com/awslabs/aws-cdk) written in TypeScript.

# Installation

You can install the library into your project using npm or pip.

```bash
npm install taimos-cdk-constructs

pip3 install taimos-cdk
```

# Constructs

* [Deployment Pipeline and Skill Blueprint for Alexa](lib/alexa/README.md)
* [Hosting for Single Page Application](lib/web/single-page-app.ts)
* [Simple CodeBuild project for NodeJS projects](lib/ci/simple-codebuild.ts)
* [Scheduled Lambda function](lib/serverless/scheduled-lambda.ts)
* [VPC Internal REST API](lib/serverless/internal-rest-api.ts)

# Contributing

We welcome community contributions and pull requests.

# License

The CDK construct library is distributed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

See [LICENSE](./LICENSE) and [NOTICE](./NOTICE) for more information.
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

import aws_cdk.alexa_ask
import aws_cdk.aws_apigateway
import aws_cdk.aws_certificatemanager
import aws_cdk.aws_cloudformation
import aws_cdk.aws_cloudfront
import aws_cdk.aws_codebuild
import aws_cdk.aws_codecommit
import aws_cdk.aws_codepipeline
import aws_cdk.aws_codepipeline_actions
import aws_cdk.aws_ec2
import aws_cdk.aws_ecr
import aws_cdk.aws_elasticloadbalancingv2
import aws_cdk.aws_events_targets
import aws_cdk.aws_iam
import aws_cdk.aws_logs
import aws_cdk.aws_route53_patterns
import aws_cdk.aws_s3_deployment
import aws_cdk.aws_sam
import aws_cdk.aws_secretsmanager
import aws_cdk.aws_sns_subscriptions
import aws_cdk.core
import aws_cdk.custom_resources

__jsii_assembly__ = jsii.JSIIAssembly.load("taimos-cdk-constructs", "1.6.0", __name__, "taimos-cdk-constructs@1.6.0.jsii.tgz")


@jsii.data_type(jsii_type="taimos-cdk-constructs.AlexaSkillConfig", jsii_struct_bases=[], name_mapping={'skill_id': 'skillId', 'skill_name': 'skillName', 'environment': 'environment', 'thundra_key': 'thundraKey', 'user_attribute': 'userAttribute'})
class AlexaSkillConfig():
    def __init__(self, *, skill_id: str, skill_name: str, environment: typing.Optional[typing.Mapping[str,str]]=None, thundra_key: typing.Optional[str]=None, user_attribute: typing.Optional[str]=None):
        """
        :param skill_id: The Alexa Skill id.
        :param skill_name: The Alexa Skill name.
        :param environment: Environement variables for the Lambda function.
        :param thundra_key: Optional API Key for Thundra.
        :param user_attribute: name of the user attribute for DynamoDB. Default: id
        """
        self._values = {
            'skill_id': skill_id,
            'skill_name': skill_name,
        }
        if environment is not None: self._values["environment"] = environment
        if thundra_key is not None: self._values["thundra_key"] = thundra_key
        if user_attribute is not None: self._values["user_attribute"] = user_attribute

    @builtins.property
    def skill_id(self) -> str:
        """The Alexa Skill id."""
        return self._values.get('skill_id')

    @builtins.property
    def skill_name(self) -> str:
        """The Alexa Skill name."""
        return self._values.get('skill_name')

    @builtins.property
    def environment(self) -> typing.Optional[typing.Mapping[str,str]]:
        """Environement variables for the Lambda function."""
        return self._values.get('environment')

    @builtins.property
    def thundra_key(self) -> typing.Optional[str]:
        """Optional API Key for Thundra."""
        return self._values.get('thundra_key')

    @builtins.property
    def user_attribute(self) -> typing.Optional[str]:
        """name of the user attribute for DynamoDB.

        default
        :default: id
        """
        return self._values.get('user_attribute')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'AlexaSkillConfig(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="taimos-cdk-constructs.AlexaSkillDeploymentConfig", jsii_struct_bases=[], name_mapping={'skill_id': 'skillId', 'skill_name': 'skillName', 'alexa_secret_id': 'alexaSecretId', 'branch': 'branch', 'github_owner': 'githubOwner', 'github_repo': 'githubRepo', 'github_secret_id': 'githubSecretId'})
class AlexaSkillDeploymentConfig():
    def __init__(self, *, skill_id: str, skill_name: str, alexa_secret_id: typing.Optional[str]=None, branch: typing.Optional[str]=None, github_owner: typing.Optional[str]=None, github_repo: typing.Optional[str]=None, github_secret_id: typing.Optional[str]=None):
        """
        :param skill_id: -
        :param skill_name: -
        :param alexa_secret_id: -
        :param branch: -
        :param github_owner: -
        :param github_repo: -
        :param github_secret_id: -
        """
        self._values = {
            'skill_id': skill_id,
            'skill_name': skill_name,
        }
        if alexa_secret_id is not None: self._values["alexa_secret_id"] = alexa_secret_id
        if branch is not None: self._values["branch"] = branch
        if github_owner is not None: self._values["github_owner"] = github_owner
        if github_repo is not None: self._values["github_repo"] = github_repo
        if github_secret_id is not None: self._values["github_secret_id"] = github_secret_id

    @builtins.property
    def skill_id(self) -> str:
        return self._values.get('skill_id')

    @builtins.property
    def skill_name(self) -> str:
        return self._values.get('skill_name')

    @builtins.property
    def alexa_secret_id(self) -> typing.Optional[str]:
        return self._values.get('alexa_secret_id')

    @builtins.property
    def branch(self) -> typing.Optional[str]:
        return self._values.get('branch')

    @builtins.property
    def github_owner(self) -> typing.Optional[str]:
        return self._values.get('github_owner')

    @builtins.property
    def github_repo(self) -> typing.Optional[str]:
        return self._values.get('github_repo')

    @builtins.property
    def github_secret_id(self) -> typing.Optional[str]:
        return self._values.get('github_secret_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'AlexaSkillDeploymentConfig(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class AlexaSkillPipelineStack(aws_cdk.core.Stack, metaclass=jsii.JSIIMeta, jsii_type="taimos-cdk-constructs.AlexaSkillPipelineStack"):
    def __init__(self, parent: aws_cdk.core.App, *, skill_id: str, skill_name: str, alexa_secret_id: typing.Optional[str]=None, branch: typing.Optional[str]=None, github_owner: typing.Optional[str]=None, github_repo: typing.Optional[str]=None, github_secret_id: typing.Optional[str]=None) -> None:
        """
        :param parent: -
        :param skill_id: -
        :param skill_name: -
        :param alexa_secret_id: -
        :param branch: -
        :param github_owner: -
        :param github_repo: -
        :param github_secret_id: -
        """
        config = AlexaSkillDeploymentConfig(skill_id=skill_id, skill_name=skill_name, alexa_secret_id=alexa_secret_id, branch=branch, github_owner=github_owner, github_repo=github_repo, github_secret_id=github_secret_id)

        jsii.create(AlexaSkillPipelineStack, self, [parent, config])


class AlexaSkillStack(aws_cdk.core.Stack, metaclass=jsii.JSIIMeta, jsii_type="taimos-cdk-constructs.AlexaSkillStack"):
    def __init__(self, parent: aws_cdk.core.App, *, skill_id: str, skill_name: str, environment: typing.Optional[typing.Mapping[str,str]]=None, thundra_key: typing.Optional[str]=None, user_attribute: typing.Optional[str]=None) -> None:
        """
        :param parent: -
        :param skill_id: The Alexa Skill id.
        :param skill_name: The Alexa Skill name.
        :param environment: Environement variables for the Lambda function.
        :param thundra_key: Optional API Key for Thundra.
        :param user_attribute: name of the user attribute for DynamoDB. Default: id
        """
        config = AlexaSkillConfig(skill_id=skill_id, skill_name=skill_name, environment=environment, thundra_key=thundra_key, user_attribute=user_attribute)

        jsii.create(AlexaSkillStack, self, [parent, config])


@jsii.implements(aws_cdk.aws_apigateway.IRestApi)
class InternalRestApi(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="taimos-cdk-constructs.InternalRestApi"):
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, domain_name: str, hosted_zone: aws_cdk.aws_route53.IHostedZone, vpc: aws_cdk.aws_ec2.IVpc, api_props: typing.Optional[aws_cdk.aws_apigateway.RestApiProps]=None, certificate: typing.Optional[aws_cdk.aws_certificatemanager.ICertificate]=None, security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param domain_name: The domain name to use for the internal API.
        :param hosted_zone: The Route53 HostedZone to add the domain to. This is used for ACM DNS validation too, if no certificate is provided.
        :param vpc: The VPC to deploy the internal ALB into.
        :param api_props: API properties for the underlying RestApi construct. Default: - None
        :param certificate: The certificate to use for the ALB listener. Default: - Use ACM to create a DNS validated certificate for the given domain name
        :param security_group: Security group to associate with the internal load balancer. Default: - A security group is created
        """
        props = InternalRestApiProps(domain_name=domain_name, hosted_zone=hosted_zone, vpc=vpc, api_props=api_props, certificate=certificate, security_group=security_group)

        jsii.create(InternalRestApi, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="alb")
    def alb(self) -> aws_cdk.aws_elasticloadbalancingv2.ApplicationLoadBalancer:
        """The underlying internal application load balancer."""
        return jsii.get(self, "alb")

    @builtins.property
    @jsii.member(jsii_name="api")
    def api(self) -> aws_cdk.aws_apigateway.RestApi:
        """The underlying RestApi."""
        return jsii.get(self, "api")

    @builtins.property
    @jsii.member(jsii_name="restApiId")
    def rest_api_id(self) -> str:
        """The ID of this API Gateway RestApi."""
        return jsii.get(self, "restApiId")

    @builtins.property
    @jsii.member(jsii_name="stack")
    def stack(self) -> aws_cdk.core.Stack:
        """The stack in which this resource is defined."""
        return jsii.get(self, "stack")


@jsii.data_type(jsii_type="taimos-cdk-constructs.InternalRestApiProps", jsii_struct_bases=[], name_mapping={'domain_name': 'domainName', 'hosted_zone': 'hostedZone', 'vpc': 'vpc', 'api_props': 'apiProps', 'certificate': 'certificate', 'security_group': 'securityGroup'})
class InternalRestApiProps():
    def __init__(self, *, domain_name: str, hosted_zone: aws_cdk.aws_route53.IHostedZone, vpc: aws_cdk.aws_ec2.IVpc, api_props: typing.Optional[aws_cdk.aws_apigateway.RestApiProps]=None, certificate: typing.Optional[aws_cdk.aws_certificatemanager.ICertificate]=None, security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]=None):
        """
        :param domain_name: The domain name to use for the internal API.
        :param hosted_zone: The Route53 HostedZone to add the domain to. This is used for ACM DNS validation too, if no certificate is provided.
        :param vpc: The VPC to deploy the internal ALB into.
        :param api_props: API properties for the underlying RestApi construct. Default: - None
        :param certificate: The certificate to use for the ALB listener. Default: - Use ACM to create a DNS validated certificate for the given domain name
        :param security_group: Security group to associate with the internal load balancer. Default: - A security group is created
        """
        if isinstance(api_props, dict): api_props = aws_cdk.aws_apigateway.RestApiProps(**api_props)
        self._values = {
            'domain_name': domain_name,
            'hosted_zone': hosted_zone,
            'vpc': vpc,
        }
        if api_props is not None: self._values["api_props"] = api_props
        if certificate is not None: self._values["certificate"] = certificate
        if security_group is not None: self._values["security_group"] = security_group

    @builtins.property
    def domain_name(self) -> str:
        """The domain name to use for the internal API."""
        return self._values.get('domain_name')

    @builtins.property
    def hosted_zone(self) -> aws_cdk.aws_route53.IHostedZone:
        """The Route53 HostedZone to add the domain to. This is used for ACM DNS validation too, if no certificate is provided."""
        return self._values.get('hosted_zone')

    @builtins.property
    def vpc(self) -> aws_cdk.aws_ec2.IVpc:
        """The VPC to deploy the internal ALB into."""
        return self._values.get('vpc')

    @builtins.property
    def api_props(self) -> typing.Optional[aws_cdk.aws_apigateway.RestApiProps]:
        """API properties for the underlying RestApi construct.

        default
        :default: - None
        """
        return self._values.get('api_props')

    @builtins.property
    def certificate(self) -> typing.Optional[aws_cdk.aws_certificatemanager.ICertificate]:
        """The certificate to use for the ALB listener.

        default
        :default: - Use ACM to create a DNS validated certificate for the given domain name
        """
        return self._values.get('certificate')

    @builtins.property
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        """Security group to associate with the internal load balancer.

        default
        :default: - A security group is created
        """
        return self._values.get('security_group')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'InternalRestApiProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class ScheduledLambda(aws_cdk.aws_lambda.Function, metaclass=jsii.JSIIMeta, jsii_type="taimos-cdk-constructs.ScheduledLambda"):
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, schedule: aws_cdk.aws_events.Schedule, input: typing.Optional[aws_cdk.aws_events.RuleTargetInput]=None, code: aws_cdk.aws_lambda.Code, handler: str, runtime: aws_cdk.aws_lambda.Runtime, allow_all_outbound: typing.Optional[bool]=None, dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue]=None, dead_letter_queue_enabled: typing.Optional[bool]=None, description: typing.Optional[str]=None, environment: typing.Optional[typing.Mapping[str,str]]=None, events: typing.Optional[typing.List[aws_cdk.aws_lambda.IEventSource]]=None, function_name: typing.Optional[str]=None, initial_policy: typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]=None, layers: typing.Optional[typing.List[aws_cdk.aws_lambda.ILayerVersion]]=None, log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays]=None, log_retention_role: typing.Optional[aws_cdk.aws_iam.IRole]=None, memory_size: typing.Optional[jsii.Number]=None, reserved_concurrent_executions: typing.Optional[jsii.Number]=None, role: typing.Optional[aws_cdk.aws_iam.IRole]=None, security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]=None, security_groups: typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]]=None, timeout: typing.Optional[aws_cdk.core.Duration]=None, tracing: typing.Optional[aws_cdk.aws_lambda.Tracing]=None, vpc: typing.Optional[aws_cdk.aws_ec2.IVpc]=None, vpc_subnets: typing.Optional[aws_cdk.aws_ec2.SubnetSelection]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param schedule: The schedule or rate (frequency) that determines when CloudWatch Events triggers the Lambda function. For more information, see Schedule Expression Syntax for Rules in the Amazon CloudWatch User Guide.
        :param input: The input to send to the lambda. Default: - use the CloudWatch Event
        :param code: The source code of your Lambda function. You can point to a file in an Amazon Simple Storage Service (Amazon S3) bucket or specify your source code as inline text.
        :param handler: The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-programmingmodel. NOTE: If you specify your source code as inline text by specifying the ZipFile property within the Code property, specify index.function_name as the handler.
        :param runtime: The runtime environment for the Lambda function that you are uploading. For valid values, see the Runtime property in the AWS Lambda Developer Guide.
        :param allow_all_outbound: Whether to allow the Lambda to send all network traffic. If set to false, you must individually add traffic rules to allow the Lambda to connect to network targets. Default: true
        :param dead_letter_queue: The SQS queue to use if DLQ is enabled. Default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        :param dead_letter_queue_enabled: Enabled DLQ. If ``deadLetterQueue`` is undefined, an SQS queue with default options will be defined for your Function. Default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        :param description: A description of the function. Default: - No description.
        :param environment: Key-value pairs that Lambda caches and makes available for your Lambda functions. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Lambda function source code. Default: - No environment variables.
        :param events: Event sources for this function. You can also add event sources using ``addEventSource``. Default: - No event sources.
        :param function_name: A name for the function. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.
        :param initial_policy: Initial policy statements to add to the created Lambda Role. You can call ``addToRolePolicy`` to the created lambda to add statements post creation. Default: - No policy statements are added to the created Lambda role.
        :param layers: A list of layers to add to the function's execution environment. You can configure your Lambda function to pull in additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies that can be used by mulitple functions. Default: - No layers.
        :param log_retention: The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``Infinity``. Default: - Logs never expire.
        :param log_retention_role: The IAM role for the Lambda function associated with the custom resource that sets the retention policy. Default: - A new role is created.
        :param memory_size: The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 128
        :param reserved_concurrent_executions: The maximum of concurrent executions you want to reserve for the function. Default: - No specific limit - account limit.
        :param role: Lambda execution role. This is the role that will be assumed by the function upon execution. It controls the permissions that the function will have. The Role must be assumable by the 'lambda.amazonaws.com' service principal. Default: - A unique role will be generated for this lambda function. Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        :param security_group: What security group to associate with the Lambda's network interfaces. This property is being deprecated, consider using securityGroups instead. Only used if 'vpc' is supplied. Use securityGroups property instead. Function constructor will throw an error if both are specified. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroups prop, a dedicated security group will be created for this function.
        :param security_groups: The list of security groups to associate with the Lambda's network interfaces. Only used if 'vpc' is supplied. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroup prop, a dedicated security group will be created for this function.
        :param timeout: The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.seconds(3)
        :param tracing: Enable AWS X-Ray Tracing for Lambda Function. Default: Tracing.Disabled
        :param vpc: VPC network to place Lambda network interfaces. Specify this if the Lambda function needs to access resources in a VPC. Default: - Function is not placed within a VPC.
        :param vpc_subnets: Where to place the network interfaces within the VPC. Only used if 'vpc' is supplied. Note: internet access for Lambdas requires a NAT gateway, so picking Public subnets is not allowed. Default: - Private subnets.
        """
        props = ScheduledLambdaProps(schedule=schedule, input=input, code=code, handler=handler, runtime=runtime, allow_all_outbound=allow_all_outbound, dead_letter_queue=dead_letter_queue, dead_letter_queue_enabled=dead_letter_queue_enabled, description=description, environment=environment, events=events, function_name=function_name, initial_policy=initial_policy, layers=layers, log_retention=log_retention, log_retention_role=log_retention_role, memory_size=memory_size, reserved_concurrent_executions=reserved_concurrent_executions, role=role, security_group=security_group, security_groups=security_groups, timeout=timeout, tracing=tracing, vpc=vpc, vpc_subnets=vpc_subnets)

        jsii.create(ScheduledLambda, self, [scope, id, props])


@jsii.data_type(jsii_type="taimos-cdk-constructs.ScheduledLambdaProps", jsii_struct_bases=[aws_cdk.aws_lambda.FunctionProps], name_mapping={'code': 'code', 'handler': 'handler', 'runtime': 'runtime', 'allow_all_outbound': 'allowAllOutbound', 'dead_letter_queue': 'deadLetterQueue', 'dead_letter_queue_enabled': 'deadLetterQueueEnabled', 'description': 'description', 'environment': 'environment', 'events': 'events', 'function_name': 'functionName', 'initial_policy': 'initialPolicy', 'layers': 'layers', 'log_retention': 'logRetention', 'log_retention_role': 'logRetentionRole', 'memory_size': 'memorySize', 'reserved_concurrent_executions': 'reservedConcurrentExecutions', 'role': 'role', 'security_group': 'securityGroup', 'security_groups': 'securityGroups', 'timeout': 'timeout', 'tracing': 'tracing', 'vpc': 'vpc', 'vpc_subnets': 'vpcSubnets', 'schedule': 'schedule', 'input': 'input'})
class ScheduledLambdaProps(aws_cdk.aws_lambda.FunctionProps):
    def __init__(self, *, code: aws_cdk.aws_lambda.Code, handler: str, runtime: aws_cdk.aws_lambda.Runtime, allow_all_outbound: typing.Optional[bool]=None, dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue]=None, dead_letter_queue_enabled: typing.Optional[bool]=None, description: typing.Optional[str]=None, environment: typing.Optional[typing.Mapping[str,str]]=None, events: typing.Optional[typing.List[aws_cdk.aws_lambda.IEventSource]]=None, function_name: typing.Optional[str]=None, initial_policy: typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]=None, layers: typing.Optional[typing.List[aws_cdk.aws_lambda.ILayerVersion]]=None, log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays]=None, log_retention_role: typing.Optional[aws_cdk.aws_iam.IRole]=None, memory_size: typing.Optional[jsii.Number]=None, reserved_concurrent_executions: typing.Optional[jsii.Number]=None, role: typing.Optional[aws_cdk.aws_iam.IRole]=None, security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]=None, security_groups: typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]]=None, timeout: typing.Optional[aws_cdk.core.Duration]=None, tracing: typing.Optional[aws_cdk.aws_lambda.Tracing]=None, vpc: typing.Optional[aws_cdk.aws_ec2.IVpc]=None, vpc_subnets: typing.Optional[aws_cdk.aws_ec2.SubnetSelection]=None, schedule: aws_cdk.aws_events.Schedule, input: typing.Optional[aws_cdk.aws_events.RuleTargetInput]=None):
        """
        :param code: The source code of your Lambda function. You can point to a file in an Amazon Simple Storage Service (Amazon S3) bucket or specify your source code as inline text.
        :param handler: The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-programmingmodel. NOTE: If you specify your source code as inline text by specifying the ZipFile property within the Code property, specify index.function_name as the handler.
        :param runtime: The runtime environment for the Lambda function that you are uploading. For valid values, see the Runtime property in the AWS Lambda Developer Guide.
        :param allow_all_outbound: Whether to allow the Lambda to send all network traffic. If set to false, you must individually add traffic rules to allow the Lambda to connect to network targets. Default: true
        :param dead_letter_queue: The SQS queue to use if DLQ is enabled. Default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        :param dead_letter_queue_enabled: Enabled DLQ. If ``deadLetterQueue`` is undefined, an SQS queue with default options will be defined for your Function. Default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        :param description: A description of the function. Default: - No description.
        :param environment: Key-value pairs that Lambda caches and makes available for your Lambda functions. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Lambda function source code. Default: - No environment variables.
        :param events: Event sources for this function. You can also add event sources using ``addEventSource``. Default: - No event sources.
        :param function_name: A name for the function. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.
        :param initial_policy: Initial policy statements to add to the created Lambda Role. You can call ``addToRolePolicy`` to the created lambda to add statements post creation. Default: - No policy statements are added to the created Lambda role.
        :param layers: A list of layers to add to the function's execution environment. You can configure your Lambda function to pull in additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies that can be used by mulitple functions. Default: - No layers.
        :param log_retention: The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``Infinity``. Default: - Logs never expire.
        :param log_retention_role: The IAM role for the Lambda function associated with the custom resource that sets the retention policy. Default: - A new role is created.
        :param memory_size: The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 128
        :param reserved_concurrent_executions: The maximum of concurrent executions you want to reserve for the function. Default: - No specific limit - account limit.
        :param role: Lambda execution role. This is the role that will be assumed by the function upon execution. It controls the permissions that the function will have. The Role must be assumable by the 'lambda.amazonaws.com' service principal. Default: - A unique role will be generated for this lambda function. Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        :param security_group: What security group to associate with the Lambda's network interfaces. This property is being deprecated, consider using securityGroups instead. Only used if 'vpc' is supplied. Use securityGroups property instead. Function constructor will throw an error if both are specified. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroups prop, a dedicated security group will be created for this function.
        :param security_groups: The list of security groups to associate with the Lambda's network interfaces. Only used if 'vpc' is supplied. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroup prop, a dedicated security group will be created for this function.
        :param timeout: The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.seconds(3)
        :param tracing: Enable AWS X-Ray Tracing for Lambda Function. Default: Tracing.Disabled
        :param vpc: VPC network to place Lambda network interfaces. Specify this if the Lambda function needs to access resources in a VPC. Default: - Function is not placed within a VPC.
        :param vpc_subnets: Where to place the network interfaces within the VPC. Only used if 'vpc' is supplied. Note: internet access for Lambdas requires a NAT gateway, so picking Public subnets is not allowed. Default: - Private subnets.
        :param schedule: The schedule or rate (frequency) that determines when CloudWatch Events triggers the Lambda function. For more information, see Schedule Expression Syntax for Rules in the Amazon CloudWatch User Guide.
        :param input: The input to send to the lambda. Default: - use the CloudWatch Event
        """
        if isinstance(vpc_subnets, dict): vpc_subnets = aws_cdk.aws_ec2.SubnetSelection(**vpc_subnets)
        self._values = {
            'code': code,
            'handler': handler,
            'runtime': runtime,
            'schedule': schedule,
        }
        if allow_all_outbound is not None: self._values["allow_all_outbound"] = allow_all_outbound
        if dead_letter_queue is not None: self._values["dead_letter_queue"] = dead_letter_queue
        if dead_letter_queue_enabled is not None: self._values["dead_letter_queue_enabled"] = dead_letter_queue_enabled
        if description is not None: self._values["description"] = description
        if environment is not None: self._values["environment"] = environment
        if events is not None: self._values["events"] = events
        if function_name is not None: self._values["function_name"] = function_name
        if initial_policy is not None: self._values["initial_policy"] = initial_policy
        if layers is not None: self._values["layers"] = layers
        if log_retention is not None: self._values["log_retention"] = log_retention
        if log_retention_role is not None: self._values["log_retention_role"] = log_retention_role
        if memory_size is not None: self._values["memory_size"] = memory_size
        if reserved_concurrent_executions is not None: self._values["reserved_concurrent_executions"] = reserved_concurrent_executions
        if role is not None: self._values["role"] = role
        if security_group is not None: self._values["security_group"] = security_group
        if security_groups is not None: self._values["security_groups"] = security_groups
        if timeout is not None: self._values["timeout"] = timeout
        if tracing is not None: self._values["tracing"] = tracing
        if vpc is not None: self._values["vpc"] = vpc
        if vpc_subnets is not None: self._values["vpc_subnets"] = vpc_subnets
        if input is not None: self._values["input"] = input

    @builtins.property
    def code(self) -> aws_cdk.aws_lambda.Code:
        """The source code of your Lambda function.

        You can point to a file in an
        Amazon Simple Storage Service (Amazon S3) bucket or specify your source
        code as inline text.
        """
        return self._values.get('code')

    @builtins.property
    def handler(self) -> str:
        """The name of the method within your code that Lambda calls to execute your function.

        The format includes the file name. It can also include
        namespaces and other qualifiers, depending on the runtime.
        For more information, see https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-programmingmodel.

        NOTE: If you specify your source code as inline text by specifying the
        ZipFile property within the Code property, specify index.function_name as
        the handler.
        """
        return self._values.get('handler')

    @builtins.property
    def runtime(self) -> aws_cdk.aws_lambda.Runtime:
        """The runtime environment for the Lambda function that you are uploading. For valid values, see the Runtime property in the AWS Lambda Developer Guide."""
        return self._values.get('runtime')

    @builtins.property
    def allow_all_outbound(self) -> typing.Optional[bool]:
        """Whether to allow the Lambda to send all network traffic.

        If set to false, you must individually add traffic rules to allow the
        Lambda to connect to network targets.

        default
        :default: true
        """
        return self._values.get('allow_all_outbound')

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[aws_cdk.aws_sqs.IQueue]:
        """The SQS queue to use if DLQ is enabled.

        default
        :default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        """
        return self._values.get('dead_letter_queue')

    @builtins.property
    def dead_letter_queue_enabled(self) -> typing.Optional[bool]:
        """Enabled DLQ.

        If ``deadLetterQueue`` is undefined,
        an SQS queue with default options will be defined for your Function.

        default
        :default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        """
        return self._values.get('dead_letter_queue_enabled')

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """A description of the function.

        default
        :default: - No description.
        """
        return self._values.get('description')

    @builtins.property
    def environment(self) -> typing.Optional[typing.Mapping[str,str]]:
        """Key-value pairs that Lambda caches and makes available for your Lambda functions.

        Use environment variables to apply configuration changes, such
        as test and production environment configurations, without changing your
        Lambda function source code.

        default
        :default: - No environment variables.
        """
        return self._values.get('environment')

    @builtins.property
    def events(self) -> typing.Optional[typing.List[aws_cdk.aws_lambda.IEventSource]]:
        """Event sources for this function.

        You can also add event sources using ``addEventSource``.

        default
        :default: - No event sources.
        """
        return self._values.get('events')

    @builtins.property
    def function_name(self) -> typing.Optional[str]:
        """A name for the function.

        default
        :default:

        - AWS CloudFormation generates a unique physical ID and uses that
          ID for the function's name. For more information, see Name Type.
        """
        return self._values.get('function_name')

    @builtins.property
    def initial_policy(self) -> typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]:
        """Initial policy statements to add to the created Lambda Role.

        You can call ``addToRolePolicy`` to the created lambda to add statements post creation.

        default
        :default: - No policy statements are added to the created Lambda role.
        """
        return self._values.get('initial_policy')

    @builtins.property
    def layers(self) -> typing.Optional[typing.List[aws_cdk.aws_lambda.ILayerVersion]]:
        """A list of layers to add to the function's execution environment.

        You can configure your Lambda function to pull in
        additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies
        that can be used by mulitple functions.

        default
        :default: - No layers.
        """
        return self._values.get('layers')

    @builtins.property
    def log_retention(self) -> typing.Optional[aws_cdk.aws_logs.RetentionDays]:
        """The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``Infinity``.

        default
        :default: - Logs never expire.
        """
        return self._values.get('log_retention')

    @builtins.property
    def log_retention_role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        """The IAM role for the Lambda function associated with the custom resource that sets the retention policy.

        default
        :default: - A new role is created.
        """
        return self._values.get('log_retention_role')

    @builtins.property
    def memory_size(self) -> typing.Optional[jsii.Number]:
        """The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide.

        default
        :default: 128
        """
        return self._values.get('memory_size')

    @builtins.property
    def reserved_concurrent_executions(self) -> typing.Optional[jsii.Number]:
        """The maximum of concurrent executions you want to reserve for the function.

        default
        :default: - No specific limit - account limit.

        see
        :see: https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html
        """
        return self._values.get('reserved_concurrent_executions')

    @builtins.property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        """Lambda execution role.

        This is the role that will be assumed by the function upon execution.
        It controls the permissions that the function will have. The Role must
        be assumable by the 'lambda.amazonaws.com' service principal.

        default
        :default:

        - A unique role will be generated for this lambda function.
          Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        """
        return self._values.get('role')

    @builtins.property
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        """What security group to associate with the Lambda's network interfaces. This property is being deprecated, consider using securityGroups instead.

        Only used if 'vpc' is supplied.

        Use securityGroups property instead.
        Function constructor will throw an error if both are specified.

        default
        :default:

        - If the function is placed within a VPC and a security group is
          not specified, either by this or securityGroups prop, a dedicated security
          group will be created for this function.

        deprecated
        :deprecated: - This property is deprecated, use securityGroups instead

        stability
        :stability: deprecated
        """
        return self._values.get('security_group')

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]]:
        """The list of security groups to associate with the Lambda's network interfaces.

        Only used if 'vpc' is supplied.

        default
        :default:

        - If the function is placed within a VPC and a security group is
          not specified, either by this or securityGroup prop, a dedicated security
          group will be created for this function.
        """
        return self._values.get('security_groups')

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.core.Duration]:
        """The function execution time (in seconds) after which Lambda terminates the function.

        Because the execution time affects cost, set this value
        based on the function's expected execution time.

        default
        :default: Duration.seconds(3)
        """
        return self._values.get('timeout')

    @builtins.property
    def tracing(self) -> typing.Optional[aws_cdk.aws_lambda.Tracing]:
        """Enable AWS X-Ray Tracing for Lambda Function.

        default
        :default: Tracing.Disabled
        """
        return self._values.get('tracing')

    @builtins.property
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        """VPC network to place Lambda network interfaces.

        Specify this if the Lambda function needs to access resources in a VPC.

        default
        :default: - Function is not placed within a VPC.
        """
        return self._values.get('vpc')

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        """Where to place the network interfaces within the VPC.

        Only used if 'vpc' is supplied. Note: internet access for Lambdas
        requires a NAT gateway, so picking Public subnets is not allowed.

        default
        :default: - Private subnets.
        """
        return self._values.get('vpc_subnets')

    @builtins.property
    def schedule(self) -> aws_cdk.aws_events.Schedule:
        """The schedule or rate (frequency) that determines when CloudWatch Events triggers the Lambda function.

        For more information, see Schedule Expression Syntax for
        Rules in the Amazon CloudWatch User Guide.

        see
        :see: http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html
        """
        return self._values.get('schedule')

    @builtins.property
    def input(self) -> typing.Optional[aws_cdk.aws_events.RuleTargetInput]:
        """The input to send to the lambda.

        default
        :default: - use the CloudWatch Event
        """
        return self._values.get('input')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'ScheduledLambdaProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="taimos-cdk-constructs.SimpleCodeBuildConfig", jsii_struct_bases=[], name_mapping={'github_owner': 'githubOwner', 'github_repo': 'githubRepo', 'alert_email': 'alertEmail', 'branch': 'branch', 'use_build_spec_file': 'useBuildSpecFile'})
class SimpleCodeBuildConfig():
    def __init__(self, *, github_owner: str, github_repo: str, alert_email: typing.Optional[str]=None, branch: typing.Optional[str]=None, use_build_spec_file: typing.Optional[bool]=None):
        """
        :param github_owner: -
        :param github_repo: -
        :param alert_email: -
        :param branch: -
        :param use_build_spec_file: -
        """
        self._values = {
            'github_owner': github_owner,
            'github_repo': github_repo,
        }
        if alert_email is not None: self._values["alert_email"] = alert_email
        if branch is not None: self._values["branch"] = branch
        if use_build_spec_file is not None: self._values["use_build_spec_file"] = use_build_spec_file

    @builtins.property
    def github_owner(self) -> str:
        return self._values.get('github_owner')

    @builtins.property
    def github_repo(self) -> str:
        return self._values.get('github_repo')

    @builtins.property
    def alert_email(self) -> typing.Optional[str]:
        return self._values.get('alert_email')

    @builtins.property
    def branch(self) -> typing.Optional[str]:
        return self._values.get('branch')

    @builtins.property
    def use_build_spec_file(self) -> typing.Optional[bool]:
        return self._values.get('use_build_spec_file')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SimpleCodeBuildConfig(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class SimpleCodeBuildStack(aws_cdk.core.Stack, metaclass=jsii.JSIIMeta, jsii_type="taimos-cdk-constructs.SimpleCodeBuildStack"):
    def __init__(self, parent: aws_cdk.core.App, *, github_owner: str, github_repo: str, alert_email: typing.Optional[str]=None, branch: typing.Optional[str]=None, use_build_spec_file: typing.Optional[bool]=None) -> None:
        """
        :param parent: -
        :param github_owner: -
        :param github_repo: -
        :param alert_email: -
        :param branch: -
        :param use_build_spec_file: -
        """
        config = SimpleCodeBuildConfig(github_owner=github_owner, github_repo=github_repo, alert_email=alert_email, branch=branch, use_build_spec_file=use_build_spec_file)

        jsii.create(SimpleCodeBuildStack, self, [parent, config])


class SinglePageAppHosting(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="taimos-cdk-constructs.SinglePageAppHosting"):
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, zone_name: str, cert_arn: typing.Optional[str]=None, redirect_to_apex: typing.Optional[bool]=None, web_folder: typing.Optional[str]=None, zone_id: typing.Optional[str]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param zone_name: Name of the HostedZone of the domain.
        :param cert_arn: The ARN of the certificate; Has to be in us-east-1 Default: - create a new certificate in us-east-1
        :param redirect_to_apex: Define if the main domain is with or without www. Default: false - Redirect example.com to www.example.com
        :param web_folder: local folder with contents for the website bucket. Default: - no file deployment
        :param zone_id: ID of the HostedZone of the domain. Default: - lookup zone from context using the zone name
        """
        props = SinglePageAppHostingProps(zone_name=zone_name, cert_arn=cert_arn, redirect_to_apex=redirect_to_apex, web_folder=web_folder, zone_id=zone_id)

        jsii.create(SinglePageAppHosting, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="distribution")
    def distribution(self) -> aws_cdk.aws_cloudfront.CloudFrontWebDistribution:
        return jsii.get(self, "distribution")

    @builtins.property
    @jsii.member(jsii_name="webBucket")
    def web_bucket(self) -> aws_cdk.aws_s3.Bucket:
        return jsii.get(self, "webBucket")


@jsii.data_type(jsii_type="taimos-cdk-constructs.SinglePageAppHostingProps", jsii_struct_bases=[], name_mapping={'zone_name': 'zoneName', 'cert_arn': 'certArn', 'redirect_to_apex': 'redirectToApex', 'web_folder': 'webFolder', 'zone_id': 'zoneId'})
class SinglePageAppHostingProps():
    def __init__(self, *, zone_name: str, cert_arn: typing.Optional[str]=None, redirect_to_apex: typing.Optional[bool]=None, web_folder: typing.Optional[str]=None, zone_id: typing.Optional[str]=None):
        """
        :param zone_name: Name of the HostedZone of the domain.
        :param cert_arn: The ARN of the certificate; Has to be in us-east-1 Default: - create a new certificate in us-east-1
        :param redirect_to_apex: Define if the main domain is with or without www. Default: false - Redirect example.com to www.example.com
        :param web_folder: local folder with contents for the website bucket. Default: - no file deployment
        :param zone_id: ID of the HostedZone of the domain. Default: - lookup zone from context using the zone name
        """
        self._values = {
            'zone_name': zone_name,
        }
        if cert_arn is not None: self._values["cert_arn"] = cert_arn
        if redirect_to_apex is not None: self._values["redirect_to_apex"] = redirect_to_apex
        if web_folder is not None: self._values["web_folder"] = web_folder
        if zone_id is not None: self._values["zone_id"] = zone_id

    @builtins.property
    def zone_name(self) -> str:
        """Name of the HostedZone of the domain."""
        return self._values.get('zone_name')

    @builtins.property
    def cert_arn(self) -> typing.Optional[str]:
        """The ARN of the certificate;

        Has to be in us-east-1

        default
        :default: - create a new certificate in us-east-1
        """
        return self._values.get('cert_arn')

    @builtins.property
    def redirect_to_apex(self) -> typing.Optional[bool]:
        """Define if the main domain is with or without www.

        default
        :default: false - Redirect example.com to www.example.com
        """
        return self._values.get('redirect_to_apex')

    @builtins.property
    def web_folder(self) -> typing.Optional[str]:
        """local folder with contents for the website bucket.

        default
        :default: - no file deployment
        """
        return self._values.get('web_folder')

    @builtins.property
    def zone_id(self) -> typing.Optional[str]:
        """ID of the HostedZone of the domain.

        default
        :default: - lookup zone from context using the zone name
        """
        return self._values.get('zone_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SinglePageAppHostingProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["AlexaSkillConfig", "AlexaSkillDeploymentConfig", "AlexaSkillPipelineStack", "AlexaSkillStack", "InternalRestApi", "InternalRestApiProps", "ScheduledLambda", "ScheduledLambdaProps", "SimpleCodeBuildConfig", "SimpleCodeBuildStack", "SinglePageAppHosting", "SinglePageAppHostingProps", "__jsii_assembly__"]

publication.publish()

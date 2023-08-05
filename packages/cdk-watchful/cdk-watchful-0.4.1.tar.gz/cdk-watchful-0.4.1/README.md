# cdk-watchful

[![CircleCI](https://circleci.com/gh/eladb/cdk-watchful.svg?style=svg)](https://circleci.com/gh/eladb/cdk-watchful)
[![python](https://img.shields.io/badge/jsii-python-blueviolet.svg)](https://pypi.org/project/cdk-watchful/)
[![typescript](https://img.shields.io/badge/jsii-typescript-blueviolet.svg)](https://www.npmjs.com/package/cdk-watchful)

> Watching your CDK back since 2019

Watchful is an [AWS CDK](https://github.com/awslabs/aws-cdk) construct library that makes it easy
to monitor CDK apps.

**TypeScript:**

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
from cdk_watchful import Watchful

wf = Watchful(self, "watchful")
wf.watch_dynamo_table("My Cute Little Table", my_table)
wf.watch_lambda_function("My Function", my_function)
wf.watch_api_gateway("My REST API", my_rest_api)
```

**Python:**

```python
from cdk_watchful import Watchful

wf = Watchful(self, 'watchful')
wf.watch_dynamo_table('My Cute Little Table', my_table)
wf.watch_lambda_function('My Function', my_function)
wf.watch_api_gateway('My REST API', my_rest_api)
```

And...

![](https://raw.githubusercontent.com/eladb/cdk-watchful/master/example/sample.png)

## Install

TypeScript/JavaScript:

```console
$ npm install cdk-watchful
```

Python:

```console
$ pip install cdk-watchful
```

## Initialize

To get started, just define a `Watchful` construct in your CDK app (code is in
TypeScript, but python will work too):

**TypeScript:**

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
from cdk_watchful import

wf = Watchful(self, "watchful",
    alarm_email="your@email.com"
)
```

**Python:**

```python
from cdk_watchful import Watchful

wf = Watchful(self, 'watchful', alarm_email='your@amil.com')
```

## Add Resources

Watchful manages a central dashboard and configures default alarming for:

* Amazon DynamoDB: `watchful.watchDynamoTable`
* AWS Lambda: `watchful.watchLambdaFunction`
* Amazon API Gateway: `watchful.watchApiGateway`
* [Request yours](https://github.com/eladb/cdk-watchful/issues/new)

## Watching Scopes

Watchful can also watch complete CDK construct scopes. It will automatically
discover all watchable resources within that scope (recursively), add them
to your dashboard and configure alarms for them.

**TypeScript:**

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
wf.watch_scope(storage_layer)
```

**Python:**

```python
wf.watch_scope(storage_layer)
```

## Example

See a more complete [example](https://github.com/eladb/cdk-watchful/blob/master/example/index.ts).

## License

[Apache 2.0](https://github.com/eladb/cdk-watchful/blob/master/LICENSE)

# CDK Constants

This repository contains constants that make it easier to work with the [aws-cdk](https://github.com/aws/aws-cdk) (CDK).

## Why?

The CDK is awesome but it currently lacks types when initializing constructs such as IAM service principals and managed policies. Finding the right construct names requires diving into AWS documentation. Because there is no verification of these construct initializers, errors are only surfaced after deployment and via a rollback.

This library aims to be an up to date constants library for all things AWS so the above never happens again!

## Quickstart

Install or update from npm

```
# install
npm i cdk-constants

# upgrade
npm i -g cdk-constants@latest
```

## Usage

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
from cdk_constants import ServicePrincipals, ManagedPolicies

lambda_role = Role(self, "lambdaDomainChecker",
    assumed_by=ServicePrincipal(ServicePrincipals.LAMBDA),
    managed_policies=[
        ManagedPolicy.from_aws_managed_policy_name(ManagedPolicies.AWS_LAMBDA_BASIC_EXECUTION_ROLE)
    ]
)
```

## Properties

### [ServicePrincipals](./src/principals.ts)

* enum of all AWS services principals

### [ManagedPolicies](./src/policies.ts)

* enum of all managed AWS policies

## Credits

`cdk-constants` wouldn't be possible without modules from the following authors

* [Jared Short](https://gist.github.com/shortjared): initial [gist](https://gist.github.com/shortjared/4c1e3fe52bdfa47522cfe5b41e5d6f22) of all service principals
* [Gene Wood](https://gist.github.com/gene1wood): [gist](https://gist.github.com/gene1wood/55b358748be3c314f956) to pull all aws managed policies

## Contributions

All contributors are welcome. As you are reading this, AWS has probably released a new service. Please see [CONTRIBUTING](CONTRIBUTING.md) for information on how to setup a development environment and submit code.

Some upcoming items on the roadmap:

* list of aws regions and azs, including gov and china
* list of all iam permissions
* jsii compilation into different languages that CDK supports

## License

cdk-constants is distributed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

See [LICENSE](./LICENSE) for more information.

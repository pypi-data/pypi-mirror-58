# mypy-boto3-pricing

Type annotations for
[boto3.Pricing 1.10.42](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/pricing.html#Pricing) service
compatible with [mypy](https://github.com/python/mypy), [VSCode](https://code.visualstudio.com/),
[PyCharm](https://www.jetbrains.com/pycharm/) and other tools.

More information can be found [here](https://vemel.github.io/mypy_boto3/).

- [mypy-boto3-pricing](#mypy-boto3-pricing)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `Pricing` service.

```bash
python -m pip install boto3-stubs[mypy-boto3-pricing]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking and auto-complete.

```python
import boto3

from mypy_boto3 import pricing
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_pricing as pricing

# Use this client as usual, now mypy can check if your code is valid.
# Check if your IDE supports function overloads,
# you probably do not need explicit type annotations
# client = boto3.client("pricing")
client: pricing.PricingClient = boto3.client("pricing")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: pricing.PricingClient = session.client("pricing")


# Paginators need type annotation on creation
describe_services_paginator: pricing.DescribeServicesPaginator = client.get_paginator("describe_services")
get_attribute_values_paginator: pricing.GetAttributeValuesPaginator = client.get_paginator("get_attribute_values")
get_products_paginator: pricing.GetProductsPaginator = client.get_paginator("get_products")
```

## How it works

Fully automated [builder](https://github.com/vemel/mypy_boto3) carefully generates
type annotations for each service, patiently waiting for `boto3` updates. It delivers
a drop-in type annotations for you and makes sure that:

- All available `boto3` services are covered.
- Each public class and method of every `boto3` service gets valid type annotations
  extracted from the documentation (blame `botocore` docs if types are incorrect).
- Type annotations include up-to-date documentation.
- Link to documentation is provided for every method.
- Code is processed by [black](https://github.com/psf/black) for readability.
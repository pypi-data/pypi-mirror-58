# mypy-boto3-mediapackage-vod

Type annotations for
[boto3.MediaPackageVod 1.10.42](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/mediapackage-vod.html#MediaPackageVod) service
compatible with [mypy](https://github.com/python/mypy), [VSCode](https://code.visualstudio.com/),
[PyCharm](https://www.jetbrains.com/pycharm/) and other tools.

More information can be found [here](https://vemel.github.io/mypy_boto3/).

- [mypy-boto3-mediapackage-vod](#mypy-boto3-mediapackage-vod)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `MediaPackageVod` service.

```bash
python -m pip install boto3-stubs[mypy-boto3-mediapackage-vod]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking and auto-complete.

```python
import boto3

from mypy_boto3 import mediapackage_vod
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_mediapackage_vod as mediapackage_vod

# Use this client as usual, now mypy can check if your code is valid.
# Check if your IDE supports function overloads,
# you probably do not need explicit type annotations
# client = boto3.client("mediapackage-vod")
client: mediapackage_vod.MediaPackageVodClient = boto3.client("mediapackage-vod")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: mediapackage_vod.MediaPackageVodClient = session.client("mediapackage-vod")


# Paginators need type annotation on creation
list_assets_paginator: mediapackage_vod.ListAssetsPaginator = client.get_paginator("list_assets")
list_packaging_configurations_paginator: mediapackage_vod.ListPackagingConfigurationsPaginator = client.get_paginator("list_packaging_configurations")
list_packaging_groups_paginator: mediapackage_vod.ListPackagingGroupsPaginator = client.get_paginator("list_packaging_groups")
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
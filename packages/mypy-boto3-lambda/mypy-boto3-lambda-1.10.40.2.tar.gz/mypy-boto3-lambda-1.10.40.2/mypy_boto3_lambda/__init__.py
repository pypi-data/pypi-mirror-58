"Main interface for lambda service"
from mypy_boto3_lambda.client import LambdaClient, LambdaClient as Client
from mypy_boto3_lambda.paginator import (
    ListAliasesPaginator,
    ListEventSourceMappingsPaginator,
    ListFunctionEventInvokeConfigsPaginator,
    ListFunctionsPaginator,
    ListLayerVersionsPaginator,
    ListLayersPaginator,
    ListProvisionedConcurrencyConfigsPaginator,
    ListVersionsByFunctionPaginator,
)
from mypy_boto3_lambda.waiter import (
    FunctionActiveWaiter,
    FunctionExistsWaiter,
    FunctionUpdatedWaiter,
)


__all__ = (
    "Client",
    "FunctionActiveWaiter",
    "FunctionExistsWaiter",
    "FunctionUpdatedWaiter",
    "LambdaClient",
    "ListAliasesPaginator",
    "ListEventSourceMappingsPaginator",
    "ListFunctionEventInvokeConfigsPaginator",
    "ListFunctionsPaginator",
    "ListLayerVersionsPaginator",
    "ListLayersPaginator",
    "ListProvisionedConcurrencyConfigsPaginator",
    "ListVersionsByFunctionPaginator",
)

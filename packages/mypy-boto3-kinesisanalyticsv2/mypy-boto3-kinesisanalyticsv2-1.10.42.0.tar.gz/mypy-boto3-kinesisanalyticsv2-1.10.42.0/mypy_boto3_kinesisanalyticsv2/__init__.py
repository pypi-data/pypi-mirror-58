"Main interface for kinesisanalyticsv2 service"
from mypy_boto3_kinesisanalyticsv2.client import (
    KinesisAnalyticsV2Client as Client,
    KinesisAnalyticsV2Client,
)
from mypy_boto3_kinesisanalyticsv2.paginator import (
    ListApplicationSnapshotsPaginator,
    ListApplicationsPaginator,
)


__all__ = (
    "Client",
    "KinesisAnalyticsV2Client",
    "ListApplicationSnapshotsPaginator",
    "ListApplicationsPaginator",
)

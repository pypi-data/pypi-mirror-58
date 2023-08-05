"Main interface for iotthingsgraph service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_iotthingsgraph.type_defs import (
    EntityFilterTypeDef,
    FlowTemplateFilterTypeDef,
    GetFlowTemplateRevisionsResponseTypeDef,
    GetSystemTemplateRevisionsResponseTypeDef,
    ListFlowExecutionMessagesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PaginatorConfigTypeDef,
    SearchEntitiesResponseTypeDef,
    SearchFlowExecutionsResponseTypeDef,
    SearchFlowTemplatesResponseTypeDef,
    SearchSystemInstancesResponseTypeDef,
    SearchSystemTemplatesResponseTypeDef,
    SearchThingsResponseTypeDef,
    SystemInstanceFilterTypeDef,
    SystemTemplateFilterTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetFlowTemplateRevisionsPaginator",
    "GetSystemTemplateRevisionsPaginator",
    "ListFlowExecutionMessagesPaginator",
    "ListTagsForResourcePaginator",
    "SearchEntitiesPaginator",
    "SearchFlowExecutionsPaginator",
    "SearchFlowTemplatesPaginator",
    "SearchSystemInstancesPaginator",
    "SearchSystemTemplatesPaginator",
    "SearchThingsPaginator",
)


class GetFlowTemplateRevisionsPaginator(Boto3Paginator):
    """
    [Paginator.GetFlowTemplateRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.GetFlowTemplateRevisions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, id: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetFlowTemplateRevisionsResponseTypeDef, None, None]:
        """
        [GetFlowTemplateRevisions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.GetFlowTemplateRevisions.paginate)
        """


class GetSystemTemplateRevisionsPaginator(Boto3Paginator):
    """
    [Paginator.GetSystemTemplateRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.GetSystemTemplateRevisions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, id: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetSystemTemplateRevisionsResponseTypeDef, None, None]:
        """
        [GetSystemTemplateRevisions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.GetSystemTemplateRevisions.paginate)
        """


class ListFlowExecutionMessagesPaginator(Boto3Paginator):
    """
    [Paginator.ListFlowExecutionMessages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.ListFlowExecutionMessages)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, flowExecutionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListFlowExecutionMessagesResponseTypeDef, None, None]:
        """
        [ListFlowExecutionMessages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.ListFlowExecutionMessages.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.ListTagsForResource)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, resourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTagsForResourceResponseTypeDef, None, None]:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.ListTagsForResource.paginate)
        """


class SearchEntitiesPaginator(Boto3Paginator):
    """
    [Paginator.SearchEntities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchEntities)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        entityTypes: List[
            Literal[
                "DEVICE",
                "SERVICE",
                "DEVICE_MODEL",
                "CAPABILITY",
                "STATE",
                "ACTION",
                "EVENT",
                "PROPERTY",
                "MAPPING",
                "ENUM",
            ]
        ],
        filters: List[EntityFilterTypeDef] = None,
        namespaceVersion: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchEntitiesResponseTypeDef, None, None]:
        """
        [SearchEntities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchEntities.paginate)
        """


class SearchFlowExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.SearchFlowExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchFlowExecutions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        systemInstanceId: str,
        flowExecutionId: str = None,
        startTime: datetime = None,
        endTime: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchFlowExecutionsResponseTypeDef, None, None]:
        """
        [SearchFlowExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchFlowExecutions.paginate)
        """


class SearchFlowTemplatesPaginator(Boto3Paginator):
    """
    [Paginator.SearchFlowTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchFlowTemplates)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        filters: List[FlowTemplateFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchFlowTemplatesResponseTypeDef, None, None]:
        """
        [SearchFlowTemplates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchFlowTemplates.paginate)
        """


class SearchSystemInstancesPaginator(Boto3Paginator):
    """
    [Paginator.SearchSystemInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchSystemInstances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        filters: List[SystemInstanceFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchSystemInstancesResponseTypeDef, None, None]:
        """
        [SearchSystemInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchSystemInstances.paginate)
        """


class SearchSystemTemplatesPaginator(Boto3Paginator):
    """
    [Paginator.SearchSystemTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchSystemTemplates)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        filters: List[SystemTemplateFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchSystemTemplatesResponseTypeDef, None, None]:
        """
        [SearchSystemTemplates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchSystemTemplates.paginate)
        """


class SearchThingsPaginator(Boto3Paginator):
    """
    [Paginator.SearchThings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchThings)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        entityId: str,
        namespaceVersion: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchThingsResponseTypeDef, None, None]:
        """
        [SearchThings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchThings.paginate)
        """

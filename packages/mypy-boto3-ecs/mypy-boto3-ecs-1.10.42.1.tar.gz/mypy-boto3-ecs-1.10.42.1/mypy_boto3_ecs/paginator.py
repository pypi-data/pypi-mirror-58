"Main interface for ecs service Paginators"
from __future__ import annotations

import sys
from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_ecs.type_defs import (
    ListAccountSettingsResponseTypeDef,
    ListAttributesResponseTypeDef,
    ListClustersResponseTypeDef,
    ListContainerInstancesResponseTypeDef,
    ListServicesResponseTypeDef,
    ListTaskDefinitionFamiliesResponseTypeDef,
    ListTaskDefinitionsResponseTypeDef,
    ListTasksResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAccountSettingsPaginator",
    "ListAttributesPaginator",
    "ListClustersPaginator",
    "ListContainerInstancesPaginator",
    "ListServicesPaginator",
    "ListTaskDefinitionFamiliesPaginator",
    "ListTaskDefinitionsPaginator",
    "ListTasksPaginator",
)


class ListAccountSettingsPaginator(Boto3Paginator):
    """
    [Paginator.ListAccountSettings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecs.html#ECS.Paginator.ListAccountSettings)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        name: Literal[
            "serviceLongArnFormat",
            "taskLongArnFormat",
            "containerInstanceLongArnFormat",
            "awsvpcTrunking",
            "containerInsights",
        ] = None,
        value: str = None,
        principalArn: str = None,
        effectiveSettings: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListAccountSettingsResponseTypeDef, None, None]:
        """
        [ListAccountSettings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecs.html#ECS.Paginator.ListAccountSettings.paginate)
        """


class ListAttributesPaginator(Boto3Paginator):
    """
    [Paginator.ListAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecs.html#ECS.Paginator.ListAttributes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        targetType: Literal["container-instance"],
        cluster: str = None,
        attributeName: str = None,
        attributeValue: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListAttributesResponseTypeDef, None, None]:
        """
        [ListAttributes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecs.html#ECS.Paginator.ListAttributes.paginate)
        """


class ListClustersPaginator(Boto3Paginator):
    """
    [Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecs.html#ECS.Paginator.ListClusters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListClustersResponseTypeDef, None, None]:
        """
        [ListClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecs.html#ECS.Paginator.ListClusters.paginate)
        """


class ListContainerInstancesPaginator(Boto3Paginator):
    """
    [Paginator.ListContainerInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecs.html#ECS.Paginator.ListContainerInstances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        cluster: str = None,
        filter: str = None,
        status: Literal[
            "ACTIVE", "DRAINING", "REGISTERING", "DEREGISTERING", "REGISTRATION_FAILED"
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListContainerInstancesResponseTypeDef, None, None]:
        """
        [ListContainerInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecs.html#ECS.Paginator.ListContainerInstances.paginate)
        """


class ListServicesPaginator(Boto3Paginator):
    """
    [Paginator.ListServices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecs.html#ECS.Paginator.ListServices)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        cluster: str = None,
        launchType: Literal["EC2", "FARGATE"] = None,
        schedulingStrategy: Literal["REPLICA", "DAEMON"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListServicesResponseTypeDef, None, None]:
        """
        [ListServices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecs.html#ECS.Paginator.ListServices.paginate)
        """


class ListTaskDefinitionFamiliesPaginator(Boto3Paginator):
    """
    [Paginator.ListTaskDefinitionFamilies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecs.html#ECS.Paginator.ListTaskDefinitionFamilies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        familyPrefix: str = None,
        status: Literal["ACTIVE", "INACTIVE", "ALL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListTaskDefinitionFamiliesResponseTypeDef, None, None]:
        """
        [ListTaskDefinitionFamilies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecs.html#ECS.Paginator.ListTaskDefinitionFamilies.paginate)
        """


class ListTaskDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.ListTaskDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecs.html#ECS.Paginator.ListTaskDefinitions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        familyPrefix: str = None,
        status: Literal["ACTIVE", "INACTIVE"] = None,
        sort: Literal["ASC", "DESC"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListTaskDefinitionsResponseTypeDef, None, None]:
        """
        [ListTaskDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecs.html#ECS.Paginator.ListTaskDefinitions.paginate)
        """


class ListTasksPaginator(Boto3Paginator):
    """
    [Paginator.ListTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecs.html#ECS.Paginator.ListTasks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        cluster: str = None,
        containerInstance: str = None,
        family: str = None,
        startedBy: str = None,
        serviceName: str = None,
        desiredStatus: Literal["RUNNING", "PENDING", "STOPPED"] = None,
        launchType: Literal["EC2", "FARGATE"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListTasksResponseTypeDef, None, None]:
        """
        [ListTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecs.html#ECS.Paginator.ListTasks.paginate)
        """

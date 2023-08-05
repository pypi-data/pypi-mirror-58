"Main interface for medialive service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_medialive.type_defs import (
    DescribeScheduleResponseTypeDef,
    ListChannelsResponseTypeDef,
    ListInputSecurityGroupsResponseTypeDef,
    ListInputsResponseTypeDef,
    ListMultiplexProgramsResponseTypeDef,
    ListMultiplexesResponseTypeDef,
    ListOfferingsResponseTypeDef,
    ListReservationsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "DescribeSchedulePaginator",
    "ListChannelsPaginator",
    "ListInputSecurityGroupsPaginator",
    "ListInputsPaginator",
    "ListMultiplexProgramsPaginator",
    "ListMultiplexesPaginator",
    "ListOfferingsPaginator",
    "ListReservationsPaginator",
)


class DescribeSchedulePaginator(Boto3Paginator):
    """
    [Paginator.DescribeSchedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Paginator.DescribeSchedule)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ChannelId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeScheduleResponseTypeDef, None, None]:
        """
        [DescribeSchedule.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Paginator.DescribeSchedule.paginate)
        """


class ListChannelsPaginator(Boto3Paginator):
    """
    [Paginator.ListChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Paginator.ListChannels)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListChannelsResponseTypeDef, None, None]:
        """
        [ListChannels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Paginator.ListChannels.paginate)
        """


class ListInputSecurityGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListInputSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Paginator.ListInputSecurityGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListInputSecurityGroupsResponseTypeDef, None, None]:
        """
        [ListInputSecurityGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Paginator.ListInputSecurityGroups.paginate)
        """


class ListInputsPaginator(Boto3Paginator):
    """
    [Paginator.ListInputs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Paginator.ListInputs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListInputsResponseTypeDef, None, None]:
        """
        [ListInputs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Paginator.ListInputs.paginate)
        """


class ListMultiplexProgramsPaginator(Boto3Paginator):
    """
    [Paginator.ListMultiplexPrograms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Paginator.ListMultiplexPrograms)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, MultiplexId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListMultiplexProgramsResponseTypeDef, None, None]:
        """
        [ListMultiplexPrograms.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Paginator.ListMultiplexPrograms.paginate)
        """


class ListMultiplexesPaginator(Boto3Paginator):
    """
    [Paginator.ListMultiplexes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Paginator.ListMultiplexes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListMultiplexesResponseTypeDef, None, None]:
        """
        [ListMultiplexes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Paginator.ListMultiplexes.paginate)
        """


class ListOfferingsPaginator(Boto3Paginator):
    """
    [Paginator.ListOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Paginator.ListOfferings)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ChannelClass: str = None,
        ChannelConfiguration: str = None,
        Codec: str = None,
        Duration: str = None,
        MaximumBitrate: str = None,
        MaximumFramerate: str = None,
        Resolution: str = None,
        ResourceType: str = None,
        SpecialFeature: str = None,
        VideoQuality: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListOfferingsResponseTypeDef, None, None]:
        """
        [ListOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Paginator.ListOfferings.paginate)
        """


class ListReservationsPaginator(Boto3Paginator):
    """
    [Paginator.ListReservations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Paginator.ListReservations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ChannelClass: str = None,
        Codec: str = None,
        MaximumBitrate: str = None,
        MaximumFramerate: str = None,
        Resolution: str = None,
        ResourceType: str = None,
        SpecialFeature: str = None,
        VideoQuality: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListReservationsResponseTypeDef, None, None]:
        """
        [ListReservations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Paginator.ListReservations.paginate)
        """

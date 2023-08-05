"Main interface for alexaforbusiness service Paginators"
from __future__ import annotations

import sys
from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_alexaforbusiness.type_defs import (
    FilterTypeDef,
    ListBusinessReportSchedulesResponseTypeDef,
    ListConferenceProvidersResponseTypeDef,
    ListDeviceEventsResponseTypeDef,
    ListSkillsResponseTypeDef,
    ListSkillsStoreCategoriesResponseTypeDef,
    ListSkillsStoreSkillsByCategoryResponseTypeDef,
    ListSmartHomeAppliancesResponseTypeDef,
    ListTagsResponseTypeDef,
    PaginatorConfigTypeDef,
    SearchDevicesResponseTypeDef,
    SearchProfilesResponseTypeDef,
    SearchRoomsResponseTypeDef,
    SearchSkillGroupsResponseTypeDef,
    SearchUsersResponseTypeDef,
    SortTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListBusinessReportSchedulesPaginator",
    "ListConferenceProvidersPaginator",
    "ListDeviceEventsPaginator",
    "ListSkillsPaginator",
    "ListSkillsStoreCategoriesPaginator",
    "ListSkillsStoreSkillsByCategoryPaginator",
    "ListSmartHomeAppliancesPaginator",
    "ListTagsPaginator",
    "SearchDevicesPaginator",
    "SearchProfilesPaginator",
    "SearchRoomsPaginator",
    "SearchSkillGroupsPaginator",
    "SearchUsersPaginator",
)


class ListBusinessReportSchedulesPaginator(Boto3Paginator):
    """
    [Paginator.ListBusinessReportSchedules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListBusinessReportSchedules)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListBusinessReportSchedulesResponseTypeDef, None, None]:
        """
        [ListBusinessReportSchedules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListBusinessReportSchedules.paginate)
        """


class ListConferenceProvidersPaginator(Boto3Paginator):
    """
    [Paginator.ListConferenceProviders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListConferenceProviders)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListConferenceProvidersResponseTypeDef, None, None]:
        """
        [ListConferenceProviders.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListConferenceProviders.paginate)
        """


class ListDeviceEventsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeviceEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListDeviceEvents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DeviceArn: str,
        EventType: Literal["CONNECTION_STATUS", "DEVICE_STATUS"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListDeviceEventsResponseTypeDef, None, None]:
        """
        [ListDeviceEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListDeviceEvents.paginate)
        """


class ListSkillsPaginator(Boto3Paginator):
    """
    [Paginator.ListSkills documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkills)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SkillGroupArn: str = None,
        EnablementType: Literal["ENABLED", "PENDING"] = None,
        SkillType: Literal["PUBLIC", "PRIVATE", "ALL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListSkillsResponseTypeDef, None, None]:
        """
        [ListSkills.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkills.paginate)
        """


class ListSkillsStoreCategoriesPaginator(Boto3Paginator):
    """
    [Paginator.ListSkillsStoreCategories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkillsStoreCategories)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSkillsStoreCategoriesResponseTypeDef, None, None]:
        """
        [ListSkillsStoreCategories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkillsStoreCategories.paginate)
        """


class ListSkillsStoreSkillsByCategoryPaginator(Boto3Paginator):
    """
    [Paginator.ListSkillsStoreSkillsByCategory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkillsStoreSkillsByCategory)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, CategoryId: int, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSkillsStoreSkillsByCategoryResponseTypeDef, None, None]:
        """
        [ListSkillsStoreSkillsByCategory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkillsStoreSkillsByCategory.paginate)
        """


class ListSmartHomeAppliancesPaginator(Boto3Paginator):
    """
    [Paginator.ListSmartHomeAppliances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSmartHomeAppliances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, RoomArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSmartHomeAppliancesResponseTypeDef, None, None]:
        """
        [ListSmartHomeAppliances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSmartHomeAppliances.paginate)
        """


class ListTagsPaginator(Boto3Paginator):
    """
    [Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListTags)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Arn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTagsResponseTypeDef, None, None]:
        """
        [ListTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListTags.paginate)
        """


class SearchDevicesPaginator(Boto3Paginator):
    """
    [Paginator.SearchDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchDevices)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        SortCriteria: List[SortTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchDevicesResponseTypeDef, None, None]:
        """
        [SearchDevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchDevices.paginate)
        """


class SearchProfilesPaginator(Boto3Paginator):
    """
    [Paginator.SearchProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchProfiles)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        SortCriteria: List[SortTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchProfilesResponseTypeDef, None, None]:
        """
        [SearchProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchProfiles.paginate)
        """


class SearchRoomsPaginator(Boto3Paginator):
    """
    [Paginator.SearchRooms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchRooms)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        SortCriteria: List[SortTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchRoomsResponseTypeDef, None, None]:
        """
        [SearchRooms.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchRooms.paginate)
        """


class SearchSkillGroupsPaginator(Boto3Paginator):
    """
    [Paginator.SearchSkillGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchSkillGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        SortCriteria: List[SortTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchSkillGroupsResponseTypeDef, None, None]:
        """
        [SearchSkillGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchSkillGroups.paginate)
        """


class SearchUsersPaginator(Boto3Paginator):
    """
    [Paginator.SearchUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchUsers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        SortCriteria: List[SortTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchUsersResponseTypeDef, None, None]:
        """
        [SearchUsers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchUsers.paginate)
        """

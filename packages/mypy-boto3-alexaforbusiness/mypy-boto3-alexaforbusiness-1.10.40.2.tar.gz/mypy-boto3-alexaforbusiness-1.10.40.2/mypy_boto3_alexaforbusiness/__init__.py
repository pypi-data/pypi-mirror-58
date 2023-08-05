"Main interface for alexaforbusiness service"
from mypy_boto3_alexaforbusiness.client import (
    AlexaForBusinessClient as Client,
    AlexaForBusinessClient,
)
from mypy_boto3_alexaforbusiness.paginator import (
    ListBusinessReportSchedulesPaginator,
    ListConferenceProvidersPaginator,
    ListDeviceEventsPaginator,
    ListSkillsPaginator,
    ListSkillsStoreCategoriesPaginator,
    ListSkillsStoreSkillsByCategoryPaginator,
    ListSmartHomeAppliancesPaginator,
    ListTagsPaginator,
    SearchDevicesPaginator,
    SearchProfilesPaginator,
    SearchRoomsPaginator,
    SearchSkillGroupsPaginator,
    SearchUsersPaginator,
)


__all__ = (
    "AlexaForBusinessClient",
    "Client",
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

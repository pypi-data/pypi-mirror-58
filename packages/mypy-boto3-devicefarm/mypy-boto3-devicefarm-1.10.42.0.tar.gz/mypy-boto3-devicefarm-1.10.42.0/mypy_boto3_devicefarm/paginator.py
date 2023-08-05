"Main interface for devicefarm service Paginators"
from __future__ import annotations

import sys
from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_devicefarm.type_defs import (
    DeviceFilterTypeDef,
    GetOfferingStatusResultTypeDef,
    ListArtifactsResultTypeDef,
    ListDeviceInstancesResultTypeDef,
    ListDevicePoolsResultTypeDef,
    ListDevicesResultTypeDef,
    ListInstanceProfilesResultTypeDef,
    ListJobsResultTypeDef,
    ListNetworkProfilesResultTypeDef,
    ListOfferingPromotionsResultTypeDef,
    ListOfferingTransactionsResultTypeDef,
    ListOfferingsResultTypeDef,
    ListProjectsResultTypeDef,
    ListRemoteAccessSessionsResultTypeDef,
    ListRunsResultTypeDef,
    ListSamplesResultTypeDef,
    ListSuitesResultTypeDef,
    ListTestsResultTypeDef,
    ListUniqueProblemsResultTypeDef,
    ListUploadsResultTypeDef,
    ListVPCEConfigurationsResultTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetOfferingStatusPaginator",
    "ListArtifactsPaginator",
    "ListDeviceInstancesPaginator",
    "ListDevicePoolsPaginator",
    "ListDevicesPaginator",
    "ListInstanceProfilesPaginator",
    "ListJobsPaginator",
    "ListNetworkProfilesPaginator",
    "ListOfferingPromotionsPaginator",
    "ListOfferingTransactionsPaginator",
    "ListOfferingsPaginator",
    "ListProjectsPaginator",
    "ListRemoteAccessSessionsPaginator",
    "ListRunsPaginator",
    "ListSamplesPaginator",
    "ListSuitesPaginator",
    "ListTestsPaginator",
    "ListUniqueProblemsPaginator",
    "ListUploadsPaginator",
    "ListVPCEConfigurationsPaginator",
)


class GetOfferingStatusPaginator(Boto3Paginator):
    """
    [Paginator.GetOfferingStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.GetOfferingStatus)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetOfferingStatusResultTypeDef, None, None]:
        """
        [GetOfferingStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.GetOfferingStatus.paginate)
        """


class ListArtifactsPaginator(Boto3Paginator):
    """
    [Paginator.ListArtifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListArtifacts)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        arn: str,
        type: Literal["SCREENSHOT", "FILE", "LOG"],
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListArtifactsResultTypeDef, None, None]:
        """
        [ListArtifacts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListArtifacts.paginate)
        """


class ListDeviceInstancesPaginator(Boto3Paginator):
    """
    [Paginator.ListDeviceInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDeviceInstances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDeviceInstancesResultTypeDef, None, None]:
        """
        [ListDeviceInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDeviceInstances.paginate)
        """


class ListDevicePoolsPaginator(Boto3Paginator):
    """
    [Paginator.ListDevicePools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDevicePools)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        arn: str,
        type: Literal["CURATED", "PRIVATE"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListDevicePoolsResultTypeDef, None, None]:
        """
        [ListDevicePools.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDevicePools.paginate)
        """


class ListDevicesPaginator(Boto3Paginator):
    """
    [Paginator.ListDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDevices)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        arn: str = None,
        filters: List[DeviceFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListDevicesResultTypeDef, None, None]:
        """
        [ListDevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDevices.paginate)
        """


class ListInstanceProfilesPaginator(Boto3Paginator):
    """
    [Paginator.ListInstanceProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListInstanceProfiles)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListInstanceProfilesResultTypeDef, None, None]:
        """
        [ListInstanceProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListInstanceProfiles.paginate)
        """


class ListJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, arn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListJobsResultTypeDef, None, None]:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListJobs.paginate)
        """


class ListNetworkProfilesPaginator(Boto3Paginator):
    """
    [Paginator.ListNetworkProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListNetworkProfiles)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        arn: str,
        type: Literal["CURATED", "PRIVATE"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListNetworkProfilesResultTypeDef, None, None]:
        """
        [ListNetworkProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListNetworkProfiles.paginate)
        """


class ListOfferingPromotionsPaginator(Boto3Paginator):
    """
    [Paginator.ListOfferingPromotions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferingPromotions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListOfferingPromotionsResultTypeDef, None, None]:
        """
        [ListOfferingPromotions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferingPromotions.paginate)
        """


class ListOfferingTransactionsPaginator(Boto3Paginator):
    """
    [Paginator.ListOfferingTransactions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferingTransactions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListOfferingTransactionsResultTypeDef, None, None]:
        """
        [ListOfferingTransactions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferingTransactions.paginate)
        """


class ListOfferingsPaginator(Boto3Paginator):
    """
    [Paginator.ListOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferings)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListOfferingsResultTypeDef, None, None]:
        """
        [ListOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferings.paginate)
        """


class ListProjectsPaginator(Boto3Paginator):
    """
    [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListProjects)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, arn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListProjectsResultTypeDef, None, None]:
        """
        [ListProjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListProjects.paginate)
        """


class ListRemoteAccessSessionsPaginator(Boto3Paginator):
    """
    [Paginator.ListRemoteAccessSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListRemoteAccessSessions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, arn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListRemoteAccessSessionsResultTypeDef, None, None]:
        """
        [ListRemoteAccessSessions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListRemoteAccessSessions.paginate)
        """


class ListRunsPaginator(Boto3Paginator):
    """
    [Paginator.ListRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListRuns)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, arn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListRunsResultTypeDef, None, None]:
        """
        [ListRuns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListRuns.paginate)
        """


class ListSamplesPaginator(Boto3Paginator):
    """
    [Paginator.ListSamples documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListSamples)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, arn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSamplesResultTypeDef, None, None]:
        """
        [ListSamples.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListSamples.paginate)
        """


class ListSuitesPaginator(Boto3Paginator):
    """
    [Paginator.ListSuites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListSuites)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, arn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSuitesResultTypeDef, None, None]:
        """
        [ListSuites.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListSuites.paginate)
        """


class ListTestsPaginator(Boto3Paginator):
    """
    [Paginator.ListTests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListTests)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, arn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTestsResultTypeDef, None, None]:
        """
        [ListTests.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListTests.paginate)
        """


class ListUniqueProblemsPaginator(Boto3Paginator):
    """
    [Paginator.ListUniqueProblems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListUniqueProblems)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, arn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListUniqueProblemsResultTypeDef, None, None]:
        """
        [ListUniqueProblems.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListUniqueProblems.paginate)
        """


class ListUploadsPaginator(Boto3Paginator):
    """
    [Paginator.ListUploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListUploads)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        arn: str,
        type: Literal[
            "ANDROID_APP",
            "IOS_APP",
            "WEB_APP",
            "EXTERNAL_DATA",
            "APPIUM_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_PYTHON_TEST_PACKAGE",
            "APPIUM_NODE_TEST_PACKAGE",
            "APPIUM_RUBY_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_WEB_PYTHON_TEST_PACKAGE",
            "APPIUM_WEB_NODE_TEST_PACKAGE",
            "APPIUM_WEB_RUBY_TEST_PACKAGE",
            "CALABASH_TEST_PACKAGE",
            "INSTRUMENTATION_TEST_PACKAGE",
            "UIAUTOMATION_TEST_PACKAGE",
            "UIAUTOMATOR_TEST_PACKAGE",
            "XCTEST_TEST_PACKAGE",
            "XCTEST_UI_TEST_PACKAGE",
            "APPIUM_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_PYTHON_TEST_SPEC",
            "APPIUM_NODE_TEST_SPEC",
            "APPIUM_RUBY_TEST_SPEC",
            "APPIUM_WEB_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_WEB_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_WEB_PYTHON_TEST_SPEC",
            "APPIUM_WEB_NODE_TEST_SPEC",
            "APPIUM_WEB_RUBY_TEST_SPEC",
            "INSTRUMENTATION_TEST_SPEC",
            "XCTEST_UI_TEST_SPEC",
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListUploadsResultTypeDef, None, None]:
        """
        [ListUploads.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListUploads.paginate)
        """


class ListVPCEConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.ListVPCEConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListVPCEConfigurations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListVPCEConfigurationsResultTypeDef, None, None]:
        """
        [ListVPCEConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListVPCEConfigurations.paginate)
        """

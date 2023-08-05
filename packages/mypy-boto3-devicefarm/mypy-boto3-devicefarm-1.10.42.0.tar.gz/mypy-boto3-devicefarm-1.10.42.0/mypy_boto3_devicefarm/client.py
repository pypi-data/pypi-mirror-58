"Main interface for devicefarm service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_devicefarm.client as client_scope

# pylint: disable=import-self
import mypy_boto3_devicefarm.paginator as paginator_scope
from mypy_boto3_devicefarm.type_defs import (
    CreateDevicePoolResultTypeDef,
    CreateInstanceProfileResultTypeDef,
    CreateNetworkProfileResultTypeDef,
    CreateProjectResultTypeDef,
    CreateRemoteAccessSessionConfigurationTypeDef,
    CreateRemoteAccessSessionResultTypeDef,
    CreateUploadResultTypeDef,
    CreateVPCEConfigurationResultTypeDef,
    DeviceFilterTypeDef,
    DeviceSelectionConfigurationTypeDef,
    ExecutionConfigurationTypeDef,
    GetAccountSettingsResultTypeDef,
    GetDeviceInstanceResultTypeDef,
    GetDevicePoolCompatibilityResultTypeDef,
    GetDevicePoolResultTypeDef,
    GetDeviceResultTypeDef,
    GetInstanceProfileResultTypeDef,
    GetJobResultTypeDef,
    GetNetworkProfileResultTypeDef,
    GetOfferingStatusResultTypeDef,
    GetProjectResultTypeDef,
    GetRemoteAccessSessionResultTypeDef,
    GetRunResultTypeDef,
    GetSuiteResultTypeDef,
    GetTestResultTypeDef,
    GetUploadResultTypeDef,
    GetVPCEConfigurationResultTypeDef,
    InstallToRemoteAccessSessionResultTypeDef,
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
    ListTagsForResourceResponseTypeDef,
    ListTestsResultTypeDef,
    ListUniqueProblemsResultTypeDef,
    ListUploadsResultTypeDef,
    ListVPCEConfigurationsResultTypeDef,
    PurchaseOfferingResultTypeDef,
    RenewOfferingResultTypeDef,
    RuleTypeDef,
    ScheduleRunConfigurationTypeDef,
    ScheduleRunResultTypeDef,
    ScheduleRunTestTypeDef,
    StopJobResultTypeDef,
    StopRemoteAccessSessionResultTypeDef,
    StopRunResultTypeDef,
    TagTypeDef,
    UpdateDeviceInstanceResultTypeDef,
    UpdateDevicePoolResultTypeDef,
    UpdateInstanceProfileResultTypeDef,
    UpdateNetworkProfileResultTypeDef,
    UpdateProjectResultTypeDef,
    UpdateUploadResultTypeDef,
    UpdateVPCEConfigurationResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DeviceFarmClient",)


class DeviceFarmClient(BaseClient):
    """
    [DeviceFarm.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_device_pool(
        self,
        projectArn: str,
        name: str,
        rules: List[RuleTypeDef],
        description: str = None,
        maxDevices: int = None,
    ) -> CreateDevicePoolResultTypeDef:
        """
        [Client.create_device_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.create_device_pool)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_instance_profile(
        self,
        name: str,
        description: str = None,
        packageCleanup: bool = None,
        excludeAppPackagesFromCleanup: List[str] = None,
        rebootAfterUse: bool = None,
    ) -> CreateInstanceProfileResultTypeDef:
        """
        [Client.create_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.create_instance_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_network_profile(
        self,
        projectArn: str,
        name: str,
        description: str = None,
        type: Literal["CURATED", "PRIVATE"] = None,
        uplinkBandwidthBits: int = None,
        downlinkBandwidthBits: int = None,
        uplinkDelayMs: int = None,
        downlinkDelayMs: int = None,
        uplinkJitterMs: int = None,
        downlinkJitterMs: int = None,
        uplinkLossPercent: int = None,
        downlinkLossPercent: int = None,
    ) -> CreateNetworkProfileResultTypeDef:
        """
        [Client.create_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.create_network_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_project(
        self, name: str, defaultJobTimeoutMinutes: int = None
    ) -> CreateProjectResultTypeDef:
        """
        [Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.create_project)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_remote_access_session(
        self,
        projectArn: str,
        deviceArn: str,
        instanceArn: str = None,
        sshPublicKey: str = None,
        remoteDebugEnabled: bool = None,
        remoteRecordEnabled: bool = None,
        remoteRecordAppArn: str = None,
        name: str = None,
        clientId: str = None,
        configuration: CreateRemoteAccessSessionConfigurationTypeDef = None,
        interactionMode: Literal["INTERACTIVE", "NO_VIDEO", "VIDEO_ONLY"] = None,
        skipAppResign: bool = None,
    ) -> CreateRemoteAccessSessionResultTypeDef:
        """
        [Client.create_remote_access_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.create_remote_access_session)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_upload(
        self,
        projectArn: str,
        name: str,
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
        ],
        contentType: str = None,
    ) -> CreateUploadResultTypeDef:
        """
        [Client.create_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.create_upload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_vpce_configuration(
        self,
        vpceConfigurationName: str,
        vpceServiceName: str,
        serviceDnsName: str,
        vpceConfigurationDescription: str = None,
    ) -> CreateVPCEConfigurationResultTypeDef:
        """
        [Client.create_vpce_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.create_vpce_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_device_pool(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_device_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.delete_device_pool)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_instance_profile(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.delete_instance_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_network_profile(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.delete_network_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_project(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.delete_project)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_remote_access_session(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_remote_access_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.delete_remote_access_session)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_run(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.delete_run)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_upload(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.delete_upload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_vpce_configuration(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_vpce_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.delete_vpce_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_account_settings(self) -> GetAccountSettingsResultTypeDef:
        """
        [Client.get_account_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.get_account_settings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_device(self, arn: str) -> GetDeviceResultTypeDef:
        """
        [Client.get_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.get_device)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_device_instance(self, arn: str) -> GetDeviceInstanceResultTypeDef:
        """
        [Client.get_device_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.get_device_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_device_pool(self, arn: str) -> GetDevicePoolResultTypeDef:
        """
        [Client.get_device_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.get_device_pool)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_device_pool_compatibility(
        self,
        devicePoolArn: str,
        appArn: str = None,
        testType: Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ] = None,
        test: ScheduleRunTestTypeDef = None,
        configuration: ScheduleRunConfigurationTypeDef = None,
    ) -> GetDevicePoolCompatibilityResultTypeDef:
        """
        [Client.get_device_pool_compatibility documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.get_device_pool_compatibility)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_instance_profile(self, arn: str) -> GetInstanceProfileResultTypeDef:
        """
        [Client.get_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.get_instance_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_job(self, arn: str) -> GetJobResultTypeDef:
        """
        [Client.get_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.get_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_network_profile(self, arn: str) -> GetNetworkProfileResultTypeDef:
        """
        [Client.get_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.get_network_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_offering_status(self, nextToken: str = None) -> GetOfferingStatusResultTypeDef:
        """
        [Client.get_offering_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.get_offering_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_project(self, arn: str) -> GetProjectResultTypeDef:
        """
        [Client.get_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.get_project)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_remote_access_session(self, arn: str) -> GetRemoteAccessSessionResultTypeDef:
        """
        [Client.get_remote_access_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.get_remote_access_session)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_run(self, arn: str) -> GetRunResultTypeDef:
        """
        [Client.get_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.get_run)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_suite(self, arn: str) -> GetSuiteResultTypeDef:
        """
        [Client.get_suite documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.get_suite)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_test(self, arn: str) -> GetTestResultTypeDef:
        """
        [Client.get_test documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.get_test)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_upload(self, arn: str) -> GetUploadResultTypeDef:
        """
        [Client.get_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.get_upload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_vpce_configuration(self, arn: str) -> GetVPCEConfigurationResultTypeDef:
        """
        [Client.get_vpce_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.get_vpce_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def install_to_remote_access_session(
        self, remoteAccessSessionArn: str, appArn: str
    ) -> InstallToRemoteAccessSessionResultTypeDef:
        """
        [Client.install_to_remote_access_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.install_to_remote_access_session)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_artifacts(
        self, arn: str, type: Literal["SCREENSHOT", "FILE", "LOG"], nextToken: str = None
    ) -> ListArtifactsResultTypeDef:
        """
        [Client.list_artifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.list_artifacts)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_device_instances(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListDeviceInstancesResultTypeDef:
        """
        [Client.list_device_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.list_device_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_device_pools(
        self, arn: str, type: Literal["CURATED", "PRIVATE"] = None, nextToken: str = None
    ) -> ListDevicePoolsResultTypeDef:
        """
        [Client.list_device_pools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.list_device_pools)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_devices(
        self, arn: str = None, nextToken: str = None, filters: List[DeviceFilterTypeDef] = None
    ) -> ListDevicesResultTypeDef:
        """
        [Client.list_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.list_devices)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_instance_profiles(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListInstanceProfilesResultTypeDef:
        """
        [Client.list_instance_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.list_instance_profiles)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_jobs(self, arn: str, nextToken: str = None) -> ListJobsResultTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.list_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_network_profiles(
        self, arn: str, type: Literal["CURATED", "PRIVATE"] = None, nextToken: str = None
    ) -> ListNetworkProfilesResultTypeDef:
        """
        [Client.list_network_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.list_network_profiles)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_offering_promotions(
        self, nextToken: str = None
    ) -> ListOfferingPromotionsResultTypeDef:
        """
        [Client.list_offering_promotions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.list_offering_promotions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_offering_transactions(
        self, nextToken: str = None
    ) -> ListOfferingTransactionsResultTypeDef:
        """
        [Client.list_offering_transactions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.list_offering_transactions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_offerings(self, nextToken: str = None) -> ListOfferingsResultTypeDef:
        """
        [Client.list_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.list_offerings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_projects(self, arn: str = None, nextToken: str = None) -> ListProjectsResultTypeDef:
        """
        [Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.list_projects)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_remote_access_sessions(
        self, arn: str, nextToken: str = None
    ) -> ListRemoteAccessSessionsResultTypeDef:
        """
        [Client.list_remote_access_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.list_remote_access_sessions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_runs(self, arn: str, nextToken: str = None) -> ListRunsResultTypeDef:
        """
        [Client.list_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.list_runs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_samples(self, arn: str, nextToken: str = None) -> ListSamplesResultTypeDef:
        """
        [Client.list_samples documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.list_samples)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_suites(self, arn: str, nextToken: str = None) -> ListSuitesResultTypeDef:
        """
        [Client.list_suites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.list_suites)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tests(self, arn: str, nextToken: str = None) -> ListTestsResultTypeDef:
        """
        [Client.list_tests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.list_tests)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_unique_problems(
        self, arn: str, nextToken: str = None
    ) -> ListUniqueProblemsResultTypeDef:
        """
        [Client.list_unique_problems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.list_unique_problems)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_uploads(
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
        nextToken: str = None,
    ) -> ListUploadsResultTypeDef:
        """
        [Client.list_uploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.list_uploads)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_vpce_configurations(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListVPCEConfigurationsResultTypeDef:
        """
        [Client.list_vpce_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.list_vpce_configurations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def purchase_offering(
        self, offeringId: str = None, quantity: int = None, offeringPromotionId: str = None
    ) -> PurchaseOfferingResultTypeDef:
        """
        [Client.purchase_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.purchase_offering)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def renew_offering(
        self, offeringId: str = None, quantity: int = None
    ) -> RenewOfferingResultTypeDef:
        """
        [Client.renew_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.renew_offering)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def schedule_run(
        self,
        projectArn: str,
        test: ScheduleRunTestTypeDef,
        appArn: str = None,
        devicePoolArn: str = None,
        deviceSelectionConfiguration: DeviceSelectionConfigurationTypeDef = None,
        name: str = None,
        configuration: ScheduleRunConfigurationTypeDef = None,
        executionConfiguration: ExecutionConfigurationTypeDef = None,
    ) -> ScheduleRunResultTypeDef:
        """
        [Client.schedule_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.schedule_run)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_job(self, arn: str) -> StopJobResultTypeDef:
        """
        [Client.stop_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.stop_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_remote_access_session(self, arn: str) -> StopRemoteAccessSessionResultTypeDef:
        """
        [Client.stop_remote_access_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.stop_remote_access_session)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_run(self, arn: str) -> StopRunResultTypeDef:
        """
        [Client.stop_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.stop_run)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceARN: str, Tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_device_instance(
        self, arn: str, profileArn: str = None, labels: List[str] = None
    ) -> UpdateDeviceInstanceResultTypeDef:
        """
        [Client.update_device_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.update_device_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_device_pool(
        self,
        arn: str,
        name: str = None,
        description: str = None,
        rules: List[RuleTypeDef] = None,
        maxDevices: int = None,
        clearMaxDevices: bool = None,
    ) -> UpdateDevicePoolResultTypeDef:
        """
        [Client.update_device_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.update_device_pool)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_instance_profile(
        self,
        arn: str,
        name: str = None,
        description: str = None,
        packageCleanup: bool = None,
        excludeAppPackagesFromCleanup: List[str] = None,
        rebootAfterUse: bool = None,
    ) -> UpdateInstanceProfileResultTypeDef:
        """
        [Client.update_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.update_instance_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_network_profile(
        self,
        arn: str,
        name: str = None,
        description: str = None,
        type: Literal["CURATED", "PRIVATE"] = None,
        uplinkBandwidthBits: int = None,
        downlinkBandwidthBits: int = None,
        uplinkDelayMs: int = None,
        downlinkDelayMs: int = None,
        uplinkJitterMs: int = None,
        downlinkJitterMs: int = None,
        uplinkLossPercent: int = None,
        downlinkLossPercent: int = None,
    ) -> UpdateNetworkProfileResultTypeDef:
        """
        [Client.update_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.update_network_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_project(
        self, arn: str, name: str = None, defaultJobTimeoutMinutes: int = None
    ) -> UpdateProjectResultTypeDef:
        """
        [Client.update_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.update_project)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_upload(
        self, arn: str, name: str = None, contentType: str = None, editContent: bool = None
    ) -> UpdateUploadResultTypeDef:
        """
        [Client.update_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.update_upload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_vpce_configuration(
        self,
        arn: str,
        vpceConfigurationName: str = None,
        vpceServiceName: str = None,
        serviceDnsName: str = None,
        vpceConfigurationDescription: str = None,
    ) -> UpdateVPCEConfigurationResultTypeDef:
        """
        [Client.update_vpce_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Client.update_vpce_configuration)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_offering_status"]
    ) -> paginator_scope.GetOfferingStatusPaginator:
        """
        [Paginator.GetOfferingStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.GetOfferingStatus)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_artifacts"]
    ) -> paginator_scope.ListArtifactsPaginator:
        """
        [Paginator.ListArtifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListArtifacts)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_device_instances"]
    ) -> paginator_scope.ListDeviceInstancesPaginator:
        """
        [Paginator.ListDeviceInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDeviceInstances)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_device_pools"]
    ) -> paginator_scope.ListDevicePoolsPaginator:
        """
        [Paginator.ListDevicePools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDevicePools)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_devices"]
    ) -> paginator_scope.ListDevicesPaginator:
        """
        [Paginator.ListDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDevices)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_instance_profiles"]
    ) -> paginator_scope.ListInstanceProfilesPaginator:
        """
        [Paginator.ListInstanceProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListInstanceProfiles)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_jobs"]
    ) -> paginator_scope.ListJobsPaginator:
        """
        [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListJobs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_network_profiles"]
    ) -> paginator_scope.ListNetworkProfilesPaginator:
        """
        [Paginator.ListNetworkProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListNetworkProfiles)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_offering_promotions"]
    ) -> paginator_scope.ListOfferingPromotionsPaginator:
        """
        [Paginator.ListOfferingPromotions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferingPromotions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_offering_transactions"]
    ) -> paginator_scope.ListOfferingTransactionsPaginator:
        """
        [Paginator.ListOfferingTransactions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferingTransactions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_offerings"]
    ) -> paginator_scope.ListOfferingsPaginator:
        """
        [Paginator.ListOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferings)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_projects"]
    ) -> paginator_scope.ListProjectsPaginator:
        """
        [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListProjects)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_remote_access_sessions"]
    ) -> paginator_scope.ListRemoteAccessSessionsPaginator:
        """
        [Paginator.ListRemoteAccessSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListRemoteAccessSessions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_runs"]
    ) -> paginator_scope.ListRunsPaginator:
        """
        [Paginator.ListRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListRuns)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_samples"]
    ) -> paginator_scope.ListSamplesPaginator:
        """
        [Paginator.ListSamples documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListSamples)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_suites"]
    ) -> paginator_scope.ListSuitesPaginator:
        """
        [Paginator.ListSuites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListSuites)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_tests"]
    ) -> paginator_scope.ListTestsPaginator:
        """
        [Paginator.ListTests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListTests)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_unique_problems"]
    ) -> paginator_scope.ListUniqueProblemsPaginator:
        """
        [Paginator.ListUniqueProblems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListUniqueProblems)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_uploads"]
    ) -> paginator_scope.ListUploadsPaginator:
        """
        [Paginator.ListUploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListUploads)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_vpce_configurations"]
    ) -> paginator_scope.ListVPCEConfigurationsPaginator:
        """
        [Paginator.ListVPCEConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/devicefarm.html#DeviceFarm.Paginator.ListVPCEConfigurations)
        """


class Exceptions:
    ArgumentException: Boto3ClientError
    ClientError: Boto3ClientError
    IdempotencyException: Boto3ClientError
    InvalidOperationException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotEligibleException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ServiceAccountException: Boto3ClientError
    TagOperationException: Boto3ClientError
    TagPolicyException: Boto3ClientError
    TooManyTagsException: Boto3ClientError

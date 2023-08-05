"Main interface for opsworks service ServiceResource"
from __future__ import annotations

import sys
from typing import Any, Dict, List
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

# pylint: disable=import-self
import mypy_boto3_opsworks.service_resource as service_resource_scope
from mypy_boto3_opsworks.type_defs import (
    ChefConfigurationTypeDef,
    CloudWatchLogsConfigurationTypeDef,
    CreateLayerResultTypeDef,
    CreateStackResultTypeDef,
    LifecycleEventConfigurationTypeDef,
    RecipesTypeDef,
    SourceTypeDef,
    StackConfigurationManagerTypeDef,
    VolumeConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "OpsWorksServiceResource",
    "Layer",
    "Stack",
    "StackSummary",
    "ServiceResourceStacksCollection",
    "StackLayersCollection",
)


class OpsWorksServiceResource(Boto3ServiceResource):
    """
    [OpsWorks.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworks.html#OpsWorks.ServiceResource)
    """

    stacks: service_resource_scope.ServiceResourceStacksCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Layer(self, id: str) -> service_resource_scope.Layer:
        """
        [ServiceResource.Layer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworks.html#OpsWorks.ServiceResource.Layer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Stack(self, id: str) -> service_resource_scope.Stack:
        """
        [ServiceResource.Stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworks.html#OpsWorks.ServiceResource.Stack)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def StackSummary(self, stack_id: str) -> service_resource_scope.StackSummary:
        """
        [ServiceResource.StackSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworks.html#OpsWorks.ServiceResource.StackSummary)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_stack(
        self,
        Name: str,
        Region: str,
        ServiceRoleArn: str,
        DefaultInstanceProfileArn: str,
        VpcId: str = None,
        Attributes: Dict[Literal["Color"], str] = None,
        DefaultOs: str = None,
        HostnameTheme: str = None,
        DefaultAvailabilityZone: str = None,
        DefaultSubnetId: str = None,
        CustomJson: str = None,
        ConfigurationManager: StackConfigurationManagerTypeDef = None,
        ChefConfiguration: ChefConfigurationTypeDef = None,
        UseCustomCookbooks: bool = None,
        UseOpsworksSecurityGroups: bool = None,
        CustomCookbooksSource: SourceTypeDef = None,
        DefaultSshKeyName: str = None,
        DefaultRootDeviceType: Literal["ebs", "instance-store"] = None,
        AgentVersion: str = None,
    ) -> CreateStackResultTypeDef:
        """
        [ServiceResource.create_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworks.html#OpsWorks.ServiceResource.create_stack)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworks.html#OpsWorks.ServiceResource.get_available_subresources)
        """


class Layer(Boto3ServiceResource):
    """
    [Layer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworks.html#OpsWorks.ServiceResource.Layer)
    """

    arn: str
    stack_id: str
    layer_id: str
    type: str
    name: str
    shortname: str
    attributes: Dict[str, Any]
    cloud_watch_logs_configuration: Dict[str, Any]
    custom_instance_profile_arn: str
    custom_json: str
    custom_security_group_ids: List[Any]
    default_security_group_names: List[Any]
    packages: List[Any]
    volume_configurations: List[Any]
    enable_auto_healing: bool
    auto_assign_elastic_ips: bool
    auto_assign_public_ips: bool
    default_recipes: Dict[str, Any]
    custom_recipes: Dict[str, Any]
    created_at: str
    install_updates_on_boot: bool
    use_ebs_optimized_instances: bool
    lifecycle_event_configuration: Dict[str, Any]
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        """
        [Layer.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworks.html#OpsWorks.Layer.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [Layer.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworks.html#OpsWorks.Layer.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [Layer.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworks.html#OpsWorks.Layer.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [Layer.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworks.html#OpsWorks.Layer.reload)
        """


class Stack(Boto3ServiceResource):
    """
    [Stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworks.html#OpsWorks.ServiceResource.Stack)
    """

    stack_id: str
    name: str
    arn: str
    region: str
    vpc_id: str
    attributes: Dict[str, Any]
    service_role_arn: str
    default_instance_profile_arn: str
    default_os: str
    hostname_theme: str
    default_availability_zone: str
    default_subnet_id: str
    custom_json: str
    configuration_manager: Dict[str, Any]
    chef_configuration: Dict[str, Any]
    use_custom_cookbooks: bool
    use_opsworks_security_groups: bool
    custom_cookbooks_source: Dict[str, Any]
    default_ssh_key_name: str
    created_at: str
    default_root_device_type: str
    agent_version: str
    id: str
    layers: service_resource_scope.StackLayersCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_layer(
        self,
        Type: Literal[
            "aws-flow-ruby",
            "ecs-cluster",
            "java-app",
            "lb",
            "web",
            "php-app",
            "rails-app",
            "nodejs-app",
            "memcached",
            "db-master",
            "monitoring-master",
            "custom",
        ],
        Name: str,
        Shortname: str,
        Attributes: Dict[
            Literal[
                "EcsClusterArn",
                "EnableHaproxyStats",
                "HaproxyStatsUrl",
                "HaproxyStatsUser",
                "HaproxyStatsPassword",
                "HaproxyHealthCheckUrl",
                "HaproxyHealthCheckMethod",
                "MysqlRootPassword",
                "MysqlRootPasswordUbiquitous",
                "GangliaUrl",
                "GangliaUser",
                "GangliaPassword",
                "MemcachedMemory",
                "NodejsVersion",
                "RubyVersion",
                "RubygemsVersion",
                "ManageBundler",
                "BundlerVersion",
                "RailsStack",
                "PassengerVersion",
                "Jvm",
                "JvmVersion",
                "JvmOptions",
                "JavaAppServer",
                "JavaAppServerVersion",
            ],
            str,
        ] = None,
        CloudWatchLogsConfiguration: CloudWatchLogsConfigurationTypeDef = None,
        CustomInstanceProfileArn: str = None,
        CustomJson: str = None,
        CustomSecurityGroupIds: List[str] = None,
        Packages: List[str] = None,
        VolumeConfigurations: List[VolumeConfigurationTypeDef] = None,
        EnableAutoHealing: bool = None,
        AutoAssignElasticIps: bool = None,
        AutoAssignPublicIps: bool = None,
        CustomRecipes: RecipesTypeDef = None,
        InstallUpdatesOnBoot: bool = None,
        UseEbsOptimizedInstances: bool = None,
        LifecycleEventConfiguration: LifecycleEventConfigurationTypeDef = None,
    ) -> CreateLayerResultTypeDef:
        """
        [Stack.create_layer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworks.html#OpsWorks.Stack.create_layer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        """
        [Stack.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworks.html#OpsWorks.Stack.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [Stack.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworks.html#OpsWorks.Stack.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [Stack.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworks.html#OpsWorks.Stack.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [Stack.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworks.html#OpsWorks.Stack.reload)
        """


class StackSummary(Boto3ServiceResource):
    """
    [StackSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworks.html#OpsWorks.ServiceResource.StackSummary)
    """

    name: str
    arn: str
    layers_count: int
    apps_count: int
    instances_count: Dict[str, Any]
    stack_id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [StackSummary.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworks.html#OpsWorks.StackSummary.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [StackSummary.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworks.html#OpsWorks.StackSummary.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [StackSummary.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworks.html#OpsWorks.StackSummary.reload)
        """


class ServiceResourceStacksCollection(ResourceCollection):
    """
    [ServiceResource.stacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworks.html#OpsWorks.ServiceResource.stacks)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceStacksCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceStacksCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceStacksCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.ServiceResourceStacksCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Stack]:
        pass


class StackLayersCollection(ResourceCollection):
    """
    [Stack.layers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworks.html#OpsWorks.Stack.layers)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.StackLayersCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.StackLayersCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.StackLayersCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.StackLayersCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Layer]:
        pass

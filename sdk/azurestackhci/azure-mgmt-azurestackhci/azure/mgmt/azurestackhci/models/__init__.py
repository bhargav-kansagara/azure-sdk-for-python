# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ArcSetting
from ._models_py3 import ArcSettingList
from ._models_py3 import Cluster
from ._models_py3 import ClusterDesiredProperties
from ._models_py3 import ClusterList
from ._models_py3 import ClusterNode
from ._models_py3 import ClusterPatch
from ._models_py3 import ClusterReportedProperties
from ._models_py3 import ComponentsL15GkaSchemasVirtualnetworkspropertiesPropertiesSubnetsItemsPropertiesRoutetable
from ._models_py3 import (
    ComponentsVqks9HSchemasVirtualnetworkspropertiesPropertiesSubnetsItemsPropertiesIpconfigurationreferencesItems,
)
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import ExtendedLocation
from ._models_py3 import Extension
from ._models_py3 import ExtensionList
from ._models_py3 import GalleryDiskImage
from ._models_py3 import GalleryImageIdentifier
from ._models_py3 import GalleryImageStatus
from ._models_py3 import GalleryImageStatusDownloadStatus
from ._models_py3 import GalleryImageStatusProvisioningStatus
from ._models_py3 import GalleryImageVersion
from ._models_py3 import GalleryImageVersionStorageProfile
from ._models_py3 import GalleryOSDiskImage
from ._models_py3 import Galleryimages
from ._models_py3 import GalleryimagesListResult
from ._models_py3 import GalleryimagesPatch
from ._models_py3 import GuestAgent
from ._models_py3 import GuestAgentList
from ._models_py3 import GuestAgentProfile
from ._models_py3 import GuestCredential
from ._models_py3 import HardwareProfileUpdate
from ._models_py3 import HttpProxyConfiguration
from ._models_py3 import HybridIdentityMetadata
from ._models_py3 import HybridIdentityMetadataList
from ._models_py3 import IPPool
from ._models_py3 import IPPoolInfo
from ._models_py3 import Identity
from ._models_py3 import InterfaceDNSSettings
from ._models_py3 import IpConfiguration
from ._models_py3 import IpConfigurationProperties
from ._models_py3 import IpConfigurationPropertiesSubnet
from ._models_py3 import MachineExtension
from ._models_py3 import MachineExtensionInstanceView
from ._models_py3 import MachineExtensionInstanceViewStatus
from ._models_py3 import MachineExtensionPropertiesInstanceView
from ._models_py3 import MachineExtensionUpdate
from ._models_py3 import MachineExtensionsListResult
from ._models_py3 import MarketplaceGalleryImageStatus
from ._models_py3 import MarketplaceGalleryImageStatusDownloadStatus
from ._models_py3 import MarketplaceGalleryImageStatusProvisioningStatus
from ._models_py3 import Marketplacegalleryimages
from ._models_py3 import MarketplacegalleryimagesListResult
from ._models_py3 import MarketplacegalleryimagesPatch
from ._models_py3 import NetworkInterfaceStatus
from ._models_py3 import NetworkInterfaceStatusProvisioningStatus
from ._models_py3 import NetworkProfileUpdate
from ._models_py3 import NetworkProfileUpdateNetworkInterfacesItem
from ._models_py3 import Networkinterfaces
from ._models_py3 import NetworkinterfacesListResult
from ._models_py3 import NetworkinterfacesPatch
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import PerNodeExtensionState
from ._models_py3 import PerNodeState
from ._models_py3 import ProxyResource
from ._models_py3 import Resource
from ._models_py3 import ResourcePatch
from ._models_py3 import StorageContainerStatus
from ._models_py3 import StorageContainerStatusProvisioningStatus
from ._models_py3 import StorageProfileUpdate
from ._models_py3 import StorageProfileUpdateDataDisksItem
from ._models_py3 import Storagecontainers
from ._models_py3 import StoragecontainersExtendedLocation
from ._models_py3 import StoragecontainersListResult
from ._models_py3 import StoragecontainersPatch
from ._models_py3 import SystemData
from ._models_py3 import TrackedResource
from ._models_py3 import VirtualHardDiskStatus
from ._models_py3 import VirtualHardDiskStatusProvisioningStatus
from ._models_py3 import VirtualMachineStatus
from ._models_py3 import VirtualMachineStatusProvisioningStatus
from ._models_py3 import VirtualMachineUpdateProperties
from ._models_py3 import VirtualNetworkStatus
from ._models_py3 import VirtualNetworkStatusProvisioningStatus
from ._models_py3 import Virtualharddisks
from ._models_py3 import VirtualharddisksListResult
from ._models_py3 import VirtualharddisksPatch
from ._models_py3 import Virtualmachines
from ._models_py3 import VirtualmachinesListResult
from ._models_py3 import VirtualmachinesPatch
from ._models_py3 import VirtualmachinesPropertiesHardwareProfile
from ._models_py3 import VirtualmachinesPropertiesHardwareProfileDynamicMemoryConfig
from ._models_py3 import VirtualmachinesPropertiesNetworkProfile
from ._models_py3 import VirtualmachinesPropertiesNetworkProfileNetworkInterfacesItem
from ._models_py3 import VirtualmachinesPropertiesOsProfile
from ._models_py3 import VirtualmachinesPropertiesOsProfileLinuxConfiguration
from ._models_py3 import VirtualmachinesPropertiesOsProfileLinuxConfigurationSsh
from ._models_py3 import VirtualmachinesPropertiesOsProfileLinuxConfigurationSshPublicKeysItem
from ._models_py3 import VirtualmachinesPropertiesOsProfileWindowsConfiguration
from ._models_py3 import VirtualmachinesPropertiesOsProfileWindowsConfigurationSsh
from ._models_py3 import VirtualmachinesPropertiesOsProfileWindowsConfigurationSshPublicKeysItem
from ._models_py3 import VirtualmachinesPropertiesSecurityProfile
from ._models_py3 import VirtualmachinesPropertiesSecurityProfileUefiSettings
from ._models_py3 import VirtualmachinesPropertiesStorageProfile
from ._models_py3 import VirtualmachinesPropertiesStorageProfileDataDisksItem
from ._models_py3 import VirtualmachinesPropertiesStorageProfileImageReference
from ._models_py3 import VirtualmachinesPropertiesStorageProfileOsDisk
from ._models_py3 import Virtualnetworks
from ._models_py3 import VirtualnetworksListResult
from ._models_py3 import VirtualnetworksPatch
from ._models_py3 import VirtualnetworksPropertiesSubnetsItem
from ._models_py3 import VirtualnetworksPropertiesSubnetsPropertiesItemsItem

from ._azure_stack_hci_client_enums import ActionType
from ._azure_stack_hci_client_enums import ArcSettingAggregateState
from ._azure_stack_hci_client_enums import CloudInitDataSource
from ._azure_stack_hci_client_enums import CreatedByType
from ._azure_stack_hci_client_enums import DiagnosticLevel
from ._azure_stack_hci_client_enums import DiskFileFormat
from ._azure_stack_hci_client_enums import ExtendedLocationTypes
from ._azure_stack_hci_client_enums import ExtensionAggregateState
from ._azure_stack_hci_client_enums import HyperVGeneration
from ._azure_stack_hci_client_enums import IPPoolTypeEnum
from ._azure_stack_hci_client_enums import ImdsAttestation
from ._azure_stack_hci_client_enums import IpAllocationMethodEnum
from ._azure_stack_hci_client_enums import NetworkTypeEnum
from ._azure_stack_hci_client_enums import NodeArcState
from ._azure_stack_hci_client_enums import NodeExtensionState
from ._azure_stack_hci_client_enums import OperatingSystemTypes
from ._azure_stack_hci_client_enums import Origin
from ._azure_stack_hci_client_enums import OsTypeEnum
from ._azure_stack_hci_client_enums import PowerStateEnum
from ._azure_stack_hci_client_enums import PrivateIPAllocationMethodEnum
from ._azure_stack_hci_client_enums import ProvisioningAction
from ._azure_stack_hci_client_enums import ProvisioningState
from ._azure_stack_hci_client_enums import ProvisioningStateEnum
from ._azure_stack_hci_client_enums import ProvisioningStatusEnum
from ._azure_stack_hci_client_enums import Status
from ._azure_stack_hci_client_enums import StatusLevelTypes
from ._azure_stack_hci_client_enums import StatusTypes
from ._azure_stack_hci_client_enums import VmSizeEnum
from ._azure_stack_hci_client_enums import WindowsServerSubscription
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ArcSetting",
    "ArcSettingList",
    "Cluster",
    "ClusterDesiredProperties",
    "ClusterList",
    "ClusterNode",
    "ClusterPatch",
    "ClusterReportedProperties",
    "ComponentsL15GkaSchemasVirtualnetworkspropertiesPropertiesSubnetsItemsPropertiesRoutetable",
    "ComponentsVqks9HSchemasVirtualnetworkspropertiesPropertiesSubnetsItemsPropertiesIpconfigurationreferencesItems",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "ExtendedLocation",
    "Extension",
    "ExtensionList",
    "GalleryDiskImage",
    "GalleryImageIdentifier",
    "GalleryImageStatus",
    "GalleryImageStatusDownloadStatus",
    "GalleryImageStatusProvisioningStatus",
    "GalleryImageVersion",
    "GalleryImageVersionStorageProfile",
    "GalleryOSDiskImage",
    "Galleryimages",
    "GalleryimagesListResult",
    "GalleryimagesPatch",
    "GuestAgent",
    "GuestAgentList",
    "GuestAgentProfile",
    "GuestCredential",
    "HardwareProfileUpdate",
    "HttpProxyConfiguration",
    "HybridIdentityMetadata",
    "HybridIdentityMetadataList",
    "IPPool",
    "IPPoolInfo",
    "Identity",
    "InterfaceDNSSettings",
    "IpConfiguration",
    "IpConfigurationProperties",
    "IpConfigurationPropertiesSubnet",
    "MachineExtension",
    "MachineExtensionInstanceView",
    "MachineExtensionInstanceViewStatus",
    "MachineExtensionPropertiesInstanceView",
    "MachineExtensionUpdate",
    "MachineExtensionsListResult",
    "MarketplaceGalleryImageStatus",
    "MarketplaceGalleryImageStatusDownloadStatus",
    "MarketplaceGalleryImageStatusProvisioningStatus",
    "Marketplacegalleryimages",
    "MarketplacegalleryimagesListResult",
    "MarketplacegalleryimagesPatch",
    "NetworkInterfaceStatus",
    "NetworkInterfaceStatusProvisioningStatus",
    "NetworkProfileUpdate",
    "NetworkProfileUpdateNetworkInterfacesItem",
    "Networkinterfaces",
    "NetworkinterfacesListResult",
    "NetworkinterfacesPatch",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "PerNodeExtensionState",
    "PerNodeState",
    "ProxyResource",
    "Resource",
    "ResourcePatch",
    "StorageContainerStatus",
    "StorageContainerStatusProvisioningStatus",
    "StorageProfileUpdate",
    "StorageProfileUpdateDataDisksItem",
    "Storagecontainers",
    "StoragecontainersExtendedLocation",
    "StoragecontainersListResult",
    "StoragecontainersPatch",
    "SystemData",
    "TrackedResource",
    "VirtualHardDiskStatus",
    "VirtualHardDiskStatusProvisioningStatus",
    "VirtualMachineStatus",
    "VirtualMachineStatusProvisioningStatus",
    "VirtualMachineUpdateProperties",
    "VirtualNetworkStatus",
    "VirtualNetworkStatusProvisioningStatus",
    "Virtualharddisks",
    "VirtualharddisksListResult",
    "VirtualharddisksPatch",
    "Virtualmachines",
    "VirtualmachinesListResult",
    "VirtualmachinesPatch",
    "VirtualmachinesPropertiesHardwareProfile",
    "VirtualmachinesPropertiesHardwareProfileDynamicMemoryConfig",
    "VirtualmachinesPropertiesNetworkProfile",
    "VirtualmachinesPropertiesNetworkProfileNetworkInterfacesItem",
    "VirtualmachinesPropertiesOsProfile",
    "VirtualmachinesPropertiesOsProfileLinuxConfiguration",
    "VirtualmachinesPropertiesOsProfileLinuxConfigurationSsh",
    "VirtualmachinesPropertiesOsProfileLinuxConfigurationSshPublicKeysItem",
    "VirtualmachinesPropertiesOsProfileWindowsConfiguration",
    "VirtualmachinesPropertiesOsProfileWindowsConfigurationSsh",
    "VirtualmachinesPropertiesOsProfileWindowsConfigurationSshPublicKeysItem",
    "VirtualmachinesPropertiesSecurityProfile",
    "VirtualmachinesPropertiesSecurityProfileUefiSettings",
    "VirtualmachinesPropertiesStorageProfile",
    "VirtualmachinesPropertiesStorageProfileDataDisksItem",
    "VirtualmachinesPropertiesStorageProfileImageReference",
    "VirtualmachinesPropertiesStorageProfileOsDisk",
    "Virtualnetworks",
    "VirtualnetworksListResult",
    "VirtualnetworksPatch",
    "VirtualnetworksPropertiesSubnetsItem",
    "VirtualnetworksPropertiesSubnetsPropertiesItemsItem",
    "ActionType",
    "ArcSettingAggregateState",
    "CloudInitDataSource",
    "CreatedByType",
    "DiagnosticLevel",
    "DiskFileFormat",
    "ExtendedLocationTypes",
    "ExtensionAggregateState",
    "HyperVGeneration",
    "IPPoolTypeEnum",
    "ImdsAttestation",
    "IpAllocationMethodEnum",
    "NetworkTypeEnum",
    "NodeArcState",
    "NodeExtensionState",
    "OperatingSystemTypes",
    "Origin",
    "OsTypeEnum",
    "PowerStateEnum",
    "PrivateIPAllocationMethodEnum",
    "ProvisioningAction",
    "ProvisioningState",
    "ProvisioningStateEnum",
    "ProvisioningStatusEnum",
    "Status",
    "StatusLevelTypes",
    "StatusTypes",
    "VmSizeEnum",
    "WindowsServerSubscription",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()

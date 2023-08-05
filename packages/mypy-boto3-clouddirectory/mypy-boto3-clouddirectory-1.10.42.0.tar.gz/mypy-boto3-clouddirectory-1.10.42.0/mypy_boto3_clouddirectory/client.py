"Main interface for clouddirectory service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_clouddirectory.client as client_scope

# pylint: disable=import-self
import mypy_boto3_clouddirectory.paginator as paginator_scope
from mypy_boto3_clouddirectory.type_defs import (
    ApplySchemaResponseTypeDef,
    AttachObjectResponseTypeDef,
    AttachToIndexResponseTypeDef,
    AttachTypedLinkResponseTypeDef,
    AttributeKeyAndValueTypeDef,
    AttributeKeyTypeDef,
    AttributeNameAndValueTypeDef,
    BatchReadOperationTypeDef,
    BatchReadResponseTypeDef,
    BatchWriteOperationTypeDef,
    BatchWriteResponseTypeDef,
    CreateDirectoryResponseTypeDef,
    CreateIndexResponseTypeDef,
    CreateObjectResponseTypeDef,
    CreateSchemaResponseTypeDef,
    DeleteDirectoryResponseTypeDef,
    DeleteSchemaResponseTypeDef,
    DetachFromIndexResponseTypeDef,
    DetachObjectResponseTypeDef,
    DisableDirectoryResponseTypeDef,
    EnableDirectoryResponseTypeDef,
    FacetAttributeTypeDef,
    FacetAttributeUpdateTypeDef,
    GetAppliedSchemaVersionResponseTypeDef,
    GetDirectoryResponseTypeDef,
    GetFacetResponseTypeDef,
    GetLinkAttributesResponseTypeDef,
    GetObjectAttributesResponseTypeDef,
    GetObjectInformationResponseTypeDef,
    GetSchemaAsJsonResponseTypeDef,
    GetTypedLinkFacetInformationResponseTypeDef,
    LinkAttributeUpdateTypeDef,
    ListAppliedSchemaArnsResponseTypeDef,
    ListAttachedIndicesResponseTypeDef,
    ListDevelopmentSchemaArnsResponseTypeDef,
    ListDirectoriesResponseTypeDef,
    ListFacetAttributesResponseTypeDef,
    ListFacetNamesResponseTypeDef,
    ListIncomingTypedLinksResponseTypeDef,
    ListIndexResponseTypeDef,
    ListManagedSchemaArnsResponseTypeDef,
    ListObjectAttributesResponseTypeDef,
    ListObjectChildrenResponseTypeDef,
    ListObjectParentPathsResponseTypeDef,
    ListObjectParentsResponseTypeDef,
    ListObjectPoliciesResponseTypeDef,
    ListOutgoingTypedLinksResponseTypeDef,
    ListPolicyAttachmentsResponseTypeDef,
    ListPublishedSchemaArnsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTypedLinkFacetAttributesResponseTypeDef,
    ListTypedLinkFacetNamesResponseTypeDef,
    LookupPolicyResponseTypeDef,
    ObjectAttributeRangeTypeDef,
    ObjectAttributeUpdateTypeDef,
    ObjectReferenceTypeDef,
    PublishSchemaResponseTypeDef,
    PutSchemaFromJsonResponseTypeDef,
    SchemaFacetTypeDef,
    TagTypeDef,
    TypedLinkAttributeRangeTypeDef,
    TypedLinkFacetAttributeUpdateTypeDef,
    TypedLinkFacetTypeDef,
    TypedLinkSchemaAndFacetNameTypeDef,
    TypedLinkSpecifierTypeDef,
    UpdateObjectAttributesResponseTypeDef,
    UpdateSchemaResponseTypeDef,
    UpgradeAppliedSchemaResponseTypeDef,
    UpgradePublishedSchemaResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CloudDirectoryClient",)


class CloudDirectoryClient(BaseClient):
    """
    [CloudDirectory.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_facet_to_object(
        self,
        DirectoryArn: str,
        SchemaFacet: SchemaFacetTypeDef,
        ObjectReference: ObjectReferenceTypeDef,
        ObjectAttributeList: List[AttributeKeyAndValueTypeDef] = None,
    ) -> Dict[str, Any]:
        """
        [Client.add_facet_to_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.add_facet_to_object)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def apply_schema(
        self, PublishedSchemaArn: str, DirectoryArn: str
    ) -> ApplySchemaResponseTypeDef:
        """
        [Client.apply_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.apply_schema)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_object(
        self,
        DirectoryArn: str,
        ParentReference: ObjectReferenceTypeDef,
        ChildReference: ObjectReferenceTypeDef,
        LinkName: str,
    ) -> AttachObjectResponseTypeDef:
        """
        [Client.attach_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.attach_object)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_policy(
        self,
        DirectoryArn: str,
        PolicyReference: ObjectReferenceTypeDef,
        ObjectReference: ObjectReferenceTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.attach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.attach_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_to_index(
        self,
        DirectoryArn: str,
        IndexReference: ObjectReferenceTypeDef,
        TargetReference: ObjectReferenceTypeDef,
    ) -> AttachToIndexResponseTypeDef:
        """
        [Client.attach_to_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.attach_to_index)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_typed_link(
        self,
        DirectoryArn: str,
        SourceObjectReference: ObjectReferenceTypeDef,
        TargetObjectReference: ObjectReferenceTypeDef,
        TypedLinkFacet: TypedLinkSchemaAndFacetNameTypeDef,
        Attributes: List[AttributeNameAndValueTypeDef],
    ) -> AttachTypedLinkResponseTypeDef:
        """
        [Client.attach_typed_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.attach_typed_link)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_read(
        self,
        DirectoryArn: str,
        Operations: List[BatchReadOperationTypeDef],
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
    ) -> BatchReadResponseTypeDef:
        """
        [Client.batch_read documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.batch_read)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_write(
        self, DirectoryArn: str, Operations: List[BatchWriteOperationTypeDef]
    ) -> BatchWriteResponseTypeDef:
        """
        [Client.batch_write documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.batch_write)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_directory(self, Name: str, SchemaArn: str) -> CreateDirectoryResponseTypeDef:
        """
        [Client.create_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.create_directory)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_facet(
        self,
        SchemaArn: str,
        Name: str,
        Attributes: List[FacetAttributeTypeDef] = None,
        ObjectType: Literal["NODE", "LEAF_NODE", "POLICY", "INDEX"] = None,
        FacetStyle: Literal["STATIC", "DYNAMIC"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_facet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.create_facet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_index(
        self,
        DirectoryArn: str,
        OrderedIndexedAttributeList: List[AttributeKeyTypeDef],
        IsUnique: bool,
        ParentReference: ObjectReferenceTypeDef = None,
        LinkName: str = None,
    ) -> CreateIndexResponseTypeDef:
        """
        [Client.create_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.create_index)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_object(
        self,
        DirectoryArn: str,
        SchemaFacets: List[SchemaFacetTypeDef],
        ObjectAttributeList: List[AttributeKeyAndValueTypeDef] = None,
        ParentReference: ObjectReferenceTypeDef = None,
        LinkName: str = None,
    ) -> CreateObjectResponseTypeDef:
        """
        [Client.create_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.create_object)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_schema(self, Name: str) -> CreateSchemaResponseTypeDef:
        """
        [Client.create_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.create_schema)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_typed_link_facet(
        self, SchemaArn: str, Facet: TypedLinkFacetTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.create_typed_link_facet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.create_typed_link_facet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_directory(self, DirectoryArn: str) -> DeleteDirectoryResponseTypeDef:
        """
        [Client.delete_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.delete_directory)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_facet(self, SchemaArn: str, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_facet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.delete_facet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_object(
        self, DirectoryArn: str, ObjectReference: ObjectReferenceTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.delete_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.delete_object)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_schema(self, SchemaArn: str) -> DeleteSchemaResponseTypeDef:
        """
        [Client.delete_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.delete_schema)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_typed_link_facet(self, SchemaArn: str, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_typed_link_facet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.delete_typed_link_facet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_from_index(
        self,
        DirectoryArn: str,
        IndexReference: ObjectReferenceTypeDef,
        TargetReference: ObjectReferenceTypeDef,
    ) -> DetachFromIndexResponseTypeDef:
        """
        [Client.detach_from_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.detach_from_index)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_object(
        self, DirectoryArn: str, ParentReference: ObjectReferenceTypeDef, LinkName: str
    ) -> DetachObjectResponseTypeDef:
        """
        [Client.detach_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.detach_object)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_policy(
        self,
        DirectoryArn: str,
        PolicyReference: ObjectReferenceTypeDef,
        ObjectReference: ObjectReferenceTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.detach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.detach_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_typed_link(
        self, DirectoryArn: str, TypedLinkSpecifier: TypedLinkSpecifierTypeDef
    ) -> None:
        """
        [Client.detach_typed_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.detach_typed_link)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_directory(self, DirectoryArn: str) -> DisableDirectoryResponseTypeDef:
        """
        [Client.disable_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.disable_directory)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_directory(self, DirectoryArn: str) -> EnableDirectoryResponseTypeDef:
        """
        [Client.enable_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.enable_directory)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_applied_schema_version(self, SchemaArn: str) -> GetAppliedSchemaVersionResponseTypeDef:
        """
        [Client.get_applied_schema_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.get_applied_schema_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_directory(self, DirectoryArn: str) -> GetDirectoryResponseTypeDef:
        """
        [Client.get_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.get_directory)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_facet(self, SchemaArn: str, Name: str) -> GetFacetResponseTypeDef:
        """
        [Client.get_facet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.get_facet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_link_attributes(
        self,
        DirectoryArn: str,
        TypedLinkSpecifier: TypedLinkSpecifierTypeDef,
        AttributeNames: List[str],
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
    ) -> GetLinkAttributesResponseTypeDef:
        """
        [Client.get_link_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.get_link_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_object_attributes(
        self,
        DirectoryArn: str,
        ObjectReference: ObjectReferenceTypeDef,
        SchemaFacet: SchemaFacetTypeDef,
        AttributeNames: List[str],
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
    ) -> GetObjectAttributesResponseTypeDef:
        """
        [Client.get_object_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.get_object_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_object_information(
        self,
        DirectoryArn: str,
        ObjectReference: ObjectReferenceTypeDef,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
    ) -> GetObjectInformationResponseTypeDef:
        """
        [Client.get_object_information documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.get_object_information)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_schema_as_json(self, SchemaArn: str) -> GetSchemaAsJsonResponseTypeDef:
        """
        [Client.get_schema_as_json documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.get_schema_as_json)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_typed_link_facet_information(
        self, SchemaArn: str, Name: str
    ) -> GetTypedLinkFacetInformationResponseTypeDef:
        """
        [Client.get_typed_link_facet_information documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.get_typed_link_facet_information)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_applied_schema_arns(
        self,
        DirectoryArn: str,
        SchemaArn: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListAppliedSchemaArnsResponseTypeDef:
        """
        [Client.list_applied_schema_arns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.list_applied_schema_arns)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_attached_indices(
        self,
        DirectoryArn: str,
        TargetReference: ObjectReferenceTypeDef,
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
    ) -> ListAttachedIndicesResponseTypeDef:
        """
        [Client.list_attached_indices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.list_attached_indices)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_development_schema_arns(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListDevelopmentSchemaArnsResponseTypeDef:
        """
        [Client.list_development_schema_arns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.list_development_schema_arns)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_directories(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        state: Literal["ENABLED", "DISABLED", "DELETED"] = None,
    ) -> ListDirectoriesResponseTypeDef:
        """
        [Client.list_directories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.list_directories)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_facet_attributes(
        self, SchemaArn: str, Name: str, NextToken: str = None, MaxResults: int = None
    ) -> ListFacetAttributesResponseTypeDef:
        """
        [Client.list_facet_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.list_facet_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_facet_names(
        self, SchemaArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListFacetNamesResponseTypeDef:
        """
        [Client.list_facet_names documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.list_facet_names)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_incoming_typed_links(
        self,
        DirectoryArn: str,
        ObjectReference: ObjectReferenceTypeDef,
        FilterAttributeRanges: List[TypedLinkAttributeRangeTypeDef] = None,
        FilterTypedLink: TypedLinkSchemaAndFacetNameTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
    ) -> ListIncomingTypedLinksResponseTypeDef:
        """
        [Client.list_incoming_typed_links documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.list_incoming_typed_links)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_index(
        self,
        DirectoryArn: str,
        IndexReference: ObjectReferenceTypeDef,
        RangesOnIndexedValues: List[ObjectAttributeRangeTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
    ) -> ListIndexResponseTypeDef:
        """
        [Client.list_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.list_index)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_managed_schema_arns(
        self, SchemaArn: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListManagedSchemaArnsResponseTypeDef:
        """
        [Client.list_managed_schema_arns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.list_managed_schema_arns)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_object_attributes(
        self,
        DirectoryArn: str,
        ObjectReference: ObjectReferenceTypeDef,
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        FacetFilter: SchemaFacetTypeDef = None,
    ) -> ListObjectAttributesResponseTypeDef:
        """
        [Client.list_object_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.list_object_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_object_children(
        self,
        DirectoryArn: str,
        ObjectReference: ObjectReferenceTypeDef,
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
    ) -> ListObjectChildrenResponseTypeDef:
        """
        [Client.list_object_children documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.list_object_children)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_object_parent_paths(
        self,
        DirectoryArn: str,
        ObjectReference: ObjectReferenceTypeDef,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListObjectParentPathsResponseTypeDef:
        """
        [Client.list_object_parent_paths documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.list_object_parent_paths)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_object_parents(
        self,
        DirectoryArn: str,
        ObjectReference: ObjectReferenceTypeDef,
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        IncludeAllLinksToEachParent: bool = None,
    ) -> ListObjectParentsResponseTypeDef:
        """
        [Client.list_object_parents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.list_object_parents)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_object_policies(
        self,
        DirectoryArn: str,
        ObjectReference: ObjectReferenceTypeDef,
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
    ) -> ListObjectPoliciesResponseTypeDef:
        """
        [Client.list_object_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.list_object_policies)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_outgoing_typed_links(
        self,
        DirectoryArn: str,
        ObjectReference: ObjectReferenceTypeDef,
        FilterAttributeRanges: List[TypedLinkAttributeRangeTypeDef] = None,
        FilterTypedLink: TypedLinkSchemaAndFacetNameTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
    ) -> ListOutgoingTypedLinksResponseTypeDef:
        """
        [Client.list_outgoing_typed_links documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.list_outgoing_typed_links)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_policy_attachments(
        self,
        DirectoryArn: str,
        PolicyReference: ObjectReferenceTypeDef,
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
    ) -> ListPolicyAttachmentsResponseTypeDef:
        """
        [Client.list_policy_attachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.list_policy_attachments)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_published_schema_arns(
        self, SchemaArn: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListPublishedSchemaArnsResponseTypeDef:
        """
        [Client.list_published_schema_arns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.list_published_schema_arns)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_typed_link_facet_attributes(
        self, SchemaArn: str, Name: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTypedLinkFacetAttributesResponseTypeDef:
        """
        [Client.list_typed_link_facet_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.list_typed_link_facet_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_typed_link_facet_names(
        self, SchemaArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTypedLinkFacetNamesResponseTypeDef:
        """
        [Client.list_typed_link_facet_names documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.list_typed_link_facet_names)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def lookup_policy(
        self,
        DirectoryArn: str,
        ObjectReference: ObjectReferenceTypeDef,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> LookupPolicyResponseTypeDef:
        """
        [Client.lookup_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.lookup_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def publish_schema(
        self, DevelopmentSchemaArn: str, Version: str, MinorVersion: str = None, Name: str = None
    ) -> PublishSchemaResponseTypeDef:
        """
        [Client.publish_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.publish_schema)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_schema_from_json(
        self, SchemaArn: str, Document: str
    ) -> PutSchemaFromJsonResponseTypeDef:
        """
        [Client.put_schema_from_json documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.put_schema_from_json)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_facet_from_object(
        self,
        DirectoryArn: str,
        SchemaFacet: SchemaFacetTypeDef,
        ObjectReference: ObjectReferenceTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.remove_facet_from_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.remove_facet_from_object)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_facet(
        self,
        SchemaArn: str,
        Name: str,
        AttributeUpdates: List[FacetAttributeUpdateTypeDef] = None,
        ObjectType: Literal["NODE", "LEAF_NODE", "POLICY", "INDEX"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_facet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.update_facet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_link_attributes(
        self,
        DirectoryArn: str,
        TypedLinkSpecifier: TypedLinkSpecifierTypeDef,
        AttributeUpdates: List[LinkAttributeUpdateTypeDef],
    ) -> Dict[str, Any]:
        """
        [Client.update_link_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.update_link_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_object_attributes(
        self,
        DirectoryArn: str,
        ObjectReference: ObjectReferenceTypeDef,
        AttributeUpdates: List[ObjectAttributeUpdateTypeDef],
    ) -> UpdateObjectAttributesResponseTypeDef:
        """
        [Client.update_object_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.update_object_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_schema(self, SchemaArn: str, Name: str) -> UpdateSchemaResponseTypeDef:
        """
        [Client.update_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.update_schema)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_typed_link_facet(
        self,
        SchemaArn: str,
        Name: str,
        AttributeUpdates: List[TypedLinkFacetAttributeUpdateTypeDef],
        IdentityAttributeOrder: List[str],
    ) -> Dict[str, Any]:
        """
        [Client.update_typed_link_facet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.update_typed_link_facet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def upgrade_applied_schema(
        self, PublishedSchemaArn: str, DirectoryArn: str, DryRun: bool = None
    ) -> UpgradeAppliedSchemaResponseTypeDef:
        """
        [Client.upgrade_applied_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.upgrade_applied_schema)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def upgrade_published_schema(
        self,
        DevelopmentSchemaArn: str,
        PublishedSchemaArn: str,
        MinorVersion: str,
        DryRun: bool = None,
    ) -> UpgradePublishedSchemaResponseTypeDef:
        """
        [Client.upgrade_published_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Client.upgrade_published_schema)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_applied_schema_arns"]
    ) -> paginator_scope.ListAppliedSchemaArnsPaginator:
        """
        [Paginator.ListAppliedSchemaArns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListAppliedSchemaArns)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_attached_indices"]
    ) -> paginator_scope.ListAttachedIndicesPaginator:
        """
        [Paginator.ListAttachedIndices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListAttachedIndices)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_development_schema_arns"]
    ) -> paginator_scope.ListDevelopmentSchemaArnsPaginator:
        """
        [Paginator.ListDevelopmentSchemaArns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListDevelopmentSchemaArns)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_directories"]
    ) -> paginator_scope.ListDirectoriesPaginator:
        """
        [Paginator.ListDirectories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListDirectories)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_facet_attributes"]
    ) -> paginator_scope.ListFacetAttributesPaginator:
        """
        [Paginator.ListFacetAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListFacetAttributes)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_facet_names"]
    ) -> paginator_scope.ListFacetNamesPaginator:
        """
        [Paginator.ListFacetNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListFacetNames)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_incoming_typed_links"]
    ) -> paginator_scope.ListIncomingTypedLinksPaginator:
        """
        [Paginator.ListIncomingTypedLinks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListIncomingTypedLinks)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_index"]
    ) -> paginator_scope.ListIndexPaginator:
        """
        [Paginator.ListIndex documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListIndex)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_managed_schema_arns"]
    ) -> paginator_scope.ListManagedSchemaArnsPaginator:
        """
        [Paginator.ListManagedSchemaArns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListManagedSchemaArns)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_object_attributes"]
    ) -> paginator_scope.ListObjectAttributesPaginator:
        """
        [Paginator.ListObjectAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectAttributes)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_object_parent_paths"]
    ) -> paginator_scope.ListObjectParentPathsPaginator:
        """
        [Paginator.ListObjectParentPaths documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectParentPaths)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_object_policies"]
    ) -> paginator_scope.ListObjectPoliciesPaginator:
        """
        [Paginator.ListObjectPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectPolicies)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_outgoing_typed_links"]
    ) -> paginator_scope.ListOutgoingTypedLinksPaginator:
        """
        [Paginator.ListOutgoingTypedLinks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListOutgoingTypedLinks)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_policy_attachments"]
    ) -> paginator_scope.ListPolicyAttachmentsPaginator:
        """
        [Paginator.ListPolicyAttachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListPolicyAttachments)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_published_schema_arns"]
    ) -> paginator_scope.ListPublishedSchemaArnsPaginator:
        """
        [Paginator.ListPublishedSchemaArns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListPublishedSchemaArns)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> paginator_scope.ListTagsForResourcePaginator:
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTagsForResource)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_typed_link_facet_attributes"]
    ) -> paginator_scope.ListTypedLinkFacetAttributesPaginator:
        """
        [Paginator.ListTypedLinkFacetAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTypedLinkFacetAttributes)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_typed_link_facet_names"]
    ) -> paginator_scope.ListTypedLinkFacetNamesPaginator:
        """
        [Paginator.ListTypedLinkFacetNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTypedLinkFacetNames)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["lookup_policy"]
    ) -> paginator_scope.LookupPolicyPaginator:
        """
        [Paginator.LookupPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/clouddirectory.html#CloudDirectory.Paginator.LookupPolicy)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    BatchWriteException: Boto3ClientError
    CannotListParentOfRootException: Boto3ClientError
    ClientError: Boto3ClientError
    DirectoryAlreadyExistsException: Boto3ClientError
    DirectoryDeletedException: Boto3ClientError
    DirectoryNotDisabledException: Boto3ClientError
    DirectoryNotEnabledException: Boto3ClientError
    FacetAlreadyExistsException: Boto3ClientError
    FacetInUseException: Boto3ClientError
    FacetNotFoundException: Boto3ClientError
    FacetValidationException: Boto3ClientError
    IncompatibleSchemaException: Boto3ClientError
    IndexedAttributeMissingException: Boto3ClientError
    InternalServiceException: Boto3ClientError
    InvalidArnException: Boto3ClientError
    InvalidAttachmentException: Boto3ClientError
    InvalidFacetUpdateException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidRuleException: Boto3ClientError
    InvalidSchemaDocException: Boto3ClientError
    InvalidTaggingRequestException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    LinkNameAlreadyInUseException: Boto3ClientError
    NotIndexException: Boto3ClientError
    NotNodeException: Boto3ClientError
    NotPolicyException: Boto3ClientError
    ObjectAlreadyDetachedException: Boto3ClientError
    ObjectNotDetachedException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    RetryableConflictException: Boto3ClientError
    SchemaAlreadyExistsException: Boto3ClientError
    SchemaAlreadyPublishedException: Boto3ClientError
    StillContainsLinksException: Boto3ClientError
    UnsupportedIndexTypeException: Boto3ClientError
    ValidationException: Boto3ClientError

"Main interface for clouddirectory service Paginators"
from __future__ import annotations

import sys
from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_clouddirectory.type_defs import (
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
    ListObjectParentPathsResponseTypeDef,
    ListObjectPoliciesResponseTypeDef,
    ListOutgoingTypedLinksResponseTypeDef,
    ListPolicyAttachmentsResponseTypeDef,
    ListPublishedSchemaArnsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTypedLinkFacetAttributesResponseTypeDef,
    ListTypedLinkFacetNamesResponseTypeDef,
    LookupPolicyResponseTypeDef,
    ObjectAttributeRangeTypeDef,
    ObjectReferenceTypeDef,
    PaginatorConfigTypeDef,
    SchemaFacetTypeDef,
    TypedLinkAttributeRangeTypeDef,
    TypedLinkSchemaAndFacetNameTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAppliedSchemaArnsPaginator",
    "ListAttachedIndicesPaginator",
    "ListDevelopmentSchemaArnsPaginator",
    "ListDirectoriesPaginator",
    "ListFacetAttributesPaginator",
    "ListFacetNamesPaginator",
    "ListIncomingTypedLinksPaginator",
    "ListIndexPaginator",
    "ListManagedSchemaArnsPaginator",
    "ListObjectAttributesPaginator",
    "ListObjectParentPathsPaginator",
    "ListObjectPoliciesPaginator",
    "ListOutgoingTypedLinksPaginator",
    "ListPolicyAttachmentsPaginator",
    "ListPublishedSchemaArnsPaginator",
    "ListTagsForResourcePaginator",
    "ListTypedLinkFacetAttributesPaginator",
    "ListTypedLinkFacetNamesPaginator",
    "LookupPolicyPaginator",
)


class ListAppliedSchemaArnsPaginator(Boto3Paginator):
    """
    [Paginator.ListAppliedSchemaArns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListAppliedSchemaArns)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryArn: str,
        SchemaArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListAppliedSchemaArnsResponseTypeDef, None, None]:
        """
        [ListAppliedSchemaArns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListAppliedSchemaArns.paginate)
        """


class ListAttachedIndicesPaginator(Boto3Paginator):
    """
    [Paginator.ListAttachedIndices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListAttachedIndices)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryArn: str,
        TargetReference: ObjectReferenceTypeDef,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListAttachedIndicesResponseTypeDef, None, None]:
        """
        [ListAttachedIndices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListAttachedIndices.paginate)
        """


class ListDevelopmentSchemaArnsPaginator(Boto3Paginator):
    """
    [Paginator.ListDevelopmentSchemaArns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListDevelopmentSchemaArns)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDevelopmentSchemaArnsResponseTypeDef, None, None]:
        """
        [ListDevelopmentSchemaArns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListDevelopmentSchemaArns.paginate)
        """


class ListDirectoriesPaginator(Boto3Paginator):
    """
    [Paginator.ListDirectories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListDirectories)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        state: Literal["ENABLED", "DISABLED", "DELETED"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListDirectoriesResponseTypeDef, None, None]:
        """
        [ListDirectories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListDirectories.paginate)
        """


class ListFacetAttributesPaginator(Boto3Paginator):
    """
    [Paginator.ListFacetAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListFacetAttributes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, SchemaArn: str, Name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListFacetAttributesResponseTypeDef, None, None]:
        """
        [ListFacetAttributes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListFacetAttributes.paginate)
        """


class ListFacetNamesPaginator(Boto3Paginator):
    """
    [Paginator.ListFacetNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListFacetNames)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, SchemaArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListFacetNamesResponseTypeDef, None, None]:
        """
        [ListFacetNames.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListFacetNames.paginate)
        """


class ListIncomingTypedLinksPaginator(Boto3Paginator):
    """
    [Paginator.ListIncomingTypedLinks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListIncomingTypedLinks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: ObjectReferenceTypeDef,
        FilterAttributeRanges: List[TypedLinkAttributeRangeTypeDef] = None,
        FilterTypedLink: TypedLinkSchemaAndFacetNameTypeDef = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListIncomingTypedLinksResponseTypeDef, None, None]:
        """
        [ListIncomingTypedLinks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListIncomingTypedLinks.paginate)
        """


class ListIndexPaginator(Boto3Paginator):
    """
    [Paginator.ListIndex documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListIndex)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryArn: str,
        IndexReference: ObjectReferenceTypeDef,
        RangesOnIndexedValues: List[ObjectAttributeRangeTypeDef] = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListIndexResponseTypeDef, None, None]:
        """
        [ListIndex.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListIndex.paginate)
        """


class ListManagedSchemaArnsPaginator(Boto3Paginator):
    """
    [Paginator.ListManagedSchemaArns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListManagedSchemaArns)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, SchemaArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListManagedSchemaArnsResponseTypeDef, None, None]:
        """
        [ListManagedSchemaArns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListManagedSchemaArns.paginate)
        """


class ListObjectAttributesPaginator(Boto3Paginator):
    """
    [Paginator.ListObjectAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectAttributes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: ObjectReferenceTypeDef,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        FacetFilter: SchemaFacetTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListObjectAttributesResponseTypeDef, None, None]:
        """
        [ListObjectAttributes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectAttributes.paginate)
        """


class ListObjectParentPathsPaginator(Boto3Paginator):
    """
    [Paginator.ListObjectParentPaths documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectParentPaths)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: ObjectReferenceTypeDef,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListObjectParentPathsResponseTypeDef, None, None]:
        """
        [ListObjectParentPaths.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectParentPaths.paginate)
        """


class ListObjectPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListObjectPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectPolicies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: ObjectReferenceTypeDef,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListObjectPoliciesResponseTypeDef, None, None]:
        """
        [ListObjectPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectPolicies.paginate)
        """


class ListOutgoingTypedLinksPaginator(Boto3Paginator):
    """
    [Paginator.ListOutgoingTypedLinks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListOutgoingTypedLinks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: ObjectReferenceTypeDef,
        FilterAttributeRanges: List[TypedLinkAttributeRangeTypeDef] = None,
        FilterTypedLink: TypedLinkSchemaAndFacetNameTypeDef = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListOutgoingTypedLinksResponseTypeDef, None, None]:
        """
        [ListOutgoingTypedLinks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListOutgoingTypedLinks.paginate)
        """


class ListPolicyAttachmentsPaginator(Boto3Paginator):
    """
    [Paginator.ListPolicyAttachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListPolicyAttachments)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryArn: str,
        PolicyReference: ObjectReferenceTypeDef,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListPolicyAttachmentsResponseTypeDef, None, None]:
        """
        [ListPolicyAttachments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListPolicyAttachments.paginate)
        """


class ListPublishedSchemaArnsPaginator(Boto3Paginator):
    """
    [Paginator.ListPublishedSchemaArns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListPublishedSchemaArns)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, SchemaArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPublishedSchemaArnsResponseTypeDef, None, None]:
        """
        [ListPublishedSchemaArns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListPublishedSchemaArns.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTagsForResource)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ResourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTagsForResourceResponseTypeDef, None, None]:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTagsForResource.paginate)
        """


class ListTypedLinkFacetAttributesPaginator(Boto3Paginator):
    """
    [Paginator.ListTypedLinkFacetAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTypedLinkFacetAttributes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, SchemaArn: str, Name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTypedLinkFacetAttributesResponseTypeDef, None, None]:
        """
        [ListTypedLinkFacetAttributes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTypedLinkFacetAttributes.paginate)
        """


class ListTypedLinkFacetNamesPaginator(Boto3Paginator):
    """
    [Paginator.ListTypedLinkFacetNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTypedLinkFacetNames)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, SchemaArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTypedLinkFacetNamesResponseTypeDef, None, None]:
        """
        [ListTypedLinkFacetNames.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTypedLinkFacetNames.paginate)
        """


class LookupPolicyPaginator(Boto3Paginator):
    """
    [Paginator.LookupPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.LookupPolicy)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: ObjectReferenceTypeDef,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[LookupPolicyResponseTypeDef, None, None]:
        """
        [LookupPolicy.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/clouddirectory.html#CloudDirectory.Paginator.LookupPolicy.paginate)
        """

"Main interface for cloudfront service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


CloudFrontOriginAccessIdentityConfigTypeDef = TypedDict(
    "CloudFrontOriginAccessIdentityConfigTypeDef", {"CallerReference": str, "Comment": str}
)

_RequiredCloudFrontOriginAccessIdentityTypeDef = TypedDict(
    "_RequiredCloudFrontOriginAccessIdentityTypeDef", {"Id": str, "S3CanonicalUserId": str}
)
_OptionalCloudFrontOriginAccessIdentityTypeDef = TypedDict(
    "_OptionalCloudFrontOriginAccessIdentityTypeDef",
    {"CloudFrontOriginAccessIdentityConfig": CloudFrontOriginAccessIdentityConfigTypeDef},
    total=False,
)


class CloudFrontOriginAccessIdentityTypeDef(
    _RequiredCloudFrontOriginAccessIdentityTypeDef, _OptionalCloudFrontOriginAccessIdentityTypeDef
):
    pass


CreateCloudFrontOriginAccessIdentityResultTypeDef = TypedDict(
    "CreateCloudFrontOriginAccessIdentityResultTypeDef",
    {
        "CloudFrontOriginAccessIdentity": CloudFrontOriginAccessIdentityTypeDef,
        "Location": str,
        "ETag": str,
    },
    total=False,
)

_RequiredKeyPairIdsTypeDef = TypedDict("_RequiredKeyPairIdsTypeDef", {"Quantity": int})
_OptionalKeyPairIdsTypeDef = TypedDict(
    "_OptionalKeyPairIdsTypeDef", {"Items": List[str]}, total=False
)


class KeyPairIdsTypeDef(_RequiredKeyPairIdsTypeDef, _OptionalKeyPairIdsTypeDef):
    pass


SignerTypeDef = TypedDict(
    "SignerTypeDef", {"AwsAccountNumber": str, "KeyPairIds": KeyPairIdsTypeDef}, total=False
)

_RequiredActiveTrustedSignersTypeDef = TypedDict(
    "_RequiredActiveTrustedSignersTypeDef", {"Enabled": bool, "Quantity": int}
)
_OptionalActiveTrustedSignersTypeDef = TypedDict(
    "_OptionalActiveTrustedSignersTypeDef", {"Items": List[SignerTypeDef]}, total=False
)


class ActiveTrustedSignersTypeDef(
    _RequiredActiveTrustedSignersTypeDef, _OptionalActiveTrustedSignersTypeDef
):
    pass


AliasICPRecordalTypeDef = TypedDict(
    "AliasICPRecordalTypeDef",
    {"CNAME": str, "ICPRecordalStatus": Literal["APPROVED", "SUSPENDED", "PENDING"]},
    total=False,
)

_RequiredAliasesTypeDef = TypedDict("_RequiredAliasesTypeDef", {"Quantity": int})
_OptionalAliasesTypeDef = TypedDict("_OptionalAliasesTypeDef", {"Items": List[str]}, total=False)


class AliasesTypeDef(_RequiredAliasesTypeDef, _OptionalAliasesTypeDef):
    pass


CachedMethodsTypeDef = TypedDict(
    "CachedMethodsTypeDef",
    {
        "Quantity": int,
        "Items": List[Literal["GET", "HEAD", "POST", "PUT", "PATCH", "OPTIONS", "DELETE"]],
    },
)

_RequiredAllowedMethodsTypeDef = TypedDict(
    "_RequiredAllowedMethodsTypeDef",
    {
        "Quantity": int,
        "Items": List[Literal["GET", "HEAD", "POST", "PUT", "PATCH", "OPTIONS", "DELETE"]],
    },
)
_OptionalAllowedMethodsTypeDef = TypedDict(
    "_OptionalAllowedMethodsTypeDef", {"CachedMethods": CachedMethodsTypeDef}, total=False
)


class AllowedMethodsTypeDef(_RequiredAllowedMethodsTypeDef, _OptionalAllowedMethodsTypeDef):
    pass


_RequiredCookieNamesTypeDef = TypedDict("_RequiredCookieNamesTypeDef", {"Quantity": int})
_OptionalCookieNamesTypeDef = TypedDict(
    "_OptionalCookieNamesTypeDef", {"Items": List[str]}, total=False
)


class CookieNamesTypeDef(_RequiredCookieNamesTypeDef, _OptionalCookieNamesTypeDef):
    pass


_RequiredCookiePreferenceTypeDef = TypedDict(
    "_RequiredCookiePreferenceTypeDef", {"Forward": Literal["none", "whitelist", "all"]}
)
_OptionalCookiePreferenceTypeDef = TypedDict(
    "_OptionalCookiePreferenceTypeDef", {"WhitelistedNames": CookieNamesTypeDef}, total=False
)


class CookiePreferenceTypeDef(_RequiredCookiePreferenceTypeDef, _OptionalCookiePreferenceTypeDef):
    pass


_RequiredHeadersTypeDef = TypedDict("_RequiredHeadersTypeDef", {"Quantity": int})
_OptionalHeadersTypeDef = TypedDict("_OptionalHeadersTypeDef", {"Items": List[str]}, total=False)


class HeadersTypeDef(_RequiredHeadersTypeDef, _OptionalHeadersTypeDef):
    pass


_RequiredQueryStringCacheKeysTypeDef = TypedDict(
    "_RequiredQueryStringCacheKeysTypeDef", {"Quantity": int}
)
_OptionalQueryStringCacheKeysTypeDef = TypedDict(
    "_OptionalQueryStringCacheKeysTypeDef", {"Items": List[str]}, total=False
)


class QueryStringCacheKeysTypeDef(
    _RequiredQueryStringCacheKeysTypeDef, _OptionalQueryStringCacheKeysTypeDef
):
    pass


_RequiredForwardedValuesTypeDef = TypedDict(
    "_RequiredForwardedValuesTypeDef", {"QueryString": bool, "Cookies": CookiePreferenceTypeDef}
)
_OptionalForwardedValuesTypeDef = TypedDict(
    "_OptionalForwardedValuesTypeDef",
    {"Headers": HeadersTypeDef, "QueryStringCacheKeys": QueryStringCacheKeysTypeDef},
    total=False,
)


class ForwardedValuesTypeDef(_RequiredForwardedValuesTypeDef, _OptionalForwardedValuesTypeDef):
    pass


_RequiredLambdaFunctionAssociationTypeDef = TypedDict(
    "_RequiredLambdaFunctionAssociationTypeDef",
    {
        "LambdaFunctionARN": str,
        "EventType": Literal[
            "viewer-request", "viewer-response", "origin-request", "origin-response"
        ],
    },
)
_OptionalLambdaFunctionAssociationTypeDef = TypedDict(
    "_OptionalLambdaFunctionAssociationTypeDef", {"IncludeBody": bool}, total=False
)


class LambdaFunctionAssociationTypeDef(
    _RequiredLambdaFunctionAssociationTypeDef, _OptionalLambdaFunctionAssociationTypeDef
):
    pass


_RequiredLambdaFunctionAssociationsTypeDef = TypedDict(
    "_RequiredLambdaFunctionAssociationsTypeDef", {"Quantity": int}
)
_OptionalLambdaFunctionAssociationsTypeDef = TypedDict(
    "_OptionalLambdaFunctionAssociationsTypeDef",
    {"Items": List[LambdaFunctionAssociationTypeDef]},
    total=False,
)


class LambdaFunctionAssociationsTypeDef(
    _RequiredLambdaFunctionAssociationsTypeDef, _OptionalLambdaFunctionAssociationsTypeDef
):
    pass


_RequiredTrustedSignersTypeDef = TypedDict(
    "_RequiredTrustedSignersTypeDef", {"Enabled": bool, "Quantity": int}
)
_OptionalTrustedSignersTypeDef = TypedDict(
    "_OptionalTrustedSignersTypeDef", {"Items": List[str]}, total=False
)


class TrustedSignersTypeDef(_RequiredTrustedSignersTypeDef, _OptionalTrustedSignersTypeDef):
    pass


_RequiredCacheBehaviorTypeDef = TypedDict(
    "_RequiredCacheBehaviorTypeDef",
    {
        "PathPattern": str,
        "TargetOriginId": str,
        "ForwardedValues": ForwardedValuesTypeDef,
        "TrustedSigners": TrustedSignersTypeDef,
        "ViewerProtocolPolicy": Literal["allow-all", "https-only", "redirect-to-https"],
        "MinTTL": int,
    },
)
_OptionalCacheBehaviorTypeDef = TypedDict(
    "_OptionalCacheBehaviorTypeDef",
    {
        "AllowedMethods": AllowedMethodsTypeDef,
        "SmoothStreaming": bool,
        "DefaultTTL": int,
        "MaxTTL": int,
        "Compress": bool,
        "LambdaFunctionAssociations": LambdaFunctionAssociationsTypeDef,
        "FieldLevelEncryptionId": str,
    },
    total=False,
)


class CacheBehaviorTypeDef(_RequiredCacheBehaviorTypeDef, _OptionalCacheBehaviorTypeDef):
    pass


_RequiredCacheBehaviorsTypeDef = TypedDict("_RequiredCacheBehaviorsTypeDef", {"Quantity": int})
_OptionalCacheBehaviorsTypeDef = TypedDict(
    "_OptionalCacheBehaviorsTypeDef", {"Items": List[CacheBehaviorTypeDef]}, total=False
)


class CacheBehaviorsTypeDef(_RequiredCacheBehaviorsTypeDef, _OptionalCacheBehaviorsTypeDef):
    pass


_RequiredCustomErrorResponseTypeDef = TypedDict(
    "_RequiredCustomErrorResponseTypeDef", {"ErrorCode": int}
)
_OptionalCustomErrorResponseTypeDef = TypedDict(
    "_OptionalCustomErrorResponseTypeDef",
    {"ResponsePagePath": str, "ResponseCode": str, "ErrorCachingMinTTL": int},
    total=False,
)


class CustomErrorResponseTypeDef(
    _RequiredCustomErrorResponseTypeDef, _OptionalCustomErrorResponseTypeDef
):
    pass


_RequiredCustomErrorResponsesTypeDef = TypedDict(
    "_RequiredCustomErrorResponsesTypeDef", {"Quantity": int}
)
_OptionalCustomErrorResponsesTypeDef = TypedDict(
    "_OptionalCustomErrorResponsesTypeDef", {"Items": List[CustomErrorResponseTypeDef]}, total=False
)


class CustomErrorResponsesTypeDef(
    _RequiredCustomErrorResponsesTypeDef, _OptionalCustomErrorResponsesTypeDef
):
    pass


_RequiredDefaultCacheBehaviorTypeDef = TypedDict(
    "_RequiredDefaultCacheBehaviorTypeDef",
    {
        "TargetOriginId": str,
        "ForwardedValues": ForwardedValuesTypeDef,
        "TrustedSigners": TrustedSignersTypeDef,
        "ViewerProtocolPolicy": Literal["allow-all", "https-only", "redirect-to-https"],
        "MinTTL": int,
    },
)
_OptionalDefaultCacheBehaviorTypeDef = TypedDict(
    "_OptionalDefaultCacheBehaviorTypeDef",
    {
        "AllowedMethods": AllowedMethodsTypeDef,
        "SmoothStreaming": bool,
        "DefaultTTL": int,
        "MaxTTL": int,
        "Compress": bool,
        "LambdaFunctionAssociations": LambdaFunctionAssociationsTypeDef,
        "FieldLevelEncryptionId": str,
    },
    total=False,
)


class DefaultCacheBehaviorTypeDef(
    _RequiredDefaultCacheBehaviorTypeDef, _OptionalDefaultCacheBehaviorTypeDef
):
    pass


LoggingConfigTypeDef = TypedDict(
    "LoggingConfigTypeDef", {"Enabled": bool, "IncludeCookies": bool, "Bucket": str, "Prefix": str}
)

StatusCodesTypeDef = TypedDict("StatusCodesTypeDef", {"Quantity": int, "Items": List[int]})

OriginGroupFailoverCriteriaTypeDef = TypedDict(
    "OriginGroupFailoverCriteriaTypeDef", {"StatusCodes": StatusCodesTypeDef}
)

OriginGroupMemberTypeDef = TypedDict("OriginGroupMemberTypeDef", {"OriginId": str})

OriginGroupMembersTypeDef = TypedDict(
    "OriginGroupMembersTypeDef", {"Quantity": int, "Items": List[OriginGroupMemberTypeDef]}
)

OriginGroupTypeDef = TypedDict(
    "OriginGroupTypeDef",
    {
        "Id": str,
        "FailoverCriteria": OriginGroupFailoverCriteriaTypeDef,
        "Members": OriginGroupMembersTypeDef,
    },
)

_RequiredOriginGroupsTypeDef = TypedDict("_RequiredOriginGroupsTypeDef", {"Quantity": int})
_OptionalOriginGroupsTypeDef = TypedDict(
    "_OptionalOriginGroupsTypeDef", {"Items": List[OriginGroupTypeDef]}, total=False
)


class OriginGroupsTypeDef(_RequiredOriginGroupsTypeDef, _OptionalOriginGroupsTypeDef):
    pass


OriginCustomHeaderTypeDef = TypedDict(
    "OriginCustomHeaderTypeDef", {"HeaderName": str, "HeaderValue": str}
)

_RequiredCustomHeadersTypeDef = TypedDict("_RequiredCustomHeadersTypeDef", {"Quantity": int})
_OptionalCustomHeadersTypeDef = TypedDict(
    "_OptionalCustomHeadersTypeDef", {"Items": List[OriginCustomHeaderTypeDef]}, total=False
)


class CustomHeadersTypeDef(_RequiredCustomHeadersTypeDef, _OptionalCustomHeadersTypeDef):
    pass


OriginSslProtocolsTypeDef = TypedDict(
    "OriginSslProtocolsTypeDef",
    {"Quantity": int, "Items": List[Literal["SSLv3", "TLSv1", "TLSv1.1", "TLSv1.2"]]},
)

_RequiredCustomOriginConfigTypeDef = TypedDict(
    "_RequiredCustomOriginConfigTypeDef",
    {
        "HTTPPort": int,
        "HTTPSPort": int,
        "OriginProtocolPolicy": Literal["http-only", "match-viewer", "https-only"],
    },
)
_OptionalCustomOriginConfigTypeDef = TypedDict(
    "_OptionalCustomOriginConfigTypeDef",
    {
        "OriginSslProtocols": OriginSslProtocolsTypeDef,
        "OriginReadTimeout": int,
        "OriginKeepaliveTimeout": int,
    },
    total=False,
)


class CustomOriginConfigTypeDef(
    _RequiredCustomOriginConfigTypeDef, _OptionalCustomOriginConfigTypeDef
):
    pass


S3OriginConfigTypeDef = TypedDict("S3OriginConfigTypeDef", {"OriginAccessIdentity": str})

_RequiredOriginTypeDef = TypedDict("_RequiredOriginTypeDef", {"Id": str, "DomainName": str})
_OptionalOriginTypeDef = TypedDict(
    "_OptionalOriginTypeDef",
    {
        "OriginPath": str,
        "CustomHeaders": CustomHeadersTypeDef,
        "S3OriginConfig": S3OriginConfigTypeDef,
        "CustomOriginConfig": CustomOriginConfigTypeDef,
    },
    total=False,
)


class OriginTypeDef(_RequiredOriginTypeDef, _OptionalOriginTypeDef):
    pass


OriginsTypeDef = TypedDict("OriginsTypeDef", {"Quantity": int, "Items": List[OriginTypeDef]})

_RequiredGeoRestrictionTypeDef = TypedDict(
    "_RequiredGeoRestrictionTypeDef",
    {"RestrictionType": Literal["blacklist", "whitelist", "none"], "Quantity": int},
)
_OptionalGeoRestrictionTypeDef = TypedDict(
    "_OptionalGeoRestrictionTypeDef", {"Items": List[str]}, total=False
)


class GeoRestrictionTypeDef(_RequiredGeoRestrictionTypeDef, _OptionalGeoRestrictionTypeDef):
    pass


RestrictionsTypeDef = TypedDict("RestrictionsTypeDef", {"GeoRestriction": GeoRestrictionTypeDef})

ViewerCertificateTypeDef = TypedDict(
    "ViewerCertificateTypeDef",
    {
        "CloudFrontDefaultCertificate": bool,
        "IAMCertificateId": str,
        "ACMCertificateArn": str,
        "SSLSupportMethod": Literal["sni-only", "vip"],
        "MinimumProtocolVersion": Literal[
            "SSLv3", "TLSv1", "TLSv1_2016", "TLSv1.1_2016", "TLSv1.2_2018"
        ],
        "Certificate": str,
        "CertificateSource": Literal["cloudfront", "iam", "acm"],
    },
    total=False,
)

_RequiredDistributionConfigTypeDef = TypedDict(
    "_RequiredDistributionConfigTypeDef",
    {
        "CallerReference": str,
        "Origins": OriginsTypeDef,
        "DefaultCacheBehavior": DefaultCacheBehaviorTypeDef,
        "Comment": str,
        "Enabled": bool,
    },
)
_OptionalDistributionConfigTypeDef = TypedDict(
    "_OptionalDistributionConfigTypeDef",
    {
        "Aliases": AliasesTypeDef,
        "DefaultRootObject": str,
        "OriginGroups": OriginGroupsTypeDef,
        "CacheBehaviors": CacheBehaviorsTypeDef,
        "CustomErrorResponses": CustomErrorResponsesTypeDef,
        "Logging": LoggingConfigTypeDef,
        "PriceClass": Literal["PriceClass_100", "PriceClass_200", "PriceClass_All"],
        "ViewerCertificate": ViewerCertificateTypeDef,
        "Restrictions": RestrictionsTypeDef,
        "WebACLId": str,
        "HttpVersion": Literal["http1.1", "http2"],
        "IsIPV6Enabled": bool,
    },
    total=False,
)


class DistributionConfigTypeDef(
    _RequiredDistributionConfigTypeDef, _OptionalDistributionConfigTypeDef
):
    pass


_RequiredDistributionTypeDef = TypedDict(
    "_RequiredDistributionTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "LastModifiedTime": datetime,
        "InProgressInvalidationBatches": int,
        "DomainName": str,
        "ActiveTrustedSigners": ActiveTrustedSignersTypeDef,
        "DistributionConfig": DistributionConfigTypeDef,
    },
)
_OptionalDistributionTypeDef = TypedDict(
    "_OptionalDistributionTypeDef",
    {"AliasICPRecordals": List[AliasICPRecordalTypeDef]},
    total=False,
)


class DistributionTypeDef(_RequiredDistributionTypeDef, _OptionalDistributionTypeDef):
    pass


CreateDistributionResultTypeDef = TypedDict(
    "CreateDistributionResultTypeDef",
    {"Distribution": DistributionTypeDef, "Location": str, "ETag": str},
    total=False,
)

CreateDistributionWithTagsResultTypeDef = TypedDict(
    "CreateDistributionWithTagsResultTypeDef",
    {"Distribution": DistributionTypeDef, "Location": str, "ETag": str},
    total=False,
)

_RequiredContentTypeProfileTypeDef = TypedDict(
    "_RequiredContentTypeProfileTypeDef", {"Format": Literal["URLEncoded"], "ContentType": str}
)
_OptionalContentTypeProfileTypeDef = TypedDict(
    "_OptionalContentTypeProfileTypeDef", {"ProfileId": str}, total=False
)


class ContentTypeProfileTypeDef(
    _RequiredContentTypeProfileTypeDef, _OptionalContentTypeProfileTypeDef
):
    pass


_RequiredContentTypeProfilesTypeDef = TypedDict(
    "_RequiredContentTypeProfilesTypeDef", {"Quantity": int}
)
_OptionalContentTypeProfilesTypeDef = TypedDict(
    "_OptionalContentTypeProfilesTypeDef", {"Items": List[ContentTypeProfileTypeDef]}, total=False
)


class ContentTypeProfilesTypeDef(
    _RequiredContentTypeProfilesTypeDef, _OptionalContentTypeProfilesTypeDef
):
    pass


_RequiredContentTypeProfileConfigTypeDef = TypedDict(
    "_RequiredContentTypeProfileConfigTypeDef", {"ForwardWhenContentTypeIsUnknown": bool}
)
_OptionalContentTypeProfileConfigTypeDef = TypedDict(
    "_OptionalContentTypeProfileConfigTypeDef",
    {"ContentTypeProfiles": ContentTypeProfilesTypeDef},
    total=False,
)


class ContentTypeProfileConfigTypeDef(
    _RequiredContentTypeProfileConfigTypeDef, _OptionalContentTypeProfileConfigTypeDef
):
    pass


QueryArgProfileTypeDef = TypedDict("QueryArgProfileTypeDef", {"QueryArg": str, "ProfileId": str})

_RequiredQueryArgProfilesTypeDef = TypedDict("_RequiredQueryArgProfilesTypeDef", {"Quantity": int})
_OptionalQueryArgProfilesTypeDef = TypedDict(
    "_OptionalQueryArgProfilesTypeDef", {"Items": List[QueryArgProfileTypeDef]}, total=False
)


class QueryArgProfilesTypeDef(_RequiredQueryArgProfilesTypeDef, _OptionalQueryArgProfilesTypeDef):
    pass


_RequiredQueryArgProfileConfigTypeDef = TypedDict(
    "_RequiredQueryArgProfileConfigTypeDef", {"ForwardWhenQueryArgProfileIsUnknown": bool}
)
_OptionalQueryArgProfileConfigTypeDef = TypedDict(
    "_OptionalQueryArgProfileConfigTypeDef",
    {"QueryArgProfiles": QueryArgProfilesTypeDef},
    total=False,
)


class QueryArgProfileConfigTypeDef(
    _RequiredQueryArgProfileConfigTypeDef, _OptionalQueryArgProfileConfigTypeDef
):
    pass


_RequiredFieldLevelEncryptionConfigTypeDef = TypedDict(
    "_RequiredFieldLevelEncryptionConfigTypeDef", {"CallerReference": str}
)
_OptionalFieldLevelEncryptionConfigTypeDef = TypedDict(
    "_OptionalFieldLevelEncryptionConfigTypeDef",
    {
        "Comment": str,
        "QueryArgProfileConfig": QueryArgProfileConfigTypeDef,
        "ContentTypeProfileConfig": ContentTypeProfileConfigTypeDef,
    },
    total=False,
)


class FieldLevelEncryptionConfigTypeDef(
    _RequiredFieldLevelEncryptionConfigTypeDef, _OptionalFieldLevelEncryptionConfigTypeDef
):
    pass


FieldLevelEncryptionTypeDef = TypedDict(
    "FieldLevelEncryptionTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "FieldLevelEncryptionConfig": FieldLevelEncryptionConfigTypeDef,
    },
)

CreateFieldLevelEncryptionConfigResultTypeDef = TypedDict(
    "CreateFieldLevelEncryptionConfigResultTypeDef",
    {"FieldLevelEncryption": FieldLevelEncryptionTypeDef, "Location": str, "ETag": str},
    total=False,
)

_RequiredFieldPatternsTypeDef = TypedDict("_RequiredFieldPatternsTypeDef", {"Quantity": int})
_OptionalFieldPatternsTypeDef = TypedDict(
    "_OptionalFieldPatternsTypeDef", {"Items": List[str]}, total=False
)


class FieldPatternsTypeDef(_RequiredFieldPatternsTypeDef, _OptionalFieldPatternsTypeDef):
    pass


EncryptionEntityTypeDef = TypedDict(
    "EncryptionEntityTypeDef",
    {"PublicKeyId": str, "ProviderId": str, "FieldPatterns": FieldPatternsTypeDef},
)

_RequiredEncryptionEntitiesTypeDef = TypedDict(
    "_RequiredEncryptionEntitiesTypeDef", {"Quantity": int}
)
_OptionalEncryptionEntitiesTypeDef = TypedDict(
    "_OptionalEncryptionEntitiesTypeDef", {"Items": List[EncryptionEntityTypeDef]}, total=False
)


class EncryptionEntitiesTypeDef(
    _RequiredEncryptionEntitiesTypeDef, _OptionalEncryptionEntitiesTypeDef
):
    pass


_RequiredFieldLevelEncryptionProfileConfigTypeDef = TypedDict(
    "_RequiredFieldLevelEncryptionProfileConfigTypeDef",
    {"Name": str, "CallerReference": str, "EncryptionEntities": EncryptionEntitiesTypeDef},
)
_OptionalFieldLevelEncryptionProfileConfigTypeDef = TypedDict(
    "_OptionalFieldLevelEncryptionProfileConfigTypeDef", {"Comment": str}, total=False
)


class FieldLevelEncryptionProfileConfigTypeDef(
    _RequiredFieldLevelEncryptionProfileConfigTypeDef,
    _OptionalFieldLevelEncryptionProfileConfigTypeDef,
):
    pass


FieldLevelEncryptionProfileTypeDef = TypedDict(
    "FieldLevelEncryptionProfileTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "FieldLevelEncryptionProfileConfig": FieldLevelEncryptionProfileConfigTypeDef,
    },
)

CreateFieldLevelEncryptionProfileResultTypeDef = TypedDict(
    "CreateFieldLevelEncryptionProfileResultTypeDef",
    {
        "FieldLevelEncryptionProfile": FieldLevelEncryptionProfileTypeDef,
        "Location": str,
        "ETag": str,
    },
    total=False,
)

_RequiredPathsTypeDef = TypedDict("_RequiredPathsTypeDef", {"Quantity": int})
_OptionalPathsTypeDef = TypedDict("_OptionalPathsTypeDef", {"Items": List[str]}, total=False)


class PathsTypeDef(_RequiredPathsTypeDef, _OptionalPathsTypeDef):
    pass


InvalidationBatchTypeDef = TypedDict(
    "InvalidationBatchTypeDef", {"Paths": PathsTypeDef, "CallerReference": str}
)

InvalidationTypeDef = TypedDict(
    "InvalidationTypeDef",
    {
        "Id": str,
        "Status": str,
        "CreateTime": datetime,
        "InvalidationBatch": InvalidationBatchTypeDef,
    },
)

CreateInvalidationResultTypeDef = TypedDict(
    "CreateInvalidationResultTypeDef",
    {"Location": str, "Invalidation": InvalidationTypeDef},
    total=False,
)

_RequiredPublicKeyConfigTypeDef = TypedDict(
    "_RequiredPublicKeyConfigTypeDef", {"CallerReference": str, "Name": str, "EncodedKey": str}
)
_OptionalPublicKeyConfigTypeDef = TypedDict(
    "_OptionalPublicKeyConfigTypeDef", {"Comment": str}, total=False
)


class PublicKeyConfigTypeDef(_RequiredPublicKeyConfigTypeDef, _OptionalPublicKeyConfigTypeDef):
    pass


PublicKeyTypeDef = TypedDict(
    "PublicKeyTypeDef",
    {"Id": str, "CreatedTime": datetime, "PublicKeyConfig": PublicKeyConfigTypeDef},
)

CreatePublicKeyResultTypeDef = TypedDict(
    "CreatePublicKeyResultTypeDef",
    {"PublicKey": PublicKeyTypeDef, "Location": str, "ETag": str},
    total=False,
)

S3OriginTypeDef = TypedDict("S3OriginTypeDef", {"DomainName": str, "OriginAccessIdentity": str})

StreamingLoggingConfigTypeDef = TypedDict(
    "StreamingLoggingConfigTypeDef", {"Enabled": bool, "Bucket": str, "Prefix": str}
)

_RequiredStreamingDistributionConfigTypeDef = TypedDict(
    "_RequiredStreamingDistributionConfigTypeDef",
    {
        "CallerReference": str,
        "S3Origin": S3OriginTypeDef,
        "Comment": str,
        "TrustedSigners": TrustedSignersTypeDef,
        "Enabled": bool,
    },
)
_OptionalStreamingDistributionConfigTypeDef = TypedDict(
    "_OptionalStreamingDistributionConfigTypeDef",
    {
        "Aliases": AliasesTypeDef,
        "Logging": StreamingLoggingConfigTypeDef,
        "PriceClass": Literal["PriceClass_100", "PriceClass_200", "PriceClass_All"],
    },
    total=False,
)


class StreamingDistributionConfigTypeDef(
    _RequiredStreamingDistributionConfigTypeDef, _OptionalStreamingDistributionConfigTypeDef
):
    pass


_RequiredStreamingDistributionTypeDef = TypedDict(
    "_RequiredStreamingDistributionTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "DomainName": str,
        "ActiveTrustedSigners": ActiveTrustedSignersTypeDef,
        "StreamingDistributionConfig": StreamingDistributionConfigTypeDef,
    },
)
_OptionalStreamingDistributionTypeDef = TypedDict(
    "_OptionalStreamingDistributionTypeDef", {"LastModifiedTime": datetime}, total=False
)


class StreamingDistributionTypeDef(
    _RequiredStreamingDistributionTypeDef, _OptionalStreamingDistributionTypeDef
):
    pass


CreateStreamingDistributionResultTypeDef = TypedDict(
    "CreateStreamingDistributionResultTypeDef",
    {"StreamingDistribution": StreamingDistributionTypeDef, "Location": str, "ETag": str},
    total=False,
)

CreateStreamingDistributionWithTagsResultTypeDef = TypedDict(
    "CreateStreamingDistributionWithTagsResultTypeDef",
    {"StreamingDistribution": StreamingDistributionTypeDef, "Location": str, "ETag": str},
    total=False,
)

_RequiredTagTypeDef = TypedDict("_RequiredTagTypeDef", {"Key": str})
_OptionalTagTypeDef = TypedDict("_OptionalTagTypeDef", {"Value": str}, total=False)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


TagsTypeDef = TypedDict("TagsTypeDef", {"Items": List[TagTypeDef]}, total=False)

DistributionConfigWithTagsTypeDef = TypedDict(
    "DistributionConfigWithTagsTypeDef",
    {"DistributionConfig": DistributionConfigTypeDef, "Tags": TagsTypeDef},
)

GetCloudFrontOriginAccessIdentityConfigResultTypeDef = TypedDict(
    "GetCloudFrontOriginAccessIdentityConfigResultTypeDef",
    {
        "CloudFrontOriginAccessIdentityConfig": CloudFrontOriginAccessIdentityConfigTypeDef,
        "ETag": str,
    },
    total=False,
)

GetCloudFrontOriginAccessIdentityResultTypeDef = TypedDict(
    "GetCloudFrontOriginAccessIdentityResultTypeDef",
    {"CloudFrontOriginAccessIdentity": CloudFrontOriginAccessIdentityTypeDef, "ETag": str},
    total=False,
)

GetDistributionConfigResultTypeDef = TypedDict(
    "GetDistributionConfigResultTypeDef",
    {"DistributionConfig": DistributionConfigTypeDef, "ETag": str},
    total=False,
)

GetDistributionResultTypeDef = TypedDict(
    "GetDistributionResultTypeDef", {"Distribution": DistributionTypeDef, "ETag": str}, total=False
)

GetFieldLevelEncryptionConfigResultTypeDef = TypedDict(
    "GetFieldLevelEncryptionConfigResultTypeDef",
    {"FieldLevelEncryptionConfig": FieldLevelEncryptionConfigTypeDef, "ETag": str},
    total=False,
)

GetFieldLevelEncryptionProfileConfigResultTypeDef = TypedDict(
    "GetFieldLevelEncryptionProfileConfigResultTypeDef",
    {"FieldLevelEncryptionProfileConfig": FieldLevelEncryptionProfileConfigTypeDef, "ETag": str},
    total=False,
)

GetFieldLevelEncryptionProfileResultTypeDef = TypedDict(
    "GetFieldLevelEncryptionProfileResultTypeDef",
    {"FieldLevelEncryptionProfile": FieldLevelEncryptionProfileTypeDef, "ETag": str},
    total=False,
)

GetFieldLevelEncryptionResultTypeDef = TypedDict(
    "GetFieldLevelEncryptionResultTypeDef",
    {"FieldLevelEncryption": FieldLevelEncryptionTypeDef, "ETag": str},
    total=False,
)

GetInvalidationResultTypeDef = TypedDict(
    "GetInvalidationResultTypeDef", {"Invalidation": InvalidationTypeDef}, total=False
)

GetPublicKeyConfigResultTypeDef = TypedDict(
    "GetPublicKeyConfigResultTypeDef",
    {"PublicKeyConfig": PublicKeyConfigTypeDef, "ETag": str},
    total=False,
)

GetPublicKeyResultTypeDef = TypedDict(
    "GetPublicKeyResultTypeDef", {"PublicKey": PublicKeyTypeDef, "ETag": str}, total=False
)

GetStreamingDistributionConfigResultTypeDef = TypedDict(
    "GetStreamingDistributionConfigResultTypeDef",
    {"StreamingDistributionConfig": StreamingDistributionConfigTypeDef, "ETag": str},
    total=False,
)

GetStreamingDistributionResultTypeDef = TypedDict(
    "GetStreamingDistributionResultTypeDef",
    {"StreamingDistribution": StreamingDistributionTypeDef, "ETag": str},
    total=False,
)

CloudFrontOriginAccessIdentitySummaryTypeDef = TypedDict(
    "CloudFrontOriginAccessIdentitySummaryTypeDef",
    {"Id": str, "S3CanonicalUserId": str, "Comment": str},
)

_RequiredCloudFrontOriginAccessIdentityListTypeDef = TypedDict(
    "_RequiredCloudFrontOriginAccessIdentityListTypeDef",
    {"Marker": str, "MaxItems": int, "IsTruncated": bool, "Quantity": int},
)
_OptionalCloudFrontOriginAccessIdentityListTypeDef = TypedDict(
    "_OptionalCloudFrontOriginAccessIdentityListTypeDef",
    {"NextMarker": str, "Items": List[CloudFrontOriginAccessIdentitySummaryTypeDef]},
    total=False,
)


class CloudFrontOriginAccessIdentityListTypeDef(
    _RequiredCloudFrontOriginAccessIdentityListTypeDef,
    _OptionalCloudFrontOriginAccessIdentityListTypeDef,
):
    pass


ListCloudFrontOriginAccessIdentitiesResultTypeDef = TypedDict(
    "ListCloudFrontOriginAccessIdentitiesResultTypeDef",
    {"CloudFrontOriginAccessIdentityList": CloudFrontOriginAccessIdentityListTypeDef},
    total=False,
)

_RequiredDistributionSummaryTypeDef = TypedDict(
    "_RequiredDistributionSummaryTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "LastModifiedTime": datetime,
        "DomainName": str,
        "Aliases": AliasesTypeDef,
        "Origins": OriginsTypeDef,
        "DefaultCacheBehavior": DefaultCacheBehaviorTypeDef,
        "CacheBehaviors": CacheBehaviorsTypeDef,
        "CustomErrorResponses": CustomErrorResponsesTypeDef,
        "Comment": str,
        "PriceClass": Literal["PriceClass_100", "PriceClass_200", "PriceClass_All"],
        "Enabled": bool,
        "ViewerCertificate": ViewerCertificateTypeDef,
        "Restrictions": RestrictionsTypeDef,
        "WebACLId": str,
        "HttpVersion": Literal["http1.1", "http2"],
        "IsIPV6Enabled": bool,
    },
)
_OptionalDistributionSummaryTypeDef = TypedDict(
    "_OptionalDistributionSummaryTypeDef",
    {"OriginGroups": OriginGroupsTypeDef, "AliasICPRecordals": List[AliasICPRecordalTypeDef]},
    total=False,
)


class DistributionSummaryTypeDef(
    _RequiredDistributionSummaryTypeDef, _OptionalDistributionSummaryTypeDef
):
    pass


_RequiredDistributionListTypeDef = TypedDict(
    "_RequiredDistributionListTypeDef",
    {"Marker": str, "MaxItems": int, "IsTruncated": bool, "Quantity": int},
)
_OptionalDistributionListTypeDef = TypedDict(
    "_OptionalDistributionListTypeDef",
    {"NextMarker": str, "Items": List[DistributionSummaryTypeDef]},
    total=False,
)


class DistributionListTypeDef(_RequiredDistributionListTypeDef, _OptionalDistributionListTypeDef):
    pass


ListDistributionsByWebACLIdResultTypeDef = TypedDict(
    "ListDistributionsByWebACLIdResultTypeDef",
    {"DistributionList": DistributionListTypeDef},
    total=False,
)

ListDistributionsResultTypeDef = TypedDict(
    "ListDistributionsResultTypeDef", {"DistributionList": DistributionListTypeDef}, total=False
)

_RequiredFieldLevelEncryptionSummaryTypeDef = TypedDict(
    "_RequiredFieldLevelEncryptionSummaryTypeDef", {"Id": str, "LastModifiedTime": datetime}
)
_OptionalFieldLevelEncryptionSummaryTypeDef = TypedDict(
    "_OptionalFieldLevelEncryptionSummaryTypeDef",
    {
        "Comment": str,
        "QueryArgProfileConfig": QueryArgProfileConfigTypeDef,
        "ContentTypeProfileConfig": ContentTypeProfileConfigTypeDef,
    },
    total=False,
)


class FieldLevelEncryptionSummaryTypeDef(
    _RequiredFieldLevelEncryptionSummaryTypeDef, _OptionalFieldLevelEncryptionSummaryTypeDef
):
    pass


_RequiredFieldLevelEncryptionListTypeDef = TypedDict(
    "_RequiredFieldLevelEncryptionListTypeDef", {"MaxItems": int, "Quantity": int}
)
_OptionalFieldLevelEncryptionListTypeDef = TypedDict(
    "_OptionalFieldLevelEncryptionListTypeDef",
    {"NextMarker": str, "Items": List[FieldLevelEncryptionSummaryTypeDef]},
    total=False,
)


class FieldLevelEncryptionListTypeDef(
    _RequiredFieldLevelEncryptionListTypeDef, _OptionalFieldLevelEncryptionListTypeDef
):
    pass


ListFieldLevelEncryptionConfigsResultTypeDef = TypedDict(
    "ListFieldLevelEncryptionConfigsResultTypeDef",
    {"FieldLevelEncryptionList": FieldLevelEncryptionListTypeDef},
    total=False,
)

_RequiredFieldLevelEncryptionProfileSummaryTypeDef = TypedDict(
    "_RequiredFieldLevelEncryptionProfileSummaryTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "Name": str,
        "EncryptionEntities": EncryptionEntitiesTypeDef,
    },
)
_OptionalFieldLevelEncryptionProfileSummaryTypeDef = TypedDict(
    "_OptionalFieldLevelEncryptionProfileSummaryTypeDef", {"Comment": str}, total=False
)


class FieldLevelEncryptionProfileSummaryTypeDef(
    _RequiredFieldLevelEncryptionProfileSummaryTypeDef,
    _OptionalFieldLevelEncryptionProfileSummaryTypeDef,
):
    pass


_RequiredFieldLevelEncryptionProfileListTypeDef = TypedDict(
    "_RequiredFieldLevelEncryptionProfileListTypeDef", {"MaxItems": int, "Quantity": int}
)
_OptionalFieldLevelEncryptionProfileListTypeDef = TypedDict(
    "_OptionalFieldLevelEncryptionProfileListTypeDef",
    {"NextMarker": str, "Items": List[FieldLevelEncryptionProfileSummaryTypeDef]},
    total=False,
)


class FieldLevelEncryptionProfileListTypeDef(
    _RequiredFieldLevelEncryptionProfileListTypeDef, _OptionalFieldLevelEncryptionProfileListTypeDef
):
    pass


ListFieldLevelEncryptionProfilesResultTypeDef = TypedDict(
    "ListFieldLevelEncryptionProfilesResultTypeDef",
    {"FieldLevelEncryptionProfileList": FieldLevelEncryptionProfileListTypeDef},
    total=False,
)

InvalidationSummaryTypeDef = TypedDict(
    "InvalidationSummaryTypeDef", {"Id": str, "CreateTime": datetime, "Status": str}
)

_RequiredInvalidationListTypeDef = TypedDict(
    "_RequiredInvalidationListTypeDef",
    {"Marker": str, "MaxItems": int, "IsTruncated": bool, "Quantity": int},
)
_OptionalInvalidationListTypeDef = TypedDict(
    "_OptionalInvalidationListTypeDef",
    {"NextMarker": str, "Items": List[InvalidationSummaryTypeDef]},
    total=False,
)


class InvalidationListTypeDef(_RequiredInvalidationListTypeDef, _OptionalInvalidationListTypeDef):
    pass


ListInvalidationsResultTypeDef = TypedDict(
    "ListInvalidationsResultTypeDef", {"InvalidationList": InvalidationListTypeDef}, total=False
)

_RequiredPublicKeySummaryTypeDef = TypedDict(
    "_RequiredPublicKeySummaryTypeDef",
    {"Id": str, "Name": str, "CreatedTime": datetime, "EncodedKey": str},
)
_OptionalPublicKeySummaryTypeDef = TypedDict(
    "_OptionalPublicKeySummaryTypeDef", {"Comment": str}, total=False
)


class PublicKeySummaryTypeDef(_RequiredPublicKeySummaryTypeDef, _OptionalPublicKeySummaryTypeDef):
    pass


_RequiredPublicKeyListTypeDef = TypedDict(
    "_RequiredPublicKeyListTypeDef", {"MaxItems": int, "Quantity": int}
)
_OptionalPublicKeyListTypeDef = TypedDict(
    "_OptionalPublicKeyListTypeDef",
    {"NextMarker": str, "Items": List[PublicKeySummaryTypeDef]},
    total=False,
)


class PublicKeyListTypeDef(_RequiredPublicKeyListTypeDef, _OptionalPublicKeyListTypeDef):
    pass


ListPublicKeysResultTypeDef = TypedDict(
    "ListPublicKeysResultTypeDef", {"PublicKeyList": PublicKeyListTypeDef}, total=False
)

StreamingDistributionSummaryTypeDef = TypedDict(
    "StreamingDistributionSummaryTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "LastModifiedTime": datetime,
        "DomainName": str,
        "S3Origin": S3OriginTypeDef,
        "Aliases": AliasesTypeDef,
        "TrustedSigners": TrustedSignersTypeDef,
        "Comment": str,
        "PriceClass": Literal["PriceClass_100", "PriceClass_200", "PriceClass_All"],
        "Enabled": bool,
    },
)

_RequiredStreamingDistributionListTypeDef = TypedDict(
    "_RequiredStreamingDistributionListTypeDef",
    {"Marker": str, "MaxItems": int, "IsTruncated": bool, "Quantity": int},
)
_OptionalStreamingDistributionListTypeDef = TypedDict(
    "_OptionalStreamingDistributionListTypeDef",
    {"NextMarker": str, "Items": List[StreamingDistributionSummaryTypeDef]},
    total=False,
)


class StreamingDistributionListTypeDef(
    _RequiredStreamingDistributionListTypeDef, _OptionalStreamingDistributionListTypeDef
):
    pass


ListStreamingDistributionsResultTypeDef = TypedDict(
    "ListStreamingDistributionsResultTypeDef",
    {"StreamingDistributionList": StreamingDistributionListTypeDef},
    total=False,
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef", {"Tags": TagsTypeDef}
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

StreamingDistributionConfigWithTagsTypeDef = TypedDict(
    "StreamingDistributionConfigWithTagsTypeDef",
    {"StreamingDistributionConfig": StreamingDistributionConfigTypeDef, "Tags": TagsTypeDef},
)

TagKeysTypeDef = TypedDict("TagKeysTypeDef", {"Items": List[str]}, total=False)

UpdateCloudFrontOriginAccessIdentityResultTypeDef = TypedDict(
    "UpdateCloudFrontOriginAccessIdentityResultTypeDef",
    {"CloudFrontOriginAccessIdentity": CloudFrontOriginAccessIdentityTypeDef, "ETag": str},
    total=False,
)

UpdateDistributionResultTypeDef = TypedDict(
    "UpdateDistributionResultTypeDef",
    {"Distribution": DistributionTypeDef, "ETag": str},
    total=False,
)

UpdateFieldLevelEncryptionConfigResultTypeDef = TypedDict(
    "UpdateFieldLevelEncryptionConfigResultTypeDef",
    {"FieldLevelEncryption": FieldLevelEncryptionTypeDef, "ETag": str},
    total=False,
)

UpdateFieldLevelEncryptionProfileResultTypeDef = TypedDict(
    "UpdateFieldLevelEncryptionProfileResultTypeDef",
    {"FieldLevelEncryptionProfile": FieldLevelEncryptionProfileTypeDef, "ETag": str},
    total=False,
)

UpdatePublicKeyResultTypeDef = TypedDict(
    "UpdatePublicKeyResultTypeDef", {"PublicKey": PublicKeyTypeDef, "ETag": str}, total=False
)

UpdateStreamingDistributionResultTypeDef = TypedDict(
    "UpdateStreamingDistributionResultTypeDef",
    {"StreamingDistribution": StreamingDistributionTypeDef, "ETag": str},
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

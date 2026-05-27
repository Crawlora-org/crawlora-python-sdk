from __future__ import annotations

import sys
from typing import Any, Callable, Literal, Mapping

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

AirbnbRoomResponse = Any
AirbnbRoomParams = TypedDict('AirbnbRoomParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

AirbnbRoomCalendarResponse = Any
AirbnbRoomCalendarParams = TypedDict('AirbnbRoomCalendarParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

AirbnbRoomReviewsResponse = Any
AirbnbRoomReviewsParams = TypedDict('AirbnbRoomReviewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

AirbnbSearchResponse = Any
AirbnbSearchParams = TypedDict('AirbnbSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'location': Required[str],
    'check_in': NotRequired[str],
    'check_out': NotRequired[str],
    'adults': NotRequired[int],
    'page': NotRequired[int],
    'currency': NotRequired[str],
    'ne_lat': NotRequired[float],
    'ne_lng': NotRequired[float],
    'sw_lat': NotRequired[float],
    'sw_lng': NotRequired[float],
    'zoom': NotRequired[int],
}, total=False)

AmazonProductResponse = Any
AmazonProductParams = TypedDict('AmazonProductParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'asin': Required[str],
    'language': NotRequired[Literal['en_US']],
    'currency': NotRequired[Literal['USD']],
}, total=False)

AmazonSearchResponse = Any
AmazonSearchParams = TypedDict('AmazonSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'k': Required[str],
    's': NotRequired[str],
    'page': NotRequired[int],
}, total=False)

AmazonSuggestResponse = Any
AmazonSuggestParams = TypedDict('AmazonSuggestParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
}, total=False)

ApplePodcastsChartsResponse = Any
ApplePodcastsChartsParams = TypedDict('ApplePodcastsChartsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'collection': NotRequired[str],
    'category': NotRequired[int],
    'country': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

ApplePodcastsEpisodesSearchResponse = Any
ApplePodcastsEpisodesSearchParams = TypedDict('ApplePodcastsEpisodesSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'term': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'limit': NotRequired[int],
    'page': NotRequired[int],
}, total=False)

ApplePodcastsSearchResponse = Any
ApplePodcastsSearchParams = TypedDict('ApplePodcastsSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'term': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'limit': NotRequired[int],
    'page': NotRequired[int],
}, total=False)

ApplePodcastsShowResponse = Any
ApplePodcastsShowParams = TypedDict('ApplePodcastsShowParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

ApplePodcastsShowEpisodesResponse = Any
ApplePodcastsShowEpisodesParams = TypedDict('ApplePodcastsShowEpisodesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

AppStoreAppResponse = Any
AppStoreAppParams = TypedDict('AppStoreAppParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'app_id': NotRequired[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'ratings': NotRequired[bool],
}, total=False)

AppStoreDeveloperResponse = Any
AppStoreDeveloperParams = TypedDict('AppStoreDeveloperParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'dev_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppStoreListResponse = Any
AppStoreListParams = TypedDict('AppStoreListParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'collection': NotRequired[str],
    'category': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'num': NotRequired[int],
    'full_detail': NotRequired[bool],
}, total=False)

AppStorePrivacyResponse = Any
AppStorePrivacyParams = TypedDict('AppStorePrivacyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppStoreRatingsResponse = Any
AppStoreRatingsParams = TypedDict('AppStoreRatingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'app_id': NotRequired[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppStoreReviewsResponse = Any
AppStoreReviewsParams = TypedDict('AppStoreReviewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'app_id': NotRequired[str],
    'country': NotRequired[str],
    'page': NotRequired[int],
    'sort': NotRequired[Literal['mostRecent', 'mostHelpful']],
    'lang': NotRequired[str],
}, total=False)

AppStoreSearchResponse = Any
AppStoreSearchParams = TypedDict('AppStoreSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'term': Required[str],
    'num': NotRequired[int],
    'page': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'ids_only': NotRequired[bool],
}, total=False)

AppStoreSimilarResponse = Any
AppStoreSimilarParams = TypedDict('AppStoreSimilarParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'app_id': NotRequired[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppStoreSuggestResponse = Any
AppStoreSuggestParams = TypedDict('AppStoreSuggestParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'term': Required[str],
    'country': NotRequired[str],
}, total=False)

AppStoreVersionHistoryResponse = Any
AppStoreVersionHistoryParams = TypedDict('AppStoreVersionHistoryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

BillingMeResponse = Any
BillingMeParams = TypedDict('BillingMeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

BillingMeCheckoutBody = dict[str, Any]
BillingMeCheckoutResponse = Any
BillingMeCheckoutParams = TypedDict('BillingMeCheckoutParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[BillingMeCheckoutBody],
}, total=False)

BillingMeEventsResponse = Any
BillingMeEventsParams = TypedDict('BillingMeEventsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'limit': NotRequired[int],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'endpoint': NotRequired[str],
    'request_id': NotRequired[str],
    'event_status': NotRequired[Literal['reserved', 'charged', 'non_billable', 'failed']],
    'billable': NotRequired[bool],
}, total=False)

BillingMePeriodsResponse = Any
BillingMePeriodsParams = TypedDict('BillingMePeriodsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'limit': NotRequired[int],
}, total=False)

BillingMePeriodResponse = Any
BillingMePeriodParams = TypedDict('BillingMePeriodParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'period_key': Required[str],
}, total=False)

BillingMePeriodStatementResponse = Any
BillingMePeriodStatementParams = TypedDict('BillingMePeriodStatementParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'period_key': Required[str],
    'include_events': NotRequired[bool],
    'event_limit': NotRequired[int],
}, total=False)

BillingMePeriodStatementDownloadResponse = Any
BillingMePeriodStatementDownloadParams = TypedDict('BillingMePeriodStatementDownloadParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'period_key': Required[str],
}, total=False)

BillingMePortalBody = dict[str, Any]
BillingMePortalResponse = Any
BillingMePortalParams = TypedDict('BillingMePortalParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[BillingMePortalBody],
}, total=False)

BingImagesResponse = Any
BingImagesParams = TypedDict('BingImagesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

BingNewsResponse = Any
BingNewsParams = TypedDict('BingNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

BingSearchResponse = Any
BingSearchParams = TypedDict('BingSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

BingSuggestResponse = Any
BingSuggestParams = TypedDict('BingSuggestParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

BingVideosResponse = Any
BingVideosParams = TypedDict('BingVideosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

BraveImagesResponse = Any
BraveImagesParams = TypedDict('BraveImagesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
}, total=False)

BraveNewsResponse = Any
BraveNewsParams = TypedDict('BraveNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
    'time_range': NotRequired[Literal['any', 'day', 'week', 'month', 'year', 'custom']],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
}, total=False)

BraveSearchResponse = Any
BraveSearchParams = TypedDict('BraveSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
    'time_range': NotRequired[Literal['any', 'day', 'week', 'month', 'year', 'custom']],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
}, total=False)

BraveSuggestResponse = Any
BraveSuggestParams = TypedDict('BraveSuggestParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'count': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
}, total=False)

BraveVideosResponse = Any
BraveVideosParams = TypedDict('BraveVideosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
    'time_range': NotRequired[Literal['any', 'day', 'week', 'month', 'year', 'custom']],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
}, total=False)

CoinGeckoCategoriesResponse = Any
CoinGeckoCategoriesParams = TypedDict('CoinGeckoCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoCategoryCoinsResponse = Any
CoinGeckoCategoryCoinsParams = TypedDict('CoinGeckoCategoryCoinsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoChainsResponse = Any
CoinGeckoChainsParams = TypedDict('CoinGeckoChainsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoChainResponse = Any
CoinGeckoChainParams = TypedDict('CoinGeckoChainParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoCoinResponse = Any
CoinGeckoCoinParams = TypedDict('CoinGeckoCoinParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoCoinAnalysisResponse = Any
CoinGeckoCoinAnalysisParams = TypedDict('CoinGeckoCoinAnalysisParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
    'range': NotRequired[Literal['24h', 'max']],
    'include_annotations': NotRequired[bool],
}, total=False)

CoinGeckoExchangeResponse = Any
CoinGeckoExchangeParams = TypedDict('CoinGeckoExchangeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoExchangesResponse = Any
CoinGeckoExchangesParams = TypedDict('CoinGeckoExchangesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'kind': NotRequired[Literal['spot', 'dex', 'derivatives', 'perp_dex']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoGainersLosersResponse = Any
CoinGeckoGainersLosersParams = TypedDict('CoinGeckoGainersLosersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoGlobalResponse = Any
CoinGeckoGlobalParams = TypedDict('CoinGeckoGlobalParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

CoinGeckoGlobalChartsResponse = Any
CoinGeckoGlobalChartsParams = TypedDict('CoinGeckoGlobalChartsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'kind': NotRequired[Literal['total_market_cap', 'bitcoin_dominance', 'altcoin_market_cap', 'defi_market_cap']],
    'range': NotRequired[Literal['24h', '7d', '14d', '30d', '90d', '1y', 'max']],
    'limit': NotRequired[int],
}, total=False)

CoinGeckoLearnArticlesResponse = Any
CoinGeckoLearnArticlesParams = TypedDict('CoinGeckoLearnArticlesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category': NotRequired[Literal['all', 'latest', 'airdrop-guides', 'coins-and-tokens', 'guides', 'wallets-and-bridges', 'api', 'reviews']],
    'limit': NotRequired[int],
}, total=False)

CoinGeckoMarketsResponse = Any
CoinGeckoMarketsParams = TypedDict('CoinGeckoMarketsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoNewCoinsResponse = Any
CoinGeckoNewCoinsParams = TypedDict('CoinGeckoNewCoinsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoNewsResponse = Any
CoinGeckoNewsParams = TypedDict('CoinGeckoNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'limit': NotRequired[int],
}, total=False)

CoinGeckoNftCategoryResponse = Any
CoinGeckoNftCategoryParams = TypedDict('CoinGeckoNftCategoryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoNftsResponse = Any
CoinGeckoNftsParams = TypedDict('CoinGeckoNftsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoSearchResponse = Any
CoinGeckoSearchParams = TypedDict('CoinGeckoSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'limit': NotRequired[int],
}, total=False)

CoinGeckoTokenUnlocksResponse = Any
CoinGeckoTokenUnlocksParams = TypedDict('CoinGeckoTokenUnlocksParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'limit': NotRequired[int],
}, total=False)

CoinGeckoTreasuriesResponse = Any
CoinGeckoTreasuriesParams = TypedDict('CoinGeckoTreasuriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'asset': NotRequired[Literal['all', 'bitcoin', 'ethereum', 'solana', 'bnb', 'xrp', 'tron']],
    'holder_type': NotRequired[Literal['all', 'companies', 'governments']],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoTrendingResponse = Any
CoinGeckoTrendingParams = TypedDict('CoinGeckoTrendingParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

DatasetsListResponse = Any
DatasetsListParams = TypedDict('DatasetsListParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

DatasetsGoogleMapBusinessesFacetsResponse = Any
DatasetsGoogleMapBusinessesFacetsParams = TypedDict('DatasetsGoogleMapBusinessesFacetsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'facet': Required[str],
    'q': NotRequired[str],
    'category': NotRequired[str],
    'country': NotRequired[str],
    'state': NotRequired[str],
    'county': NotRequired[str],
    'city': NotRequired[str],
    'town': NotRequired[str],
    'min_rating': NotRequired[float],
    'min_review_count': NotRequired[int],
    'has_website': NotRequired[bool],
    'has_phone': NotRequired[bool],
    'lat': NotRequired[float],
    'lon': NotRequired[float],
    'radius_m': NotRequired[int],
    'sort': NotRequired[str],
}, total=False)

DatasetsGoogleMapBusinessesItemResponse = Any
DatasetsGoogleMapBusinessesItemParams = TypedDict('DatasetsGoogleMapBusinessesItemParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'place_id': Required[str],
}, total=False)

DatasetsGoogleMapBusinessesNearbyResponse = Any
DatasetsGoogleMapBusinessesNearbyParams = TypedDict('DatasetsGoogleMapBusinessesNearbyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'lat': Required[float],
    'lon': Required[float],
    'radius_m': Required[int],
    'category': NotRequired[str],
    'min_rating': NotRequired[float],
    'min_review_count': NotRequired[int],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

DatasetsGoogleMapBusinessesSearchResponse = Any
DatasetsGoogleMapBusinessesSearchParams = TypedDict('DatasetsGoogleMapBusinessesSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': NotRequired[str],
    'category': NotRequired[str],
    'country': NotRequired[str],
    'state': NotRequired[str],
    'county': NotRequired[str],
    'city': NotRequired[str],
    'town': NotRequired[str],
    'min_rating': NotRequired[float],
    'min_review_count': NotRequired[int],
    'has_website': NotRequired[bool],
    'has_phone': NotRequired[bool],
    'lat': NotRequired[float],
    'lon': NotRequired[float],
    'radius_m': NotRequired[int],
    'sort': NotRequired[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

EBayEbayItemResponse = Any
EBayEbayItemParams = TypedDict('EBayEbayItemParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'item_id': Required[str],
}, total=False)

EBayEbaySearchBody = dict[str, Any]
EBayEbaySearchResponse = Any
EBayEbaySearchParams = TypedDict('EBayEbaySearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'option': Required[EBayEbaySearchBody],
}, total=False)

EBayEbaySellerResponse = Any
EBayEbaySellerParams = TypedDict('EBayEbaySellerParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'seller': Required[str],
}, total=False)

EBayEbaySellerAboutResponse = Any
EBayEbaySellerAboutParams = TypedDict('EBayEbaySellerAboutParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'seller': Required[str],
}, total=False)

EBayEbaySellerFeedbackResponse = Any
EBayEbaySellerFeedbackParams = TypedDict('EBayEbaySellerFeedbackParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'seller': Required[str],
    'page': NotRequired[int],
    'per_page': NotRequired[Literal['24', '48', '72']],
}, total=False)

EBayEbaySellerShopResponse = Any
EBayEbaySellerShopParams = TypedDict('EBayEbaySellerShopParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'seller': Required[str],
    'page': NotRequired[int],
}, total=False)

GeocodingLookupResponse = Any
GeocodingLookupParams = TypedDict('GeocodingLookupParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'osm_ids': Required[str],
    'accept_language': NotRequired[str],
    'addressdetails': NotRequired[bool],
    'extratags': NotRequired[bool],
    'namedetails': NotRequired[bool],
}, total=False)

GeocodingReverseResponse = Any
GeocodingReverseParams = TypedDict('GeocodingReverseParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'lat': Required[float],
    'lon': Required[float],
    'zoom': NotRequired[int],
    'accept_language': NotRequired[str],
    'addressdetails': NotRequired[bool],
    'extratags': NotRequired[bool],
    'namedetails': NotRequired[bool],
}, total=False)

GeocodingSearchResponse = Any
GeocodingSearchParams = TypedDict('GeocodingSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': NotRequired[str],
    'street': NotRequired[str],
    'city': NotRequired[str],
    'county': NotRequired[str],
    'state': NotRequired[str],
    'country': NotRequired[str],
    'postalcode': NotRequired[str],
    'limit': NotRequired[int],
    'countrycodes': NotRequired[str],
    'accept_language': NotRequired[str],
    'addressdetails': NotRequired[bool],
    'extratags': NotRequired[bool],
    'namedetails': NotRequired[bool],
}, total=False)

GoogleFinanceAnalystArticlesResponse = Any
GoogleFinanceAnalystArticlesParams = TypedDict('GoogleFinanceAnalystArticlesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'quote': Required[str],
}, total=False)

GoogleFinanceChartResponse = Any
GoogleFinanceChartParams = TypedDict('GoogleFinanceChartParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'quote': Required[str],
    'window': NotRequired[str],
}, total=False)

GoogleFinanceClassificationResponse = Any
GoogleFinanceClassificationParams = TypedDict('GoogleFinanceClassificationParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'quote': Required[str],
}, total=False)

GoogleFinanceCompanyResponse = Any
GoogleFinanceCompanyParams = TypedDict('GoogleFinanceCompanyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'quote': Required[str],
}, total=False)

GoogleFinanceContextResponse = Any
GoogleFinanceContextParams = TypedDict('GoogleFinanceContextParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
}, total=False)

GoogleFinanceFinancialsResponse = Any
GoogleFinanceFinancialsParams = TypedDict('GoogleFinanceFinancialsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'quote': Required[str],
}, total=False)

GoogleFinanceMarketsCategoryNewsResponse = Any
GoogleFinanceMarketsCategoryNewsParams = TypedDict('GoogleFinanceMarketsCategoryNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category': Required[str],
    'offset': NotRequired[int],
}, total=False)

GoogleFinanceMarketsCategoryStocksResponse = Any
GoogleFinanceMarketsCategoryStocksParams = TypedDict('GoogleFinanceMarketsCategoryStocksParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category': Required[str],
    'offset': NotRequired[int],
}, total=False)

GoogleFinanceMarketsEarningsResponse = Any
GoogleFinanceMarketsEarningsParams = TypedDict('GoogleFinanceMarketsEarningsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

GoogleFinanceMarketsFeaturedResponse = Any
GoogleFinanceMarketsFeaturedParams = TypedDict('GoogleFinanceMarketsFeaturedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

GoogleFinanceMarketsHeadlineResponse = Any
GoogleFinanceMarketsHeadlineParams = TypedDict('GoogleFinanceMarketsHeadlineParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

GoogleFinanceMarketsIndicesResponse = Any
GoogleFinanceMarketsIndicesParams = TypedDict('GoogleFinanceMarketsIndicesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

GoogleFinanceMarketsMoversResponse = Any
GoogleFinanceMarketsMoversParams = TypedDict('GoogleFinanceMarketsMoversParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'categories': NotRequired[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

GoogleFinanceMarketsTopResponse = Any
GoogleFinanceMarketsTopParams = TypedDict('GoogleFinanceMarketsTopParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'metric': NotRequired[int],
    'page': NotRequired[int],
}, total=False)

GoogleFinanceMarketsTrendingResponse = Any
GoogleFinanceMarketsTrendingParams = TypedDict('GoogleFinanceMarketsTrendingParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'limit': NotRequired[int],
}, total=False)

GoogleFinanceNewsResponse = Any
GoogleFinanceNewsParams = TypedDict('GoogleFinanceNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'quote': Required[str],
    'limit': NotRequired[int],
}, total=False)

GoogleFinanceQuoteResponse = Any
GoogleFinanceQuoteParams = TypedDict('GoogleFinanceQuoteParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'quote': Required[str],
}, total=False)

GoogleFinanceRelatedResponse = Any
GoogleFinanceRelatedParams = TypedDict('GoogleFinanceRelatedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'quote': Required[str],
}, total=False)

GoogleFinanceSearchResponse = Any
GoogleFinanceSearchParams = TypedDict('GoogleFinanceSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
}, total=False)

GoogleFinanceTickerResponse = Any
GoogleFinanceTickerParams = TypedDict('GoogleFinanceTickerParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'ticker': Required[str],
    'window': NotRequired[str],
}, total=False)

GoogleJobsBody = dict[str, Any]
GoogleJobsResponse = Any
GoogleJobsParams = TypedDict('GoogleJobsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'option': Required[GoogleJobsBody],
}, total=False)

GoogleMapPlaceResponse = Any
GoogleMapPlaceParams = TypedDict('GoogleMapPlaceParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'place_id': Required[str],
}, total=False)

GoogleMapSearchBody = dict[str, Any]
GoogleMapSearchResponse = Any
GoogleMapSearchParams = TypedDict('GoogleMapSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'mapSearchOption': Required[GoogleMapSearchBody],
}, total=False)

GoogleSearchBody = dict[str, Any]
GoogleSearchResponse = Any
GoogleSearchParams = TypedDict('GoogleSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'searchOption': Required[GoogleSearchBody],
}, total=False)

GoogleSuggestResponse = Any
GoogleSuggestParams = TypedDict('GoogleSuggestParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GoogleTrendsCategoriesResponse = Any
GoogleTrendsCategoriesParams = TypedDict('GoogleTrendsCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

GoogleTrendsEnumsResponse = Any
GoogleTrendsEnumsParams = TypedDict('GoogleTrendsEnumsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

GoogleTrendsExploreBody = dict[str, Any]
GoogleTrendsExploreResponse = Any
GoogleTrendsExploreParams = TypedDict('GoogleTrendsExploreParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[GoogleTrendsExploreBody],
}, total=False)

GoogleTrendsExploreInterestByRegionBody = dict[str, Any]
GoogleTrendsExploreInterestByRegionResponse = Any
GoogleTrendsExploreInterestByRegionParams = TypedDict('GoogleTrendsExploreInterestByRegionParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[GoogleTrendsExploreInterestByRegionBody],
}, total=False)

GoogleTrendsExploreInterestOverTimeBody = dict[str, Any]
GoogleTrendsExploreInterestOverTimeResponse = Any
GoogleTrendsExploreInterestOverTimeParams = TypedDict('GoogleTrendsExploreInterestOverTimeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[GoogleTrendsExploreInterestOverTimeBody],
}, total=False)

GoogleTrendsExploreRelatedTopicsBody = dict[str, Any]
GoogleTrendsExploreRelatedTopicsResponse = Any
GoogleTrendsExploreRelatedTopicsParams = TypedDict('GoogleTrendsExploreRelatedTopicsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[GoogleTrendsExploreRelatedTopicsBody],
}, total=False)

GoogleTrendsExploreRisingQueriesBody = dict[str, Any]
GoogleTrendsExploreRisingQueriesResponse = Any
GoogleTrendsExploreRisingQueriesParams = TypedDict('GoogleTrendsExploreRisingQueriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[GoogleTrendsExploreRisingQueriesBody],
}, total=False)

GoogleTrendsExploreTopQueriesBody = dict[str, Any]
GoogleTrendsExploreTopQueriesResponse = Any
GoogleTrendsExploreTopQueriesParams = TypedDict('GoogleTrendsExploreTopQueriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[GoogleTrendsExploreTopQueriesBody],
}, total=False)

GoogleTrendsLocationsResponse = Any
GoogleTrendsLocationsParams = TypedDict('GoogleTrendsLocationsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

GoogleTrendsTrendingResponse = Any
GoogleTrendsTrendingParams = TypedDict('GoogleTrendsTrendingParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'geo': NotRequired[Literal['AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BV', 'BR', 'IO', 'VG', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CA', 'CV', 'BQ', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CW', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'SZ', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'XK', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'KP', 'MK', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'KR', 'SS', 'ES', 'LK', 'BL', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'SD', 'SR', 'SJ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UM', 'VI', 'UG', 'UA', 'AE', 'GB', 'US', 'UY', 'UZ', 'VU', 'VA', 'VE', 'VN', 'WF', 'EH', 'YE', 'ZM', 'ZW']],
    'hl': NotRequired[str],
    'tz': NotRequired[int],
    'window': NotRequired[Literal['4h', '24h', '48h', '7d']],
    'time_range': NotRequired[Literal['4h', '24h', '48h', '7d']],
    'category': NotRequired[Literal['0', '3', '47', '44', '22', '12', '5', '7', '71', '8', '45', '65', '11', '13', '958', '19', '16', '299', '14', '66', '29', '533', '174', '18', '20', '67']],
    'status': NotRequired[Literal['all', 'active', 'ended']],
    'sort_by': NotRequired[Literal['relevance', 'title', 'recency', 'search_volume']],
    'limit': NotRequired[int],
}, total=False)

GoogleTrendsTrendingDetailBody = dict[str, Any]
GoogleTrendsTrendingDetailResponse = Any
GoogleTrendsTrendingDetailParams = TypedDict('GoogleTrendsTrendingDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[GoogleTrendsTrendingDetailBody],
}, total=False)

GooglePlayAppResponse = Any
GooglePlayAppParams = TypedDict('GooglePlayAppParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'app_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GooglePlayCategoriesResponse = Any
GooglePlayCategoriesParams = TypedDict('GooglePlayCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GooglePlayDatasafetyResponse = Any
GooglePlayDatasafetyParams = TypedDict('GooglePlayDatasafetyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'app_id': Required[str],
    'lang': NotRequired[str],
}, total=False)

GooglePlayDeveloperResponse = Any
GooglePlayDeveloperParams = TypedDict('GooglePlayDeveloperParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'dev_id': Required[str],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'full_detail': NotRequired[bool],
}, total=False)

GooglePlayListResponse = Any
GooglePlayListParams = TypedDict('GooglePlayListParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'collection': NotRequired[str],
    'category': NotRequired[str],
    'age': NotRequired[str],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'full_detail': NotRequired[bool],
}, total=False)

GooglePlayPermissionsResponse = Any
GooglePlayPermissionsParams = TypedDict('GooglePlayPermissionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'app_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'short': NotRequired[bool],
}, total=False)

GooglePlayReviewsResponse = Any
GooglePlayReviewsParams = TypedDict('GooglePlayReviewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'app_id': Required[str],
    'sort': NotRequired[str],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'paginate': NotRequired[bool],
    'next_pagination_token': NotRequired[str],
}, total=False)

GooglePlaySearchResponse = Any
GooglePlaySearchParams = TypedDict('GooglePlaySearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'term': Required[str],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'full_detail': NotRequired[bool],
    'price': NotRequired[str],
}, total=False)

GooglePlaySimilarResponse = Any
GooglePlaySimilarParams = TypedDict('GooglePlaySimilarParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'app_id': Required[str],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'full_detail': NotRequired[bool],
}, total=False)

GooglePlaySuggestResponse = Any
GooglePlaySuggestParams = TypedDict('GooglePlaySuggestParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'term': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

InstagramPostResponse = Any
InstagramPostParams = TypedDict('InstagramPostParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'post_id': Required[str],
}, total=False)

InstagramProfileResponse = Any
InstagramProfileParams = TypedDict('InstagramProfileParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': Required[str],
}, total=False)

InstagramReelsResponse = Any
InstagramReelsParams = TypedDict('InstagramReelsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'max_id': NotRequired[str],
}, total=False)

JustWatchJustwatchAgeCertificationsResponse = Any
JustWatchJustwatchAgeCertificationsParams = TypedDict('JustWatchJustwatchAgeCertificationsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': NotRequired[str],
}, total=False)

JustWatchJustwatchDiscoverResponse = Any
JustWatchJustwatchDiscoverParams = TypedDict('JustWatchJustwatchDiscoverParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': NotRequired[str],
    'language': NotRequired[str],
    'limit': NotRequired[int],
    'type': NotRequired[Literal['all', 'movie', 'show']],
    'genres': NotRequired[str],
    'providers': NotRequired[str],
    'monetization_types': NotRequired[Literal['FLATRATE', 'FREE', 'ADS', 'RENT', 'BUY']],
    'year_min': NotRequired[int],
    'year_max': NotRequired[int],
}, total=False)

JustWatchJustwatchEpisodeByIdResponse = Any
JustWatchJustwatchEpisodeByIdParams = TypedDict('JustWatchJustwatchEpisodeByIdParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'country': NotRequired[str],
    'language': NotRequired[str],
}, total=False)

JustWatchJustwatchEpisodeOffersResponse = Any
JustWatchJustwatchEpisodeOffersParams = TypedDict('JustWatchJustwatchEpisodeOffersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'countries': NotRequired[str],
    'language': NotRequired[str],
}, total=False)

JustWatchJustwatchGenreTitlesResponse = Any
JustWatchJustwatchGenreTitlesParams = TypedDict('JustWatchJustwatchGenreTitlesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'genre': Required[str],
    'country': NotRequired[str],
    'language': NotRequired[str],
    'limit': NotRequired[int],
    'type': NotRequired[Literal['all', 'movie', 'show']],
}, total=False)

JustWatchJustwatchGenresResponse = Any
JustWatchJustwatchGenresParams = TypedDict('JustWatchJustwatchGenresParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'language': NotRequired[str],
}, total=False)

JustWatchJustwatchMonetizationTitlesResponse = Any
JustWatchJustwatchMonetizationTitlesParams = TypedDict('JustWatchJustwatchMonetizationTitlesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'monetization_type': Required[Literal['FLATRATE', 'FREE', 'ADS', 'RENT', 'BUY']],
    'country': NotRequired[str],
    'language': NotRequired[str],
    'limit': NotRequired[int],
    'type': NotRequired[Literal['all', 'movie', 'show']],
}, total=False)

JustWatchJustwatchNewResponse = Any
JustWatchJustwatchNewParams = TypedDict('JustWatchJustwatchNewParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': NotRequired[str],
    'language': NotRequired[str],
    'limit': NotRequired[int],
    'type': NotRequired[Literal['all', 'movie', 'show']],
}, total=False)

JustWatchJustwatchPopularResponse = Any
JustWatchJustwatchPopularParams = TypedDict('JustWatchJustwatchPopularParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': NotRequired[str],
    'language': NotRequired[str],
    'limit': NotRequired[int],
    'type': NotRequired[Literal['all', 'movie', 'show']],
}, total=False)

JustWatchJustwatchProviderTitlesResponse = Any
JustWatchJustwatchProviderTitlesParams = TypedDict('JustWatchJustwatchProviderTitlesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'provider': Required[str],
    'country': NotRequired[str],
    'language': NotRequired[str],
    'limit': NotRequired[int],
    'type': NotRequired[Literal['all', 'movie', 'show']],
}, total=False)

JustWatchJustwatchProvidersResponse = Any
JustWatchJustwatchProvidersParams = TypedDict('JustWatchJustwatchProvidersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': NotRequired[str],
}, total=False)

JustWatchJustwatchSearchResponse = Any
JustWatchJustwatchSearchParams = TypedDict('JustWatchJustwatchSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'query': Required[str],
    'country': NotRequired[str],
    'language': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

JustWatchJustwatchSeasonByIdResponse = Any
JustWatchJustwatchSeasonByIdParams = TypedDict('JustWatchJustwatchSeasonByIdParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'country': NotRequired[str],
    'language': NotRequired[str],
}, total=False)

JustWatchJustwatchSeasonEpisodesResponse = Any
JustWatchJustwatchSeasonEpisodesParams = TypedDict('JustWatchJustwatchSeasonEpisodesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'season_id': Required[str],
    'country': NotRequired[str],
    'language': NotRequired[str],
}, total=False)

JustWatchJustwatchShowSeasonsResponse = Any
JustWatchJustwatchShowSeasonsParams = TypedDict('JustWatchJustwatchShowSeasonsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'show_id': Required[str],
    'country': NotRequired[str],
    'language': NotRequired[str],
}, total=False)

JustWatchJustwatchTitleResponse = Any
JustWatchJustwatchTitleParams = TypedDict('JustWatchJustwatchTitleParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'path': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

JustWatchJustwatchTitleAnalysisResponse = Any
JustWatchJustwatchTitleAnalysisParams = TypedDict('JustWatchJustwatchTitleAnalysisParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'path': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

JustWatchJustwatchTitleByIdResponse = Any
JustWatchJustwatchTitleByIdParams = TypedDict('JustWatchJustwatchTitleByIdParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'country': NotRequired[str],
    'language': NotRequired[str],
}, total=False)

JustWatchJustwatchTitleMediaResponse = Any
JustWatchJustwatchTitleMediaParams = TypedDict('JustWatchJustwatchTitleMediaParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'country': NotRequired[str],
    'language': NotRequired[str],
}, total=False)

JustWatchJustwatchTitleOffersResponse = Any
JustWatchJustwatchTitleOffersParams = TypedDict('JustWatchJustwatchTitleOffersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'countries': NotRequired[str],
    'language': NotRequired[str],
}, total=False)

JustWatchJustwatchTitleSimilarResponse = Any
JustWatchJustwatchTitleSimilarParams = TypedDict('JustWatchJustwatchTitleSimilarParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'country': NotRequired[str],
    'language': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

LinkedInLinkedinCompanyResponse = Any
LinkedInLinkedinCompanyParams = TypedDict('LinkedInLinkedinCompanyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

LinkedInLinkedinProductResponse = Any
LinkedInLinkedinProductParams = TypedDict('LinkedInLinkedinProductParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

LinkedInLinkedinShowcaseResponse = Any
LinkedInLinkedinShowcaseParams = TypedDict('LinkedInLinkedinShowcaseParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

MetaPingResponse = Any
MetaPingParams = TypedDict('MetaPingParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

ProductHuntCategoryResponse = Any
ProductHuntCategoryParams = TypedDict('ProductHuntCategoryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
}, total=False)

ProductHuntCategoryProductsResponse = Any
ProductHuntCategoryProductsParams = TypedDict('ProductHuntCategoryProductsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
    'featured_only': NotRequired[bool],
    'order': NotRequired[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
    'tags': NotRequired[str],
}, total=False)

ProductHuntLeaderboardResponse = Any
ProductHuntLeaderboardParams = TypedDict('ProductHuntLeaderboardParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'scope': NotRequired[Literal['daily', 'weekly', 'monthly', 'yearly']],
    'date': NotRequired[str],
    'year': NotRequired[int],
    'month': NotRequired[int],
    'day': NotRequired[int],
    'week': NotRequired[int],
    'featured': NotRequired[bool],
    'order': NotRequired[str],
    'cursor': NotRequired[str],
}, total=False)

ProductHuntProductResponse = Any
ProductHuntProductParams = TypedDict('ProductHuntProductParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

ProductHuntAboutResponse = Any
ProductHuntAboutParams = TypedDict('ProductHuntAboutParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

ProductHuntAlternativesResponse = Any
ProductHuntAlternativesParams = TypedDict('ProductHuntAlternativesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'first': NotRequired[int],
    'cursor': NotRequired[str],
    'order': NotRequired[str],
    'tags': NotRequired[str],
}, total=False)

ProductHuntCustomersResponse = Any
ProductHuntCustomersParams = TypedDict('ProductHuntCustomersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'order': NotRequired[Literal['customers', 'latest_launch']],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

ProductHuntLaunchesResponse = Any
ProductHuntLaunchesParams = TypedDict('ProductHuntLaunchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'cursor': NotRequired[str],
    'order': NotRequired[str],
}, total=False)

ProductHuntMakersResponse = Any
ProductHuntMakersParams = TypedDict('ProductHuntMakersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'cursor': NotRequired[str],
}, total=False)

ProductHuntReviewsResponse = Any
ProductHuntReviewsParams = TypedDict('ProductHuntReviewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

ProductHuntSearchResponse = Any
ProductHuntSearchParams = TypedDict('ProductHuntSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'query': Required[str],
    'type': NotRequired[Literal['product', 'user', 'launch']],
    'page': NotRequired[int],
    'featured': NotRequired[bool],
    'topics': NotRequired[str],
}, total=False)

MetaReadyResponse = Any
MetaReadyParams = TypedDict('MetaReadyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

ReferralsClickBody = dict[str, Any]
ReferralsClickResponse = Any
ReferralsClickParams = TypedDict('ReferralsClickParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[ReferralsClickBody],
}, total=False)

ReferralsMeResponse = Any
ReferralsMeParams = TypedDict('ReferralsMeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

ReferralsMeEventsResponse = Any
ReferralsMeEventsParams = TypedDict('ReferralsMeEventsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'limit': NotRequired[int],
}, total=False)

SimilarWebSearchResponse = Any
SimilarWebSearchParams = TypedDict('SimilarWebSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
}, total=False)

SimilarWebWebResponse = Any
SimilarWebWebParams = TypedDict('SimilarWebWebParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'domain': Required[str],
}, total=False)

SpotifyPodcastsCategoriesResponse = Any
SpotifyPodcastsCategoriesParams = TypedDict('SpotifyPodcastsCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'page_offset': NotRequired[int],
    'page_limit': NotRequired[int],
    'section_offset': NotRequired[int],
    'section_limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsChartsResponse = Any
SpotifyPodcastsChartsParams = TypedDict('SpotifyPodcastsChartsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'chart': NotRequired[str],
    'region': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

SpotifyPodcastsEpisodeResponse = Any
SpotifyPodcastsEpisodeParams = TypedDict('SpotifyPodcastsEpisodeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyPodcastsHomeResponse = Any
SpotifyPodcastsHomeParams = TypedDict('SpotifyPodcastsHomeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'page_offset': NotRequired[int],
    'page_limit': NotRequired[int],
    'section_offset': NotRequired[int],
    'section_limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsSearchResponse = Any
SpotifyPodcastsSearchParams = TypedDict('SpotifyPodcastsSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_audiobooks': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsShowResponse = Any
SpotifyPodcastsShowParams = TypedDict('SpotifyPodcastsShowParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'include_content_capability_trait': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsShowEpisodesResponse = Any
SpotifyPodcastsShowEpisodesParams = TypedDict('SpotifyPodcastsShowEpisodesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsShowRecommendationsResponse = Any
SpotifyPodcastsShowRecommendationsParams = TypedDict('SpotifyPodcastsShowRecommendationsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
}, total=False)

SpotifyAlbumResponse = Any
SpotifyAlbumParams = TypedDict('SpotifyAlbumParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyAlbumTracksResponse = Any
SpotifyAlbumTracksParams = TypedDict('SpotifyAlbumTracksParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyAlbumsSearchResponse = Any
SpotifyAlbumsSearchParams = TypedDict('SpotifyAlbumsSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyArtistResponse = Any
SpotifyArtistParams = TypedDict('SpotifyArtistParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyArtistAlbumsResponse = Any
SpotifyArtistAlbumsParams = TypedDict('SpotifyArtistAlbumsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'type': NotRequired[str],
    'order': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyArtistPlaylistsResponse = Any
SpotifyArtistPlaylistsParams = TypedDict('SpotifyArtistPlaylistsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyArtistRelatedResponse = Any
SpotifyArtistRelatedParams = TypedDict('SpotifyArtistRelatedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyArtistsSearchResponse = Any
SpotifyArtistsSearchParams = TypedDict('SpotifyArtistsSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyAudiobookResponse = Any
SpotifyAudiobookParams = TypedDict('SpotifyAudiobookParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyAudiobookChaptersResponse = Any
SpotifyAudiobookChaptersParams = TypedDict('SpotifyAudiobookChaptersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyAudiobooksSearchResponse = Any
SpotifyAudiobooksSearchParams = TypedDict('SpotifyAudiobooksSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyChapterResponse = Any
SpotifyChapterParams = TypedDict('SpotifyChapterParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyEpisodesSearchResponse = Any
SpotifyEpisodesSearchParams = TypedDict('SpotifyEpisodesSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyFeaturedChartsByCountryResponse = Any
SpotifyFeaturedChartsByCountryParams = TypedDict('SpotifyFeaturedChartsByCountryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country_code': NotRequired[str],
    'content_id': NotRequired[str],
}, total=False)

SpotifyGenreResponse = Any
SpotifyGenreParams = TypedDict('SpotifyGenreParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'page_offset': NotRequired[int],
    'page_limit': NotRequired[int],
    'section_offset': NotRequired[int],
    'section_limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyHomeResponse = Any
SpotifyHomeParams = TypedDict('SpotifyHomeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'time_zone': NotRequired[str],
    'sp_t': NotRequired[str],
    'facet': NotRequired[str],
    'section_items_limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPlaylistResponse = Any
SpotifyPlaylistParams = TypedDict('SpotifyPlaylistParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'enable_watch_feed_entrypoint': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPlaylistsSearchResponse = Any
SpotifyPlaylistsSearchParams = TypedDict('SpotifyPlaylistsSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPopularByCountryResponse = Any
SpotifyPopularByCountryParams = TypedDict('SpotifyPopularByCountryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country_code': NotRequired[str],
}, total=False)

SpotifyProfileResponse = Any
SpotifyProfileParams = TypedDict('SpotifyProfileParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': NotRequired[str],
    'uri': NotRequired[str],
    'url': NotRequired[str],
    'playlist_limit': NotRequired[int],
    'artist_limit': NotRequired[int],
    'episode_limit': NotRequired[int],
}, total=False)

SpotifyProfileFollowersResponse = Any
SpotifyProfileFollowersParams = TypedDict('SpotifyProfileFollowersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': NotRequired[str],
    'uri': NotRequired[str],
    'url': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyProfilePlaylistsResponse = Any
SpotifyProfilePlaylistsParams = TypedDict('SpotifyProfilePlaylistsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': NotRequired[str],
    'uri': NotRequired[str],
    'url': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyProfilesSearchResponse = Any
SpotifyProfilesSearchParams = TypedDict('SpotifyProfilesSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifySearchResponse = Any
SpotifySearchParams = TypedDict('SpotifySearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_artist_has_concerts_field': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
    'is_prefix': NotRequired[bool],
}, total=False)

SpotifySectionResponse = Any
SpotifySectionParams = TypedDict('SpotifySectionParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyShowsSearchResponse = Any
SpotifyShowsSearchParams = TypedDict('SpotifyShowsSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyTrackResponse = Any
SpotifyTrackParams = TypedDict('SpotifyTrackParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyTrackRecommendedResponse = Any
SpotifyTrackRecommendedParams = TypedDict('SpotifyTrackRecommendedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

SpotifyTrackSimilarAlbumsResponse = Any
SpotifyTrackSimilarAlbumsParams = TypedDict('SpotifyTrackSimilarAlbumsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'limit': NotRequired[int],
    'albums_only': NotRequired[bool],
}, total=False)

SpotifyTracksSearchResponse = Any
SpotifyTracksSearchParams = TypedDict('SpotifyTracksSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

TiktokCategoryResponse = Any
TiktokCategoryParams = TypedDict('TiktokCategoryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokVideoCommentsResponse = Any
TiktokVideoCommentsParams = TypedDict('TiktokVideoCommentsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'aweme_id': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokExploreResponse = Any
TiktokExploreParams = TypedDict('TiktokExploreParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[int],
}, total=False)

TiktokChallengeResponse = Any
TiktokChallengeParams = TypedDict('TiktokChallengeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'name': Required[str],
}, total=False)

TiktokChallengeListResponse = Any
TiktokChallengeListParams = TypedDict('TiktokChallengeListParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokPopularTrendCountryIndustryMetaResponse = Any
TiktokPopularTrendCountryIndustryMetaParams = TypedDict('TiktokPopularTrendCountryIndustryMetaParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokPopularTrendCreatorResponse = Any
TiktokPopularTrendCreatorParams = TypedDict('TiktokPopularTrendCreatorParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'sort_by': NotRequired[Literal['follower', 'engagement', 'avg_views']],
    'creator_country': NotRequired[str],
    'audience_count': NotRequired[Literal['1', '2', '3', '4']],
}, total=False)

TiktokPostResponse = Any
TiktokPostParams = TypedDict('TiktokPostParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

TiktokProfilePostResponse = Any
TiktokProfilePostParams = TypedDict('TiktokProfilePostParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'secUid': Required[str],
    'cursor': NotRequired[int],
    'sort_type': NotRequired[Literal['0', '1', '2']],
}, total=False)

TiktokProfileResponse = Any
TiktokProfileParams = TypedDict('TiktokProfileParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'handler': Required[str],
}, total=False)

TiktokSearchResponse = Any
TiktokSearchParams = TypedDict('TiktokSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokSearchHashtagResponse = Any
TiktokSearchHashtagParams = TypedDict('TiktokSearchHashtagParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokSearchUserResponse = Any
TiktokSearchUserParams = TypedDict('TiktokSearchUserParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokTopAdsAnalysisResponse = Any
TiktokTopAdsAnalysisParams = TypedDict('TiktokTopAdsAnalysisParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'material_id': Required[str],
    'metric': NotRequired[Literal['retain_ctr', 'retain_cvr', 'click_cnt', 'convert_cnt', 'play_retain_cnt']],
    'period_type': NotRequired[Literal['7', '30', '180']],
}, total=False)

TiktokTopAdsDetailResponse = Any
TiktokTopAdsDetailParams = TypedDict('TiktokTopAdsDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'material_id': Required[str],
}, total=False)

TiktokTopAdsFiltersResponse = Any
TiktokTopAdsFiltersParams = TypedDict('TiktokTopAdsFiltersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokTopAdsListResponse = Any
TiktokTopAdsListParams = TypedDict('TiktokTopAdsListParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'period': NotRequired[Literal['7', '30', '180']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'order_by': NotRequired[Literal['for_you', 'impression', 'ctr', 'play_2s_rate', 'play_6s_rate', 'cvr', 'like']],
    'country_code': NotRequired[str],
    'keyword': NotRequired[str],
    'industry': NotRequired[str],
    'objective': NotRequired[str],
    'ad_language': NotRequired[str],
    'pattern_label': NotRequired[str],
    'duration': NotRequired[Literal['time-2', 'time-3', 'time-4', 'time-5', 'time-6', 'time-7']],
    'like': NotRequired[Literal['1', '2', '3', '4', '5']],
    'ad_format': NotRequired[Literal['1', '2']],
}, total=False)

TiktokTopAdsLocationInfoResponse = Any
TiktokTopAdsLocationInfoParams = TypedDict('TiktokTopAdsLocationInfoParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'module': NotRequired[int],
}, total=False)

TiktokTopAdsLocationsResponse = Any
TiktokTopAdsLocationsParams = TypedDict('TiktokTopAdsLocationsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokTopAdsRecommendResponse = Any
TiktokTopAdsRecommendParams = TypedDict('TiktokTopAdsRecommendParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'material_id': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

TiktokTopAdsSafetyResponse = Any
TiktokTopAdsSafetyParams = TypedDict('TiktokTopAdsSafetyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokTopAdsSpotlightResponse = Any
TiktokTopAdsSpotlightParams = TypedDict('TiktokTopAdsSpotlightParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

TiktokTopAdsSuggestionsResponse = Any
TiktokTopAdsSuggestionsParams = TypedDict('TiktokTopAdsSuggestionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'count': NotRequired[int],
    'scenario': NotRequired[int],
}, total=False)

TiktokTrendingResponse = Any
TiktokTrendingParams = TypedDict('TiktokTrendingParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TripAdvisorTripadvisorAutocompleteResponse = Any
TripAdvisorTripadvisorAutocompleteParams = TypedDict('TripAdvisorTripadvisorAutocompleteParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'limit': NotRequired[int],
    'locale': NotRequired[str],
    'scope_geo_id': NotRequired[int],
    'type': NotRequired[str],
    'search_session_id': NotRequired[str],
    'typeahead_id': NotRequired[str],
    'route_uid': NotRequired[str],
}, total=False)

TripAdvisorTripadvisorEnumsResponse = Any
TripAdvisorTripadvisorEnumsParams = TypedDict('TripAdvisorTripadvisorEnumsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TripAdvisorTripadvisorHotelsResponse = Any
TripAdvisorTripadvisorHotelsParams = TypedDict('TripAdvisorTripadvisorHotelsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'geo_id': Required[int],
    'filter_id': NotRequired[str],
    'class': NotRequired[int],
    'amenities': NotRequired[list[int]],
    'price_min': NotRequired[int],
    'price_max': NotRequired[int],
    'pricing_mode': NotRequired[str],
    'travelers_choice': NotRequired[bool],
    'travelers_choice_botb': NotRequired[bool],
    'currency': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'sort': NotRequired[str],
}, total=False)

TripAdvisorTripadvisorPlaceResponse = Any
TripAdvisorTripadvisorPlaceParams = TypedDict('TripAdvisorTripadvisorPlaceParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'url': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

TripAdvisorTripadvisorReviewsResponse = Any
TripAdvisorTripadvisorReviewsParams = TypedDict('TripAdvisorTripadvisorReviewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'language': NotRequired[str],
    'sort_type': NotRequired[str],
    'sort_by': NotRequired[str],
    'ratings': NotRequired[list[int]],
    'do_machine_translation': NotRequired[bool],
    'photos_per_review_limit': NotRequired[int],
}, total=False)

TripAdvisorTripadvisorSearchResponse = Any
TripAdvisorTripadvisorSearchParams = TypedDict('TripAdvisorTripadvisorSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'geo_id': Required[int],
    'type': Required[str],
    'filter_id': NotRequired[str],
    'class': NotRequired[int],
    'amenities': NotRequired[list[int]],
    'price_min': NotRequired[int],
    'price_max': NotRequired[int],
    'pricing_mode': NotRequired[str],
    'travelers_choice': NotRequired[bool],
    'travelers_choice_botb': NotRequired[bool],
    'restaurant_date': NotRequired[str],
    'restaurant_time': NotRequired[str],
    'restaurant_guests': NotRequired[int],
    'establishment_types': NotRequired[list[int]],
    'online_options': NotRequired[list[int]],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'locale': NotRequired[str],
    'currency': NotRequired[str],
    'sort': NotRequired[str],
}, total=False)

TrustpilotBusinessSearchResponse = Any
TrustpilotBusinessSearchParams = TypedDict('TrustpilotBusinessSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'country': NotRequired[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

TrustpilotBusinessResponse = Any
TrustpilotBusinessParams = TypedDict('TrustpilotBusinessParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
}, total=False)

TrustpilotBusinessRelatedResponse = Any
TrustpilotBusinessRelatedParams = TypedDict('TrustpilotBusinessRelatedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
}, total=False)

TrustpilotBusinessReviewsResponse = Any
TrustpilotBusinessReviewsParams = TypedDict('TrustpilotBusinessReviewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
    'page': NotRequired[int],
    'stars': NotRequired[int],
    'verified': NotRequired[bool],
    'replied': NotRequired[bool],
    'language': NotRequired[str],
    'q': NotRequired[str],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
}, total=False)

TrustpilotCategoriesResponse = Any
TrustpilotCategoriesParams = TypedDict('TrustpilotCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TrustpilotCategorySearchResponse = Any
TrustpilotCategorySearchParams = TypedDict('TrustpilotCategorySearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'country': NotRequired[str],
    'locale': NotRequired[str],
    'size': NotRequired[int],
}, total=False)

TrustpilotCategoryResponse = Any
TrustpilotCategoryParams = TypedDict('TrustpilotCategoryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
    'page': NotRequired[int],
}, total=False)

UsageMeEndpointsResponse = Any
UsageMeEndpointsParams = TypedDict('UsageMeEndpointsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'range': NotRequired[Literal['period', 'day', 'week', 'month', 'custom']],
    'limit': NotRequired[int],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

UsageMeOverviewResponse = Any
UsageMeOverviewParams = TypedDict('UsageMeOverviewParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'range': NotRequired[Literal['period', 'day', 'week', 'month', 'custom']],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

UsageMeRecentIpsResponse = Any
UsageMeRecentIpsParams = TypedDict('UsageMeRecentIpsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'range': NotRequired[Literal['period', 'day', 'week', 'month', 'custom']],
    'limit': NotRequired[int],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

UsageMeTimeseriesResponse = Any
UsageMeTimeseriesParams = TypedDict('UsageMeTimeseriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'range': NotRequired[Literal['period', 'day', 'week', 'month', 'custom']],
    'bucket': NotRequired[Literal['hour', 'day']],
    'endpoint': NotRequired[str],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

UserMeResponse = Any
UserMeParams = TypedDict('UserMeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

UserMeApiKeysResponse = Any
UserMeApiKeysParams = TypedDict('UserMeApiKeysParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

UserMeApiKeysRotateResponse = Any
UserMeApiKeysRotateParams = TypedDict('UserMeApiKeysRotateParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

UserMeApiKeysRevealResponse = Any
UserMeApiKeysRevealParams = TypedDict('UserMeApiKeysRevealParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

YahooFinanceCalendarsResponse = Any
YahooFinanceCalendarsParams = TypedDict('YahooFinanceCalendarsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

YahooFinanceCalendarResponse = Any
YahooFinanceCalendarParams = TypedDict('YahooFinanceCalendarParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'type': Required[str],
    'start': NotRequired[str],
    'end': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'market_cap': NotRequired[float],
    'filter_most_active': NotRequired[bool],
}, total=False)

YahooFinanceDownloadBody = dict[str, Any]
YahooFinanceDownloadResponse = Any
YahooFinanceDownloadParams = TypedDict('YahooFinanceDownloadParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[YahooFinanceDownloadBody],
}, total=False)

YahooFinanceIndustriesResponse = Any
YahooFinanceIndustriesParams = TypedDict('YahooFinanceIndustriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

YahooFinanceIndustryResponse = Any
YahooFinanceIndustryParams = TypedDict('YahooFinanceIndustryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'key': Required[str],
}, total=False)

YahooFinanceMarketStatusResponse = Any
YahooFinanceMarketStatusParams = TypedDict('YahooFinanceMarketStatusParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'market': Required[str],
}, total=False)

YahooFinanceMarketSummaryResponse = Any
YahooFinanceMarketSummaryParams = TypedDict('YahooFinanceMarketSummaryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'market': Required[str],
}, total=False)

YahooFinanceScreenerCustomBody = dict[str, Any]
YahooFinanceScreenerCustomResponse = Any
YahooFinanceScreenerCustomParams = TypedDict('YahooFinanceScreenerCustomParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[YahooFinanceScreenerCustomBody],
}, total=False)

YahooFinanceScreenerResponse = Any
YahooFinanceScreenerParams = TypedDict('YahooFinanceScreenerParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'sort_field': NotRequired[str],
    'sort_asc': NotRequired[bool],
}, total=False)

YahooFinanceScreenersResponse = Any
YahooFinanceScreenersParams = TypedDict('YahooFinanceScreenersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

YahooFinanceSearchResponse = Any
YahooFinanceSearchParams = TypedDict('YahooFinanceSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'quotes_count': NotRequired[int],
    'news_count': NotRequired[int],
    'lists_count': NotRequired[int],
    'include_research': NotRequired[bool],
    'enable_fuzzy_query': NotRequired[bool],
}, total=False)

YahooFinanceSectorsResponse = Any
YahooFinanceSectorsParams = TypedDict('YahooFinanceSectorsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

YahooFinanceSectorResponse = Any
YahooFinanceSectorParams = TypedDict('YahooFinanceSectorParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'key': Required[str],
}, total=False)

YahooFinanceTickerActionsResponse = Any
YahooFinanceTickerActionsParams = TypedDict('YahooFinanceTickerActionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerAnalystsResponse = Any
YahooFinanceTickerAnalystsParams = TypedDict('YahooFinanceTickerAnalystsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerCalendarResponse = Any
YahooFinanceTickerCalendarParams = TypedDict('YahooFinanceTickerCalendarParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerCapitalGainsResponse = Any
YahooFinanceTickerCapitalGainsParams = TypedDict('YahooFinanceTickerCapitalGainsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerDividendsResponse = Any
YahooFinanceTickerDividendsParams = TypedDict('YahooFinanceTickerDividendsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerEarningsResponse = Any
YahooFinanceTickerEarningsParams = TypedDict('YahooFinanceTickerEarningsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerEarningsDatesResponse = Any
YahooFinanceTickerEarningsDatesParams = TypedDict('YahooFinanceTickerEarningsDatesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

YahooFinanceTickerFinancialsResponse = Any
YahooFinanceTickerFinancialsParams = TypedDict('YahooFinanceTickerFinancialsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
    'statement': NotRequired[str],
    'period': NotRequired[str],
}, total=False)

YahooFinanceTickerFundsResponse = Any
YahooFinanceTickerFundsParams = TypedDict('YahooFinanceTickerFundsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerHistoryResponse = Any
YahooFinanceTickerHistoryParams = TypedDict('YahooFinanceTickerHistoryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
    'period': NotRequired[str],
    'start': NotRequired[str],
    'end': NotRequired[str],
    'interval': NotRequired[str],
    'include_prepost': NotRequired[bool],
    'include_actions': NotRequired[bool],
    'auto_adjust': NotRequired[bool],
    'back_adjust': NotRequired[bool],
    'keepna': NotRequired[bool],
    'rounding': NotRequired[bool],
}, total=False)

YahooFinanceTickerHistoryMetadataResponse = Any
YahooFinanceTickerHistoryMetadataParams = TypedDict('YahooFinanceTickerHistoryMetadataParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerHoldersResponse = Any
YahooFinanceTickerHoldersParams = TypedDict('YahooFinanceTickerHoldersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerInfoResponse = Any
YahooFinanceTickerInfoParams = TypedDict('YahooFinanceTickerInfoParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerIsinResponse = Any
YahooFinanceTickerIsinParams = TypedDict('YahooFinanceTickerIsinParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerNewsResponse = Any
YahooFinanceTickerNewsParams = TypedDict('YahooFinanceTickerNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
    'count': NotRequired[int],
    'tab': NotRequired[str],
}, total=False)

YahooFinanceTickerOptionsResponse = Any
YahooFinanceTickerOptionsParams = TypedDict('YahooFinanceTickerOptionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerOptionsExpirationResponse = Any
YahooFinanceTickerOptionsExpirationParams = TypedDict('YahooFinanceTickerOptionsExpirationParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
    'expiration': Required[str],
}, total=False)

YahooFinanceTickerQuoteResponse = Any
YahooFinanceTickerQuoteParams = TypedDict('YahooFinanceTickerQuoteParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerSecFilingsResponse = Any
YahooFinanceTickerSecFilingsParams = TypedDict('YahooFinanceTickerSecFilingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerSharesResponse = Any
YahooFinanceTickerSharesParams = TypedDict('YahooFinanceTickerSharesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerSharesFullResponse = Any
YahooFinanceTickerSharesFullParams = TypedDict('YahooFinanceTickerSharesFullParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
    'start': NotRequired[str],
    'end': NotRequired[str],
}, total=False)

YahooFinanceTickerSplitsResponse = Any
YahooFinanceTickerSplitsParams = TypedDict('YahooFinanceTickerSplitsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerSustainabilityResponse = Any
YahooFinanceTickerSustainabilityParams = TypedDict('YahooFinanceTickerSustainabilityParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerValuationResponse = Any
YahooFinanceTickerValuationParams = TypedDict('YahooFinanceTickerValuationParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTrendingResponse = Any
YahooFinanceTrendingParams = TypedDict('YahooFinanceTrendingParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'region': Required[str],
    'count': NotRequired[int],
}, total=False)

YoutubeCaptionsResponse = Any
YoutubeCaptionsParams = TypedDict('YoutubeCaptionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'lang': NotRequired[str],
}, total=False)

YoutubeChannelPlaylistsResponse = Any
YoutubeChannelPlaylistsParams = TypedDict('YoutubeChannelPlaylistsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'continuation_token': NotRequired[str],
}, total=False)

YoutubeChannelSearchResponse = Any
YoutubeChannelSearchParams = TypedDict('YoutubeChannelSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'q': Required[str],
    'continuation_token': NotRequired[str],
}, total=False)

YoutubeChannelShortsResponse = Any
YoutubeChannelShortsParams = TypedDict('YoutubeChannelShortsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

YoutubeChannelVideosResponse = Any
YoutubeChannelVideosParams = TypedDict('YoutubeChannelVideosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'continuation_token': NotRequired[str],
}, total=False)

YoutubeCommentsResponse = Any
YoutubeCommentsParams = TypedDict('YoutubeCommentsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'continuation_token': NotRequired[str],
}, total=False)

YoutubePlaylistResponse = Any
YoutubePlaylistParams = TypedDict('YoutubePlaylistParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'continuation_token': NotRequired[str],
}, total=False)

YoutubeProfileResponse = Any
YoutubeProfileParams = TypedDict('YoutubeProfileParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

YoutubeSearchResponse = Any
YoutubeSearchParams = TypedDict('YoutubeSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': NotRequired[str],
    'search_query': NotRequired[str],
    'continuation_token': NotRequired[str],
    'type': NotRequired[Literal['video', 'channel', 'playlist', 'movie']],
    'sort_by': NotRequired[Literal['relevance', 'upload_date', 'view_count', 'rating']],
    'upload_date': NotRequired[Literal['last_hour', 'today', 'this_week', 'this_month', 'this_year']],
    'duration': NotRequired[Literal['short', 'medium', 'long']],
    'features': NotRequired[str],
    'params': NotRequired[str],
}, total=False)

YoutubeTagResponse = Any
YoutubeTagParams = TypedDict('YoutubeTagParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'tag': Required[str],
    'type': NotRequired[Literal['all', 'shorts']],
    'continuation_token': NotRequired[str],
}, total=False)

YoutubeTranscriptResponse = Any
YoutubeTranscriptParams = TypedDict('YoutubeTranscriptParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'lang': NotRequired[str],
    'translate_to': NotRequired[str],
    'format': NotRequired[Literal['json', 'text', 'srt', 'vtt']],
    'timestamps': NotRequired[bool],
}, total=False)

YoutubeTranscriptLanguagesResponse = Any
YoutubeTranscriptLanguagesParams = TypedDict('YoutubeTranscriptLanguagesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

YoutubeVideoResponse = Any
YoutubeVideoParams = TypedDict('YoutubeVideoParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

ZillowAutocompleteResponse = Any
ZillowAutocompleteParams = TypedDict('ZillowAutocompleteParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'query': Required[str],
    'limit': NotRequired[int],
    'status': NotRequired[str],
}, total=False)

ZillowPropertyResponse = Any
ZillowPropertyParams = TypedDict('ZillowPropertyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'zpid': Required[str],
}, total=False)

ZillowSearchResponse = Any
ZillowSearchParams = TypedDict('ZillowSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'location': Required[str],
    'page': NotRequired[int],
    'status': NotRequired[str],
    'region_id': NotRequired[int],
    'region_type': NotRequired[int],
    'west': NotRequired[float],
    'east': NotRequired[float],
    'south': NotRequired[float],
    'north': NotRequired[float],
}, total=False)

class AirbnbGroup:
    def room(self, **params: Unpack[AirbnbRoomParams]) -> AirbnbRoomResponse: ...
    def room_calendar(self, **params: Unpack[AirbnbRoomCalendarParams]) -> AirbnbRoomCalendarResponse: ...
    def room_reviews(self, **params: Unpack[AirbnbRoomReviewsParams]) -> AirbnbRoomReviewsResponse: ...
    def search(self, **params: Unpack[AirbnbSearchParams]) -> AirbnbSearchResponse: ...

class AmazonGroup:
    def product(self, **params: Unpack[AmazonProductParams]) -> AmazonProductResponse: ...
    def search(self, **params: Unpack[AmazonSearchParams]) -> AmazonSearchResponse: ...
    def suggest(self, **params: Unpack[AmazonSuggestParams]) -> AmazonSuggestResponse: ...

class ApplePodcastsGroup:
    def charts(self, **params: Unpack[ApplePodcastsChartsParams]) -> ApplePodcastsChartsResponse: ...
    def episodes_search(self, **params: Unpack[ApplePodcastsEpisodesSearchParams]) -> ApplePodcastsEpisodesSearchResponse: ...
    def search(self, **params: Unpack[ApplePodcastsSearchParams]) -> ApplePodcastsSearchResponse: ...
    def show(self, **params: Unpack[ApplePodcastsShowParams]) -> ApplePodcastsShowResponse: ...
    def show_episodes(self, **params: Unpack[ApplePodcastsShowEpisodesParams]) -> ApplePodcastsShowEpisodesResponse: ...

class AppStoreGroup:
    def app(self, **params: Unpack[AppStoreAppParams]) -> AppStoreAppResponse: ...
    def developer(self, **params: Unpack[AppStoreDeveloperParams]) -> AppStoreDeveloperResponse: ...
    def list(self, **params: Unpack[AppStoreListParams]) -> AppStoreListResponse: ...
    def privacy(self, **params: Unpack[AppStorePrivacyParams]) -> AppStorePrivacyResponse: ...
    def ratings(self, **params: Unpack[AppStoreRatingsParams]) -> AppStoreRatingsResponse: ...
    def reviews(self, **params: Unpack[AppStoreReviewsParams]) -> AppStoreReviewsResponse: ...
    def search(self, **params: Unpack[AppStoreSearchParams]) -> AppStoreSearchResponse: ...
    def similar(self, **params: Unpack[AppStoreSimilarParams]) -> AppStoreSimilarResponse: ...
    def suggest(self, **params: Unpack[AppStoreSuggestParams]) -> AppStoreSuggestResponse: ...
    def version_history(self, **params: Unpack[AppStoreVersionHistoryParams]) -> AppStoreVersionHistoryResponse: ...

class BillingGroup:
    def me(self, **params: Unpack[BillingMeParams]) -> BillingMeResponse: ...
    def me_checkout(self, **params: Unpack[BillingMeCheckoutParams]) -> BillingMeCheckoutResponse: ...
    def me_events(self, **params: Unpack[BillingMeEventsParams]) -> BillingMeEventsResponse: ...
    def me_periods(self, **params: Unpack[BillingMePeriodsParams]) -> BillingMePeriodsResponse: ...
    def me_period(self, **params: Unpack[BillingMePeriodParams]) -> BillingMePeriodResponse: ...
    def me_period_statement(self, **params: Unpack[BillingMePeriodStatementParams]) -> BillingMePeriodStatementResponse: ...
    def me_period_statement_download(self, **params: Unpack[BillingMePeriodStatementDownloadParams]) -> BillingMePeriodStatementDownloadResponse: ...
    def me_portal(self, **params: Unpack[BillingMePortalParams]) -> BillingMePortalResponse: ...

class BingGroup:
    def images(self, **params: Unpack[BingImagesParams]) -> BingImagesResponse: ...
    def news(self, **params: Unpack[BingNewsParams]) -> BingNewsResponse: ...
    def search(self, **params: Unpack[BingSearchParams]) -> BingSearchResponse: ...
    def suggest(self, **params: Unpack[BingSuggestParams]) -> BingSuggestResponse: ...
    def videos(self, **params: Unpack[BingVideosParams]) -> BingVideosResponse: ...

class BraveGroup:
    def images(self, **params: Unpack[BraveImagesParams]) -> BraveImagesResponse: ...
    def news(self, **params: Unpack[BraveNewsParams]) -> BraveNewsResponse: ...
    def search(self, **params: Unpack[BraveSearchParams]) -> BraveSearchResponse: ...
    def suggest(self, **params: Unpack[BraveSuggestParams]) -> BraveSuggestResponse: ...
    def videos(self, **params: Unpack[BraveVideosParams]) -> BraveVideosResponse: ...

class CoinGeckoGroup:
    def categories(self, **params: Unpack[CoinGeckoCategoriesParams]) -> CoinGeckoCategoriesResponse: ...
    def category_coins(self, **params: Unpack[CoinGeckoCategoryCoinsParams]) -> CoinGeckoCategoryCoinsResponse: ...
    def chains(self, **params: Unpack[CoinGeckoChainsParams]) -> CoinGeckoChainsResponse: ...
    def chain(self, **params: Unpack[CoinGeckoChainParams]) -> CoinGeckoChainResponse: ...
    def coin(self, **params: Unpack[CoinGeckoCoinParams]) -> CoinGeckoCoinResponse: ...
    def coin_analysis(self, **params: Unpack[CoinGeckoCoinAnalysisParams]) -> CoinGeckoCoinAnalysisResponse: ...
    def exchange(self, **params: Unpack[CoinGeckoExchangeParams]) -> CoinGeckoExchangeResponse: ...
    def exchanges(self, **params: Unpack[CoinGeckoExchangesParams]) -> CoinGeckoExchangesResponse: ...
    def gainers_losers(self, **params: Unpack[CoinGeckoGainersLosersParams]) -> CoinGeckoGainersLosersResponse: ...
    def global_(self, **params: Unpack[CoinGeckoGlobalParams]) -> CoinGeckoGlobalResponse: ...
    def global_charts(self, **params: Unpack[CoinGeckoGlobalChartsParams]) -> CoinGeckoGlobalChartsResponse: ...
    def learn_articles(self, **params: Unpack[CoinGeckoLearnArticlesParams]) -> CoinGeckoLearnArticlesResponse: ...
    def markets(self, **params: Unpack[CoinGeckoMarketsParams]) -> CoinGeckoMarketsResponse: ...
    def new_coins(self, **params: Unpack[CoinGeckoNewCoinsParams]) -> CoinGeckoNewCoinsResponse: ...
    def news(self, **params: Unpack[CoinGeckoNewsParams]) -> CoinGeckoNewsResponse: ...
    def nft_category(self, **params: Unpack[CoinGeckoNftCategoryParams]) -> CoinGeckoNftCategoryResponse: ...
    def nfts(self, **params: Unpack[CoinGeckoNftsParams]) -> CoinGeckoNftsResponse: ...
    def search(self, **params: Unpack[CoinGeckoSearchParams]) -> CoinGeckoSearchResponse: ...
    def token_unlocks(self, **params: Unpack[CoinGeckoTokenUnlocksParams]) -> CoinGeckoTokenUnlocksResponse: ...
    def treasuries(self, **params: Unpack[CoinGeckoTreasuriesParams]) -> CoinGeckoTreasuriesResponse: ...
    def trending(self, **params: Unpack[CoinGeckoTrendingParams]) -> CoinGeckoTrendingResponse: ...

class DatasetsGroup:
    def list(self, **params: Unpack[DatasetsListParams]) -> DatasetsListResponse: ...
    def google_map_businesses_facets(self, **params: Unpack[DatasetsGoogleMapBusinessesFacetsParams]) -> DatasetsGoogleMapBusinessesFacetsResponse: ...
    def google_map_businesses_item(self, **params: Unpack[DatasetsGoogleMapBusinessesItemParams]) -> DatasetsGoogleMapBusinessesItemResponse: ...
    def google_map_businesses_nearby(self, **params: Unpack[DatasetsGoogleMapBusinessesNearbyParams]) -> DatasetsGoogleMapBusinessesNearbyResponse: ...
    def google_map_businesses_search(self, **params: Unpack[DatasetsGoogleMapBusinessesSearchParams]) -> DatasetsGoogleMapBusinessesSearchResponse: ...

class EBayGroup:
    def ebay_item(self, **params: Unpack[EBayEbayItemParams]) -> EBayEbayItemResponse: ...
    def ebay_search(self, **params: Unpack[EBayEbaySearchParams]) -> EBayEbaySearchResponse: ...
    def ebay_seller(self, **params: Unpack[EBayEbaySellerParams]) -> EBayEbaySellerResponse: ...
    def ebay_seller_about(self, **params: Unpack[EBayEbaySellerAboutParams]) -> EBayEbaySellerAboutResponse: ...
    def ebay_seller_feedback(self, **params: Unpack[EBayEbaySellerFeedbackParams]) -> EBayEbaySellerFeedbackResponse: ...
    def ebay_seller_shop(self, **params: Unpack[EBayEbaySellerShopParams]) -> EBayEbaySellerShopResponse: ...

class GeocodingGroup:
    def lookup(self, **params: Unpack[GeocodingLookupParams]) -> GeocodingLookupResponse: ...
    def reverse(self, **params: Unpack[GeocodingReverseParams]) -> GeocodingReverseResponse: ...
    def search(self, **params: Unpack[GeocodingSearchParams]) -> GeocodingSearchResponse: ...

class GoogleGroup:
    def finance_analyst_articles(self, **params: Unpack[GoogleFinanceAnalystArticlesParams]) -> GoogleFinanceAnalystArticlesResponse: ...
    def finance_chart(self, **params: Unpack[GoogleFinanceChartParams]) -> GoogleFinanceChartResponse: ...
    def finance_classification(self, **params: Unpack[GoogleFinanceClassificationParams]) -> GoogleFinanceClassificationResponse: ...
    def finance_company(self, **params: Unpack[GoogleFinanceCompanyParams]) -> GoogleFinanceCompanyResponse: ...
    def finance_context(self, **params: Unpack[GoogleFinanceContextParams]) -> GoogleFinanceContextResponse: ...
    def finance_financials(self, **params: Unpack[GoogleFinanceFinancialsParams]) -> GoogleFinanceFinancialsResponse: ...
    def finance_markets_category_news(self, **params: Unpack[GoogleFinanceMarketsCategoryNewsParams]) -> GoogleFinanceMarketsCategoryNewsResponse: ...
    def finance_markets_category_stocks(self, **params: Unpack[GoogleFinanceMarketsCategoryStocksParams]) -> GoogleFinanceMarketsCategoryStocksResponse: ...
    def finance_markets_earnings(self, **params: Unpack[GoogleFinanceMarketsEarningsParams]) -> GoogleFinanceMarketsEarningsResponse: ...
    def finance_markets_featured(self, **params: Unpack[GoogleFinanceMarketsFeaturedParams]) -> GoogleFinanceMarketsFeaturedResponse: ...
    def finance_markets_headline(self, **params: Unpack[GoogleFinanceMarketsHeadlineParams]) -> GoogleFinanceMarketsHeadlineResponse: ...
    def finance_markets_indices(self, **params: Unpack[GoogleFinanceMarketsIndicesParams]) -> GoogleFinanceMarketsIndicesResponse: ...
    def finance_markets_movers(self, **params: Unpack[GoogleFinanceMarketsMoversParams]) -> GoogleFinanceMarketsMoversResponse: ...
    def finance_markets_top(self, **params: Unpack[GoogleFinanceMarketsTopParams]) -> GoogleFinanceMarketsTopResponse: ...
    def finance_markets_trending(self, **params: Unpack[GoogleFinanceMarketsTrendingParams]) -> GoogleFinanceMarketsTrendingResponse: ...
    def finance_news(self, **params: Unpack[GoogleFinanceNewsParams]) -> GoogleFinanceNewsResponse: ...
    def finance_quote(self, **params: Unpack[GoogleFinanceQuoteParams]) -> GoogleFinanceQuoteResponse: ...
    def finance_related(self, **params: Unpack[GoogleFinanceRelatedParams]) -> GoogleFinanceRelatedResponse: ...
    def finance_search(self, **params: Unpack[GoogleFinanceSearchParams]) -> GoogleFinanceSearchResponse: ...
    def finance_ticker(self, **params: Unpack[GoogleFinanceTickerParams]) -> GoogleFinanceTickerResponse: ...
    def jobs(self, **params: Unpack[GoogleJobsParams]) -> GoogleJobsResponse: ...
    def map_place(self, **params: Unpack[GoogleMapPlaceParams]) -> GoogleMapPlaceResponse: ...
    def map_search(self, **params: Unpack[GoogleMapSearchParams]) -> GoogleMapSearchResponse: ...
    def search(self, **params: Unpack[GoogleSearchParams]) -> GoogleSearchResponse: ...
    def suggest(self, **params: Unpack[GoogleSuggestParams]) -> GoogleSuggestResponse: ...
    def trends_categories(self, **params: Unpack[GoogleTrendsCategoriesParams]) -> GoogleTrendsCategoriesResponse: ...
    def trends_enums(self, **params: Unpack[GoogleTrendsEnumsParams]) -> GoogleTrendsEnumsResponse: ...
    def trends_explore(self, **params: Unpack[GoogleTrendsExploreParams]) -> GoogleTrendsExploreResponse: ...
    def trends_explore_interest_by_region(self, **params: Unpack[GoogleTrendsExploreInterestByRegionParams]) -> GoogleTrendsExploreInterestByRegionResponse: ...
    def trends_explore_interest_over_time(self, **params: Unpack[GoogleTrendsExploreInterestOverTimeParams]) -> GoogleTrendsExploreInterestOverTimeResponse: ...
    def trends_explore_related_topics(self, **params: Unpack[GoogleTrendsExploreRelatedTopicsParams]) -> GoogleTrendsExploreRelatedTopicsResponse: ...
    def trends_explore_rising_queries(self, **params: Unpack[GoogleTrendsExploreRisingQueriesParams]) -> GoogleTrendsExploreRisingQueriesResponse: ...
    def trends_explore_top_queries(self, **params: Unpack[GoogleTrendsExploreTopQueriesParams]) -> GoogleTrendsExploreTopQueriesResponse: ...
    def trends_locations(self, **params: Unpack[GoogleTrendsLocationsParams]) -> GoogleTrendsLocationsResponse: ...
    def trends_trending(self, **params: Unpack[GoogleTrendsTrendingParams]) -> GoogleTrendsTrendingResponse: ...
    def trends_trending_detail(self, **params: Unpack[GoogleTrendsTrendingDetailParams]) -> GoogleTrendsTrendingDetailResponse: ...

class GooglePlayGroup:
    def app(self, **params: Unpack[GooglePlayAppParams]) -> GooglePlayAppResponse: ...
    def categories(self, **params: Unpack[GooglePlayCategoriesParams]) -> GooglePlayCategoriesResponse: ...
    def datasafety(self, **params: Unpack[GooglePlayDatasafetyParams]) -> GooglePlayDatasafetyResponse: ...
    def developer(self, **params: Unpack[GooglePlayDeveloperParams]) -> GooglePlayDeveloperResponse: ...
    def list(self, **params: Unpack[GooglePlayListParams]) -> GooglePlayListResponse: ...
    def permissions(self, **params: Unpack[GooglePlayPermissionsParams]) -> GooglePlayPermissionsResponse: ...
    def reviews(self, **params: Unpack[GooglePlayReviewsParams]) -> GooglePlayReviewsResponse: ...
    def search(self, **params: Unpack[GooglePlaySearchParams]) -> GooglePlaySearchResponse: ...
    def similar(self, **params: Unpack[GooglePlaySimilarParams]) -> GooglePlaySimilarResponse: ...
    def suggest(self, **params: Unpack[GooglePlaySuggestParams]) -> GooglePlaySuggestResponse: ...

class InstagramGroup:
    def post(self, **params: Unpack[InstagramPostParams]) -> InstagramPostResponse: ...
    def profile(self, **params: Unpack[InstagramProfileParams]) -> InstagramProfileResponse: ...
    def reels(self, **params: Unpack[InstagramReelsParams]) -> InstagramReelsResponse: ...

class JustWatchGroup:
    def justwatch_age_certifications(self, **params: Unpack[JustWatchJustwatchAgeCertificationsParams]) -> JustWatchJustwatchAgeCertificationsResponse: ...
    def justwatch_discover(self, **params: Unpack[JustWatchJustwatchDiscoverParams]) -> JustWatchJustwatchDiscoverResponse: ...
    def justwatch_episode_by_id(self, **params: Unpack[JustWatchJustwatchEpisodeByIdParams]) -> JustWatchJustwatchEpisodeByIdResponse: ...
    def justwatch_episode_offers(self, **params: Unpack[JustWatchJustwatchEpisodeOffersParams]) -> JustWatchJustwatchEpisodeOffersResponse: ...
    def justwatch_genre_titles(self, **params: Unpack[JustWatchJustwatchGenreTitlesParams]) -> JustWatchJustwatchGenreTitlesResponse: ...
    def justwatch_genres(self, **params: Unpack[JustWatchJustwatchGenresParams]) -> JustWatchJustwatchGenresResponse: ...
    def justwatch_monetization_titles(self, **params: Unpack[JustWatchJustwatchMonetizationTitlesParams]) -> JustWatchJustwatchMonetizationTitlesResponse: ...
    def justwatch_new(self, **params: Unpack[JustWatchJustwatchNewParams]) -> JustWatchJustwatchNewResponse: ...
    def justwatch_popular(self, **params: Unpack[JustWatchJustwatchPopularParams]) -> JustWatchJustwatchPopularResponse: ...
    def justwatch_provider_titles(self, **params: Unpack[JustWatchJustwatchProviderTitlesParams]) -> JustWatchJustwatchProviderTitlesResponse: ...
    def justwatch_providers(self, **params: Unpack[JustWatchJustwatchProvidersParams]) -> JustWatchJustwatchProvidersResponse: ...
    def justwatch_search(self, **params: Unpack[JustWatchJustwatchSearchParams]) -> JustWatchJustwatchSearchResponse: ...
    def justwatch_season_by_id(self, **params: Unpack[JustWatchJustwatchSeasonByIdParams]) -> JustWatchJustwatchSeasonByIdResponse: ...
    def justwatch_season_episodes(self, **params: Unpack[JustWatchJustwatchSeasonEpisodesParams]) -> JustWatchJustwatchSeasonEpisodesResponse: ...
    def justwatch_show_seasons(self, **params: Unpack[JustWatchJustwatchShowSeasonsParams]) -> JustWatchJustwatchShowSeasonsResponse: ...
    def justwatch_title(self, **params: Unpack[JustWatchJustwatchTitleParams]) -> JustWatchJustwatchTitleResponse: ...
    def justwatch_title_analysis(self, **params: Unpack[JustWatchJustwatchTitleAnalysisParams]) -> JustWatchJustwatchTitleAnalysisResponse: ...
    def justwatch_title_by_id(self, **params: Unpack[JustWatchJustwatchTitleByIdParams]) -> JustWatchJustwatchTitleByIdResponse: ...
    def justwatch_title_media(self, **params: Unpack[JustWatchJustwatchTitleMediaParams]) -> JustWatchJustwatchTitleMediaResponse: ...
    def justwatch_title_offers(self, **params: Unpack[JustWatchJustwatchTitleOffersParams]) -> JustWatchJustwatchTitleOffersResponse: ...
    def justwatch_title_similar(self, **params: Unpack[JustWatchJustwatchTitleSimilarParams]) -> JustWatchJustwatchTitleSimilarResponse: ...

class LinkedInGroup:
    def linkedin_company(self, **params: Unpack[LinkedInLinkedinCompanyParams]) -> LinkedInLinkedinCompanyResponse: ...
    def linkedin_product(self, **params: Unpack[LinkedInLinkedinProductParams]) -> LinkedInLinkedinProductResponse: ...
    def linkedin_showcase(self, **params: Unpack[LinkedInLinkedinShowcaseParams]) -> LinkedInLinkedinShowcaseResponse: ...

class MetaGroup:
    def ping(self, **params: Unpack[MetaPingParams]) -> MetaPingResponse: ...
    def ready(self, **params: Unpack[MetaReadyParams]) -> MetaReadyResponse: ...

class ProductHuntGroup:
    def category(self, **params: Unpack[ProductHuntCategoryParams]) -> ProductHuntCategoryResponse: ...
    def category_products(self, **params: Unpack[ProductHuntCategoryProductsParams]) -> ProductHuntCategoryProductsResponse: ...
    def leaderboard(self, **params: Unpack[ProductHuntLeaderboardParams]) -> ProductHuntLeaderboardResponse: ...
    def product(self, **params: Unpack[ProductHuntProductParams]) -> ProductHuntProductResponse: ...
    def about(self, **params: Unpack[ProductHuntAboutParams]) -> ProductHuntAboutResponse: ...
    def alternatives(self, **params: Unpack[ProductHuntAlternativesParams]) -> ProductHuntAlternativesResponse: ...
    def customers(self, **params: Unpack[ProductHuntCustomersParams]) -> ProductHuntCustomersResponse: ...
    def launches(self, **params: Unpack[ProductHuntLaunchesParams]) -> ProductHuntLaunchesResponse: ...
    def makers(self, **params: Unpack[ProductHuntMakersParams]) -> ProductHuntMakersResponse: ...
    def reviews(self, **params: Unpack[ProductHuntReviewsParams]) -> ProductHuntReviewsResponse: ...
    def search(self, **params: Unpack[ProductHuntSearchParams]) -> ProductHuntSearchResponse: ...

class ReferralsGroup:
    def click(self, **params: Unpack[ReferralsClickParams]) -> ReferralsClickResponse: ...
    def me(self, **params: Unpack[ReferralsMeParams]) -> ReferralsMeResponse: ...
    def me_events(self, **params: Unpack[ReferralsMeEventsParams]) -> ReferralsMeEventsResponse: ...

class SimilarWebGroup:
    def search(self, **params: Unpack[SimilarWebSearchParams]) -> SimilarWebSearchResponse: ...
    def web(self, **params: Unpack[SimilarWebWebParams]) -> SimilarWebWebResponse: ...

class SpotifyPodcastsGroup:
    def categories(self, **params: Unpack[SpotifyPodcastsCategoriesParams]) -> SpotifyPodcastsCategoriesResponse: ...
    def charts(self, **params: Unpack[SpotifyPodcastsChartsParams]) -> SpotifyPodcastsChartsResponse: ...
    def episode(self, **params: Unpack[SpotifyPodcastsEpisodeParams]) -> SpotifyPodcastsEpisodeResponse: ...
    def home(self, **params: Unpack[SpotifyPodcastsHomeParams]) -> SpotifyPodcastsHomeResponse: ...
    def search(self, **params: Unpack[SpotifyPodcastsSearchParams]) -> SpotifyPodcastsSearchResponse: ...
    def show(self, **params: Unpack[SpotifyPodcastsShowParams]) -> SpotifyPodcastsShowResponse: ...
    def show_episodes(self, **params: Unpack[SpotifyPodcastsShowEpisodesParams]) -> SpotifyPodcastsShowEpisodesResponse: ...
    def show_recommendations(self, **params: Unpack[SpotifyPodcastsShowRecommendationsParams]) -> SpotifyPodcastsShowRecommendationsResponse: ...

class SpotifyGroup:
    def album(self, **params: Unpack[SpotifyAlbumParams]) -> SpotifyAlbumResponse: ...
    def album_tracks(self, **params: Unpack[SpotifyAlbumTracksParams]) -> SpotifyAlbumTracksResponse: ...
    def albums_search(self, **params: Unpack[SpotifyAlbumsSearchParams]) -> SpotifyAlbumsSearchResponse: ...
    def artist(self, **params: Unpack[SpotifyArtistParams]) -> SpotifyArtistResponse: ...
    def artist_albums(self, **params: Unpack[SpotifyArtistAlbumsParams]) -> SpotifyArtistAlbumsResponse: ...
    def artist_playlists(self, **params: Unpack[SpotifyArtistPlaylistsParams]) -> SpotifyArtistPlaylistsResponse: ...
    def artist_related(self, **params: Unpack[SpotifyArtistRelatedParams]) -> SpotifyArtistRelatedResponse: ...
    def artists_search(self, **params: Unpack[SpotifyArtistsSearchParams]) -> SpotifyArtistsSearchResponse: ...
    def audiobook(self, **params: Unpack[SpotifyAudiobookParams]) -> SpotifyAudiobookResponse: ...
    def audiobook_chapters(self, **params: Unpack[SpotifyAudiobookChaptersParams]) -> SpotifyAudiobookChaptersResponse: ...
    def audiobooks_search(self, **params: Unpack[SpotifyAudiobooksSearchParams]) -> SpotifyAudiobooksSearchResponse: ...
    def chapter(self, **params: Unpack[SpotifyChapterParams]) -> SpotifyChapterResponse: ...
    def episodes_search(self, **params: Unpack[SpotifyEpisodesSearchParams]) -> SpotifyEpisodesSearchResponse: ...
    def featured_charts_by_country(self, **params: Unpack[SpotifyFeaturedChartsByCountryParams]) -> SpotifyFeaturedChartsByCountryResponse: ...
    def genre(self, **params: Unpack[SpotifyGenreParams]) -> SpotifyGenreResponse: ...
    def home(self, **params: Unpack[SpotifyHomeParams]) -> SpotifyHomeResponse: ...
    def playlist(self, **params: Unpack[SpotifyPlaylistParams]) -> SpotifyPlaylistResponse: ...
    def playlists_search(self, **params: Unpack[SpotifyPlaylistsSearchParams]) -> SpotifyPlaylistsSearchResponse: ...
    def popular_by_country(self, **params: Unpack[SpotifyPopularByCountryParams]) -> SpotifyPopularByCountryResponse: ...
    def profile(self, **params: Unpack[SpotifyProfileParams]) -> SpotifyProfileResponse: ...
    def profile_followers(self, **params: Unpack[SpotifyProfileFollowersParams]) -> SpotifyProfileFollowersResponse: ...
    def profile_playlists(self, **params: Unpack[SpotifyProfilePlaylistsParams]) -> SpotifyProfilePlaylistsResponse: ...
    def profiles_search(self, **params: Unpack[SpotifyProfilesSearchParams]) -> SpotifyProfilesSearchResponse: ...
    def search(self, **params: Unpack[SpotifySearchParams]) -> SpotifySearchResponse: ...
    def section(self, **params: Unpack[SpotifySectionParams]) -> SpotifySectionResponse: ...
    def shows_search(self, **params: Unpack[SpotifyShowsSearchParams]) -> SpotifyShowsSearchResponse: ...
    def track(self, **params: Unpack[SpotifyTrackParams]) -> SpotifyTrackResponse: ...
    def track_recommended(self, **params: Unpack[SpotifyTrackRecommendedParams]) -> SpotifyTrackRecommendedResponse: ...
    def track_similar_albums(self, **params: Unpack[SpotifyTrackSimilarAlbumsParams]) -> SpotifyTrackSimilarAlbumsResponse: ...
    def tracks_search(self, **params: Unpack[SpotifyTracksSearchParams]) -> SpotifyTracksSearchResponse: ...

class TiktokGroup:
    def category(self, **params: Unpack[TiktokCategoryParams]) -> TiktokCategoryResponse: ...
    def video_comments(self, **params: Unpack[TiktokVideoCommentsParams]) -> TiktokVideoCommentsResponse: ...
    def explore(self, **params: Unpack[TiktokExploreParams]) -> TiktokExploreResponse: ...
    def challenge(self, **params: Unpack[TiktokChallengeParams]) -> TiktokChallengeResponse: ...
    def challenge_list(self, **params: Unpack[TiktokChallengeListParams]) -> TiktokChallengeListResponse: ...
    def popular_trend_country_industry_meta(self, **params: Unpack[TiktokPopularTrendCountryIndustryMetaParams]) -> TiktokPopularTrendCountryIndustryMetaResponse: ...
    def popular_trend_creator(self, **params: Unpack[TiktokPopularTrendCreatorParams]) -> TiktokPopularTrendCreatorResponse: ...
    def post(self, **params: Unpack[TiktokPostParams]) -> TiktokPostResponse: ...
    def profile_post(self, **params: Unpack[TiktokProfilePostParams]) -> TiktokProfilePostResponse: ...
    def profile(self, **params: Unpack[TiktokProfileParams]) -> TiktokProfileResponse: ...
    def search(self, **params: Unpack[TiktokSearchParams]) -> TiktokSearchResponse: ...
    def search_hashtag(self, **params: Unpack[TiktokSearchHashtagParams]) -> TiktokSearchHashtagResponse: ...
    def search_user(self, **params: Unpack[TiktokSearchUserParams]) -> TiktokSearchUserResponse: ...
    def top_ads_analysis(self, **params: Unpack[TiktokTopAdsAnalysisParams]) -> TiktokTopAdsAnalysisResponse: ...
    def top_ads_detail(self, **params: Unpack[TiktokTopAdsDetailParams]) -> TiktokTopAdsDetailResponse: ...
    def top_ads_filters(self, **params: Unpack[TiktokTopAdsFiltersParams]) -> TiktokTopAdsFiltersResponse: ...
    def top_ads_list(self, **params: Unpack[TiktokTopAdsListParams]) -> TiktokTopAdsListResponse: ...
    def top_ads_location_info(self, **params: Unpack[TiktokTopAdsLocationInfoParams]) -> TiktokTopAdsLocationInfoResponse: ...
    def top_ads_locations(self, **params: Unpack[TiktokTopAdsLocationsParams]) -> TiktokTopAdsLocationsResponse: ...
    def top_ads_recommend(self, **params: Unpack[TiktokTopAdsRecommendParams]) -> TiktokTopAdsRecommendResponse: ...
    def top_ads_safety(self, **params: Unpack[TiktokTopAdsSafetyParams]) -> TiktokTopAdsSafetyResponse: ...
    def top_ads_spotlight(self, **params: Unpack[TiktokTopAdsSpotlightParams]) -> TiktokTopAdsSpotlightResponse: ...
    def top_ads_suggestions(self, **params: Unpack[TiktokTopAdsSuggestionsParams]) -> TiktokTopAdsSuggestionsResponse: ...
    def trending(self, **params: Unpack[TiktokTrendingParams]) -> TiktokTrendingResponse: ...

class TripAdvisorGroup:
    def tripadvisor_autocomplete(self, **params: Unpack[TripAdvisorTripadvisorAutocompleteParams]) -> TripAdvisorTripadvisorAutocompleteResponse: ...
    def tripadvisor_enums(self, **params: Unpack[TripAdvisorTripadvisorEnumsParams]) -> TripAdvisorTripadvisorEnumsResponse: ...
    def tripadvisor_hotels(self, **params: Unpack[TripAdvisorTripadvisorHotelsParams]) -> TripAdvisorTripadvisorHotelsResponse: ...
    def tripadvisor_place(self, **params: Unpack[TripAdvisorTripadvisorPlaceParams]) -> TripAdvisorTripadvisorPlaceResponse: ...
    def tripadvisor_reviews(self, **params: Unpack[TripAdvisorTripadvisorReviewsParams]) -> TripAdvisorTripadvisorReviewsResponse: ...
    def tripadvisor_search(self, **params: Unpack[TripAdvisorTripadvisorSearchParams]) -> TripAdvisorTripadvisorSearchResponse: ...

class TrustpilotGroup:
    def business_search(self, **params: Unpack[TrustpilotBusinessSearchParams]) -> TrustpilotBusinessSearchResponse: ...
    def business(self, **params: Unpack[TrustpilotBusinessParams]) -> TrustpilotBusinessResponse: ...
    def business_related(self, **params: Unpack[TrustpilotBusinessRelatedParams]) -> TrustpilotBusinessRelatedResponse: ...
    def business_reviews(self, **params: Unpack[TrustpilotBusinessReviewsParams]) -> TrustpilotBusinessReviewsResponse: ...
    def categories(self, **params: Unpack[TrustpilotCategoriesParams]) -> TrustpilotCategoriesResponse: ...
    def category_search(self, **params: Unpack[TrustpilotCategorySearchParams]) -> TrustpilotCategorySearchResponse: ...
    def category(self, **params: Unpack[TrustpilotCategoryParams]) -> TrustpilotCategoryResponse: ...

class UsageGroup:
    def me_endpoints(self, **params: Unpack[UsageMeEndpointsParams]) -> UsageMeEndpointsResponse: ...
    def me_overview(self, **params: Unpack[UsageMeOverviewParams]) -> UsageMeOverviewResponse: ...
    def me_recent_ips(self, **params: Unpack[UsageMeRecentIpsParams]) -> UsageMeRecentIpsResponse: ...
    def me_timeseries(self, **params: Unpack[UsageMeTimeseriesParams]) -> UsageMeTimeseriesResponse: ...

class UserGroup:
    def me(self, **params: Unpack[UserMeParams]) -> UserMeResponse: ...
    def me_api_keys(self, **params: Unpack[UserMeApiKeysParams]) -> UserMeApiKeysResponse: ...
    def me_api_keys_rotate(self, **params: Unpack[UserMeApiKeysRotateParams]) -> UserMeApiKeysRotateResponse: ...
    def me_api_keys_reveal(self, **params: Unpack[UserMeApiKeysRevealParams]) -> UserMeApiKeysRevealResponse: ...

class YahooFinanceGroup:
    def calendars(self, **params: Unpack[YahooFinanceCalendarsParams]) -> YahooFinanceCalendarsResponse: ...
    def calendar(self, **params: Unpack[YahooFinanceCalendarParams]) -> YahooFinanceCalendarResponse: ...
    def download(self, **params: Unpack[YahooFinanceDownloadParams]) -> YahooFinanceDownloadResponse: ...
    def industries(self, **params: Unpack[YahooFinanceIndustriesParams]) -> YahooFinanceIndustriesResponse: ...
    def industry(self, **params: Unpack[YahooFinanceIndustryParams]) -> YahooFinanceIndustryResponse: ...
    def market_status(self, **params: Unpack[YahooFinanceMarketStatusParams]) -> YahooFinanceMarketStatusResponse: ...
    def market_summary(self, **params: Unpack[YahooFinanceMarketSummaryParams]) -> YahooFinanceMarketSummaryResponse: ...
    def screener_custom(self, **params: Unpack[YahooFinanceScreenerCustomParams]) -> YahooFinanceScreenerCustomResponse: ...
    def screener(self, **params: Unpack[YahooFinanceScreenerParams]) -> YahooFinanceScreenerResponse: ...
    def screeners(self, **params: Unpack[YahooFinanceScreenersParams]) -> YahooFinanceScreenersResponse: ...
    def search(self, **params: Unpack[YahooFinanceSearchParams]) -> YahooFinanceSearchResponse: ...
    def sectors(self, **params: Unpack[YahooFinanceSectorsParams]) -> YahooFinanceSectorsResponse: ...
    def sector(self, **params: Unpack[YahooFinanceSectorParams]) -> YahooFinanceSectorResponse: ...
    def ticker_actions(self, **params: Unpack[YahooFinanceTickerActionsParams]) -> YahooFinanceTickerActionsResponse: ...
    def ticker_analysts(self, **params: Unpack[YahooFinanceTickerAnalystsParams]) -> YahooFinanceTickerAnalystsResponse: ...
    def ticker_calendar(self, **params: Unpack[YahooFinanceTickerCalendarParams]) -> YahooFinanceTickerCalendarResponse: ...
    def ticker_capital_gains(self, **params: Unpack[YahooFinanceTickerCapitalGainsParams]) -> YahooFinanceTickerCapitalGainsResponse: ...
    def ticker_dividends(self, **params: Unpack[YahooFinanceTickerDividendsParams]) -> YahooFinanceTickerDividendsResponse: ...
    def ticker_earnings(self, **params: Unpack[YahooFinanceTickerEarningsParams]) -> YahooFinanceTickerEarningsResponse: ...
    def ticker_earnings_dates(self, **params: Unpack[YahooFinanceTickerEarningsDatesParams]) -> YahooFinanceTickerEarningsDatesResponse: ...
    def ticker_financials(self, **params: Unpack[YahooFinanceTickerFinancialsParams]) -> YahooFinanceTickerFinancialsResponse: ...
    def ticker_funds(self, **params: Unpack[YahooFinanceTickerFundsParams]) -> YahooFinanceTickerFundsResponse: ...
    def ticker_history(self, **params: Unpack[YahooFinanceTickerHistoryParams]) -> YahooFinanceTickerHistoryResponse: ...
    def ticker_history_metadata(self, **params: Unpack[YahooFinanceTickerHistoryMetadataParams]) -> YahooFinanceTickerHistoryMetadataResponse: ...
    def ticker_holders(self, **params: Unpack[YahooFinanceTickerHoldersParams]) -> YahooFinanceTickerHoldersResponse: ...
    def ticker_info(self, **params: Unpack[YahooFinanceTickerInfoParams]) -> YahooFinanceTickerInfoResponse: ...
    def ticker_isin(self, **params: Unpack[YahooFinanceTickerIsinParams]) -> YahooFinanceTickerIsinResponse: ...
    def ticker_news(self, **params: Unpack[YahooFinanceTickerNewsParams]) -> YahooFinanceTickerNewsResponse: ...
    def ticker_options(self, **params: Unpack[YahooFinanceTickerOptionsParams]) -> YahooFinanceTickerOptionsResponse: ...
    def ticker_options_expiration(self, **params: Unpack[YahooFinanceTickerOptionsExpirationParams]) -> YahooFinanceTickerOptionsExpirationResponse: ...
    def ticker_quote(self, **params: Unpack[YahooFinanceTickerQuoteParams]) -> YahooFinanceTickerQuoteResponse: ...
    def ticker_sec_filings(self, **params: Unpack[YahooFinanceTickerSecFilingsParams]) -> YahooFinanceTickerSecFilingsResponse: ...
    def ticker_shares(self, **params: Unpack[YahooFinanceTickerSharesParams]) -> YahooFinanceTickerSharesResponse: ...
    def ticker_shares_full(self, **params: Unpack[YahooFinanceTickerSharesFullParams]) -> YahooFinanceTickerSharesFullResponse: ...
    def ticker_splits(self, **params: Unpack[YahooFinanceTickerSplitsParams]) -> YahooFinanceTickerSplitsResponse: ...
    def ticker_sustainability(self, **params: Unpack[YahooFinanceTickerSustainabilityParams]) -> YahooFinanceTickerSustainabilityResponse: ...
    def ticker_valuation(self, **params: Unpack[YahooFinanceTickerValuationParams]) -> YahooFinanceTickerValuationResponse: ...
    def trending(self, **params: Unpack[YahooFinanceTrendingParams]) -> YahooFinanceTrendingResponse: ...

class YoutubeGroup:
    def captions(self, **params: Unpack[YoutubeCaptionsParams]) -> YoutubeCaptionsResponse: ...
    def channel_playlists(self, **params: Unpack[YoutubeChannelPlaylistsParams]) -> YoutubeChannelPlaylistsResponse: ...
    def channel_search(self, **params: Unpack[YoutubeChannelSearchParams]) -> YoutubeChannelSearchResponse: ...
    def channel_shorts(self, **params: Unpack[YoutubeChannelShortsParams]) -> YoutubeChannelShortsResponse: ...
    def channel_videos(self, **params: Unpack[YoutubeChannelVideosParams]) -> YoutubeChannelVideosResponse: ...
    def comments(self, **params: Unpack[YoutubeCommentsParams]) -> YoutubeCommentsResponse: ...
    def playlist(self, **params: Unpack[YoutubePlaylistParams]) -> YoutubePlaylistResponse: ...
    def profile(self, **params: Unpack[YoutubeProfileParams]) -> YoutubeProfileResponse: ...
    def search(self, **params: Unpack[YoutubeSearchParams]) -> YoutubeSearchResponse: ...
    def tag(self, **params: Unpack[YoutubeTagParams]) -> YoutubeTagResponse: ...
    def transcript(self, **params: Unpack[YoutubeTranscriptParams]) -> YoutubeTranscriptResponse: ...
    def transcript_languages(self, **params: Unpack[YoutubeTranscriptLanguagesParams]) -> YoutubeTranscriptLanguagesResponse: ...
    def video(self, **params: Unpack[YoutubeVideoParams]) -> YoutubeVideoResponse: ...

class ZillowGroup:
    def autocomplete(self, **params: Unpack[ZillowAutocompleteParams]) -> ZillowAutocompleteResponse: ...
    def property(self, **params: Unpack[ZillowPropertyParams]) -> ZillowPropertyResponse: ...
    def search(self, **params: Unpack[ZillowSearchParams]) -> ZillowSearchResponse: ...

class CrawloraClient:
    airbnb: AirbnbGroup
    amazon: AmazonGroup
    apple_podcasts: ApplePodcastsGroup
    app_store: AppStoreGroup
    billing: BillingGroup
    bing: BingGroup
    brave: BraveGroup
    coin_gecko: CoinGeckoGroup
    datasets: DatasetsGroup
    e_bay: EBayGroup
    geocoding: GeocodingGroup
    google: GoogleGroup
    google_play: GooglePlayGroup
    instagram: InstagramGroup
    just_watch: JustWatchGroup
    linked_in: LinkedInGroup
    meta: MetaGroup
    product_hunt: ProductHuntGroup
    referrals: ReferralsGroup
    similar_web: SimilarWebGroup
    spotify_podcasts: SpotifyPodcastsGroup
    spotify: SpotifyGroup
    tiktok: TiktokGroup
    trip_advisor: TripAdvisorGroup
    trustpilot: TrustpilotGroup
    usage: UsageGroup
    user: UserGroup
    yahoo_finance: YahooFinanceGroup
    youtube: YoutubeGroup
    zillow: ZillowGroup
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Any: ...
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Any: ...

VERSION: str

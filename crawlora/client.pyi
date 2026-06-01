from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAirbnbCalendarMonth = TypedDict('ModelAirbnbCalendarMonth', {
    'month': NotRequired[str],
    'year': NotRequired[int],
}, total=False)

ModelAirbnbCalendarResponse = TypedDict('ModelAirbnbCalendarResponse', {
    'id': NotRequired[str],
    'months': NotRequired[list[ModelAirbnbCalendarMonth]],
}, total=False)

ModelAirbnbListingItem = TypedDict('ModelAirbnbListingItem', {
    'host': NotRequired[str],
    'id': NotRequired[str],
    'image': NotRequired[str],
    'latitude': NotRequired[float],
    'location': NotRequired[str],
    'longitude': NotRequired[float],
    'price': NotRequired[float],
    'rating': NotRequired[float],
    'review_count': NotRequired[int],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelAirbnbReviewItem = TypedDict('ModelAirbnbReviewItem', {
    'author': NotRequired[str],
    'date': NotRequired[str],
    'rating': NotRequired[float],
    'text': NotRequired[str],
}, total=False)

ModelAirbnbReviewsResponse = TypedDict('ModelAirbnbReviewsResponse', {
    'id': NotRequired[str],
    'page': NotRequired[int],
    'reviews': NotRequired[list[ModelAirbnbReviewItem]],
}, total=False)

ModelAirbnbRoomResponse = TypedDict('ModelAirbnbRoomResponse', {
    'amenities': NotRequired[list[str]],
    'description': NotRequired[str],
    'host': NotRequired[str],
    'id': NotRequired[str],
    'image': NotRequired[str],
    'latitude': NotRequired[float],
    'location': NotRequired[str],
    'longitude': NotRequired[float],
    'price': NotRequired[float],
    'rating': NotRequired[float],
    'review_count': NotRequired[int],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelAirbnbSearchResponse = TypedDict('ModelAirbnbSearchResponse', {
    'location': NotRequired[str],
    'page': NotRequired[int],
    'results': NotRequired[list[ModelAirbnbListingItem]],
}, total=False)

ModelAmazonProduct = TypedDict('ModelAmazonProduct', {
    'about': NotRequired[str],
    'asin': NotRequired[str],
    'availability': NotRequired[bool],
    'brand_link': NotRequired[str],
    'brand_name': NotRequired[str],
    'customers_say': NotRequired[str],
    'description': NotRequired[str],
    'images': NotRequired[list[str]],
    'is_free_delivery': NotRequired[bool],
    'is_free_return': NotRequired[bool],
    'link': NotRequired[str],
    'number_of_bought_in_last_month': NotRequired[int],
    'overview': NotRequired[dict[str, str]],
    'price': NotRequired[float],
    'rating': NotRequired[float],
    'rating_hist': NotRequired[dict[str, float]],
    'review_count': NotRequired[int],
    'review_images': NotRequired[list[ModelAmazonReviewImage]],
    'review_insights': NotRequired[list[ModelAmazonReviewInsight]],
    'reviews': NotRequired[list[ModelAmazonReview]],
    'seller_link': NotRequired[str],
    'seller_name': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelAmazonReview = TypedDict('ModelAmazonReview', {
    'content': NotRequired[str],
    'country': NotRequired[str],
    'helpful_count': NotRequired[int],
    'link': NotRequired[str],
    'rating': NotRequired[float],
    'review_date': NotRequired[str],
    'title': NotRequired[str],
    'user_link': NotRequired[str],
    'user_name': NotRequired[str],
    'verified_purchase': NotRequired[bool],
}, total=False)

ModelAmazonReviewImage = TypedDict('ModelAmazonReviewImage', {
    'review_id': NotRequired[str],
    'thumbnail': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelAmazonReviewInsight = TypedDict('ModelAmazonReviewInsight', {
    'label': NotRequired[str],
    'mention_percent': NotRequired[int],
    'mentions': NotRequired[int],
    'sentiment': NotRequired[str],
    'summary': NotRequired[str],
}, total=False)

ModelAmazonSearchResponseItem = TypedDict('ModelAmazonSearchResponseItem', {
    'asin': NotRequired[str],
    'image': NotRequired[str],
    'is_free_delivery': NotRequired[bool],
    'is_sponsored': NotRequired[bool],
    'link': NotRequired[str],
    'list_price': NotRequired[float],
    'more_choice': NotRequired[str],
    'number_of_bought_in_last_month': NotRequired[int],
    'price': NotRequired[float],
    'rating': NotRequired[float],
    'review_count': NotRequired[int],
    'title': NotRequired[str],
}, total=False)

ModelAmazonProductResponseDoc = TypedDict('ModelAmazonProductResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelAmazonProduct],
    'msg': NotRequired[str],
}, total=False)

ModelAmazonSearchResponseDoc = TypedDict('ModelAmazonSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelAmazonSearchResponseItem]],
    'msg': NotRequired[str],
}, total=False)

ModelAmazonSuggestResponseDoc = TypedDict('ModelAmazonSuggestResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[str]],
    'msg': NotRequired[str],
}, total=False)

ModelApiComponentStatus = TypedDict('ModelApiComponentStatus', {
    'error': NotRequired[str],
    'ready': NotRequired[bool],
}, total=False)

ModelApiPingResponseDoc = TypedDict('ModelApiPingResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBuildinfoInfo],
    'msg': NotRequired[str],
}, total=False)

ModelApiReadinessResponseDoc = TypedDict('ModelApiReadinessResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelApiReadinessState],
    'msg': NotRequired[str],
}, total=False)

ModelApiReadinessState = TypedDict('ModelApiReadinessState', {
    'checked_at': NotRequired[str],
    'components': NotRequired[dict[str, ModelApiComponentStatus]],
    'ready': NotRequired[bool],
}, total=False)

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelApplepodcastsGenre = TypedDict('ModelApplepodcastsGenre', {
    'id': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelApplepodcastsPodcastChartItem = TypedDict('ModelApplepodcastsPodcastChartItem', {
    'artist_name': NotRequired[str],
    'artist_url': NotRequired[str],
    'artwork_url': NotRequired[str],
    'currency': NotRequired[str],
    'description': NotRequired[str],
    'free': NotRequired[bool],
    'genre': NotRequired[str],
    'genre_id': NotRequired[int],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'price': NotRequired[float],
    'release_date': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelApplepodcastsPodcastEpisode = TypedDict('ModelApplepodcastsPodcastEpisode', {
    'artwork_url_160': NotRequired[str],
    'artwork_url_60': NotRequired[str],
    'artwork_url_600': NotRequired[str],
    'closed_captioning': NotRequired[str],
    'content_advisory_rating': NotRequired[str],
    'country': NotRequired[str],
    'description': NotRequired[str],
    'duration_millis': NotRequired[int],
    'episode_content_type': NotRequired[str],
    'episode_file_extension': NotRequired[str],
    'episode_guid': NotRequired[str],
    'episode_url': NotRequired[str],
    'feed_url': NotRequired[str],
    'genres': NotRequired[list[ModelApplepodcastsGenre]],
    'id': NotRequired[int],
    'preview_url': NotRequired[str],
    'release_date': NotRequired[str],
    'short_description': NotRequired[str],
    'show_id': NotRequired[int],
    'show_name': NotRequired[str],
    'show_url': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelApplepodcastsPodcastShow = TypedDict('ModelApplepodcastsPodcastShow', {
    'artist_id': NotRequired[int],
    'artist_name': NotRequired[str],
    'artist_url': NotRequired[str],
    'artwork_url_100': NotRequired[str],
    'artwork_url_30': NotRequired[str],
    'artwork_url_60': NotRequired[str],
    'artwork_url_600': NotRequired[str],
    'collection_explicitness': NotRequired[str],
    'collection_name': NotRequired[str],
    'content_advisory_rating': NotRequired[str],
    'country': NotRequired[str],
    'currency': NotRequired[str],
    'feed_url': NotRequired[str],
    'genre_ids': NotRequired[list[str]],
    'genres': NotRequired[list[str]],
    'id': NotRequired[int],
    'primary_genre_name': NotRequired[str],
    'release_date': NotRequired[str],
    'track_count': NotRequired[int],
    'track_explicitness': NotRequired[str],
    'track_name': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelApplepodcastsShowEpisodesResult = TypedDict('ModelApplepodcastsShowEpisodesResult', {
    'episodes': NotRequired[list[ModelApplepodcastsPodcastEpisode]],
    'show': NotRequired[ModelApplepodcastsPodcastShow],
}, total=False)

ModelApplepodcastsChartsResponseDoc = TypedDict('ModelApplepodcastsChartsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelApplepodcastsPodcastChartItem]],
    'msg': NotRequired[str],
}, total=False)

ModelApplepodcastsEpisodeSearchResponseDoc = TypedDict('ModelApplepodcastsEpisodeSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelApplepodcastsPodcastEpisode]],
    'msg': NotRequired[str],
}, total=False)

ModelApplepodcastsSearchResponseDoc = TypedDict('ModelApplepodcastsSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelApplepodcastsPodcastShow]],
    'msg': NotRequired[str],
}, total=False)

ModelApplepodcastsShowEpisodesResponseDoc = TypedDict('ModelApplepodcastsShowEpisodesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelApplepodcastsShowEpisodesResult],
    'msg': NotRequired[str],
}, total=False)

ModelApplepodcastsShowResponseDoc = TypedDict('ModelApplepodcastsShowResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelApplepodcastsPodcastShow],
    'msg': NotRequired[str],
}, total=False)

ModelAppstoreApp = TypedDict('ModelAppstoreApp', {
    'app_id': NotRequired[str],
    'appletv_screenshots': NotRequired[list[str]],
    'content_rating': NotRequired[str],
    'currency': NotRequired[str],
    'current_version_reviews': NotRequired[int],
    'current_version_score': NotRequired[float],
    'description': NotRequired[str],
    'developer': NotRequired[str],
    'developer_id': NotRequired[int],
    'developer_url': NotRequired[str],
    'developer_website': NotRequired[str],
    'free': NotRequired[bool],
    'genre_ids': NotRequired[list[str]],
    'genres': NotRequired[list[str]],
    'histogram': NotRequired[dict[str, int]],
    'icon': NotRequired[str],
    'id': NotRequired[int],
    'ipad_screenshots': NotRequired[list[str]],
    'languages': NotRequired[list[str]],
    'price': NotRequired[float],
    'primary_genre': NotRequired[str],
    'primary_genre_id': NotRequired[int],
    'ratings': NotRequired[int],
    'release_notes': NotRequired[str],
    'released': NotRequired[str],
    'required_os_version': NotRequired[str],
    'reviews': NotRequired[int],
    'score': NotRequired[float],
    'screenshots': NotRequired[list[str]],
    'size': NotRequired[str],
    'supported_devices': NotRequired[list[str]],
    'title': NotRequired[str],
    'updated': NotRequired[str],
    'url': NotRequired[str],
    'version': NotRequired[str],
}, total=False)

ModelAppstorePrivacyCategory = TypedDict('ModelAppstorePrivacyCategory', {
    'data_category': NotRequired[str],
    'data_types': NotRequired[list[str]],
    'identifier': NotRequired[str],
}, total=False)

ModelAppstorePrivacyDetails = TypedDict('ModelAppstorePrivacyDetails', {
    'manage_privacy_choices_url': NotRequired[str],
    'privacy_policy_url': NotRequired[str],
    'privacy_types': NotRequired[list[ModelAppstorePrivacyType]],
}, total=False)

ModelAppstorePrivacyPurpose = TypedDict('ModelAppstorePrivacyPurpose', {
    'data_categories': NotRequired[list[ModelAppstorePrivacyCategory]],
    'identifier': NotRequired[str],
    'purpose': NotRequired[str],
}, total=False)

ModelAppstorePrivacyType = TypedDict('ModelAppstorePrivacyType', {
    'data_categories': NotRequired[list[ModelAppstorePrivacyCategory]],
    'description': NotRequired[str],
    'identifier': NotRequired[str],
    'privacy_type': NotRequired[str],
    'purposes': NotRequired[list[ModelAppstorePrivacyPurpose]],
}, total=False)

ModelAppstoreRatingsResult = TypedDict('ModelAppstoreRatingsResult', {
    'histogram': NotRequired[dict[str, int]],
    'ratings': NotRequired[int],
}, total=False)

ModelAppstoreReview = TypedDict('ModelAppstoreReview', {
    'id': NotRequired[str],
    'score': NotRequired[int],
    'text': NotRequired[str],
    'title': NotRequired[str],
    'updated': NotRequired[str],
    'url': NotRequired[str],
    'user_name': NotRequired[str],
    'user_url': NotRequired[str],
    'version': NotRequired[str],
}, total=False)

ModelAppstoreSuggestion = TypedDict('ModelAppstoreSuggestion', {
    'term': NotRequired[str],
}, total=False)

ModelAppstoreVersionHistoryItem = TypedDict('ModelAppstoreVersionHistoryItem', {
    'release_date': NotRequired[str],
    'release_notes': NotRequired[str],
    'release_timestamp': NotRequired[str],
    'version_display': NotRequired[str],
}, total=False)

ModelAppstoreAppDetailsResponseDoc = TypedDict('ModelAppstoreAppDetailsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelAppstoreApp],
    'msg': NotRequired[str],
}, total=False)

ModelAppstoreDeveloperResponseDoc = TypedDict('ModelAppstoreDeveloperResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelAppstoreApp]],
    'msg': NotRequired[str],
}, total=False)

ModelAppstoreListResultsResponseDoc = TypedDict('ModelAppstoreListResultsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[Any]],
    'msg': NotRequired[str],
}, total=False)

ModelAppstorePrivacyResponseDoc = TypedDict('ModelAppstorePrivacyResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelAppstorePrivacyDetails],
    'msg': NotRequired[str],
}, total=False)

ModelAppstoreRatingsResponseDoc = TypedDict('ModelAppstoreRatingsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelAppstoreRatingsResult],
    'msg': NotRequired[str],
}, total=False)

ModelAppstoreReviewsResponseDoc = TypedDict('ModelAppstoreReviewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelAppstoreReview]],
    'msg': NotRequired[str],
}, total=False)

ModelAppstoreSearchResultsResponseDoc = TypedDict('ModelAppstoreSearchResultsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[Any]],
    'msg': NotRequired[str],
}, total=False)

ModelAppstoreSimilarResponseDoc = TypedDict('ModelAppstoreSimilarResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelAppstoreApp]],
    'msg': NotRequired[str],
}, total=False)

ModelAppstoreSuggestResponseDoc = TypedDict('ModelAppstoreSuggestResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelAppstoreSuggestion]],
    'msg': NotRequired[str],
}, total=False)

ModelAppstoreVersionHistoryResponseDoc = TypedDict('ModelAppstoreVersionHistoryResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelAppstoreVersionHistoryItem]],
    'msg': NotRequired[str],
}, total=False)

ModelBillingBillingEndpointLedgerDoc = TypedDict('ModelBillingBillingEndpointLedgerDoc', {
    'charged_requests': NotRequired[int],
    'credits': NotRequired[int],
    'endpoint': NotRequired[str],
    'failed_requests': NotRequired[int],
    'non_billable_requests': NotRequired[int],
    'overage': NotRequired[int],
    'requests': NotRequired[int],
}, total=False)

ModelBillingBillingEventDoc = TypedDict('ModelBillingBillingEventDoc', {
    'billable': NotRequired[bool],
    'charged_at': NotRequired[str],
    'created_at': NotRequired[str],
    'credit_cost': NotRequired[int],
    'credits_remaining_after': NotRequired[int],
    'credits_remaining_before': NotRequired[int],
    'credits_used_after': NotRequired[int],
    'credits_used_before': NotRequired[int],
    'daily_key': NotRequired[str],
    'endpoint': NotRequired[str],
    'event_status': NotRequired[str],
    'failure_reason': NotRequired[str],
    'finalized_at': NotRequired[str],
    'idempotency_key': NotRequired[str],
    'method': NotRequired[str],
    'non_billable_reason': NotRequired[str],
    'overage_credits_delta': NotRequired[int],
    'period_key': NotRequired[str],
    'plan': NotRequired[str],
    'principal_type': NotRequired[str],
    'request_id': NotRequired[str],
    'route_pattern': NotRequired[str],
    'status_code': NotRequired[int],
    'user_id': NotRequired[str],
}, total=False)

ModelBillingBillingEventsResponseDoc = TypedDict('ModelBillingBillingEventsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelBillingBillingEventDoc]],
    'msg': NotRequired[str],
}, total=False)

ModelBillingBillingPeriodLedgerDoc = TypedDict('ModelBillingBillingPeriodLedgerDoc', {
    'charged_requests': NotRequired[int],
    'closed_at': NotRequired[str],
    'credits_used': NotRequired[int],
    'currency': NotRequired[str],
    'endpoint_breakdown': NotRequired[list[ModelBillingBillingEndpointLedgerDoc]],
    'expected_subscription_amount_cents': NotRequired[int],
    'expected_total_amount_cents': NotRequired[int],
    'failed_requests': NotRequired[int],
    'generated_at': NotRequired[str],
    'included_credits': NotRequired[int],
    'mismatch_flags': NotRequired[list[str]],
    'mismatch_total_cents': NotRequired[int],
    'non_billable_requests': NotRequired[int],
    'overage_amount_cents': NotRequired[int],
    'overage_credits': NotRequired[int],
    'overage_price_per_1000': NotRequired[float],
    'period_end': NotRequired[str],
    'period_key': NotRequired[str],
    'period_start': NotRequired[str],
    'plan': NotRequired[str],
    'pricing_source': NotRequired[str],
    'status': NotRequired[str],
    'stripe_actual_amount_due_cents': NotRequired[int],
    'stripe_actual_amount_paid_cents': NotRequired[int],
    'stripe_actual_amount_remaining_cents': NotRequired[int],
    'stripe_actual_credit_note_cents': NotRequired[int],
    'stripe_actual_discount_cents': NotRequired[int],
    'stripe_actual_net_cash_cents': NotRequired[int],
    'stripe_actual_one_time_cents': NotRequired[int],
    'stripe_actual_overage_cents': NotRequired[int],
    'stripe_actual_proration_cents': NotRequired[int],
    'stripe_actual_refund_cents': NotRequired[int],
    'stripe_actual_subscription_cents': NotRequired[int],
    'stripe_actual_tax_cents': NotRequired[int],
    'stripe_actual_total_cents': NotRequired[int],
    'stripe_customer_id': NotRequired[str],
    'stripe_invoice_amount_due': NotRequired[int],
    'stripe_invoice_amount_paid': NotRequired[int],
    'stripe_invoice_amount_remaining': NotRequired[int],
    'stripe_invoice_currency': NotRequired[str],
    'stripe_invoice_due_date': NotRequired[str],
    'stripe_invoice_effective_due_date': NotRequired[str],
    'stripe_invoice_finalized_at': NotRequired[str],
    'stripe_invoice_hosted_url': NotRequired[str],
    'stripe_invoice_id': NotRequired[str],
    'stripe_invoice_last_event_created': NotRequired[str],
    'stripe_invoice_last_event_id': NotRequired[str],
    'stripe_invoice_number': NotRequired[str],
    'stripe_invoice_paid_at': NotRequired[str],
    'stripe_invoice_payment_failed_at': NotRequired[str],
    'stripe_invoice_pdf': NotRequired[str],
    'stripe_invoice_period_end': NotRequired[str],
    'stripe_invoice_period_start': NotRequired[str],
    'stripe_invoice_reconciliation_error': NotRequired[str],
    'stripe_invoice_reconciliation_status': NotRequired[str],
    'stripe_invoice_status': NotRequired[str],
    'stripe_meter_event_identifier': NotRequired[str],
    'stripe_meter_event_name': NotRequired[str],
    'stripe_snapshot_updated_at': NotRequired[str],
    'stripe_sync_attempts': NotRequired[int],
    'stripe_sync_error': NotRequired[str],
    'stripe_sync_first_attempt_at': NotRequired[str],
    'stripe_sync_last_attempt_at': NotRequired[str],
    'stripe_sync_status': NotRequired[str],
    'stripe_synced_at': NotRequired[str],
    'subscription_price_cents': NotRequired[int],
    'updated_at': NotRequired[str],
    'user_id': NotRequired[str],
}, total=False)

ModelBillingBillingPeriodLedgerResponseDoc = TypedDict('ModelBillingBillingPeriodLedgerResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBillingBillingPeriodLedgerDoc],
    'msg': NotRequired[str],
}, total=False)

ModelBillingBillingPeriodLedgersResponseDoc = TypedDict('ModelBillingBillingPeriodLedgersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelBillingBillingPeriodLedgerDoc]],
    'msg': NotRequired[str],
}, total=False)

ModelBillingBillingPeriodStatementDoc = TypedDict('ModelBillingBillingPeriodStatementDoc', {
    'accounts_receivable': NotRequired[ModelBillingBillingStatementAccountsReceivableDoc],
    'adjustment_events': NotRequired[list[ModelBillingBillingStatementAdjustmentEvidenceDoc]],
    'endpoint_breakdown': NotRequired[list[ModelBillingBillingEndpointLedgerDoc]],
    'events': NotRequired[list[ModelBillingBillingStatementEventItemDoc]],
    'expected': NotRequired[ModelBillingBillingStatementExpectedRevenueDoc],
    'generated_at': NotRequired[str],
    'invoice': NotRequired[ModelBillingBillingStatementInvoiceEvidenceDoc],
    'invoice_events': NotRequired[list[ModelBillingBillingStatementInvoiceEventEvidenceDoc]],
    'mismatch': NotRequired[ModelBillingBillingStatementMismatchDoc],
    'period': NotRequired[ModelBillingBillingStatementPeriodDoc],
    'plan': NotRequired[str],
    'repair': NotRequired[ModelBillingBillingStatementRepairDoc],
    'snapshot': NotRequired[ModelBillingBillingStatementSnapshotMetadataDoc],
    'stripe_actual': NotRequired[ModelBillingBillingStatementStripeActualDoc],
    'user': NotRequired[ModelBillingBillingStatementUserDoc],
}, total=False)

ModelBillingBillingPeriodStatementResponseDoc = TypedDict('ModelBillingBillingPeriodStatementResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBillingBillingPeriodStatementDoc],
    'msg': NotRequired[str],
}, total=False)

ModelBillingBillingStateDoc = TypedDict('ModelBillingBillingStateDoc', {
    'allow_overage': NotRequired[bool],
    'created_at': NotRequired[str],
    'credits_remaining': NotRequired[int],
    'credits_used': NotRequired[int],
    'currency': NotRequired[str],
    'daily_credit_limit': NotRequired[int],
    'daily_credits_remaining': NotRequired[int],
    'daily_credits_used': NotRequired[int],
    'daily_key': NotRequired[str],
    'expected_subscription_amount_cents': NotRequired[int],
    'expected_total_amount_cents': NotRequired[int],
    'hard_limit': NotRequired[bool],
    'included_credits': NotRequired[int],
    'overage_credits': NotRequired[int],
    'period_end': NotRequired[str],
    'period_key': NotRequired[str],
    'period_start': NotRequired[str],
    'plan': NotRequired[str],
    'pricing_source': NotRequired[str],
    'subscription_price_cents': NotRequired[int],
    'updated_at': NotRequired[str],
    'user_id': NotRequired[str],
}, total=False)

ModelBillingBillingStateResponseDoc = TypedDict('ModelBillingBillingStateResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBillingBillingStateDoc],
    'msg': NotRequired[str],
}, total=False)

ModelBillingBillingStatementAccountsReceivableDoc = TypedDict('ModelBillingBillingStatementAccountsReceivableDoc', {
    'amount_due_cents': NotRequired[int],
    'amount_paid_cents': NotRequired[int],
    'amount_remaining_cents': NotRequired[int],
    'due_date': NotRequired[str],
    'effective_due_date': NotRequired[str],
    'finalized_at': NotRequired[str],
    'invoice_status': NotRequired[str],
    'paid_at': NotRequired[str],
    'payment_failed_at': NotRequired[str],
}, total=False)

ModelBillingBillingStatementAdjustmentEvidenceDoc = TypedDict('ModelBillingBillingStatementAdjustmentEvidenceDoc', {
    'amount_cents': NotRequired[int],
    'currency': NotRequired[str],
    'error': NotRequired[str],
    'event_created': NotRequired[str],
    'event_id': NotRequired[str],
    'event_type': NotRequired[str],
    'kind': NotRequired[str],
    'match_status': NotRequired[str],
    'processed_at': NotRequired[str],
    'reconciliation_status': NotRequired[str],
    'repair_attempts': NotRequired[int],
    'repair_last_error': NotRequired[str],
    'repair_status': NotRequired[str],
    'resource_id': NotRequired[str],
    'resource_status': NotRequired[str],
    'stripe_invoice_id': NotRequired[str],
}, total=False)

ModelBillingBillingStatementEventItemDoc = TypedDict('ModelBillingBillingStatementEventItemDoc', {
    'billable': NotRequired[bool],
    'created_at': NotRequired[str],
    'credit_cost': NotRequired[int],
    'endpoint': NotRequired[str],
    'event_status': NotRequired[str],
    'non_billable_reason': NotRequired[str],
    'request_id': NotRequired[str],
    'status_code': NotRequired[int],
}, total=False)

ModelBillingBillingStatementExpectedRevenueDoc = TypedDict('ModelBillingBillingStatementExpectedRevenueDoc', {
    'credits_used': NotRequired[int],
    'currency': NotRequired[str],
    'expected_subscription_amount_cents': NotRequired[int],
    'expected_total_amount_cents': NotRequired[int],
    'included_credits': NotRequired[int],
    'overage_amount_cents': NotRequired[int],
    'overage_credits': NotRequired[int],
    'overage_price_per_1000': NotRequired[float],
    'pricing_source': NotRequired[str],
    'subscription_price_cents': NotRequired[int],
}, total=False)

ModelBillingBillingStatementInvoiceEventEvidenceDoc = TypedDict('ModelBillingBillingStatementInvoiceEventEvidenceDoc', {
    'error': NotRequired[str],
    'event_created': NotRequired[str],
    'event_id': NotRequired[str],
    'event_type': NotRequired[str],
    'match_status': NotRequired[str],
    'processed_at': NotRequired[str],
    'reconciliation_status': NotRequired[str],
    'repair_attempts': NotRequired[int],
    'repair_last_error': NotRequired[str],
    'repair_status': NotRequired[str],
    'stripe_invoice_id': NotRequired[str],
    'stripe_invoice_status': NotRequired[str],
}, total=False)

ModelBillingBillingStatementInvoiceEvidenceDoc = TypedDict('ModelBillingBillingStatementInvoiceEvidenceDoc', {
    'amount_due_cents': NotRequired[int],
    'amount_paid_cents': NotRequired[int],
    'amount_remaining_cents': NotRequired[int],
    'currency': NotRequired[str],
    'due_date': NotRequired[str],
    'effective_due_date': NotRequired[str],
    'finalized_at': NotRequired[str],
    'hosted_invoice_url': NotRequired[str],
    'invoice_pdf': NotRequired[str],
    'line_items': NotRequired[list[ModelBillingStripeInvoiceLineItemDoc]],
    'mismatch_flags': NotRequired[list[str]],
    'mismatch_total_cents': NotRequired[int],
    'paid_at': NotRequired[str],
    'period_end': NotRequired[str],
    'period_start': NotRequired[str],
    'reconciliation_status': NotRequired[str],
    'repair_attempts': NotRequired[int],
    'repair_error': NotRequired[str],
    'repair_status': NotRequired[str],
    'stripe_invoice_id': NotRequired[str],
    'stripe_invoice_number': NotRequired[str],
    'stripe_invoice_status': NotRequired[str],
}, total=False)

ModelBillingBillingStatementMismatchDoc = TypedDict('ModelBillingBillingStatementMismatchDoc', {
    'mismatch_flags': NotRequired[list[str]],
    'mismatch_total_cents': NotRequired[int],
}, total=False)

ModelBillingBillingStatementPeriodDoc = TypedDict('ModelBillingBillingStatementPeriodDoc', {
    'closed_at': NotRequired[str],
    'period_end': NotRequired[str],
    'period_key': NotRequired[str],
    'period_start': NotRequired[str],
    'status': NotRequired[str],
}, total=False)

ModelBillingBillingStatementRepairDoc = TypedDict('ModelBillingBillingStatementRepairDoc', {
    'repair_attempts': NotRequired[int],
    'repair_last_attempt_at': NotRequired[str],
    'repair_last_error': NotRequired[str],
    'repair_status': NotRequired[str],
    'stripe_sync_attempts': NotRequired[int],
    'stripe_sync_error': NotRequired[str],
    'stripe_sync_status': NotRequired[str],
    'stripe_synced_at': NotRequired[str],
}, total=False)

ModelBillingBillingStatementSnapshotMetadataDoc = TypedDict('ModelBillingBillingStatementSnapshotMetadataDoc', {
    'canonical_json_sha256': NotRequired[str],
    'frozen_at': NotRequired[str],
    'generated_at': NotRequired[str],
    'revision': NotRequired[int],
    'snapshot_status': NotRequired[str],
    'source_ledger_updated_at': NotRequired[str],
    'source_snapshot_updated_at': NotRequired[str],
    'statement_id': NotRequired[str],
    'statement_version': NotRequired[str],
}, total=False)

ModelBillingBillingStatementStripeActualDoc = TypedDict('ModelBillingBillingStatementStripeActualDoc', {
    'amount_due_cents': NotRequired[int],
    'amount_paid_cents': NotRequired[int],
    'amount_remaining_cents': NotRequired[int],
    'credit_note_cents': NotRequired[int],
    'currency': NotRequired[str],
    'discount_cents': NotRequired[int],
    'net_cash_cents': NotRequired[int],
    'one_time_cents': NotRequired[int],
    'overage_cents': NotRequired[int],
    'proration_cents': NotRequired[int],
    'refund_cents': NotRequired[int],
    'snapshot_updated_at': NotRequired[str],
    'subscription_cents': NotRequired[int],
    'tax_cents': NotRequired[int],
    'total_cents': NotRequired[int],
}, total=False)

ModelBillingBillingStatementUserDoc = TypedDict('ModelBillingBillingStatementUserDoc', {
    'email': NotRequired[str],
    'plan': NotRequired[str],
    'stripe_customer_id': NotRequired[str],
    'user_id': NotRequired[str],
    'username': NotRequired[str],
}, total=False)

ModelBillingStripeCheckoutRequestDoc = TypedDict('ModelBillingStripeCheckoutRequestDoc', {
    'cancel_url': NotRequired[str],
    'plan': NotRequired[str],
    'success_url': NotRequired[str],
}, total=False)

ModelBillingStripeInvoiceLineItemDoc = TypedDict('ModelBillingStripeInvoiceLineItemDoc', {
    'amount_cents': NotRequired[int],
    'category': NotRequired[str],
    'currency': NotRequired[str],
    'description': NotRequired[str],
    'line_id': NotRequired[str],
    'period_end': NotRequired[str],
    'period_start': NotRequired[str],
    'proration': NotRequired[bool],
    'source_ref': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelBillingStripePortalRequestDoc = TypedDict('ModelBillingStripePortalRequestDoc', {
    'return_url': NotRequired[str],
}, total=False)

ModelBillingStripeSessionDoc = TypedDict('ModelBillingStripeSessionDoc', {
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBillingStripeSessionResponseDoc = TypedDict('ModelBillingStripeSessionResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBillingStripeSessionDoc],
    'msg': NotRequired[str],
}, total=False)

ModelBingContextAttribute = TypedDict('ModelBingContextAttribute', {
    'label': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelBingImageResult = TypedDict('ModelBingImageResult', {
    'height': NotRequired[int],
    'image_url': NotRequired[str],
    'position': NotRequired[int],
    'source': NotRequired[str],
    'source_url': NotRequired[str],
    'thumbnail': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'width': NotRequired[int],
}, total=False)

ModelBingImagesResponse = TypedDict('ModelBingImagesResponse', {
    'pagination': NotRequired[ModelBingSearchPagination],
    'results': NotRequired[list[ModelBingImageResult]],
}, total=False)

ModelBingNewsResponse = TypedDict('ModelBingNewsResponse', {
    'pagination': NotRequired[ModelBingSearchPagination],
    'results': NotRequired[list[ModelBingNewsResult]],
}, total=False)

ModelBingNewsResult = TypedDict('ModelBingNewsResult', {
    'age': NotRequired[str],
    'age_timestamp': NotRequired[int],
    'description': NotRequired[str],
    'position': NotRequired[int],
    'related_count': NotRequired[int],
    'source': NotRequired[str],
    'thumbnail': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBingSearchContext = TypedDict('ModelBingSearchContext', {
    'attributes': NotRequired[list[ModelBingContextAttribute]],
    'description': NotRequired[str],
    'image': NotRequired[str],
    'subtitle': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBingSearchPagination = TypedDict('ModelBingSearchPagination', {
    'count': NotRequired[int],
    'next_page': NotRequired[int],
    'page': NotRequired[int],
    'previous_page': NotRequired[int],
}, total=False)

ModelBingSearchResponse = TypedDict('ModelBingSearchResponse', {
    'context': NotRequired[ModelBingSearchContext],
    'news': NotRequired[list[ModelBingNewsResult]],
    'pagination': NotRequired[ModelBingSearchPagination],
    'people_also_ask': NotRequired[list[str]],
    'related_queries': NotRequired[list[str]],
    'results': NotRequired[list[ModelBingSearchResult]],
    'videos': NotRequired[list[ModelBingVideoResult]],
}, total=False)

ModelBingSearchResult = TypedDict('ModelBingSearchResult', {
    'age': NotRequired[str],
    'age_timestamp': NotRequired[int],
    'description': NotRequired[str],
    'display_url': NotRequired[str],
    'favicon': NotRequired[str],
    'hostname': NotRequired[str],
    'position': NotRequired[int],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBingSuggestResponse = TypedDict('ModelBingSuggestResponse', {
    'query': NotRequired[str],
    'suggestions': NotRequired[list[ModelBingSuggestionResult]],
}, total=False)

ModelBingSuggestionResult = TypedDict('ModelBingSuggestionResult', {
    'position': NotRequired[int],
    'query': NotRequired[str],
}, total=False)

ModelBingVideoResult = TypedDict('ModelBingVideoResult', {
    'age': NotRequired[str],
    'age_timestamp': NotRequired[int],
    'creator': NotRequired[str],
    'duration': NotRequired[str],
    'platform': NotRequired[str],
    'position': NotRequired[int],
    'thumbnail': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'views': NotRequired[str],
}, total=False)

ModelBingVideosResponse = TypedDict('ModelBingVideosResponse', {
    'pagination': NotRequired[ModelBingSearchPagination],
    'results': NotRequired[list[ModelBingVideoResult]],
}, total=False)

ModelBingImagesResponseDoc = TypedDict('ModelBingImagesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBingImagesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBingNewsResponseDoc = TypedDict('ModelBingNewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBingNewsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBingSearchResponseDoc = TypedDict('ModelBingSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBingSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBingSuggestResponseDoc = TypedDict('ModelBingSuggestResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBingSuggestResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBingVideosResponseDoc = TypedDict('ModelBingVideosResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBingVideosResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBraveDiscussion = TypedDict('ModelBraveDiscussion', {
    'age': NotRequired[str],
    'comment_count': NotRequired[int],
    'description': NotRequired[str],
    'favicon': NotRequired[str],
    'forum': NotRequired[str],
    'hostname': NotRequired[str],
    'path': NotRequired[str],
    'position': NotRequired[int],
    'score': NotRequired[int],
    'title': NotRequired[str],
    'top_comment': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBraveImageResult = TypedDict('ModelBraveImageResult', {
    'age': NotRequired[str],
    'height': NotRequired[int],
    'image_url': NotRequired[str],
    'position': NotRequired[int],
    'source': NotRequired[str],
    'thumbnail': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'width': NotRequired[int],
}, total=False)

ModelBraveImagesResponse = TypedDict('ModelBraveImagesResponse', {
    'pagination': NotRequired[ModelBraveSearchPagination],
    'results': NotRequired[list[ModelBraveImageResult]],
}, total=False)

ModelBraveKnowledgeCard = TypedDict('ModelBraveKnowledgeCard', {
    'category': NotRequired[str],
    'description': NotRequired[str],
    'image': NotRequired[str],
    'long_description': NotRequired[str],
    'provider': NotRequired[ModelBraveKnowledgeCardProvider],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBraveKnowledgeCardProvider = TypedDict('ModelBraveKnowledgeCardProvider', {
    'icon': NotRequired[str],
    'name': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBraveNewsResponse = TypedDict('ModelBraveNewsResponse', {
    'pagination': NotRequired[ModelBraveSearchPagination],
    'results': NotRequired[list[ModelBraveNewsResult]],
}, total=False)

ModelBraveNewsResult = TypedDict('ModelBraveNewsResult', {
    'age': NotRequired[str],
    'description': NotRequired[str],
    'favicon': NotRequired[str],
    'hostname': NotRequired[str],
    'path': NotRequired[str],
    'position': NotRequired[int],
    'source': NotRequired[str],
    'thumbnail': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBraveSearchPagination = TypedDict('ModelBraveSearchPagination', {
    'next_offset': NotRequired[int],
    'offset': NotRequired[int],
    'previous_offset': NotRequired[int],
}, total=False)

ModelBraveSearchResponse = TypedDict('ModelBraveSearchResponse', {
    'discussions': NotRequired[list[ModelBraveDiscussion]],
    'knowledge_card': NotRequired[ModelBraveKnowledgeCard],
    'pagination': NotRequired[ModelBraveSearchPagination],
    'related_queries': NotRequired[list[str]],
    'results': NotRequired[list[ModelBraveSearchResult]],
    'videos': NotRequired[list[ModelBraveVideoResult]],
}, total=False)

ModelBraveSearchResult = TypedDict('ModelBraveSearchResult', {
    'age': NotRequired[str],
    'description': NotRequired[str],
    'favicon': NotRequired[str],
    'hostname': NotRequired[str],
    'path': NotRequired[str],
    'position': NotRequired[int],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBraveSuggestResponse = TypedDict('ModelBraveSuggestResponse', {
    'query': NotRequired[str],
    'suggestions': NotRequired[list[ModelBraveSuggestionResult]],
}, total=False)

ModelBraveSuggestionResult = TypedDict('ModelBraveSuggestionResult', {
    'position': NotRequired[int],
    'query': NotRequired[str],
}, total=False)

ModelBraveVideoResult = TypedDict('ModelBraveVideoResult', {
    'age': NotRequired[str],
    'creator': NotRequired[str],
    'description': NotRequired[str],
    'duration': NotRequired[str],
    'favicon': NotRequired[str],
    'hostname': NotRequired[str],
    'path': NotRequired[str],
    'platform': NotRequired[str],
    'position': NotRequired[int],
    'thumbnail': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'views': NotRequired[str],
}, total=False)

ModelBraveVideosResponse = TypedDict('ModelBraveVideosResponse', {
    'pagination': NotRequired[ModelBraveSearchPagination],
    'results': NotRequired[list[ModelBraveVideoResult]],
}, total=False)

ModelBraveImagesResponseDoc = TypedDict('ModelBraveImagesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBraveImagesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBraveNewsResponseDoc = TypedDict('ModelBraveNewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBraveNewsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBraveSearchResponseDoc = TypedDict('ModelBraveSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBraveSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBraveSuggestResponseDoc = TypedDict('ModelBraveSuggestResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBraveSuggestResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBraveVideosResponseDoc = TypedDict('ModelBraveVideosResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBraveVideosResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBuildinfoInfo = TypedDict('ModelBuildinfoInfo', {
    'api': NotRequired[str],
    'build_time': NotRequired[str],
    'commit': NotRequired[str],
    'commit_short': NotRequired[str],
    'dirty': NotRequired[bool],
    'service': NotRequired[str],
    'status': NotRequired[str],
    'version': NotRequired[str],
}, total=False)

ModelCoingeckoAnalysisResponse = TypedDict('ModelCoingeckoAnalysisResponse', {
    'absolute_change': NotRequired[float],
    'annotations': NotRequired[list[dict[str, Any]]],
    'annotations_point_count': NotRequired[int],
    'annotations_source_url': NotRequired[str],
    'fetched_at': NotRequired[str],
    'first_price': NotRequired[float],
    'high_low_range_percent': NotRequired[float],
    'id': NotRequired[str],
    'last_price': NotRequired[float],
    'max_price': NotRequired[float],
    'min_price': NotRequired[float],
    'percent_change': NotRequired[float],
    'points': NotRequired[list[ModelCoingeckoChartPoint]],
    'points_count': NotRequired[int],
    'range': NotRequired[str],
    'source_url': NotRequired[str],
    'vs_currency': NotRequired[str],
}, total=False)

ModelCoingeckoCategoriesResponse = TypedDict('ModelCoingeckoCategoriesResponse', {
    'categories': NotRequired[list[ModelCoingeckoCategoryRow]],
    'fetched_at': NotRequired[str],
    'limit': NotRequired[int],
    'source_url': NotRequired[str],
    'vs_currency': NotRequired[str],
}, total=False)

ModelCoingeckoCategoryCoinRow = TypedDict('ModelCoingeckoCategoryCoinRow', {
    'change_1h_percent': NotRequired[float],
    'change_24h_percent': NotRequired[float],
    'change_30d_percent': NotRequired[float],
    'change_7d_percent': NotRequired[float],
    'fully_diluted_valuation': NotRequired[float],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'market_cap': NotRequired[float],
    'market_cap_fdv_ratio': NotRequired[float],
    'name': NotRequired[str],
    'price': NotRequired[float],
    'rank': NotRequired[int],
    'symbol': NotRequired[str],
    'url': NotRequired[str],
    'volume_24h': NotRequired[float],
}, total=False)

ModelCoingeckoCategoryCoinsResponse = TypedDict('ModelCoingeckoCategoryCoinsResponse', {
    'coins': NotRequired[list[ModelCoingeckoCategoryCoinRow]],
    'fetched_at': NotRequired[str],
    'limit': NotRequired[int],
    'name': NotRequired[str],
    'page': NotRequired[int],
    'slug': NotRequired[str],
    'source_url': NotRequired[str],
    'vs_currency': NotRequired[str],
}, total=False)

ModelCoingeckoCategoryRow = TypedDict('ModelCoingeckoCategoryRow', {
    'change_1h_percent': NotRequired[float],
    'change_24h_percent': NotRequired[float],
    'change_7d_percent': NotRequired[float],
    'coin_count': NotRequired[int],
    'id': NotRequired[str],
    'market_cap': NotRequired[float],
    'name': NotRequired[str],
    'rank': NotRequired[int],
    'slug': NotRequired[str],
    'url': NotRequired[str],
    'volume_24h': NotRequired[float],
}, total=False)

ModelCoingeckoChainDetailResponse = TypedDict('ModelCoingeckoChainDetailResponse', {
    'coins': NotRequired[list[ModelCoingeckoCategoryCoinRow]],
    'collections': NotRequired[list[ModelCoingeckoNftcollectionRow]],
    'exchanges': NotRequired[list[ModelCoingeckoChainExchangeRow]],
    'fetched_at': NotRequired[str],
    'id': NotRequired[str],
    'limit': NotRequired[int],
    'name': NotRequired[str],
    'source_url': NotRequired[str],
    'vs_currency': NotRequired[str],
}, total=False)

ModelCoingeckoChainExchangeRow = TypedDict('ModelCoingeckoChainExchangeRow', {
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'market_share_percent': NotRequired[float],
    'name': NotRequired[str],
    'rank': NotRequired[int],
    'url': NotRequired[str],
    'volume_24h': NotRequired[float],
    'volume_24h_text': NotRequired[str],
}, total=False)

ModelCoingeckoChainRow = TypedDict('ModelCoingeckoChainRow', {
    'change_24h_percent': NotRequired[float],
    'change_30d_percent': NotRequired[float],
    'change_7d_percent': NotRequired[float],
    'coin_count': NotRequired[int],
    'dominance_percent': NotRequired[float],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'name': NotRequired[str],
    'rank': NotRequired[int],
    'top_gainers': NotRequired[list[str]],
    'tvl': NotRequired[float],
    'url': NotRequired[str],
    'volume_24h': NotRequired[float],
}, total=False)

ModelCoingeckoChainsResponse = TypedDict('ModelCoingeckoChainsResponse', {
    'chains': NotRequired[list[ModelCoingeckoChainRow]],
    'fetched_at': NotRequired[str],
    'limit': NotRequired[int],
    'source_url': NotRequired[str],
    'vs_currency': NotRequired[str],
}, total=False)

ModelCoingeckoChartPoint = TypedDict('ModelCoingeckoChartPoint', {
    'datetime': NotRequired[str],
    'price': NotRequired[float],
    'timestamp': NotRequired[int],
}, total=False)

ModelCoingeckoCoinResponse = TypedDict('ModelCoingeckoCoinResponse', {
    'categories': NotRequired[list[str]],
    'change_1h_percent': NotRequired[float],
    'change_24h_percent': NotRequired[float],
    'change_7d_percent': NotRequired[float],
    'circulating_supply': NotRequired[float],
    'fetched_at': NotRequired[str],
    'fully_diluted_valuation': NotRequired[float],
    'id': NotRequired[str],
    'links': NotRequired[dict[str, str]],
    'market_cap': NotRequired[float],
    'max_supply': NotRequired[float],
    'name': NotRequired[str],
    'price': NotRequired[float],
    'rank': NotRequired[int],
    'source_url': NotRequired[str],
    'symbol': NotRequired[str],
    'total_supply': NotRequired[float],
    'volume_24h': NotRequired[float],
}, total=False)

ModelCoingeckoExchangeDetailResponse = TypedDict('ModelCoingeckoExchangeDetailResponse', {
    'fetched_at': NotRequired[str],
    'id': NotRequired[str],
    'kind': NotRequired[str],
    'limit': NotRequired[int],
    'markets': NotRequired[list[ModelCoingeckoExchangeMarketRow]],
    'name': NotRequired[str],
    'source_url': NotRequired[str],
    'trust_score': NotRequired[float],
    'volume_24h': NotRequired[float],
    'volume_24h_text': NotRequired[str],
    'vs_currency': NotRequired[str],
}, total=False)

ModelCoingeckoExchangeMarketRow = TypedDict('ModelCoingeckoExchangeMarketRow', {
    'coin_id': NotRequired[str],
    'coin_name': NotRequired[str],
    'coin_symbol': NotRequired[str],
    'coin_url': NotRequired[str],
    'depth_minus_2_percent': NotRequired[float],
    'depth_plus_2_percent': NotRequired[float],
    'last_updated': NotRequired[str],
    'pair': NotRequired[str],
    'price': NotRequired[float],
    'rank': NotRequired[int],
    'spread_percent': NotRequired[float],
    'volume_24h': NotRequired[float],
    'volume_percent': NotRequired[float],
}, total=False)

ModelCoingeckoExchangeRow = TypedDict('ModelCoingeckoExchangeRow', {
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'kind': NotRequired[str],
    'name': NotRequired[str],
    'rank': NotRequired[int],
    'trust_score': NotRequired[float],
    'url': NotRequired[str],
    'volume_24h': NotRequired[float],
    'volume_24h_text': NotRequired[str],
}, total=False)

ModelCoingeckoExchangesResponse = TypedDict('ModelCoingeckoExchangesResponse', {
    'exchanges': NotRequired[list[ModelCoingeckoExchangeRow]],
    'fetched_at': NotRequired[str],
    'kind': NotRequired[str],
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'source_url': NotRequired[str],
    'vs_currency': NotRequired[str],
}, total=False)

ModelCoingeckoGainerLoserRow = TypedDict('ModelCoingeckoGainerLoserRow', {
    'change_24h_percent': NotRequired[float],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'name': NotRequired[str],
    'price': NotRequired[float],
    'rank': NotRequired[int],
    'symbol': NotRequired[str],
    'url': NotRequired[str],
    'volume_24h': NotRequired[float],
}, total=False)

ModelCoingeckoGainersLosersResponse = TypedDict('ModelCoingeckoGainersLosersResponse', {
    'fetched_at': NotRequired[str],
    'gainers': NotRequired[list[ModelCoingeckoGainerLoserRow]],
    'limit': NotRequired[int],
    'losers': NotRequired[list[ModelCoingeckoGainerLoserRow]],
    'source_url': NotRequired[str],
    'vs_currency': NotRequired[str],
}, total=False)

ModelCoingeckoGlobalChartPoint = TypedDict('ModelCoingeckoGlobalChartPoint', {
    'datetime': NotRequired[str],
    'timestamp': NotRequired[int],
    'value': NotRequired[float],
}, total=False)

ModelCoingeckoGlobalChartSeries = TypedDict('ModelCoingeckoGlobalChartSeries', {
    'name': NotRequired[str],
    'points': NotRequired[list[ModelCoingeckoGlobalChartPoint]],
}, total=False)

ModelCoingeckoGlobalChartsResponse = TypedDict('ModelCoingeckoGlobalChartsResponse', {
    'fetched_at': NotRequired[str],
    'kind': NotRequired[str],
    'limit': NotRequired[int],
    'range': NotRequired[str],
    'series': NotRequired[list[ModelCoingeckoGlobalChartSeries]],
    'source_url': NotRequired[str],
}, total=False)

ModelCoingeckoGlobalResponse = TypedDict('ModelCoingeckoGlobalResponse', {
    'bitcoin_dominance_percent': NotRequired[float],
    'bitcoin_market_cap_usd': NotRequired[float],
    'categories_tracked': NotRequired[int],
    'coins_tracked': NotRequired[int],
    'ethereum_dominance_percent': NotRequired[float],
    'exchanges_tracked': NotRequired[int],
    'fetched_at': NotRequired[str],
    'market_cap_change_1y_percent': NotRequired[float],
    'market_cap_change_24h_percent': NotRequired[float],
    'market_cap_usd': NotRequired[float],
    'source_url': NotRequired[str],
    'stablecoin_market_cap_usd': NotRequired[float],
    'stablecoin_share_percent': NotRequired[float],
}, total=False)

ModelCoingeckoLearnArticle = TypedDict('ModelCoingeckoLearnArticle', {
    'author': NotRequired[str],
    'category': NotRequired[str],
    'excerpt': NotRequired[str],
    'image_url': NotRequired[str],
    'published_date': NotRequired[str],
    'rating_score': NotRequired[float],
    'rating_text': NotRequired[str],
    'rating_votes': NotRequired[int],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelCoingeckoLearnArticlesResponse = TypedDict('ModelCoingeckoLearnArticlesResponse', {
    'articles': NotRequired[list[ModelCoingeckoLearnArticle]],
    'category': NotRequired[str],
    'fetched_at': NotRequired[str],
    'limit': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelCoingeckoMarketCoin = TypedDict('ModelCoingeckoMarketCoin', {
    'change_1h_percent': NotRequired[float],
    'change_24h_percent': NotRequired[float],
    'change_7d_percent': NotRequired[float],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'market_cap': NotRequired[float],
    'name': NotRequired[str],
    'price': NotRequired[float],
    'rank': NotRequired[int],
    'symbol': NotRequired[str],
    'url': NotRequired[str],
    'volume_24h': NotRequired[float],
}, total=False)

ModelCoingeckoMarketsResponse = TypedDict('ModelCoingeckoMarketsResponse', {
    'coins': NotRequired[list[ModelCoingeckoMarketCoin]],
    'fetched_at': NotRequired[str],
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'source_url': NotRequired[str],
    'vs_currency': NotRequired[str],
}, total=False)

ModelCoingeckoNftcategoryResponse = TypedDict('ModelCoingeckoNftcategoryResponse', {
    'collections': NotRequired[list[ModelCoingeckoNftcollectionRow]],
    'fetched_at': NotRequired[str],
    'limit': NotRequired[int],
    'name': NotRequired[str],
    'page': NotRequired[int],
    'slug': NotRequired[str],
    'source_url': NotRequired[str],
    'vs_currency': NotRequired[str],
}, total=False)

ModelCoingeckoNftcollectionRow = TypedDict('ModelCoingeckoNftcollectionRow', {
    'chain': NotRequired[str],
    'change_24h_percent': NotRequired[float],
    'change_30d_percent': NotRequired[float],
    'change_7d_percent': NotRequired[float],
    'floor_price_native': NotRequired[float],
    'floor_price_usd': NotRequired[float],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'market_cap_native': NotRequired[float],
    'market_cap_usd': NotRequired[float],
    'name': NotRequired[str],
    'rank': NotRequired[int],
    'sales_24h': NotRequired[int],
    'url': NotRequired[str],
    'volume_24h_native': NotRequired[float],
    'volume_24h_usd': NotRequired[float],
}, total=False)

ModelCoingeckoNftsResponse = TypedDict('ModelCoingeckoNftsResponse', {
    'collections': NotRequired[list[ModelCoingeckoNftcollectionRow]],
    'fetched_at': NotRequired[str],
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'source_url': NotRequired[str],
    'vs_currency': NotRequired[str],
}, total=False)

ModelCoingeckoNewCoinRow = TypedDict('ModelCoingeckoNewCoinRow', {
    'chain': NotRequired[str],
    'change_1h_percent': NotRequired[float],
    'change_24h_percent': NotRequired[float],
    'fully_diluted_valuation': NotRequired[float],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'last_added': NotRequired[str],
    'name': NotRequired[str],
    'price': NotRequired[float],
    'rank': NotRequired[int],
    'symbol': NotRequired[str],
    'url': NotRequired[str],
    'volume_24h': NotRequired[float],
}, total=False)

ModelCoingeckoNewCoinsResponse = TypedDict('ModelCoingeckoNewCoinsResponse', {
    'coins': NotRequired[list[ModelCoingeckoNewCoinRow]],
    'fetched_at': NotRequired[str],
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'source_url': NotRequired[str],
    'vs_currency': NotRequired[str],
}, total=False)

ModelCoingeckoNewsArticle = TypedDict('ModelCoingeckoNewsArticle', {
    'coins': NotRequired[list[ModelCoingeckoNewsCoin]],
    'image_url': NotRequired[str],
    'published_text': NotRequired[str],
    'publisher': NotRequired[str],
    'summary': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelCoingeckoNewsCoin = TypedDict('ModelCoingeckoNewsCoin', {
    'change_percent': NotRequired[float],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'symbol': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelCoingeckoNewsResponse = TypedDict('ModelCoingeckoNewsResponse', {
    'articles': NotRequired[list[ModelCoingeckoNewsArticle]],
    'fetched_at': NotRequired[str],
    'limit': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelCoingeckoSearchAssetPlatform = TypedDict('ModelCoingeckoSearchAssetPlatform', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelCoingeckoSearchCategory = TypedDict('ModelCoingeckoSearchCategory', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelCoingeckoSearchCoin = TypedDict('ModelCoingeckoSearchCoin', {
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'market_cap_rank': NotRequired[int],
    'name': NotRequired[str],
    'symbol': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelCoingeckoSearchMarket = TypedDict('ModelCoingeckoSearchMarket', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'type': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelCoingeckoSearchNftcontract = TypedDict('ModelCoingeckoSearchNftcontract', {
    'address': NotRequired[str],
    'asset_platform_id': NotRequired[str],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'symbol': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelCoingeckoSearchPost = TypedDict('ModelCoingeckoSearchPost', {
    'description': NotRequired[str],
    'id': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelCoingeckoSearchResponse = TypedDict('ModelCoingeckoSearchResponse', {
    'asset_platforms': NotRequired[list[ModelCoingeckoSearchAssetPlatform]],
    'categories': NotRequired[list[ModelCoingeckoSearchCategory]],
    'coins': NotRequired[list[ModelCoingeckoSearchCoin]],
    'fetched_at': NotRequired[str],
    'limit': NotRequired[int],
    'markets': NotRequired[list[ModelCoingeckoSearchMarket]],
    'nft_contracts': NotRequired[list[ModelCoingeckoSearchNftcontract]],
    'posts': NotRequired[list[ModelCoingeckoSearchPost]],
    'query': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelCoingeckoTokenUnlockRow = TypedDict('ModelCoingeckoTokenUnlockRow', {
    'change_1h_percent': NotRequired[float],
    'change_24h_percent': NotRequired[float],
    'change_7d_percent': NotRequired[float],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'market_cap': NotRequired[float],
    'name': NotRequired[str],
    'next_unlock_amount': NotRequired[float],
    'next_unlock_percent': NotRequired[float],
    'next_unlock_symbol': NotRequired[str],
    'next_unlock_time_left': NotRequired[str],
    'next_unlock_value_usd': NotRequired[float],
    'price': NotRequired[float],
    'rank': NotRequired[int],
    'released_percent': NotRequired[float],
    'symbol': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelCoingeckoTokenUnlocksResponse = TypedDict('ModelCoingeckoTokenUnlocksResponse', {
    'coins': NotRequired[list[ModelCoingeckoTokenUnlockRow]],
    'fetched_at': NotRequired[str],
    'limit': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelCoingeckoTreasuriesResponse = TypedDict('ModelCoingeckoTreasuriesResponse', {
    'asset': NotRequired[str],
    'entities': NotRequired[list[ModelCoingeckoTreasuryEntityRow]],
    'fetched_at': NotRequired[str],
    'holder_type': NotRequired[str],
    'limit': NotRequired[int],
    'source_url': NotRequired[str],
    'vs_currency': NotRequired[str],
}, total=False)

ModelCoingeckoTreasuryEntityRow = TypedDict('ModelCoingeckoTreasuryEntityRow', {
    'activity_30d': NotRequired[str],
    'country': NotRequired[str],
    'entity_type': NotRequired[str],
    'id': NotRequired[str],
    'mnav': NotRequired[float],
    'name': NotRequired[str],
    'rank': NotRequired[int],
    'ticker': NotRequired[str],
    'today_value_usd': NotRequired[float],
    'top_holdings': NotRequired[str],
    'total_cost_usd': NotRequired[float],
    'url': NotRequired[str],
}, total=False)

ModelCoingeckoTrendingCategory = TypedDict('ModelCoingeckoTrendingCategory', {
    'change_1h_percent': NotRequired[float],
    'change_24h_percent': NotRequired[float],
    'change_7d_percent': NotRequired[float],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelCoingeckoTrendingCoin = TypedDict('ModelCoingeckoTrendingCoin', {
    'change_1h_percent': NotRequired[float],
    'change_24h_percent': NotRequired[float],
    'change_7d_percent': NotRequired[float],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'price': NotRequired[float],
    'symbol': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelCoingeckoTrendingResponse = TypedDict('ModelCoingeckoTrendingResponse', {
    'categories': NotRequired[list[ModelCoingeckoTrendingCategory]],
    'coins': NotRequired[list[ModelCoingeckoTrendingCoin]],
    'fetched_at': NotRequired[str],
    'limit': NotRequired[int],
    'source_url': NotRequired[str],
    'vs_currency': NotRequired[str],
}, total=False)

ModelCoingeckoAnalysisResponseDoc = TypedDict('ModelCoingeckoAnalysisResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCoingeckoAnalysisResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCoingeckoCategoriesResponseDoc = TypedDict('ModelCoingeckoCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCoingeckoCategoriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCoingeckoCategoryCoinsResponseDoc = TypedDict('ModelCoingeckoCategoryCoinsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCoingeckoCategoryCoinsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCoingeckoChainDetailResponseDoc = TypedDict('ModelCoingeckoChainDetailResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCoingeckoChainDetailResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCoingeckoChainsResponseDoc = TypedDict('ModelCoingeckoChainsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCoingeckoChainsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCoingeckoCoinResponseDoc = TypedDict('ModelCoingeckoCoinResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCoingeckoCoinResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCoingeckoExchangeDetailResponseDoc = TypedDict('ModelCoingeckoExchangeDetailResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCoingeckoExchangeDetailResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCoingeckoExchangesResponseDoc = TypedDict('ModelCoingeckoExchangesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCoingeckoExchangesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCoingeckoGainersLosersResponseDoc = TypedDict('ModelCoingeckoGainersLosersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCoingeckoGainersLosersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCoingeckoGlobalChartsResponseDoc = TypedDict('ModelCoingeckoGlobalChartsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCoingeckoGlobalChartsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCoingeckoGlobalResponseDoc = TypedDict('ModelCoingeckoGlobalResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCoingeckoGlobalResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCoingeckoLearnArticlesResponseDoc = TypedDict('ModelCoingeckoLearnArticlesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCoingeckoLearnArticlesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCoingeckoMarketsResponseDoc = TypedDict('ModelCoingeckoMarketsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCoingeckoMarketsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCoingeckoNewCoinsResponseDoc = TypedDict('ModelCoingeckoNewCoinsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCoingeckoNewCoinsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCoingeckoNewsResponseDoc = TypedDict('ModelCoingeckoNewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCoingeckoNewsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCoingeckoNftCategoryResponseDoc = TypedDict('ModelCoingeckoNftCategoryResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCoingeckoNftcategoryResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCoingeckoNftsResponseDoc = TypedDict('ModelCoingeckoNftsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCoingeckoNftsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCoingeckoSearchResponseDoc = TypedDict('ModelCoingeckoSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCoingeckoSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCoingeckoTokenUnlocksResponseDoc = TypedDict('ModelCoingeckoTokenUnlocksResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCoingeckoTokenUnlocksResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCoingeckoTreasuriesResponseDoc = TypedDict('ModelCoingeckoTreasuriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCoingeckoTreasuriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCoingeckoTrendingResponseDoc = TypedDict('ModelCoingeckoTrendingResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCoingeckoTrendingResponse],
    'msg': NotRequired[str],
}, total=False)

ModelContactContact = TypedDict('ModelContactContact', {
    'emails': NotRequired[list[str]],
    'socials': NotRequired[dict[str, Any]],
    'url': NotRequired[str],
}, total=False)

ModelDatasetsDatasetInfo = TypedDict('ModelDatasetsDatasetInfo', {
    'capabilities': NotRequired[list[str]],
    'description': NotRequired[str],
    'id': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelDatasetsDatasetListResponse = TypedDict('ModelDatasetsDatasetListResponse', {
    'items': NotRequired[list[ModelDatasetsDatasetInfo]],
}, total=False)

ModelDatasetsGoogleBusinessFacetResponse = TypedDict('ModelDatasetsGoogleBusinessFacetResponse', {
    'dataset': NotRequired[str],
    'facet': NotRequired[str],
    'items': NotRequired[list[ModelEsGoogleBusinessDatasetFacetItem]],
}, total=False)

ModelDatasetsGoogleBusinessSearchResponse = TypedDict('ModelDatasetsGoogleBusinessSearchResponse', {
    'dataset': NotRequired[str],
    'items': NotRequired[list[ModelEsGoogleBusinessDatasetItem]],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
    'sort': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelDatasetsGoogleMapBusinessResponseDoc = TypedDict('ModelDatasetsGoogleMapBusinessResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelEsGoogleBusiness],
    'msg': NotRequired[str],
}, total=False)

ModelDatasetsGoogleMapBusinessesFacetResponseDoc = TypedDict('ModelDatasetsGoogleMapBusinessesFacetResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelDatasetsGoogleBusinessFacetResponse],
    'msg': NotRequired[str],
}, total=False)

ModelDatasetsGoogleMapBusinessesSearchResponseDoc = TypedDict('ModelDatasetsGoogleMapBusinessesSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelDatasetsGoogleBusinessSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelDatasetsListResponseDoc = TypedDict('ModelDatasetsListResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelDatasetsDatasetListResponse],
    'msg': NotRequired[str],
}, total=False)

ModelEbayItem = TypedDict('ModelEbayItem', {
    'availability': NotRequired[str],
    'condition': NotRequired[str],
    'description': NotRequired[str],
    'images': NotRequired[list[str]],
    'item_feedback_count': NotRequired[int],
    'item_id': NotRequired[str],
    'item_specifics': NotRequired[dict[str, str]],
    'link': NotRequired[str],
    'location': NotRequired[str],
    'price': NotRequired[float],
    'price_text': NotRequired[str],
    'rating': NotRequired[float],
    'rating_count': NotRequired[int],
    'sale_status': NotRequired[str],
    'seller_categories': NotRequired[list[str]],
    'seller_description': NotRequired[str],
    'seller_detailed_ratings': NotRequired[dict[str, float]],
    'seller_feedback_score': NotRequired[int],
    'seller_followers': NotRequired[int],
    'seller_items_sold': NotRequired[int],
    'seller_link': NotRequired[str],
    'seller_logo_url': NotRequired[str],
    'seller_member_since': NotRequired[str],
    'seller_name': NotRequired[str],
    'seller_positive_feedback': NotRequired[float],
    'seller_store_name': NotRequired[str],
    'seller_total_feedback_count': NotRequired[int],
    'shipping': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelEbaySearchItem = TypedDict('ModelEbaySearchItem', {
    'bid_count': NotRequired[int],
    'caption': NotRequired[str],
    'image': NotRequired[str],
    'is_authenticity_guaranteed': NotRequired[bool],
    'item_id': NotRequired[str],
    'link': NotRequired[str],
    'location': NotRequired[str],
    'logistic': NotRequired[str],
    'offer_note': NotRequired[str],
    'price': NotRequired[float],
    'price_from': NotRequired[float],
    'price_to': NotRequired[float],
    'rating': NotRequired[float],
    'rating_num': NotRequired[int],
    'seller': NotRequired[str],
    'sold_count': NotRequired[int],
    'sub_title': NotRequired[str],
    'title': NotRequired[str],
    'watcher_count': NotRequired[int],
}, total=False)

ModelEbaySearchOption = TypedDict('ModelEbaySearchOption', {
    'keyword': Required[str],
    'limit': NotRequired[Literal['60', '120', '240']],
    'listing_type': NotRequired[Literal['active', 'sold', 'completed', 'sold_completed']],
    'page': NotRequired[int],
}, total=False)

ModelEbaySearchResp = TypedDict('ModelEbaySearchResp', {
    'has_more': NotRequired[bool],
    'page': NotRequired[int],
    'result': NotRequired[list[ModelEbaySearchItem]],
    'total': NotRequired[int],
}, total=False)

ModelEbaySeller = TypedDict('ModelEbaySeller', {
    'description': NotRequired[str],
    'detailed_seller_ratings': NotRequired[dict[str, float]],
    'display_name': NotRequired[str],
    'feedback_count': NotRequired[int],
    'feedback_summary': NotRequired[dict[str, int]],
    'followers': NotRequired[int],
    'items_sold': NotRequired[int],
    'location': NotRequired[str],
    'member_since': NotRequired[str],
    'positive_feedback_percent': NotRequired[float],
    'profile_url': NotRequired[str],
    'seller': NotRequired[str],
    'store_name': NotRequired[str],
    'store_url': NotRequired[str],
}, total=False)

ModelEbaySellerAbout = TypedDict('ModelEbaySellerAbout', {
    'banner_url': NotRequired[str],
    'categories': NotRequired[list[ModelEbaySellerAboutCategory]],
    'contact_seller_url': NotRequired[str],
    'description': NotRequired[str],
    'followers': NotRequired[int],
    'items_sold': NotRequired[int],
    'location': NotRequired[str],
    'logo_url': NotRequired[str],
    'member_since': NotRequired[str],
    'positive_feedback_percent': NotRequired[float],
    'seller': NotRequired[str],
    'store_name': NotRequired[str],
    'store_url': NotRequired[str],
    'top_rated_seller': NotRequired[bool],
    'top_rated_seller_summary': NotRequired[str],
}, total=False)

ModelEbaySellerAboutCategory = TypedDict('ModelEbaySellerAboutCategory', {
    'name': NotRequired[str],
    'subcategories': NotRequired[list[ModelEbaySellerAboutSubcategory]],
    'url': NotRequired[str],
}, total=False)

ModelEbaySellerAboutSubcategory = TypedDict('ModelEbaySellerAboutSubcategory', {
    'name': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelEbaySellerFeedback = TypedDict('ModelEbaySellerFeedback', {
    'description': NotRequired[str],
    'detailed_seller_ratings': NotRequired[dict[str, float]],
    'followers': NotRequired[int],
    'has_more': NotRequired[bool],
    'items_sold': NotRequired[int],
    'next_page': NotRequired[int],
    'overall_rating_summary': NotRequired[dict[str, int]],
    'page': NotRequired[int],
    'per_page': NotRequired[int],
    'positive_feedback_percent': NotRequired[float],
    'reviews': NotRequired[list[ModelEbaySellerReview]],
    'seller': NotRequired[str],
    'store_name': NotRequired[str],
    'store_url': NotRequired[str],
    'total_feedback_count': NotRequired[int],
}, total=False)

ModelEbaySellerReview = TypedDict('ModelEbaySellerReview', {
    'buyer': NotRequired[str],
    'buyer_feedback': NotRequired[int],
    'comment': NotRequired[str],
    'period': NotRequired[str],
    'rating': NotRequired[str],
    'verified_purchase': NotRequired[bool],
}, total=False)

ModelEbayItemResponseDoc = TypedDict('ModelEbayItemResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelEbayItem],
    'msg': NotRequired[Any],
}, total=False)

ModelEbaySearchResponseDoc = TypedDict('ModelEbaySearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelEbaySearchResp],
    'msg': NotRequired[Any],
}, total=False)

ModelEbaySellerAboutResponseDoc = TypedDict('ModelEbaySellerAboutResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelEbaySellerAbout],
    'msg': NotRequired[Any],
}, total=False)

ModelEbaySellerFeedbackResponseDoc = TypedDict('ModelEbaySellerFeedbackResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelEbaySellerFeedback],
    'msg': NotRequired[Any],
}, total=False)

ModelEbaySellerResponseDoc = TypedDict('ModelEbaySellerResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelEbaySeller],
    'msg': NotRequired[Any],
}, total=False)

ModelEbaySellerShopResponseDoc = TypedDict('ModelEbaySellerShopResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelEbaySearchResp],
    'msg': NotRequired[Any],
}, total=False)

ModelEsGeoPoint = TypedDict('ModelEsGeoPoint', {
    'lat': NotRequired[float],
    'lon': NotRequired[float],
}, total=False)

ModelEsGoogleBusiness = TypedDict('ModelEsGoogleBusiness', {
    'address': NotRequired[str],
    'amenities': NotRequired[list[str]],
    'category': NotRequired[list[str]],
    'city': NotRequired[str],
    'contact': NotRequired[ModelContactContact],
    'contact_is_updated': NotRequired[bool],
    'country': NotRequired[str],
    'county': NotRequired[str],
    'created_at': NotRequired[str],
    'description': NotRequired[str],
    'geo': NotRequired[ModelEsGeoPoint],
    'geo_is_updated': NotRequired[bool],
    'id': NotRequired[str],
    'image': NotRequired[str],
    'locations': NotRequired[list[str]],
    'name': NotRequired[str],
    'phone': NotRequired[str],
    'place_id': NotRequired[str],
    'rating': NotRequired[float],
    'review_count': NotRequired[int],
    'similarweb': NotRequired[ModelSimilarwebSimilarWebResp],
    'state': NotRequired[str],
    'town': NotRequired[str],
    'updated_at': NotRequired[str],
    'url': NotRequired[str],
    'website': NotRequired[str],
    'website_status': NotRequired[ModelEsWebsiteStatus],
}, total=False)

ModelEsGoogleBusinessDatasetFacetItem = TypedDict('ModelEsGoogleBusinessDatasetFacetItem', {
    'count': NotRequired[int],
    'value': NotRequired[str],
}, total=False)

ModelEsGoogleBusinessDatasetItem = TypedDict('ModelEsGoogleBusinessDatasetItem', {
    'address': NotRequired[str],
    'amenities': NotRequired[list[str]],
    'category': NotRequired[list[str]],
    'city': NotRequired[str],
    'contact': NotRequired[ModelContactContact],
    'contact_is_updated': NotRequired[bool],
    'country': NotRequired[str],
    'county': NotRequired[str],
    'created_at': NotRequired[str],
    'description': NotRequired[str],
    'distance_m': NotRequired[float],
    'geo': NotRequired[ModelEsGeoPoint],
    'geo_is_updated': NotRequired[bool],
    'id': NotRequired[str],
    'image': NotRequired[str],
    'locations': NotRequired[list[str]],
    'name': NotRequired[str],
    'phone': NotRequired[str],
    'place_id': NotRequired[str],
    'rating': NotRequired[float],
    'review_count': NotRequired[int],
    'similarweb': NotRequired[ModelSimilarwebSimilarWebResp],
    'state': NotRequired[str],
    'town': NotRequired[str],
    'updated_at': NotRequired[str],
    'url': NotRequired[str],
    'website': NotRequired[str],
    'website_status': NotRequired[ModelEsWebsiteStatus],
}, total=False)

ModelEsWebsiteStatus = TypedDict('ModelEsWebsiteStatus', {
    'checked_at': NotRequired[str],
    'dns_resolvable': NotRequired[bool],
    'error': NotRequired[str],
    'http_reachable': NotRequired[bool],
    'status_code': NotRequired[int],
    'url': NotRequired[str],
}, total=False)

ModelFinanceAbout = TypedDict('ModelFinanceAbout', {
    'about': NotRequired[str],
    'ceo': NotRequired[str],
    'employees': NotRequired[int],
    'founded': NotRequired[str],
    'headquarters': NotRequired[str],
    'website': NotRequired[str],
}, total=False)

ModelFinanceBalanceSheet = TypedDict('ModelFinanceBalanceSheet', {
    'cash_and_short_term_change_yy': NotRequired[float],
    'cash_and_short_term_investments': NotRequired[float],
    'price_to_book': NotRequired[float],
    'quarter': NotRequired[int],
    'return_on_assets': NotRequired[float],
    'return_on_capital': NotRequired[float],
    'shares_outstanding': NotRequired[float],
    'total_assets': NotRequired[float],
    'total_assets_change_yy': NotRequired[float],
    'total_equity': NotRequired[float],
    'total_liabilities': NotRequired[float],
    'total_liabilities_change_yy': NotRequired[float],
    'year': NotRequired[int],
}, total=False)

ModelFinanceCashFlow = TypedDict('ModelFinanceCashFlow', {
    'cash_from_financing': NotRequired[float],
    'cash_from_financing_change_yy': NotRequired[float],
    'cash_from_investing': NotRequired[float],
    'cash_from_investing_change_yy': NotRequired[float],
    'cash_from_operations': NotRequired[float],
    'cash_from_operations_change_yy': NotRequired[float],
    'free_cash_flow': NotRequired[float],
    'free_cash_flow_change_yy': NotRequired[float],
    'net_change_in_cash': NotRequired[float],
    'net_change_in_cash_change_yy': NotRequired[float],
    'net_income': NotRequired[float],
    'net_income_change_yy': NotRequired[float],
    'quarter': NotRequired[int],
    'year': NotRequired[int],
}, total=False)

ModelFinanceCategoryNewsResponse = TypedDict('ModelFinanceCategoryNewsResponse', {
    'category': NotRequired[str],
    'items': NotRequired[list[ModelFinanceFinanceArticle]],
    'offset': NotRequired[int],
}, total=False)

ModelFinanceCategoryStocksResponse = TypedDict('ModelFinanceCategoryStocksResponse', {
    'category': NotRequired[str],
    'items': NotRequired[list[ModelFinanceInstrument]],
    'offset': NotRequired[int],
}, total=False)

ModelFinanceChartResponse = TypedDict('ModelFinanceChartResponse', {
    'instrument': NotRequired[ModelFinanceInstrument],
    'points': NotRequired[list[ModelFinanceTicker]],
    'previous_close': NotRequired[float],
    'window': NotRequired[str],
}, total=False)

ModelFinanceClassificationResponse = TypedDict('ModelFinanceClassificationResponse', {
    'categories': NotRequired[list[str]],
    'instrument': NotRequired[ModelFinanceInstrument],
}, total=False)

ModelFinanceCompanyInfo = TypedDict('ModelFinanceCompanyInfo', {
    'ceo': NotRequired[str],
    'description': NotRequired[str],
    'employees': NotRequired[int],
    'fifty_two_week_high': NotRequired[float],
    'fifty_two_week_low': NotRequired[float],
    'headquarters': NotRequired[str],
    'high': NotRequired[float],
    'low': NotRequired[float],
    'market_cap': NotRequired[float],
    'open': NotRequired[float],
    'pe_ratio': NotRequired[float],
    'sector': NotRequired[str],
    'volume': NotRequired[int],
}, total=False)

ModelFinanceContextResponse = TypedDict('ModelFinanceContextResponse', {
    'items': NotRequired[list[ModelFinanceInstrument]],
    'query': NotRequired[str],
}, total=False)

ModelFinanceEarningsCalendarResponse = TypedDict('ModelFinanceEarningsCalendarResponse', {
    'items': NotRequired[list[ModelFinanceEarningsEvent]],
}, total=False)

ModelFinanceEarningsEvent = TypedDict('ModelFinanceEarningsEvent', {
    'company_name': NotRequired[str],
    'conference_phone': NotRequired[str],
    'conference_url': NotRequired[str],
    'event_time': NotRequired[str],
    'event_unix': NotRequired[int],
    'fiscal_period': NotRequired[str],
    'instrument': NotRequired[ModelFinanceInstrument],
}, total=False)

ModelFinanceFinanceArticle = TypedDict('ModelFinanceFinanceArticle', {
    'published_at': NotRequired[str],
    'published_unix': NotRequired[int],
    'related': NotRequired[list[ModelFinanceInstrument]],
    'source': NotRequired[str],
    'thumbnail_url': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFinanceFinancialPeriod = TypedDict('ModelFinanceFinancialPeriod', {
    'capital_expenditure': NotRequired[float],
    'ebitda': NotRequired[float],
    'eps': NotRequired[float],
    'eps_diluted': NotRequired[float],
    'free_cash_flow': NotRequired[float],
    'net_income': NotRequired[float],
    'operating_cash_flow': NotRequired[float],
    'operating_income': NotRequired[float],
    'operating_margin': NotRequired[float],
    'pe_ratio': NotRequired[float],
    'period': NotRequired[str],
    'period_end': NotRequired[str],
    'profit_margin': NotRequired[float],
    'revenue': NotRequired[float],
    'revenue_growth_yoy': NotRequired[float],
    'shares_outstanding': NotRequired[float],
    'total_assets': NotRequired[float],
    'total_equity': NotRequired[float],
    'total_liabilities': NotRequired[float],
}, total=False)

ModelFinanceFinancialsResponse = TypedDict('ModelFinanceFinancialsResponse', {
    'annual': NotRequired[list[ModelFinanceFinancialPeriod]],
    'currency': NotRequired[str],
    'quarterly': NotRequired[list[ModelFinanceFinancialPeriod]],
}, total=False)

ModelFinanceHeadlineResponse = TypedDict('ModelFinanceHeadlineResponse', {
    'article': NotRequired[ModelFinanceFinanceArticle],
}, total=False)

ModelFinanceIncomeStatement = TypedDict('ModelFinanceIncomeStatement', {
    'earnings_per_share': NotRequired[float],
    'earnings_per_share_change_yy': NotRequired[float],
    'ebitda': NotRequired[float],
    'ebitda_change_yy': NotRequired[float],
    'effective_tax_rate': NotRequired[float],
    'net_income': NotRequired[float],
    'net_income_change_yy': NotRequired[float],
    'net_profit_margin': NotRequired[float],
    'net_profit_margin_change_yy': NotRequired[float],
    'operating_expense': NotRequired[float],
    'operating_expense_change_yy': NotRequired[float],
    'quarter': NotRequired[int],
    'revenue': NotRequired[float],
    'revenue_change_yy': NotRequired[float],
    'year': NotRequired[int],
}, total=False)

ModelFinanceInstrument = TypedDict('ModelFinanceInstrument', {
    'after_hours': NotRequired[ModelFinancePriceChange],
    'change': NotRequired[float],
    'change_percent': NotRequired[float],
    'country': NotRequired[str],
    'currency': NotRequired[str],
    'exchange': NotRequired[str],
    'google_id': NotRequired[str],
    'identifier': NotRequired[str],
    'last_update_unix': NotRequired[int],
    'name': NotRequired[str],
    'previous_close': NotRequired[float],
    'price': NotRequired[float],
    'ticker': NotRequired[str],
    'timezone': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelFinanceInvestment = TypedDict('ModelFinanceInvestment', {
    'balance_sheet': NotRequired[list[ModelFinanceBalanceSheet]],
    'cash_flow': NotRequired[list[ModelFinanceCashFlow]],
    'income_statement': NotRequired[list[ModelFinanceIncomeStatement]],
}, total=False)

ModelFinanceKeyStats = TypedDict('ModelFinanceKeyStats', {
    'avg_volume': NotRequired[int],
    'climate_change_score': NotRequired[str],
    'currency': NotRequired[str],
    'day_range': NotRequired[ModelFinanceRange],
    'dividend_yield': NotRequired[float],
    'market_cap': NotRequired[int],
    'pe_ratio': NotRequired[float],
    'previous_close': NotRequired[float],
    'primary_exchange': NotRequired[str],
    'tags': NotRequired[list[str]],
    'year_range': NotRequired[ModelFinanceRange],
}, total=False)

ModelFinanceMarketMoversResponse = TypedDict('ModelFinanceMarketMoversResponse', {
    'categories': NotRequired[list[int]],
    'count': NotRequired[int],
    'items': NotRequired[list[ModelFinanceInstrument]],
    'offset': NotRequired[int],
}, total=False)

ModelFinanceNews = TypedDict('ModelFinanceNews', {
    'source': NotRequired[str],
    'time': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFinancePriceChange = TypedDict('ModelFinancePriceChange', {
    'change': NotRequired[float],
    'change_percent': NotRequired[float],
    'price': NotRequired[float],
}, total=False)

ModelFinanceQuoteResp = TypedDict('ModelFinanceQuoteResp', {
    'about': NotRequired[ModelFinanceAbout],
    'investment': NotRequired[ModelFinanceInvestment],
    'key_stats': NotRequired[ModelFinanceKeyStats],
    'news': NotRequired[list[ModelFinanceNews]],
    'tickers': NotRequired[list[ModelFinanceTicker]],
    'title': NotRequired[str],
}, total=False)

ModelFinanceRange = TypedDict('ModelFinanceRange', {
    'from': NotRequired[float],
    'to': NotRequired[float],
}, total=False)

ModelFinanceRelatedResponse = TypedDict('ModelFinanceRelatedResponse', {
    'instrument': NotRequired[ModelFinanceInstrument],
    'items': NotRequired[list[ModelFinanceInstrument]],
}, total=False)

ModelFinanceStockData = TypedDict('ModelFinanceStockData', {
    'change': NotRequired[float],
    'company_name': NotRequired[str],
    'currency': NotRequired[str],
    'exchange': NotRequired[str],
    'percentage': NotRequired[float],
    'price': NotRequired[float],
    'ticker': NotRequired[str],
}, total=False)

ModelFinanceTicker = TypedDict('ModelFinanceTicker', {
    'price': NotRequired[float],
    'time': NotRequired[str],
    'volume': NotRequired[int],
}, total=False)

ModelFinanceTopStocksResponse = TypedDict('ModelFinanceTopStocksResponse', {
    'items': NotRequired[list[ModelFinanceInstrument]],
    'metric': NotRequired[int],
    'page': NotRequired[int],
}, total=False)

ModelFinanceArticlesResponseDoc = TypedDict('ModelFinanceArticlesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelFinanceFinanceArticle]],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceCategoryNewsResponseDoc = TypedDict('ModelFinanceCategoryNewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceCategoryNewsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceCategoryStocksResponseDoc = TypedDict('ModelFinanceCategoryStocksResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceCategoryStocksResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceChartResponseDoc = TypedDict('ModelFinanceChartResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceChartResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceClassificationResponseDoc = TypedDict('ModelFinanceClassificationResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceClassificationResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceCompanyResponseDoc = TypedDict('ModelFinanceCompanyResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceCompanyInfo],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceContextResponseDoc = TypedDict('ModelFinanceContextResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceContextResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceEarningsResponseDoc = TypedDict('ModelFinanceEarningsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceEarningsCalendarResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceFinancialsResponseDoc = TypedDict('ModelFinanceFinancialsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceFinancialsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceHeadlineResponseDoc = TypedDict('ModelFinanceHeadlineResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceHeadlineResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceInstrumentsResponseDoc = TypedDict('ModelFinanceInstrumentsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelFinanceInstrument]],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceMarketMoversResponseDoc = TypedDict('ModelFinanceMarketMoversResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceMarketMoversResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceQuoteResponseDoc = TypedDict('ModelFinanceQuoteResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceQuoteResp],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceRelatedResponseDoc = TypedDict('ModelFinanceRelatedResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceRelatedResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceSearchResponseDoc = TypedDict('ModelFinanceSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelFinanceStockData]],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceTickerResponseDoc = TypedDict('ModelFinanceTickerResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelFinanceTicker]],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceTopStocksResponseDoc = TypedDict('ModelFinanceTopStocksResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceTopStocksResponse],
    'msg': NotRequired[str],
}, total=False)

ModelGeocodingAddress = TypedDict('ModelGeocodingAddress', {
    'ISO3166-2-lvl4': NotRequired[str],
    'ISO3166-2-lvl6': NotRequired[str],
    'city': NotRequired[str],
    'country': NotRequired[str],
    'country_code': NotRequired[str],
    'county': NotRequired[str],
    'house_number': NotRequired[str],
    'neighbourhood': NotRequired[str],
    'office': NotRequired[str],
    'postcode': NotRequired[str],
    'road': NotRequired[str],
    'state': NotRequired[str],
    'state_district': NotRequired[str],
    'suburb': NotRequired[str],
    'town': NotRequired[str],
    'village': NotRequired[str],
}, total=False)

ModelGeocodingLookupResponse = TypedDict('ModelGeocodingLookupResponse', {
    'query': NotRequired[str],
    'results': NotRequired[list[ModelGeocodingPlace]],
}, total=False)

ModelGeocodingPlace = TypedDict('ModelGeocodingPlace', {
    'address': NotRequired[ModelGeocodingAddress],
    'addresstype': NotRequired[str],
    'boundingbox': NotRequired[list[str]],
    'category': NotRequired[str],
    'display_name': NotRequired[str],
    'extratags': NotRequired[dict[str, str]],
    'importance': NotRequired[float],
    'lat': NotRequired[str],
    'licence': NotRequired[str],
    'lon': NotRequired[str],
    'name': NotRequired[str],
    'namedetails': NotRequired[dict[str, str]],
    'osm_id': NotRequired[int],
    'osm_type': NotRequired[str],
    'place_id': NotRequired[int],
    'place_rank': NotRequired[int],
    'type': NotRequired[str],
}, total=False)

ModelGeocodingSearchResponse = TypedDict('ModelGeocodingSearchResponse', {
    'query': NotRequired[str],
    'results': NotRequired[list[ModelGeocodingPlace]],
}, total=False)

ModelGeocodingLookupResponseDoc = TypedDict('ModelGeocodingLookupResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelGeocodingLookupResponse],
    'msg': NotRequired[str],
}, total=False)

ModelGeocodingReverseResponseDoc = TypedDict('ModelGeocodingReverseResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelGeocodingPlace],
    'msg': NotRequired[str],
}, total=False)

ModelGeocodingSearchResponseDoc = TypedDict('ModelGeocodingSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelGeocodingSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleJobItem = TypedDict('ModelGoogleJobItem', {
    'company': NotRequired[str],
    'employment': NotRequired[str],
    'location': NotRequired[str],
    'posted_at': NotRequired[str],
    'snippet': NotRequired[str],
    'source': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelGoogleJobsOption = TypedDict('ModelGoogleJobsOption', {
    'location': NotRequired[str],
    'page': NotRequired[int],
    'query': Required[str],
}, total=False)

ModelGoogleJobsResponse = TypedDict('ModelGoogleJobsResponse', {
    'location': NotRequired[str],
    'page': NotRequired[int],
    'query': NotRequired[str],
    'results': NotRequired[list[ModelGoogleJobItem]],
}, total=False)

ModelGoogleKgAttrItem = TypedDict('ModelGoogleKgAttrItem', {
    'id': NotRequired[str],
    'label': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelGoogleKnowledgeGraph = TypedDict('ModelGoogleKnowledgeGraph', {
    'attributes': NotRequired[list[ModelGoogleKgAttrItem]],
    'description': NotRequired[str],
    'sub_title': NotRequired[str],
    'title': NotRequired[str],
    'wikipedia_link': NotRequired[str],
}, total=False)

ModelGoogleMapSearchOption = TypedDict('ModelGoogleMapSearchOption', {
    'country': NotRequired[str],
    'keyword': NotRequired[str],
    'language': NotRequired[str],
}, total=False)

ModelGooglePeopleAlsoAskItem = TypedDict('ModelGooglePeopleAlsoAskItem', {
    'answer': NotRequired[str],
    'date': NotRequired[str],
    'link': NotRequired[str],
    'question': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelGooglePlace = TypedDict('ModelGooglePlace', {
    'address': NotRequired[str],
    'amenities': NotRequired[list[str]],
    'category': NotRequired[list[str]],
    'description': NotRequired[str],
    'image': NotRequired[str],
    'latitude': NotRequired[float],
    'locations': NotRequired[list[str]],
    'longitude': NotRequired[float],
    'name': NotRequired[str],
    'phone': NotRequired[str],
    'place_id': NotRequired[str],
    'rating': NotRequired[float],
    'review_count': NotRequired[int],
    'url': NotRequired[str],
    'website': NotRequired[str],
}, total=False)

ModelGoogleSearchItem = TypedDict('ModelGoogleSearchItem', {
    'Snippet': NotRequired[str],
    'icon': NotRequired[str],
    'link': NotRequired[str],
    'position': NotRequired[int],
    'time': NotRequired[str],
    'title': NotRequired[str],
    'website_name': NotRequired[str],
}, total=False)

ModelGoogleSearchOption = TypedDict('ModelGoogleSearchOption', {
    'country': Required[str],
    'keyword': Required[str],
    'language': Required[str],
    'limit': NotRequired[int],
    'page': NotRequired[int],
}, total=False)

ModelGoogleSearchResp = TypedDict('ModelGoogleSearchResp', {
    'knowledge_graph': NotRequired[ModelGoogleKnowledgeGraph],
    'people_also_ask': NotRequired[list[ModelGooglePeopleAlsoAskItem]],
    'people_also_search_for': NotRequired[list[str]],
    'related_searches': NotRequired[list[str]],
    'result': NotRequired[list[ModelGoogleSearchItem]],
}, total=False)

ModelGoogleSuggestResponse = TypedDict('ModelGoogleSuggestResponse', {
    'query': NotRequired[str],
    'suggestions': NotRequired[list[ModelGoogleSuggestionResult]],
}, total=False)

ModelGoogleSuggestionResult = TypedDict('ModelGoogleSuggestionResult', {
    'position': NotRequired[int],
    'query': NotRequired[str],
}, total=False)

ModelGoogleMapPlaceResponseDoc = TypedDict('ModelGoogleMapPlaceResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelGooglePlace],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleMapSearchResponseDoc = TypedDict('ModelGoogleMapSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelGooglePlace]],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleSearchResponseDoc = TypedDict('ModelGoogleSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelGoogleSearchResp],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleSuggestResponseDoc = TypedDict('ModelGoogleSuggestResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelGoogleSuggestResponse],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleplayApp = TypedDict('ModelGoogleplayApp', {
    'ad_supported': NotRequired[bool],
    'android_max_version': NotRequired[str],
    'android_version': NotRequired[str],
    'android_version_text': NotRequired[str],
    'app_id': NotRequired[str],
    'available': NotRequired[bool],
    'categories': NotRequired[list[ModelGoogleplayCategory]],
    'comments': NotRequired[list[str]],
    'content_rating': NotRequired[str],
    'content_rating_description': NotRequired[str],
    'currency': NotRequired[str],
    'description': NotRequired[str],
    'description_html': NotRequired[str],
    'developer': NotRequired[str],
    'developer_address': NotRequired[str],
    'developer_email': NotRequired[str],
    'developer_id': NotRequired[str],
    'developer_internal_id': NotRequired[str],
    'developer_legal_address': NotRequired[str],
    'developer_legal_email': NotRequired[str],
    'developer_legal_name': NotRequired[str],
    'developer_legal_phone_number': NotRequired[str],
    'developer_website': NotRequired[str],
    'discount_end_date': NotRequired[str],
    'early_access_enabled': NotRequired[bool],
    'features': NotRequired[list[ModelGoogleplayFeature]],
    'free': NotRequired[bool],
    'genre': NotRequired[str],
    'genre_id': NotRequired[str],
    'header_image': NotRequired[str],
    'histogram': NotRequired[dict[str, Any]],
    'iap_range': NotRequired[str],
    'icon': NotRequired[str],
    'installs': NotRequired[str],
    'is_available_in_play_pass': NotRequired[bool],
    'max_installs': NotRequired[int],
    'min_installs': NotRequired[int],
    'offers_iap': NotRequired[bool],
    'original_price': NotRequired[float],
    'preregister': NotRequired[bool],
    'preview_video': NotRequired[str],
    'price': NotRequired[float],
    'price_text': NotRequired[str],
    'privacy_policy': NotRequired[str],
    'ratings': NotRequired[int],
    'recent_changes': NotRequired[str],
    'released': NotRequired[str],
    'reviews': NotRequired[int],
    'score': NotRequired[float],
    'score_text': NotRequired[str],
    'screenshots': NotRequired[list[str]],
    'summary': NotRequired[str],
    'title': NotRequired[str],
    'updated': NotRequired[int],
    'url': NotRequired[str],
    'version': NotRequired[str],
    'video': NotRequired[str],
    'video_image': NotRequired[str],
}, total=False)

ModelGoogleplayAppDetailsResponse = TypedDict('ModelGoogleplayAppDetailsResponse', {
    'code': NotRequired[int],
    'data': NotRequired[ModelGoogleplayApp],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleplayCategory = TypedDict('ModelGoogleplayCategory', {
    'id': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelGoogleplayDataSafetyEntry = TypedDict('ModelGoogleplayDataSafetyEntry', {
    'data': NotRequired[str],
    'optional': NotRequired[bool],
    'purpose': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelGoogleplayDataSafetyResult = TypedDict('ModelGoogleplayDataSafetyResult', {
    'collected_data': NotRequired[list[ModelGoogleplayDataSafetyEntry]],
    'privacy_policy_url': NotRequired[str],
    'security_practices': NotRequired[list[ModelGoogleplaySecurityPractice]],
    'shared_data': NotRequired[list[ModelGoogleplayDataSafetyEntry]],
}, total=False)

ModelGoogleplayFeature = TypedDict('ModelGoogleplayFeature', {
    'description': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelGoogleplayReview = TypedDict('ModelGoogleplayReview', {
    'criterias': NotRequired[list[ModelGoogleplayReviewCriteria]],
    'date': NotRequired[str],
    'id': NotRequired[str],
    'reply_date': NotRequired[str],
    'reply_text': NotRequired[str],
    'score': NotRequired[int],
    'score_text': NotRequired[str],
    'text': NotRequired[str],
    'thumbs_up': NotRequired[int],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'user_image': NotRequired[str],
    'user_name': NotRequired[str],
    'version': NotRequired[str],
}, total=False)

ModelGoogleplayReviewCriteria = TypedDict('ModelGoogleplayReviewCriteria', {
    'criteria': NotRequired[str],
    'rating': NotRequired[int],
}, total=False)

ModelGoogleplayReviewsResult = TypedDict('ModelGoogleplayReviewsResult', {
    'data': NotRequired[list[ModelGoogleplayReview]],
    'next_pagination_token': NotRequired[str],
}, total=False)

ModelGoogleplaySecurityPractice = TypedDict('ModelGoogleplaySecurityPractice', {
    'description': NotRequired[str],
    'practice': NotRequired[str],
}, total=False)

ModelGoogleplaySuggestion = TypedDict('ModelGoogleplaySuggestion', {
    'term': NotRequired[str],
}, total=False)

ModelGoogleplayCategoriesResponseDoc = TypedDict('ModelGoogleplayCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[str]],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleplayDataSafetyResponseDoc = TypedDict('ModelGoogleplayDataSafetyResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelGoogleplayDataSafetyResult],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleplayDeveloperResultsResponseDoc = TypedDict('ModelGoogleplayDeveloperResultsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[Any]],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleplayListResultsResponseDoc = TypedDict('ModelGoogleplayListResultsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[Any]],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleplayPermissionsResultsResponseDoc = TypedDict('ModelGoogleplayPermissionsResultsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[Any]],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleplayReviewsResponseDoc = TypedDict('ModelGoogleplayReviewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelGoogleplayReviewsResult],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleplaySearchResultsResponseDoc = TypedDict('ModelGoogleplaySearchResultsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[Any]],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleplaySimilarResultsResponseDoc = TypedDict('ModelGoogleplaySimilarResultsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[Any]],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleplaySuggestResponseDoc = TypedDict('ModelGoogleplaySuggestResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelGoogleplaySuggestion]],
    'msg': NotRequired[str],
}, total=False)

ModelInstagramBusinessAddress = TypedDict('ModelInstagramBusinessAddress', {
    'city_name': NotRequired[str],
    'latitude': NotRequired[float],
    'longitude': NotRequired[float],
    'street_address': NotRequired[str],
    'zip_code': NotRequired[str],
}, total=False)

ModelInstagramCaption = TypedDict('ModelInstagramCaption', {
    'text': NotRequired[str],
    'user': NotRequired[ModelInstagramUser],
}, total=False)

ModelInstagramClipsMetadata = TypedDict('ModelInstagramClipsMetadata', {
    'audio_type': NotRequired[str],
    'is_shared_to_fb': NotRequired[bool],
    'original_sound_info': NotRequired[ModelInstagramOriginalSoundInfo],
}, total=False)

ModelInstagramIgartist = TypedDict('ModelInstagramIgartist', {
    'id': NotRequired[str],
    'username': NotRequired[str],
}, total=False)

ModelInstagramIgcaption = TypedDict('ModelInstagramIgcaption', {
    'created_at': NotRequired[int],
    'pk': NotRequired[str],
    'text': NotRequired[str],
}, total=False)

ModelInstagramIgowner = TypedDict('ModelInstagramIgowner', {
    'id': NotRequired[str],
    'is_private': NotRequired[bool],
    'pk': NotRequired[str],
    'profile_pic_url': NotRequired[str],
    'username': NotRequired[str],
}, total=False)

ModelInstagramIguser = TypedDict('ModelInstagramIguser', {
    'full_name': NotRequired[str],
    'id': NotRequired[str],
    'is_private': NotRequired[bool],
    'is_verified': NotRequired[bool],
    'pk': NotRequired[str],
    'profile_pic_url': NotRequired[str],
    'username': NotRequired[str],
}, total=False)

ModelInstagramImageCandidate = TypedDict('ModelInstagramImageCandidate', {
    'height': NotRequired[int],
    'url': NotRequired[str],
    'width': NotRequired[int],
}, total=False)

ModelInstagramImageVersions = TypedDict('ModelInstagramImageVersions', {
    'candidates': NotRequired[list[ModelInstagramImageCandidate]],
}, total=False)

ModelInstagramImageVersions2 = TypedDict('ModelInstagramImageVersions2', {
    'candidates': NotRequired[list[ModelInstagramImageCandidate]],
}, total=False)

ModelInstagramItem = TypedDict('ModelInstagramItem', {
    'media': NotRequired[ModelInstagramMedia],
}, total=False)

ModelInstagramMedia = TypedDict('ModelInstagramMedia', {
    'caption': NotRequired[ModelInstagramCaption],
    'code': NotRequired[str],
    'comment_count': NotRequired[int],
    'display_uri': NotRequired[str],
    'id': NotRequired[str],
    'image_versions2': NotRequired[ModelInstagramImageVersions],
    'like_count': NotRequired[int],
    'media_type': NotRequired[int],
    'play_count': NotRequired[int],
    'taken_at': NotRequired[int],
}, total=False)

ModelInstagramMediaItem = TypedDict('ModelInstagramMediaItem', {
    'accessibility_caption': NotRequired[str],
    'caption': NotRequired[ModelInstagramIgcaption],
    'clips_metadata': NotRequired[ModelInstagramClipsMetadata],
    'code': NotRequired[str],
    'comment_count': NotRequired[int],
    'display_uri': NotRequired[str],
    'has_audio': NotRequired[bool],
    'id': NotRequired[str],
    'image_versions2': NotRequired[ModelInstagramImageVersions2],
    'like_count': NotRequired[int],
    'link': NotRequired[str],
    'media_type': NotRequired[int],
    'original_height': NotRequired[int],
    'original_width': NotRequired[int],
    'owner': NotRequired[ModelInstagramIgowner],
    'pk': NotRequired[str],
    'product_type': NotRequired[str],
    'taken_at': NotRequired[int],
    'user': NotRequired[ModelInstagramIguser],
    'video_versions': NotRequired[list[ModelInstagramVideoVersion]],
    'view_count': NotRequired[int],
}, total=False)

ModelInstagramOriginalSoundInfo = TypedDict('ModelInstagramOriginalSoundInfo', {
    'audio_asset_id': NotRequired[str],
    'ig_artist': NotRequired[ModelInstagramIgartist],
    'is_explicit': NotRequired[bool],
    'original_audio_title': NotRequired[str],
    'should_mute_audio': NotRequired[bool],
}, total=False)

ModelInstagramPagingInfo = TypedDict('ModelInstagramPagingInfo', {
    'max_id': NotRequired[str],
    'more_available': NotRequired[bool],
}, total=False)

ModelInstagramPost = TypedDict('ModelInstagramPost', {
    'caption': NotRequired[str],
    'children': NotRequired[list[ModelInstagramPost]],
    'comment_count': NotRequired[int],
    'height': NotRequired[int],
    'id': NotRequired[str],
    'is_video': NotRequired[bool],
    'like_count': NotRequired[int],
    'media_url': NotRequired[str],
    'product_type': NotRequired[str],
    'shortcode': NotRequired[str],
    'taken_at': NotRequired[str],
    'video_url': NotRequired[str],
    'view_count': NotRequired[int],
    'width': NotRequired[int],
}, total=False)

ModelInstagramReelResponse = TypedDict('ModelInstagramReelResponse', {
    'items': NotRequired[list[ModelInstagramItem]],
    'paging_info': NotRequired[ModelInstagramPagingInfo],
}, total=False)

ModelInstagramRelatedProfile = TypedDict('ModelInstagramRelatedProfile', {
    'full_name': NotRequired[str],
    'id': NotRequired[str],
    'is_private': NotRequired[bool],
    'is_verified': NotRequired[bool],
    'profile_pic_url': NotRequired[str],
    'username': NotRequired[str],
}, total=False)

ModelInstagramUser = TypedDict('ModelInstagramUser', {
    'full_name': NotRequired[str],
    'id': NotRequired[str],
    'username': NotRequired[str],
}, total=False)

ModelInstagramUserProfile = TypedDict('ModelInstagramUserProfile', {
    'bio_links': NotRequired[list[str]],
    'biography': NotRequired[str],
    'category_name': NotRequired[str],
    'external_url': NotRequired[str],
    'fbid': NotRequired[str],
    'followers_count': NotRequired[int],
    'following_count': NotRequired[int],
    'full_name': NotRequired[str],
    'id': NotRequired[str],
    'is_private': NotRequired[bool],
    'is_verified': NotRequired[bool],
    'location': NotRequired[ModelInstagramBusinessAddress],
    'posts': NotRequired[list[ModelInstagramPost]],
    'posts_count': NotRequired[int],
    'profile_pic_url': NotRequired[str],
    'related_profiles': NotRequired[list[ModelInstagramRelatedProfile]],
    'username': NotRequired[str],
}, total=False)

ModelInstagramVideoVersion = TypedDict('ModelInstagramVideoVersion', {
    'height': NotRequired[int],
    'type': NotRequired[int],
    'url': NotRequired[str],
    'width': NotRequired[int],
}, total=False)

ModelInstagramPostResponseDoc = TypedDict('ModelInstagramPostResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelInstagramMediaItem],
    'msg': NotRequired[str],
}, total=False)

ModelInstagramProfileResponseDoc = TypedDict('ModelInstagramProfileResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelInstagramUserProfile],
    'msg': NotRequired[str],
}, total=False)

ModelInstagramReelsResponseDoc = TypedDict('ModelInstagramReelsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelInstagramReelResponse],
    'msg': NotRequired[str],
}, total=False)

ModelJustwatchAgeCertification = TypedDict('ModelJustwatchAgeCertification', {
    'technical_name': NotRequired[str],
}, total=False)

ModelJustwatchAgeCertificationsResponse = TypedDict('ModelJustwatchAgeCertificationsResponse', {
    'age_certifications': NotRequired[list[ModelJustwatchAgeCertification]],
    'country': NotRequired[str],
}, total=False)

ModelJustwatchAnalysisResponse = TypedDict('ModelJustwatchAnalysisResponse', {
    'summary': NotRequired[ModelJustwatchAnalysisSummary],
    'title': NotRequired[ModelJustwatchTitleResponse],
}, total=False)

ModelJustwatchAnalysisSummary = TypedDict('ModelJustwatchAnalysisSummary', {
    'available': NotRequired[bool],
    'best_buy': NotRequired[ModelJustwatchOffer],
    'best_free': NotRequired[ModelJustwatchOffer],
    'best_rent': NotRequired[ModelJustwatchOffer],
    'best_subscription': NotRequired[ModelJustwatchOffer],
    'format_counts': NotRequired[dict[str, int]],
    'monetization_counts': NotRequired[dict[str, int]],
    'price_ranges': NotRequired[dict[str, ModelJustwatchPriceRange]],
    'provider_count': NotRequired[int],
    'total_offers': NotRequired[int],
}, total=False)

ModelJustwatchBackdrop = TypedDict('ModelJustwatchBackdrop', {
    'url': NotRequired[str],
}, total=False)

ModelJustwatchClip = TypedDict('ModelJustwatchClip', {
    'external_id': NotRequired[str],
    'provider': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelJustwatchCredit = TypedDict('ModelJustwatchCredit', {
    'character_name': NotRequired[str],
    'name': NotRequired[str],
    'person_id': NotRequired[int],
    'role': NotRequired[str],
}, total=False)

ModelJustwatchDiscoverResponse = TypedDict('ModelJustwatchDiscoverResponse', {
    'country': NotRequired[str],
    'genres': NotRequired[list[str]],
    'language': NotRequired[str],
    'monetization_types': NotRequired[list[str]],
    'providers': NotRequired[list[str]],
    'results': NotRequired[list[ModelJustwatchSearchTitle]],
    'type': NotRequired[str],
    'year_max': NotRequired[int],
    'year_min': NotRequired[int],
}, total=False)

ModelJustwatchEpisodeByIdresponse = TypedDict('ModelJustwatchEpisodeByIdresponse', {
    'country': NotRequired[str],
    'episode': NotRequired[ModelJustwatchEpisodeSummary],
    'language': NotRequired[str],
}, total=False)

ModelJustwatchEpisodeCountryOffers = TypedDict('ModelJustwatchEpisodeCountryOffers', {
    'country': NotRequired[str],
    'episode': NotRequired[ModelJustwatchEpisodeSummary],
    'offers': NotRequired[list[ModelJustwatchOffer]],
}, total=False)

ModelJustwatchEpisodeOffersResponse = TypedDict('ModelJustwatchEpisodeOffersResponse', {
    'countries': NotRequired[list[ModelJustwatchEpisodeCountryOffers]],
    'id': NotRequired[str],
    'language': NotRequired[str],
}, total=False)

ModelJustwatchEpisodeSummary = TypedDict('ModelJustwatchEpisodeSummary', {
    'description': NotRequired[str],
    'episode_number': NotRequired[int],
    'id': NotRequired[str],
    'object_id': NotRequired[int],
    'object_type': NotRequired[str],
    'offers': NotRequired[list[ModelJustwatchOffer]],
    'path': NotRequired[str],
    'poster_url': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'year': NotRequired[int],
}, total=False)

ModelJustwatchGenre = TypedDict('ModelJustwatchGenre', {
    'short_name': NotRequired[str],
    'translation': NotRequired[str],
}, total=False)

ModelJustwatchGenreTitlesResponse = TypedDict('ModelJustwatchGenreTitlesResponse', {
    'country': NotRequired[str],
    'genre': NotRequired[str],
    'language': NotRequired[str],
    'results': NotRequired[list[ModelJustwatchSearchTitle]],
    'type': NotRequired[str],
}, total=False)

ModelJustwatchGenresResponse = TypedDict('ModelJustwatchGenresResponse', {
    'genres': NotRequired[list[ModelJustwatchGenre]],
    'language': NotRequired[str],
}, total=False)

ModelJustwatchMonetizationTitlesResponse = TypedDict('ModelJustwatchMonetizationTitlesResponse', {
    'country': NotRequired[str],
    'language': NotRequired[str],
    'monetization_type': NotRequired[str],
    'results': NotRequired[list[ModelJustwatchSearchTitle]],
    'type': NotRequired[str],
}, total=False)

ModelJustwatchNewTitlesResponse = TypedDict('ModelJustwatchNewTitlesResponse', {
    'country': NotRequired[str],
    'language': NotRequired[str],
    'results': NotRequired[list[ModelJustwatchSearchTitle]],
    'type': NotRequired[str],
}, total=False)

ModelJustwatchOffer = TypedDict('ModelJustwatchOffer', {
    'availability': NotRequired[str],
    'category': NotRequired[str],
    'currency': NotRequired[str],
    'monetization_type': NotRequired[str],
    'presentation_type': NotRequired[str],
    'price': NotRequired[float],
    'provider': NotRequired[str],
    'provider_id': NotRequired[int],
    'provider_short': NotRequired[str],
    'provider_technical': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelJustwatchPopularResponse = TypedDict('ModelJustwatchPopularResponse', {
    'country': NotRequired[str],
    'language': NotRequired[str],
    'results': NotRequired[list[ModelJustwatchSearchTitle]],
    'type': NotRequired[str],
}, total=False)

ModelJustwatchPriceRange = TypedDict('ModelJustwatchPriceRange', {
    'currency': NotRequired[str],
    'max': NotRequired[float],
    'min': NotRequired[float],
}, total=False)

ModelJustwatchProvider = TypedDict('ModelJustwatchProvider', {
    'clear_name': NotRequired[str],
    'icon_url': NotRequired[str],
    'id': NotRequired[int],
    'short_name': NotRequired[str],
    'technical_name': NotRequired[str],
}, total=False)

ModelJustwatchProviderTitlesResponse = TypedDict('ModelJustwatchProviderTitlesResponse', {
    'country': NotRequired[str],
    'language': NotRequired[str],
    'provider': NotRequired[str],
    'results': NotRequired[list[ModelJustwatchSearchTitle]],
    'type': NotRequired[str],
}, total=False)

ModelJustwatchProvidersResponse = TypedDict('ModelJustwatchProvidersResponse', {
    'country': NotRequired[str],
    'providers': NotRequired[list[ModelJustwatchProvider]],
}, total=False)

ModelJustwatchScoring = TypedDict('ModelJustwatchScoring', {
    'best_rating': NotRequired[str],
    'certified_fresh': NotRequired[bool],
    'imdb_score': NotRequired[float],
    'imdb_votes': NotRequired[int],
    'justwatch_rating': NotRequired[float],
    'rating_count': NotRequired[int],
    'tmdb_popularity': NotRequired[float],
    'tmdb_score': NotRequired[float],
    'tomato_meter': NotRequired[int],
}, total=False)

ModelJustwatchSearchResponse = TypedDict('ModelJustwatchSearchResponse', {
    'country': NotRequired[str],
    'language': NotRequired[str],
    'query': NotRequired[str],
    'results': NotRequired[list[ModelJustwatchSearchTitle]],
}, total=False)

ModelJustwatchSearchTitle = TypedDict('ModelJustwatchSearchTitle', {
    'id': NotRequired[str],
    'object_id': NotRequired[int],
    'object_type': NotRequired[str],
    'offers': NotRequired[list[ModelJustwatchOffer]],
    'path': NotRequired[str],
    'poster_url': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'year': NotRequired[int],
}, total=False)

ModelJustwatchSeasonByIdresponse = TypedDict('ModelJustwatchSeasonByIdresponse', {
    'country': NotRequired[str],
    'language': NotRequired[str],
    'season': NotRequired[ModelJustwatchSeasonSummary],
}, total=False)

ModelJustwatchSeasonEpisodesResponse = TypedDict('ModelJustwatchSeasonEpisodesResponse', {
    'country': NotRequired[str],
    'episodes': NotRequired[list[ModelJustwatchEpisodeSummary]],
    'language': NotRequired[str],
    'season': NotRequired[ModelJustwatchSeasonSummary],
}, total=False)

ModelJustwatchSeasonSummary = TypedDict('ModelJustwatchSeasonSummary', {
    'description': NotRequired[str],
    'id': NotRequired[str],
    'object_id': NotRequired[int],
    'object_type': NotRequired[str],
    'path': NotRequired[str],
    'poster_url': NotRequired[str],
    'season_number': NotRequired[int],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'year': NotRequired[int],
}, total=False)

ModelJustwatchShowSeasonsResponse = TypedDict('ModelJustwatchShowSeasonsResponse', {
    'country': NotRequired[str],
    'language': NotRequired[str],
    'seasons': NotRequired[list[ModelJustwatchSeasonSummary]],
    'show': NotRequired[ModelJustwatchTitleResponse],
}, total=False)

ModelJustwatchSimilarTitlesResponse = TypedDict('ModelJustwatchSimilarTitlesResponse', {
    'country': NotRequired[str],
    'id': NotRequired[str],
    'language': NotRequired[str],
    'results': NotRequired[list[ModelJustwatchSearchTitle]],
}, total=False)

ModelJustwatchTitleCountryOffers = TypedDict('ModelJustwatchTitleCountryOffers', {
    'country': NotRequired[str],
    'offers': NotRequired[list[ModelJustwatchOffer]],
    'title': NotRequired[ModelJustwatchTitleResponse],
}, total=False)

ModelJustwatchTitleMediaResponse = TypedDict('ModelJustwatchTitleMediaResponse', {
    'backdrops': NotRequired[list[ModelJustwatchBackdrop]],
    'clips': NotRequired[list[ModelJustwatchClip]],
    'country': NotRequired[str],
    'credits': NotRequired[list[ModelJustwatchCredit]],
    'id': NotRequired[str],
    'language': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelJustwatchTitleOffersResponse = TypedDict('ModelJustwatchTitleOffersResponse', {
    'countries': NotRequired[list[ModelJustwatchTitleCountryOffers]],
    'id': NotRequired[str],
    'language': NotRequired[str],
}, total=False)

ModelJustwatchTitleResponse = TypedDict('ModelJustwatchTitleResponse', {
    'content_rating': NotRequired[str],
    'description': NotRequired[str],
    'genres': NotRequired[list[str]],
    'id': NotRequired[str],
    'object_id': NotRequired[int],
    'object_type': NotRequired[str],
    'offers': NotRequired[list[ModelJustwatchOffer]],
    'path': NotRequired[str],
    'poster_url': NotRequired[str],
    'release_date': NotRequired[str],
    'runtime': NotRequired[str],
    'scoring': NotRequired[ModelJustwatchScoring],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'year': NotRequired[int],
}, total=False)

ModelJustwatchAgeCertificationsResponseDoc = TypedDict('ModelJustwatchAgeCertificationsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJustwatchAgeCertificationsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelJustwatchAnalysisResponseDoc = TypedDict('ModelJustwatchAnalysisResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJustwatchAnalysisResponse],
    'msg': NotRequired[str],
}, total=False)

ModelJustwatchDiscoverResponseDoc = TypedDict('ModelJustwatchDiscoverResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJustwatchDiscoverResponse],
    'msg': NotRequired[str],
}, total=False)

ModelJustwatchEpisodeByIdresponseDoc = TypedDict('ModelJustwatchEpisodeByIdresponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJustwatchEpisodeByIdresponse],
    'msg': NotRequired[str],
}, total=False)

ModelJustwatchEpisodeOffersResponseDoc = TypedDict('ModelJustwatchEpisodeOffersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJustwatchEpisodeOffersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelJustwatchGenreTitlesResponseDoc = TypedDict('ModelJustwatchGenreTitlesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJustwatchGenreTitlesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelJustwatchGenresResponseDoc = TypedDict('ModelJustwatchGenresResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJustwatchGenresResponse],
    'msg': NotRequired[str],
}, total=False)

ModelJustwatchMonetizationTitlesResponseDoc = TypedDict('ModelJustwatchMonetizationTitlesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJustwatchMonetizationTitlesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelJustwatchNewTitlesResponseDoc = TypedDict('ModelJustwatchNewTitlesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJustwatchNewTitlesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelJustwatchPopularResponseDoc = TypedDict('ModelJustwatchPopularResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJustwatchPopularResponse],
    'msg': NotRequired[str],
}, total=False)

ModelJustwatchProviderTitlesResponseDoc = TypedDict('ModelJustwatchProviderTitlesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJustwatchProviderTitlesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelJustwatchProvidersResponseDoc = TypedDict('ModelJustwatchProvidersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJustwatchProvidersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelJustwatchSearchResponseDoc = TypedDict('ModelJustwatchSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJustwatchSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelJustwatchSeasonByIdresponseDoc = TypedDict('ModelJustwatchSeasonByIdresponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJustwatchSeasonByIdresponse],
    'msg': NotRequired[str],
}, total=False)

ModelJustwatchSeasonEpisodesResponseDoc = TypedDict('ModelJustwatchSeasonEpisodesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJustwatchSeasonEpisodesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelJustwatchShowSeasonsResponseDoc = TypedDict('ModelJustwatchShowSeasonsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJustwatchShowSeasonsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelJustwatchSimilarTitlesResponseDoc = TypedDict('ModelJustwatchSimilarTitlesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJustwatchSimilarTitlesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelJustwatchTitleMediaResponseDoc = TypedDict('ModelJustwatchTitleMediaResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJustwatchTitleMediaResponse],
    'msg': NotRequired[str],
}, total=False)

ModelJustwatchTitleOffersResponseDoc = TypedDict('ModelJustwatchTitleOffersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJustwatchTitleOffersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelJustwatchTitleResponseDoc = TypedDict('ModelJustwatchTitleResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelJustwatchTitleResponse],
    'msg': NotRequired[str],
}, total=False)

ModelLinkedinCustomer = TypedDict('ModelLinkedinCustomer', {
    'follower_count': NotRequired[int],
    'industry': NotRequired[str],
    'link': NotRequired[str],
    'logo': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelLinkedinLinkedinCompanyResponse = TypedDict('ModelLinkedinLinkedinCompanyResponse', {
    'about': NotRequired[str],
    'affiliated_pages': NotRequired[list[ModelLinkedinPage]],
    'company_size': NotRequired[str],
    'follower_count': NotRequired[int],
    'founded_on': NotRequired[int],
    'headline': NotRequired[str],
    'headquarters': NotRequired[str],
    'industry': NotRequired[str],
    'link': NotRequired[str],
    'locations': NotRequired[list[ModelLinkedinLocation]],
    'logo': NotRequired[str],
    'name': NotRequired[str],
    'num_of_employees_on_linkedin': NotRequired[int],
    'similar_pages': NotRequired[list[ModelLinkedinPage]],
    'specialties': NotRequired[str],
    'type': NotRequired[str],
    'updates': NotRequired[list[ModelLinkedinUpdate]],
    'website': NotRequired[str],
}, total=False)

ModelLinkedinLinkedinProductResponse = TypedDict('ModelLinkedinLinkedinProductResponse', {
    'about': NotRequired[str],
    'category_link': NotRequired[str],
    'category_name': NotRequired[str],
    'cover_image': NotRequired[str],
    'external_link': NotRequired[str],
    'featured_customers': NotRequired[list[ModelLinkedinCustomer]],
    'link': NotRequired[str],
    'logo': NotRequired[str],
    'medias': NotRequired[list[ModelLinkedinMedia]],
    'name': NotRequired[str],
    'organization_link': NotRequired[str],
    'organization_name': NotRequired[str],
    'other_products': NotRequired[list[ModelLinkedinProduct]],
    'similar_products': NotRequired[list[ModelLinkedinProduct]],
}, total=False)

ModelLinkedinLocation = TypedDict('ModelLinkedinLocation', {
    'address': NotRequired[str],
    'is_primary': NotRequired[bool],
}, total=False)

ModelLinkedinMedia = TypedDict('ModelLinkedinMedia', {
    'link': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelLinkedinPage = TypedDict('ModelLinkedinPage', {
    'address': NotRequired[str],
    'industry': NotRequired[str],
    'link': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelLinkedinProduct = TypedDict('ModelLinkedinProduct', {
    'category_link': NotRequired[str],
    'category_name': NotRequired[str],
    'link': NotRequired[str],
    'logo': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelLinkedinUpdate = TypedDict('ModelLinkedinUpdate', {
    'author': NotRequired[str],
    'author_link': NotRequired[str],
    'images': NotRequired[list[str]],
    'is_reposted': NotRequired[bool],
    'logo': NotRequired[str],
    'num_of_comments': NotRequired[int],
    'num_of_reactions': NotRequired[int],
    'post_link': NotRequired[str],
    'published_at': NotRequired[str],
    'summary': NotRequired[str],
    'videos': NotRequired[list[str]],
}, total=False)

ModelLinkedinCompanyResponseDoc = TypedDict('ModelLinkedinCompanyResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelLinkedinLinkedinCompanyResponse],
    'msg': NotRequired[str],
}, total=False)

ModelLinkedinProductResponseDoc = TypedDict('ModelLinkedinProductResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelLinkedinLinkedinProductResponse],
    'msg': NotRequired[str],
}, total=False)

ModelLinkedinShowcaseResponseDoc = TypedDict('ModelLinkedinShowcaseResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelLinkedinLinkedinCompanyResponse],
    'msg': NotRequired[str],
}, total=False)

ModelPopularTrendCountryIndustryMeta = TypedDict('ModelPopularTrendCountryIndustryMeta', {
    'country': NotRequired[list[ModelPopularTrendCountryIndustryMetaItem]],
    'industry': NotRequired[list[ModelPopularTrendCountryIndustryMetaItem]],
}, total=False)

ModelPopularTrendCountryIndustryMetaItem = TypedDict('ModelPopularTrendCountryIndustryMetaItem', {
    'id': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelPopularTrendCreatorTrendResp = TypedDict('ModelPopularTrendCreatorTrendResp', {
    'code': NotRequired[int],
    'data': NotRequired[dict[str, Any]],
    'msg': NotRequired[str],
    'request_id': NotRequired[str],
}, total=False)

ModelPopularTrendTopAdsAnalysisPoint = TypedDict('ModelPopularTrendTopAdsAnalysisPoint', {
    'second': NotRequired[int],
    'value': NotRequired[float],
}, total=False)

ModelPopularTrendTopAdsAnalysisResp = TypedDict('ModelPopularTrendTopAdsAnalysisResp', {
    'code': NotRequired[int],
    'data': NotRequired[dict[str, Any]],
    'msg': NotRequired[str],
    'request_id': NotRequired[str],
}, total=False)

ModelPopularTrendTopAdsDetailResp = TypedDict('ModelPopularTrendTopAdsDetailResp', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendTopAdsMaterial],
    'msg': NotRequired[str],
    'request_id': NotRequired[str],
}, total=False)

ModelPopularTrendTopAdsFilterItem = TypedDict('ModelPopularTrendTopAdsFilterItem', {
    'has_conversion': NotRequired[bool],
    'id': NotRequired[dict[str, Any]],
    'label': NotRequired[str],
    'parent_id': NotRequired[dict[str, Any]],
    'value': NotRequired[str],
}, total=False)

ModelPopularTrendTopAdsFiltersResp = TypedDict('ModelPopularTrendTopAdsFiltersResp', {
    'code': NotRequired[int],
    'data': NotRequired[dict[str, Any]],
    'msg': NotRequired[str],
    'request_id': NotRequired[str],
}, total=False)

ModelPopularTrendTopAdsListResp = TypedDict('ModelPopularTrendTopAdsListResp', {
    'code': NotRequired[int],
    'data': NotRequired[dict[str, Any]],
    'msg': NotRequired[str],
    'request_id': NotRequired[str],
}, total=False)

ModelPopularTrendTopAdsLocationInfoResp = TypedDict('ModelPopularTrendTopAdsLocationInfoResp', {
    'code': NotRequired[int],
    'data': NotRequired[dict[str, Any]],
    'msg': NotRequired[str],
    'request_id': NotRequired[str],
}, total=False)

ModelPopularTrendTopAdsLocationsResp = TypedDict('ModelPopularTrendTopAdsLocationsResp', {
    'code': NotRequired[int],
    'data': NotRequired[dict[str, Any]],
    'msg': NotRequired[str],
    'request_id': NotRequired[str],
}, total=False)

ModelPopularTrendTopAdsMaterial = TypedDict('ModelPopularTrendTopAdsMaterial', {
    'ad_title': NotRequired[str],
    'brand_name': NotRequired[str],
    'comment': NotRequired[int],
    'cost': NotRequired[int],
    'country_code': NotRequired[list[str]],
    'ctr': NotRequired[float],
    'favorite': NotRequired[bool],
    'has_summary': NotRequired[bool],
    'highlight': NotRequired[str],
    'highlight_text': NotRequired[str],
    'id': NotRequired[str],
    'industry_key': NotRequired[str],
    'is_search': NotRequired[bool],
    'keyword_list': NotRequired[list[str]],
    'landing_page': NotRequired[str],
    'like': NotRequired[int],
    'objective_key': NotRequired[str],
    'objectives': NotRequired[list[ModelPopularTrendTopAdsFilterItem]],
    'pattern_label': NotRequired[list[ModelPopularTrendTopAdsFilterItem]],
    'share': NotRequired[int],
    'source': NotRequired[str],
    'source_key': NotRequired[int],
    'video_info': NotRequired[ModelPopularTrendTopAdsVideoInfo],
    'voice_over': NotRequired[bool],
}, total=False)

ModelPopularTrendTopAdsPagination = TypedDict('ModelPopularTrendTopAdsPagination', {
    'has_more': NotRequired[bool],
    'page': NotRequired[int],
    'size': NotRequired[int],
    'total': NotRequired[int],
    'total_count': NotRequired[int],
}, total=False)

ModelPopularTrendTopAdsRecommendResp = TypedDict('ModelPopularTrendTopAdsRecommendResp', {
    'code': NotRequired[int],
    'data': NotRequired[dict[str, Any]],
    'msg': NotRequired[str],
    'request_id': NotRequired[str],
}, total=False)

ModelPopularTrendTopAdsSafetyResp = TypedDict('ModelPopularTrendTopAdsSafetyResp', {
    'code': NotRequired[int],
    'data': NotRequired[dict[str, Any]],
    'msg': NotRequired[str],
    'request_id': NotRequired[str],
}, total=False)

ModelPopularTrendTopAdsSpotlightResp = TypedDict('ModelPopularTrendTopAdsSpotlightResp', {
    'code': NotRequired[int],
    'data': NotRequired[dict[str, Any]],
    'msg': NotRequired[str],
    'request_id': NotRequired[str],
}, total=False)

ModelPopularTrendTopAdsSuggestionsResp = TypedDict('ModelPopularTrendTopAdsSuggestionsResp', {
    'code': NotRequired[int],
    'data': NotRequired[dict[str, Any]],
    'msg': NotRequired[str],
    'request_id': NotRequired[str],
}, total=False)

ModelPopularTrendTopAdsVideoInfo = TypedDict('ModelPopularTrendTopAdsVideoInfo', {
    'cover': NotRequired[str],
    'duration': NotRequired[float],
    'height': NotRequired[int],
    'vid': NotRequired[str],
    'video_url': NotRequired[dict[str, str]],
    'width': NotRequired[int],
}, total=False)

ModelPopulartrendCountryIndustryMetaResponseDoc = TypedDict('ModelPopulartrendCountryIndustryMetaResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendCountryIndustryMeta],
    'msg': NotRequired[str],
}, total=False)

ModelPopulartrendCreatorTrendResponseDoc = TypedDict('ModelPopulartrendCreatorTrendResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendCreatorTrendResp],
    'msg': NotRequired[str],
}, total=False)

ModelPopulartrendTopAdsAnalysisResponseDoc = TypedDict('ModelPopulartrendTopAdsAnalysisResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendTopAdsAnalysisResp],
    'msg': NotRequired[str],
}, total=False)

ModelPopulartrendTopAdsDetailResponseDoc = TypedDict('ModelPopulartrendTopAdsDetailResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendTopAdsDetailResp],
    'msg': NotRequired[str],
}, total=False)

ModelPopulartrendTopAdsFiltersResponseDoc = TypedDict('ModelPopulartrendTopAdsFiltersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendTopAdsFiltersResp],
    'msg': NotRequired[str],
}, total=False)

ModelPopulartrendTopAdsListResponseDoc = TypedDict('ModelPopulartrendTopAdsListResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendTopAdsListResp],
    'msg': NotRequired[str],
}, total=False)

ModelPopulartrendTopAdsLocationInfoResponseDoc = TypedDict('ModelPopulartrendTopAdsLocationInfoResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendTopAdsLocationInfoResp],
    'msg': NotRequired[str],
}, total=False)

ModelPopulartrendTopAdsLocationsResponseDoc = TypedDict('ModelPopulartrendTopAdsLocationsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendTopAdsLocationsResp],
    'msg': NotRequired[str],
}, total=False)

ModelPopulartrendTopAdsRecommendResponseDoc = TypedDict('ModelPopulartrendTopAdsRecommendResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendTopAdsRecommendResp],
    'msg': NotRequired[str],
}, total=False)

ModelPopulartrendTopAdsSafetyResponseDoc = TypedDict('ModelPopulartrendTopAdsSafetyResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendTopAdsSafetyResp],
    'msg': NotRequired[str],
}, total=False)

ModelPopulartrendTopAdsSpotlightResponseDoc = TypedDict('ModelPopulartrendTopAdsSpotlightResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendTopAdsSpotlightResp],
    'msg': NotRequired[str],
}, total=False)

ModelPopulartrendTopAdsSuggestionsResponseDoc = TypedDict('ModelPopulartrendTopAdsSuggestionsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendTopAdsSuggestionsResp],
    'msg': NotRequired[str],
}, total=False)

ModelProducthuntLeaderboardAdItem = TypedDict('ModelProducthuntLeaderboardAdItem', {
    'channel_kind': NotRequired[str],
    'id': NotRequired[str],
    'large_asset_uuid': NotRequired[str],
    'name': NotRequired[str],
    'post': NotRequired[ModelProducthuntLeaderboardAdPost],
    'small_asset_uuid': NotRequired[str],
    'subject': NotRequired[str],
    'tagline': NotRequired[str],
    'thumbnail_uuid': NotRequired[str],
    'url': NotRequired[str],
    'variation_id': NotRequired[str],
}, total=False)

ModelProducthuntLeaderboardAdPost = TypedDict('ModelProducthuntLeaderboardAdPost', {
    'comments_count': NotRequired[int],
    'created_at': NotRequired[str],
    'disabled_when_scheduled': NotRequired[bool],
    'embargo_preview_at': NotRequired[str],
    'featured_at': NotRequired[str],
    'featured_comment': NotRequired[ModelProducthuntProductCategoryAdComment],
    'has_voted': NotRequired[bool],
    'hide_votes_count': NotRequired[bool],
    'id': NotRequired[str],
    'latest_score': NotRequired[int],
    'launch_day_score': NotRequired[int],
    'name': NotRequired[str],
    'product': NotRequired[ModelProducthuntLeaderboardProductRef],
    'randomization_status': NotRequired[ModelProducthuntLeaderboardRandomizationStatus],
    'slug': NotRequired[str],
    'topics': NotRequired[list[ModelProducthuntLeaderboardTopic]],
    'updated_at': NotRequired[str],
}, total=False)

ModelProducthuntLeaderboardGhostItem = TypedDict('ModelProducthuntLeaderboardGhostItem', {
    'id': NotRequired[str],
    'subject': NotRequired[str],
}, total=False)

ModelProducthuntLeaderboardItem = TypedDict('ModelProducthuntLeaderboardItem', {
    'ad': NotRequired[ModelProducthuntLeaderboardAdItem],
    'ghost_ad': NotRequired[ModelProducthuntLeaderboardGhostItem],
    'post': NotRequired[ModelProducthuntLeaderboardPostItem],
    'type': NotRequired[str],
}, total=False)

ModelProducthuntLeaderboardPage = TypedDict('ModelProducthuntLeaderboardPage', {
    'connection': NotRequired[str],
    'day': NotRequired[int],
    'end_cursor': NotRequired[str],
    'featured': NotRequired[bool],
    'golden_kitty_years': NotRequired[list[int]],
    'has_next_page': NotRequired[bool],
    'items': NotRequired[list[ModelProducthuntLeaderboardItem]],
    'month': NotRequired[int],
    'order': NotRequired[str],
    'raw_page_info': NotRequired[dict[str, Any]],
    'scope': NotRequired[str],
    'total_count': NotRequired[int],
    'week': NotRequired[int],
    'year': NotRequired[int],
}, total=False)

ModelProducthuntLeaderboardPostItem = TypedDict('ModelProducthuntLeaderboardPostItem', {
    'comments_count': NotRequired[int],
    'created_at': NotRequired[str],
    'daily_rank': NotRequired[int],
    'disabled_when_scheduled': NotRequired[bool],
    'embargo_preview_at': NotRequired[str],
    'featured_at': NotRequired[str],
    'friend_voters_count': NotRequired[int],
    'has_voted': NotRequired[bool],
    'hide_votes_count': NotRequired[bool],
    'id': NotRequired[str],
    'is_subscribed': NotRequired[bool],
    'latest_score': NotRequired[int],
    'launch_day_score': NotRequired[int],
    'monthly_rank': NotRequired[int],
    'name': NotRequired[str],
    'product': NotRequired[ModelProducthuntLeaderboardProductRef],
    'product_state': NotRequired[str],
    'randomization_status': NotRequired[ModelProducthuntLeaderboardRandomizationStatus],
    'scheduled_at': NotRequired[str],
    'shortened_url': NotRequired[str],
    'slug': NotRequired[str],
    'tagline': NotRequired[str],
    'thumbnail_image_uuid': NotRequired[str],
    'topics': NotRequired[list[ModelProducthuntLeaderboardTopic]],
    'updated_at': NotRequired[str],
    'weekly_rank': NotRequired[int],
}, total=False)

ModelProducthuntLeaderboardProductRef = TypedDict('ModelProducthuntLeaderboardProductRef', {
    'id': NotRequired[str],
    'is_no_longer_online': NotRequired[bool],
    'is_subscribed': NotRequired[bool],
    'is_top_product': NotRequired[bool],
    'logo_uuid': NotRequired[str],
    'name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelProducthuntLeaderboardRandomizationStatus = TypedDict('ModelProducthuntLeaderboardRandomizationStatus', {
    'active': NotRequired[bool],
    'next_transition_at': NotRequired[str],
    'random_day': NotRequired[bool],
    'randomize_order': NotRequired[bool],
}, total=False)

ModelProducthuntLeaderboardTopic = TypedDict('ModelProducthuntLeaderboardTopic', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelProducthuntProduct = TypedDict('ModelProducthuntProduct', {
    'categories': NotRequired[list[str]],
    'daily_rank': NotRequired[int],
    'date_published': NotRequired[str],
    'description': NotRequired[str],
    'followers_count': NotRequired[int],
    'id': NotRequired[str],
    'monthly_rank': NotRequired[int],
    'name': NotRequired[str],
    'rating': NotRequired[float],
    'review_count': NotRequired[int],
    'similar_products': NotRequired[list[ModelProducthuntSimilarProduct]],
    'social_links': NotRequired[list[str]],
    'tagline': NotRequired[str],
    'website': NotRequired[str],
    'weekly_rank': NotRequired[int],
}, total=False)

ModelProducthuntProductAboutAd = TypedDict('ModelProducthuntProductAboutAd', {
    'channel_kind': NotRequired[str],
    'id': NotRequired[str],
    'large_asset_uuid': NotRequired[str],
    'name': NotRequired[str],
    'small_asset_uuid': NotRequired[str],
    'subject': NotRequired[str],
    'tagline': NotRequired[str],
    'thumbnail_uuid': NotRequired[str],
    'url': NotRequired[str],
    'variation_id': NotRequired[str],
}, total=False)

ModelProducthuntProductAboutDiscussionForum = TypedDict('ModelProducthuntProductAboutDiscussionForum', {
    'id': NotRequired[str],
    'path': NotRequired[str],
    'threads': NotRequired[list[ModelProducthuntProductAboutDiscussionThread]],
    'total_count': NotRequired[int],
}, total=False)

ModelProducthuntProductAboutDiscussionThread = TypedDict('ModelProducthuntProductAboutDiscussionThread', {
    'commentable_id': NotRequired[str],
    'comments_count': NotRequired[int],
    'created_at': NotRequired[str],
    'description_preview': NotRequired[str],
    'forum': NotRequired[ModelProducthuntProductAboutForumRef],
    'has_voted': NotRequired[bool],
    'id': NotRequired[str],
    'is_featured': NotRequired[bool],
    'is_pinned': NotRequired[bool],
    'path': NotRequired[str],
    'slug': NotRequired[str],
    'title': NotRequired[str],
    'user': NotRequired[ModelProducthuntProductCategoryUser],
    'votes_count': NotRequired[int],
}, total=False)

ModelProducthuntProductAboutForumRef = TypedDict('ModelProducthuntProductAboutForumRef', {
    'id': NotRequired[str],
    'path': NotRequired[str],
    'slug': NotRequired[str],
    'subject': NotRequired[ModelProducthuntProductAboutForumSubject],
}, total=False)

ModelProducthuntProductAboutForumSubject = TypedDict('ModelProducthuntProductAboutForumSubject', {
    'id': NotRequired[str],
    'is_no_longer_online': NotRequired[bool],
    'logo_uuid': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelProducthuntProductAboutGhostAd = TypedDict('ModelProducthuntProductAboutGhostAd', {
    'id': NotRequired[str],
    'subject': NotRequired[str],
}, total=False)

ModelProducthuntProductAboutLatestLaunch = TypedDict('ModelProducthuntProductAboutLatestLaunch', {
    'id': NotRequired[str],
    'is_maker': NotRequired[bool],
    'launch_number': NotRequired[int],
    'launched_this_week': NotRequired[bool],
    'launching_today': NotRequired[bool],
    'name': NotRequired[str],
    'product_state': NotRequired[str],
    'scheduled_at': NotRequired[str],
    'slug': NotRequired[str],
    'tagline': NotRequired[str],
    'thumbnail_image_uuid': NotRequired[str],
}, total=False)

ModelProducthuntProductAboutLaunch = TypedDict('ModelProducthuntProductAboutLaunch', {
    'ad1': NotRequired[ModelProducthuntProductAboutGhostAd],
    'ad2': NotRequired[ModelProducthuntProductAboutGhostAd],
    'badges': NotRequired[list[ModelProducthuntProductCategoryListBadge]],
    'can_deputy_manage': NotRequired[bool],
    'can_manage': NotRequired[bool],
    'comments_count': NotRequired[int],
    'created_at': NotRequired[str],
    'daily_rank': NotRequired[int],
    'description': NotRequired[str],
    'detailed_reviews': NotRequired[list[ModelProducthuntProductAboutShoutout]],
    'disabled_when_scheduled': NotRequired[bool],
    'embargo_preview_at': NotRequired[str],
    'featured': NotRequired[bool],
    'featured_at': NotRequired[str],
    'has_voted': NotRequired[bool],
    'hide_votes_count': NotRequired[bool],
    'id': NotRequired[str],
    'is_archived': NotRequired[bool],
    'is_available': NotRequired[bool],
    'is_hunter': NotRequired[bool],
    'is_maker': NotRequired[bool],
    'is_top_launch': NotRequired[bool],
    'latest_score': NotRequired[int],
    'launch_day_score': NotRequired[int],
    'launch_number': NotRequired[int],
    'launch_state': NotRequired[str],
    'launched_this_week': NotRequired[bool],
    'launching_today': NotRequired[bool],
    'links': NotRequired[list[ModelProducthuntProductAboutLink]],
    'makers': NotRequired[list[ModelProducthuntProductAboutUser]],
    'media': NotRequired[list[ModelProducthuntProductAboutMedia]],
    'meta': NotRequired[ModelProducthuntProductAboutMeta],
    'moderation_reason': NotRequired[str],
    'name': NotRequired[str],
    'pricing_type': NotRequired[str],
    'primary_link': NotRequired[ModelProducthuntProductAboutPrimaryLink],
    'product': NotRequired[ModelProducthuntProductAboutLaunchProduct],
    'product_state': NotRequired[str],
    'promo': NotRequired[dict[str, Any]],
    'redirect_to_product': NotRequired[ModelProducthuntLeaderboardProductRef],
    'scheduled_at': NotRequired[str],
    'slug': NotRequired[str],
    'tagline': NotRequired[str],
    'thumbnail_image_uuid': NotRequired[str],
    'topics': NotRequired[list[ModelProducthuntProductCategoryRef]],
    'trashed_at': NotRequired[str],
    'updated_at': NotRequired[str],
    'url': NotRequired[str],
    'user': NotRequired[ModelProducthuntProductAboutUser],
    'weekly_rank': NotRequired[int],
}, total=False)

ModelProducthuntProductAboutLaunchFlags = TypedDict('ModelProducthuntProductAboutLaunchFlags', {
    'id': NotRequired[str],
    'launched_this_week': NotRequired[bool],
    'launching_today': NotRequired[bool],
}, total=False)

ModelProducthuntProductAboutLaunchProduct = TypedDict('ModelProducthuntProductAboutLaunchProduct', {
    'can_claim': NotRequired[bool],
    'can_edit': NotRequired[bool],
    'clean_url': NotRequired[str],
    'detailed_review': NotRequired[dict[str, Any]],
    'first_launch': NotRequired[bool],
    'id': NotRequired[str],
    'is_claimed': NotRequired[bool],
    'is_no_longer_online': NotRequired[bool],
    'is_subscribed': NotRequired[bool],
    'is_top_product': NotRequired[bool],
    'is_viewer_team_member': NotRequired[dict[str, Any]],
    'latest_launch': NotRequired[ModelProducthuntProductAboutLaunchFlags],
    'logo_uuid': NotRequired[str],
    'name': NotRequired[str],
    'posts_count': NotRequired[int],
    'pro_con_tags': NotRequired[list[ModelProducthuntProductDetailedReviewTag]],
    'review_questions': NotRequired[list[ModelProducthuntProductAboutReviewQuestion]],
    'reviews_rating': NotRequired[float],
    'slug': NotRequired[str],
    'tagline': NotRequired[str],
    'viewer_pending_team_request': NotRequired[dict[str, Any]],
    'website_domain': NotRequired[str],
    'website_url': NotRequired[str],
}, total=False)

ModelProducthuntProductAboutLink = TypedDict('ModelProducthuntProductAboutLink', {
    'devices': NotRequired[list[str]],
    'id': NotRequired[str],
    'redirect_path': NotRequired[str],
    'store_name': NotRequired[str],
    'website_name': NotRequired[str],
}, total=False)

ModelProducthuntProductAboutMedia = TypedDict('ModelProducthuntProductAboutMedia', {
    'id': NotRequired[str],
    'image_uuid': NotRequired[str],
    'interactive_demo_id': NotRequired[str],
    'interactive_demo_type': NotRequired[str],
    'media_type': NotRequired[str],
    'original_height': NotRequired[int],
    'original_width': NotRequired[int],
    'platform': NotRequired[str],
    'thumbnail_height': NotRequired[int],
    'thumbnail_width': NotRequired[int],
    'url': NotRequired[str],
    'video_id': NotRequired[str],
}, total=False)

ModelProducthuntProductAboutMentionedProduct = TypedDict('ModelProducthuntProductAboutMentionedProduct', {
    'id': NotRequired[str],
    'is_no_longer_online': NotRequired[bool],
    'logo_uuid': NotRequired[str],
    'name': NotRequired[str],
    'path': NotRequired[str],
    'slug': NotRequired[str],
    'tagline': NotRequired[str],
}, total=False)

ModelProducthuntProductAboutMeta = TypedDict('ModelProducthuntProductAboutMeta', {
    'title': NotRequired[str],
}, total=False)

ModelProducthuntProductAboutPage = TypedDict('ModelProducthuntProductAboutPage', {
    'ad': NotRequired[ModelProducthuntProductAboutAd],
    'launch': NotRequired[ModelProducthuntProductAboutLaunch],
    'page_variant_typename': NotRequired[str],
    'product': NotRequired[ModelProducthuntProductAboutProduct],
    'product_id': NotRequired[str],
    'viewer': NotRequired[ModelProducthuntProductAboutViewer],
}, total=False)

ModelProducthuntProductAboutPageVariant = TypedDict('ModelProducthuntProductAboutPageVariant', {
    'launch_id': NotRequired[str],
    'typename': NotRequired[str],
}, total=False)

ModelProducthuntProductAboutPost = TypedDict('ModelProducthuntProductAboutPost', {
    'badges': NotRequired[list[ModelProducthuntProductCategoryListBadge]],
    'comments_count': NotRequired[int],
    'created_at': NotRequired[str],
    'daily_rank': NotRequired[int],
    'disabled_when_scheduled': NotRequired[bool],
    'embargo_preview_at': NotRequired[str],
    'featured_at': NotRequired[str],
    'has_voted': NotRequired[bool],
    'hide_votes_count': NotRequired[bool],
    'id': NotRequired[str],
    'latest_score': NotRequired[int],
    'launch_day_score': NotRequired[int],
    'monthly_rank': NotRequired[int],
    'name': NotRequired[str],
    'product': NotRequired[ModelProducthuntLeaderboardProductRef],
    'product_state': NotRequired[str],
    'randomization_status': NotRequired[ModelProducthuntLeaderboardRandomizationStatus],
    'redirect_to_product': NotRequired[ModelProducthuntLeaderboardProductRef],
    'shortened_url': NotRequired[str],
    'slug': NotRequired[str],
    'tagline': NotRequired[str],
    'thumbnail_image_uuid': NotRequired[str],
    'updated_at': NotRequired[str],
    'weekly_rank': NotRequired[int],
}, total=False)

ModelProducthuntProductAboutPrimaryLink = TypedDict('ModelProducthuntProductAboutPrimaryLink', {
    'id': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelProducthuntProductAboutProduct = TypedDict('ModelProducthuntProductAboutProduct', {
    'badges': NotRequired[list[ModelProducthuntProductCategoryListBadge]],
    'detailed_review': NotRequired[dict[str, Any]],
    'discussion_forum': NotRequired[ModelProducthuntProductAboutDiscussionForum],
    'followers_count': NotRequired[int],
    'id': NotRequired[str],
    'is_no_longer_online': NotRequired[bool],
    'is_subscribed': NotRequired[bool],
    'latest_launch': NotRequired[ModelProducthuntProductAboutLatestLaunch],
    'logo_uuid': NotRequired[str],
    'media': NotRequired[list[ModelProducthuntProductAboutMedia]],
    'name': NotRequired[str],
    'page_variant': NotRequired[ModelProducthuntProductAboutPageVariant],
    'posts': NotRequired[list[ModelProducthuntProductAboutPost]],
    'posts_count': NotRequired[int],
    'pro_con_tags': NotRequired[list[ModelProducthuntProductDetailedReviewTag]],
    'review_questions': NotRequired[list[ModelProducthuntProductAboutReviewQuestion]],
    'reviews_rating': NotRequired[float],
    'screenshots': NotRequired[list[ModelProducthuntProductAboutScreenshot]],
    'slug': NotRequired[str],
    'tagline': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelProducthuntProductAboutReviewQuestion = TypedDict('ModelProducthuntProductAboutReviewQuestion', {
    'category': NotRequired[str],
    'id': NotRequired[str],
    'question': NotRequired[str],
}, total=False)

ModelProducthuntProductAboutScreenshot = TypedDict('ModelProducthuntProductAboutScreenshot', {
    'id': NotRequired[str],
    'image_uuid': NotRequired[str],
    'media_type': NotRequired[str],
    'original_height': NotRequired[int],
    'original_width': NotRequired[int],
}, total=False)

ModelProducthuntProductAboutShoutout = TypedDict('ModelProducthuntProductAboutShoutout', {
    'alternative_products': NotRequired[list[ModelProducthuntProductAboutMentionedProduct]],
    'id': NotRequired[str],
    'product': NotRequired[ModelProducthuntProductAboutMentionedProduct],
    'shoutout_note': NotRequired[str],
}, total=False)

ModelProducthuntProductAboutUser = TypedDict('ModelProducthuntProductAboutUser', {
    'avatar_url': NotRequired[str],
    'headline': NotRequired[str],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'username': NotRequired[str],
}, total=False)

ModelProducthuntProductAboutViewer = TypedDict('ModelProducthuntProductAboutViewer', {
    'is_featured_post_maker': NotRequired[bool],
    'recent_launch': NotRequired[dict[str, Any]],
}, total=False)

ModelProducthuntProductAlternativeBadge = TypedDict('ModelProducthuntProductAlternativeBadge', {
    'date': NotRequired[str],
    'id': NotRequired[str],
    'period': NotRequired[str],
    'position': NotRequired[int],
    'post_name': NotRequired[str],
    'post_slug': NotRequired[str],
}, total=False)

ModelProducthuntProductAlternativeDiscussion = TypedDict('ModelProducthuntProductAlternativeDiscussion', {
    'comments_count': NotRequired[int],
    'created_at': NotRequired[str],
    'description_preview': NotRequired[str],
    'has_voted': NotRequired[bool],
    'id': NotRequired[str],
    'path': NotRequired[str],
    'pinned': NotRequired[bool],
    'primary_forum': NotRequired[ModelProducthuntProductAlternativeDiscussionForum],
    'slug': NotRequired[str],
    'title': NotRequired[str],
    'user': NotRequired[ModelProducthuntProductAlternativeDiscussionUser],
    'votes_count': NotRequired[int],
}, total=False)

ModelProducthuntProductAlternativeDiscussionForum = TypedDict('ModelProducthuntProductAlternativeDiscussionForum', {
    'id': NotRequired[str],
    'slug': NotRequired[str],
    'subject_id': NotRequired[str],
    'subject_name': NotRequired[str],
}, total=False)

ModelProducthuntProductAlternativeDiscussionUser = TypedDict('ModelProducthuntProductAlternativeDiscussionUser', {
    'avatar_url': NotRequired[str],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'username': NotRequired[str],
}, total=False)

ModelProducthuntProductAlternativeItem = TypedDict('ModelProducthuntProductAlternativeItem', {
    'category_score': NotRequired[float],
    'category_weight': NotRequired[float],
    'combined_score': NotRequired[float],
    'embedding_score': NotRequired[float],
    'embedding_weight': NotRequired[float],
    'id': NotRequired[str],
    'product': NotRequired[ModelProducthuntProductAlternativeProduct],
    'rating_score': NotRequired[float],
    'rating_weight': NotRequired[float],
}, total=False)

ModelProducthuntProductAlternativeProduct = TypedDict('ModelProducthuntProductAlternativeProduct', {
    'badges': NotRequired[list[ModelProducthuntProductAlternativeBadge]],
    'categories': NotRequired[list[str]],
    'followers_count': NotRequired[int],
    'id': NotRequired[str],
    'is_subscribed': NotRequired[bool],
    'is_top_product': NotRequired[bool],
    'logo_uuid': NotRequired[str],
    'name': NotRequired[str],
    'reviews_count': NotRequired[int],
    'reviews_rating': NotRequired[float],
    'slug': NotRequired[str],
    'structured_data': NotRequired[ModelProducthuntProductAlternativeStructuredData],
    'tagline': NotRequired[str],
    'tags': NotRequired[list[str]],
}, total=False)

ModelProducthuntProductAlternativeStructuredData = TypedDict('ModelProducthuntProductAlternativeStructuredData', {
    'application_category': NotRequired[str],
    'context': NotRequired[str],
    'date_modified': NotRequired[str],
    'date_published': NotRequired[str],
    'description': NotRequired[str],
    'id': NotRequired[str],
    'image': NotRequired[str],
    'name': NotRequired[str],
    'operating_system': NotRequired[str],
    'screenshot': NotRequired[list[str]],
    'url': NotRequired[str],
}, total=False)

ModelProducthuntProductAlternativeTag = TypedDict('ModelProducthuntProductAlternativeTag', {
    'count': NotRequired[int],
    'name': NotRequired[str],
}, total=False)

ModelProducthuntProductAlternativesPage = TypedDict('ModelProducthuntProductAlternativesPage', {
    'alternative_tags': NotRequired[list[ModelProducthuntProductAlternativeTag]],
    'alternatives_markdown_description': NotRequired[str],
    'categories': NotRequired[list[str]],
    'discussions': NotRequired[list[ModelProducthuntProductAlternativeDiscussion]],
    'discussions_has_next_page': NotRequired[bool],
    'end_cursor': NotRequired[str],
    'followers_count': NotRequired[int],
    'has_next_page': NotRequired[bool],
    'items': NotRequired[list[ModelProducthuntProductAlternativeItem]],
    'name': NotRequired[str],
    'product_id': NotRequired[str],
    'slug': NotRequired[str],
    'total_count': NotRequired[int],
}, total=False)

ModelProducthuntProductCategoryAd = TypedDict('ModelProducthuntProductCategoryAd', {
    'channel_kind': NotRequired[str],
    'id': NotRequired[str],
    'large_asset_uuid': NotRequired[str],
    'name': NotRequired[str],
    'post': NotRequired[ModelProducthuntProductCategoryAdPost],
    'small_asset_uuid': NotRequired[str],
    'subject': NotRequired[str],
    'tagline': NotRequired[str],
    'thumbnail_uuid': NotRequired[str],
    'url': NotRequired[str],
    'variation_id': NotRequired[str],
}, total=False)

ModelProducthuntProductCategoryAdComment = TypedDict('ModelProducthuntProductCategoryAdComment', {
    'body_text': NotRequired[str],
    'id': NotRequired[str],
    'is_pinned': NotRequired[bool],
    'path': NotRequired[str],
    'subject_id': NotRequired[str],
    'user': NotRequired[ModelProducthuntProductCategoryUser],
}, total=False)

ModelProducthuntProductCategoryAdPost = TypedDict('ModelProducthuntProductCategoryAdPost', {
    'comments_count': NotRequired[int],
    'created_at': NotRequired[str],
    'disabled_when_scheduled': NotRequired[bool],
    'embargo_preview_at': NotRequired[str],
    'featured_at': NotRequired[str],
    'featured_comment': NotRequired[ModelProducthuntProductCategoryAdComment],
    'has_voted': NotRequired[bool],
    'hide_votes_count': NotRequired[bool],
    'id': NotRequired[str],
    'latest_score': NotRequired[int],
    'launch_day_score': NotRequired[int],
    'name': NotRequired[str],
    'product_id': NotRequired[str],
    'product_slug': NotRequired[str],
    'product_subscribed': NotRequired[bool],
    'randomization_status': NotRequired[ModelProducthuntProductCategoryRandomizationStatus],
    'slug': NotRequired[str],
    'topics': NotRequired[list[ModelProducthuntProductCategoryTopic]],
    'updated_at': NotRequired[str],
}, total=False)

ModelProducthuntProductCategoryAnswer = TypedDict('ModelProducthuntProductCategoryAnswer', {
    'body': NotRequired[ModelProducthuntProductCategoryMarkdown],
    'id': NotRequired[str],
    'sources': NotRequired[list[ModelProducthuntProductCategorySource]],
}, total=False)

ModelProducthuntProductCategoryFounderPost = TypedDict('ModelProducthuntProductCategoryFounderPost', {
    'badges': NotRequired[list[ModelProducthuntProductCategoryListBadge]],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'product_id': NotRequired[str],
    'product_slug': NotRequired[str],
    'product_state': NotRequired[str],
    'slug': NotRequired[str],
    'thumbnail_image_uuid': NotRequired[str],
}, total=False)

ModelProducthuntProductCategoryFounderShoutout = TypedDict('ModelProducthuntProductCategoryFounderShoutout', {
    'from_post': NotRequired[ModelProducthuntProductCategoryFounderPost],
    'id': NotRequired[str],
    'product_id': NotRequired[str],
}, total=False)

ModelProducthuntProductCategoryHeroProduct = TypedDict('ModelProducthuntProductCategoryHeroProduct', {
    'id': NotRequired[str],
    'is_no_longer_online': NotRequired[bool],
    'logo_uuid': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelProducthuntProductCategoryLatestLaunch = TypedDict('ModelProducthuntProductCategoryLatestLaunch', {
    'id': NotRequired[str],
    'scheduled_at': NotRequired[str],
}, total=False)

ModelProducthuntProductCategoryListBadge = TypedDict('ModelProducthuntProductCategoryListBadge', {
    'category': NotRequired[str],
    'date': NotRequired[str],
    'id': NotRequired[str],
    'period': NotRequired[str],
    'position': NotRequired[int],
    'post_id': NotRequired[str],
    'post_name': NotRequired[str],
    'post_slug': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

ModelProducthuntProductCategoryListProduct = TypedDict('ModelProducthuntProductCategoryListProduct', {
    'badges': NotRequired[list[ModelProducthuntProductCategoryListBadge]],
    'categories': NotRequired[list[ModelProducthuntProductCategoryRef]],
    'detailed_reviews_count': NotRequired[int],
    'followers_count': NotRequired[int],
    'founder_reviews_count': NotRequired[int],
    'founder_shoutouts': NotRequired[list[ModelProducthuntProductCategoryFounderShoutout]],
    'id': NotRequired[str],
    'is_no_longer_online': NotRequired[bool],
    'is_subscribed': NotRequired[bool],
    'is_top_product': NotRequired[bool],
    'latest_launch': NotRequired[ModelProducthuntProductCategoryLatestLaunch],
    'logo_uuid': NotRequired[str],
    'name': NotRequired[str],
    'posts_count': NotRequired[int],
    'reviews_count': NotRequired[int],
    'reviews_rating': NotRequired[float],
    'slug': NotRequired[str],
    'structured_data': NotRequired[ModelProducthuntProductAlternativeStructuredData],
    'tagline': NotRequired[str],
    'tags': NotRequired[list[str]],
}, total=False)

ModelProducthuntProductCategoryMarkdown = TypedDict('ModelProducthuntProductCategoryMarkdown', {
    'markdown': NotRequired[str],
    'text': NotRequired[str],
}, total=False)

ModelProducthuntProductCategoryPage = TypedDict('ModelProducthuntProductCategoryPage', {
    'description': NotRequired[str],
    'discussions': NotRequired[list[ModelProducthuntProductAlternativeDiscussion]],
    'discussions_has_next_page': NotRequired[bool],
    'expandable_html': NotRequired[str],
    'hero_products': NotRequired[list[ModelProducthuntProductCategoryHeroProduct]],
    'hero_products_count': NotRequired[int],
    'id': NotRequired[str],
    'last_updated_at': NotRequired[str],
    'meta_title': NotRequired[str],
    'name': NotRequired[str],
    'parent': NotRequired[ModelProducthuntProductCategoryParent],
    'path': NotRequired[str],
    'questions': NotRequired[list[ModelProducthuntProductCategoryQuestion]],
    'raw_relevant_reviews': NotRequired[list[dict[str, Any]]],
    'recent_launches_count': NotRequired[int],
    'recent_summary': NotRequired[ModelProducthuntProductCategoryRecentSummary],
    'reviews_count': NotRequired[int],
    'slug': NotRequired[str],
    'sub_categories': NotRequired[list[ModelProducthuntProductCategoryRef]],
    'targeted_ad': NotRequired[ModelProducthuntProductCategoryAd],
}, total=False)

ModelProducthuntProductCategoryParent = TypedDict('ModelProducthuntProductCategoryParent', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'path': NotRequired[str],
    'sub_categories': NotRequired[list[ModelProducthuntProductCategoryRef]],
}, total=False)

ModelProducthuntProductCategoryProductsPage = TypedDict('ModelProducthuntProductCategoryProductsPage', {
    'ai_summary': NotRequired[str],
    'category_tags': NotRequired[list[ModelProducthuntProductAlternativeTag]],
    'connection': NotRequired[str],
    'description': NotRequired[str],
    'end_cursor': NotRequired[str],
    'featured_only': NotRequired[bool],
    'has_next_page': NotRequired[bool],
    'has_previous_page': NotRequired[bool],
    'id': NotRequired[str],
    'items': NotRequired[list[ModelProducthuntProductCategoryListProduct]],
    'last_updated_at': NotRequired[str],
    'name': NotRequired[str],
    'order': NotRequired[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
    'path': NotRequired[str],
    'slug': NotRequired[str],
    'tags': NotRequired[list[str]],
    'total_count': NotRequired[int],
}, total=False)

ModelProducthuntProductCategoryQuestion = TypedDict('ModelProducthuntProductCategoryQuestion', {
    'body': NotRequired[ModelProducthuntProductCategoryMarkdown],
    'id': NotRequired[str],
    'top_answer': NotRequired[ModelProducthuntProductCategoryAnswer],
}, total=False)

ModelProducthuntProductCategoryRandomizationStatus = TypedDict('ModelProducthuntProductCategoryRandomizationStatus', {
    'active': NotRequired[bool],
    'next_transition_at': NotRequired[str],
    'random_day': NotRequired[bool],
}, total=False)

ModelProducthuntProductCategoryRecentSummary = TypedDict('ModelProducthuntProductCategoryRecentSummary', {
    'products': NotRequired[list[ModelProducthuntProductCategorySummaryProduct]],
    'summary': NotRequired[str],
}, total=False)

ModelProducthuntProductCategoryRef = TypedDict('ModelProducthuntProductCategoryRef', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'path': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelProducthuntProductCategorySource = TypedDict('ModelProducthuntProductCategorySource', {
    'badges': NotRequired[list[str]],
    'id': NotRequired[str],
    'path': NotRequired[str],
    'subject_id': NotRequired[str],
    'type': NotRequired[str],
    'user': NotRequired[ModelProducthuntProductCategoryUser],
    'visible_at': NotRequired[str],
}, total=False)

ModelProducthuntProductCategorySummaryProduct = TypedDict('ModelProducthuntProductCategorySummaryProduct', {
    'badges': NotRequired[list[ModelProducthuntProductAlternativeBadge]],
    'categories': NotRequired[list[ModelProducthuntProductCategoryRef]],
    'followers_count': NotRequired[int],
    'id': NotRequired[str],
    'is_no_longer_online': NotRequired[bool],
    'is_subscribed': NotRequired[bool],
    'is_top_product': NotRequired[bool],
    'latest_launch': NotRequired[ModelProducthuntProductCategoryLatestLaunch],
    'logo_uuid': NotRequired[str],
    'name': NotRequired[str],
    'reviews_count': NotRequired[int],
    'reviews_rating': NotRequired[float],
    'slug': NotRequired[str],
    'tagline': NotRequired[str],
    'tags': NotRequired[list[str]],
}, total=False)

ModelProducthuntProductCategoryTopic = TypedDict('ModelProducthuntProductCategoryTopic', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelProducthuntProductCategoryUser = TypedDict('ModelProducthuntProductCategoryUser', {
    'avatar_url': NotRequired[str],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'username': NotRequired[str],
}, total=False)

ModelProducthuntProductCustomersPage = TypedDict('ModelProducthuntProductCustomersPage', {
    'connection': NotRequired[str],
    'end_cursor': NotRequired[str],
    'has_next_page': NotRequired[bool],
    'has_previous_page': NotRequired[bool],
    'items': NotRequired[list[ModelProducthuntProductCategoryListProduct]],
    'name': NotRequired[str],
    'order': NotRequired[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
    'pages_count': NotRequired[int],
    'product_id': NotRequired[str],
    'raw_page_info': NotRequired[dict[str, Any]],
    'slug': NotRequired[str],
    'total_count': NotRequired[int],
}, total=False)

ModelProducthuntProductDetailedReview = TypedDict('ModelProducthuntProductDetailedReview', {
    'alternative_products': NotRequired[list[ModelProducthuntProductDetailedReviewProduct]],
    'alternatives_feedback': NotRequired[str],
    'can_destroy': NotRequired[bool],
    'can_moderate': NotRequired[bool],
    'can_reply': NotRequired[bool],
    'can_update': NotRequired[bool],
    'comments_count': NotRequired[int],
    'created_at': NotRequired[str],
    'customization_rating': NotRequired[int],
    'ease_of_use_rating': NotRequired[int],
    'follow_product': NotRequired[ModelProducthuntProductDetailedReviewFollowProduct],
    'from_post': NotRequired[ModelProducthuntProductDetailedReviewPost],
    'has_voted': NotRequired[bool],
    'id': NotRequired[str],
    'impression_count': NotRequired[int],
    'is_hidden': NotRequired[bool],
    'llm_content_quality_grade': NotRequired[str],
    'llm_content_quality_reason': NotRequired[str],
    'negative_feedback': NotRequired[str],
    'overall_experience': NotRequired[str],
    'overall_rating': NotRequired[int],
    'positive_feedback': NotRequired[str],
    'product': NotRequired[ModelProducthuntProductDetailedReviewProduct],
    'question_answers': NotRequired[list[ModelProducthuntProductDetailedReviewQuestionAnswer]],
    'reliability_rating': NotRequired[int],
    'review_type': NotRequired[str],
    'selected_cons': NotRequired[list[ModelProducthuntProductDetailedReviewTag]],
    'selected_pros': NotRequired[list[ModelProducthuntProductDetailedReviewTag]],
    'status': NotRequired[str],
    'threads_end_cursor': NotRequired[str],
    'threads_has_next_page': NotRequired[bool],
    'threads_total_count': NotRequired[int],
    'user': NotRequired[ModelProducthuntProductDetailedReviewUser],
    'value_for_money_rating': NotRequired[int],
    'votes_count': NotRequired[int],
}, total=False)

ModelProducthuntProductDetailedReviewFollowProduct = TypedDict('ModelProducthuntProductDetailedReviewFollowProduct', {
    'id': NotRequired[str],
    'is_no_longer_online': NotRequired[bool],
    'is_subscribed': NotRequired[bool],
    'logo_uuid': NotRequired[str],
    'name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelProducthuntProductDetailedReviewPost = TypedDict('ModelProducthuntProductDetailedReviewPost', {
    'badges': NotRequired[list[ModelProducthuntProductCategoryListBadge]],
    'id': NotRequired[str],
    'is_top_launch': NotRequired[bool],
    'latest_score': NotRequired[int],
    'name': NotRequired[str],
    'product_id': NotRequired[str],
    'product_is_top_product': NotRequired[bool],
    'product_slug': NotRequired[str],
    'product_state': NotRequired[str],
    'slug': NotRequired[str],
    'thumbnail_image_uuid': NotRequired[str],
}, total=False)

ModelProducthuntProductDetailedReviewProduct = TypedDict('ModelProducthuntProductDetailedReviewProduct', {
    'id': NotRequired[str],
    'is_no_longer_online': NotRequired[bool],
    'logo_uuid': NotRequired[str],
    'name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelProducthuntProductDetailedReviewQuestionAnswer = TypedDict('ModelProducthuntProductDetailedReviewQuestionAnswer', {
    'answer': NotRequired[str],
    'id': NotRequired[str],
    'question': NotRequired[str],
    'question_id': NotRequired[str],
}, total=False)

ModelProducthuntProductDetailedReviewTag = TypedDict('ModelProducthuntProductDetailedReviewTag', {
    'count': NotRequired[int],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelProducthuntProductDetailedReviewUser = TypedDict('ModelProducthuntProductDetailedReviewUser', {
    'avatar_url': NotRequired[str],
    'headline': NotRequired[str],
    'id': NotRequired[str],
    'is_account_verified': NotRequired[bool],
    'is_ambassador': NotRequired[bool],
    'is_followed': NotRequired[bool],
    'name': NotRequired[str],
    'reviews_count': NotRequired[int],
    'selected_byline_product': NotRequired[ModelProducthuntProductDetailedReviewProduct],
    'top_hunter_badge': NotRequired[dict[str, Any]],
    'top_launch_badge': NotRequired[dict[str, Any]],
    'top_product_badge': NotRequired[dict[str, Any]],
    'username': NotRequired[str],
}, total=False)

ModelProducthuntProductDetailedReviewsPage = TypedDict('ModelProducthuntProductDetailedReviewsPage', {
    'connection': NotRequired[str],
    'detailed_review': NotRequired[dict[str, Any]],
    'detailed_reviews_count': NotRequired[int],
    'end_cursor': NotRequired[str],
    'founder_detailed_reviews_count': NotRequired[int],
    'has_next_page': NotRequired[bool],
    'is_maker': NotRequired[bool],
    'is_trashed': NotRequired[bool],
    'items': NotRequired[list[ModelProducthuntProductDetailedReview]],
    'name': NotRequired[str],
    'other_detailed_reviews_count': NotRequired[int],
    'product_id': NotRequired[str],
    'raw_page_info': NotRequired[dict[str, Any]],
    'reviews_count': NotRequired[int],
    'reviews_rating': NotRequired[float],
    'reviews_recent_rating': NotRequired[float],
    'slug': NotRequired[str],
    'total_count': NotRequired[int],
}, total=False)

ModelProducthuntProductLaunchesPage = TypedDict('ModelProducthuntProductLaunchesPage', {
    'connection': NotRequired[str],
    'end_cursor': NotRequired[str],
    'has_next_page': NotRequired[bool],
    'items': NotRequired[list[ModelProducthuntProductAboutPost]],
    'name': NotRequired[str],
    'order': NotRequired[str],
    'product_id': NotRequired[str],
    'raw_page_info': NotRequired[dict[str, Any]],
    'slug': NotRequired[str],
    'total_count': NotRequired[int],
}, total=False)

ModelProducthuntProductMaker = TypedDict('ModelProducthuntProductMaker', {
    'avatar_url': NotRequired[str],
    'followers_count': NotRequired[int],
    'headline': NotRequired[str],
    'id': NotRequired[str],
    'is_followed': NotRequired[bool],
    'made_posts': NotRequired[list[ModelProducthuntProductMakerPost]],
    'name': NotRequired[str],
    'username': NotRequired[str],
}, total=False)

ModelProducthuntProductMakerPost = TypedDict('ModelProducthuntProductMakerPost', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'product_id': NotRequired[str],
    'product_slug': NotRequired[str],
    'product_state': NotRequired[str],
    'slug': NotRequired[str],
    'thumbnail_image_uuid': NotRequired[str],
}, total=False)

ModelProducthuntProductMakersPage = TypedDict('ModelProducthuntProductMakersPage', {
    'can_claim': NotRequired[bool],
    'connection': NotRequired[str],
    'end_cursor': NotRequired[str],
    'has_next_page': NotRequired[bool],
    'is_claimed': NotRequired[bool],
    'is_trashed': NotRequired[bool],
    'items': NotRequired[list[ModelProducthuntProductMaker]],
    'name': NotRequired[str],
    'product_id': NotRequired[str],
    'raw_page_info': NotRequired[dict[str, Any]],
    'slug': NotRequired[str],
    'total_count': NotRequired[int],
    'viewer_pending_team_request': NotRequired[dict[str, Any]],
}, total=False)

ModelProducthuntSimilarProduct = TypedDict('ModelProducthuntSimilarProduct', {
    'categories': NotRequired[list[str]],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'rating': NotRequired[float],
    'review_count': NotRequired[int],
}, total=False)

ModelProducthuntAboutResponseDoc = TypedDict('ModelProducthuntAboutResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelProducthuntProductAboutPage],
    'msg': NotRequired[str],
}, total=False)

ModelProducthuntAlternativesResponseDoc = TypedDict('ModelProducthuntAlternativesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelProducthuntProductAlternativesPage],
    'msg': NotRequired[str],
}, total=False)

ModelProducthuntCategoryProductsResponseDoc = TypedDict('ModelProducthuntCategoryProductsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelProducthuntProductCategoryProductsPage],
    'msg': NotRequired[str],
}, total=False)

ModelProducthuntCategoryResponseDoc = TypedDict('ModelProducthuntCategoryResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelProducthuntProductCategoryPage],
    'msg': NotRequired[str],
}, total=False)

ModelProducthuntCustomersResponseDoc = TypedDict('ModelProducthuntCustomersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelProducthuntProductCustomersPage],
    'msg': NotRequired[str],
}, total=False)

ModelProducthuntLaunchesResponseDoc = TypedDict('ModelProducthuntLaunchesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelProducthuntProductLaunchesPage],
    'msg': NotRequired[str],
}, total=False)

ModelProducthuntLeaderboardResponseDoc = TypedDict('ModelProducthuntLeaderboardResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelProducthuntLeaderboardPage],
    'msg': NotRequired[str],
}, total=False)

ModelProducthuntMakersResponseDoc = TypedDict('ModelProducthuntMakersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelProducthuntProductMakersPage],
    'msg': NotRequired[str],
}, total=False)

ModelProducthuntProductResponseDoc = TypedDict('ModelProducthuntProductResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelProducthuntProduct],
    'msg': NotRequired[str],
}, total=False)

ModelProducthuntReviewsResponseDoc = TypedDict('ModelProducthuntReviewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelProducthuntProductDetailedReviewsPage],
    'msg': NotRequired[str],
}, total=False)

ModelProducthuntSearchAggregationsDoc = TypedDict('ModelProducthuntSearchAggregationsDoc', {
    'topics': NotRequired[list[ModelProducthuntSearchTopicDoc]],
}, total=False)

ModelProducthuntSearchDataDoc = TypedDict('ModelProducthuntSearchDataDoc', {
    'aggregations': NotRequired[ModelProducthuntSearchAggregationsDoc],
    'edges': NotRequired[list[ModelProducthuntSearchEdgeDoc]],
    'pageInfo': NotRequired[ModelProducthuntSearchPageInfoDoc],
    'pagesCount': NotRequired[int],
}, total=False)

ModelProducthuntSearchEdgeDoc = TypedDict('ModelProducthuntSearchEdgeDoc', {
    'node': NotRequired[dict[str, Any]],
}, total=False)

ModelProducthuntSearchPageInfoDoc = TypedDict('ModelProducthuntSearchPageInfoDoc', {
    'hasNextPage': NotRequired[bool],
    'hasPreviousPage': NotRequired[bool],
    'page': NotRequired[int],
}, total=False)

ModelProducthuntSearchResponseDoc = TypedDict('ModelProducthuntSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelProducthuntSearchDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelProducthuntSearchTopicDoc = TypedDict('ModelProducthuntSearchTopicDoc', {
    'count': NotRequired[int],
    'topic': NotRequired[dict[str, Any]],
}, total=False)

ModelReferralsReferralAttributionDoc = TypedDict('ModelReferralsReferralAttributionDoc', {
    'campaign': NotRequired[str],
    'code': NotRequired[str],
    'created_at': NotRequired[str],
    'expires_at': NotRequired[str],
    'id': NotRequired[str],
    'qualified_at': NotRequired[str],
    'reward_credits': NotRequired[int],
    'rewarded_at': NotRequired[str],
    'role': NotRequired[Literal['referrer', 'referred']],
    'status': NotRequired[Literal['attributed', 'qualified', 'review_required', 'rewarded', 'expired', 'capped', 'failed', 'rejected']],
}, total=False)

ModelReferralsReferralClickRequestDoc = TypedDict('ModelReferralsReferralClickRequestDoc', {
    'click_id': NotRequired[str],
    'code': NotRequired[str],
    'landing_path': NotRequired[str],
    'utm_campaign': NotRequired[str],
    'utm_medium': NotRequired[str],
    'utm_source': NotRequired[str],
}, total=False)

ModelReferralsReferralClickResponseDoc = TypedDict('ModelReferralsReferralClickResponseDoc', {
    'click_id': NotRequired[str],
    'code': NotRequired[str],
}, total=False)

ModelReferralsReferralsEventsResponseDoc = TypedDict('ModelReferralsReferralsEventsResponseDoc', {
    'items': NotRequired[list[ModelReferralsReferralAttributionDoc]],
}, total=False)

ModelReferralsReferralsMeResponseDoc = TypedDict('ModelReferralsReferralsMeResponseDoc', {
    'attribution_window_days': NotRequired[int],
    'code': NotRequired[str],
    'items': NotRequired[list[ModelReferralsReferralAttributionDoc]],
    'monthly_referrer_reward_cap': NotRequired[int],
    'referred_reward_credits': NotRequired[int],
    'reward_credits': NotRequired[int],
    'share_path': NotRequired[str],
    'stats': NotRequired[ModelReferralsReferralsStatsDoc],
}, total=False)

ModelReferralsReferralsStatsDoc = TypedDict('ModelReferralsReferralsStatsDoc', {
    'attributed': NotRequired[int],
    'capped': NotRequired[int],
    'expired': NotRequired[int],
    'qualified': NotRequired[int],
    'rejected': NotRequired[int],
    'review_required': NotRequired[int],
    'rewarded': NotRequired[int],
}, total=False)

ModelShopappAnalysisResponse = TypedDict('ModelShopappAnalysisResponse', {
    'currencies': NotRequired[list[str]],
    'discounts': NotRequired[ModelShopappDiscountSummary],
    'groups_count': NotRequired[int],
    'prices_by_currency': NotRequired[list[ModelShopappCurrencyPriceSummary]],
    'products_count': NotRequired[int],
    'query': NotRequired[str],
    'sale_count': NotRequired[int],
    'sampled_product_ids': NotRequired[list[str]],
    'shops_count': NotRequired[int],
    'top_shops': NotRequired[list[ModelShopappShopSummary]],
}, total=False)

ModelShopappCategoriesResponse = TypedDict('ModelShopappCategoriesResponse', {
    'categories': NotRequired[list[ModelShopappCategoryItem]],
}, total=False)

ModelShopappCategoryItem = TypedDict('ModelShopappCategoryItem', {
    'children': NotRequired[list[ModelShopappCategoryItem]],
    'gid': NotRequired[str],
    'has_children': NotRequired[bool],
    'id': NotRequired[str],
    'image': NotRequired[str],
    'name': NotRequired[str],
    'path': NotRequired[list[ModelShopappCategoryPath]],
    'slug': NotRequired[str],
}, total=False)

ModelShopappCategoryPath = TypedDict('ModelShopappCategoryPath', {
    'gid': NotRequired[str],
    'id': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelShopappCurrencyPriceSummary = TypedDict('ModelShopappCurrencyPriceSummary', {
    'average': NotRequired[float],
    'count': NotRequired[int],
    'currency': NotRequired[str],
    'max': NotRequired[float],
    'min': NotRequired[float],
}, total=False)

ModelShopappDiscountSummary = TypedDict('ModelShopappDiscountSummary', {
    'average_percent': NotRequired[float],
    'max_percent': NotRequired[float],
    'min_percent': NotRequired[float],
}, total=False)

ModelShopappImageItem = TypedDict('ModelShopappImageItem', {
    'alt': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelShopappLocationAddress = TypedDict('ModelShopappLocationAddress', {
    'address1': NotRequired[str],
    'address2': NotRequired[str],
    'city': NotRequired[str],
    'country': NotRequired[str],
    'postal_code': NotRequired[str],
    'zone_code': NotRequired[str],
}, total=False)

ModelShopappOptionGroup = TypedDict('ModelShopappOptionGroup', {
    'name': NotRequired[str],
    'values': NotRequired[list[str]],
}, total=False)

ModelShopappProductDetail = TypedDict('ModelShopappProductDetail', {
    'available': NotRequired[bool],
    'currency': NotRequired[str],
    'description': NotRequired[str],
    'external_url': NotRequired[str],
    'id': NotRequired[str],
    'images': NotRequired[list[ModelShopappImageItem]],
    'option_groups': NotRequired[list[ModelShopappOptionGroup]],
    'original_price': NotRequired[float],
    'price': NotRequired[float],
    'rating': NotRequired[float],
    'related_products': NotRequired[list[ModelShopappProductItem]],
    'reviews': NotRequired[list[ModelShopappReviewItem]],
    'reviews_count': NotRequired[int],
    'shop_handle': NotRequired[str],
    'shop_id': NotRequired[str],
    'shop_name': NotRequired[str],
    'slug': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'variant_id': NotRequired[str],
}, total=False)

ModelShopappProductDetailResponse = TypedDict('ModelShopappProductDetailResponse', {
    'product': NotRequired[ModelShopappProductDetail],
}, total=False)

ModelShopappProductItem = TypedDict('ModelShopappProductItem', {
    'currency': NotRequired[str],
    'group_query': NotRequired[str],
    'group_title': NotRequired[str],
    'id': NotRequired[str],
    'image': NotRequired[str],
    'image_alt': NotRequired[str],
    'on_sale': NotRequired[bool],
    'original_price': NotRequired[float],
    'position': NotRequired[int],
    'price': NotRequired[float],
    'shop_id': NotRequired[str],
    'shop_name': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'variant_id': NotRequired[str],
}, total=False)

ModelShopappProductShopResponse = TypedDict('ModelShopappProductShopResponse', {
    'product_id': NotRequired[str],
    'shop': NotRequired[ModelShopappShopDetail],
}, total=False)

ModelShopappProductVariantResponse = TypedDict('ModelShopappProductVariantResponse', {
    'product_id': NotRequired[str],
    'variant': NotRequired[ModelShopappVariantItem],
}, total=False)

ModelShopappRelatedResponse = TypedDict('ModelShopappRelatedResponse', {
    'limit': NotRequired[int],
    'product_id': NotRequired[str],
    'products': NotRequired[list[ModelShopappProductItem]],
}, total=False)

ModelShopappReviewItem = TypedDict('ModelShopappReviewItem', {
    'author': NotRequired[str],
    'body': NotRequired[str],
    'date': NotRequired[str],
    'helpful_count': NotRequired[int],
    'id': NotRequired[str],
    'product': NotRequired[ModelShopappReviewProduct],
    'rating': NotRequired[float],
    'title': NotRequired[str],
    'variant_label': NotRequired[str],
}, total=False)

ModelShopappReviewProduct = TypedDict('ModelShopappReviewProduct', {
    'id': NotRequired[str],
    'image': NotRequired[str],
    'image_alt': NotRequired[str],
    'slug': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'variant': NotRequired[str],
}, total=False)

ModelShopappReviewsResponse = TypedDict('ModelShopappReviewsResponse', {
    'limit': NotRequired[int],
    'product_id': NotRequired[str],
    'reviews': NotRequired[list[ModelShopappReviewItem]],
}, total=False)

ModelShopappSearchGroup = TypedDict('ModelShopappSearchGroup', {
    'product_ids': NotRequired[list[str]],
    'products_seen': NotRequired[int],
    'query': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelShopappSearchResponse = TypedDict('ModelShopappSearchResponse', {
    'groups': NotRequired[list[ModelShopappSearchGroup]],
    'limit': NotRequired[int],
    'products': NotRequired[list[ModelShopappProductItem]],
    'query': NotRequired[str],
}, total=False)

ModelShopappShopCollection = TypedDict('ModelShopappShopCollection', {
    'id': NotRequired[str],
    'slug': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelShopappShopDetail = TypedDict('ModelShopappShopDetail', {
    'banner': NotRequired[str],
    'collections': NotRequired[list[ModelShopappShopCollection]],
    'description': NotRequired[str],
    'handle': NotRequired[str],
    'id': NotRequired[str],
    'logo': NotRequired[str],
    'name': NotRequired[str],
    'rating': NotRequired[float],
    'reviews_count': NotRequired[int],
    'shopify_id': NotRequired[str],
    'storefront': NotRequired[str],
    'url': NotRequired[str],
    'uuid': NotRequired[str],
}, total=False)

ModelShopappShopLocationItem = TypedDict('ModelShopappShopLocationItem', {
    'address': NotRequired[ModelShopappLocationAddress],
    'id': NotRequired[str],
    'latitude': NotRequired[float],
    'longitude': NotRequired[float],
    'name': NotRequired[str],
}, total=False)

ModelShopappShopLocationsResponse = TypedDict('ModelShopappShopLocationsResponse', {
    'limit': NotRequired[int],
    'locations': NotRequired[list[ModelShopappShopLocationItem]],
    'next_cursor': NotRequired[str],
    'shop_handle': NotRequired[str],
    'shop_id': NotRequired[str],
    'total_count': NotRequired[int],
}, total=False)

ModelShopappShopProductsResponse = TypedDict('ModelShopappShopProductsResponse', {
    'collection': NotRequired[ModelShopappShopCollection],
    'collection_id': NotRequired[str],
    'limit': NotRequired[int],
    'next_cursor': NotRequired[str],
    'products': NotRequired[list[ModelShopappProductItem]],
    'shop_handle': NotRequired[str],
    'sort_by': NotRequired[str],
}, total=False)

ModelShopappShopResponse = TypedDict('ModelShopappShopResponse', {
    'shop': NotRequired[ModelShopappShopDetail],
}, total=False)

ModelShopappShopReviewsResponse = TypedDict('ModelShopappShopReviewsResponse', {
    'limit': NotRequired[int],
    'next_cursor': NotRequired[str],
    'reviews': NotRequired[list[ModelShopappReviewItem]],
    'shop_handle': NotRequired[str],
    'shop_id': NotRequired[str],
    'total_count': NotRequired[int],
}, total=False)

ModelShopappShopSummary = TypedDict('ModelShopappShopSummary', {
    'count': NotRequired[int],
    'shop_id': NotRequired[str],
    'shop_name': NotRequired[str],
}, total=False)

ModelShopappShopTypeaheadItem = TypedDict('ModelShopappShopTypeaheadItem', {
    'collection': NotRequired[ModelShopappShopCollection],
    'id': NotRequired[str],
    'position': NotRequired[int],
    'product': NotRequired[ModelShopappProductItem],
    'text': NotRequired[str],
    'type': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelShopappShopTypeaheadResponse = TypedDict('ModelShopappShopTypeaheadResponse', {
    'limit': NotRequired[int],
    'query': NotRequired[str],
    'shop_handle': NotRequired[str],
    'shop_id': NotRequired[str],
    'suggestions': NotRequired[list[ModelShopappShopTypeaheadItem]],
}, total=False)

ModelShopappSuggestResponse = TypedDict('ModelShopappSuggestResponse', {
    'limit': NotRequired[int],
    'query': NotRequired[str],
    'suggestions': NotRequired[list[ModelShopappSuggestionItem]],
}, total=False)

ModelShopappSuggestionItem = TypedDict('ModelShopappSuggestionItem', {
    'image': NotRequired[str],
    'rating': NotRequired[float],
    'shop_handle': NotRequired[str],
    'shop_id': NotRequired[str],
    'shop_name': NotRequired[str],
    'text': NotRequired[str],
    'type': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelShopappVariantItem = TypedDict('ModelShopappVariantItem', {
    'available_for_sale': NotRequired[bool],
    'currency': NotRequired[str],
    'gid': NotRequired[str],
    'id': NotRequired[str],
    'image': NotRequired[ModelShopappImageItem],
    'options': NotRequired[dict[str, str]],
    'original_price': NotRequired[float],
    'price': NotRequired[float],
    'requires_shipping': NotRequired[bool],
    'title': NotRequired[str],
}, total=False)

ModelShopappVariantsResponse = TypedDict('ModelShopappVariantsResponse', {
    'limit': NotRequired[int],
    'product_id': NotRequired[str],
    'variants': NotRequired[list[ModelShopappVariantItem]],
}, total=False)

ModelShopappAnalysisResponseDoc = TypedDict('ModelShopappAnalysisResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopappAnalysisResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopappCategoriesResponseDoc = TypedDict('ModelShopappCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopappCategoriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopappProductResponseDoc = TypedDict('ModelShopappProductResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopappProductDetailResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopappProductShopResponseDoc = TypedDict('ModelShopappProductShopResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopappProductShopResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopappProductVariantResponseDoc = TypedDict('ModelShopappProductVariantResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopappProductVariantResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopappRelatedResponseDoc = TypedDict('ModelShopappRelatedResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopappRelatedResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopappReviewsResponseDoc = TypedDict('ModelShopappReviewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopappReviewsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopappSearchResponseDoc = TypedDict('ModelShopappSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopappSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopappShopLocationsResponseDoc = TypedDict('ModelShopappShopLocationsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopappShopLocationsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopappShopProductsResponseDoc = TypedDict('ModelShopappShopProductsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopappShopProductsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopappShopResponseDoc = TypedDict('ModelShopappShopResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopappShopResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopappShopReviewsResponseDoc = TypedDict('ModelShopappShopReviewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopappShopReviewsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopappShopTypeaheadResponseDoc = TypedDict('ModelShopappShopTypeaheadResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopappShopTypeaheadResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopappSuggestionsResponseDoc = TypedDict('ModelShopappSuggestionsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopappSuggestResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopappVariantsResponseDoc = TypedDict('ModelShopappVariantsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopappVariantsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopifyCollectionItem = TypedDict('ModelShopifyCollectionItem', {
    'created_at': NotRequired[str],
    'description': NotRequired[str],
    'handle': NotRequired[str],
    'id': NotRequired[str],
    'products_count': NotRequired[int],
    'published_at': NotRequired[str],
    'title': NotRequired[str],
    'updated_at': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelShopifyCollectionProductsResponse = TypedDict('ModelShopifyCollectionProductsResponse', {
    'collection': NotRequired[str],
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'products': NotRequired[list[ModelShopifyProductItem]],
    'source_url': NotRequired[str],
    'store_url': NotRequired[str],
}, total=False)

ModelShopifyCollectionsResponse = TypedDict('ModelShopifyCollectionsResponse', {
    'collections': NotRequired[list[ModelShopifyCollectionItem]],
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'source_url': NotRequired[str],
    'store_url': NotRequired[str],
}, total=False)

ModelShopifyImageItem = TypedDict('ModelShopifyImageItem', {
    'alt': NotRequired[str],
    'created_at': NotRequired[str],
    'height': NotRequired[int],
    'id': NotRequired[str],
    'position': NotRequired[int],
    'updated_at': NotRequired[str],
    'url': NotRequired[str],
    'variant_ids': NotRequired[list[str]],
    'width': NotRequired[int],
}, total=False)

ModelShopifyOptionItem = TypedDict('ModelShopifyOptionItem', {
    'name': NotRequired[str],
    'position': NotRequired[int],
    'values': NotRequired[list[str]],
}, total=False)

ModelShopifyPageItem = TypedDict('ModelShopifyPageItem', {
    'content': NotRequired[str],
    'created_at': NotRequired[str],
    'handle': NotRequired[str],
    'id': NotRequired[str],
    'published_at': NotRequired[str],
    'title': NotRequired[str],
    'updated_at': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelShopifyPageResponse = TypedDict('ModelShopifyPageResponse', {
    'page': NotRequired[ModelShopifyPageItem],
    'source_url': NotRequired[str],
    'store_url': NotRequired[str],
}, total=False)

ModelShopifyPagesResponse = TypedDict('ModelShopifyPagesResponse', {
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'pages': NotRequired[list[ModelShopifyPageItem]],
    'source_url': NotRequired[str],
    'store_url': NotRequired[str],
}, total=False)

ModelShopifyProductItem = TypedDict('ModelShopifyProductItem', {
    'available': NotRequired[bool],
    'compare_at_price': NotRequired[float],
    'created_at': NotRequired[str],
    'description': NotRequired[str],
    'featured_image': NotRequired[str],
    'handle': NotRequired[str],
    'id': NotRequired[str],
    'images': NotRequired[list[ModelShopifyImageItem]],
    'options': NotRequired[list[ModelShopifyOptionItem]],
    'price': NotRequired[float],
    'product_type': NotRequired[str],
    'published_at': NotRequired[str],
    'tags': NotRequired[list[str]],
    'title': NotRequired[str],
    'updated_at': NotRequired[str],
    'url': NotRequired[str],
    'variants': NotRequired[list[ModelShopifyVariantItem]],
    'vendor': NotRequired[str],
}, total=False)

ModelShopifyProductRecommendationsResponse = TypedDict('ModelShopifyProductRecommendationsResponse', {
    'handle': NotRequired[str],
    'intent': NotRequired[str],
    'limit': NotRequired[int],
    'product_id': NotRequired[str],
    'products': NotRequired[list[ModelShopifyProductItem]],
    'source_url': NotRequired[str],
    'store_url': NotRequired[str],
}, total=False)

ModelShopifyProductResponse = TypedDict('ModelShopifyProductResponse', {
    'product': NotRequired[ModelShopifyProductItem],
    'source_url': NotRequired[str],
    'store_url': NotRequired[str],
}, total=False)

ModelShopifyProductsResponse = TypedDict('ModelShopifyProductsResponse', {
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'products': NotRequired[list[ModelShopifyProductItem]],
    'source_url': NotRequired[str],
    'store_url': NotRequired[str],
}, total=False)

ModelShopifySearchQueryItem = TypedDict('ModelShopifySearchQueryItem', {
    'text': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelShopifySearchSuggestResponse = TypedDict('ModelShopifySearchSuggestResponse', {
    'collections': NotRequired[list[ModelShopifyCollectionItem]],
    'limit': NotRequired[int],
    'products': NotRequired[list[ModelShopifyProductItem]],
    'queries': NotRequired[list[ModelShopifySearchQueryItem]],
    'query': NotRequired[str],
    'source_url': NotRequired[str],
    'store_url': NotRequired[str],
    'types': NotRequired[list[str]],
}, total=False)

ModelShopifySitemapImage = TypedDict('ModelShopifySitemapImage', {
    'caption': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelShopifySitemapIndexResponse = TypedDict('ModelShopifySitemapIndexResponse', {
    'sitemaps': NotRequired[list[ModelShopifySitemapItem]],
    'source_url': NotRequired[str],
    'store_url': NotRequired[str],
}, total=False)

ModelShopifySitemapItem = TypedDict('ModelShopifySitemapItem', {
    'loc': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelShopifySitemapUrlitem = TypedDict('ModelShopifySitemapUrlitem', {
    'changefreq': NotRequired[str],
    'handle': NotRequired[str],
    'images': NotRequired[list[ModelShopifySitemapImage]],
    'lastmod': NotRequired[str],
    'loc': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelShopifySitemapUrlsResponse = TypedDict('ModelShopifySitemapUrlsResponse', {
    'limit': NotRequired[int],
    'source_url': NotRequired[str],
    'store_url': NotRequired[str],
    'type': NotRequired[str],
    'urls': NotRequired[list[ModelShopifySitemapUrlitem]],
}, total=False)

ModelShopifyStoreResponse = TypedDict('ModelShopifyStoreResponse', {
    'city': NotRequired[str],
    'country': NotRequired[str],
    'currency': NotRequired[str],
    'description': NotRequired[str],
    'domain': NotRequired[str],
    'myshopify_domain': NotRequired[str],
    'name': NotRequired[str],
    'province': NotRequired[str],
    'published_collections_count': NotRequired[int],
    'published_products_count': NotRequired[int],
    'requested_url': NotRequired[str],
    'source_domain': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelShopifyVariantItem = TypedDict('ModelShopifyVariantItem', {
    'available': NotRequired[bool],
    'barcode': NotRequired[str],
    'compare_at_price': NotRequired[float],
    'created_at': NotRequired[str],
    'featured_image': NotRequired[str],
    'grams': NotRequired[int],
    'id': NotRequired[str],
    'option1': NotRequired[str],
    'option2': NotRequired[str],
    'option3': NotRequired[str],
    'position': NotRequired[int],
    'price': NotRequired[float],
    'product_id': NotRequired[str],
    'requires_shipping': NotRequired[bool],
    'sku': NotRequired[str],
    'taxable': NotRequired[bool],
    'title': NotRequired[str],
    'updated_at': NotRequired[str],
}, total=False)

ModelShopifyCollectionProductsResponseDoc = TypedDict('ModelShopifyCollectionProductsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopifyCollectionProductsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopifyCollectionsResponseDoc = TypedDict('ModelShopifyCollectionsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopifyCollectionsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopifyPageResponseDoc = TypedDict('ModelShopifyPageResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopifyPageResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopifyPagesResponseDoc = TypedDict('ModelShopifyPagesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopifyPagesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopifyProductRecommendationsResponseDoc = TypedDict('ModelShopifyProductRecommendationsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopifyProductRecommendationsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopifyProductResponseDoc = TypedDict('ModelShopifyProductResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopifyProductResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopifyProductsResponseDoc = TypedDict('ModelShopifyProductsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopifyProductsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopifySearchSuggestResponseDoc = TypedDict('ModelShopifySearchSuggestResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopifySearchSuggestResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopifySitemapIndexResponseDoc = TypedDict('ModelShopifySitemapIndexResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopifySitemapIndexResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopifySitemapUrlsResponseDoc = TypedDict('ModelShopifySitemapUrlsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopifySitemapUrlsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelShopifyStoreResponseDoc = TypedDict('ModelShopifyStoreResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelShopifyStoreResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSimilarwebSearchResp = TypedDict('ModelSimilarwebSearchResp', {
    'apps': NotRequired[dict[str, Any]],
    'companies': NotRequired[list[dict[str, Any]]],
    'websites': NotRequired[list[dict[str, Any]]],
}, total=False)

ModelSimilarwebSimilarWebResp = TypedDict('ModelSimilarwebSimilarWebResp', {
    'Category': NotRequired[str],
    'CategoryRank': NotRequired[dict[str, Any]],
    'Competitors': NotRequired[dict[str, Any]],
    'Countries': NotRequired[list[dict[str, Any]]],
    'CountryRank': NotRequired[dict[str, Any]],
    'Description': NotRequired[str],
    'Engagments': NotRequired[dict[str, Any]],
    'EstimatedMonthlyVisits': NotRequired[dict[str, Any]],
    'GlobalCategoryRank': NotRequired[Any],
    'GlobalRank': NotRequired[dict[str, Any]],
    'IsDataFromGa': NotRequired[bool],
    'IsSmall': NotRequired[bool],
    'LargeScreenshot': NotRequired[str],
    'Notification': NotRequired[dict[str, Any]],
    'Policy': NotRequired[int],
    'SiteName': NotRequired[str],
    'SnapshotDate': NotRequired[str],
    'Title': NotRequired[str],
    'TopCountryShares': NotRequired[list[dict[str, Any]]],
    'TopKeywords': NotRequired[list[dict[str, Any]]],
    'TrafficSources': NotRequired[dict[str, Any]],
    'Version': NotRequired[int],
}, total=False)

ModelSimilarwebSearchResponseDoc = TypedDict('ModelSimilarwebSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSimilarwebSearchResp],
    'msg': NotRequired[str],
}, total=False)

ModelSimilarwebWebResponseDoc = TypedDict('ModelSimilarwebWebResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSimilarwebSimilarWebResp],
    'msg': NotRequired[str],
}, total=False)

ModelSpotifyAlbumMeta = TypedDict('ModelSpotifyAlbumMeta', {
    'appVersion': NotRequired[str],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
    'trackCount': NotRequired[int],
}, total=False)

ModelSpotifyAlbumResponse = TypedDict('ModelSpotifyAlbumResponse', {
    'albumType': NotRequired[str],
    'artists': NotRequired[list[ModelSpotifySearchResultSummary]],
    'copyrights': NotRequired[list[str]],
    'durationMs': NotRequired[int],
    'externalUrl': NotRequired[str],
    'id': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'isExplicit': NotRequired[bool],
    'isPlayable': NotRequired[bool],
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifyAlbumMeta],
    'name': NotRequired[str],
    'offset': NotRequired[int],
    'releaseDate': NotRequired[str],
    'shareUrl': NotRequired[str],
    'totalTracks': NotRequired[int],
    'tracks': NotRequired[list[ModelSpotifySearchResultSummary]],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyArtistAlbumsMeta = TypedDict('ModelSpotifyArtistAlbumsMeta', {
    'appVersion': NotRequired[str],
    'count': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
}, total=False)

ModelSpotifyArtistAlbumsResponse = TypedDict('ModelSpotifyArtistAlbumsResponse', {
    'id': NotRequired[str],
    'items': NotRequired[list[ModelSpotifySearchResultSummary]],
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifyArtistAlbumsMeta],
    'offset': NotRequired[int],
    'order': NotRequired[str],
    'total': NotRequired[int],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyArtistCollectionMeta = TypedDict('ModelSpotifyArtistCollectionMeta', {
    'appVersion': NotRequired[str],
    'count': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
}, total=False)

ModelSpotifyArtistCollectionResponse = TypedDict('ModelSpotifyArtistCollectionResponse', {
    'id': NotRequired[str],
    'items': NotRequired[list[ModelSpotifySearchResultSummary]],
    'meta': NotRequired[ModelSpotifyArtistCollectionMeta],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyArtistMeta = TypedDict('ModelSpotifyArtistMeta', {
    'appVersion': NotRequired[str],
    'discographyCount': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
    'playlistCount': NotRequired[int],
    'relatedCount': NotRequired[int],
    'topTrackCount': NotRequired[int],
}, total=False)

ModelSpotifyArtistResponse = TypedDict('ModelSpotifyArtistResponse', {
    'biography': NotRequired[str],
    'discography': NotRequired[list[ModelSpotifySearchResultSummary]],
    'externalUrl': NotRequired[str],
    'followers': NotRequired[int],
    'id': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'meta': NotRequired[ModelSpotifyArtistMeta],
    'monthlyUsers': NotRequired[int],
    'name': NotRequired[str],
    'playlists': NotRequired[list[ModelSpotifySearchResultSummary]],
    'related': NotRequired[list[ModelSpotifySearchResultSummary]],
    'shareUrl': NotRequired[str],
    'topTracks': NotRequired[list[ModelSpotifySearchResultSummary]],
    'type': NotRequired[str],
    'uri': NotRequired[str],
    'verified': NotRequired[bool],
}, total=False)

ModelSpotifyAudiobookChaptersMeta = TypedDict('ModelSpotifyAudiobookChaptersMeta', {
    'appVersion': NotRequired[str],
    'count': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
}, total=False)

ModelSpotifyAudiobookChaptersResponse = TypedDict('ModelSpotifyAudiobookChaptersResponse', {
    'chapters': NotRequired[list[ModelSpotifyPodcastEpisodeSummary]],
    'id': NotRequired[str],
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifyAudiobookChaptersMeta],
    'offset': NotRequired[int],
    'total': NotRequired[int],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyAudiobookMeta = TypedDict('ModelSpotifyAudiobookMeta', {
    'appVersion': NotRequired[str],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
}, total=False)

ModelSpotifyAudiobookResponse = TypedDict('ModelSpotifyAudiobookResponse', {
    'authors': NotRequired[list[str]],
    'description': NotRequired[str],
    'externalUrl': NotRequired[str],
    'id': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'isExplicit': NotRequired[bool],
    'mediaType': NotRequired[str],
    'meta': NotRequired[ModelSpotifyAudiobookMeta],
    'name': NotRequired[str],
    'narrators': NotRequired[list[str]],
    'publisher': NotRequired[str],
    'totalChapters': NotRequired[int],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyBrowsePageItem = TypedDict('ModelSpotifyBrowsePageItem', {
    'description': NotRequired[str],
    'externalUrl': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'publisher': NotRequired[str],
    'subtitle': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyBrowsePageMeta = TypedDict('ModelSpotifyBrowsePageMeta', {
    'appVersion': NotRequired[str],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
    'sectionCount': NotRequired[int],
}, total=False)

ModelSpotifyBrowsePageResponse = TypedDict('ModelSpotifyBrowsePageResponse', {
    'meta': NotRequired[ModelSpotifyBrowsePageMeta],
    'sections': NotRequired[list[ModelSpotifyBrowsePageSection]],
    'subtitle': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyBrowsePageSection = TypedDict('ModelSpotifyBrowsePageSection', {
    'items': NotRequired[list[ModelSpotifyBrowsePageItem]],
    'subtitle': NotRequired[str],
    'title': NotRequired[str],
    'totalCount': NotRequired[int],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyBrowseSectionMeta = TypedDict('ModelSpotifyBrowseSectionMeta', {
    'appVersion': NotRequired[str],
    'count': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
}, total=False)

ModelSpotifyBrowseSectionResponse = TypedDict('ModelSpotifyBrowseSectionResponse', {
    'items': NotRequired[list[ModelSpotifyBrowsePageItem]],
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifyBrowseSectionMeta],
    'offset': NotRequired[int],
    'subtitle': NotRequired[str],
    'title': NotRequired[str],
    'totalCount': NotRequired[int],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyChartItem = TypedDict('ModelSpotifyChartItem', {
    'description': NotRequired[str],
    'episodeDescription': NotRequired[str],
    'episodeExternalUrl': NotRequired[str],
    'episodeImageUrl': NotRequired[str],
    'episodeName': NotRequired[str],
    'episodeUri': NotRequired[str],
    'externalUrl': NotRequired[str],
    'imageUrl': NotRequired[str],
    'name': NotRequired[str],
    'publisher': NotRequired[str],
    'rank': NotRequired[int],
    'rankMove': NotRequired[str],
    'showDescription': NotRequired[str],
    'showExternalUrl': NotRequired[str],
    'showImageUrl': NotRequired[str],
    'showName': NotRequired[str],
    'showPublisher': NotRequired[str],
    'showUri': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyChartMeta = TypedDict('ModelSpotifyChartMeta', {
    'count': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'sourceUrl': NotRequired[str],
}, total=False)

ModelSpotifyChartResponse = TypedDict('ModelSpotifyChartResponse', {
    'chart': NotRequired[str],
    'chartName': NotRequired[str],
    'chartType': NotRequired[str],
    'items': NotRequired[list[ModelSpotifyChartItem]],
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifyChartMeta],
    'region': NotRequired[str],
    'regionName': NotRequired[str],
}, total=False)

ModelSpotifyCountryHubContentId = TypedDict('ModelSpotifyCountryHubContentId', {
    'id': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelSpotifyCountryHubContentMeta = TypedDict('ModelSpotifyCountryHubContentMeta', {
    'appVersion': NotRequired[str],
    'fetchedAt': NotRequired[str],
    'itemCount': NotRequired[int],
    'operationName': NotRequired[str],
}, total=False)

ModelSpotifyCountryHubContentResponse = TypedDict('ModelSpotifyCountryHubContentResponse', {
    'contentId': NotRequired[str],
    'countryCode': NotRequired[str],
    'countryName': NotRequired[str],
    'hexColor': NotRequired[str],
    'items': NotRequired[list[ModelSpotifyCountryHubItem]],
    'meta': NotRequired[ModelSpotifyCountryHubContentMeta],
    'supportedContentIds': NotRequired[list[ModelSpotifyCountryHubContentId]],
    'supportedCountries': NotRequired[list[ModelSpotifyPopularCountry]],
    'title': NotRequired[str],
}, total=False)

ModelSpotifyCountryHubItem = TypedDict('ModelSpotifyCountryHubItem', {
    'album': NotRequired[ModelSpotifySearchResultSummary],
    'artists': NotRequired[list[ModelSpotifySearchResultSummary]],
    'attributes': NotRequired[dict[str, str]],
    'description': NotRequired[str],
    'externalUrl': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'owner': NotRequired[ModelSpotifySearchResultSummary],
    'subtitle': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyCountryHubMeta = TypedDict('ModelSpotifyCountryHubMeta', {
    'appVersion': NotRequired[str],
    'fetchedAt': NotRequired[str],
    'itemCount': NotRequired[int],
    'operationName': NotRequired[str],
    'sectionCount': NotRequired[int],
}, total=False)

ModelSpotifyCountryHubResponse = TypedDict('ModelSpotifyCountryHubResponse', {
    'countryCode': NotRequired[str],
    'countryName': NotRequired[str],
    'hexColor': NotRequired[str],
    'meta': NotRequired[ModelSpotifyCountryHubMeta],
    'sections': NotRequired[list[ModelSpotifyCountryHubSection]],
    'supportedCountries': NotRequired[list[ModelSpotifyPopularCountry]],
}, total=False)

ModelSpotifyCountryHubSection = TypedDict('ModelSpotifyCountryHubSection', {
    'contentId': NotRequired[str],
    'items': NotRequired[list[ModelSpotifyCountryHubItem]],
    'title': NotRequired[str],
    'totalCount': NotRequired[int],
}, total=False)

ModelSpotifyHomeMeta = TypedDict('ModelSpotifyHomeMeta', {
    'appVersion': NotRequired[str],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
    'sectionCount': NotRequired[int],
}, total=False)

ModelSpotifyHomeResponse = TypedDict('ModelSpotifyHomeResponse', {
    'facet': NotRequired[str],
    'greeting': NotRequired[str],
    'meta': NotRequired[ModelSpotifyHomeMeta],
    'sections': NotRequired[list[ModelSpotifyBrowsePageSection]],
    'timeZone': NotRequired[str],
}, total=False)

ModelSpotifyImageAsset = TypedDict('ModelSpotifyImageAsset', {
    'height': NotRequired[int],
    'url': NotRequired[str],
    'width': NotRequired[int],
}, total=False)

ModelSpotifyPlaylistMeta = TypedDict('ModelSpotifyPlaylistMeta', {
    'appVersion': NotRequired[str],
    'episodeCount': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'itemCount': NotRequired[int],
    'operationName': NotRequired[str],
    'trackCount': NotRequired[int],
}, total=False)

ModelSpotifyPlaylistResponse = TypedDict('ModelSpotifyPlaylistResponse', {
    'collaborative': NotRequired[bool],
    'description': NotRequired[str],
    'episodes': NotRequired[list[ModelSpotifySearchResultSummary]],
    'externalUrl': NotRequired[str],
    'followers': NotRequired[int],
    'id': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'items': NotRequired[list[ModelSpotifySearchResultSummary]],
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifyPlaylistMeta],
    'name': NotRequired[str],
    'offset': NotRequired[int],
    'owner': NotRequired[ModelSpotifySearchResultSummary],
    'shareUrl': NotRequired[str],
    'total': NotRequired[int],
    'tracks': NotRequired[list[ModelSpotifySearchResultSummary]],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyPodcastEpisodeMeta = TypedDict('ModelSpotifyPodcastEpisodeMeta', {
    'appVersion': NotRequired[str],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
    'sourceUrl': NotRequired[str],
}, total=False)

ModelSpotifyPodcastEpisodeResponse = TypedDict('ModelSpotifyPodcastEpisodeResponse', {
    'description': NotRequired[str],
    'durationMs': NotRequired[int],
    'externalUrl': NotRequired[str],
    'htmlDescription': NotRequired[str],
    'id': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'isExplicit': NotRequired[bool],
    'isPaywallContent': NotRequired[bool],
    'isPlayable': NotRequired[bool],
    'mediaTypes': NotRequired[list[str]],
    'meta': NotRequired[ModelSpotifyPodcastEpisodeMeta],
    'name': NotRequired[str],
    'playabilityReason': NotRequired[str],
    'previewAudioUrl': NotRequired[str],
    'previewAudioUrls': NotRequired[list[str]],
    'previewVideoUrl': NotRequired[str],
    'releaseDate': NotRequired[str],
    'releaseDatePrecision': NotRequired[str],
    'shareUrl': NotRequired[str],
    'show': NotRequired[ModelSpotifyPodcastEpisodeShowSummary],
    'transcriptCount': NotRequired[int],
    'type': NotRequired[str],
    'unplayabilityReasons': NotRequired[list[str]],
    'uri': NotRequired[str],
    'videoThumbnailUrl': NotRequired[str],
    'videoThumbnails': NotRequired[list[ModelSpotifyImageAsset]],
}, total=False)

ModelSpotifyPodcastEpisodeShowSummary = TypedDict('ModelSpotifyPodcastEpisodeShowSummary', {
    'description': NotRequired[str],
    'externalUrl': NotRequired[str],
    'id': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'mediaType': NotRequired[str],
    'name': NotRequired[str],
    'publisher': NotRequired[str],
    'showTypes': NotRequired[list[str]],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyPodcastEpisodeSummary = TypedDict('ModelSpotifyPodcastEpisodeSummary', {
    'description': NotRequired[str],
    'durationMs': NotRequired[int],
    'externalUrl': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'isExplicit': NotRequired[bool],
    'isPlayable': NotRequired[bool],
    'name': NotRequired[str],
    'releaseDate': NotRequired[str],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyPodcastEpisodesMeta = TypedDict('ModelSpotifyPodcastEpisodesMeta', {
    'appVersion': NotRequired[str],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
}, total=False)

ModelSpotifyPodcastEpisodesResponse = TypedDict('ModelSpotifyPodcastEpisodesResponse', {
    'episodes': NotRequired[list[ModelSpotifyPodcastEpisodeSummary]],
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifyPodcastEpisodesMeta],
    'offset': NotRequired[int],
    'total': NotRequired[int],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyPopularCountry = TypedDict('ModelSpotifyPopularCountry', {
    'code': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelSpotifyRecommendationSummary = TypedDict('ModelSpotifyRecommendationSummary', {
    'description': NotRequired[str],
    'externalUrl': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'publisher': NotRequired[str],
    'subtitle': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifySearchMeta = TypedDict('ModelSpotifySearchMeta', {
    'albumCount': NotRequired[int],
    'appVersion': NotRequired[str],
    'artistCount': NotRequired[int],
    'audiobookCount': NotRequired[int],
    'episodeCount': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
    'playlistCount': NotRequired[int],
    'resultCount': NotRequired[int],
    'showCount': NotRequired[int],
    'topCount': NotRequired[int],
    'trackCount': NotRequired[int],
    'userCount': NotRequired[int],
}, total=False)

ModelSpotifySearchPodcastsMeta = TypedDict('ModelSpotifySearchPodcastsMeta', {
    'appVersion': NotRequired[str],
    'episodeCount': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
    'showCount': NotRequired[int],
    'topCount': NotRequired[int],
}, total=False)

ModelSpotifySearchPodcastsResponse = TypedDict('ModelSpotifySearchPodcastsResponse', {
    'episodes': NotRequired[list[ModelSpotifyPodcastEpisodeSummary]],
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifySearchPodcastsMeta],
    'offset': NotRequired[int],
    'searchTerm': NotRequired[str],
    'shows': NotRequired[list[ModelSpotifyRecommendationSummary]],
    'topResults': NotRequired[list[ModelSpotifySearchResultSummary]],
}, total=False)

ModelSpotifySearchResponse = TypedDict('ModelSpotifySearchResponse', {
    'albums': NotRequired[list[ModelSpotifySearchResultSummary]],
    'artists': NotRequired[list[ModelSpotifySearchResultSummary]],
    'audiobooks': NotRequired[list[ModelSpotifySearchResultSummary]],
    'episodes': NotRequired[list[ModelSpotifySearchResultSummary]],
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifySearchMeta],
    'offset': NotRequired[int],
    'playlists': NotRequired[list[ModelSpotifySearchResultSummary]],
    'results': NotRequired[list[ModelSpotifySearchResultSummary]],
    'searchTerm': NotRequired[str],
    'shows': NotRequired[list[ModelSpotifySearchResultSummary]],
    'topResults': NotRequired[list[ModelSpotifySearchResultSummary]],
    'tracks': NotRequired[list[ModelSpotifySearchResultSummary]],
    'users': NotRequired[list[ModelSpotifySearchResultSummary]],
}, total=False)

ModelSpotifySearchResultSummary = TypedDict('ModelSpotifySearchResultSummary', {
    'description': NotRequired[str],
    'externalUrl': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'publisher': NotRequired[str],
    'subtitle': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyShowMetadataMeta = TypedDict('ModelSpotifyShowMetadataMeta', {
    'appVersion': NotRequired[str],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
}, total=False)

ModelSpotifyShowMetadataResponse = TypedDict('ModelSpotifyShowMetadataResponse', {
    'description': NotRequired[str],
    'externalUrl': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'isExplicit': NotRequired[bool],
    'mediaType': NotRequired[str],
    'meta': NotRequired[ModelSpotifyShowMetadataMeta],
    'name': NotRequired[str],
    'publisher': NotRequired[str],
    'totalEpisodes': NotRequired[int],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyShowRecommendationsMeta = TypedDict('ModelSpotifyShowRecommendationsMeta', {
    'appVersion': NotRequired[str],
    'count': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
}, total=False)

ModelSpotifyShowRecommendationsResponse = TypedDict('ModelSpotifyShowRecommendationsResponse', {
    'meta': NotRequired[ModelSpotifyShowRecommendationsMeta],
    'recommendations': NotRequired[list[ModelSpotifyRecommendationSummary]],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyTrackMeta = TypedDict('ModelSpotifyTrackMeta', {
    'appVersion': NotRequired[str],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
}, total=False)

ModelSpotifyTrackRecommendedMeta = TypedDict('ModelSpotifyTrackRecommendedMeta', {
    'appVersion': NotRequired[str],
    'count': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
}, total=False)

ModelSpotifyTrackRecommendedResponse = TypedDict('ModelSpotifyTrackRecommendedResponse', {
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifyTrackRecommendedMeta],
    'recommendations': NotRequired[list[ModelSpotifyRecommendationSummary]],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyTrackResponse = TypedDict('ModelSpotifyTrackResponse', {
    'album': NotRequired[ModelSpotifySearchResultSummary],
    'artists': NotRequired[list[ModelSpotifySearchResultSummary]],
    'discNumber': NotRequired[int],
    'durationMs': NotRequired[int],
    'externalUrl': NotRequired[str],
    'id': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'isExplicit': NotRequired[bool],
    'isPlayable': NotRequired[bool],
    'meta': NotRequired[ModelSpotifyTrackMeta],
    'name': NotRequired[str],
    'playabilityReason': NotRequired[str],
    'playcount': NotRequired[str],
    'previewAudioUrl': NotRequired[str],
    'previewAudioUrls': NotRequired[list[str]],
    'shareUrl': NotRequired[str],
    'trackNumber': NotRequired[int],
    'type': NotRequired[str],
    'unplayabilityReasons': NotRequired[list[str]],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyTrackSimilarAlbumsMeta = TypedDict('ModelSpotifyTrackSimilarAlbumsMeta', {
    'appVersion': NotRequired[str],
    'count': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
}, total=False)

ModelSpotifyTrackSimilarAlbumsResponse = TypedDict('ModelSpotifyTrackSimilarAlbumsResponse', {
    'albums': NotRequired[list[ModelSpotifySearchResultSummary]],
    'albumsOnly': NotRequired[bool],
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifyTrackSimilarAlbumsMeta],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyUserProfileFollowersResponse = TypedDict('ModelSpotifyUserProfileFollowersResponse', {
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifyUserProfileMeta],
    'offset': NotRequired[int],
    'profiles': NotRequired[list[ModelSpotifyUserProfileSummary]],
    'total': NotRequired[int],
    'uri': NotRequired[str],
    'username': NotRequired[str],
}, total=False)

ModelSpotifyUserProfileMeta = TypedDict('ModelSpotifyUserProfileMeta', {
    'appVersion': NotRequired[str],
    'artistCount': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
    'playlistCount': NotRequired[int],
    'profileCount': NotRequired[int],
}, total=False)

ModelSpotifyUserProfilePlaylist = TypedDict('ModelSpotifyUserProfilePlaylist', {
    'externalUrl': NotRequired[str],
    'followersCount': NotRequired[int],
    'id': NotRequired[str],
    'imageUrl': NotRequired[str],
    'isFollowing': NotRequired[bool],
    'name': NotRequired[str],
    'ownerName': NotRequired[str],
    'ownerUri': NotRequired[str],
    'ownerUrl': NotRequired[str],
    'ownerUsername': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyUserProfilePlaylistsResponse = TypedDict('ModelSpotifyUserProfilePlaylistsResponse', {
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifyUserProfileMeta],
    'offset': NotRequired[int],
    'publicPlaylists': NotRequired[list[ModelSpotifyUserProfilePlaylist]],
    'totalPublicPlaylistsCount': NotRequired[int],
    'uri': NotRequired[str],
    'username': NotRequired[str],
}, total=False)

ModelSpotifyUserProfileResponse = TypedDict('ModelSpotifyUserProfileResponse', {
    'allowFollows': NotRequired[bool],
    'color': NotRequired[int],
    'externalUrl': NotRequired[str],
    'followersCount': NotRequired[int],
    'followingCount': NotRequired[int],
    'hasSpotifyImage': NotRequired[bool],
    'hasSpotifyName': NotRequired[bool],
    'imageUrl': NotRequired[str],
    'isCurrentUser': NotRequired[bool],
    'isVerified': NotRequired[bool],
    'meta': NotRequired[ModelSpotifyUserProfileMeta],
    'name': NotRequired[str],
    'publicPlaylists': NotRequired[list[ModelSpotifyUserProfilePlaylist]],
    'recentlyPlayedArtists': NotRequired[list[ModelSpotifyUserProfileSummary]],
    'showFollows': NotRequired[bool],
    'topArtists': NotRequired[ModelSpotifyUserProfileTopArtists],
    'totalPublicPlaylistsCount': NotRequired[int],
    'uri': NotRequired[str],
    'username': NotRequired[str],
}, total=False)

ModelSpotifyUserProfileSummary = TypedDict('ModelSpotifyUserProfileSummary', {
    'color': NotRequired[int],
    'externalUrl': NotRequired[str],
    'followersCount': NotRequired[int],
    'imageUrl': NotRequired[str],
    'isFollowing': NotRequired[bool],
    'name': NotRequired[str],
    'uri': NotRequired[str],
    'username': NotRequired[str],
}, total=False)

ModelSpotifyUserProfileTopArtists = TypedDict('ModelSpotifyUserProfileTopArtists', {
    'imageUrl': NotRequired[str],
    'subtitle': NotRequired[str],
    'title': NotRequired[str],
    'topArtistsPageUri': NotRequired[str],
}, total=False)

ModelSpotifyAlbumResponseDoc = TypedDict('ModelSpotifyAlbumResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyAlbumResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyArtistAlbumsResponseDoc = TypedDict('ModelSpotifyArtistAlbumsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyArtistAlbumsResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyArtistCollectionResponseDoc = TypedDict('ModelSpotifyArtistCollectionResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyArtistCollectionResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyArtistResponseDoc = TypedDict('ModelSpotifyArtistResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyArtistResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyAudiobookChaptersResponseDoc = TypedDict('ModelSpotifyAudiobookChaptersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyAudiobookChaptersResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyAudiobookResponseDoc = TypedDict('ModelSpotifyAudiobookResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyAudiobookResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyBrowsePageResponseDoc = TypedDict('ModelSpotifyBrowsePageResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyBrowsePageResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyBrowseSectionResponseDoc = TypedDict('ModelSpotifyBrowseSectionResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyBrowseSectionResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyChartsResponseDoc = TypedDict('ModelSpotifyChartsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyChartResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyCountryHubContentResponseDoc = TypedDict('ModelSpotifyCountryHubContentResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyCountryHubContentResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyCountryHubResponseDoc = TypedDict('ModelSpotifyCountryHubResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyCountryHubResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyEpisodeResponseDoc = TypedDict('ModelSpotifyEpisodeResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyPodcastEpisodeResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyHomeResponseDoc = TypedDict('ModelSpotifyHomeResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyHomeResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyPlaylistResponseDoc = TypedDict('ModelSpotifyPlaylistResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyPlaylistResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifySearchCatalogResponseDoc = TypedDict('ModelSpotifySearchCatalogResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifySearchResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifySearchResponseDoc = TypedDict('ModelSpotifySearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifySearchPodcastsResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyShowEpisodesResponseDoc = TypedDict('ModelSpotifyShowEpisodesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyPodcastEpisodesResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyShowRecommendationsResponseDoc = TypedDict('ModelSpotifyShowRecommendationsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyShowRecommendationsResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyShowResponseDoc = TypedDict('ModelSpotifyShowResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyShowMetadataResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyTrackRecommendedResponseDoc = TypedDict('ModelSpotifyTrackRecommendedResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyTrackRecommendedResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyTrackResponseDoc = TypedDict('ModelSpotifyTrackResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyTrackResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyTrackSimilarAlbumsResponseDoc = TypedDict('ModelSpotifyTrackSimilarAlbumsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyTrackSimilarAlbumsResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyUserProfileFollowersResponseDoc = TypedDict('ModelSpotifyUserProfileFollowersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyUserProfileFollowersResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyUserProfilePlaylistsResponseDoc = TypedDict('ModelSpotifyUserProfilePlaylistsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyUserProfilePlaylistsResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyUserProfileResponseDoc = TypedDict('ModelSpotifyUserProfileResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyUserProfileResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelTiktokCategory = TypedDict('ModelTiktokCategory', {
    'name': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelTiktokChallengeDetailResp = TypedDict('ModelTiktokChallengeDetailResp', {
    'challengeInfo': NotRequired[Any],
    'extra': NotRequired[dict[str, Any]],
    'log_pb': NotRequired[dict[str, Any]],
    'shareMeta': NotRequired[dict[str, Any]],
    'statusCode': NotRequired[int],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokChallengeListResp = TypedDict('ModelTiktokChallengeListResp', {
    'cursor': NotRequired[str],
    'extra': NotRequired[dict[str, Any]],
    'hasMore': NotRequired[bool],
    'itemList': NotRequired[list[Any]],
    'log_pb': NotRequired[dict[str, Any]],
    'statusCode': NotRequired[int],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokCommentResp = TypedDict('ModelTiktokCommentResp', {
    'alias_comment_deleted': NotRequired[bool],
    'comments': NotRequired[list[Any]],
    'cursor': NotRequired[int],
    'extra': NotRequired[dict[str, Any]],
    'has_filtered_comments': NotRequired[int],
    'has_more': NotRequired[int],
    'log_pb': NotRequired[dict[str, Any]],
    'reply_style': NotRequired[int],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'top_gifts': NotRequired[Any],
    'total': NotRequired[int],
}, total=False)

ModelTiktokExploreResp = TypedDict('ModelTiktokExploreResp', {
    'cursor': NotRequired[str],
    'extra': NotRequired[dict[str, Any]],
    'hasMore': NotRequired[bool],
    'itemList': NotRequired[list[Any]],
    'log_pb': NotRequired[dict[str, Any]],
    'statusCode': NotRequired[int],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokProfile = TypedDict('ModelTiktokProfile', {
    'stats': NotRequired[ModelTiktokProfileStats],
    'user': NotRequired[ModelTiktokUser],
}, total=False)

ModelTiktokProfileStats = TypedDict('ModelTiktokProfileStats', {
    'diggCount': NotRequired[int],
    'followerCount': NotRequired[int],
    'followingCount': NotRequired[int],
    'friendCount': NotRequired[int],
    'heart': NotRequired[int],
    'heartCount': NotRequired[int],
    'videoCount': NotRequired[int],
}, total=False)

ModelTiktokSearchHashtagResp = TypedDict('ModelTiktokSearchHashtagResp', {
    'challenge_list': NotRequired[list[Any]],
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'has_more': NotRequired[int],
    'input_keyword': NotRequired[str],
    'log_pb': NotRequired[dict[str, Any]],
    'music_list': NotRequired[Any],
    'qc': NotRequired[str],
    'rid': NotRequired[str],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'type': NotRequired[int],
    'user_list': NotRequired[Any],
}, total=False)

ModelTiktokSearchResp = TypedDict('ModelTiktokSearchResp', {
    'cursor': NotRequired[int],
    'data': NotRequired[list[Any]],
    'extra': NotRequired[Any],
    'feedback_type': NotRequired[str],
    'has_more': NotRequired[int],
    'input_keyword': NotRequired[str],
    'itemList': NotRequired[list[Any]],
    'log_pb': NotRequired[dict[str, Any]],
    'qc': NotRequired[str],
    'rid': NotRequired[str],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'type': NotRequired[int],
}, total=False)

ModelTiktokSearchUserResp = TypedDict('ModelTiktokSearchUserResp', {
    'challenge_list': NotRequired[Any],
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'feedback_type': NotRequired[str],
    'global_doodle_config': NotRequired[Any],
    'has_more': NotRequired[int],
    'input_keyword': NotRequired[str],
    'log_pb': NotRequired[dict[str, Any]],
    'music_list': NotRequired[Any],
    'qc': NotRequired[str],
    'rid': NotRequired[str],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'type': NotRequired[int],
    'user_list': NotRequired[list[Any]],
}, total=False)

ModelTiktokTrendingResp = TypedDict('ModelTiktokTrendingResp', {
    'cursor': NotRequired[str],
    'extra': NotRequired[dict[str, Any]],
    'hasMore': NotRequired[bool],
    'itemList': NotRequired[list[Any]],
    'log_pb': NotRequired[dict[str, Any]],
    'statusCode': NotRequired[int],
    'statusMsg': NotRequired[str],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'trendingTopics': NotRequired[list[Any]],
}, total=False)

ModelTiktokUser = TypedDict('ModelTiktokUser', {
    'avatarLarger': NotRequired[str],
    'bioLink': NotRequired[dict[str, Any]],
    'commerceUserInfo': NotRequired[dict[str, Any]],
    'createTime': NotRequired[int],
    'id': NotRequired[str],
    'isOrganization': NotRequired[int],
    'language': NotRequired[str],
    'nickname': NotRequired[str],
    'privateAccount': NotRequired[bool],
    'region': NotRequired[str],
    'secUid': NotRequired[str],
    'secret': NotRequired[bool],
    'signature': NotRequired[str],
    'ttSeller': NotRequired[bool],
    'uniqueId': NotRequired[str],
    'verified': NotRequired[bool],
}, total=False)

ModelTiktokUserPostLinkResp = TypedDict('ModelTiktokUserPostLinkResp', {
    'cursor': NotRequired[str],
    'extra': NotRequired[dict[str, Any]],
    'hasMore': NotRequired[bool],
    'itemList': NotRequired[list[Any]],
    'log_pb': NotRequired[dict[str, Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokVideoDetailResp = TypedDict('ModelTiktokVideoDetailResp', {
    'extra': NotRequired[dict[str, Any]],
    'itemInfo': NotRequired[Any],
    'log_pb': NotRequired[dict[str, Any]],
    'shareMeta': NotRequired[dict[str, Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokCategoryResponseDoc = TypedDict('ModelTiktokCategoryResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelTiktokCategory]],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokChallengeListResponseDoc = TypedDict('ModelTiktokChallengeListResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokChallengeListResp],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokChallengeResponseDoc = TypedDict('ModelTiktokChallengeResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokChallengeDetailResp],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokCommentsResponseDoc = TypedDict('ModelTiktokCommentsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokCommentResp],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokExploreResponseDoc = TypedDict('ModelTiktokExploreResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokExploreResp],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokPostResponseDoc = TypedDict('ModelTiktokPostResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokVideoDetailResp],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokProfilePostResponseDoc = TypedDict('ModelTiktokProfilePostResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokUserPostLinkResp],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokProfileResponseDoc = TypedDict('ModelTiktokProfileResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokProfile],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokSearchHashtagResponseDoc = TypedDict('ModelTiktokSearchHashtagResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokSearchHashtagResp],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokSearchResponseDoc = TypedDict('ModelTiktokSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokSearchResp],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokSearchUserResponseDoc = TypedDict('ModelTiktokSearchUserResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokSearchUserResp],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokTrendingResponseDoc = TypedDict('ModelTiktokTrendingResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokTrendingResp],
    'msg': NotRequired[str],
}, total=False)

ModelTrendsExploreQueriesResponse = TypedDict('ModelTrendsExploreQueriesResponse', {
    'category': NotRequired[int],
    'geo': NotRequired[str],
    'hl': NotRequired[str],
    'keywords': NotRequired[list[str]],
    'property': NotRequired[str],
    'queries': NotRequired[list[ModelTrendsRelatedGroup]],
    'query_type': NotRequired[str],
    'time_range': NotRequired[str],
    'type': NotRequired[str],
    'tz': NotRequired[int],
}, total=False)

ModelTrendsExploreRequest = TypedDict('ModelTrendsExploreRequest', {
    'category': NotRequired[int],
    'geo': NotRequired[Literal['WORLDWIDE', 'AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BV', 'BR', 'IO', 'VG', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CA', 'CV', 'BQ', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CW', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'SZ', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'XK', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'KP', 'MK', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'KR', 'SS', 'ES', 'LK', 'BL', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'SD', 'SR', 'SJ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UM', 'VI', 'UG', 'UA', 'AE', 'GB', 'US', 'UY', 'UZ', 'VU', 'VA', 'VE', 'VN', 'WF', 'EH', 'YE', 'ZM', 'ZW']],
    'hl': NotRequired[str],
    'keywords': NotRequired[list[str]],
    'property': NotRequired[str],
    'time_range': NotRequired[Literal['now 1-H', 'now 4-H', 'now 1-d', 'now 7-d', 'today 1-m', 'today 3-m', 'today 12-m', 'today 5-y', 'all']],
    'type': NotRequired[Literal['web', 'image', 'news', 'youtube', 'shopping']],
    'tz': NotRequired[int],
}, total=False)

ModelTrendsExploreResponse = TypedDict('ModelTrendsExploreResponse', {
    'category': NotRequired[int],
    'geo': NotRequired[str],
    'hl': NotRequired[str],
    'interest_by_region': NotRequired[list[ModelTrendsRegionInterest]],
    'interest_over_time': NotRequired[list[ModelTrendsInterestPoint]],
    'keywords': NotRequired[list[str]],
    'property': NotRequired[str],
    'related_queries': NotRequired[list[ModelTrendsRelatedGroup]],
    'related_topics': NotRequired[list[ModelTrendsRelatedGroup]],
    'rising_queries': NotRequired[list[ModelTrendsRelatedGroup]],
    'time_range': NotRequired[str],
    'top_queries': NotRequired[list[ModelTrendsRelatedGroup]],
    'type': NotRequired[str],
    'tz': NotRequired[int],
}, total=False)

ModelTrendsInterestByRegionResponse = TypedDict('ModelTrendsInterestByRegionResponse', {
    'category': NotRequired[int],
    'geo': NotRequired[str],
    'hl': NotRequired[str],
    'interest_by_region': NotRequired[list[ModelTrendsRegionInterest]],
    'keywords': NotRequired[list[str]],
    'property': NotRequired[str],
    'time_range': NotRequired[str],
    'type': NotRequired[str],
    'tz': NotRequired[int],
}, total=False)

ModelTrendsInterestOverTimeResponse = TypedDict('ModelTrendsInterestOverTimeResponse', {
    'category': NotRequired[int],
    'geo': NotRequired[str],
    'hl': NotRequired[str],
    'interest_over_time': NotRequired[list[ModelTrendsInterestPoint]],
    'keywords': NotRequired[list[str]],
    'property': NotRequired[str],
    'time_range': NotRequired[str],
    'type': NotRequired[str],
    'tz': NotRequired[int],
}, total=False)

ModelTrendsInterestPoint = TypedDict('ModelTrendsInterestPoint', {
    'formatted_axis_time': NotRequired[str],
    'formatted_time': NotRequired[str],
    'time': NotRequired[str],
    'values': NotRequired[list[ModelTrendsTrendValue]],
}, total=False)

ModelTrendsRegionInterest = TypedDict('ModelTrendsRegionInterest', {
    'geo_code': NotRequired[str],
    'geo_name': NotRequired[str],
    'values': NotRequired[list[ModelTrendsTrendValue]],
}, total=False)

ModelTrendsRelatedGroup = TypedDict('ModelTrendsRelatedGroup', {
    'items': NotRequired[list[ModelTrendsRelatedItem]],
    'keyword': NotRequired[str],
}, total=False)

ModelTrendsRelatedItem = TypedDict('ModelTrendsRelatedItem', {
    'formatted_value': NotRequired[str],
    'link': NotRequired[str],
    'query': NotRequired[str],
    'topic_mid': NotRequired[str],
    'topic_title': NotRequired[str],
    'topic_type': NotRequired[str],
    'value': NotRequired[int],
}, total=False)

ModelTrendsRelatedTopicsResponse = TypedDict('ModelTrendsRelatedTopicsResponse', {
    'category': NotRequired[int],
    'geo': NotRequired[str],
    'hl': NotRequired[str],
    'keywords': NotRequired[list[str]],
    'property': NotRequired[str],
    'related_topics': NotRequired[list[ModelTrendsRelatedGroup]],
    'time_range': NotRequired[str],
    'type': NotRequired[str],
    'tz': NotRequired[int],
}, total=False)

ModelTrendsTrendCategory = TypedDict('ModelTrendsTrendCategory', {
    'id': NotRequired[int],
    'name': NotRequired[str],
}, total=False)

ModelTrendsTrendValue = TypedDict('ModelTrendsTrendValue', {
    'formatted_value': NotRequired[str],
    'has_data': NotRequired[bool],
    'keyword': NotRequired[str],
    'value': NotRequired[int],
}, total=False)

ModelTrendsTrendingArticle = TypedDict('ModelTrendsTrendingArticle', {
    'source': NotRequired[str],
    'time': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelTrendsTrendingDetailRequest = TypedDict('ModelTrendsTrendingDetailRequest', {
    'category': NotRequired[int],
    'geo': NotRequired[Literal['WORLDWIDE', 'AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BV', 'BR', 'IO', 'VG', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CV', 'CA', 'BQ', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CW', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'SZ', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'XK', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'KP', 'MK', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'KR', 'SS', 'ES', 'LK', 'BL', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'SD', 'SR', 'SJ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UM', 'VI', 'UG', 'UA', 'AE', 'GB', 'US', 'UY', 'UZ', 'VU', 'VA', 'VE', 'VN', 'WF', 'EH', 'YE', 'ZM', 'ZW']],
    'hl': NotRequired[str],
    'property': NotRequired[str],
    'query': NotRequired[str],
    'time_range': NotRequired[Literal['now 1-H', 'now 4-H', 'now 1-d', 'now 7-d', 'today 1-m', 'today 3-m', 'today 12-m', 'today 5-y', 'all']],
    'type': NotRequired[Literal['web', 'image', 'news', 'youtube', 'shopping']],
    'tz': NotRequired[int],
}, total=False)

ModelTrendsTrendingItem = TypedDict('ModelTrendsTrendingItem', {
    'articles': NotRequired[list[ModelTrendsTrendingArticle]],
    'explore_url': NotRequired[str],
    'query': NotRequired[str],
    'rank': NotRequired[int],
    'related_terms': NotRequired[list[str]],
    'share_url': NotRequired[str],
    'started_unix': NotRequired[int],
    'status': NotRequired[str],
    'title': NotRequired[str],
    'traffic': NotRequired[str],
    'updated_unix': NotRequired[int],
}, total=False)

ModelTrendsTrendingResponse = TypedDict('ModelTrendsTrendingResponse', {
    'category': NotRequired[int],
    'geo': NotRequired[str],
    'hl': NotRequired[str],
    'items': NotRequired[list[ModelTrendsTrendingItem]],
    'sort_by': NotRequired[str],
    'status': NotRequired[str],
    'time_range': NotRequired[str],
    'tz': NotRequired[int],
    'window': NotRequired[str],
}, total=False)

ModelTrendsTrendsCategoriesResponse = TypedDict('ModelTrendsTrendsCategoriesResponse', {
    'categories': NotRequired[list[ModelTrendsTrendCategory]],
}, total=False)

ModelTrendsTrendsEnumsResponse = TypedDict('ModelTrendsTrendsEnumsResponse', {
    'explore_time_ranges': NotRequired[list[str]],
    'locations': NotRequired[list[str]],
    'search_types': NotRequired[list[str]],
    'trend_statuses': NotRequired[list[str]],
    'trending_categories': NotRequired[list[ModelTrendsTrendCategory]],
    'trending_sort_bys': NotRequired[list[str]],
    'trending_time_ranges': NotRequired[list[str]],
}, total=False)

ModelTrendsTrendsLocationsResponse = TypedDict('ModelTrendsTrendsLocationsResponse', {
    'locations': NotRequired[list[str]],
}, total=False)

ModelTrendsExploreQueriesResponseDoc = TypedDict('ModelTrendsExploreQueriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrendsExploreQueriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTrendsExploreResponseDoc = TypedDict('ModelTrendsExploreResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrendsExploreResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTrendsInterestByRegionResponseDoc = TypedDict('ModelTrendsInterestByRegionResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrendsInterestByRegionResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTrendsInterestOverTimeResponseDoc = TypedDict('ModelTrendsInterestOverTimeResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrendsInterestOverTimeResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTrendsRelatedTopicsResponseDoc = TypedDict('ModelTrendsRelatedTopicsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrendsRelatedTopicsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTrendsTrendingResponseDoc = TypedDict('ModelTrendsTrendingResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrendsTrendingResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTrendsTrendsCategoriesResponseDoc = TypedDict('ModelTrendsTrendsCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrendsTrendsCategoriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTrendsTrendsEnumsResponseDoc = TypedDict('ModelTrendsTrendsEnumsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrendsTrendsEnumsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTrendsTrendsLocationsResponseDoc = TypedDict('ModelTrendsTrendsLocationsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrendsTrendsLocationsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTripadvisorAutocompleteResponse = TypedDict('ModelTripadvisorAutocompleteResponse', {
    'locale': NotRequired[str],
    'query': NotRequired[str],
    'results': NotRequired[list[ModelTripadvisorSearchItem]],
    'scope_geo_id': NotRequired[int],
}, total=False)

ModelTripadvisorEnumsResponse = TypedDict('ModelTripadvisorEnumsResponse', {
    'attraction_categories': NotRequired[list[str]],
    'attraction_category_ids': NotRequired[dict[str, str]],
    'currencies': NotRequired[list[str]],
    'filter_ids': NotRequired[list[str]],
    'hotel_amenities': NotRequired[list[int]],
    'hotel_classes': NotRequired[list[int]],
    'languages': NotRequired[list[str]],
    'listing_types': NotRequired[list[str]],
    'locales': NotRequired[list[str]],
    'pricing_modes': NotRequired[list[str]],
    'restaurant_options': NotRequired[list[int]],
    'restaurant_types': NotRequired[list[int]],
    'sorts': NotRequired[list[str]],
    'unsupported_entity_types': NotRequired[list[str]],
}, total=False)

ModelTripadvisorHotelItem = TypedDict('ModelTripadvisorHotelItem', {
    'address': NotRequired[str],
    'currency': NotRequired[str],
    'id': NotRequired[str],
    'image': NotRequired[str],
    'latitude': NotRequired[float],
    'longitude': NotRequired[float],
    'parent': NotRequired[str],
    'phone': NotRequired[str],
    'price': NotRequired[str],
    'provider': NotRequired[str],
    'rank': NotRequired[int],
    'rank_label': NotRequired[str],
    'rating': NotRequired[float],
    'review_count': NotRequired[int],
    'review_rating': NotRequired[float],
    'review_snippet': NotRequired[str],
    'review_title': NotRequired[str],
    'star_rating': NotRequired[float],
    'tags': NotRequired[list[str]],
    'title': NotRequired[str],
    'type': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelTripadvisorHotelListResponse = TypedDict('ModelTripadvisorHotelListResponse', {
    'currency': NotRequired[str],
    'full_matches': NotRequired[int],
    'geo_id': NotRequired[int],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'results': NotRequired[list[ModelTripadvisorHotelItem]],
    'sort': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelTripadvisorNestedSearchItem = TypedDict('ModelTripadvisorNestedSearchItem', {
    'query': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelTripadvisorPlaceAddressParts = TypedDict('ModelTripadvisorPlaceAddressParts', {
    'country': NotRequired[str],
    'locality': NotRequired[str],
    'postal_code': NotRequired[str],
    'region': NotRequired[str],
    'street': NotRequired[str],
}, total=False)

ModelTripadvisorPlaceImage = TypedDict('ModelTripadvisorPlaceImage', {
    'caption': NotRequired[str],
    'height': NotRequired[int],
    'url': NotRequired[str],
    'width': NotRequired[int],
}, total=False)

ModelTripadvisorPlaceItem = TypedDict('ModelTripadvisorPlaceItem', {
    'address': NotRequired[str],
    'booking_url': NotRequired[str],
    'categories': NotRequired[list[str]],
    'cuisines': NotRequired[list[str]],
    'currency': NotRequired[str],
    'id': NotRequired[str],
    'image': NotRequired[str],
    'latitude': NotRequired[float],
    'longitude': NotRequired[float],
    'parent': NotRequired[str],
    'phone': NotRequired[str],
    'price': NotRequired[str],
    'price_level': NotRequired[str],
    'provider': NotRequired[str],
    'rank': NotRequired[int],
    'rank_label': NotRequired[str],
    'rating': NotRequired[float],
    'review_count': NotRequired[int],
    'review_rating': NotRequired[float],
    'review_snippet': NotRequired[str],
    'review_title': NotRequired[str],
    'star_rating': NotRequired[float],
    'tags': NotRequired[list[str]],
    'title': NotRequired[str],
    'type': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelTripadvisorPlaceLink = TypedDict('ModelTripadvisorPlaceLink', {
    'label': NotRequired[str],
    'type': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelTripadvisorPlaceResponse = TypedDict('ModelTripadvisorPlaceResponse', {
    'address': NotRequired[str],
    'address_parts': NotRequired[ModelTripadvisorPlaceAddressParts],
    'amenities': NotRequired[list[str]],
    'awards': NotRequired[list[str]],
    'breadcrumbs': NotRequired[list[str]],
    'canonical_url': NotRequired[str],
    'categories': NotRequired[list[str]],
    'cuisines': NotRequired[list[str]],
    'description': NotRequired[str],
    'features': NotRequired[list[str]],
    'geo_id': NotRequired[str],
    'id': NotRequired[str],
    'image': NotRequired[str],
    'images': NotRequired[list[ModelTripadvisorPlaceImage]],
    'latitude': NotRequired[float],
    'links': NotRequired[list[ModelTripadvisorPlaceLink]],
    'longitude': NotRequired[float],
    'opening_hours': NotRequired[list[str]],
    'phone': NotRequired[str],
    'price_level': NotRequired[str],
    'price_range': NotRequired[str],
    'rank': NotRequired[int],
    'rank_label': NotRequired[str],
    'rating': NotRequired[float],
    'reviews': NotRequired[int],
    'summary': NotRequired[str],
    'tags': NotRequired[list[str]],
    'title': NotRequired[str],
    'type': NotRequired[str],
    'url': NotRequired[str],
    'website_url': NotRequired[str],
}, total=False)

ModelTripadvisorReviewItem = TypedDict('ModelTripadvisorReviewItem', {
    'author': NotRequired[str],
    'author_avatar': NotRequired[str],
    'author_hometown': NotRequired[str],
    'author_id': NotRequired[str],
    'author_url': NotRequired[str],
    'created_date': NotRequired[str],
    'date': NotRequired[str],
    'helpful': NotRequired[int],
    'id': NotRequired[str],
    'language': NotRequired[str],
    'original_language': NotRequired[str],
    'photos': NotRequired[list[str]],
    'rating': NotRequired[float],
    'stay_date': NotRequired[str],
    'text': NotRequired[str],
    'title': NotRequired[str],
    'trip_type': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelTripadvisorReviewsResponse = TypedDict('ModelTripadvisorReviewsResponse', {
    'id': NotRequired[str],
    'language': NotRequired[str],
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'reviews': NotRequired[list[ModelTripadvisorReviewItem]],
    'total': NotRequired[int],
    'url': NotRequired[str],
}, total=False)

ModelTripadvisorSearchItem = TypedDict('ModelTripadvisorSearchItem', {
    'document_id': NotRequired[str],
    'id': NotRequired[str],
    'image': NotRequired[str],
    'latitude': NotRequired[float],
    'longitude': NotRequired[float],
    'nested_results': NotRequired[list[ModelTripadvisorNestedSearchItem]],
    'parent': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelTripadvisorSearchResponse = TypedDict('ModelTripadvisorSearchResponse', {
    'currency': NotRequired[str],
    'geo_id': NotRequired[int],
    'limit': NotRequired[int],
    'locale': NotRequired[str],
    'offset': NotRequired[int],
    'results': NotRequired[list[ModelTripadvisorPlaceItem]],
    'sort': NotRequired[str],
    'source': NotRequired[str],
    'type': NotRequired[str],
    'unsupported_types': NotRequired[list[str]],
}, total=False)

ModelTripadvisorTripadvisorAutocompleteResponseDoc = TypedDict('ModelTripadvisorTripadvisorAutocompleteResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTripadvisorAutocompleteResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTripadvisorTripadvisorEnumsResponseDoc = TypedDict('ModelTripadvisorTripadvisorEnumsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTripadvisorEnumsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTripadvisorTripadvisorHotelsResponseDoc = TypedDict('ModelTripadvisorTripadvisorHotelsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTripadvisorHotelListResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTripadvisorTripadvisorReviewsResponseDoc = TypedDict('ModelTripadvisorTripadvisorReviewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTripadvisorReviewsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTripadvisorTripadvisorSearchResponseDoc = TypedDict('ModelTripadvisorTripadvisorSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTripadvisorSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTrustpilotBusinessAbout = TypedDict('ModelTrustpilotBusinessAbout', {
    'business_country_code': NotRequired[str],
    'contact': NotRequired[ModelTrustpilotBusinessContact],
    'description_html': NotRequired[str],
    'description_text': NotRequired[str],
    'facebook_url': NotRequired[str],
    'has_company_elements': NotRequired[bool],
    'information_source': NotRequired[str],
    'promotion_points': NotRequired[list[str]],
    'promotion_title': NotRequired[str],
}, total=False)

ModelTrustpilotBusinessActivity = TypedDict('ModelTrustpilotBusinessActivity', {
    'claimed_date': NotRequired[str],
    'has_business_unit_merge_history': NotRequired[bool],
    'has_subscription': NotRequired[bool],
    'is_asking_for_reviews': NotRequired[bool],
    'is_claimed': NotRequired[bool],
    'is_using_ai_responses': NotRequired[bool],
    'is_using_paid_features': NotRequired[bool],
    'previously_claimed': NotRequired[bool],
    'verification': NotRequired[ModelTrustpilotBusinessVerification],
}, total=False)

ModelTrustpilotBusinessBreadcrumb = TypedDict('ModelTrustpilotBusinessBreadcrumb', {
    'id': NotRequired[str],
    'level': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelTrustpilotBusinessCategory = TypedDict('ModelTrustpilotBusinessCategory', {
    'cardinality': NotRequired[int],
    'id': NotRequired[str],
    'is_primary': NotRequired[bool],
    'name': NotRequired[str],
    'rank': NotRequired[int],
}, total=False)

ModelTrustpilotBusinessCompanyReply = TypedDict('ModelTrustpilotBusinessCompanyReply', {
    'message': NotRequired[str],
    'published_at_text': NotRequired[str],
    'updated_at_text': NotRequired[str],
}, total=False)

ModelTrustpilotBusinessContact = TypedDict('ModelTrustpilotBusinessContact', {
    'address': NotRequired[str],
    'city': NotRequired[str],
    'country': NotRequired[str],
    'email': NotRequired[str],
    'phone': NotRequired[str],
    'zip_code': NotRequired[str],
}, total=False)

ModelTrustpilotBusinessPageLanguage = TypedDict('ModelTrustpilotBusinessPageLanguage', {
    'iso_language': NotRequired[str],
    'language_code': NotRequired[str],
    'locale': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelTrustpilotBusinessPageMeta = TypedDict('ModelTrustpilotBusinessPageMeta', {
    'canonical_url': NotRequired[str],
    'domain': NotRequired[str],
    'languages': NotRequired[list[ModelTrustpilotBusinessPageLanguage]],
    'locale': NotRequired[str],
}, total=False)

ModelTrustpilotBusinessRatingHistogram = TypedDict('ModelTrustpilotBusinessRatingHistogram', {
    'five': NotRequired[int],
    'four': NotRequired[int],
    'one': NotRequired[int],
    'three': NotRequired[int],
    'total': NotRequired[int],
    'two': NotRequired[int],
}, total=False)

ModelTrustpilotBusinessRelatedResponse = TypedDict('ModelTrustpilotBusinessRelatedResponse', {
    'business': NotRequired[ModelTrustpilotBusinessHeader],
    'items': NotRequired[list[ModelTrustpilotRelatedBusiness]],
}, total=False)

ModelTrustpilotBusinessReplyMetrics = TypedDict('ModelTrustpilotBusinessReplyMetrics', {
    'average_days_to_reply': NotRequired[float],
    'last_reply_to_negative_review': NotRequired[str],
    'negative_reviews_with_replies': NotRequired[int],
    'reply_percentage': NotRequired[float],
    'total_negative_reviews': NotRequired[int],
}, total=False)

ModelTrustpilotBusinessResponse = TypedDict('ModelTrustpilotBusinessResponse', {
    'about': NotRequired[ModelTrustpilotBusinessAbout],
    'breadcrumbs': NotRequired[list[ModelTrustpilotBusinessBreadcrumb]],
    'categories': NotRequired[list[ModelTrustpilotBusinessCategory]],
    'claimed': NotRequired[bool],
    'company_activity': NotRequired[ModelTrustpilotBusinessActivity],
    'name': NotRequired[str],
    'page_meta': NotRequired[ModelTrustpilotBusinessPageMeta],
    'paid_subscription': NotRequired[bool],
    'rating': NotRequired[float],
    'rating_histogram': NotRequired[ModelTrustpilotBusinessRatingHistogram],
    'reply_metrics': NotRequired[ModelTrustpilotBusinessReplyMetrics],
    'review_count': NotRequired[int],
    'review_summary': NotRequired[ModelTrustpilotBusinessReviewSummary],
    'review_topics': NotRequired[list[ModelTrustpilotBusinessReviewTopic]],
    'slug': NotRequired[str],
    'trust_score': NotRequired[float],
    'trustpilot_url': NotRequired[str],
    'website_url': NotRequired[str],
}, total=False)

ModelTrustpilotBusinessReviewItem = TypedDict('ModelTrustpilotBusinessReviewItem', {
    'author_country': NotRequired[str],
    'author_name': NotRequired[str],
    'author_review_count': NotRequired[int],
    'body': NotRequired[str],
    'company_reply': NotRequired[ModelTrustpilotBusinessCompanyReply],
    'experienced_at_text': NotRequired[str],
    'id': NotRequired[str],
    'invited': NotRequired[bool],
    'labels': NotRequired[ModelTrustpilotBusinessReviewLabels],
    'published_at_text': NotRequired[str],
    'rating': NotRequired[int],
    'title': NotRequired[str],
    'updated_at_text': NotRequired[str],
    'verified': NotRequired[bool],
}, total=False)

ModelTrustpilotBusinessReviewLabels = TypedDict('ModelTrustpilotBusinessReviewLabels', {
    'filtered': NotRequired[bool],
    'merged': NotRequired[str],
    'pending': NotRequired[bool],
    'review_source': NotRequired[str],
    'verification_level': NotRequired[str],
    'verification_source': NotRequired[str],
}, total=False)

ModelTrustpilotBusinessReviewSummary = TypedDict('ModelTrustpilotBusinessReviewSummary', {
    'model_version': NotRequired[str],
    'status': NotRequired[str],
    'summary': NotRequired[str],
    'updated_at': NotRequired[str],
}, total=False)

ModelTrustpilotBusinessReviewTopic = TypedDict('ModelTrustpilotBusinessReviewTopic', {
    'model_version': NotRequired[str],
    'order': NotRequired[int],
    'summary': NotRequired[str],
    'topic': NotRequired[str],
    'updated_at': NotRequired[str],
}, total=False)

ModelTrustpilotBusinessReviewsAppliedFilters = TypedDict('ModelTrustpilotBusinessReviewsAppliedFilters', {
    'language': NotRequired[str],
    'query': NotRequired[str],
    'replied': NotRequired[bool],
    'stars': NotRequired[int],
    'verified': NotRequired[bool],
}, total=False)

ModelTrustpilotBusinessReviewsPagination = TypedDict('ModelTrustpilotBusinessReviewsPagination', {
    'has_next_page': NotRequired[bool],
    'next_page': NotRequired[int],
    'page': NotRequired[int],
    'per_page': NotRequired[int],
    'total_pages': NotRequired[int],
    'total_reviews': NotRequired[int],
}, total=False)

ModelTrustpilotBusinessReviewsResponse = TypedDict('ModelTrustpilotBusinessReviewsResponse', {
    'applied_filters': NotRequired[ModelTrustpilotBusinessReviewsAppliedFilters],
    'business': NotRequired[ModelTrustpilotBusinessHeader],
    'items': NotRequired[list[ModelTrustpilotBusinessReviewItem]],
    'pagination': NotRequired[ModelTrustpilotBusinessReviewsPagination],
}, total=False)

ModelTrustpilotBusinessVerification = TypedDict('ModelTrustpilotBusinessVerification', {
    'verified_by_google': NotRequired[bool],
    'verified_payment_method': NotRequired[bool],
    'verified_user_identity': NotRequired[bool],
}, total=False)

ModelTrustpilotCategoriesResponse = TypedDict('ModelTrustpilotCategoriesResponse', {
    'groups': NotRequired[list[ModelTrustpilotCategoryGroup]],
}, total=False)

ModelTrustpilotCategoryBusiness = TypedDict('ModelTrustpilotCategoryBusiness', {
    'business_unit_id': NotRequired[str],
    'categories': NotRequired[list[ModelTrustpilotCategoryBusinessTag]],
    'display_name': NotRequired[str],
    'email': NotRequired[str],
    'identifying_name': NotRequired[str],
    'location': NotRequired[ModelTrustpilotCategoryBusinessLocation],
    'logo_url': NotRequired[str],
    'phone': NotRequired[str],
    'recommended': NotRequired[bool],
    'review_count': NotRequired[int],
    'stars': NotRequired[float],
    'trust_score': NotRequired[float],
    'trustpilot_url': NotRequired[str],
    'website_url': NotRequired[str],
}, total=False)

ModelTrustpilotCategoryBusinessLocation = TypedDict('ModelTrustpilotCategoryBusinessLocation', {
    'address': NotRequired[str],
    'city': NotRequired[str],
    'country': NotRequired[str],
    'zip_code': NotRequired[str],
}, total=False)

ModelTrustpilotCategoryBusinessTag = TypedDict('ModelTrustpilotCategoryBusinessTag', {
    'category_id': NotRequired[str],
    'display_name': NotRequired[str],
    'is_predicted': NotRequired[bool],
    'is_primary': NotRequired[bool],
}, total=False)

ModelTrustpilotCategoryGroup = TypedDict('ModelTrustpilotCategoryGroup', {
    'items': NotRequired[list[ModelTrustpilotCategoryLink]],
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelTrustpilotCategoryLink = TypedDict('ModelTrustpilotCategoryLink', {
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelTrustpilotCategoryPagination = TypedDict('ModelTrustpilotCategoryPagination', {
    'has_next_page': NotRequired[bool],
    'next_page': NotRequired[int],
    'page': NotRequired[int],
    'per_page': NotRequired[int],
    'total_hits': NotRequired[int],
    'total_pages': NotRequired[int],
}, total=False)

ModelTrustpilotCategoryResponse = TypedDict('ModelTrustpilotCategoryResponse', {
    'breadcrumbs': NotRequired[list[ModelTrustpilotCategoryLink]],
    'country': NotRequired[str],
    'items': NotRequired[list[ModelTrustpilotCategoryBusiness]],
    'name': NotRequired[str],
    'newest_companies': NotRequired[list[ModelTrustpilotCategoryBusiness]],
    'page': NotRequired[int],
    'pagination': NotRequired[ModelTrustpilotCategoryPagination],
    'recently_reviewed_companies': NotRequired[list[ModelTrustpilotCategoryBusiness]],
    'related_categories': NotRequired[list[ModelTrustpilotCategoryLink]],
    'slug': NotRequired[str],
    'sort': NotRequired[str],
    'trustpilot_url': NotRequired[str],
}, total=False)

ModelTrustpilotCategorySearchResponse = TypedDict('ModelTrustpilotCategorySearchResponse', {
    'categories': NotRequired[list[ModelTrustpilotCategorySearchResult]],
    'country': NotRequired[str],
    'locale': NotRequired[str],
    'query': NotRequired[str],
    'size': NotRequired[int],
}, total=False)

ModelTrustpilotCategorySearchResult = TypedDict('ModelTrustpilotCategorySearchResult', {
    'category_id': NotRequired[str],
    'display_name': NotRequired[str],
    'top_level_category_id': NotRequired[str],
}, total=False)

ModelTrustpilotRelatedBusiness = TypedDict('ModelTrustpilotRelatedBusiness', {
    'business_unit_id': NotRequired[str],
    'display_name': NotRequired[str],
    'identifying_name': NotRequired[str],
    'logo_url': NotRequired[str],
    'review_count': NotRequired[int],
    'source': NotRequired[str],
    'stars': NotRequired[float],
    'trust_score': NotRequired[float],
    'trustpilot_url': NotRequired[str],
}, total=False)

ModelTrustpilotSearchAddress = TypedDict('ModelTrustpilotSearchAddress', {
    'approximate_area': NotRequired[ModelTrustpilotSearchAreaBounds],
    'city': NotRequired[str],
    'coordinates': NotRequired[ModelTrustpilotSearchCoordinates],
    'country': NotRequired[str],
    'country_code': NotRequired[str],
    'postcode': NotRequired[str],
    'street': NotRequired[str],
}, total=False)

ModelTrustpilotSearchAreaBounds = TypedDict('ModelTrustpilotSearchAreaBounds', {
    'north_west': NotRequired[ModelTrustpilotSearchCoordinates],
    'south_east': NotRequired[ModelTrustpilotSearchCoordinates],
}, total=False)

ModelTrustpilotSearchCategory = TypedDict('ModelTrustpilotSearchCategory', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'primary': NotRequired[bool],
}, total=False)

ModelTrustpilotSearchCoordinates = TypedDict('ModelTrustpilotSearchCoordinates', {
    'lat': NotRequired[float],
    'lon': NotRequired[float],
}, total=False)

ModelTrustpilotSearchResponse = TypedDict('ModelTrustpilotSearchResponse', {
    'country': NotRequired[str],
    'items': NotRequired[list[ModelTrustpilotSearchResult]],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
    'query': NotRequired[str],
    'search_mode': NotRequired[str],
    'total_hits': NotRequired[int],
    'total_pages': NotRequired[int],
}, total=False)

ModelTrustpilotSearchResult = TypedDict('ModelTrustpilotSearchResult', {
    'address': NotRequired[ModelTrustpilotSearchAddress],
    'business_unit_id': NotRequired[str],
    'categories': NotRequired[list[ModelTrustpilotSearchCategory]],
    'country_code': NotRequired[str],
    'display_name': NotRequired[str],
    'email': NotRequired[str],
    'identifying_name': NotRequired[str],
    'logo_url': NotRequired[str],
    'phone': NotRequired[str],
    'predicted_top_category': NotRequired[ModelTrustpilotSearchCategory],
    'review_count': NotRequired[int],
    'stars': NotRequired[float],
    'trust_score': NotRequired[float],
    'trustpilot_url': NotRequired[str],
    'verified': NotRequired[bool],
    'website_url': NotRequired[str],
}, total=False)

ModelTrustpilotBusinessHeader = TypedDict('ModelTrustpilotBusinessHeader', {
    'claimed': NotRequired[bool],
    'name': NotRequired[str],
    'rating': NotRequired[float],
    'review_count': NotRequired[int],
    'slug': NotRequired[str],
    'trust_score': NotRequired[float],
    'trustpilot_url': NotRequired[str],
    'website_url': NotRequired[str],
}, total=False)

ModelTrustpilotBusinessProfileResponseDoc = TypedDict('ModelTrustpilotBusinessProfileResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrustpilotBusinessResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTrustpilotBusinessRelatedResponseDoc = TypedDict('ModelTrustpilotBusinessRelatedResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrustpilotBusinessRelatedResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTrustpilotBusinessReviewsResponseDoc = TypedDict('ModelTrustpilotBusinessReviewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrustpilotBusinessReviewsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTrustpilotBusinessSearchResponseDoc = TypedDict('ModelTrustpilotBusinessSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrustpilotSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTrustpilotCategoriesResponseDoc = TypedDict('ModelTrustpilotCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrustpilotCategoriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTrustpilotCategoryResponseDoc = TypedDict('ModelTrustpilotCategoryResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrustpilotCategoryResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTrustpilotCategorySearchResponseDoc = TypedDict('ModelTrustpilotCategorySearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrustpilotCategorySearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelUsageUsageBillingStateDoc = TypedDict('ModelUsageUsageBillingStateDoc', {
    'allow_overage': NotRequired[bool],
    'created_at': NotRequired[str],
    'credits_remaining': NotRequired[int],
    'credits_used': NotRequired[int],
    'currency': NotRequired[str],
    'daily_credit_limit': NotRequired[int],
    'daily_credits_remaining': NotRequired[int],
    'daily_credits_used': NotRequired[int],
    'daily_key': NotRequired[str],
    'expected_subscription_amount_cents': NotRequired[int],
    'expected_total_amount_cents': NotRequired[int],
    'hard_limit': NotRequired[bool],
    'included_credits': NotRequired[int],
    'overage_credits': NotRequired[int],
    'period_end': NotRequired[str],
    'period_key': NotRequired[str],
    'period_start': NotRequired[str],
    'plan': NotRequired[str],
    'pricing_source': NotRequired[str],
    'subscription_price_cents': NotRequired[int],
    'updated_at': NotRequired[str],
    'user_id': NotRequired[str],
}, total=False)

ModelUsageUsageEndpointItemDoc = TypedDict('ModelUsageUsageEndpointItemDoc', {
    'charged_requests': NotRequired[int],
    'credits': NotRequired[int],
    'endpoint': NotRequired[str],
    'failed_requests': NotRequired[int],
    'non_billable_requests': NotRequired[int],
    'overage': NotRequired[int],
    'requests': NotRequired[int],
}, total=False)

ModelUsageUsageEndpointsDoc = TypedDict('ModelUsageUsageEndpointsDoc', {
    'from': NotRequired[str],
    'items': NotRequired[list[ModelUsageUsageEndpointItemDoc]],
    'range': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

ModelUsageUsageEndpointsResponseDoc = TypedDict('ModelUsageUsageEndpointsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelUsageUsageEndpointsDoc],
    'msg': NotRequired[str],
}, total=False)

ModelUsageUsageOverviewDoc = TypedDict('ModelUsageUsageOverviewDoc', {
    'billing': NotRequired[ModelUsageUsageBillingStateDoc],
    'from': NotRequired[str],
    'range': NotRequired[str],
    'requests': NotRequired[ModelUsageUsageRequestSummaryDoc],
    'to': NotRequired[str],
    'usage': NotRequired[ModelUsageUsageWindowSummaryDoc],
}, total=False)

ModelUsageUsageOverviewResponseDoc = TypedDict('ModelUsageUsageOverviewResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelUsageUsageOverviewDoc],
    'msg': NotRequired[str],
}, total=False)

ModelUsageUsageRecentIpitemDoc = TypedDict('ModelUsageUsageRecentIpitemDoc', {
    'error_count': NotRequired[int],
    'ip': NotRequired[str],
    'last_seen_at': NotRequired[str],
    'last_user_agent': NotRequired[str],
    'request_count': NotRequired[int],
    'success_count': NotRequired[int],
}, total=False)

ModelUsageUsageRecentIpsDoc = TypedDict('ModelUsageUsageRecentIpsDoc', {
    'from': NotRequired[str],
    'items': NotRequired[list[ModelUsageUsageRecentIpitemDoc]],
    'range': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

ModelUsageUsageRecentIpsResponseDoc = TypedDict('ModelUsageUsageRecentIpsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelUsageUsageRecentIpsDoc],
    'msg': NotRequired[str],
}, total=False)

ModelUsageUsageRequestSummaryDoc = TypedDict('ModelUsageUsageRequestSummaryDoc', {
    'avg_latency_ms': NotRequired[float],
    'distinct_ip_count': NotRequired[int],
    'error_requests': NotRequired[int],
    'last_request_at': NotRequired[str],
    'requests': NotRequired[int],
    'success_requests': NotRequired[int],
}, total=False)

ModelUsageUsageTimeseriesDoc = TypedDict('ModelUsageUsageTimeseriesDoc', {
    'bucket': NotRequired[str],
    'from': NotRequired[str],
    'items': NotRequired[list[ModelUsageUsageTimeseriesItemDoc]],
    'range': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

ModelUsageUsageTimeseriesItemDoc = TypedDict('ModelUsageUsageTimeseriesItemDoc', {
    'bucket_end': NotRequired[str],
    'bucket_start': NotRequired[str],
    'charged_requests': NotRequired[int],
    'credits': NotRequired[int],
    'failed_requests': NotRequired[int],
    'non_billable_requests': NotRequired[int],
    'overage': NotRequired[int],
    'requests': NotRequired[int],
}, total=False)

ModelUsageUsageTimeseriesResponseDoc = TypedDict('ModelUsageUsageTimeseriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelUsageUsageTimeseriesDoc],
    'msg': NotRequired[str],
}, total=False)

ModelUsageUsageWindowSummaryDoc = TypedDict('ModelUsageUsageWindowSummaryDoc', {
    'charged_requests': NotRequired[int],
    'credits': NotRequired[int],
    'failed_requests': NotRequired[int],
    'non_billable_requests': NotRequired[int],
    'overage': NotRequired[int],
    'requests': NotRequired[int],
}, total=False)

ModelUserUserApikeyItemDoc = TypedDict('ModelUserUserApikeyItemDoc', {
    'created_at': NotRequired[str],
    'expires_at': NotRequired[str],
    'id': NotRequired[str],
    'key_prefix': NotRequired[str],
    'key_suffix': NotRequired[str],
    'last_used_at': NotRequired[str],
    'last_used_ip': NotRequired[str],
    'masked_key': NotRequired[str],
    'rotated_at': NotRequired[str],
    'source': NotRequired[str],
    'status': NotRequired[str],
    'updated_at': NotRequired[str],
}, total=False)

ModelUserUserApikeysDoc = TypedDict('ModelUserUserApikeysDoc', {
    'items': NotRequired[list[ModelUserUserApikeyItemDoc]],
}, total=False)

ModelUserUserApikeysResponseDoc = TypedDict('ModelUserUserApikeysResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelUserUserApikeysDoc],
    'msg': NotRequired[str],
}, total=False)

ModelUserUserMeDoc = TypedDict('ModelUserUserMeDoc', {
    'email': NotRequired[str],
    'id': NotRequired[str],
    'plan': NotRequired[str],
    'username': NotRequired[str],
}, total=False)

ModelUserUserMeResponseDoc = TypedDict('ModelUserUserMeResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelUserUserMeDoc],
    'msg': NotRequired[str],
}, total=False)

ModelUserUserRevealApikeyDoc = TypedDict('ModelUserUserRevealApikeyDoc', {
    'api_key': NotRequired[str],
    'key': NotRequired[ModelUserUserApikeyItemDoc],
}, total=False)

ModelUserUserRevealApikeyResponseDoc = TypedDict('ModelUserUserRevealApikeyResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelUserUserRevealApikeyDoc],
    'msg': NotRequired[str],
}, total=False)

ModelUserUserRotateApikeyDoc = TypedDict('ModelUserUserRotateApikeyDoc', {
    'active_key': NotRequired[ModelUserUserApikeyItemDoc],
    'grace_period_seconds': NotRequired[int],
    'new_api_key': NotRequired[str],
    'previous_key': NotRequired[ModelUserUserApikeyItemDoc],
}, total=False)

ModelUserUserRotateApikeyResponseDoc = TypedDict('ModelUserUserRotateApikeyResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelUserUserRotateApikeyDoc],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceActionEvents = TypedDict('ModelYahoofinanceActionEvents', {
    'capital_gains': NotRequired[list[dict[str, Any]]],
    'dividends': NotRequired[list[dict[str, Any]]],
    'splits': NotRequired[list[dict[str, Any]]],
}, total=False)

ModelYahoofinanceCalendarResponse = TypedDict('ModelYahoofinanceCalendarResponse', {
    'end': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'rows': NotRequired[list[dict[str, Any]]],
    'start': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelYahoofinanceCalendarsResponse = TypedDict('ModelYahoofinanceCalendarsResponse', {
    'calendars': NotRequired[list[str]],
}, total=False)

ModelYahoofinanceDomainListResponse = TypedDict('ModelYahoofinanceDomainListResponse', {
    'items': NotRequired[list[ModelYahoofinanceDomainRef]],
}, total=False)

ModelYahoofinanceDomainRef = TypedDict('ModelYahoofinanceDomainRef', {
    'key': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelYahoofinanceDownloadRequest = TypedDict('ModelYahoofinanceDownloadRequest', {
    'auto_adjust': NotRequired[bool],
    'back_adjust': NotRequired[bool],
    'end': NotRequired[str],
    'include_actions': NotRequired[bool],
    'include_prepost': NotRequired[bool],
    'interval': NotRequired[str],
    'keepna': NotRequired[bool],
    'period': NotRequired[str],
    'rounding': NotRequired[bool],
    'start': NotRequired[str],
    'symbols': Required[list[str]],
}, total=False)

ModelYahoofinanceDownloadResponse = TypedDict('ModelYahoofinanceDownloadResponse', {
    'results': NotRequired[list[ModelYahoofinanceDownloadResult]],
}, total=False)

ModelYahoofinanceDownloadResult = TypedDict('ModelYahoofinanceDownloadResult', {
    'error': NotRequired[str],
    'history': NotRequired[ModelYahoofinanceHistoryResponse],
    'symbol': NotRequired[str],
}, total=False)

ModelYahoofinanceEarningsDatesResponse = TypedDict('ModelYahoofinanceEarningsDatesResponse', {
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'rows': NotRequired[list[dict[str, Any]]],
    'symbol': NotRequired[str],
}, total=False)

ModelYahoofinanceFinancialsResponse = TypedDict('ModelYahoofinanceFinancialsResponse', {
    'modules': NotRequired[dict[str, Any]],
    'period': NotRequired[str],
    'statement': NotRequired[str],
    'symbol': NotRequired[str],
}, total=False)

ModelYahoofinanceHistoryMetadataResponse = TypedDict('ModelYahoofinanceHistoryMetadataResponse', {
    'meta': NotRequired[dict[str, Any]],
    'symbol': NotRequired[str],
}, total=False)

ModelYahoofinanceHistoryResponse = TypedDict('ModelYahoofinanceHistoryResponse', {
    'events': NotRequired[ModelYahoofinanceActionEvents],
    'meta': NotRequired[dict[str, Any]],
    'points': NotRequired[list[ModelYahoofinancePricePoint]],
    'symbol': NotRequired[str],
}, total=False)

ModelYahoofinanceIsinresponse = TypedDict('ModelYahoofinanceIsinresponse', {
    'isin': NotRequired[str],
    'symbol': NotRequired[str],
}, total=False)

ModelYahoofinanceIndustryResponse = TypedDict('ModelYahoofinanceIndustryResponse', {
    'key': NotRequired[str],
    'name': NotRequired[str],
    'overview': NotRequired[dict[str, Any]],
    'research_reports': NotRequired[list[dict[str, Any]]],
    'sector_key': NotRequired[str],
    'sector_name': NotRequired[str],
    'symbol': NotRequired[str],
    'top_companies': NotRequired[list[dict[str, Any]]],
    'top_growth_companies': NotRequired[list[dict[str, Any]]],
    'top_performing_companies': NotRequired[list[dict[str, Any]]],
}, total=False)

ModelYahoofinanceInfoResponse = TypedDict('ModelYahoofinanceInfoResponse', {
    'modules': NotRequired[dict[str, Any]],
    'symbol': NotRequired[str],
}, total=False)

ModelYahoofinanceMarketStatusResponse = TypedDict('ModelYahoofinanceMarketStatusResponse', {
    'market': NotRequired[str],
    'status': NotRequired[dict[str, Any]],
}, total=False)

ModelYahoofinanceMarketSummaryResponse = TypedDict('ModelYahoofinanceMarketSummaryResponse', {
    'market': NotRequired[str],
    'summary': NotRequired[list[dict[str, Any]]],
}, total=False)

ModelYahoofinanceModuleResponse = TypedDict('ModelYahoofinanceModuleResponse', {
    'modules': NotRequired[dict[str, Any]],
    'symbol': NotRequired[str],
}, total=False)

ModelYahoofinanceOptionExpiration = TypedDict('ModelYahoofinanceOptionExpiration', {
    'calls': NotRequired[list[dict[str, Any]]],
    'expiration_date': NotRequired[int],
    'puts': NotRequired[list[dict[str, Any]]],
}, total=False)

ModelYahoofinanceOptionsResponse = TypedDict('ModelYahoofinanceOptionsResponse', {
    'expiration_dates': NotRequired[list[int]],
    'options': NotRequired[list[ModelYahoofinanceOptionExpiration]],
    'symbol': NotRequired[str],
    'underlying': NotRequired[dict[str, Any]],
}, total=False)

ModelYahoofinancePricePoint = TypedDict('ModelYahoofinancePricePoint', {
    'adj_close': NotRequired[float],
    'close': NotRequired[float],
    'datetime': NotRequired[str],
    'high': NotRequired[float],
    'low': NotRequired[float],
    'open': NotRequired[float],
    'timestamp': NotRequired[int],
    'volume': NotRequired[int],
}, total=False)

ModelYahoofinanceQuoteResponse = TypedDict('ModelYahoofinanceQuoteResponse', {
    'quotes': NotRequired[list[dict[str, Any]]],
    'symbols': NotRequired[list[str]],
}, total=False)

ModelYahoofinanceScreenerRequest = TypedDict('ModelYahoofinanceScreenerRequest', {
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'query': Required[dict[str, Any]],
    'quote_type': NotRequired[str],
    'sort_asc': NotRequired[bool],
    'sort_field': NotRequired[str],
}, total=False)

ModelYahoofinanceScreenerResponse = TypedDict('ModelYahoofinanceScreenerResponse', {
    'description': NotRequired[str],
    'id': NotRequired[str],
    'meta': NotRequired[dict[str, Any]],
    'quotes': NotRequired[list[dict[str, Any]]],
    'title': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelYahoofinanceScreenersResponse = TypedDict('ModelYahoofinanceScreenersResponse', {
    'screeners': NotRequired[list[str]],
}, total=False)

ModelYahoofinanceSearchResponse = TypedDict('ModelYahoofinanceSearchResponse', {
    'lists': NotRequired[list[dict[str, Any]]],
    'news': NotRequired[list[dict[str, Any]]],
    'query': NotRequired[str],
    'quotes': NotRequired[list[dict[str, Any]]],
    'research': NotRequired[list[dict[str, Any]]],
}, total=False)

ModelYahoofinanceSectorResponse = TypedDict('ModelYahoofinanceSectorResponse', {
    'industries': NotRequired[list[dict[str, Any]]],
    'key': NotRequired[str],
    'name': NotRequired[str],
    'overview': NotRequired[dict[str, Any]],
    'research_reports': NotRequired[list[dict[str, Any]]],
    'symbol': NotRequired[str],
    'top_companies': NotRequired[list[dict[str, Any]]],
    'top_etfs': NotRequired[dict[str, str]],
    'top_mutual_funds': NotRequired[dict[str, str]],
}, total=False)

ModelYahoofinanceSharesFullResponse = TypedDict('ModelYahoofinanceSharesFullResponse', {
    'end': NotRequired[str],
    'points': NotRequired[list[dict[str, Any]]],
    'start': NotRequired[str],
    'symbol': NotRequired[str],
}, total=False)

ModelYahoofinanceSharesResponse = TypedDict('ModelYahoofinanceSharesResponse', {
    'shares': NotRequired[dict[str, Any]],
    'symbol': NotRequired[str],
}, total=False)

ModelYahoofinanceTrendingResponse = TypedDict('ModelYahoofinanceTrendingResponse', {
    'count': NotRequired[int],
    'job_timestamp': NotRequired[int],
    'region': NotRequired[str],
    'start_interval': NotRequired[int],
    'symbols': NotRequired[list[str]],
}, total=False)

ModelYahoofinanceValuationResponse = TypedDict('ModelYahoofinanceValuationResponse', {
    'headers': NotRequired[list[str]],
    'rows': NotRequired[list[dict[str, Any]]],
    'symbol': NotRequired[str],
}, total=False)

ModelYahoofinanceActionsResponseDoc = TypedDict('ModelYahoofinanceActionsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceActionEvents],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceCalendarResponseDoc = TypedDict('ModelYahoofinanceCalendarResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceCalendarResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceCalendarsResponseDoc = TypedDict('ModelYahoofinanceCalendarsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceCalendarsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceDomainListResponseDoc = TypedDict('ModelYahoofinanceDomainListResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceDomainListResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceDownloadResponseDoc = TypedDict('ModelYahoofinanceDownloadResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceDownloadResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceEarningsDatesResponseDoc = TypedDict('ModelYahoofinanceEarningsDatesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceEarningsDatesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceFinancialsResponseDoc = TypedDict('ModelYahoofinanceFinancialsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceFinancialsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceHistoryMetadataResponseDoc = TypedDict('ModelYahoofinanceHistoryMetadataResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceHistoryMetadataResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceHistoryResponseDoc = TypedDict('ModelYahoofinanceHistoryResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceHistoryResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceIndustryResponseDoc = TypedDict('ModelYahoofinanceIndustryResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceIndustryResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceInfoResponseDoc = TypedDict('ModelYahoofinanceInfoResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceInfoResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceIsinResponseDoc = TypedDict('ModelYahoofinanceIsinResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceIsinresponse],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceMarketStatusResponseDoc = TypedDict('ModelYahoofinanceMarketStatusResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceMarketStatusResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceMarketSummaryResponseDoc = TypedDict('ModelYahoofinanceMarketSummaryResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceMarketSummaryResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceModuleResponseDoc = TypedDict('ModelYahoofinanceModuleResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceModuleResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceOptionsResponseDoc = TypedDict('ModelYahoofinanceOptionsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceOptionsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceQuoteResponseDoc = TypedDict('ModelYahoofinanceQuoteResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceQuoteResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceScreenerResponseDoc = TypedDict('ModelYahoofinanceScreenerResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceScreenerResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceScreenersResponseDoc = TypedDict('ModelYahoofinanceScreenersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceScreenersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceSearchResponseDoc = TypedDict('ModelYahoofinanceSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceSectorResponseDoc = TypedDict('ModelYahoofinanceSectorResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceSectorResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceSharesFullResponseDoc = TypedDict('ModelYahoofinanceSharesFullResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceSharesFullResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceSharesResponseDoc = TypedDict('ModelYahoofinanceSharesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceSharesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceTrendingResponseDoc = TypedDict('ModelYahoofinanceTrendingResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceTrendingResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYahoofinanceValuationResponseDoc = TypedDict('ModelYahoofinanceValuationResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYahoofinanceValuationResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYoutubeCaption = TypedDict('ModelYoutubeCaption', {
    'duration': NotRequired[float],
    'start': NotRequired[float],
    'text': NotRequired[str],
}, total=False)

ModelYoutubeChannelFeedResponse = TypedDict('ModelYoutubeChannelFeedResponse', {
    'channel_id': NotRequired[str],
    'channel_title': NotRequired[str],
    'channel_url': NotRequired[str],
    'continuation_token': NotRequired[str],
    'handle': NotRequired[str],
    'items': NotRequired[list[ModelYoutubeSearchItem]],
    'query': NotRequired[str],
    'thumbnail': NotRequired[str],
}, total=False)

ModelYoutubeChannelShort = TypedDict('ModelYoutubeChannelShort', {
    'position': NotRequired[int],
    'thumbnail': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'video_id': NotRequired[str],
    'view_count': NotRequired[str],
}, total=False)

ModelYoutubeChannelShortsResponse = TypedDict('ModelYoutubeChannelShortsResponse', {
    'channel_id': NotRequired[str],
    'channel_title': NotRequired[str],
    'channel_url': NotRequired[str],
    'handle': NotRequired[str],
    'shorts': NotRequired[list[ModelYoutubeChannelShort]],
    'thumbnail': NotRequired[str],
}, total=False)

ModelYoutubeComment = TypedDict('ModelYoutubeComment', {
    'channel_id': NotRequired[str],
    'comment_id': NotRequired[str],
    'content': NotRequired[str],
    'continuation_token': NotRequired[str],
    'likes_count': NotRequired[int],
    'published_time': NotRequired[str],
    'reply_count': NotRequired[int],
    'user_name': NotRequired[str],
}, total=False)

ModelYoutubeCommentResponse = TypedDict('ModelYoutubeCommentResponse', {
    'comments': NotRequired[list[ModelYoutubeComment]],
    'continuation_token': NotRequired[str],
}, total=False)

ModelYoutubePlaylistResponse = TypedDict('ModelYoutubePlaylistResponse', {
    'channel_id': NotRequired[str],
    'channel_title': NotRequired[str],
    'continuation_token': NotRequired[str],
    'items': NotRequired[list[ModelYoutubeSearchItem]],
    'playlist_id': NotRequired[str],
    'thumbnail': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'video_count': NotRequired[str],
}, total=False)

ModelYoutubeProfile = TypedDict('ModelYoutubeProfile', {
    'bio': NotRequired[str],
    'channel_id': NotRequired[str],
    'channel_name': NotRequired[str],
    'channel_url': NotRequired[str],
    'created_at': NotRequired[str],
    'id': NotRequired[str],
    'joined_date': NotRequired[str],
    'links': NotRequired[list[str]],
    'profile_pic': NotRequired[str],
    'region': NotRequired[str],
    'stats': NotRequired[ModelYoutubeProfileStats],
    'updated_at': NotRequired[str],
}, total=False)

ModelYoutubeProfileStats = TypedDict('ModelYoutubeProfileStats', {
    'followers_count': NotRequired[int],
    'videos_count': NotRequired[int],
    'views_count': NotRequired[int],
}, total=False)

ModelYoutubeSearchItem = TypedDict('ModelYoutubeSearchItem', {
    'badges': NotRequired[list[str]],
    'channel_id': NotRequired[str],
    'channel_thumbnail': NotRequired[str],
    'channel_title': NotRequired[str],
    'description_snippet': NotRequired[str],
    'duration': NotRequired[str],
    'duration_seconds': NotRequired[int],
    'handle': NotRequired[str],
    'is_live': NotRequired[bool],
    'is_short': NotRequired[bool],
    'is_verified': NotRequired[bool],
    'playlist_id': NotRequired[str],
    'position': NotRequired[int],
    'published_text': NotRequired[str],
    'short_view_count': NotRequired[str],
    'subscriber_count': NotRequired[str],
    'thumbnail': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[str],
    'url': NotRequired[str],
    'video_count': NotRequired[str],
    'video_id': NotRequired[str],
    'view_count': NotRequired[str],
}, total=False)

ModelYoutubeSearchResponse = TypedDict('ModelYoutubeSearchResponse', {
    'continuation_token': NotRequired[str],
    'estimated_results': NotRequired[int],
    'items': NotRequired[list[ModelYoutubeSearchItem]],
    'query': NotRequired[str],
}, total=False)

ModelYoutubeTagResp = TypedDict('ModelYoutubeTagResp', {
    'continuation_token': NotRequired[str],
    'meta': NotRequired[ModelYoutubeTagMeta],
    'videos': NotRequired[list[ModelYoutubeVideoDetail]],
}, total=False)

ModelYoutubeTranscriptLanguage = TypedDict('ModelYoutubeTranscriptLanguage', {
    'is_generated': NotRequired[bool],
    'is_translatable': NotRequired[bool],
    'language': NotRequired[str],
    'language_code': NotRequired[str],
}, total=False)

ModelYoutubeTranscriptResponse = TypedDict('ModelYoutubeTranscriptResponse', {
    'is_generated': NotRequired[bool],
    'language': NotRequired[str],
    'language_code': NotRequired[str],
    'segments': NotRequired[list[ModelYoutubeTranscriptSegment]],
    'text': NotRequired[str],
    'translation_language': NotRequired[str],
    'video_id': NotRequired[str],
}, total=False)

ModelYoutubeTranscriptSegment = TypedDict('ModelYoutubeTranscriptSegment', {
    'duration': NotRequired[float],
    'start': NotRequired[float],
    'text': NotRequired[str],
}, total=False)

ModelYoutubeVideoDetail = TypedDict('ModelYoutubeVideoDetail', {
    'channel_id': NotRequired[str],
    'channel_title': NotRequired[str],
    'comments_count': NotRequired[int],
    'description': NotRequired[str],
    'dislikes_count': NotRequired[int],
    'duration_seconds': NotRequired[float],
    'id': NotRequired[str],
    'likes_count': NotRequired[int],
    'published_at': NotRequired[str],
    'title': NotRequired[str],
    'views_count': NotRequired[int],
}, total=False)

ModelYoutubeCaptionsResponseDoc = TypedDict('ModelYoutubeCaptionsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelYoutubeCaption]],
    'msg': NotRequired[str],
}, total=False)

ModelYoutubeChannelFeedResponseDoc = TypedDict('ModelYoutubeChannelFeedResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYoutubeChannelFeedResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYoutubeChannelSearchResponseDataDoc = TypedDict('ModelYoutubeChannelSearchResponseDataDoc', {
    'channel_id': NotRequired[str],
    'channel_title': NotRequired[str],
    'channel_url': NotRequired[str],
    'continuation_token': NotRequired[str],
    'handle': NotRequired[str],
    'items': NotRequired[list[ModelYoutubeSearchItem]],
    'query': NotRequired[str],
    'thumbnail': NotRequired[str],
}, total=False)

ModelYoutubeChannelSearchResponseDoc = TypedDict('ModelYoutubeChannelSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYoutubeChannelSearchResponseDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelYoutubeChannelShortsResponseDoc = TypedDict('ModelYoutubeChannelShortsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYoutubeChannelShortsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYoutubeCommentsResponseDoc = TypedDict('ModelYoutubeCommentsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYoutubeCommentResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYoutubePlaylistResponseDoc = TypedDict('ModelYoutubePlaylistResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYoutubePlaylistResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYoutubeProfileResponseDoc = TypedDict('ModelYoutubeProfileResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYoutubeProfile],
    'msg': NotRequired[str],
}, total=False)

ModelYoutubeSearchResponseDoc = TypedDict('ModelYoutubeSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYoutubeSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYoutubeTagMeta = TypedDict('ModelYoutubeTagMeta', {
    'channelsCount': NotRequired[int],
    'videosCount': NotRequired[int],
}, total=False)

ModelYoutubeTagResponseDoc = TypedDict('ModelYoutubeTagResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYoutubeTagResp],
    'msg': NotRequired[str],
}, total=False)

ModelYoutubeTranscriptLanguagesResponseDoc = TypedDict('ModelYoutubeTranscriptLanguagesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelYoutubeTranscriptLanguage]],
    'msg': NotRequired[str],
}, total=False)

ModelYoutubeTranscriptResponseDoc = TypedDict('ModelYoutubeTranscriptResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYoutubeTranscriptResponse],
    'msg': NotRequired[str],
}, total=False)

ModelYoutubeVideoResponseDoc = TypedDict('ModelYoutubeVideoResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelYoutubeVideoDetail],
    'msg': NotRequired[str],
}, total=False)

ModelZillowAutocompleteItem = TypedDict('ModelZillowAutocompleteItem', {
    'city': NotRequired[str],
    'county': NotRequired[str],
    'id': NotRequired[str],
    'latitude': NotRequired[float],
    'longitude': NotRequired[float],
    'near_me': NotRequired[bool],
    'plid': NotRequired[str],
    'region_display_ids': NotRequired[list[str]],
    'region_id': NotRequired[int],
    'region_ids': NotRequired[list[int]],
    'region_type': NotRequired[int],
    'region_types': NotRequired[list[int]],
    'school_district_ids': NotRequired[list[int]],
    'school_ids': NotRequired[list[int]],
    'state': NotRequired[str],
    'sub_type': NotRequired[str],
    'view_latitude_delta': NotRequired[float],
}, total=False)

ModelZillowAutocompleteResponse = TypedDict('ModelZillowAutocompleteResponse', {
    'query': NotRequired[str],
    'request_id': NotRequired[str],
    'results': NotRequired[list[ModelZillowAutocompleteItem]],
}, total=False)

ModelZillowPropertyAddressParts = TypedDict('ModelZillowPropertyAddressParts', {
    'city': NotRequired[str],
    'county': NotRequired[str],
    'neighborhood': NotRequired[str],
    'state': NotRequired[str],
    'street': NotRequired[str],
    'subdivision': NotRequired[str],
    'zipcode': NotRequired[str],
}, total=False)

ModelZillowPropertyAgent = TypedDict('ModelZillowPropertyAgent', {
    'email': NotRequired[str],
    'name': NotRequired[str],
    'phone': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelZillowPropertyArea = TypedDict('ModelZillowPropertyArea', {
    'text': NotRequired[str],
    'unit': NotRequired[str],
    'value': NotRequired[float],
}, total=False)

ModelZillowPropertyFact = TypedDict('ModelZillowPropertyFact', {
    'key': NotRequired[str],
    'label': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelZillowPropertyFacts = TypedDict('ModelZillowPropertyFacts', {
    'accessibility_features': NotRequired[list[str]],
    'additional': NotRequired[list[ModelZillowPropertyFact]],
    'appliances': NotRequired[list[str]],
    'architectural_style': NotRequired[str],
    'basement': NotRequired[str],
    'bathrooms': NotRequired[float],
    'bathrooms_full': NotRequired[int],
    'bathrooms_half': NotRequired[int],
    'bathrooms_one_quarter': NotRequired[int],
    'bathrooms_three_quarter': NotRequired[int],
    'bedrooms': NotRequired[float],
    'builder_model': NotRequired[str],
    'builder_name': NotRequired[str],
    'community_features': NotRequired[list[str]],
    'construction_materials': NotRequired[list[str]],
    'cooling': NotRequired[list[str]],
    'exterior_features': NotRequired[list[str]],
    'fireplace_features': NotRequired[list[str]],
    'flooring': NotRequired[list[str]],
    'foundation_details': NotRequired[list[str]],
    'garage_spaces': NotRequired[float],
    'has_fireplace': NotRequired[bool],
    'heating': NotRequired[list[str]],
    'hoa_fee': NotRequired[str],
    'home_type': NotRequired[str],
    'laundry_features': NotRequired[list[str]],
    'levels': NotRequired[list[str]],
    'living_area': NotRequired[ModelZillowPropertyArea],
    'lot_size': NotRequired[ModelZillowPropertyArea],
    'lot_size_dimensions': NotRequired[str],
    'parcel_number': NotRequired[str],
    'parking_capacity': NotRequired[int],
    'parking_features': NotRequired[list[str]],
    'patio_and_porch_features': NotRequired[list[str]],
    'pool_features': NotRequired[list[str]],
    'property_sub_type': NotRequired[list[str]],
    'roof': NotRequired[str],
    'rooms': NotRequired[list[str]],
    'security_features': NotRequired[list[str]],
    'sewer': NotRequired[list[str]],
    'spa_features': NotRequired[list[str]],
    'stories': NotRequired[float],
    'structure_type': NotRequired[str],
    'tax_annual_amount': NotRequired[float],
    'tax_assessed_value': NotRequired[float],
    'utilities': NotRequired[list[str]],
    'view': NotRequired[list[str]],
    'water_source': NotRequired[list[str]],
    'waterfront_features': NotRequired[list[str]],
    'year_built': NotRequired[int],
    'zoning': NotRequired[str],
}, total=False)

ModelZillowPropertyHistory = TypedDict('ModelZillowPropertyHistory', {
    'price': NotRequired[list[ModelZillowPropertyPriceHistoryEntry]],
    'tax': NotRequired[list[ModelZillowPropertyTaxHistoryEntry]],
}, total=False)

ModelZillowPropertyItem = TypedDict('ModelZillowPropertyItem', {
    'address': NotRequired[str],
    'baths': NotRequired[float],
    'beds': NotRequired[float],
    'broker_name': NotRequired[str],
    'currency': NotRequired[str],
    'days_on_zillow': NotRequired[int],
    'detail_text': NotRequired[str],
    'has_3d_model': NotRequired[bool],
    'has_video': NotRequired[bool],
    'home_status': NotRequired[str],
    'home_type': NotRequired[str],
    'image': NotRequired[str],
    'is_showcase': NotRequired[bool],
    'latitude': NotRequired[float],
    'listing_sub_type': NotRequired[list[str]],
    'living_area': NotRequired[float],
    'longitude': NotRequired[float],
    'lot_area': NotRequired[float],
    'lot_area_unit': NotRequired[str],
    'photos': NotRequired[list[str]],
    'price': NotRequired[float],
    'price_text': NotRequired[str],
    'rent_zestimate': NotRequired[float],
    'status_text': NotRequired[str],
    'url': NotRequired[str],
    'zestimate': NotRequired[float],
    'zpid': NotRequired[str],
}, total=False)

ModelZillowPropertyListing = TypedDict('ModelZillowPropertyListing', {
    'agent_name': NotRequired[str],
    'agents': NotRequired[list[ModelZillowPropertyAgent]],
    'attribution_text': NotRequired[str],
    'broker_name': NotRequired[str],
    'broker_phone': NotRequired[str],
    'date_posted': NotRequired[str],
    'date_updated': NotRequired[str],
    'days_on_zillow': NotRequired[int],
    'listing_id': NotRequired[str],
    'mls_id': NotRequired[str],
    'open_houses': NotRequired[list[ModelZillowPropertyOpenHouse]],
    'provider': NotRequired[str],
    'provider_listing_id': NotRequired[str],
    'source': NotRequired[str],
    'status': NotRequired[str],
    'sub_types': NotRequired[list[str]],
    'time_on_zillow': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelZillowPropertyMedia = TypedDict('ModelZillowPropertyMedia', {
    'has_3d_model': NotRequired[bool],
    'has_video': NotRequired[bool],
    'photo_count': NotRequired[int],
    'photos': NotRequired[list[ModelZillowPropertyPhoto]],
    'primary_image': NotRequired[str],
    'video_url': NotRequired[str],
    'virtual_tour_url': NotRequired[str],
}, total=False)

ModelZillowPropertyNearby = TypedDict('ModelZillowPropertyNearby', {
    'address': NotRequired[str],
    'baths': NotRequired[float],
    'beds': NotRequired[float],
    'home_status': NotRequired[str],
    'living_area': NotRequired[float],
    'price': NotRequired[float],
    'price_text': NotRequired[str],
    'url': NotRequired[str],
    'zpid': NotRequired[str],
}, total=False)

ModelZillowPropertyOpenHouse = TypedDict('ModelZillowPropertyOpenHouse', {
    'end_time': NotRequired[str],
    'start_time': NotRequired[str],
    'text': NotRequired[str],
}, total=False)

ModelZillowPropertyPhoto = TypedDict('ModelZillowPropertyPhoto', {
    'height': NotRequired[int],
    'source': NotRequired[str],
    'url': NotRequired[str],
    'width': NotRequired[int],
}, total=False)

ModelZillowPropertyPriceHistoryEntry = TypedDict('ModelZillowPropertyPriceHistoryEntry', {
    'buyer_agent': NotRequired[str],
    'change': NotRequired[float],
    'date': NotRequired[str],
    'event': NotRequired[str],
    'price': NotRequired[float],
    'price_text': NotRequired[str],
    'seller_agent': NotRequired[str],
    'source': NotRequired[str],
    'time': NotRequired[int],
}, total=False)

ModelZillowPropertyPricing = TypedDict('ModelZillowPropertyPricing', {
    'currency': NotRequired[str],
    'estimated_monthly_payment': NotRequired[float],
    'monthly_hoa_fee': NotRequired[float],
    'price': NotRequired[float],
    'price_per_square_foot': NotRequired[float],
    'price_text': NotRequired[str],
    'property_tax_rate': NotRequired[float],
    'rent_zestimate': NotRequired[float],
    'zestimate': NotRequired[float],
}, total=False)

ModelZillowPropertyResponse = TypedDict('ModelZillowPropertyResponse', {
    'address': NotRequired[str],
    'address_parts': NotRequired[ModelZillowPropertyAddressParts],
    'baths': NotRequired[float],
    'beds': NotRequired[float],
    'broker_name': NotRequired[str],
    'currency': NotRequired[str],
    'days_on_zillow': NotRequired[int],
    'description': NotRequired[str],
    'detail_text': NotRequired[str],
    'facts': NotRequired[ModelZillowPropertyFacts],
    'has_3d_model': NotRequired[bool],
    'has_video': NotRequired[bool],
    'history': NotRequired[ModelZillowPropertyHistory],
    'home_status': NotRequired[str],
    'home_type': NotRequired[str],
    'image': NotRequired[str],
    'is_showcase': NotRequired[bool],
    'latitude': NotRequired[float],
    'listing': NotRequired[ModelZillowPropertyListing],
    'listing_sub_type': NotRequired[list[str]],
    'living_area': NotRequired[float],
    'longitude': NotRequired[float],
    'lot_area': NotRequired[float],
    'lot_area_unit': NotRequired[str],
    'media': NotRequired[ModelZillowPropertyMedia],
    'nearby': NotRequired[list[ModelZillowPropertyNearby]],
    'photos': NotRequired[list[str]],
    'price': NotRequired[float],
    'price_text': NotRequired[str],
    'pricing': NotRequired[ModelZillowPropertyPricing],
    'rent_zestimate': NotRequired[float],
    'schools': NotRequired[list[ModelZillowPropertySchool]],
    'status_text': NotRequired[str],
    'url': NotRequired[str],
    'zestimate': NotRequired[float],
    'zpid': NotRequired[str],
}, total=False)

ModelZillowPropertySchool = TypedDict('ModelZillowPropertySchool', {
    'assigned': NotRequired[bool],
    'distance': NotRequired[float],
    'district': NotRequired[str],
    'grades': NotRequired[str],
    'id': NotRequired[str],
    'level': NotRequired[str],
    'link': NotRequired[str],
    'name': NotRequired[str],
    'rating': NotRequired[float],
    'type': NotRequired[str],
}, total=False)

ModelZillowPropertyTaxHistoryEntry = TypedDict('ModelZillowPropertyTaxHistoryEntry', {
    'tax_increase': NotRequired[float],
    'tax_paid': NotRequired[float],
    'time': NotRequired[int],
    'value': NotRequired[float],
    'value_increase': NotRequired[float],
    'year': NotRequired[int],
}, total=False)

ModelZillowSearchResponse = TypedDict('ModelZillowSearchResponse', {
    'location': NotRequired[str],
    'page': NotRequired[int],
    'results': NotRequired[list[ModelZillowPropertyItem]],
}, total=False)

AirbnbRoomResponse = ModelAirbnbRoomResponse
AirbnbRoomParams = TypedDict('AirbnbRoomParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

AirbnbRoomCalendarResponse = ModelAirbnbCalendarResponse
AirbnbRoomCalendarParams = TypedDict('AirbnbRoomCalendarParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

AirbnbRoomReviewsResponse = ModelAirbnbReviewsResponse
AirbnbRoomReviewsParams = TypedDict('AirbnbRoomReviewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

AirbnbSearchResponse = ModelAirbnbSearchResponse
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

AmazonProductResponse = ModelAmazonProductResponseDoc
AmazonProductParams = TypedDict('AmazonProductParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'asin': Required[str],
    'language': NotRequired[Literal['en_US']],
    'currency': NotRequired[Literal['USD']],
}, total=False)

AmazonSearchResponse = ModelAmazonSearchResponseDoc
AmazonSearchParams = TypedDict('AmazonSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'k': Required[str],
    's': NotRequired[str],
    'page': NotRequired[int],
}, total=False)

AmazonSuggestResponse = ModelAmazonSuggestResponseDoc
AmazonSuggestParams = TypedDict('AmazonSuggestParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
}, total=False)

ApplePodcastsChartsResponse = ModelApplepodcastsChartsResponseDoc
ApplePodcastsChartsParams = TypedDict('ApplePodcastsChartsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'collection': NotRequired[str],
    'category': NotRequired[int],
    'country': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

ApplePodcastsEpisodesSearchResponse = ModelApplepodcastsEpisodeSearchResponseDoc
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

ApplePodcastsSearchResponse = ModelApplepodcastsSearchResponseDoc
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

ApplePodcastsShowResponse = ModelApplepodcastsShowResponseDoc
ApplePodcastsShowParams = TypedDict('ApplePodcastsShowParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

ApplePodcastsShowEpisodesResponse = ModelApplepodcastsShowEpisodesResponseDoc
ApplePodcastsShowEpisodesParams = TypedDict('ApplePodcastsShowEpisodesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

AppStoreAppResponse = ModelAppstoreAppDetailsResponseDoc
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

AppStoreDeveloperResponse = ModelAppstoreDeveloperResponseDoc
AppStoreDeveloperParams = TypedDict('AppStoreDeveloperParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'dev_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppStoreListResponse = ModelAppstoreListResultsResponseDoc
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

AppStorePrivacyResponse = ModelAppstorePrivacyResponseDoc
AppStorePrivacyParams = TypedDict('AppStorePrivacyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppStoreRatingsResponse = ModelAppstoreRatingsResponseDoc
AppStoreRatingsParams = TypedDict('AppStoreRatingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'app_id': NotRequired[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppStoreReviewsResponse = ModelAppstoreReviewsResponseDoc
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

AppStoreSearchResponse = ModelAppstoreSearchResultsResponseDoc
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

AppStoreSimilarResponse = ModelAppstoreSimilarResponseDoc
AppStoreSimilarParams = TypedDict('AppStoreSimilarParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'app_id': NotRequired[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppStoreSuggestResponse = ModelAppstoreSuggestResponseDoc
AppStoreSuggestParams = TypedDict('AppStoreSuggestParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'term': Required[str],
    'country': NotRequired[str],
}, total=False)

AppStoreVersionHistoryResponse = ModelAppstoreVersionHistoryResponseDoc
AppStoreVersionHistoryParams = TypedDict('AppStoreVersionHistoryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

BillingMeResponse = ModelBillingBillingStateResponseDoc
BillingMeParams = TypedDict('BillingMeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

BillingMeCheckoutBody = ModelBillingStripeCheckoutRequestDoc
BillingMeCheckoutResponse = ModelBillingStripeSessionResponseDoc
BillingMeCheckoutParams = TypedDict('BillingMeCheckoutParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[BillingMeCheckoutBody],
}, total=False)

BillingMeEventsResponse = ModelBillingBillingEventsResponseDoc
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

BillingMePeriodsResponse = ModelBillingBillingPeriodLedgersResponseDoc
BillingMePeriodsParams = TypedDict('BillingMePeriodsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'limit': NotRequired[int],
}, total=False)

BillingMePeriodResponse = ModelBillingBillingPeriodLedgerResponseDoc
BillingMePeriodParams = TypedDict('BillingMePeriodParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'period_key': Required[str],
}, total=False)

BillingMePeriodStatementResponse = ModelBillingBillingPeriodStatementResponseDoc
BillingMePeriodStatementParams = TypedDict('BillingMePeriodStatementParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'period_key': Required[str],
    'include_events': NotRequired[bool],
    'event_limit': NotRequired[int],
}, total=False)

BillingMePeriodStatementDownloadResponse = str
BillingMePeriodStatementDownloadParams = TypedDict('BillingMePeriodStatementDownloadParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'period_key': Required[str],
}, total=False)

BillingMePortalBody = ModelBillingStripePortalRequestDoc
BillingMePortalResponse = ModelBillingStripeSessionResponseDoc
BillingMePortalParams = TypedDict('BillingMePortalParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[BillingMePortalBody],
}, total=False)

BingImagesResponse = ModelBingImagesResponseDoc
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

BingNewsResponse = ModelBingNewsResponseDoc
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

BingSearchResponse = ModelBingSearchResponseDoc
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

BingSuggestResponse = ModelBingSuggestResponseDoc
BingSuggestParams = TypedDict('BingSuggestParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

BingVideosResponse = ModelBingVideosResponseDoc
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

BraveImagesResponse = ModelBraveImagesResponseDoc
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

BraveNewsResponse = ModelBraveNewsResponseDoc
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

BraveSearchResponse = ModelBraveSearchResponseDoc
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

BraveSuggestResponse = ModelBraveSuggestResponseDoc
BraveSuggestParams = TypedDict('BraveSuggestParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'count': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
}, total=False)

BraveVideosResponse = ModelBraveVideosResponseDoc
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

CoinGeckoCategoriesResponse = ModelCoingeckoCategoriesResponseDoc
CoinGeckoCategoriesParams = TypedDict('CoinGeckoCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoCategoryCoinsResponse = ModelCoingeckoCategoryCoinsResponseDoc
CoinGeckoCategoryCoinsParams = TypedDict('CoinGeckoCategoryCoinsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoChainsResponse = ModelCoingeckoChainsResponseDoc
CoinGeckoChainsParams = TypedDict('CoinGeckoChainsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoChainResponse = ModelCoingeckoChainDetailResponseDoc
CoinGeckoChainParams = TypedDict('CoinGeckoChainParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoCoinResponse = ModelCoingeckoCoinResponseDoc
CoinGeckoCoinParams = TypedDict('CoinGeckoCoinParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoCoinAnalysisResponse = ModelCoingeckoAnalysisResponseDoc
CoinGeckoCoinAnalysisParams = TypedDict('CoinGeckoCoinAnalysisParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
    'range': NotRequired[Literal['24h', 'max']],
    'include_annotations': NotRequired[bool],
}, total=False)

CoinGeckoExchangeResponse = ModelCoingeckoExchangeDetailResponseDoc
CoinGeckoExchangeParams = TypedDict('CoinGeckoExchangeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoExchangesResponse = ModelCoingeckoExchangesResponseDoc
CoinGeckoExchangesParams = TypedDict('CoinGeckoExchangesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'kind': NotRequired[Literal['spot', 'dex', 'derivatives', 'perp_dex']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoGainersLosersResponse = ModelCoingeckoGainersLosersResponseDoc
CoinGeckoGainersLosersParams = TypedDict('CoinGeckoGainersLosersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoGlobalResponse = ModelCoingeckoGlobalResponseDoc
CoinGeckoGlobalParams = TypedDict('CoinGeckoGlobalParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

CoinGeckoGlobalChartsResponse = ModelCoingeckoGlobalChartsResponseDoc
CoinGeckoGlobalChartsParams = TypedDict('CoinGeckoGlobalChartsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'kind': NotRequired[Literal['total_market_cap', 'bitcoin_dominance', 'altcoin_market_cap', 'defi_market_cap']],
    'range': NotRequired[Literal['24h', '7d', '14d', '30d', '90d', '1y', 'max']],
    'limit': NotRequired[int],
}, total=False)

CoinGeckoLearnArticlesResponse = ModelCoingeckoLearnArticlesResponseDoc
CoinGeckoLearnArticlesParams = TypedDict('CoinGeckoLearnArticlesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category': NotRequired[Literal['all', 'latest', 'airdrop-guides', 'coins-and-tokens', 'guides', 'wallets-and-bridges', 'api', 'reviews']],
    'limit': NotRequired[int],
}, total=False)

CoinGeckoMarketsResponse = ModelCoingeckoMarketsResponseDoc
CoinGeckoMarketsParams = TypedDict('CoinGeckoMarketsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoNewCoinsResponse = ModelCoingeckoNewCoinsResponseDoc
CoinGeckoNewCoinsParams = TypedDict('CoinGeckoNewCoinsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoNewsResponse = ModelCoingeckoNewsResponseDoc
CoinGeckoNewsParams = TypedDict('CoinGeckoNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'limit': NotRequired[int],
}, total=False)

CoinGeckoNftCategoryResponse = ModelCoingeckoNftCategoryResponseDoc
CoinGeckoNftCategoryParams = TypedDict('CoinGeckoNftCategoryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoNftsResponse = ModelCoingeckoNftsResponseDoc
CoinGeckoNftsParams = TypedDict('CoinGeckoNftsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoSearchResponse = ModelCoingeckoSearchResponseDoc
CoinGeckoSearchParams = TypedDict('CoinGeckoSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'limit': NotRequired[int],
}, total=False)

CoinGeckoTokenUnlocksResponse = ModelCoingeckoTokenUnlocksResponseDoc
CoinGeckoTokenUnlocksParams = TypedDict('CoinGeckoTokenUnlocksParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'limit': NotRequired[int],
}, total=False)

CoinGeckoTreasuriesResponse = ModelCoingeckoTreasuriesResponseDoc
CoinGeckoTreasuriesParams = TypedDict('CoinGeckoTreasuriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'asset': NotRequired[Literal['all', 'bitcoin', 'ethereum', 'solana', 'bnb', 'xrp', 'tron']],
    'holder_type': NotRequired[Literal['all', 'companies', 'governments']],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

CoinGeckoTrendingResponse = ModelCoingeckoTrendingResponseDoc
CoinGeckoTrendingParams = TypedDict('CoinGeckoTrendingParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'limit': NotRequired[int],
    'vs_currency': NotRequired[Literal['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'sol', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']],
}, total=False)

DatasetsListResponse = ModelDatasetsListResponseDoc
DatasetsListParams = TypedDict('DatasetsListParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

DatasetsGoogleMapBusinessesFacetsResponse = ModelDatasetsGoogleMapBusinessesFacetResponseDoc
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

DatasetsGoogleMapBusinessesItemResponse = ModelDatasetsGoogleMapBusinessResponseDoc
DatasetsGoogleMapBusinessesItemParams = TypedDict('DatasetsGoogleMapBusinessesItemParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'place_id': Required[str],
}, total=False)

DatasetsGoogleMapBusinessesNearbyResponse = ModelDatasetsGoogleMapBusinessesSearchResponseDoc
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

DatasetsGoogleMapBusinessesSearchResponse = ModelDatasetsGoogleMapBusinessesSearchResponseDoc
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

EBayEbayItemResponse = ModelEbayItemResponseDoc
EBayEbayItemParams = TypedDict('EBayEbayItemParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'item_id': Required[str],
}, total=False)

EBayEbaySearchBody = ModelEbaySearchOption
EBayEbaySearchResponse = ModelEbaySearchResponseDoc
EBayEbaySearchParams = TypedDict('EBayEbaySearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'option': Required[EBayEbaySearchBody],
}, total=False)

EBayEbaySellerResponse = ModelEbaySellerResponseDoc
EBayEbaySellerParams = TypedDict('EBayEbaySellerParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'seller': Required[str],
}, total=False)

EBayEbaySellerAboutResponse = ModelEbaySellerAboutResponseDoc
EBayEbaySellerAboutParams = TypedDict('EBayEbaySellerAboutParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'seller': Required[str],
}, total=False)

EBayEbaySellerFeedbackResponse = ModelEbaySellerFeedbackResponseDoc
EBayEbaySellerFeedbackParams = TypedDict('EBayEbaySellerFeedbackParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'seller': Required[str],
    'page': NotRequired[int],
    'per_page': NotRequired[Literal['24', '48', '72']],
}, total=False)

EBayEbaySellerShopResponse = ModelEbaySellerShopResponseDoc
EBayEbaySellerShopParams = TypedDict('EBayEbaySellerShopParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'seller': Required[str],
    'page': NotRequired[int],
}, total=False)

GeocodingLookupResponse = ModelGeocodingLookupResponseDoc
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

GeocodingReverseResponse = ModelGeocodingReverseResponseDoc
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

GeocodingSearchResponse = ModelGeocodingSearchResponseDoc
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

GoogleFinanceAnalystArticlesResponse = ModelFinanceArticlesResponseDoc
GoogleFinanceAnalystArticlesParams = TypedDict('GoogleFinanceAnalystArticlesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'quote': Required[str],
}, total=False)

GoogleFinanceChartResponse = ModelFinanceChartResponseDoc
GoogleFinanceChartParams = TypedDict('GoogleFinanceChartParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'quote': Required[str],
    'window': NotRequired[str],
}, total=False)

GoogleFinanceClassificationResponse = ModelFinanceClassificationResponseDoc
GoogleFinanceClassificationParams = TypedDict('GoogleFinanceClassificationParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'quote': Required[str],
}, total=False)

GoogleFinanceCompanyResponse = ModelFinanceCompanyResponseDoc
GoogleFinanceCompanyParams = TypedDict('GoogleFinanceCompanyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'quote': Required[str],
}, total=False)

GoogleFinanceContextResponse = ModelFinanceContextResponseDoc
GoogleFinanceContextParams = TypedDict('GoogleFinanceContextParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
}, total=False)

GoogleFinanceFinancialsResponse = ModelFinanceFinancialsResponseDoc
GoogleFinanceFinancialsParams = TypedDict('GoogleFinanceFinancialsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'quote': Required[str],
}, total=False)

GoogleFinanceMarketsCategoryNewsResponse = ModelFinanceCategoryNewsResponseDoc
GoogleFinanceMarketsCategoryNewsParams = TypedDict('GoogleFinanceMarketsCategoryNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category': Required[str],
    'offset': NotRequired[int],
}, total=False)

GoogleFinanceMarketsCategoryStocksResponse = ModelFinanceCategoryStocksResponseDoc
GoogleFinanceMarketsCategoryStocksParams = TypedDict('GoogleFinanceMarketsCategoryStocksParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category': Required[str],
    'offset': NotRequired[int],
}, total=False)

GoogleFinanceMarketsEarningsResponse = ModelFinanceEarningsResponseDoc
GoogleFinanceMarketsEarningsParams = TypedDict('GoogleFinanceMarketsEarningsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

GoogleFinanceMarketsFeaturedResponse = ModelFinanceInstrumentsResponseDoc
GoogleFinanceMarketsFeaturedParams = TypedDict('GoogleFinanceMarketsFeaturedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

GoogleFinanceMarketsHeadlineResponse = ModelFinanceHeadlineResponseDoc
GoogleFinanceMarketsHeadlineParams = TypedDict('GoogleFinanceMarketsHeadlineParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

GoogleFinanceMarketsIndicesResponse = ModelFinanceInstrumentsResponseDoc
GoogleFinanceMarketsIndicesParams = TypedDict('GoogleFinanceMarketsIndicesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

GoogleFinanceMarketsMoversResponse = ModelFinanceMarketMoversResponseDoc
GoogleFinanceMarketsMoversParams = TypedDict('GoogleFinanceMarketsMoversParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'categories': NotRequired[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

GoogleFinanceMarketsTopResponse = ModelFinanceTopStocksResponseDoc
GoogleFinanceMarketsTopParams = TypedDict('GoogleFinanceMarketsTopParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'metric': NotRequired[int],
    'page': NotRequired[int],
}, total=False)

GoogleFinanceMarketsTrendingResponse = ModelFinanceInstrumentsResponseDoc
GoogleFinanceMarketsTrendingParams = TypedDict('GoogleFinanceMarketsTrendingParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'limit': NotRequired[int],
}, total=False)

GoogleFinanceNewsResponse = ModelFinanceArticlesResponseDoc
GoogleFinanceNewsParams = TypedDict('GoogleFinanceNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'quote': Required[str],
    'limit': NotRequired[int],
}, total=False)

GoogleFinanceQuoteResponse = ModelFinanceQuoteResponseDoc
GoogleFinanceQuoteParams = TypedDict('GoogleFinanceQuoteParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'quote': Required[str],
}, total=False)

GoogleFinanceRelatedResponse = ModelFinanceRelatedResponseDoc
GoogleFinanceRelatedParams = TypedDict('GoogleFinanceRelatedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'quote': Required[str],
}, total=False)

GoogleFinanceSearchResponse = ModelFinanceSearchResponseDoc
GoogleFinanceSearchParams = TypedDict('GoogleFinanceSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
}, total=False)

GoogleFinanceTickerResponse = ModelFinanceTickerResponseDoc
GoogleFinanceTickerParams = TypedDict('GoogleFinanceTickerParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'ticker': Required[str],
    'window': NotRequired[str],
}, total=False)

GoogleJobsBody = ModelGoogleJobsOption
GoogleJobsResponse = ModelGoogleJobsResponse
GoogleJobsParams = TypedDict('GoogleJobsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'option': Required[GoogleJobsBody],
}, total=False)

GoogleMapPlaceResponse = ModelGoogleMapPlaceResponseDoc
GoogleMapPlaceParams = TypedDict('GoogleMapPlaceParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'place_id': Required[str],
}, total=False)

GoogleMapSearchBody = ModelGoogleMapSearchOption
GoogleMapSearchResponse = ModelGoogleMapSearchResponseDoc
GoogleMapSearchParams = TypedDict('GoogleMapSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'mapSearchOption': Required[GoogleMapSearchBody],
}, total=False)

GoogleSearchBody = ModelGoogleSearchOption
GoogleSearchResponse = ModelGoogleSearchResponseDoc
GoogleSearchParams = TypedDict('GoogleSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'searchOption': Required[GoogleSearchBody],
}, total=False)

GoogleSuggestResponse = ModelGoogleSuggestResponseDoc
GoogleSuggestParams = TypedDict('GoogleSuggestParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GoogleTrendsCategoriesResponse = ModelTrendsTrendsCategoriesResponseDoc
GoogleTrendsCategoriesParams = TypedDict('GoogleTrendsCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

GoogleTrendsEnumsResponse = ModelTrendsTrendsEnumsResponseDoc
GoogleTrendsEnumsParams = TypedDict('GoogleTrendsEnumsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

GoogleTrendsExploreBody = ModelTrendsExploreRequest
GoogleTrendsExploreResponse = ModelTrendsExploreResponseDoc
GoogleTrendsExploreParams = TypedDict('GoogleTrendsExploreParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[GoogleTrendsExploreBody],
}, total=False)

GoogleTrendsExploreInterestByRegionBody = ModelTrendsExploreRequest
GoogleTrendsExploreInterestByRegionResponse = ModelTrendsInterestByRegionResponseDoc
GoogleTrendsExploreInterestByRegionParams = TypedDict('GoogleTrendsExploreInterestByRegionParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[GoogleTrendsExploreInterestByRegionBody],
}, total=False)

GoogleTrendsExploreInterestOverTimeBody = ModelTrendsExploreRequest
GoogleTrendsExploreInterestOverTimeResponse = ModelTrendsInterestOverTimeResponseDoc
GoogleTrendsExploreInterestOverTimeParams = TypedDict('GoogleTrendsExploreInterestOverTimeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[GoogleTrendsExploreInterestOverTimeBody],
}, total=False)

GoogleTrendsExploreRelatedTopicsBody = ModelTrendsExploreRequest
GoogleTrendsExploreRelatedTopicsResponse = ModelTrendsRelatedTopicsResponseDoc
GoogleTrendsExploreRelatedTopicsParams = TypedDict('GoogleTrendsExploreRelatedTopicsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[GoogleTrendsExploreRelatedTopicsBody],
}, total=False)

GoogleTrendsExploreRisingQueriesBody = ModelTrendsExploreRequest
GoogleTrendsExploreRisingQueriesResponse = ModelTrendsExploreQueriesResponseDoc
GoogleTrendsExploreRisingQueriesParams = TypedDict('GoogleTrendsExploreRisingQueriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[GoogleTrendsExploreRisingQueriesBody],
}, total=False)

GoogleTrendsExploreTopQueriesBody = ModelTrendsExploreRequest
GoogleTrendsExploreTopQueriesResponse = ModelTrendsExploreQueriesResponseDoc
GoogleTrendsExploreTopQueriesParams = TypedDict('GoogleTrendsExploreTopQueriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[GoogleTrendsExploreTopQueriesBody],
}, total=False)

GoogleTrendsLocationsResponse = ModelTrendsTrendsLocationsResponseDoc
GoogleTrendsLocationsParams = TypedDict('GoogleTrendsLocationsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

GoogleTrendsTrendingResponse = ModelTrendsTrendingResponseDoc
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

GoogleTrendsTrendingDetailBody = ModelTrendsTrendingDetailRequest
GoogleTrendsTrendingDetailResponse = ModelTrendsExploreResponseDoc
GoogleTrendsTrendingDetailParams = TypedDict('GoogleTrendsTrendingDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[GoogleTrendsTrendingDetailBody],
}, total=False)

GooglePlayAppResponse = ModelGoogleplayAppDetailsResponse
GooglePlayAppParams = TypedDict('GooglePlayAppParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'app_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GooglePlayCategoriesResponse = ModelGoogleplayCategoriesResponseDoc
GooglePlayCategoriesParams = TypedDict('GooglePlayCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GooglePlayDatasafetyResponse = ModelGoogleplayDataSafetyResponseDoc
GooglePlayDatasafetyParams = TypedDict('GooglePlayDatasafetyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'app_id': Required[str],
    'lang': NotRequired[str],
}, total=False)

GooglePlayDeveloperResponse = ModelGoogleplayDeveloperResultsResponseDoc
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

GooglePlayListResponse = ModelGoogleplayListResultsResponseDoc
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

GooglePlayPermissionsResponse = ModelGoogleplayPermissionsResultsResponseDoc
GooglePlayPermissionsParams = TypedDict('GooglePlayPermissionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'app_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'short': NotRequired[bool],
}, total=False)

GooglePlayReviewsResponse = ModelGoogleplayReviewsResponseDoc
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

GooglePlaySearchResponse = ModelGoogleplaySearchResultsResponseDoc
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

GooglePlaySimilarResponse = ModelGoogleplaySimilarResultsResponseDoc
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

GooglePlaySuggestResponse = ModelGoogleplaySuggestResponseDoc
GooglePlaySuggestParams = TypedDict('GooglePlaySuggestParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'term': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

InstagramPostResponse = ModelInstagramPostResponseDoc
InstagramPostParams = TypedDict('InstagramPostParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'post_id': Required[str],
}, total=False)

InstagramProfileResponse = ModelInstagramProfileResponseDoc
InstagramProfileParams = TypedDict('InstagramProfileParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': Required[str],
}, total=False)

InstagramReelsResponse = ModelInstagramReelsResponseDoc
InstagramReelsParams = TypedDict('InstagramReelsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'max_id': NotRequired[str],
}, total=False)

JustWatchJustwatchAgeCertificationsResponse = ModelJustwatchAgeCertificationsResponseDoc
JustWatchJustwatchAgeCertificationsParams = TypedDict('JustWatchJustwatchAgeCertificationsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': NotRequired[str],
}, total=False)

JustWatchJustwatchDiscoverResponse = ModelJustwatchDiscoverResponseDoc
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

JustWatchJustwatchEpisodeByIdResponse = ModelJustwatchEpisodeByIdresponseDoc
JustWatchJustwatchEpisodeByIdParams = TypedDict('JustWatchJustwatchEpisodeByIdParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'country': NotRequired[str],
    'language': NotRequired[str],
}, total=False)

JustWatchJustwatchEpisodeOffersResponse = ModelJustwatchEpisodeOffersResponseDoc
JustWatchJustwatchEpisodeOffersParams = TypedDict('JustWatchJustwatchEpisodeOffersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'countries': NotRequired[str],
    'language': NotRequired[str],
}, total=False)

JustWatchJustwatchGenreTitlesResponse = ModelJustwatchGenreTitlesResponseDoc
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

JustWatchJustwatchGenresResponse = ModelJustwatchGenresResponseDoc
JustWatchJustwatchGenresParams = TypedDict('JustWatchJustwatchGenresParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'language': NotRequired[str],
}, total=False)

JustWatchJustwatchMonetizationTitlesResponse = ModelJustwatchMonetizationTitlesResponseDoc
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

JustWatchJustwatchNewResponse = ModelJustwatchNewTitlesResponseDoc
JustWatchJustwatchNewParams = TypedDict('JustWatchJustwatchNewParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': NotRequired[str],
    'language': NotRequired[str],
    'limit': NotRequired[int],
    'type': NotRequired[Literal['all', 'movie', 'show']],
}, total=False)

JustWatchJustwatchPopularResponse = ModelJustwatchPopularResponseDoc
JustWatchJustwatchPopularParams = TypedDict('JustWatchJustwatchPopularParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': NotRequired[str],
    'language': NotRequired[str],
    'limit': NotRequired[int],
    'type': NotRequired[Literal['all', 'movie', 'show']],
}, total=False)

JustWatchJustwatchProviderTitlesResponse = ModelJustwatchProviderTitlesResponseDoc
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

JustWatchJustwatchProvidersResponse = ModelJustwatchProvidersResponseDoc
JustWatchJustwatchProvidersParams = TypedDict('JustWatchJustwatchProvidersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': NotRequired[str],
}, total=False)

JustWatchJustwatchSearchResponse = ModelJustwatchSearchResponseDoc
JustWatchJustwatchSearchParams = TypedDict('JustWatchJustwatchSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'query': Required[str],
    'country': NotRequired[str],
    'language': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

JustWatchJustwatchSeasonByIdResponse = ModelJustwatchSeasonByIdresponseDoc
JustWatchJustwatchSeasonByIdParams = TypedDict('JustWatchJustwatchSeasonByIdParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'country': NotRequired[str],
    'language': NotRequired[str],
}, total=False)

JustWatchJustwatchSeasonEpisodesResponse = ModelJustwatchSeasonEpisodesResponseDoc
JustWatchJustwatchSeasonEpisodesParams = TypedDict('JustWatchJustwatchSeasonEpisodesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'season_id': Required[str],
    'country': NotRequired[str],
    'language': NotRequired[str],
}, total=False)

JustWatchJustwatchShowSeasonsResponse = ModelJustwatchShowSeasonsResponseDoc
JustWatchJustwatchShowSeasonsParams = TypedDict('JustWatchJustwatchShowSeasonsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'show_id': Required[str],
    'country': NotRequired[str],
    'language': NotRequired[str],
}, total=False)

JustWatchJustwatchTitleResponse = ModelJustwatchTitleResponseDoc
JustWatchJustwatchTitleParams = TypedDict('JustWatchJustwatchTitleParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'path': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

JustWatchJustwatchTitleAnalysisResponse = ModelJustwatchAnalysisResponseDoc
JustWatchJustwatchTitleAnalysisParams = TypedDict('JustWatchJustwatchTitleAnalysisParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'path': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

JustWatchJustwatchTitleByIdResponse = ModelJustwatchTitleResponseDoc
JustWatchJustwatchTitleByIdParams = TypedDict('JustWatchJustwatchTitleByIdParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'country': NotRequired[str],
    'language': NotRequired[str],
}, total=False)

JustWatchJustwatchTitleMediaResponse = ModelJustwatchTitleMediaResponseDoc
JustWatchJustwatchTitleMediaParams = TypedDict('JustWatchJustwatchTitleMediaParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'country': NotRequired[str],
    'language': NotRequired[str],
}, total=False)

JustWatchJustwatchTitleOffersResponse = ModelJustwatchTitleOffersResponseDoc
JustWatchJustwatchTitleOffersParams = TypedDict('JustWatchJustwatchTitleOffersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'countries': NotRequired[str],
    'language': NotRequired[str],
}, total=False)

JustWatchJustwatchTitleSimilarResponse = ModelJustwatchSimilarTitlesResponseDoc
JustWatchJustwatchTitleSimilarParams = TypedDict('JustWatchJustwatchTitleSimilarParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'country': NotRequired[str],
    'language': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

LinkedInLinkedinCompanyResponse = ModelLinkedinCompanyResponseDoc
LinkedInLinkedinCompanyParams = TypedDict('LinkedInLinkedinCompanyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

LinkedInLinkedinProductResponse = ModelLinkedinProductResponseDoc
LinkedInLinkedinProductParams = TypedDict('LinkedInLinkedinProductParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

LinkedInLinkedinShowcaseResponse = ModelLinkedinShowcaseResponseDoc
LinkedInLinkedinShowcaseParams = TypedDict('LinkedInLinkedinShowcaseParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

MetaPingResponse = ModelApiPingResponseDoc
MetaPingParams = TypedDict('MetaPingParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

ProductHuntCategoryResponse = ModelProducthuntCategoryResponseDoc
ProductHuntCategoryParams = TypedDict('ProductHuntCategoryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
}, total=False)

ProductHuntCategoryProductsResponse = ModelProducthuntCategoryProductsResponseDoc
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

ProductHuntLeaderboardResponse = ModelProducthuntLeaderboardResponseDoc
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

ProductHuntProductResponse = ModelProducthuntProductResponseDoc
ProductHuntProductParams = TypedDict('ProductHuntProductParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

ProductHuntAboutResponse = ModelProducthuntAboutResponseDoc
ProductHuntAboutParams = TypedDict('ProductHuntAboutParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

ProductHuntAlternativesResponse = ModelProducthuntAlternativesResponseDoc
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

ProductHuntCustomersResponse = ModelProducthuntCustomersResponseDoc
ProductHuntCustomersParams = TypedDict('ProductHuntCustomersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'order': NotRequired[Literal['customers', 'latest_launch']],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

ProductHuntLaunchesResponse = ModelProducthuntLaunchesResponseDoc
ProductHuntLaunchesParams = TypedDict('ProductHuntLaunchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'cursor': NotRequired[str],
    'order': NotRequired[str],
}, total=False)

ProductHuntMakersResponse = ModelProducthuntMakersResponseDoc
ProductHuntMakersParams = TypedDict('ProductHuntMakersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'cursor': NotRequired[str],
}, total=False)

ProductHuntReviewsResponse = ModelProducthuntReviewsResponseDoc
ProductHuntReviewsParams = TypedDict('ProductHuntReviewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

ProductHuntSearchResponse = ModelProducthuntSearchResponseDoc
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

MetaReadyResponse = ModelApiReadinessResponseDoc
MetaReadyParams = TypedDict('MetaReadyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

ReferralsClickBody = ModelReferralsReferralClickRequestDoc
ReferralsClickResponse = ModelReferralsReferralClickResponseDoc
ReferralsClickParams = TypedDict('ReferralsClickParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[ReferralsClickBody],
}, total=False)

ReferralsMeResponse = ModelReferralsReferralsMeResponseDoc
ReferralsMeParams = TypedDict('ReferralsMeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

ReferralsMeEventsResponse = ModelReferralsReferralsEventsResponseDoc
ReferralsMeEventsParams = TypedDict('ReferralsMeEventsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'limit': NotRequired[int],
}, total=False)

ShopAppAnalysisResponse = ModelShopappAnalysisResponseDoc
ShopAppAnalysisParams = TypedDict('ShopAppAnalysisParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'query': Required[str],
    'limit': NotRequired[int],
    'in_stock': NotRequired[bool],
    'on_sale': NotRequired[bool],
    'deep_search': NotRequired[bool],
}, total=False)

ShopAppCategoriesResponse = ModelShopappCategoriesResponseDoc
ShopAppCategoriesParams = TypedDict('ShopAppCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

ShopAppProductResponse = ModelShopappProductResponseDoc
ShopAppProductParams = TypedDict('ShopAppProductParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'variant_id': NotRequired[str],
}, total=False)

ShopAppProductRelatedResponse = ModelShopappRelatedResponseDoc
ShopAppProductRelatedParams = TypedDict('ShopAppProductRelatedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'limit': NotRequired[int],
}, total=False)

ShopAppProductReviewsResponse = ModelShopappReviewsResponseDoc
ShopAppProductReviewsParams = TypedDict('ShopAppProductReviewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'limit': NotRequired[int],
}, total=False)

ShopAppProductShopResponse = ModelShopappProductShopResponseDoc
ShopAppProductShopParams = TypedDict('ShopAppProductShopParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

ShopAppProductVariantResponse = ModelShopappProductVariantResponseDoc
ShopAppProductVariantParams = TypedDict('ShopAppProductVariantParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'selected_options': NotRequired[str],
}, total=False)

ShopAppProductVariantsResponse = ModelShopappVariantsResponseDoc
ShopAppProductVariantsParams = TypedDict('ShopAppProductVariantsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'selected_options': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

ShopAppSearchResponse = ModelShopappSearchResponseDoc
ShopAppSearchParams = TypedDict('ShopAppSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'query': Required[str],
    'limit': NotRequired[int],
    'in_stock': NotRequired[bool],
    'on_sale': NotRequired[bool],
    'deep_search': NotRequired[bool],
}, total=False)

ShopAppShopResponse = ModelShopappShopResponseDoc
ShopAppShopParams = TypedDict('ShopAppShopParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'handle': Required[str],
}, total=False)

ShopAppCollectionProductsResponse = ModelShopappShopProductsResponseDoc
ShopAppCollectionProductsParams = TypedDict('ShopAppCollectionProductsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'handle': Required[str],
    'collection_id': Required[str],
    'limit': NotRequired[int],
    'sort_by': NotRequired[Literal['MOST_SALES', 'PRICE_LOW_TO_HIGH', 'PRICE_HIGH_TO_LOW', 'RELEVANCE']],
    'in_stock': NotRequired[bool],
}, total=False)

ShopAppShopLocationsResponse = ModelShopappShopLocationsResponseDoc
ShopAppShopLocationsParams = TypedDict('ShopAppShopLocationsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'handle': Required[str],
    'limit': NotRequired[int],
}, total=False)

ShopAppShopProductsResponse = ModelShopappShopProductsResponseDoc
ShopAppShopProductsParams = TypedDict('ShopAppShopProductsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'handle': Required[str],
    'limit': NotRequired[int],
    'sort_by': NotRequired[Literal['MOST_SALES', 'PRICE_LOW_TO_HIGH', 'PRICE_HIGH_TO_LOW', 'RELEVANCE']],
    'in_stock': NotRequired[bool],
}, total=False)

ShopAppShopReviewsResponse = ModelShopappShopReviewsResponseDoc
ShopAppShopReviewsParams = TypedDict('ShopAppShopReviewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'handle': Required[str],
    'limit': NotRequired[int],
}, total=False)

ShopAppShopTypeaheadResponse = ModelShopappShopTypeaheadResponseDoc
ShopAppShopTypeaheadParams = TypedDict('ShopAppShopTypeaheadParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'handle': Required[str],
    'query': Required[str],
    'limit': NotRequired[int],
}, total=False)

ShopAppSuggestionsResponse = ModelShopappSuggestionsResponseDoc
ShopAppSuggestionsParams = TypedDict('ShopAppSuggestionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'query': Required[str],
    'limit': NotRequired[int],
}, total=False)

ShopifyCollectionsResponse = ModelShopifyCollectionsResponseDoc
ShopifyCollectionsParams = TypedDict('ShopifyCollectionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'url': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

ShopifyCollectionProductsResponse = ModelShopifyCollectionProductsResponseDoc
ShopifyCollectionProductsParams = TypedDict('ShopifyCollectionProductsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'handle': Required[str],
    'url': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

ShopifyPagesResponse = ModelShopifyPagesResponseDoc
ShopifyPagesParams = TypedDict('ShopifyPagesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'url': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

ShopifyPageResponse = ModelShopifyPageResponseDoc
ShopifyPageParams = TypedDict('ShopifyPageParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'handle': Required[str],
    'url': Required[str],
}, total=False)

ShopifyProductsResponse = ModelShopifyProductsResponseDoc
ShopifyProductsParams = TypedDict('ShopifyProductsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'url': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

ShopifyProductResponse = ModelShopifyProductResponseDoc
ShopifyProductParams = TypedDict('ShopifyProductParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'handle': Required[str],
    'url': Required[str],
}, total=False)

ShopifyProductRecommendationsResponse = ModelShopifyProductRecommendationsResponseDoc
ShopifyProductRecommendationsParams = TypedDict('ShopifyProductRecommendationsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'handle': Required[str],
    'url': Required[str],
    'limit': NotRequired[int],
    'intent': NotRequired[Literal['related', 'complementary']],
}, total=False)

ShopifySearchSuggestResponse = ModelShopifySearchSuggestResponseDoc
ShopifySearchSuggestParams = TypedDict('ShopifySearchSuggestParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'url': Required[str],
    'q': Required[str],
    'types': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

ShopifySitemapUrlsResponse = ModelShopifySitemapUrlsResponseDoc
ShopifySitemapUrlsParams = TypedDict('ShopifySitemapUrlsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'url': Required[str],
    'type': NotRequired[Literal['all', 'products', 'collections', 'pages', 'blogs', 'agentic_discovery', 'other']],
    'limit': NotRequired[int],
}, total=False)

ShopifySitemapsResponse = ModelShopifySitemapIndexResponseDoc
ShopifySitemapsParams = TypedDict('ShopifySitemapsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'url': Required[str],
}, total=False)

ShopifyStoreResponse = ModelShopifyStoreResponseDoc
ShopifyStoreParams = TypedDict('ShopifyStoreParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'url': Required[str],
}, total=False)

SimilarWebSearchResponse = ModelSimilarwebSearchResponseDoc
SimilarWebSearchParams = TypedDict('SimilarWebSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
}, total=False)

SimilarWebWebResponse = ModelSimilarwebWebResponseDoc
SimilarWebWebParams = TypedDict('SimilarWebWebParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'domain': Required[str],
}, total=False)

SpotifyPodcastsCategoriesResponse = ModelSpotifyBrowsePageResponseDoc
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

SpotifyPodcastsChartsResponse = ModelSpotifyChartsResponseDoc
SpotifyPodcastsChartsParams = TypedDict('SpotifyPodcastsChartsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'chart': NotRequired[str],
    'region': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

SpotifyPodcastsEpisodeResponse = ModelSpotifyEpisodeResponseDoc
SpotifyPodcastsEpisodeParams = TypedDict('SpotifyPodcastsEpisodeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyPodcastsHomeResponse = ModelSpotifyBrowsePageResponseDoc
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

SpotifyPodcastsSearchResponse = ModelSpotifySearchResponseDoc
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

SpotifyPodcastsShowResponse = ModelSpotifyShowResponseDoc
SpotifyPodcastsShowParams = TypedDict('SpotifyPodcastsShowParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'include_content_capability_trait': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsShowEpisodesResponse = ModelSpotifyShowEpisodesResponseDoc
SpotifyPodcastsShowEpisodesParams = TypedDict('SpotifyPodcastsShowEpisodesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsShowRecommendationsResponse = ModelSpotifyShowRecommendationsResponseDoc
SpotifyPodcastsShowRecommendationsParams = TypedDict('SpotifyPodcastsShowRecommendationsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
}, total=False)

SpotifyAlbumResponse = ModelSpotifyAlbumResponseDoc
SpotifyAlbumParams = TypedDict('SpotifyAlbumParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyAlbumTracksResponse = ModelSpotifyAlbumResponseDoc
SpotifyAlbumTracksParams = TypedDict('SpotifyAlbumTracksParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyAlbumsSearchResponse = ModelSpotifySearchCatalogResponseDoc
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

SpotifyArtistResponse = ModelSpotifyArtistResponseDoc
SpotifyArtistParams = TypedDict('SpotifyArtistParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyArtistAlbumsResponse = ModelSpotifyArtistAlbumsResponseDoc
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

SpotifyArtistPlaylistsResponse = ModelSpotifyArtistCollectionResponseDoc
SpotifyArtistPlaylistsParams = TypedDict('SpotifyArtistPlaylistsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyArtistRelatedResponse = ModelSpotifyArtistCollectionResponseDoc
SpotifyArtistRelatedParams = TypedDict('SpotifyArtistRelatedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyArtistsSearchResponse = ModelSpotifySearchCatalogResponseDoc
SpotifyArtistsSearchParams = TypedDict('SpotifyArtistsSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyAudiobookResponse = ModelSpotifyAudiobookResponseDoc
SpotifyAudiobookParams = TypedDict('SpotifyAudiobookParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyAudiobookChaptersResponse = ModelSpotifyAudiobookChaptersResponseDoc
SpotifyAudiobookChaptersParams = TypedDict('SpotifyAudiobookChaptersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyAudiobooksSearchResponse = ModelSpotifySearchCatalogResponseDoc
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

SpotifyChapterResponse = ModelSpotifyEpisodeResponseDoc
SpotifyChapterParams = TypedDict('SpotifyChapterParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyEpisodesSearchResponse = ModelSpotifySearchCatalogResponseDoc
SpotifyEpisodesSearchParams = TypedDict('SpotifyEpisodesSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyFeaturedChartsByCountryResponse = ModelSpotifyCountryHubContentResponseDoc
SpotifyFeaturedChartsByCountryParams = TypedDict('SpotifyFeaturedChartsByCountryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country_code': NotRequired[str],
    'content_id': NotRequired[str],
}, total=False)

SpotifyGenreResponse = ModelSpotifyBrowsePageResponseDoc
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

SpotifyHomeResponse = ModelSpotifyHomeResponseDoc
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

SpotifyPlaylistResponse = ModelSpotifyPlaylistResponseDoc
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

SpotifyPlaylistsSearchResponse = ModelSpotifySearchCatalogResponseDoc
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

SpotifyPopularByCountryResponse = ModelSpotifyCountryHubResponseDoc
SpotifyPopularByCountryParams = TypedDict('SpotifyPopularByCountryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country_code': NotRequired[str],
}, total=False)

SpotifyProfileResponse = ModelSpotifyUserProfileResponseDoc
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

SpotifyProfileFollowersResponse = ModelSpotifyUserProfileFollowersResponseDoc
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

SpotifyProfilePlaylistsResponse = ModelSpotifyUserProfilePlaylistsResponseDoc
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

SpotifyProfilesSearchResponse = ModelSpotifySearchCatalogResponseDoc
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

SpotifySearchResponse = ModelSpotifySearchCatalogResponseDoc
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

SpotifySectionResponse = ModelSpotifyBrowseSectionResponseDoc
SpotifySectionParams = TypedDict('SpotifySectionParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyShowsSearchResponse = ModelSpotifySearchCatalogResponseDoc
SpotifyShowsSearchParams = TypedDict('SpotifyShowsSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyTrackResponse = ModelSpotifyTrackResponseDoc
SpotifyTrackParams = TypedDict('SpotifyTrackParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyTrackRecommendedResponse = ModelSpotifyTrackRecommendedResponseDoc
SpotifyTrackRecommendedParams = TypedDict('SpotifyTrackRecommendedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

SpotifyTrackSimilarAlbumsResponse = ModelSpotifyTrackSimilarAlbumsResponseDoc
SpotifyTrackSimilarAlbumsParams = TypedDict('SpotifyTrackSimilarAlbumsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'limit': NotRequired[int],
    'albums_only': NotRequired[bool],
}, total=False)

SpotifyTracksSearchResponse = ModelSpotifySearchCatalogResponseDoc
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

TiktokCategoryResponse = ModelTiktokCategoryResponseDoc
TiktokCategoryParams = TypedDict('TiktokCategoryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokVideoCommentsResponse = ModelTiktokCommentsResponseDoc
TiktokVideoCommentsParams = TypedDict('TiktokVideoCommentsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'aweme_id': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokExploreResponse = ModelTiktokExploreResponseDoc
TiktokExploreParams = TypedDict('TiktokExploreParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[int],
}, total=False)

TiktokChallengeResponse = ModelTiktokChallengeResponseDoc
TiktokChallengeParams = TypedDict('TiktokChallengeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'name': Required[str],
}, total=False)

TiktokChallengeListResponse = ModelTiktokChallengeListResponseDoc
TiktokChallengeListParams = TypedDict('TiktokChallengeListParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokPopularTrendCountryIndustryMetaResponse = ModelPopulartrendCountryIndustryMetaResponseDoc
TiktokPopularTrendCountryIndustryMetaParams = TypedDict('TiktokPopularTrendCountryIndustryMetaParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokPopularTrendCreatorResponse = ModelPopulartrendCreatorTrendResponseDoc
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

TiktokPostResponse = ModelTiktokPostResponseDoc
TiktokPostParams = TypedDict('TiktokPostParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

TiktokProfilePostResponse = ModelTiktokProfilePostResponseDoc
TiktokProfilePostParams = TypedDict('TiktokProfilePostParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'secUid': Required[str],
    'cursor': NotRequired[int],
    'sort_type': NotRequired[Literal['0', '1', '2']],
}, total=False)

TiktokProfileResponse = ModelTiktokProfileResponseDoc
TiktokProfileParams = TypedDict('TiktokProfileParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'handler': Required[str],
}, total=False)

TiktokSearchResponse = ModelTiktokSearchResponseDoc
TiktokSearchParams = TypedDict('TiktokSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokSearchHashtagResponse = ModelTiktokSearchHashtagResponseDoc
TiktokSearchHashtagParams = TypedDict('TiktokSearchHashtagParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokSearchUserResponse = ModelTiktokSearchUserResponseDoc
TiktokSearchUserParams = TypedDict('TiktokSearchUserParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokTopAdsAnalysisResponse = ModelPopulartrendTopAdsAnalysisResponseDoc
TiktokTopAdsAnalysisParams = TypedDict('TiktokTopAdsAnalysisParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'material_id': Required[str],
    'metric': NotRequired[Literal['retain_ctr', 'retain_cvr', 'click_cnt', 'convert_cnt', 'play_retain_cnt']],
    'period_type': NotRequired[Literal['7', '30', '180']],
}, total=False)

TiktokTopAdsDetailResponse = ModelPopulartrendTopAdsDetailResponseDoc
TiktokTopAdsDetailParams = TypedDict('TiktokTopAdsDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'material_id': Required[str],
}, total=False)

TiktokTopAdsFiltersResponse = ModelPopulartrendTopAdsFiltersResponseDoc
TiktokTopAdsFiltersParams = TypedDict('TiktokTopAdsFiltersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokTopAdsListResponse = ModelPopulartrendTopAdsListResponseDoc
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

TiktokTopAdsLocationInfoResponse = ModelPopulartrendTopAdsLocationInfoResponseDoc
TiktokTopAdsLocationInfoParams = TypedDict('TiktokTopAdsLocationInfoParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'module': NotRequired[int],
}, total=False)

TiktokTopAdsLocationsResponse = ModelPopulartrendTopAdsLocationsResponseDoc
TiktokTopAdsLocationsParams = TypedDict('TiktokTopAdsLocationsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokTopAdsRecommendResponse = ModelPopulartrendTopAdsRecommendResponseDoc
TiktokTopAdsRecommendParams = TypedDict('TiktokTopAdsRecommendParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'material_id': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

TiktokTopAdsSafetyResponse = ModelPopulartrendTopAdsSafetyResponseDoc
TiktokTopAdsSafetyParams = TypedDict('TiktokTopAdsSafetyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokTopAdsSpotlightResponse = ModelPopulartrendTopAdsSpotlightResponseDoc
TiktokTopAdsSpotlightParams = TypedDict('TiktokTopAdsSpotlightParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

TiktokTopAdsSuggestionsResponse = ModelPopulartrendTopAdsSuggestionsResponseDoc
TiktokTopAdsSuggestionsParams = TypedDict('TiktokTopAdsSuggestionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'count': NotRequired[int],
    'scenario': NotRequired[int],
}, total=False)

TiktokTrendingResponse = ModelTiktokTrendingResponseDoc
TiktokTrendingParams = TypedDict('TiktokTrendingParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TripAdvisorTripadvisorAutocompleteResponse = ModelTripadvisorTripadvisorAutocompleteResponseDoc
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

TripAdvisorTripadvisorEnumsResponse = ModelTripadvisorTripadvisorEnumsResponseDoc
TripAdvisorTripadvisorEnumsParams = TypedDict('TripAdvisorTripadvisorEnumsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TripAdvisorTripadvisorHotelsResponse = ModelTripadvisorTripadvisorHotelsResponseDoc
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

TripAdvisorTripadvisorPlaceResponse = ModelTripadvisorPlaceResponse
TripAdvisorTripadvisorPlaceParams = TypedDict('TripAdvisorTripadvisorPlaceParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'url': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

TripAdvisorTripadvisorReviewsResponse = ModelTripadvisorTripadvisorReviewsResponseDoc
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

TripAdvisorTripadvisorSearchResponse = ModelTripadvisorTripadvisorSearchResponseDoc
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

TrustpilotBusinessSearchResponse = ModelTrustpilotBusinessSearchResponseDoc
TrustpilotBusinessSearchParams = TypedDict('TrustpilotBusinessSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'country': NotRequired[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

TrustpilotBusinessResponse = ModelTrustpilotBusinessProfileResponseDoc
TrustpilotBusinessParams = TypedDict('TrustpilotBusinessParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
}, total=False)

TrustpilotBusinessRelatedResponse = ModelTrustpilotBusinessRelatedResponseDoc
TrustpilotBusinessRelatedParams = TypedDict('TrustpilotBusinessRelatedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
}, total=False)

TrustpilotBusinessReviewsResponse = ModelTrustpilotBusinessReviewsResponseDoc
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

TrustpilotCategoriesResponse = ModelTrustpilotCategoriesResponseDoc
TrustpilotCategoriesParams = TypedDict('TrustpilotCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TrustpilotCategorySearchResponse = ModelTrustpilotCategorySearchResponseDoc
TrustpilotCategorySearchParams = TypedDict('TrustpilotCategorySearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'country': NotRequired[str],
    'locale': NotRequired[str],
    'size': NotRequired[int],
}, total=False)

TrustpilotCategoryResponse = ModelTrustpilotCategoryResponseDoc
TrustpilotCategoryParams = TypedDict('TrustpilotCategoryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
    'page': NotRequired[int],
}, total=False)

UsageMeEndpointsResponse = ModelUsageUsageEndpointsResponseDoc
UsageMeEndpointsParams = TypedDict('UsageMeEndpointsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'range': NotRequired[Literal['period', 'day', 'week', 'month', 'custom']],
    'limit': NotRequired[int],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

UsageMeOverviewResponse = ModelUsageUsageOverviewResponseDoc
UsageMeOverviewParams = TypedDict('UsageMeOverviewParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'range': NotRequired[Literal['period', 'day', 'week', 'month', 'custom']],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

UsageMeRecentIpsResponse = ModelUsageUsageRecentIpsResponseDoc
UsageMeRecentIpsParams = TypedDict('UsageMeRecentIpsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'range': NotRequired[Literal['period', 'day', 'week', 'month', 'custom']],
    'limit': NotRequired[int],
    'from': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

UsageMeTimeseriesResponse = ModelUsageUsageTimeseriesResponseDoc
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

UserMeResponse = ModelUserUserMeResponseDoc
UserMeParams = TypedDict('UserMeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

UserMeApiKeysResponse = ModelUserUserApikeysResponseDoc
UserMeApiKeysParams = TypedDict('UserMeApiKeysParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

UserMeApiKeysRotateResponse = ModelUserUserRotateApikeyResponseDoc
UserMeApiKeysRotateParams = TypedDict('UserMeApiKeysRotateParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

UserMeApiKeysRevealResponse = ModelUserUserRevealApikeyResponseDoc
UserMeApiKeysRevealParams = TypedDict('UserMeApiKeysRevealParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

YahooFinanceCalendarsResponse = ModelYahoofinanceCalendarsResponseDoc
YahooFinanceCalendarsParams = TypedDict('YahooFinanceCalendarsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

YahooFinanceCalendarResponse = ModelYahoofinanceCalendarResponseDoc
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

YahooFinanceDownloadBody = ModelYahoofinanceDownloadRequest
YahooFinanceDownloadResponse = ModelYahoofinanceDownloadResponseDoc
YahooFinanceDownloadParams = TypedDict('YahooFinanceDownloadParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[YahooFinanceDownloadBody],
}, total=False)

YahooFinanceIndustriesResponse = ModelYahoofinanceDomainListResponseDoc
YahooFinanceIndustriesParams = TypedDict('YahooFinanceIndustriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

YahooFinanceIndustryResponse = ModelYahoofinanceIndustryResponseDoc
YahooFinanceIndustryParams = TypedDict('YahooFinanceIndustryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'key': Required[str],
}, total=False)

YahooFinanceMarketStatusResponse = ModelYahoofinanceMarketStatusResponseDoc
YahooFinanceMarketStatusParams = TypedDict('YahooFinanceMarketStatusParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'market': Required[str],
}, total=False)

YahooFinanceMarketSummaryResponse = ModelYahoofinanceMarketSummaryResponseDoc
YahooFinanceMarketSummaryParams = TypedDict('YahooFinanceMarketSummaryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'market': Required[str],
}, total=False)

YahooFinanceScreenerCustomBody = ModelYahoofinanceScreenerRequest
YahooFinanceScreenerCustomResponse = ModelYahoofinanceScreenerResponseDoc
YahooFinanceScreenerCustomParams = TypedDict('YahooFinanceScreenerCustomParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[YahooFinanceScreenerCustomBody],
}, total=False)

YahooFinanceScreenerResponse = ModelYahoofinanceScreenerResponseDoc
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

YahooFinanceScreenersResponse = ModelYahoofinanceScreenersResponseDoc
YahooFinanceScreenersParams = TypedDict('YahooFinanceScreenersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

YahooFinanceSearchResponse = ModelYahoofinanceSearchResponseDoc
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

YahooFinanceSectorsResponse = ModelYahoofinanceDomainListResponseDoc
YahooFinanceSectorsParams = TypedDict('YahooFinanceSectorsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

YahooFinanceSectorResponse = ModelYahoofinanceSectorResponseDoc
YahooFinanceSectorParams = TypedDict('YahooFinanceSectorParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'key': Required[str],
}, total=False)

YahooFinanceTickerActionsResponse = ModelYahoofinanceActionsResponseDoc
YahooFinanceTickerActionsParams = TypedDict('YahooFinanceTickerActionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerAnalystsResponse = ModelYahoofinanceModuleResponseDoc
YahooFinanceTickerAnalystsParams = TypedDict('YahooFinanceTickerAnalystsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerCalendarResponse = ModelYahoofinanceModuleResponseDoc
YahooFinanceTickerCalendarParams = TypedDict('YahooFinanceTickerCalendarParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerCapitalGainsResponse = ModelYahoofinanceActionsResponseDoc
YahooFinanceTickerCapitalGainsParams = TypedDict('YahooFinanceTickerCapitalGainsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerDividendsResponse = ModelYahoofinanceActionsResponseDoc
YahooFinanceTickerDividendsParams = TypedDict('YahooFinanceTickerDividendsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerEarningsResponse = ModelYahoofinanceModuleResponseDoc
YahooFinanceTickerEarningsParams = TypedDict('YahooFinanceTickerEarningsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerEarningsDatesResponse = ModelYahoofinanceEarningsDatesResponseDoc
YahooFinanceTickerEarningsDatesParams = TypedDict('YahooFinanceTickerEarningsDatesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

YahooFinanceTickerFinancialsResponse = ModelYahoofinanceFinancialsResponseDoc
YahooFinanceTickerFinancialsParams = TypedDict('YahooFinanceTickerFinancialsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
    'statement': NotRequired[str],
    'period': NotRequired[str],
}, total=False)

YahooFinanceTickerFundsResponse = ModelYahoofinanceModuleResponseDoc
YahooFinanceTickerFundsParams = TypedDict('YahooFinanceTickerFundsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerHistoryResponse = ModelYahoofinanceHistoryResponseDoc
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

YahooFinanceTickerHistoryMetadataResponse = ModelYahoofinanceHistoryMetadataResponseDoc
YahooFinanceTickerHistoryMetadataParams = TypedDict('YahooFinanceTickerHistoryMetadataParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerHoldersResponse = ModelYahoofinanceModuleResponseDoc
YahooFinanceTickerHoldersParams = TypedDict('YahooFinanceTickerHoldersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerInfoResponse = ModelYahoofinanceInfoResponseDoc
YahooFinanceTickerInfoParams = TypedDict('YahooFinanceTickerInfoParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerIsinResponse = ModelYahoofinanceIsinResponseDoc
YahooFinanceTickerIsinParams = TypedDict('YahooFinanceTickerIsinParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerNewsResponse = ModelYahoofinanceSearchResponseDoc
YahooFinanceTickerNewsParams = TypedDict('YahooFinanceTickerNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
    'count': NotRequired[int],
    'tab': NotRequired[str],
}, total=False)

YahooFinanceTickerOptionsResponse = ModelYahoofinanceOptionsResponseDoc
YahooFinanceTickerOptionsParams = TypedDict('YahooFinanceTickerOptionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerOptionsExpirationResponse = ModelYahoofinanceOptionsResponseDoc
YahooFinanceTickerOptionsExpirationParams = TypedDict('YahooFinanceTickerOptionsExpirationParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
    'expiration': Required[str],
}, total=False)

YahooFinanceTickerQuoteResponse = ModelYahoofinanceQuoteResponseDoc
YahooFinanceTickerQuoteParams = TypedDict('YahooFinanceTickerQuoteParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerSecFilingsResponse = ModelYahoofinanceModuleResponseDoc
YahooFinanceTickerSecFilingsParams = TypedDict('YahooFinanceTickerSecFilingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerSharesResponse = ModelYahoofinanceSharesResponseDoc
YahooFinanceTickerSharesParams = TypedDict('YahooFinanceTickerSharesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerSharesFullResponse = ModelYahoofinanceSharesFullResponseDoc
YahooFinanceTickerSharesFullParams = TypedDict('YahooFinanceTickerSharesFullParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
    'start': NotRequired[str],
    'end': NotRequired[str],
}, total=False)

YahooFinanceTickerSplitsResponse = ModelYahoofinanceActionsResponseDoc
YahooFinanceTickerSplitsParams = TypedDict('YahooFinanceTickerSplitsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerSustainabilityResponse = ModelYahoofinanceModuleResponseDoc
YahooFinanceTickerSustainabilityParams = TypedDict('YahooFinanceTickerSustainabilityParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTickerValuationResponse = ModelYahoofinanceValuationResponseDoc
YahooFinanceTickerValuationParams = TypedDict('YahooFinanceTickerValuationParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'symbol': Required[str],
}, total=False)

YahooFinanceTrendingResponse = ModelYahoofinanceTrendingResponseDoc
YahooFinanceTrendingParams = TypedDict('YahooFinanceTrendingParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'region': Required[str],
    'count': NotRequired[int],
}, total=False)

YoutubeCaptionsResponse = ModelYoutubeCaptionsResponseDoc
YoutubeCaptionsParams = TypedDict('YoutubeCaptionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'lang': NotRequired[str],
}, total=False)

YoutubeChannelPlaylistsResponse = ModelYoutubeChannelFeedResponseDoc
YoutubeChannelPlaylistsParams = TypedDict('YoutubeChannelPlaylistsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'continuation_token': NotRequired[str],
}, total=False)

YoutubeChannelSearchResponse = ModelYoutubeChannelSearchResponseDoc
YoutubeChannelSearchParams = TypedDict('YoutubeChannelSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'q': Required[str],
    'continuation_token': NotRequired[str],
}, total=False)

YoutubeChannelShortsResponse = ModelYoutubeChannelShortsResponseDoc
YoutubeChannelShortsParams = TypedDict('YoutubeChannelShortsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

YoutubeChannelVideosResponse = ModelYoutubeChannelFeedResponseDoc
YoutubeChannelVideosParams = TypedDict('YoutubeChannelVideosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'continuation_token': NotRequired[str],
}, total=False)

YoutubeCommentsResponse = ModelYoutubeCommentsResponseDoc
YoutubeCommentsParams = TypedDict('YoutubeCommentsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'continuation_token': NotRequired[str],
}, total=False)

YoutubePlaylistResponse = ModelYoutubePlaylistResponseDoc
YoutubePlaylistParams = TypedDict('YoutubePlaylistParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'continuation_token': NotRequired[str],
}, total=False)

YoutubeProfileResponse = ModelYoutubeProfileResponseDoc
YoutubeProfileParams = TypedDict('YoutubeProfileParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

YoutubeSearchResponse = ModelYoutubeSearchResponseDoc
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

YoutubeTagResponse = ModelYoutubeTagResponseDoc
YoutubeTagParams = TypedDict('YoutubeTagParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'tag': Required[str],
    'type': NotRequired[Literal['all', 'shorts']],
    'continuation_token': NotRequired[str],
}, total=False)

YoutubeTranscriptResponse = ModelYoutubeTranscriptResponseDoc
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

YoutubeTranscriptLanguagesResponse = ModelYoutubeTranscriptLanguagesResponseDoc
YoutubeTranscriptLanguagesParams = TypedDict('YoutubeTranscriptLanguagesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

YoutubeVideoResponse = ModelYoutubeVideoResponseDoc
YoutubeVideoParams = TypedDict('YoutubeVideoParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

ZillowAutocompleteResponse = ModelZillowAutocompleteResponse
ZillowAutocompleteParams = TypedDict('ZillowAutocompleteParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'query': Required[str],
    'limit': NotRequired[int],
    'status': NotRequired[str],
}, total=False)

ZillowPropertyResponse = ModelZillowPropertyResponse
ZillowPropertyParams = TypedDict('ZillowPropertyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'zpid': Required[str],
}, total=False)

ZillowSearchResponse = ModelZillowSearchResponse
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

class ShopAppGroup:
    def analysis(self, **params: Unpack[ShopAppAnalysisParams]) -> ShopAppAnalysisResponse: ...
    def categories(self, **params: Unpack[ShopAppCategoriesParams]) -> ShopAppCategoriesResponse: ...
    def product(self, **params: Unpack[ShopAppProductParams]) -> ShopAppProductResponse: ...
    def product_related(self, **params: Unpack[ShopAppProductRelatedParams]) -> ShopAppProductRelatedResponse: ...
    def product_reviews(self, **params: Unpack[ShopAppProductReviewsParams]) -> ShopAppProductReviewsResponse: ...
    def product_shop(self, **params: Unpack[ShopAppProductShopParams]) -> ShopAppProductShopResponse: ...
    def product_variant(self, **params: Unpack[ShopAppProductVariantParams]) -> ShopAppProductVariantResponse: ...
    def product_variants(self, **params: Unpack[ShopAppProductVariantsParams]) -> ShopAppProductVariantsResponse: ...
    def search(self, **params: Unpack[ShopAppSearchParams]) -> ShopAppSearchResponse: ...
    def shop(self, **params: Unpack[ShopAppShopParams]) -> ShopAppShopResponse: ...
    def collection_products(self, **params: Unpack[ShopAppCollectionProductsParams]) -> ShopAppCollectionProductsResponse: ...
    def shop_locations(self, **params: Unpack[ShopAppShopLocationsParams]) -> ShopAppShopLocationsResponse: ...
    def shop_products(self, **params: Unpack[ShopAppShopProductsParams]) -> ShopAppShopProductsResponse: ...
    def shop_reviews(self, **params: Unpack[ShopAppShopReviewsParams]) -> ShopAppShopReviewsResponse: ...
    def shop_typeahead(self, **params: Unpack[ShopAppShopTypeaheadParams]) -> ShopAppShopTypeaheadResponse: ...
    def suggestions(self, **params: Unpack[ShopAppSuggestionsParams]) -> ShopAppSuggestionsResponse: ...

class ShopifyGroup:
    def collections(self, **params: Unpack[ShopifyCollectionsParams]) -> ShopifyCollectionsResponse: ...
    def collection_products(self, **params: Unpack[ShopifyCollectionProductsParams]) -> ShopifyCollectionProductsResponse: ...
    def pages(self, **params: Unpack[ShopifyPagesParams]) -> ShopifyPagesResponse: ...
    def page(self, **params: Unpack[ShopifyPageParams]) -> ShopifyPageResponse: ...
    def products(self, **params: Unpack[ShopifyProductsParams]) -> ShopifyProductsResponse: ...
    def product(self, **params: Unpack[ShopifyProductParams]) -> ShopifyProductResponse: ...
    def product_recommendations(self, **params: Unpack[ShopifyProductRecommendationsParams]) -> ShopifyProductRecommendationsResponse: ...
    def search_suggest(self, **params: Unpack[ShopifySearchSuggestParams]) -> ShopifySearchSuggestResponse: ...
    def sitemap_urls(self, **params: Unpack[ShopifySitemapUrlsParams]) -> ShopifySitemapUrlsResponse: ...
    def sitemaps(self, **params: Unpack[ShopifySitemapsParams]) -> ShopifySitemapsResponse: ...
    def store(self, **params: Unpack[ShopifyStoreParams]) -> ShopifyStoreResponse: ...

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

OperationId = Literal[
    'airbnb-room',
    'airbnb-room-calendar',
    'airbnb-room-reviews',
    'airbnb-search',
    'amazon-product',
    'amazon-search',
    'amazon-suggest',
    'apple-podcasts-charts',
    'apple-podcasts-episodes-search',
    'apple-podcasts-search',
    'apple-podcasts-show',
    'apple-podcasts-show-episodes',
    'appstore-app',
    'appstore-developer',
    'appstore-list',
    'appstore-privacy',
    'appstore-ratings',
    'appstore-reviews',
    'appstore-search',
    'appstore-similar',
    'appstore-suggest',
    'appstore-version-history',
    'billing-me',
    'billing-me-checkout',
    'billing-me-events',
    'billing-me-periods',
    'billing-me-period',
    'billing-me-period-statement',
    'billing-me-period-statement-download',
    'billing-me-portal',
    'bing-images',
    'bing-news',
    'bing-search',
    'bing-suggest',
    'bing-videos',
    'brave-images',
    'brave-news',
    'brave-search',
    'brave-suggest',
    'brave-videos',
    'coingecko-categories',
    'coingecko-category-coins',
    'coingecko-chains',
    'coingecko-chain',
    'coingecko-coin',
    'coingecko-coin-analysis',
    'coingecko-exchange',
    'coingecko-exchanges',
    'coingecko-gainers-losers',
    'coingecko-global',
    'coingecko-global-charts',
    'coingecko-learn-articles',
    'coingecko-markets',
    'coingecko-new-coins',
    'coingecko-news',
    'coingecko-nft-category',
    'coingecko-nfts',
    'coingecko-search',
    'coingecko-token-unlocks',
    'coingecko-treasuries',
    'coingecko-trending',
    'datasets-list',
    'datasets-google-map-businesses-facets',
    'datasets-google-map-businesses-item',
    'datasets-google-map-businesses-nearby',
    'datasets-google-map-businesses-search',
    'ebay-item',
    'ebay-search',
    'ebay-seller',
    'ebay-seller-about',
    'ebay-seller-feedback',
    'ebay-seller-shop',
    'geocoding-lookup',
    'geocoding-reverse',
    'geocoding-search',
    'google-finance-analyst-articles',
    'google-finance-chart',
    'google-finance-classification',
    'google-finance-company',
    'google-finance-context',
    'google-finance-financials',
    'google-finance-markets-category-news',
    'google-finance-markets-category-stocks',
    'google-finance-markets-earnings',
    'google-finance-markets-featured',
    'google-finance-markets-headline',
    'google-finance-markets-indices',
    'google-finance-markets-movers',
    'google-finance-markets-top',
    'google-finance-markets-trending',
    'google-finance-news',
    'google-finance-quote',
    'google-finance-related',
    'google-finance-search',
    'google-finance-ticker',
    'google-jobs',
    'google-map-place',
    'google-map-search',
    'google-search',
    'google-suggest',
    'google-trends-categories',
    'google-trends-enums',
    'google-trends-explore',
    'google-trends-explore-interest-by-region',
    'google-trends-explore-interest-over-time',
    'google-trends-explore-related-topics',
    'google-trends-explore-rising-queries',
    'google-trends-explore-top-queries',
    'google-trends-locations',
    'google-trends-trending',
    'google-trends-trending-detail',
    'googleplay-app',
    'googleplay-categories',
    'googleplay-datasafety',
    'googleplay-developer',
    'googleplay-list',
    'googleplay-permissions',
    'googleplay-reviews',
    'googleplay-search',
    'googleplay-similar',
    'googleplay-suggest',
    'instagram-post',
    'instagram-profile',
    'instagram-reels',
    'justwatch-age-certifications',
    'justwatch-discover',
    'justwatch-episode-by-id',
    'justwatch-episode-offers',
    'justwatch-genre-titles',
    'justwatch-genres',
    'justwatch-monetization-titles',
    'justwatch-new',
    'justwatch-popular',
    'justwatch-provider-titles',
    'justwatch-providers',
    'justwatch-search',
    'justwatch-season-by-id',
    'justwatch-season-episodes',
    'justwatch-show-seasons',
    'justwatch-title',
    'justwatch-title-analysis',
    'justwatch-title-by-id',
    'justwatch-title-media',
    'justwatch-title-offers',
    'justwatch-title-similar',
    'linkedin-company',
    'linkedin-product',
    'linkedin-showcase',
    'ping',
    'producthunt-category',
    'producthunt-category-products',
    'producthunt-leaderboard',
    'producthunt-product',
    'producthunt-about',
    'producthunt-alternatives',
    'producthunt-customers',
    'producthunt-launches',
    'producthunt-makers',
    'producthunt-reviews',
    'producthunt-search',
    'ready',
    'referrals-click',
    'referrals-me',
    'referrals-me-events',
    'shop-app-analysis',
    'shop-app-categories',
    'shop-app-product',
    'shop-app-product-related',
    'shop-app-product-reviews',
    'shop-app-product-shop',
    'shop-app-product-variant',
    'shop-app-product-variants',
    'shop-app-search',
    'shop-app-shop',
    'shop-app-collection-products',
    'shop-app-shop-locations',
    'shop-app-shop-products',
    'shop-app-shop-reviews',
    'shop-app-shop-typeahead',
    'shop-app-suggestions',
    'shopify-collections',
    'shopify-collection-products',
    'shopify-pages',
    'shopify-page',
    'shopify-products',
    'shopify-product',
    'shopify-product-recommendations',
    'shopify-search-suggest',
    'shopify-sitemap-urls',
    'shopify-sitemaps',
    'shopify-store',
    'similarweb-search',
    'similarweb-web',
    'spotify-podcasts-categories',
    'spotify-podcasts-charts',
    'spotify-podcasts-episode',
    'spotify-podcasts-home',
    'spotify-podcasts-search',
    'spotify-podcasts-show',
    'spotify-podcasts-show-episodes',
    'spotify-podcasts-show-recommendations',
    'spotify-album',
    'spotify-album-tracks',
    'spotify-albums-search',
    'spotify-artist',
    'spotify-artist-albums',
    'spotify-artist-playlists',
    'spotify-artist-related',
    'spotify-artists-search',
    'spotify-audiobook',
    'spotify-audiobook-chapters',
    'spotify-audiobooks-search',
    'spotify-chapter',
    'spotify-episodes-search',
    'spotify-featured-charts-by-country',
    'spotify-genre',
    'spotify-home',
    'spotify-playlist',
    'spotify-playlists-search',
    'spotify-popular-by-country',
    'spotify-profile',
    'spotify-profile-followers',
    'spotify-profile-playlists',
    'spotify-profiles-search',
    'spotify-search',
    'spotify-section',
    'spotify-shows-search',
    'spotify-track',
    'spotify-track-recommended',
    'spotify-track-similar-albums',
    'spotify-tracks-search',
    'tiktok-category',
    'tiktok-video-comments',
    'tiktok-explore',
    'tiktok-challenge',
    'tiktok-challenge-list',
    'tiktok-popular-trend-country-industry-meta',
    'tiktok-popular-trend-creator',
    'tiktok-post',
    'tiktok-profile-post',
    'tiktok-profile',
    'tiktok-search',
    'tiktok-search-hashtag',
    'tiktok-search-user',
    'tiktok-top-ads-analysis',
    'tiktok-top-ads-detail',
    'tiktok-top-ads-filters',
    'tiktok-top-ads-list',
    'tiktok-top-ads-location-info',
    'tiktok-top-ads-locations',
    'tiktok-top-ads-recommend',
    'tiktok-top-ads-safety',
    'tiktok-top-ads-spotlight',
    'tiktok-top-ads-suggestions',
    'tiktok-trending',
    'tripadvisor-autocomplete',
    'tripadvisor-enums',
    'tripadvisor-hotels',
    'tripadvisor-place',
    'tripadvisor-reviews',
    'tripadvisor-search',
    'trustpilot-business-search',
    'trustpilot-business',
    'trustpilot-business-related',
    'trustpilot-business-reviews',
    'trustpilot-categories',
    'trustpilot-category-search',
    'trustpilot-category',
    'usage-me-endpoints',
    'usage-me-overview',
    'usage-me-recent-ips',
    'usage-me-timeseries',
    'user-me',
    'user-me-api-keys',
    'user-me-api-keys-rotate',
    'user-me-api-keys-reveal',
    'yahoo-finance-calendars',
    'yahoo-finance-calendar',
    'yahoo-finance-download',
    'yahoo-finance-industries',
    'yahoo-finance-industry',
    'yahoo-finance-market-status',
    'yahoo-finance-market-summary',
    'yahoo-finance-screener-custom',
    'yahoo-finance-screener',
    'yahoo-finance-screeners',
    'yahoo-finance-search',
    'yahoo-finance-sectors',
    'yahoo-finance-sector',
    'yahoo-finance-ticker-actions',
    'yahoo-finance-ticker-analysts',
    'yahoo-finance-ticker-calendar',
    'yahoo-finance-ticker-capital-gains',
    'yahoo-finance-ticker-dividends',
    'yahoo-finance-ticker-earnings',
    'yahoo-finance-ticker-earnings-dates',
    'yahoo-finance-ticker-financials',
    'yahoo-finance-ticker-funds',
    'yahoo-finance-ticker-history',
    'yahoo-finance-ticker-history-metadata',
    'yahoo-finance-ticker-holders',
    'yahoo-finance-ticker-info',
    'yahoo-finance-ticker-isin',
    'yahoo-finance-ticker-news',
    'yahoo-finance-ticker-options',
    'yahoo-finance-ticker-options-expiration',
    'yahoo-finance-ticker-quote',
    'yahoo-finance-ticker-sec-filings',
    'yahoo-finance-ticker-shares',
    'yahoo-finance-ticker-shares-full',
    'yahoo-finance-ticker-splits',
    'yahoo-finance-ticker-sustainability',
    'yahoo-finance-ticker-valuation',
    'yahoo-finance-trending',
    'youtube-captions',
    'youtube-channel-playlists',
    'youtube-channel-search',
    'youtube-channel-shorts',
    'youtube-channel-videos',
    'youtube-comments',
    'youtube-playlist',
    'youtube-profile',
    'youtube-search',
    'youtube-tag',
    'youtube-transcript',
    'youtube-transcript-languages',
    'youtube-video',
    'zillow-autocomplete',
    'zillow-property',
    'zillow-search',
]

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
    shop_app: ShopAppGroup
    shopify: ShopifyGroup
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
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['airbnb-room'],
        params: AirbnbRoomParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AirbnbRoomResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['airbnb-room-calendar'],
        params: AirbnbRoomCalendarParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AirbnbRoomCalendarResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['airbnb-room-reviews'],
        params: AirbnbRoomReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AirbnbRoomReviewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['airbnb-search'],
        params: AirbnbSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AirbnbSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['amazon-product'],
        params: AmazonProductParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AmazonProductResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['amazon-search'],
        params: AmazonSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AmazonSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['amazon-suggest'],
        params: AmazonSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AmazonSuggestResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['apple-podcasts-charts'],
        params: ApplePodcastsChartsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ApplePodcastsChartsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['apple-podcasts-episodes-search'],
        params: ApplePodcastsEpisodesSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ApplePodcastsEpisodesSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['apple-podcasts-search'],
        params: ApplePodcastsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ApplePodcastsSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['apple-podcasts-show'],
        params: ApplePodcastsShowParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ApplePodcastsShowResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['apple-podcasts-show-episodes'],
        params: ApplePodcastsShowEpisodesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ApplePodcastsShowEpisodesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-app'],
        params: AppStoreAppParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppStoreAppResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-developer'],
        params: AppStoreDeveloperParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppStoreDeveloperResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-list'],
        params: AppStoreListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppStoreListResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-privacy'],
        params: AppStorePrivacyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppStorePrivacyResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-ratings'],
        params: AppStoreRatingsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppStoreRatingsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-reviews'],
        params: AppStoreReviewsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppStoreReviewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-search'],
        params: AppStoreSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppStoreSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-similar'],
        params: AppStoreSimilarParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppStoreSimilarResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-suggest'],
        params: AppStoreSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppStoreSuggestResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-version-history'],
        params: AppStoreVersionHistoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppStoreVersionHistoryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['billing-me'],
        params: BillingMeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BillingMeResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['billing-me-checkout'],
        params: BillingMeCheckoutParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BillingMeCheckoutResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['billing-me-events'],
        params: BillingMeEventsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BillingMeEventsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['billing-me-periods'],
        params: BillingMePeriodsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BillingMePeriodsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['billing-me-period'],
        params: BillingMePeriodParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BillingMePeriodResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['billing-me-period-statement'],
        params: BillingMePeriodStatementParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BillingMePeriodStatementResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['billing-me-period-statement-download'],
        params: BillingMePeriodStatementDownloadParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BillingMePeriodStatementDownloadResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['billing-me-portal'],
        params: BillingMePortalParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BillingMePortalResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bing-images'],
        params: BingImagesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BingImagesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bing-news'],
        params: BingNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BingNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bing-search'],
        params: BingSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BingSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bing-suggest'],
        params: BingSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BingSuggestResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bing-videos'],
        params: BingVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BingVideosResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['brave-images'],
        params: BraveImagesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BraveImagesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['brave-news'],
        params: BraveNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BraveNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['brave-search'],
        params: BraveSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BraveSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['brave-suggest'],
        params: BraveSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BraveSuggestResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['brave-videos'],
        params: BraveVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BraveVideosResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['coingecko-categories'],
        params: CoinGeckoCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['coingecko-category-coins'],
        params: CoinGeckoCategoryCoinsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoCategoryCoinsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['coingecko-chains'],
        params: CoinGeckoChainsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoChainsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['coingecko-chain'],
        params: CoinGeckoChainParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoChainResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['coingecko-coin'],
        params: CoinGeckoCoinParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoCoinResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['coingecko-coin-analysis'],
        params: CoinGeckoCoinAnalysisParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoCoinAnalysisResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['coingecko-exchange'],
        params: CoinGeckoExchangeParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoExchangeResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['coingecko-exchanges'],
        params: CoinGeckoExchangesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoExchangesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['coingecko-gainers-losers'],
        params: CoinGeckoGainersLosersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoGainersLosersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['coingecko-global'],
        params: CoinGeckoGlobalParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoGlobalResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['coingecko-global-charts'],
        params: CoinGeckoGlobalChartsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoGlobalChartsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['coingecko-learn-articles'],
        params: CoinGeckoLearnArticlesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoLearnArticlesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['coingecko-markets'],
        params: CoinGeckoMarketsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoMarketsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['coingecko-new-coins'],
        params: CoinGeckoNewCoinsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoNewCoinsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['coingecko-news'],
        params: CoinGeckoNewsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['coingecko-nft-category'],
        params: CoinGeckoNftCategoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoNftCategoryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['coingecko-nfts'],
        params: CoinGeckoNftsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoNftsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['coingecko-search'],
        params: CoinGeckoSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['coingecko-token-unlocks'],
        params: CoinGeckoTokenUnlocksParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoTokenUnlocksResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['coingecko-treasuries'],
        params: CoinGeckoTreasuriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoTreasuriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['coingecko-trending'],
        params: CoinGeckoTrendingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoTrendingResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['datasets-list'],
        params: DatasetsListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DatasetsListResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['datasets-google-map-businesses-facets'],
        params: DatasetsGoogleMapBusinessesFacetsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DatasetsGoogleMapBusinessesFacetsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['datasets-google-map-businesses-item'],
        params: DatasetsGoogleMapBusinessesItemParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DatasetsGoogleMapBusinessesItemResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['datasets-google-map-businesses-nearby'],
        params: DatasetsGoogleMapBusinessesNearbyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DatasetsGoogleMapBusinessesNearbyResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['datasets-google-map-businesses-search'],
        params: DatasetsGoogleMapBusinessesSearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DatasetsGoogleMapBusinessesSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['ebay-item'],
        params: EBayEbayItemParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EBayEbayItemResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['ebay-search'],
        params: EBayEbaySearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EBayEbaySearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['ebay-seller'],
        params: EBayEbaySellerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EBayEbaySellerResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['ebay-seller-about'],
        params: EBayEbaySellerAboutParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EBayEbaySellerAboutResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['ebay-seller-feedback'],
        params: EBayEbaySellerFeedbackParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EBayEbaySellerFeedbackResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['ebay-seller-shop'],
        params: EBayEbaySellerShopParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EBayEbaySellerShopResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['geocoding-lookup'],
        params: GeocodingLookupParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GeocodingLookupResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['geocoding-reverse'],
        params: GeocodingReverseParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GeocodingReverseResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['geocoding-search'],
        params: GeocodingSearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GeocodingSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-analyst-articles'],
        params: GoogleFinanceAnalystArticlesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceAnalystArticlesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-chart'],
        params: GoogleFinanceChartParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceChartResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-classification'],
        params: GoogleFinanceClassificationParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceClassificationResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-company'],
        params: GoogleFinanceCompanyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceCompanyResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-context'],
        params: GoogleFinanceContextParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceContextResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-financials'],
        params: GoogleFinanceFinancialsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceFinancialsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-markets-category-news'],
        params: GoogleFinanceMarketsCategoryNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsCategoryNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-markets-category-stocks'],
        params: GoogleFinanceMarketsCategoryStocksParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsCategoryStocksResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-markets-earnings'],
        params: GoogleFinanceMarketsEarningsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsEarningsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-markets-featured'],
        params: GoogleFinanceMarketsFeaturedParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsFeaturedResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-markets-headline'],
        params: GoogleFinanceMarketsHeadlineParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsHeadlineResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-markets-indices'],
        params: GoogleFinanceMarketsIndicesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsIndicesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-markets-movers'],
        params: GoogleFinanceMarketsMoversParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsMoversResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-markets-top'],
        params: GoogleFinanceMarketsTopParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsTopResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-markets-trending'],
        params: GoogleFinanceMarketsTrendingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsTrendingResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-news'],
        params: GoogleFinanceNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-quote'],
        params: GoogleFinanceQuoteParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceQuoteResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-related'],
        params: GoogleFinanceRelatedParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceRelatedResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-search'],
        params: GoogleFinanceSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-ticker'],
        params: GoogleFinanceTickerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceTickerResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-jobs'],
        params: GoogleJobsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleJobsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-map-place'],
        params: GoogleMapPlaceParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleMapPlaceResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-map-search'],
        params: GoogleMapSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleMapSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-search'],
        params: GoogleSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-suggest'],
        params: GoogleSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleSuggestResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-trends-categories'],
        params: GoogleTrendsCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-trends-enums'],
        params: GoogleTrendsEnumsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsEnumsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-trends-explore'],
        params: GoogleTrendsExploreParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsExploreResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-trends-explore-interest-by-region'],
        params: GoogleTrendsExploreInterestByRegionParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsExploreInterestByRegionResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-trends-explore-interest-over-time'],
        params: GoogleTrendsExploreInterestOverTimeParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsExploreInterestOverTimeResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-trends-explore-related-topics'],
        params: GoogleTrendsExploreRelatedTopicsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsExploreRelatedTopicsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-trends-explore-rising-queries'],
        params: GoogleTrendsExploreRisingQueriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsExploreRisingQueriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-trends-explore-top-queries'],
        params: GoogleTrendsExploreTopQueriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsExploreTopQueriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-trends-locations'],
        params: GoogleTrendsLocationsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsLocationsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-trends-trending'],
        params: GoogleTrendsTrendingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsTrendingResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-trends-trending-detail'],
        params: GoogleTrendsTrendingDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsTrendingDetailResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['googleplay-app'],
        params: GooglePlayAppParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GooglePlayAppResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['googleplay-categories'],
        params: GooglePlayCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GooglePlayCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['googleplay-datasafety'],
        params: GooglePlayDatasafetyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GooglePlayDatasafetyResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['googleplay-developer'],
        params: GooglePlayDeveloperParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GooglePlayDeveloperResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['googleplay-list'],
        params: GooglePlayListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GooglePlayListResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['googleplay-permissions'],
        params: GooglePlayPermissionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GooglePlayPermissionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['googleplay-reviews'],
        params: GooglePlayReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GooglePlayReviewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['googleplay-search'],
        params: GooglePlaySearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GooglePlaySearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['googleplay-similar'],
        params: GooglePlaySimilarParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GooglePlaySimilarResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['googleplay-suggest'],
        params: GooglePlaySuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GooglePlaySuggestResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['instagram-post'],
        params: InstagramPostParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> InstagramPostResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['instagram-profile'],
        params: InstagramProfileParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> InstagramProfileResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['instagram-reels'],
        params: InstagramReelsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> InstagramReelsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['justwatch-age-certifications'],
        params: JustWatchJustwatchAgeCertificationsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchAgeCertificationsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['justwatch-discover'],
        params: JustWatchJustwatchDiscoverParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchDiscoverResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['justwatch-episode-by-id'],
        params: JustWatchJustwatchEpisodeByIdParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchEpisodeByIdResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['justwatch-episode-offers'],
        params: JustWatchJustwatchEpisodeOffersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchEpisodeOffersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['justwatch-genre-titles'],
        params: JustWatchJustwatchGenreTitlesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchGenreTitlesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['justwatch-genres'],
        params: JustWatchJustwatchGenresParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchGenresResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['justwatch-monetization-titles'],
        params: JustWatchJustwatchMonetizationTitlesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchMonetizationTitlesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['justwatch-new'],
        params: JustWatchJustwatchNewParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchNewResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['justwatch-popular'],
        params: JustWatchJustwatchPopularParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchPopularResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['justwatch-provider-titles'],
        params: JustWatchJustwatchProviderTitlesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchProviderTitlesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['justwatch-providers'],
        params: JustWatchJustwatchProvidersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchProvidersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['justwatch-search'],
        params: JustWatchJustwatchSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['justwatch-season-by-id'],
        params: JustWatchJustwatchSeasonByIdParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchSeasonByIdResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['justwatch-season-episodes'],
        params: JustWatchJustwatchSeasonEpisodesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchSeasonEpisodesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['justwatch-show-seasons'],
        params: JustWatchJustwatchShowSeasonsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchShowSeasonsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['justwatch-title'],
        params: JustWatchJustwatchTitleParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchTitleResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['justwatch-title-analysis'],
        params: JustWatchJustwatchTitleAnalysisParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchTitleAnalysisResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['justwatch-title-by-id'],
        params: JustWatchJustwatchTitleByIdParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchTitleByIdResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['justwatch-title-media'],
        params: JustWatchJustwatchTitleMediaParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchTitleMediaResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['justwatch-title-offers'],
        params: JustWatchJustwatchTitleOffersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchTitleOffersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['justwatch-title-similar'],
        params: JustWatchJustwatchTitleSimilarParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchTitleSimilarResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['linkedin-company'],
        params: LinkedInLinkedinCompanyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LinkedInLinkedinCompanyResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['linkedin-product'],
        params: LinkedInLinkedinProductParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LinkedInLinkedinProductResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['linkedin-showcase'],
        params: LinkedInLinkedinShowcaseParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LinkedInLinkedinShowcaseResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['ping'],
        params: MetaPingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> MetaPingResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['producthunt-category'],
        params: ProductHuntCategoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ProductHuntCategoryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['producthunt-category-products'],
        params: ProductHuntCategoryProductsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ProductHuntCategoryProductsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['producthunt-leaderboard'],
        params: ProductHuntLeaderboardParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ProductHuntLeaderboardResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['producthunt-product'],
        params: ProductHuntProductParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ProductHuntProductResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['producthunt-about'],
        params: ProductHuntAboutParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ProductHuntAboutResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['producthunt-alternatives'],
        params: ProductHuntAlternativesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ProductHuntAlternativesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['producthunt-customers'],
        params: ProductHuntCustomersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ProductHuntCustomersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['producthunt-launches'],
        params: ProductHuntLaunchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ProductHuntLaunchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['producthunt-makers'],
        params: ProductHuntMakersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ProductHuntMakersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['producthunt-reviews'],
        params: ProductHuntReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ProductHuntReviewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['producthunt-search'],
        params: ProductHuntSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ProductHuntSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['ready'],
        params: MetaReadyParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> MetaReadyResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['referrals-click'],
        params: ReferralsClickParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReferralsClickResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['referrals-me'],
        params: ReferralsMeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReferralsMeResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['referrals-me-events'],
        params: ReferralsMeEventsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReferralsMeEventsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shop-app-analysis'],
        params: ShopAppAnalysisParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppAnalysisResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shop-app-categories'],
        params: ShopAppCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shop-app-product'],
        params: ShopAppProductParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppProductResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shop-app-product-related'],
        params: ShopAppProductRelatedParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppProductRelatedResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shop-app-product-reviews'],
        params: ShopAppProductReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppProductReviewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shop-app-product-shop'],
        params: ShopAppProductShopParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppProductShopResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shop-app-product-variant'],
        params: ShopAppProductVariantParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppProductVariantResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shop-app-product-variants'],
        params: ShopAppProductVariantsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppProductVariantsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shop-app-search'],
        params: ShopAppSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shop-app-shop'],
        params: ShopAppShopParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppShopResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shop-app-collection-products'],
        params: ShopAppCollectionProductsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppCollectionProductsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shop-app-shop-locations'],
        params: ShopAppShopLocationsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppShopLocationsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shop-app-shop-products'],
        params: ShopAppShopProductsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppShopProductsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shop-app-shop-reviews'],
        params: ShopAppShopReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppShopReviewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shop-app-shop-typeahead'],
        params: ShopAppShopTypeaheadParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppShopTypeaheadResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shop-app-suggestions'],
        params: ShopAppSuggestionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppSuggestionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shopify-collections'],
        params: ShopifyCollectionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopifyCollectionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shopify-collection-products'],
        params: ShopifyCollectionProductsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopifyCollectionProductsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shopify-pages'],
        params: ShopifyPagesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopifyPagesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shopify-page'],
        params: ShopifyPageParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopifyPageResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shopify-products'],
        params: ShopifyProductsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopifyProductsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shopify-product'],
        params: ShopifyProductParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopifyProductResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shopify-product-recommendations'],
        params: ShopifyProductRecommendationsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopifyProductRecommendationsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shopify-search-suggest'],
        params: ShopifySearchSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopifySearchSuggestResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shopify-sitemap-urls'],
        params: ShopifySitemapUrlsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopifySitemapUrlsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shopify-sitemaps'],
        params: ShopifySitemapsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopifySitemapsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['shopify-store'],
        params: ShopifyStoreParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopifyStoreResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['similarweb-search'],
        params: SimilarWebSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SimilarWebSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['similarweb-web'],
        params: SimilarWebWebParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SimilarWebWebResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-podcasts-categories'],
        params: SpotifyPodcastsCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-podcasts-charts'],
        params: SpotifyPodcastsChartsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsChartsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-podcasts-episode'],
        params: SpotifyPodcastsEpisodeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsEpisodeResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-podcasts-home'],
        params: SpotifyPodcastsHomeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsHomeResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-podcasts-search'],
        params: SpotifyPodcastsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-podcasts-show'],
        params: SpotifyPodcastsShowParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsShowResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-podcasts-show-episodes'],
        params: SpotifyPodcastsShowEpisodesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsShowEpisodesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-podcasts-show-recommendations'],
        params: SpotifyPodcastsShowRecommendationsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsShowRecommendationsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-album'],
        params: SpotifyAlbumParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyAlbumResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-album-tracks'],
        params: SpotifyAlbumTracksParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyAlbumTracksResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-albums-search'],
        params: SpotifyAlbumsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyAlbumsSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-artist'],
        params: SpotifyArtistParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyArtistResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-artist-albums'],
        params: SpotifyArtistAlbumsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyArtistAlbumsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-artist-playlists'],
        params: SpotifyArtistPlaylistsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyArtistPlaylistsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-artist-related'],
        params: SpotifyArtistRelatedParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyArtistRelatedResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-artists-search'],
        params: SpotifyArtistsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyArtistsSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-audiobook'],
        params: SpotifyAudiobookParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyAudiobookResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-audiobook-chapters'],
        params: SpotifyAudiobookChaptersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyAudiobookChaptersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-audiobooks-search'],
        params: SpotifyAudiobooksSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyAudiobooksSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-chapter'],
        params: SpotifyChapterParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyChapterResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-episodes-search'],
        params: SpotifyEpisodesSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyEpisodesSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-featured-charts-by-country'],
        params: SpotifyFeaturedChartsByCountryParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyFeaturedChartsByCountryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-genre'],
        params: SpotifyGenreParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyGenreResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-home'],
        params: SpotifyHomeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyHomeResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-playlist'],
        params: SpotifyPlaylistParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPlaylistResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-playlists-search'],
        params: SpotifyPlaylistsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPlaylistsSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-popular-by-country'],
        params: SpotifyPopularByCountryParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPopularByCountryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-profile'],
        params: SpotifyProfileParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyProfileResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-profile-followers'],
        params: SpotifyProfileFollowersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyProfileFollowersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-profile-playlists'],
        params: SpotifyProfilePlaylistsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyProfilePlaylistsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-profiles-search'],
        params: SpotifyProfilesSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyProfilesSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-search'],
        params: SpotifySearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifySearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-section'],
        params: SpotifySectionParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifySectionResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-shows-search'],
        params: SpotifyShowsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyShowsSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-track'],
        params: SpotifyTrackParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyTrackResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-track-recommended'],
        params: SpotifyTrackRecommendedParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyTrackRecommendedResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-track-similar-albums'],
        params: SpotifyTrackSimilarAlbumsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyTrackSimilarAlbumsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-tracks-search'],
        params: SpotifyTracksSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyTracksSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-category'],
        params: TiktokCategoryParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokCategoryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-video-comments'],
        params: TiktokVideoCommentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokVideoCommentsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-explore'],
        params: TiktokExploreParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokExploreResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-challenge'],
        params: TiktokChallengeParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokChallengeResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-challenge-list'],
        params: TiktokChallengeListParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokChallengeListResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-popular-trend-country-industry-meta'],
        params: TiktokPopularTrendCountryIndustryMetaParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokPopularTrendCountryIndustryMetaResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-popular-trend-creator'],
        params: TiktokPopularTrendCreatorParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokPopularTrendCreatorResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-post'],
        params: TiktokPostParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokPostResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-profile-post'],
        params: TiktokProfilePostParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokProfilePostResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-profile'],
        params: TiktokProfileParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokProfileResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-search'],
        params: TiktokSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-search-hashtag'],
        params: TiktokSearchHashtagParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokSearchHashtagResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-search-user'],
        params: TiktokSearchUserParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokSearchUserResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-top-ads-analysis'],
        params: TiktokTopAdsAnalysisParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsAnalysisResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-top-ads-detail'],
        params: TiktokTopAdsDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsDetailResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-top-ads-filters'],
        params: TiktokTopAdsFiltersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsFiltersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-top-ads-list'],
        params: TiktokTopAdsListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsListResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-top-ads-location-info'],
        params: TiktokTopAdsLocationInfoParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsLocationInfoResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-top-ads-locations'],
        params: TiktokTopAdsLocationsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsLocationsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-top-ads-recommend'],
        params: TiktokTopAdsRecommendParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsRecommendResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-top-ads-safety'],
        params: TiktokTopAdsSafetyParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsSafetyResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-top-ads-spotlight'],
        params: TiktokTopAdsSpotlightParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsSpotlightResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-top-ads-suggestions'],
        params: TiktokTopAdsSuggestionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsSuggestionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-trending'],
        params: TiktokTrendingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTrendingResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tripadvisor-autocomplete'],
        params: TripAdvisorTripadvisorAutocompleteParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TripAdvisorTripadvisorAutocompleteResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tripadvisor-enums'],
        params: TripAdvisorTripadvisorEnumsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TripAdvisorTripadvisorEnumsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tripadvisor-hotels'],
        params: TripAdvisorTripadvisorHotelsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TripAdvisorTripadvisorHotelsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tripadvisor-place'],
        params: TripAdvisorTripadvisorPlaceParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TripAdvisorTripadvisorPlaceResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tripadvisor-reviews'],
        params: TripAdvisorTripadvisorReviewsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TripAdvisorTripadvisorReviewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tripadvisor-search'],
        params: TripAdvisorTripadvisorSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TripAdvisorTripadvisorSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['trustpilot-business-search'],
        params: TrustpilotBusinessSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TrustpilotBusinessSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['trustpilot-business'],
        params: TrustpilotBusinessParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TrustpilotBusinessResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['trustpilot-business-related'],
        params: TrustpilotBusinessRelatedParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TrustpilotBusinessRelatedResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['trustpilot-business-reviews'],
        params: TrustpilotBusinessReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TrustpilotBusinessReviewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['trustpilot-categories'],
        params: TrustpilotCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TrustpilotCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['trustpilot-category-search'],
        params: TrustpilotCategorySearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TrustpilotCategorySearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['trustpilot-category'],
        params: TrustpilotCategoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TrustpilotCategoryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['usage-me-endpoints'],
        params: UsageMeEndpointsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> UsageMeEndpointsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['usage-me-overview'],
        params: UsageMeOverviewParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> UsageMeOverviewResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['usage-me-recent-ips'],
        params: UsageMeRecentIpsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> UsageMeRecentIpsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['usage-me-timeseries'],
        params: UsageMeTimeseriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> UsageMeTimeseriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['user-me'],
        params: UserMeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> UserMeResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['user-me-api-keys'],
        params: UserMeApiKeysParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> UserMeApiKeysResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['user-me-api-keys-rotate'],
        params: UserMeApiKeysRotateParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> UserMeApiKeysRotateResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['user-me-api-keys-reveal'],
        params: UserMeApiKeysRevealParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> UserMeApiKeysRevealResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-calendars'],
        params: YahooFinanceCalendarsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceCalendarsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-calendar'],
        params: YahooFinanceCalendarParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceCalendarResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-download'],
        params: YahooFinanceDownloadParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceDownloadResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-industries'],
        params: YahooFinanceIndustriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceIndustriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-industry'],
        params: YahooFinanceIndustryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceIndustryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-market-status'],
        params: YahooFinanceMarketStatusParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceMarketStatusResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-market-summary'],
        params: YahooFinanceMarketSummaryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceMarketSummaryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-screener-custom'],
        params: YahooFinanceScreenerCustomParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceScreenerCustomResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-screener'],
        params: YahooFinanceScreenerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceScreenerResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-screeners'],
        params: YahooFinanceScreenersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceScreenersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-search'],
        params: YahooFinanceSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-sectors'],
        params: YahooFinanceSectorsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceSectorsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-sector'],
        params: YahooFinanceSectorParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceSectorResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-ticker-actions'],
        params: YahooFinanceTickerActionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerActionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-ticker-analysts'],
        params: YahooFinanceTickerAnalystsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerAnalystsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-ticker-calendar'],
        params: YahooFinanceTickerCalendarParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerCalendarResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-ticker-capital-gains'],
        params: YahooFinanceTickerCapitalGainsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerCapitalGainsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-ticker-dividends'],
        params: YahooFinanceTickerDividendsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerDividendsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-ticker-earnings'],
        params: YahooFinanceTickerEarningsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerEarningsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-ticker-earnings-dates'],
        params: YahooFinanceTickerEarningsDatesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerEarningsDatesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-ticker-financials'],
        params: YahooFinanceTickerFinancialsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerFinancialsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-ticker-funds'],
        params: YahooFinanceTickerFundsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerFundsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-ticker-history'],
        params: YahooFinanceTickerHistoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerHistoryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-ticker-history-metadata'],
        params: YahooFinanceTickerHistoryMetadataParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerHistoryMetadataResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-ticker-holders'],
        params: YahooFinanceTickerHoldersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerHoldersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-ticker-info'],
        params: YahooFinanceTickerInfoParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerInfoResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-ticker-isin'],
        params: YahooFinanceTickerIsinParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerIsinResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-ticker-news'],
        params: YahooFinanceTickerNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-ticker-options'],
        params: YahooFinanceTickerOptionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerOptionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-ticker-options-expiration'],
        params: YahooFinanceTickerOptionsExpirationParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerOptionsExpirationResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-ticker-quote'],
        params: YahooFinanceTickerQuoteParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerQuoteResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-ticker-sec-filings'],
        params: YahooFinanceTickerSecFilingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerSecFilingsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-ticker-shares'],
        params: YahooFinanceTickerSharesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerSharesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-ticker-shares-full'],
        params: YahooFinanceTickerSharesFullParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerSharesFullResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-ticker-splits'],
        params: YahooFinanceTickerSplitsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerSplitsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-ticker-sustainability'],
        params: YahooFinanceTickerSustainabilityParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerSustainabilityResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-ticker-valuation'],
        params: YahooFinanceTickerValuationParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerValuationResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['yahoo-finance-trending'],
        params: YahooFinanceTrendingParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTrendingResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['youtube-captions'],
        params: YoutubeCaptionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubeCaptionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['youtube-channel-playlists'],
        params: YoutubeChannelPlaylistsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubeChannelPlaylistsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['youtube-channel-search'],
        params: YoutubeChannelSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubeChannelSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['youtube-channel-shorts'],
        params: YoutubeChannelShortsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubeChannelShortsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['youtube-channel-videos'],
        params: YoutubeChannelVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubeChannelVideosResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['youtube-comments'],
        params: YoutubeCommentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubeCommentsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['youtube-playlist'],
        params: YoutubePlaylistParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubePlaylistResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['youtube-profile'],
        params: YoutubeProfileParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubeProfileResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['youtube-search'],
        params: YoutubeSearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubeSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['youtube-tag'],
        params: YoutubeTagParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubeTagResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['youtube-transcript'],
        params: YoutubeTranscriptParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubeTranscriptResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['youtube-transcript-languages'],
        params: YoutubeTranscriptLanguagesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubeTranscriptLanguagesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['youtube-video'],
        params: YoutubeVideoParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubeVideoResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['zillow-autocomplete'],
        params: ZillowAutocompleteParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ZillowAutocompleteResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['zillow-property'],
        params: ZillowPropertyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ZillowPropertyResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['zillow-search'],
        params: ZillowSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ZillowSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['airbnb-room'],
        params: AirbnbRoomParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AirbnbRoomResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['airbnb-room-calendar'],
        params: AirbnbRoomCalendarParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AirbnbRoomCalendarResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['airbnb-room-reviews'],
        params: AirbnbRoomReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AirbnbRoomReviewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['airbnb-search'],
        params: AirbnbSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AirbnbSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['amazon-product'],
        params: AmazonProductParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AmazonProductResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['amazon-search'],
        params: AmazonSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AmazonSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['amazon-suggest'],
        params: AmazonSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AmazonSuggestResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['apple-podcasts-charts'],
        params: ApplePodcastsChartsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ApplePodcastsChartsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['apple-podcasts-episodes-search'],
        params: ApplePodcastsEpisodesSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ApplePodcastsEpisodesSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['apple-podcasts-search'],
        params: ApplePodcastsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ApplePodcastsSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['apple-podcasts-show'],
        params: ApplePodcastsShowParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ApplePodcastsShowResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['apple-podcasts-show-episodes'],
        params: ApplePodcastsShowEpisodesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ApplePodcastsShowEpisodesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-app'],
        params: AppStoreAppParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppStoreAppResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-developer'],
        params: AppStoreDeveloperParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppStoreDeveloperResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-list'],
        params: AppStoreListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppStoreListResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-privacy'],
        params: AppStorePrivacyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppStorePrivacyResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-ratings'],
        params: AppStoreRatingsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppStoreRatingsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-reviews'],
        params: AppStoreReviewsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppStoreReviewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-search'],
        params: AppStoreSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppStoreSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-similar'],
        params: AppStoreSimilarParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppStoreSimilarResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-suggest'],
        params: AppStoreSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppStoreSuggestResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-version-history'],
        params: AppStoreVersionHistoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppStoreVersionHistoryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['billing-me'],
        params: BillingMeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BillingMeResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['billing-me-checkout'],
        params: BillingMeCheckoutParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BillingMeCheckoutResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['billing-me-events'],
        params: BillingMeEventsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BillingMeEventsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['billing-me-periods'],
        params: BillingMePeriodsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BillingMePeriodsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['billing-me-period'],
        params: BillingMePeriodParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BillingMePeriodResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['billing-me-period-statement'],
        params: BillingMePeriodStatementParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BillingMePeriodStatementResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['billing-me-period-statement-download'],
        params: BillingMePeriodStatementDownloadParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BillingMePeriodStatementDownloadResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['billing-me-portal'],
        params: BillingMePortalParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BillingMePortalResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bing-images'],
        params: BingImagesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BingImagesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bing-news'],
        params: BingNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BingNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bing-search'],
        params: BingSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BingSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bing-suggest'],
        params: BingSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BingSuggestResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bing-videos'],
        params: BingVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BingVideosResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['brave-images'],
        params: BraveImagesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BraveImagesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['brave-news'],
        params: BraveNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BraveNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['brave-search'],
        params: BraveSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BraveSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['brave-suggest'],
        params: BraveSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BraveSuggestResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['brave-videos'],
        params: BraveVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BraveVideosResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['coingecko-categories'],
        params: CoinGeckoCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['coingecko-category-coins'],
        params: CoinGeckoCategoryCoinsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoCategoryCoinsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['coingecko-chains'],
        params: CoinGeckoChainsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoChainsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['coingecko-chain'],
        params: CoinGeckoChainParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoChainResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['coingecko-coin'],
        params: CoinGeckoCoinParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoCoinResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['coingecko-coin-analysis'],
        params: CoinGeckoCoinAnalysisParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoCoinAnalysisResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['coingecko-exchange'],
        params: CoinGeckoExchangeParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoExchangeResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['coingecko-exchanges'],
        params: CoinGeckoExchangesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoExchangesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['coingecko-gainers-losers'],
        params: CoinGeckoGainersLosersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoGainersLosersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['coingecko-global'],
        params: CoinGeckoGlobalParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoGlobalResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['coingecko-global-charts'],
        params: CoinGeckoGlobalChartsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoGlobalChartsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['coingecko-learn-articles'],
        params: CoinGeckoLearnArticlesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoLearnArticlesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['coingecko-markets'],
        params: CoinGeckoMarketsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoMarketsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['coingecko-new-coins'],
        params: CoinGeckoNewCoinsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoNewCoinsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['coingecko-news'],
        params: CoinGeckoNewsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['coingecko-nft-category'],
        params: CoinGeckoNftCategoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoNftCategoryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['coingecko-nfts'],
        params: CoinGeckoNftsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoNftsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['coingecko-search'],
        params: CoinGeckoSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['coingecko-token-unlocks'],
        params: CoinGeckoTokenUnlocksParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoTokenUnlocksResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['coingecko-treasuries'],
        params: CoinGeckoTreasuriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoTreasuriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['coingecko-trending'],
        params: CoinGeckoTrendingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CoinGeckoTrendingResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['datasets-list'],
        params: DatasetsListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DatasetsListResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['datasets-google-map-businesses-facets'],
        params: DatasetsGoogleMapBusinessesFacetsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DatasetsGoogleMapBusinessesFacetsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['datasets-google-map-businesses-item'],
        params: DatasetsGoogleMapBusinessesItemParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DatasetsGoogleMapBusinessesItemResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['datasets-google-map-businesses-nearby'],
        params: DatasetsGoogleMapBusinessesNearbyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DatasetsGoogleMapBusinessesNearbyResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['datasets-google-map-businesses-search'],
        params: DatasetsGoogleMapBusinessesSearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DatasetsGoogleMapBusinessesSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['ebay-item'],
        params: EBayEbayItemParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EBayEbayItemResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['ebay-search'],
        params: EBayEbaySearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EBayEbaySearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['ebay-seller'],
        params: EBayEbaySellerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EBayEbaySellerResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['ebay-seller-about'],
        params: EBayEbaySellerAboutParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EBayEbaySellerAboutResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['ebay-seller-feedback'],
        params: EBayEbaySellerFeedbackParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EBayEbaySellerFeedbackResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['ebay-seller-shop'],
        params: EBayEbaySellerShopParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> EBayEbaySellerShopResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['geocoding-lookup'],
        params: GeocodingLookupParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GeocodingLookupResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['geocoding-reverse'],
        params: GeocodingReverseParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GeocodingReverseResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['geocoding-search'],
        params: GeocodingSearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GeocodingSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-analyst-articles'],
        params: GoogleFinanceAnalystArticlesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceAnalystArticlesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-chart'],
        params: GoogleFinanceChartParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceChartResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-classification'],
        params: GoogleFinanceClassificationParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceClassificationResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-company'],
        params: GoogleFinanceCompanyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceCompanyResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-context'],
        params: GoogleFinanceContextParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceContextResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-financials'],
        params: GoogleFinanceFinancialsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceFinancialsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-markets-category-news'],
        params: GoogleFinanceMarketsCategoryNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsCategoryNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-markets-category-stocks'],
        params: GoogleFinanceMarketsCategoryStocksParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsCategoryStocksResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-markets-earnings'],
        params: GoogleFinanceMarketsEarningsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsEarningsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-markets-featured'],
        params: GoogleFinanceMarketsFeaturedParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsFeaturedResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-markets-headline'],
        params: GoogleFinanceMarketsHeadlineParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsHeadlineResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-markets-indices'],
        params: GoogleFinanceMarketsIndicesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsIndicesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-markets-movers'],
        params: GoogleFinanceMarketsMoversParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsMoversResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-markets-top'],
        params: GoogleFinanceMarketsTopParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsTopResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-markets-trending'],
        params: GoogleFinanceMarketsTrendingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsTrendingResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-news'],
        params: GoogleFinanceNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-quote'],
        params: GoogleFinanceQuoteParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceQuoteResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-related'],
        params: GoogleFinanceRelatedParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceRelatedResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-search'],
        params: GoogleFinanceSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-ticker'],
        params: GoogleFinanceTickerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceTickerResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-jobs'],
        params: GoogleJobsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleJobsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-map-place'],
        params: GoogleMapPlaceParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleMapPlaceResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-map-search'],
        params: GoogleMapSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleMapSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-search'],
        params: GoogleSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-suggest'],
        params: GoogleSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleSuggestResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-trends-categories'],
        params: GoogleTrendsCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-trends-enums'],
        params: GoogleTrendsEnumsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsEnumsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-trends-explore'],
        params: GoogleTrendsExploreParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsExploreResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-trends-explore-interest-by-region'],
        params: GoogleTrendsExploreInterestByRegionParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsExploreInterestByRegionResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-trends-explore-interest-over-time'],
        params: GoogleTrendsExploreInterestOverTimeParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsExploreInterestOverTimeResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-trends-explore-related-topics'],
        params: GoogleTrendsExploreRelatedTopicsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsExploreRelatedTopicsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-trends-explore-rising-queries'],
        params: GoogleTrendsExploreRisingQueriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsExploreRisingQueriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-trends-explore-top-queries'],
        params: GoogleTrendsExploreTopQueriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsExploreTopQueriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-trends-locations'],
        params: GoogleTrendsLocationsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsLocationsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-trends-trending'],
        params: GoogleTrendsTrendingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsTrendingResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-trends-trending-detail'],
        params: GoogleTrendsTrendingDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsTrendingDetailResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['googleplay-app'],
        params: GooglePlayAppParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GooglePlayAppResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['googleplay-categories'],
        params: GooglePlayCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GooglePlayCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['googleplay-datasafety'],
        params: GooglePlayDatasafetyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GooglePlayDatasafetyResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['googleplay-developer'],
        params: GooglePlayDeveloperParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GooglePlayDeveloperResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['googleplay-list'],
        params: GooglePlayListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GooglePlayListResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['googleplay-permissions'],
        params: GooglePlayPermissionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GooglePlayPermissionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['googleplay-reviews'],
        params: GooglePlayReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GooglePlayReviewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['googleplay-search'],
        params: GooglePlaySearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GooglePlaySearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['googleplay-similar'],
        params: GooglePlaySimilarParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GooglePlaySimilarResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['googleplay-suggest'],
        params: GooglePlaySuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GooglePlaySuggestResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['instagram-post'],
        params: InstagramPostParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> InstagramPostResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['instagram-profile'],
        params: InstagramProfileParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> InstagramProfileResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['instagram-reels'],
        params: InstagramReelsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> InstagramReelsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['justwatch-age-certifications'],
        params: JustWatchJustwatchAgeCertificationsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchAgeCertificationsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['justwatch-discover'],
        params: JustWatchJustwatchDiscoverParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchDiscoverResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['justwatch-episode-by-id'],
        params: JustWatchJustwatchEpisodeByIdParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchEpisodeByIdResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['justwatch-episode-offers'],
        params: JustWatchJustwatchEpisodeOffersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchEpisodeOffersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['justwatch-genre-titles'],
        params: JustWatchJustwatchGenreTitlesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchGenreTitlesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['justwatch-genres'],
        params: JustWatchJustwatchGenresParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchGenresResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['justwatch-monetization-titles'],
        params: JustWatchJustwatchMonetizationTitlesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchMonetizationTitlesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['justwatch-new'],
        params: JustWatchJustwatchNewParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchNewResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['justwatch-popular'],
        params: JustWatchJustwatchPopularParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchPopularResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['justwatch-provider-titles'],
        params: JustWatchJustwatchProviderTitlesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchProviderTitlesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['justwatch-providers'],
        params: JustWatchJustwatchProvidersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchProvidersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['justwatch-search'],
        params: JustWatchJustwatchSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['justwatch-season-by-id'],
        params: JustWatchJustwatchSeasonByIdParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchSeasonByIdResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['justwatch-season-episodes'],
        params: JustWatchJustwatchSeasonEpisodesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchSeasonEpisodesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['justwatch-show-seasons'],
        params: JustWatchJustwatchShowSeasonsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchShowSeasonsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['justwatch-title'],
        params: JustWatchJustwatchTitleParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchTitleResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['justwatch-title-analysis'],
        params: JustWatchJustwatchTitleAnalysisParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchTitleAnalysisResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['justwatch-title-by-id'],
        params: JustWatchJustwatchTitleByIdParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchTitleByIdResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['justwatch-title-media'],
        params: JustWatchJustwatchTitleMediaParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchTitleMediaResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['justwatch-title-offers'],
        params: JustWatchJustwatchTitleOffersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchTitleOffersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['justwatch-title-similar'],
        params: JustWatchJustwatchTitleSimilarParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> JustWatchJustwatchTitleSimilarResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['linkedin-company'],
        params: LinkedInLinkedinCompanyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LinkedInLinkedinCompanyResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['linkedin-product'],
        params: LinkedInLinkedinProductParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LinkedInLinkedinProductResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['linkedin-showcase'],
        params: LinkedInLinkedinShowcaseParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LinkedInLinkedinShowcaseResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['ping'],
        params: MetaPingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> MetaPingResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['producthunt-category'],
        params: ProductHuntCategoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ProductHuntCategoryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['producthunt-category-products'],
        params: ProductHuntCategoryProductsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ProductHuntCategoryProductsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['producthunt-leaderboard'],
        params: ProductHuntLeaderboardParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ProductHuntLeaderboardResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['producthunt-product'],
        params: ProductHuntProductParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ProductHuntProductResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['producthunt-about'],
        params: ProductHuntAboutParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ProductHuntAboutResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['producthunt-alternatives'],
        params: ProductHuntAlternativesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ProductHuntAlternativesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['producthunt-customers'],
        params: ProductHuntCustomersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ProductHuntCustomersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['producthunt-launches'],
        params: ProductHuntLaunchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ProductHuntLaunchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['producthunt-makers'],
        params: ProductHuntMakersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ProductHuntMakersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['producthunt-reviews'],
        params: ProductHuntReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ProductHuntReviewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['producthunt-search'],
        params: ProductHuntSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ProductHuntSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['ready'],
        params: MetaReadyParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> MetaReadyResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['referrals-click'],
        params: ReferralsClickParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReferralsClickResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['referrals-me'],
        params: ReferralsMeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReferralsMeResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['referrals-me-events'],
        params: ReferralsMeEventsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReferralsMeEventsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shop-app-analysis'],
        params: ShopAppAnalysisParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppAnalysisResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shop-app-categories'],
        params: ShopAppCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shop-app-product'],
        params: ShopAppProductParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppProductResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shop-app-product-related'],
        params: ShopAppProductRelatedParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppProductRelatedResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shop-app-product-reviews'],
        params: ShopAppProductReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppProductReviewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shop-app-product-shop'],
        params: ShopAppProductShopParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppProductShopResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shop-app-product-variant'],
        params: ShopAppProductVariantParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppProductVariantResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shop-app-product-variants'],
        params: ShopAppProductVariantsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppProductVariantsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shop-app-search'],
        params: ShopAppSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shop-app-shop'],
        params: ShopAppShopParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppShopResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shop-app-collection-products'],
        params: ShopAppCollectionProductsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppCollectionProductsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shop-app-shop-locations'],
        params: ShopAppShopLocationsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppShopLocationsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shop-app-shop-products'],
        params: ShopAppShopProductsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppShopProductsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shop-app-shop-reviews'],
        params: ShopAppShopReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppShopReviewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shop-app-shop-typeahead'],
        params: ShopAppShopTypeaheadParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppShopTypeaheadResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shop-app-suggestions'],
        params: ShopAppSuggestionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopAppSuggestionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shopify-collections'],
        params: ShopifyCollectionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopifyCollectionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shopify-collection-products'],
        params: ShopifyCollectionProductsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopifyCollectionProductsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shopify-pages'],
        params: ShopifyPagesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopifyPagesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shopify-page'],
        params: ShopifyPageParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopifyPageResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shopify-products'],
        params: ShopifyProductsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopifyProductsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shopify-product'],
        params: ShopifyProductParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopifyProductResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shopify-product-recommendations'],
        params: ShopifyProductRecommendationsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopifyProductRecommendationsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shopify-search-suggest'],
        params: ShopifySearchSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopifySearchSuggestResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shopify-sitemap-urls'],
        params: ShopifySitemapUrlsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopifySitemapUrlsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shopify-sitemaps'],
        params: ShopifySitemapsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopifySitemapsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['shopify-store'],
        params: ShopifyStoreParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ShopifyStoreResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['similarweb-search'],
        params: SimilarWebSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SimilarWebSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['similarweb-web'],
        params: SimilarWebWebParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SimilarWebWebResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-podcasts-categories'],
        params: SpotifyPodcastsCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-podcasts-charts'],
        params: SpotifyPodcastsChartsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsChartsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-podcasts-episode'],
        params: SpotifyPodcastsEpisodeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsEpisodeResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-podcasts-home'],
        params: SpotifyPodcastsHomeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsHomeResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-podcasts-search'],
        params: SpotifyPodcastsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-podcasts-show'],
        params: SpotifyPodcastsShowParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsShowResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-podcasts-show-episodes'],
        params: SpotifyPodcastsShowEpisodesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsShowEpisodesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-podcasts-show-recommendations'],
        params: SpotifyPodcastsShowRecommendationsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsShowRecommendationsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-album'],
        params: SpotifyAlbumParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyAlbumResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-album-tracks'],
        params: SpotifyAlbumTracksParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyAlbumTracksResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-albums-search'],
        params: SpotifyAlbumsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyAlbumsSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-artist'],
        params: SpotifyArtistParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyArtistResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-artist-albums'],
        params: SpotifyArtistAlbumsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyArtistAlbumsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-artist-playlists'],
        params: SpotifyArtistPlaylistsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyArtistPlaylistsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-artist-related'],
        params: SpotifyArtistRelatedParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyArtistRelatedResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-artists-search'],
        params: SpotifyArtistsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyArtistsSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-audiobook'],
        params: SpotifyAudiobookParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyAudiobookResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-audiobook-chapters'],
        params: SpotifyAudiobookChaptersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyAudiobookChaptersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-audiobooks-search'],
        params: SpotifyAudiobooksSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyAudiobooksSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-chapter'],
        params: SpotifyChapterParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyChapterResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-episodes-search'],
        params: SpotifyEpisodesSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyEpisodesSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-featured-charts-by-country'],
        params: SpotifyFeaturedChartsByCountryParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyFeaturedChartsByCountryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-genre'],
        params: SpotifyGenreParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyGenreResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-home'],
        params: SpotifyHomeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyHomeResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-playlist'],
        params: SpotifyPlaylistParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPlaylistResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-playlists-search'],
        params: SpotifyPlaylistsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPlaylistsSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-popular-by-country'],
        params: SpotifyPopularByCountryParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPopularByCountryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-profile'],
        params: SpotifyProfileParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyProfileResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-profile-followers'],
        params: SpotifyProfileFollowersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyProfileFollowersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-profile-playlists'],
        params: SpotifyProfilePlaylistsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyProfilePlaylistsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-profiles-search'],
        params: SpotifyProfilesSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyProfilesSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-search'],
        params: SpotifySearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifySearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-section'],
        params: SpotifySectionParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifySectionResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-shows-search'],
        params: SpotifyShowsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyShowsSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-track'],
        params: SpotifyTrackParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyTrackResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-track-recommended'],
        params: SpotifyTrackRecommendedParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyTrackRecommendedResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-track-similar-albums'],
        params: SpotifyTrackSimilarAlbumsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyTrackSimilarAlbumsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-tracks-search'],
        params: SpotifyTracksSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyTracksSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-category'],
        params: TiktokCategoryParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokCategoryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-video-comments'],
        params: TiktokVideoCommentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokVideoCommentsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-explore'],
        params: TiktokExploreParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokExploreResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-challenge'],
        params: TiktokChallengeParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokChallengeResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-challenge-list'],
        params: TiktokChallengeListParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokChallengeListResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-popular-trend-country-industry-meta'],
        params: TiktokPopularTrendCountryIndustryMetaParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokPopularTrendCountryIndustryMetaResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-popular-trend-creator'],
        params: TiktokPopularTrendCreatorParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokPopularTrendCreatorResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-post'],
        params: TiktokPostParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokPostResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-profile-post'],
        params: TiktokProfilePostParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokProfilePostResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-profile'],
        params: TiktokProfileParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokProfileResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-search'],
        params: TiktokSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-search-hashtag'],
        params: TiktokSearchHashtagParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokSearchHashtagResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-search-user'],
        params: TiktokSearchUserParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokSearchUserResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-top-ads-analysis'],
        params: TiktokTopAdsAnalysisParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsAnalysisResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-top-ads-detail'],
        params: TiktokTopAdsDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsDetailResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-top-ads-filters'],
        params: TiktokTopAdsFiltersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsFiltersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-top-ads-list'],
        params: TiktokTopAdsListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsListResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-top-ads-location-info'],
        params: TiktokTopAdsLocationInfoParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsLocationInfoResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-top-ads-locations'],
        params: TiktokTopAdsLocationsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsLocationsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-top-ads-recommend'],
        params: TiktokTopAdsRecommendParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsRecommendResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-top-ads-safety'],
        params: TiktokTopAdsSafetyParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsSafetyResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-top-ads-spotlight'],
        params: TiktokTopAdsSpotlightParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsSpotlightResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-top-ads-suggestions'],
        params: TiktokTopAdsSuggestionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsSuggestionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-trending'],
        params: TiktokTrendingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTrendingResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tripadvisor-autocomplete'],
        params: TripAdvisorTripadvisorAutocompleteParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TripAdvisorTripadvisorAutocompleteResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tripadvisor-enums'],
        params: TripAdvisorTripadvisorEnumsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TripAdvisorTripadvisorEnumsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tripadvisor-hotels'],
        params: TripAdvisorTripadvisorHotelsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TripAdvisorTripadvisorHotelsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tripadvisor-place'],
        params: TripAdvisorTripadvisorPlaceParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TripAdvisorTripadvisorPlaceResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tripadvisor-reviews'],
        params: TripAdvisorTripadvisorReviewsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TripAdvisorTripadvisorReviewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tripadvisor-search'],
        params: TripAdvisorTripadvisorSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TripAdvisorTripadvisorSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['trustpilot-business-search'],
        params: TrustpilotBusinessSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TrustpilotBusinessSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['trustpilot-business'],
        params: TrustpilotBusinessParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TrustpilotBusinessResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['trustpilot-business-related'],
        params: TrustpilotBusinessRelatedParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TrustpilotBusinessRelatedResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['trustpilot-business-reviews'],
        params: TrustpilotBusinessReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TrustpilotBusinessReviewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['trustpilot-categories'],
        params: TrustpilotCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TrustpilotCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['trustpilot-category-search'],
        params: TrustpilotCategorySearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TrustpilotCategorySearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['trustpilot-category'],
        params: TrustpilotCategoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TrustpilotCategoryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['usage-me-endpoints'],
        params: UsageMeEndpointsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> UsageMeEndpointsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['usage-me-overview'],
        params: UsageMeOverviewParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> UsageMeOverviewResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['usage-me-recent-ips'],
        params: UsageMeRecentIpsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> UsageMeRecentIpsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['usage-me-timeseries'],
        params: UsageMeTimeseriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> UsageMeTimeseriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['user-me'],
        params: UserMeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> UserMeResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['user-me-api-keys'],
        params: UserMeApiKeysParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> UserMeApiKeysResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['user-me-api-keys-rotate'],
        params: UserMeApiKeysRotateParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> UserMeApiKeysRotateResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['user-me-api-keys-reveal'],
        params: UserMeApiKeysRevealParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> UserMeApiKeysRevealResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-calendars'],
        params: YahooFinanceCalendarsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceCalendarsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-calendar'],
        params: YahooFinanceCalendarParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceCalendarResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-download'],
        params: YahooFinanceDownloadParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceDownloadResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-industries'],
        params: YahooFinanceIndustriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceIndustriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-industry'],
        params: YahooFinanceIndustryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceIndustryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-market-status'],
        params: YahooFinanceMarketStatusParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceMarketStatusResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-market-summary'],
        params: YahooFinanceMarketSummaryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceMarketSummaryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-screener-custom'],
        params: YahooFinanceScreenerCustomParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceScreenerCustomResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-screener'],
        params: YahooFinanceScreenerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceScreenerResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-screeners'],
        params: YahooFinanceScreenersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceScreenersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-search'],
        params: YahooFinanceSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-sectors'],
        params: YahooFinanceSectorsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceSectorsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-sector'],
        params: YahooFinanceSectorParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceSectorResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-ticker-actions'],
        params: YahooFinanceTickerActionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerActionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-ticker-analysts'],
        params: YahooFinanceTickerAnalystsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerAnalystsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-ticker-calendar'],
        params: YahooFinanceTickerCalendarParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerCalendarResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-ticker-capital-gains'],
        params: YahooFinanceTickerCapitalGainsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerCapitalGainsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-ticker-dividends'],
        params: YahooFinanceTickerDividendsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerDividendsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-ticker-earnings'],
        params: YahooFinanceTickerEarningsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerEarningsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-ticker-earnings-dates'],
        params: YahooFinanceTickerEarningsDatesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerEarningsDatesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-ticker-financials'],
        params: YahooFinanceTickerFinancialsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerFinancialsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-ticker-funds'],
        params: YahooFinanceTickerFundsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerFundsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-ticker-history'],
        params: YahooFinanceTickerHistoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerHistoryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-ticker-history-metadata'],
        params: YahooFinanceTickerHistoryMetadataParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerHistoryMetadataResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-ticker-holders'],
        params: YahooFinanceTickerHoldersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerHoldersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-ticker-info'],
        params: YahooFinanceTickerInfoParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerInfoResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-ticker-isin'],
        params: YahooFinanceTickerIsinParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerIsinResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-ticker-news'],
        params: YahooFinanceTickerNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-ticker-options'],
        params: YahooFinanceTickerOptionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerOptionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-ticker-options-expiration'],
        params: YahooFinanceTickerOptionsExpirationParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerOptionsExpirationResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-ticker-quote'],
        params: YahooFinanceTickerQuoteParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerQuoteResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-ticker-sec-filings'],
        params: YahooFinanceTickerSecFilingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerSecFilingsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-ticker-shares'],
        params: YahooFinanceTickerSharesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerSharesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-ticker-shares-full'],
        params: YahooFinanceTickerSharesFullParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerSharesFullResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-ticker-splits'],
        params: YahooFinanceTickerSplitsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerSplitsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-ticker-sustainability'],
        params: YahooFinanceTickerSustainabilityParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerSustainabilityResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-ticker-valuation'],
        params: YahooFinanceTickerValuationParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTickerValuationResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['yahoo-finance-trending'],
        params: YahooFinanceTrendingParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YahooFinanceTrendingResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['youtube-captions'],
        params: YoutubeCaptionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubeCaptionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['youtube-channel-playlists'],
        params: YoutubeChannelPlaylistsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubeChannelPlaylistsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['youtube-channel-search'],
        params: YoutubeChannelSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubeChannelSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['youtube-channel-shorts'],
        params: YoutubeChannelShortsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubeChannelShortsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['youtube-channel-videos'],
        params: YoutubeChannelVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubeChannelVideosResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['youtube-comments'],
        params: YoutubeCommentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubeCommentsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['youtube-playlist'],
        params: YoutubePlaylistParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubePlaylistResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['youtube-profile'],
        params: YoutubeProfileParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubeProfileResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['youtube-search'],
        params: YoutubeSearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubeSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['youtube-tag'],
        params: YoutubeTagParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubeTagResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['youtube-transcript'],
        params: YoutubeTranscriptParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubeTranscriptResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['youtube-transcript-languages'],
        params: YoutubeTranscriptLanguagesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubeTranscriptLanguagesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['youtube-video'],
        params: YoutubeVideoParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> YoutubeVideoResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['zillow-autocomplete'],
        params: ZillowAutocompleteParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ZillowAutocompleteResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['zillow-property'],
        params: ZillowPropertyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ZillowPropertyResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['zillow-search'],
        params: ZillowSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ZillowSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

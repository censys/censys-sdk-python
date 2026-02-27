import os
import time
from datetime import date, datetime, timedelta, timezone

import pytest

from censys_platform import SDK, models


# ---------------------------------------------------------------------------
# Test fixtures
# ---------------------------------------------------------------------------

CERT_IDS = [
    "00000002741c89f06524afbbb4720876bc173aca3a6ce344e08584859b9ac34e",
    "000000033b547e13ee216c65b0ff50237f0decef12acb76fce0a96afa9c70d50",
]
HOST_IDS = ["1.1.1.1", "8.8.8.8"]
WEB_PROPERTY_IDS = ["104.236.29.250:443", "78.133.74.135:49152"]
COLLECTION_QUERY = (
    "host.services.protocol='SSH' and host.location.country = 'Netherlands'"
    " and host.services.port = 9100"
    " and host.autonomous_system.name = 'WORLDSTREAM'"
)


@pytest.fixture(autouse=True)
def delay_between_tests():
    yield
    time.sleep(2)


@pytest.fixture
def sdk_client():
    api_key = os.getenv("CENSYS_PAT")
    org_id = os.getenv("CENSYS_ORG_ID")
    assert api_key, "CENSYS_PAT environment variable must be set"
    assert org_id, "CENSYS_ORG_ID environment variable must be set"
    return SDK(personal_access_token=api_key, organization_id=org_id)


@pytest.fixture
def org_id():
    val = os.getenv("CENSYS_ORG_ID")
    assert val
    return val


def _thirty_days_ago() -> date:
    return (datetime.now(timezone.utc) - timedelta(days=30)).date()


# ---------------------------------------------------------------------------
# GlobalData — Certificates
# ---------------------------------------------------------------------------


class TestGlobalData_Certificates:
    def test_get_certificates(self, sdk_client):
        with sdk_client as s:
            res = s.global_data.get_certificates(
                asset_certificate_list_input_body={"certificate_ids": CERT_IDS}
            )
            assert res is not None

    def test_get_certificates_raw(self, sdk_client):
        with sdk_client as s:
            res = s.global_data.get_certificates_raw(
                asset_certificate_list_input_body={"certificate_ids": CERT_IDS}
            )
            assert res is not None

    def test_get_certificate(self, sdk_client):
        with sdk_client as s:
            res = s.global_data.get_certificate(certificate_id=CERT_IDS[0])
            assert res is not None

    def test_get_certificate_raw(self, sdk_client):
        with sdk_client as s:
            res = s.global_data.get_certificate_raw(certificate_id=CERT_IDS[0])
            assert res is not None


# ---------------------------------------------------------------------------
# GlobalData — Hosts
# ---------------------------------------------------------------------------


class TestGlobalData_Hosts:
    def test_get_hosts(self, sdk_client):
        with sdk_client as s:
            res = s.global_data.get_hosts(
                asset_host_list_input_body={"host_ids": HOST_IDS}
            )
            assert res is not None

    def test_get_host(self, sdk_client):
        with sdk_client as s:
            res = s.global_data.get_host(host_id="108.137.3.85")
            assert res is not None

    def test_get_host_timeline(self, sdk_client):
        with sdk_client as s:
            res = s.global_data.get_host_timeline(
                host_id="125.13.31.107",
                start_time=datetime(2025, 3, 20, tzinfo=timezone.utc),
                end_time=datetime(2025, 3, 22, tzinfo=timezone.utc),
            )
            assert res is not None


# ---------------------------------------------------------------------------
# GlobalData — Web Properties
# ---------------------------------------------------------------------------


class TestGlobalData_WebProperties:
    def test_get_web_properties(self, sdk_client):
        with sdk_client as s:
            res = s.global_data.get_web_properties(
                asset_webproperty_list_input_body={
                    "webproperty_ids": WEB_PROPERTY_IDS
                }
            )
            assert res is not None

    def test_get_web_property(self, sdk_client):
        with sdk_client as s:
            res = s.global_data.get_web_property(
                webproperty_id=WEB_PROPERTY_IDS[0]
            )
            assert res is not None


# ---------------------------------------------------------------------------
# GlobalData — Search
# ---------------------------------------------------------------------------


class TestGlobalData_Search:
    def test_search(self, sdk_client):
        with sdk_client as s:
            res = s.global_data.search(
                search_query_input_body={
                    "query": "web.port: *",
                    "page_size": 3,
                    "fields": ["web.port"],
                }
            )
            assert res is not None

    def test_aggregate(self, sdk_client):
        with sdk_client as s:
            res = s.global_data.aggregate(
                search_aggregate_input_body={
                    "field": "web.endpoints.http.status_reason",
                    "number_of_buckets": 2,
                    "query": "web.port: *",
                }
            )
            assert res is not None

    def test_convert_legacy_search_queries(self, sdk_client):
        with sdk_client as s:
            res = s.global_data.convert_legacy_search_queries(
                search_convert_query_input_body={
                    "queries": ["parsed.names: censys.io"]
                }
            )
            assert res is not None


# ---------------------------------------------------------------------------
# GlobalData — Tracked Scans
# ---------------------------------------------------------------------------


class TestGlobalData_TrackedScans:
    def test_create_and_get_tracked_scan(self, sdk_client):
        with sdk_client as s:
            try:
                create_res = s.global_data.create_tracked_scan(
                    scans_rescan_input_body={
                        "target": {
                            "service_id": {
                                "ip": "1.1.1.1",
                                "port": 80,
                                "protocol": "HTTP",
                                "transport_protocol": "tcp",
                            }
                        }
                    }
                )
            except models.SDKError as e:
                if e.status_code == 429:
                    pytest.skip("Rate limited (429)")
                raise
            assert create_res is not None
            scan_id = create_res.result.result.tracked_scan_id
            assert scan_id is not None

            get_res = s.global_data.get_tracked_scan(scan_id=scan_id)
            assert get_res is not None


# ---------------------------------------------------------------------------
# Collections — Full CRUD + Search
# ---------------------------------------------------------------------------


class TestCollections:
    def test_list(self, sdk_client):
        with sdk_client as s:
            res = s.collections.list(page_size=2)
            assert res is not None

    def test_crud(self, sdk_client):
        with sdk_client as s:
            create_res = s.collections.create(
                crud_create_input_body={
                    "name": "SDK Smoke Test Collection",
                    "description": "Created by Python SDK smoke tests",
                    "query": COLLECTION_QUERY,
                }
            )
            assert create_res is not None
            collection_uid = create_res.result.result.id
            assert collection_uid is not None

            try:
                # Get
                get_res = s.collections.get(collection_uid=collection_uid)
                assert get_res is not None

                # Update
                update_res = s.collections.update(
                    collection_uid=collection_uid,
                    crud_update_input_body={
                        "name": "Updated SDK Smoke Test",
                        "description": "Updated description",
                        "query": COLLECTION_QUERY,
                    },
                )
                assert update_res is not None
                get_res = s.collections.get(collection_uid=collection_uid)
                assert get_res.result.result.description == "Updated description"

                # ListEvents
                events_res = s.collections.list_events(
                    request={"collection_uid": collection_uid}
                )
                assert events_res is not None

                # Aggregate
                agg_res = s.collections.aggregate(
                    collection_uid=collection_uid,
                    search_aggregate_input_body={
                        "field": "host.autonomous_system.name",
                        "number_of_buckets": 10,
                        "query": "host.services.labels.value = 'REMOTE_ACCESS'",
                    },
                )
                assert agg_res is not None

                # Search
                search_res = s.collections.search(
                    collection_uid=collection_uid,
                    search_query_input_body={
                        "query": "host.services.labels.value = 'REMOTE_ACCESS'"
                    },
                )
                assert search_res is not None

            finally:
                # Delete
                delete_res = s.collections.delete(collection_uid=collection_uid)
                assert delete_res is not None

                with pytest.raises(Exception):
                    s.collections.get(collection_uid=collection_uid)


# ---------------------------------------------------------------------------
# Account Management — Organization
# ---------------------------------------------------------------------------


class TestAccountManagement_Organization:
    def test_get_organization_details(self, sdk_client, org_id):
        with sdk_client as s:
            res = s.account_management.get_organization_details(
                organization_id=org_id, include_member_counts=True
            )
            assert res is not None

    def test_get_organization_credits(self, sdk_client, org_id):
        with sdk_client as s:
            res = s.account_management.get_organization_credits(
                organization_id=org_id
            )
            assert res is not None

    def test_get_organization_credit_usage(self, sdk_client, org_id):
        with sdk_client as s:
            res = s.account_management.get_organization_credit_usage(
                request={
                    "organization_id": org_id,
                    "start_date": _thirty_days_ago(),
                    "granularity": "daily",
                }
            )
            assert res is not None


# ---------------------------------------------------------------------------
# Account Management — Members
# ---------------------------------------------------------------------------


class TestAccountManagement_Members:
    def test_list_organization_members(self, sdk_client, org_id):
        with sdk_client as s:
            res = s.account_management.list_organization_members(
                organization_id=org_id, page_size=5
            )
            assert res is not None

    def test_get_member_credit_usage(self, sdk_client, org_id):
        with sdk_client as s:
            members_res = s.account_management.list_organization_members(
                organization_id=org_id
            )
            members = members_res.result.result.members
            assert len(members) > 0

            res = s.account_management.get_member_credit_usage(
                request={
                    "organization_id": org_id,
                    "user_id": members[0].uid,
                    "start_date": _thirty_days_ago(),
                    "granularity": "daily",
                }
            )
            assert res is not None


# ---------------------------------------------------------------------------
# Account Management — User (self)
# ---------------------------------------------------------------------------


class TestAccountManagement_User:
    def test_get_user_credits(self, sdk_client):
        with sdk_client as s:
            res = s.account_management.get_user_credits()
            assert res is not None

    def test_get_user_credits_usage(self, sdk_client):
        with sdk_client as s:
            res = s.account_management.get_user_credits_usage(
                start_date=_thirty_days_ago(),
                granularity="daily",
            )
            assert res is not None


# ---------------------------------------------------------------------------
# Threat Hunting
# ---------------------------------------------------------------------------


class TestThreatHunting:
    def test_value_counts(self, sdk_client):
        with sdk_client as s:
            res = s.threat_hunting.value_counts(
                search_value_counts_input_body={
                    "and_count_conditions": [
                        {
                            "field_value_pairs": [
                                {"field": "host.services.port", "value": "80"}
                            ]
                        }
                    ]
                }
            )
            assert res is not None

    def test_get_host_observations_with_certificate(self, sdk_client):
        with sdk_client as s:
            res = s.threat_hunting.get_host_observations_with_certificate(
                request={"certificate_id": CERT_IDS[0]}
            )
            assert res is not None

    def test_list_threats(self, sdk_client):
        with sdk_client as s:
            res = s.threat_hunting.list_threats()
            assert res is not None

    def test_create_and_get_tracked_scan(self, sdk_client):
        with sdk_client as s:
            try:
                create_res = s.threat_hunting.create_tracked_scan(
                    scans_discovery_input_body={
                        "target": {"host_port": {"ip": "1.1.1.1", "port": 443}}
                    }
                )
            except models.SDKError as e:
                if e.status_code == 429:
                    pytest.skip("Rate limited (429)")
                raise
            assert create_res is not None
            scan_id = create_res.result.result.tracked_scan_id
            assert scan_id is not None

            get_res = s.threat_hunting.get_tracked_scan_threat_hunting(
                scan_id=scan_id
            )
            assert get_res is not None

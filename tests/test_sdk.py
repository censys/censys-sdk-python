import os
import pytest
from datetime import datetime, timezone

from censys_platform import SDK, models


@pytest.fixture
def sdk_client():
    """Initialize SDK client with environment variables."""
    api_key = os.getenv("CENSYS_PAT")
    org_id = os.getenv("CENSYS_ORG_ID")
    
    assert api_key, "CENSYS_PAT environment variable must be set"
    assert org_id, "CENSYS_ORG_ID environment variable must be set"
    
    return SDK(
        personal_access_token=api_key,
        organization_id=org_id
    )

class TestGlobalData:
    """Test suite for Global Data functionality."""

    def test_certificate(self, sdk_client):
        """Test getting a single certificate."""
        with sdk_client as platform:
            cert_id = "00000002741c89f06524afbbb4720876bc173aca3a6ce344e08584859b9ac34e"
            res = platform.global_data.get_certificate(certificate_id=cert_id)
            assert res is not None
            assert res.result is not None

    def test_certificates_list(self, sdk_client):
        """Test getting multiple certificates."""
        with sdk_client as platform:
            cert_ids = [
                "00000002741c89f06524afbbb4720876bc173aca3a6ce344e08584859b9ac34e",
                "000000033b547e13ee216c65b0ff50237f0decef12acb76fce0a96afa9c70d50"
            ]
            res = platform.global_data.get_certificates(
                asset_certificate_list_input_body={
                    "certificate_ids": cert_ids
                }
            )
            assert res is not None
            assert res.result is not None

    def test_certificates_list_raw(self, sdk_client):
        """Test getting multiple certificates in raw format."""
        with sdk_client as platform:
            cert_ids = [
                "00000002741c89f06524afbbb4720876bc173aca3a6ce344e08584859b9ac34e",
                "000000033b547e13ee216c65b0ff50237f0decef12acb76fce0a96afa9c70d50"
            ]
            res = platform.global_data.get_certificates_raw(
                asset_certificate_list_input_body={
                    "certificate_ids": cert_ids
                }
            )
            assert res is not None
            assert res.result is not None

    def test_certificate_raw(self, sdk_client):
        """Test getting a single certificate in raw format."""
        with sdk_client as platform:
            cert_id = "00000002741c89f06524afbbb4720876bc173aca3a6ce344e08584859b9ac34e"
            res = platform.global_data.get_certificate_raw(certificate_id=cert_id)
            assert res is not None
            assert res.result is not None

    def test_host_list(self, sdk_client):
        """Test getting multiple hosts."""
        with sdk_client as platform:
            host_ids = ["1.1.1.1", "8.8.8.8"]
            res = platform.global_data.get_hosts(
                asset_host_list_input_body={
                    "host_ids": host_ids
                }
            )
            assert res is not None
            assert res.result is not None

    def test_host(self, sdk_client):
        """Test getting a single host."""
        with sdk_client as platform:
            res = platform.global_data.get_host(host_id="108.137.3.85")
            assert res is not None
            assert res.result is not None
            assert res.result.result is not None
            assert res.result.result.resource is not None

    def test_host_timeline(self, sdk_client):
        """Test getting host timeline."""
        with sdk_client as platform:
            host_id = "125.13.31.107"
            start_time = "2025-03-20T00:00:00Z"
            end_time = "2025-03-22T00:00:00Z"
            res = platform.global_data.get_host_timeline(
                host_id=host_id,
                start_time=start_time,
                end_time=end_time
            )
            assert res is not None
            assert res.result is not None

    def test_web_property(self, sdk_client):
        """Test getting a single web property."""
        with sdk_client as platform:
            web_property_id = "104.236.29.250:443"
            res = platform.global_data.get_web_property(webproperty_id=web_property_id)
            assert res is not None
            assert res.result is not None

    def test_web_properties_list(self, sdk_client):
        """Test getting multiple web properties."""
        with sdk_client as platform:
            web_property_ids = [
                "104.236.29.250:443",
                "78.133.74.135:49152"
            ]
            res = platform.global_data.get_web_properties(
                asset_webproperty_list_input_body={
                    "webproperty_ids": web_property_ids
                }
            )
            assert res is not None
            assert res.result is not None

    def test_search_aggregate(self, sdk_client):
        """Test search aggregate functionality."""
        with sdk_client as platform:
            res = platform.global_data.aggregate(
                search_aggregate_input_body={
                    "field": "web.endpoints.http.status_reason",
                    "number_of_buckets": 2,
                    "query": "web.port: *"
                }
            )
            assert res is not None
            assert res.result is not None

    def test_search_query(self, sdk_client):
        """Test search query functionality."""
        with sdk_client as platform:
            res = platform.global_data.search(
                search_query_input_body={
                    "query": "web.port: *",
                    "page_size": 3,
                    "fields": ["web.port"]
                }
            )
            assert res is not None
            assert res.result is not None
            assert res.result.result is not None
            assert res.result.result.hits is not None
            assert len(res.result.result.hits) <= 3

    def test_search_query_with_pagination(self, sdk_client):
        """Test search query with pagination."""
        with sdk_client as platform:
            page_token = ""
            hits = []
            
            for _ in range(3):
                res = platform.global_data.search(
                    search_query_input_body=models.SearchQueryInputBody(
                        query="web.port: *",
                        page_size=3,
                        fields=["web.port"],
                        page_token=page_token
                    )
                )
                assert res is not None
                assert res.result is not None
                assert res.result.result is not None
                assert res.result.result.hits is not None
                
                hits.extend(res.result.result.hits)
                page_token = res.result.result.next_page_token
                
                if not page_token:
                    break
            
            assert len(hits) > 0


class TestCollections:
    """Test suite for Collections functionality."""

    def test_collections_crud(self, sdk_client):
        """Test full CRUD operations on collections."""
        with sdk_client as platform:
            # Create collection
            create_res = platform.collections.create(
                crud_create_input_body={
                    "name": "Test Collection NL",
                    "description": "Test Collection NL",
                    "query": "host.services.protocol='SSH' and host.location.country = 'Netherlands' and host.services.port = 9100 and host.autonomous_system.name = 'WORLDSTREAM'"
                }
            )
            assert create_res is not None
            assert create_res.result is not None
            assert create_res.result.result is not None
            
            collection_uid = create_res.result.result.id
            assert collection_uid is not None

            try:
                # Get collection
                get_res = platform.collections.get(collection_uid=collection_uid)
                assert get_res is not None
                assert get_res.result is not None

                # List events
                list_events_res = platform.collections.list_events(request={"collection_uid": collection_uid})
                assert list_events_res is not None

                # Search aggregate
                search_aggregate_res = platform.collections.aggregate(
                    search_aggregate_input_body={
                        "field": "host.autonomous_system.name",
                        "number_of_buckets": 10,
                        "query": "host.services.labels.value = 'REMOTE_ACCESS'"
                    },
                    collection_uid=collection_uid
                )
                assert search_aggregate_res is not None

                # Search query
                search_query_res = platform.collections.search(
                    search_query_input_body={
                        "query": "host.services.labels.value = 'REMOTE_ACCESS'"
                    },
                    collection_uid=collection_uid
                )
                assert search_query_res is not None

                # Update collection
                update_res = platform.collections.update(
                    crud_update_input_body={
                        "description": "New desc",
                        "name": "New name",
                        "query": "host.services.protocol='SSH' and host.location.country = 'Netherlands' and host.services.port = 9100 and host.autonomous_system.name = 'WORLDSTREAM'"
                    },
                    collection_uid=collection_uid
                )
                assert update_res is not None

                # Verify update
                get_res = platform.collections.get(collection_uid=collection_uid)
                assert get_res.result.result.description == "New desc"

            finally:
                # Clean up - delete collection
                delete_res = platform.collections.delete(collection_uid=collection_uid)
                assert delete_res is not None

                # Verify deletion
                with pytest.raises(Exception):
                    platform.collections.get(collection_uid=collection_uid)


class TestThreatHunting:
    """Test suite for Threat Hunting functionality."""

    def test_value_counts(self, sdk_client):
        """Test threat hunting value counts."""
        with sdk_client as platform:
            res = platform.threat_hunting.value_counts(
                search_value_counts_input_body={
                    "and_count_conditions": [
                        {
                            "field_value_pairs": [
                                {
                                    "field": "host.services.port",
                                    "value": "80"
                                }
                            ]
                        }
                    ]
                }
            )
            assert res is not None
            assert res.result is not None 
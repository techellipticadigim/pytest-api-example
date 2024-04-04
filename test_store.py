from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_
import  string
import random
'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''

@pytest.fixture
def unique_order_data():
    test_endpoint = "/store/order"
    params = {
        "pet_id": 0
    }
    response = api_helpers.post_api_data(test_endpoint, params)
    order_id = response.json()["id"]
    return {
        "order_id": str(order_id),
        "pet_id": 0,
        "quantity": 1,
        "status": "placed"
    }

def test_patch_order_by_id(unique_order_data):
    order_id = unique_order_data["order_id"]
    test_endpoint = f"/store/order/{order_id}"
    response = api_helpers.patch_api_data(test_endpoint, {"status": "pending"})
    assert response.status_code == 200
    assert response.json()["message"] == "Order and pet status updated successfully"
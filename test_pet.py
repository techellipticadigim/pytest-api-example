from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Troubleshooting and fixing the test failure
The purpose of this test is to validate the response matches the expected schema defined in schemas.py
'''
@pytest.mark.parametrize("id, status", [("0","available"), ("1","pending"), ("2","available")])
def test_pet_schema(id,status):
    test_endpoint = f"/pets/{id}"
    response = api_helpers.get_api_data(test_endpoint)
    assert response.status_code == 200
    validate(instance=response.json(), schema=schemas.pet)

'''
TODO: Finish this test by...
1) Extending the parameterization to include all available statuses
2) Validate the appropriate response code
3) Validate the 'status' property in the response is equal to the expected status
4) Validate the schema for each object in the response
'''
@pytest.mark.parametrize("status,expected_status_code", [("available",200), ("pending",200)])
def test_find_by_status_200(status, expected_status_code):
    test_endpoint = "/pets/findByStatus"
    params = {
        "status": status
    }

    response = api_helpers.get_api_data(test_endpoint, params)
    assert response.status_code == expected_status_code
    assert response.json()[0]['status'] == status

    # TODO...

'''
TODO: Finish this test by...
1) Testing and validating the appropriate 404 response for /pets/{pet_id}
2) Parameterizing the test for any edge cases
'''
@pytest.mark.parametrize("invalid_id", [63738,-1,"xyz", None])
def test_get_by_id_404(invalid_id):
    test_endpoint = f"/pets/{invalid_id}"
    response = api_helpers.get_api_data(test_endpoint)
    assert response.status_code == 404

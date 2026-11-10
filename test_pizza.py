import pytest


# A vegetarian request returns a pizza with vegetarian ingredients only.
def test_vegetarian_pizza(api, auth):
    res = api.post("/api/pizza", json={"mustBeVegetarian": True}, headers=auth)
    assert res.status_code == 200
    pizza = res.json()["pizza"]
    assert pizza["name"]
    for ingredient in pizza["ingredients"]:
        assert ingredient["vegetarian"] is True, ingredient["name"]


# A pizza request without a token is refused with an authentication error.
def test_pizza_without_token_is_refused(api):
    res = api.post("/api/pizza", json={"mustBeVegetarian": True})
    assert res.status_code == 401
    assert res.json() == {"error": "authentication failed"}


# Excluding all tools exposes the documented server defect.
@pytest.mark.xfail(reason="Defect 1: excluding all tools returns 500 with an empty body; expected 400 with a JSON error", strict=True)
def test_excluding_all_tools_returns_client_error(api, auth):
    res = api.post("/api/pizza", json={"excludedTools": ["Knife", "Pizza cutter", "Scissors"]}, headers=auth)
    assert res.status_code == 400
    assert res.json()

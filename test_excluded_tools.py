import pytest


# The pizza never needs an excluded tool when at least one tool remains available.
@pytest.mark.parametrize("excluded", [["Knife"], ["Scissors"], []])
def test_excluded_tool_is_not_used(api, auth, excluded):
    res = api.post("/api/pizza", json={"excludedTools": excluded}, headers=auth)
    assert res.status_code == 200
    assert res.json()["pizza"]["tool"] not in excluded

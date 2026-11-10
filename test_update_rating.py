import pytest


# Boundary values are saved or refused, and a refused update leaves stars unchanged.
@pytest.mark.parametrize("stars, status", [(0, 400), (1, 200), (5, 200), (6, 400)])
def test_update_rating_boundaries(api, auth, rating, stars, status):
    path = f"/api/ratings/{rating['id']}"
    res = api.put(path, json={"stars": stars}, headers=auth)
    assert res.status_code == status
    current = api.get(path, headers=auth)
    assert current.status_code == 200
    assert current.json()["stars"] == (stars if status == 200 else 3)

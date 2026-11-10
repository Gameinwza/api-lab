# Another user cannot read the rating, and the owner still can.
def test_other_user_cannot_read_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.get(path, headers=other_auth)
    assert 400 <= res.status_code < 500
    owner_view = api.get(path, headers=auth)
    assert owner_view.status_code == 200
    assert owner_view.json() == rating


# Another user cannot change the rating, and the owner still sees its original value.
def test_other_user_cannot_change_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.put(path, json={"stars": 1}, headers=other_auth)
    assert 400 <= res.status_code < 500
    owner_view = api.get(path, headers=auth)
    assert owner_view.status_code == 200
    assert owner_view.json() == rating


# Another user cannot delete the rating, and the owner can still read it.
def test_other_user_cannot_delete_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.delete(path, headers=other_auth)
    assert 400 <= res.status_code < 500
    owner_view = api.get(path, headers=auth)
    assert owner_view.status_code == 200
    assert owner_view.json() == rating

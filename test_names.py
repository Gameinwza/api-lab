# The pizza name list answers 200 and includes a known name.
def test_names_are_listed(api):
    res = api.get("/api/names")
    assert res.status_code == 200
    assert "Margherita" in res.json()["names"]

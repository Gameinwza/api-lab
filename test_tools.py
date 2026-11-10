# The tools endpoint requires authentication and lists all three tools.
def test_tools_are_listed(api):
    res = api.get("/api/tools", headers={"Authorization": "token abcdef0123456789"})
    assert res.status_code == 200
    assert res.json() == {"tools": ["Knife", "Pizza cutter", "Scissors"]}


# The tools endpoint refuses requests without a token.
def test_tools_without_token_are_refused(api):
    res = api.get("/api/tools")
    assert res.status_code == 401
    assert res.json() == {"error": "authentication failed"}

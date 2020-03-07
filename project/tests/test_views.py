def test_homepage(client):
    response = client.get("/")
    assert b"My TODO List" in response.data

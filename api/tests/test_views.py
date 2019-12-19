async def test_healthz(app_client):
    resp = await app_client.get('/healthz')
    assert resp.status == 200
    text = await resp.text()
    assert text == 'OK'


async def test_index(app_client):
    resp = await app_client.get('/')
    assert resp.status == 200

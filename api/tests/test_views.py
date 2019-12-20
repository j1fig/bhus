async def test_healthz(app_client):
    resp = await app_client.get('/healthz')
    assert resp.status == 200
    json = await resp.json()
    assert json['status'] == 'OK'


async def test_index(app_client):
    resp = await app_client.get('/')
    assert resp.status == 200


async def test_operators(app_client):
    resp = await app_client.get('/api/operator')
    assert resp.status == 200


async def test_operator_vehicles(app_client):
    operator_id = 'MEH'
    resp = await app_client.get(f'/api/operator/{operator_id}/vehicle')
    assert resp.status == 200


async def test_vehicles(app_client):
    resp = await app_client.get('/api/vehicle')
    assert resp.status == 200


async def test_vehicle(app_client):
    vehicle_id = 98234
    resp = await app_client.get(f'/api/vehicle/{vehicle_id}')
    assert resp.status == 200

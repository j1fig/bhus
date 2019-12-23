import pytest


def test_as_dict(monkeypatch):
    monkeypatch.setenv('DB_DSN', 'postgres://some:pass@host/db')
    from bhus import config
    expected_dict = {
        'db_dsn': 'postgres://some:pass@host/db'
    }
    assert config.as_dict() == expected_dict

import pytest

from bhus import config


def test_as_dict(monkeypatch):
    monkeypatch.setenv('DB_DSN', 'postgres://some:pass@host/db')
    expected_dict = {
        'db_dsn': 'postgres://some:pass@host/db'
    }
    assert config.as_dict() == expected_dict

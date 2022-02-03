from recipes import create_app


def test_config():
    """
    If config is not passed, there should be a default configuraton.
    Otherwise, the configuration should be overridden.
    """
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing
import pytest
from data.fake_users import usuarios
from data.fake_cultivos import cultivos


# ============================================
# FIXTURES GLOBALES
# ============================================

@pytest.fixture
def db_users():
    return usuarios


@pytest.fixture
def db_cultivos():
    return cultivos
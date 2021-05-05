# костиль
import sys
import os
sys.path.append(os.getcwd())


import pytest

from app import db, create_app
import models
from db_methods import delete_all_course
from config import TestConfiguration


@pytest.fixture(scope='module', autouse=True)
def test_client():
    """Description."""
    app = create_app(TestConfiguration)
    with app.app_context():
        db.create_all()
        delete_all_course()
    # -----------------------------------------------------------------------------
    # Create a test client using the Flask application configured for testing
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client

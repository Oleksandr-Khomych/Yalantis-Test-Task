# -*- coding: utf-8 -*-

from catalog_api.app import db, create_app
import catalog_api.models
from catalog_api.config import ProdConfiguration


if __name__ == '__main__':
    app = create_app(ProdConfiguration)
    with app.app_context():
        db.create_all()
    app.run()

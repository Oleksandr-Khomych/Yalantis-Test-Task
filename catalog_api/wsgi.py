# -*- coding: utf-8 -*-

from app import db, create_app
import models
from config import ProdConfiguration


if __name__ == '__main__':
    app = create_app(ProdConfiguration)
    with app.app_context():
        db.create_all()
    app.run()

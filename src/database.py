from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def get_or_create(model, **kwargs):
    query = db.select(model).filter_by(**kwargs)
    model_object = db.session.execute(query).first()
    if model_object:
        # TODO ADD LOGGER
        return model_object
    else:
        model_object = model(**kwargs)
        db.session.add(model_object)
        db.session.commit()
        # TODO ADD LOGGER

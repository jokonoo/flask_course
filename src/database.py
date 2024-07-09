from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def get_or_create(model, **kwargs):
    created = True
    query = db.select(model).filter_by(name=kwargs["name"])
    model_object = db.session.scalars(query).first()
    if model_object:
        created = False
        # TODO ADD LOGGER
    else:
        if "id" in kwargs:
            del kwargs["id"]
        model_object = model(**kwargs)
        db.session.add(model_object)
        db.session.commit()
        # TODO ADD LOGGER
    return model_object, created


def get_first(model, **kwargs):
    query = db.select(model).filter_by(**kwargs)
    model_object = db.session.scalars(query).first()
    return model_object

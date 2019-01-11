from app import db
from datetime import datetime

class BaseMixin(object):
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    __repr__hide = ['created_at','updated_at']

    @classmethod
    def query(cls):
        return db.session.query(cls).all()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get(cls,id):
        return cls.query.get(id)

    @classmethod
    def get_by(cls,**kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def get_or_404(cls,id):
        instance_found = cls.get(id)
        if instance_found is None:
            abort(404)
        return instance_found

    @classmethod
    def get_or_create(cls,**kwargs):
        instance = cls.get_by(**kwargs)
        if not instance:
            instance = cls(**kwargs)
            db.session.add(r)
        return instance

    @classmethod
    def create(cls, commit=True,**kwargs):
        instance = cls(**kwargs)
        return instance.save(commit=commit)
        
    def save(self,commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)

    def filter_string(self):
        return self.__str__()

    def __repr__(self):
        values = ', '.join("%s=%r" % (n, getattr(self, n)) for n in self.__table__.c.keys() if n not in self._repr_hide)
        return "%s(%s)" % (self.__class__.__name__, values)



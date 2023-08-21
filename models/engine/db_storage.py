from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from os import getenv

class DBStorage:
    __engine = None
    __session = None
    
    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        from models import classes  # Import inside the function to avoid circular imports
        session = self.__session
        
        objects = {}
        if cls:
            if type(cls) == str:
                cls = classes.get(cls, None)
            if cls:
                query_result = session.query(cls).all()
                for obj in query_result:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objects[key] = obj
        else:
            for name, _cls in classes.items():
                query_result = session.query(_cls).all()
                for obj in query_result:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objects[key] = obj
        
        return objects
    
    def new(self, obj):
        if obj:
            self.__session.add(obj)
    
    def save(self):
        self.__session.commit()
    
    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        from models.base_model import Base
        
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

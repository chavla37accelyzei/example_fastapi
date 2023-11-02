from app.db.database import Base,engine

from app.model.user_model import User

from app.model.location_model import Location
from app.model.orgs_model import Org
from app.model.role_model import Role


Base.metadata.create_all(engine)





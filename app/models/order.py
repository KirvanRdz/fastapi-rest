from sqlalchemy import Column, Integer, String, ForeignKey

from app.db.session import Base


# Modelo SQLAlchemy para la base de datos
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_name = Column(String, index=True)
    quantity = Column(Integer)

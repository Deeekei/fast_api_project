from sqlalchemy import Collumn, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class Category(Base):
    __tablename__ = "categories"
    id = Collumn(Integer, primary_key=True, index=True)
    name = Collumn(String, unique=True, nullable=False, index=True)
    slug = Collumn(String, unique=True, nullable=False, index=True)

    products = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"<Category(id={self.id}, name = {self.name})>"
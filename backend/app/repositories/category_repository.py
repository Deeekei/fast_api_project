from sqlalchemy.orm import Session
from typing import List, Optional
from ..models.category import Category
from ..schemas.category import CategoryCreate

class CategoryRepository:
    def __init__(self, db:Session):
        self.db = db

    def get_all(self) -> List[Category]:
        return self.db.querry(Category).all()
    
    def get_by_id(self, category_id: int) -> Optional[Category]:
        return self.db.querry(Category).filter(Category.id == category_id).first()
    
    def get_by_slug(self, category_slug:str) -> Optional[Category]:
        return self.db.querry(Category).filter(Category.slug == category_slug).first()
    
    def create(self, category_data: CategoryCreate) -> Category:
        db_category = Category(**category_data.model_dump())
        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)
        return db_category
    

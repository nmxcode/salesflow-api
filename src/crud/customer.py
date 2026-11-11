from sqlalchemy.orm import Session
from src.models.customer import Customer
from src.schemas.customer import CustomerCreate, CustomerUpdate


def get_customer(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.id == customer_id).first()


def get_customers(db: Session, skip: int = 0, limit: int = 100, search: str = None):
    query = db.query(Customer)
    if search:
        query = query.filter(Customer.name.ilike(f"%{search}%"))
    return query.offset(skip).limit(limit).all()


def create_customer(db: Session, customer: CustomerCreate):
    db_customer = Customer(name=customer.name, email=customer.email)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def update_customer(db: Session, customer_id: int, customer: CustomerUpdate):
    db_customer = get_customer(db, customer_id)
    if not db_customer:
        return None
    update_data = customer.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_customer, key, value)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def delete_customer(db: Session, customer_id: int):
    db_customer = get_customer(db, customer_id)
    if not db_customer:
        return None
    db.delete(db_customer)
    db.commit()
    return db_customer
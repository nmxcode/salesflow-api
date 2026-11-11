from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from src.database import get_db
from src.schemas.customer import CustomerCreate, CustomerResponse, CustomerUpdate
from src.crud import customer as crud_customer

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.get("/", response_model=list[CustomerResponse])
def read_customers(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    search: str | None = None,
    db: Session = Depends(get_db),
):
    return crud_customer.get_customers(db, skip=skip, limit=limit, search=search)


@router.get("/{customer_id}", response_model=CustomerResponse)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud_customer.get_customer(db, customer_id)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer


@router.post("/", response_model=CustomerResponse, status_code=201)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return crud_customer.create_customer(db, customer)


@router.put("/{customer_id}", response_model=CustomerResponse)
def update_customer(
    customer_id: int, customer: CustomerUpdate, db: Session = Depends(get_db)
):
    db_customer = crud_customer.update_customer(db, customer_id, customer)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer


@router.delete("/{customer_id}", status_code=204)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud_customer.delete_customer(db, customer_id)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return None
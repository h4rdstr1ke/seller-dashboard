from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db.database import get_db
from app.models.seller import Seller
from app.schemas.seller import SellerCreate
from app.core.security import get_password_hash

router = APIRouter(prefix="/api/v1/auth", tags=["Auth"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_seller(seller_in: SellerCreate, db: AsyncSession = Depends(get_db)):

    query = select(Seller).where(Seller.email == seller_in.email)
    result = await db.execute(query)
    if result.scalars().first():

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Продавец с таким email уже зарегистрирован"
        )

    new_seller = Seller(
        email=seller_in.email,
        hashed_password=get_password_hash(seller_in.password),
        first_name=seller_in.first_name,
        last_name=seller_in.last_name,
        middle_name=seller_in.middle_name,
        company_name=seller_in.company_name,
        inn=seller_in.inn,
        phone=seller_in.phone
    )

    db.add(new_seller)
    await db.commit()          
    await db.refresh(new_seller) 
# заглушка токена TODO: JWT
    return {
        "user_id": str(new_seller.id),
        "access_token": "dummy_access_token_will_be_here",
        "refresh_token": "dummy_refresh_token_will_be_here",
        "token_type": "Bearer",
        "expires_in": 3600
    }
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src.config import settings

# ۱. ساخت Engine (موتور اتصال به دیتابیس)
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,  # اگه DEBUG=True باشه، کوئری‌های SQL توی ترمینال چاپ می‌شن
    pool_pre_ping=True,   # قبل از هر کوئری، سلامت اتصال رو چک می‌کنه
)

# ۲. ساخت Session Factory (کارخانه ساخت جلسه)
SessionLocal = sessionmaker(
    autocommit=False,  # ما خودمون دستی commit می‌کنیم
    autoflush=False,   # ما خودمون دستی flush می‌کنیم
    bind=engine,
)

# ۳. کلاس پایه برای مدل‌ها
Base = declarative_base()


# ۴. وابستگی (Dependency) برای FastAPI
def get_db():
    """
    این تابع به هر درخواست یه Session می‌ده و بعد از تموم شدن کار،
    حتی اگه خطا بیاد، Session رو می‌بنده.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
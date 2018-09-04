from sqlalchemy import Column, Integer, String, SmallInteger

from app.models.base import Base

from app.libs.pendingEnum import PendingStatus

class Drift(Base):
    id = Column(Integer, primary_key=True)
    _pending = Column('pending', SmallInteger, default=1)

    #邮寄信息
    recipient_name = Column(String(20), nullable=False) #可以为空，否
    address = Column(String(100), nullable=False)
    message = Column(String(200))
    mobile = Column(String(20), nullable=False)

    #书籍信息
    isbn = Column(String(13))
    book_title = Column(String(50))
    book_author = Column(String(30))
    book_img = Column(String(50))

    #请求者信息
    request_id = Column(Integer, nullable=False)
    recipient_name = Column(String(30))

    #赠送者信息
    gift_id = Column(Integer, nullable=False)
    gifter_id = Column(Integer,nullable=False)
    gifter_nickname = Column(String(30))

    @property
    def penging(self):
        return self._pending
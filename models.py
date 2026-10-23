from database import Base
from sqlalchemy import String , Column,Integer,Text,ForeignKey,DateTime,func
from sqlalchemy.orm import relationship



class User(Base):
    __table_name__= 'users'

    id = Column(Integer , primary_key=True, index=True)
    username = Column(String(50),unique=True , index= True ,nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    password_hash =Column(String(255), nullable=False)
    created_at = Column(DateTime,server_default=func.now())

    posts = relationship('Post', back_populates='author', cascade='all , delete-orphan')
    comments  = relationship('Comment', back_populates='author',cascade='all , delete-orphan')
    likes = relationship('Like',back_populates='user',cascade='all , delete-orphan')



class Post(Base):
    __table_name__ = 'posts'

    id = Column(Integer, primary_key= True , index=True)
    title = Column(String(200),nullable= False)
    content = Column(Text , nullable=False)
    created_at =Column(DateTime, server_default=func.now(), index=True)
    updated_at =Column(DateTime , server_default=func.now(), onupdate= func.now())

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)

    author =relationship('User',back_populates='posts')
    comments = relationship('Comments', back_populates='post', cascade='all, delete-orphan')
    likes = relationship('Like', back_populates='post', cascade='all, delete-orphan')




class Comment(Base):
    __table_name__ = 'comments'

    id = Column(Integer,primary_key= True, index=True)
    comment = Column(Text,nullable=False)
    created_at =Column(DateTime, server_default=func.now, index=True)

    user_id =Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    post_id =Column(Integer, ForeignKey('posts.id'), nullable=False, index=True)

    author = relationship('User', back_populates='comments')
    post = relationship('Post', back_populates= 'comments')



class Like(Base):
    __table_name__  = 'likes'

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, server_default=func.now())

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False, index=True)

    user = relationship("User", back_populates="likes")
    post = relationship("Post", back_populates="likes")


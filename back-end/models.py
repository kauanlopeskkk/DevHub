from sqlalchemy import Column,Integer,String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Usuario(Base):
    __tablename__ = "Usuarios"

    id = Column(
        Integer,primary_key= True,
        index = True
    )

nome = Column(

    String,
    nullable= False

)


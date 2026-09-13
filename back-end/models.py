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
    index = True
)
email = Column(
    String,
    nullable= False,
    index = True
)

senha = Column(
    String,
    nullable = False,
    index = True
)

projetos = relationship("Projeto", back_populates="usuario")


class Projeto(Base):
    __tablename__ = "Projetos"

    id = Column(
        
        Integer, primary_key = True,
        index = True

    )
    nome = Column(

        String,
        nullable = False,
        index = True

    )
    descricao = Column(
        Text,
        nullable = False,
        index = True
    )
    status = Column(
        String,
        nullable =  False,
        index = True
    )
    usuario_id = Column(
        Integer,
        ForeignKey("Usuarios.id"),
        nullable = False,
        index = True
    )

    usuario = relationship("Usuario", back_populates="projetos")

    tarefas = relationship("Tarefa", back_populates="projetos")
    bugs = relationship("Bug", back_populates="projetos")

    class Tarefa(Base):
        __tablename__ = "Tarefas"

        id = Column(
            Integer, primary_key = True,
            index = True
        )
        nome = Column(
            String,
            nullable = False,
            index = True
        )
        descricao = Column(
            Text,
            nullable = False,
            index = True
        )
        status = Column(
            String,
            nullable = False,
            index = True
        )
        projeto_id = Column(
            Integer,
            ForeignKey("Projetos.id"),
            nullable = False,
            index = True
        )

        projetos = relationship("Projeto", back_populates="tarefas")

    class Bug(Base):
        __tablename__ = "Bugs"

        id = Column(
            Integer, primary_key = True,
            index = True
        )
        nome = Column(
            String,
            nullable = False,
            index = True
        )
        descricao = Column(
            Text,
            nullable = False,
            index = True
        )
        status = Column(
            String,
            nullable = False,
            index = True
        )
        projeto_id = Column(
            Integer,
            ForeignKey("Projetos.id"),
            nullable = False,
            index = True
        )

        projetos = relationship("Projeto", back_populates="bugs")
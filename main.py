from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, NVARCHAR, Boolean, VARCHAR, LargeBinary, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import date
from fastapi import FastAPI

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

Base = declarative_base()


class Arch_doc_cards(Base):
    __tablename__="arch_doc_cards"
    
    id:Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    year: Mapped["Arch_sq"] = relationship(back_populates="year")
    number:Mapped[int] # номер дела
    reg_date = Column(DateTime, nullable=False)
    LITERAL = Column(NVARCHAR(length=5))
    reg_number = Column(String())
    q_initiator = Column(NVARCHAR(length=100))
    surname_dep = Column(NVARCHAR(length=40))
    name_dep = Column(NVARCHAR(length=15))
    fname_dep = Column(NVARCHAR(length=15))
    q_person = Column(NVARCHAR(length=100))
    num_deponents = Column(Integer)
    inf = Column(Integer)
    inf_cmnt1 = Column(NVARCHAR(length=30))
    inf_cmnt2 = Column(NVARCHAR(length=30))
    note = Column(Integer)
    execute_date: Mapped(date)
    surname_repr = Column(NVARCHAR(length=15))
    name_repr = Column(NVARCHAR(length=15))
    fname_repr = Column(NVARCHAR(length=15))
    output_number = Column(NVARCHAR(length=50))
    num_d = Column(NVARCHAR(length=20))
    num_t = Column(NVARCHAR(length=20))
    num_p = Column(NVARCHAR(length=20))
    note_text = Column(NVARCHAR(length=30))
    sign_text = Column(NVARCHAR(length=30))
    repeated_of = Column(Integer)
    full_address = Column(NVARCHAR(length=500))
    is_repeated: Mapped[bool]
    type_letter = Column(Integer)
    p_num = Column(Integer)
    p_num_ap = Column(Integer)
    result = Column(Integer)
    result2 = Column(Integer)
    result3 = Column(Integer)
    doc_from = Column(Integer)
    result1 = Column(Integer)
    result4 = Column(Integer)
    numres1 = Column(Integer)
    numres2 = Column(Integer)
    numres3 = Column(Integer)
    numres4 = Column(Integer)
    result5 = Column(Integer)
    numres5 = Column(Integer)
    num_year = Column(Integer)
    output_number2 = Column(NVARCHAR(length=50))
    send_type = Column(Integer)

class Arch_sq(Base):
    __tablename__="arch_sq"
    id = Column(Integer, primary_key=True)
    year: Mapped["arch_doc_cards"] = relationship(back_populates="year")
    cur_number = Column(Integer, nullable=False)
    
class Arch_dict(Base):
    __tablename__="arch_dict"
    type_d = Column(Integer, nullable=False)
    value = Column(Integer)
    text = Column(NVARCHAR(length=50))
    id = Column(Integer, primary_key=True, nullable=False)
    n_order = Column(Integer)

class Arch_doc_signs(Base):
    __tablename__="arch_doc_signs"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    sign = Column(Integer, nullable=False)
    ex_sign = Column(Integer)
    id_card = Column(Integer, nullable=False)

class Arch_doc_signs_new(Base):
    __tablename__="arch_doc_signs_new"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    sign_group = Column(Integer, nullable=False) 
    sign_child = Column(Integer, nullable=False)
    ex_sign = Column(Integer)
    id_card = Column(Integer, nullable=False)
    
class Arch_doc_signs_new2(Base):
    __tablename__="arch_doc_signs_new2"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    sign_group = Column(Integer, nullable=False) 
    sign_child = Column(Integer)
    ex_sign = Column(Integer)
    id_card = Column(Integer, nullable=False)
    
class Dtproperties(Base):
    __tablename__="dtproperties"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    objectid = Column(Integer)
    property = Column(VARCHAR, primary_key=True, index=True, nullable=False)
    value = Column(VARCHAR(length=255))
    uvalue = Column(NVARCHAR(length=255))
    lvalue = Column(LargeBinary)
    version = Column(Integer, nullable=False)
        
Base.metadata.create_all(bind=engine)

app = FastAPI()

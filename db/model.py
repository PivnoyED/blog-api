from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from .db_helpers import Base

class Arch_doc_cards(Base):
    __tablename__="arch_doc_cards"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    year: Mapped[int] = mapped_column(comment='Год')
    number:Mapped[int] = mapped_column(comment='Номер дела')
    reg_date: Mapped[datetime] = mapped_column(comment='Дата регистрации')
    literal: Mapped[str]
    reg_number: Mapped[str]
    q_initiator: Mapped[str]
    surname_dep: Mapped[str]
    name_dep: Mapped[str]
    fname_dep: Mapped[str]
    q_person: Mapped[str]
    num_deponents: Mapped[int]
    inf: Mapped[int]
    inf_cmnt1: Mapped[str]
    inf_cmnt2: Mapped[str]
    note: Mapped[int]
    execute_date: Mapped[datetime]
    surname_repr: Mapped[str]
    name_repr: Mapped[str]
    fname_repr: Mapped[str]
    output_number: Mapped[str]
    num_d: Mapped[str]
    num_t: Mapped[str]
    num_p: Mapped[str]
    note_text: Mapped[str]
    sign_text: Mapped[str]
    repeated_of: Mapped[int]
    full_address: Mapped[str]
    is_repeated: Mapped[bool]
    type_letter: Mapped[int]
    p_num: Mapped[int]
    p_num_ap: Mapped[int]
    result: Mapped[int]
    result2: Mapped[int]
    result3: Mapped[int]
    doc_from: Mapped[int]
    result1: Mapped[int]
    result4: Mapped[int]
    numres1: Mapped[int]
    numres2: Mapped[int]
    numres3: Mapped[int]
    numres4: Mapped[int]
    result5: Mapped[int]
    numres5: Mapped[int]
    num_year: Mapped[int]
    output_number2: Mapped[str]
    send_type: Mapped[int]

class Arch_sq(Base):
    __tablename__="arch_sq"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    year: Mapped[int] = mapped_column(comment='Год')
    cur_number: Mapped[int]
    
class Arch_dict(Base):
    __tablename__="arch_dict"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    type_d: Mapped[int]
    value: Mapped[int]
    text: Mapped[str]
    n_order: Mapped[int]

class Arch_doc_signs(Base):
    __tablename__="arch_doc_signs"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    sign: Mapped[int]
    ex_sign: Mapped[int]
    id_card: Mapped[int]

class Arch_doc_signs_new(Base):
    __tablename__="arch_doc_signs_new"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    sign_group: Mapped[int] 
    sign_child: Mapped[int]
    ex_sign: Mapped[int]
    id_card: Mapped[int]
    
class Arch_doc_signs_new2(Base):
    __tablename__="arch_doc_signs_new2"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    sign_group: Mapped[int] 
    sign_child: Mapped[int]
    ex_sign: Mapped[int]
    id_card: Mapped[int]
    
class Dtproperties(Base):
    __tablename__="dtproperties"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    objectid: Mapped[int]
    property: Mapped[str]
    value: Mapped[str]
    uvalue: Mapped[str]
    lvalue: Mapped[str]
    version: Mapped[int]
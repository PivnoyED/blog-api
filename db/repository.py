from sqlalchemy.orm import Session

from db.model import Arch_doc_cards, Arch_sq, Arch_dict


def create_arch(archive, db):
    archive = Arch_doc_cards(
        id=archive.id,year=archive.year,number=archive.number,
        reg_date=archive.reg_date,literal=archive.literal,
        reg_number=archive.reg_number,q_initiator=archive.q_initiator,
        surname_dep=archive.surname_dep,name_dep=archive.name_dep,
        fname_dep=archive.fname_dep,q_person=archive.q_person,
        num_deponents=archive.num_deponents,inf=archive.inf,
        inf_cmnt1=archive.inf_cmnt1,inf_cmnt2=archive.inf_cmnt2,
        note=archive.note,execute_date=archive.execute_date,
        surname_repr=archive.surname_repr,name_repr=archive.name_repr,
        fname_repr=archive.fname_repr,output_number=archive.output_number,
        num_d=archive.num_d,num_t=archive.num_t,num_p=archive.num_p,
        note_text=archive.note_text,sign_text=archive.sign_text,
        repeated_of=archive.repeated_of,full_address=archive.full_address,
        is_repeated=archive.is_repeated,type_letter=archive.type_letter,
        p_num=archive.p_num,p_num_ap=archive.p_num_ap,result=archive.result,
        result2=archive.result2,result3=archive.result3,doc_from=archive.doc_from,
        result1=archive.result1,result4=archive.result4,numres1=archive.numres1,
        numres2=archive.numres2,numres3=archive.numres3,numres4=archive.numres4,
        result5=archive.result5,numres5=archive.numres5,num_year=archive.num_year,
        output_number2=archive.output_number2, send_type=archive.send_type)

    db.add(archive)
    db.commit()
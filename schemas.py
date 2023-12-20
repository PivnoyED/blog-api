from pydantic import BaseModel
from datetime import datetime

class Archive_request(BaseModel):
    id: int
    year: int
    number: int
    reg_date: datetime
    literal: str
    reg_number: str
    q_initiator: str
    surname_dep: str
    name_dep: str
    fname_dep: str
    q_person: str
    num_deponents: int
    inf: int
    inf_cmnt1: str
    inf_cmnt2: str
    note: int
    execute_date: datetime
    surname_repr: str
    name_repr: str
    fname_repr: str
    output_number: str
    num_d: str
    num_t: str
    num_p: str
    note_text: str
    sign_text: str
    repeated_of: int
    full_address: str
    is_repeated: bool
    type_letter: int
    p_num: int
    p_num_ap: int
    result: int
    result2: int
    result3: int
    doc_from: int
    result1: int
    result4: int
    numres1: int
    numres2: int
    numres3: int
    numres4: int
    result5: int
    numres5: int
    num_year: int
    output_number2: str
    send_type: int
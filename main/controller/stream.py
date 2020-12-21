from main.model import lists, db

def all_notes():
    data = lists.get_all_note()
    return data

def notes_by_id(id):
    data = lists.get_note_by_id(id)
    return data

def add_note(note:str):
    data_add = lists.listnote(note)
    db.session.add(data_add)
    db.session.commit()
    return data_add

def delete_note(id):
    data_delete = lists.get_note_by_id(id)
    if data_delete:
        data_delete.is_deleted = 1
        db.session.add(data_delete)
        db.session.commit()
        return True
    else:
        return False
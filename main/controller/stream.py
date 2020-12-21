from main.model import lists

def all_notes():
    data = lists.get_all_note()
    return data

def notes_by_id(id):
    data = lists.get_note_by_id(id)
    return data
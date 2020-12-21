from flask import Blueprint, jsonify, request
from . import routes
from main.controller import stream
from main.controller import book

@routes.route('/notes') #return all notes
@routes.route('/notes/<int:id>') #return specific note by id
def get_all_notes(id=0):
    if id:
        all_notes = stream.notes_by_id(id)
        data = {
            "id": all_notes.id,
            "note": all_notes.notes,
            "create_on": all_notes.timestamp.timestamp()
        }
    else:
        all_notes = stream.all_notes()
        data = []
        for note in all_notes:
            data.append({
                "id": note.id,
                "note": note.notes,
                "created_on": note.timestamp.timestamp()
            })
    response = {
        'result': data
    }
    return jsonify(response), 200
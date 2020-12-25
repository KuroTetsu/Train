from flask import Blueprint, jsonify, request
from . import routes
from main.controller import stream

@routes.route('/notes') #return all notes
@routes.route('/notes/<int:id>') #return specific note by id
def get_all_notes(id=0):
    if id:
        all_notes = stream.notes_by_id(id)
    else:
        all_notes = stream.all_notes()

    if not all_notes:
        return jsonify({"result": "data not found"}), 404
    try:
        data = []
        for note in all_notes:
            data.append(response_note(note))
    except:
        data = response_note(all_notes)

    response = {
        'result': data
    }
    return jsonify(response), 200

@routes.route('/add', methods=["POST"])
def add_note():
    note = request.form.get("note")
    
    data = stream.add_note(note)

    response = {
        'result': response_note(data)
    }

    return jsonify(response), 200

@routes.route('/delete/<int:id>', methods=["DELETE"])
def delete_note(id):
    result = stream.delete_note(id)
    
    if result:
        return jsonify(), 204
    else:
        return jsonify({"result":"note not found"}), 404

@routes.route('/edit/<int:id>', methods=['PATCH'])
def update_note(id):
    note = request.form.get("note")
    
    try:
        data = stream.update_note(id,note)
        response = {
            'result':response_note(data)
        }

        return jsonify(response), 200
    except:
        return jsonify({"result":"note not found"}), 404

def response_note(note):
    return {
        "id": note.id,
        "note": note.notes,
        "create_on": note.timestamp.timestamp()
    }
from flask import Blueprint, jsonify, request
from . import routes
from main.controller import stream

#
# return all note or a spesific note by note id
#
@routes.route('/notes', methods=['GET']) 
@routes.route('/notes/<int:id>', methods=['GET']) 
def get_notes(id=0):
    if id:
        notes = stream.notes_by_id(id)
    else:
        notes = stream.all_notes()

    if not notes:
        return jsonify({"result": "data not found"}), 404
    try:
        data = []
        for note in notes:
            data.append(response_note(note))
    except:
        data = response_note(notes)

    response = {
        'result': data
    }
    return jsonify(response), 200

# 
# return all archive note
#
@routes.route('/archive', methods=['GET']) 
def get_archives():
    notes = stream.archive_notes()

    data = []
    for note in notes:
        data.append(response_note(note))

    response = {
        'result': data
    }

    return jsonify(response), 200

#
# create a note
# possible to archive after create a note
#
@routes.route('/add', methods=["POST"])
def add_note():
    note = request.form.get("note")
    is_archive = request.form.get("is_archive", 0)
    
    data = stream.add_note(note, is_archive)

    response = {
        'result': response_note(data)
    }

    return jsonify(response), 200

#
# delete a note with response no content
# possible to response 404 because id note is not found
#
@routes.route('/delete/<int:id>', methods=["DELETE"])
def delete_note(id):
    result = stream.delete_note(id)
    
    if result:
        return jsonify(), 204
    else:
        return jsonify({"result":"note not found"}), 404

#
# update a note and also can archive it
#
@routes.route('/edit/<int:id>', methods=['PATCH'])
def update_note(id):
    note = request.form.get("note")
    is_archive = request.form.get("is_archive")
    
    try:
        data = stream.update_note(id,note, is_archive)
        response = {
            'result':response_note(data)
        }

        return jsonify(response), 200
    except:
        return jsonify({"result":"note not found"}), 404

#
# default respone a note
#
def response_note(note):
    return {
        "id": note.id,
        "note": note.notes,
        "create_on": note.timestamp.timestamp()
    }
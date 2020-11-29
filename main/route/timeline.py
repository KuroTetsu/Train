from flask import Blueprint, jsonify, request
from . import routes
from main.controller import stream
from main.controller import book

@routes.route('/')
def index():
    return 'Hello'

@routes.route('/timeline')
def timeline_get():
    streams = stream.get_timeline()
    response = {
        'hasil' : streams['a'],
        'hasil_2': streams['a'] + streams['b'],
    }

    return jsonify(response), 200


@routes.route('/rekomendasi')
def rekomendasi():
    
    page = request.args.get("page", "1")
    filter_1 = request.args.get("filter_1", "update") #update, new, rank
    filter_2 = request.args.get("filter_2", None) #all, manga, manhwa, manhua
    filter_3 = request.args.get("filter_3", None) #all, action, adv, comedy, ..

    page = int(page)
    rekomendasi = book.rekomendasi(page, filter_1, 'manhua', filter_3)

    response = {
        'result': rekomendasi['data'],
        'next': rekomendasi['next'],
        'prev': rekomendasi['prev']
    }
    return jsonify(response), 200
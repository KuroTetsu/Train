from main.model import book

def rekomendasi(page:int, filter_1:str, filter_2:str, filter_3:str):
    data = book.get_data(filter_1, filter_2, filter_3)
    hasil = {
        'data': data,
        'next': page + 1,
        'prev': page - 1,
    }
    return hasil
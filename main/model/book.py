import json
def get_data(filter_1:str, filter_2:str=None, filter_3:str=None):
    data = [{
                'id': 1,
                'rank': 1, 
                'filter_2':'manga',
                'filter_3':'action',
                'title':'ini title 1',
                'desc':'ini desc',
                'chapter_1': 1,
                'chapter_last': 99,
                'komikus':'nama komikus',
                'status':'ongoing',
                'total pembaca': 999999
            },{
                'id': 2,
                'rank': 24,
                'filter_2':'manga',
                'filter_3':'action',
                'title':'ini title 2',
                'desc':'ini desc',
                'chapter_1': 1,
                'chapter_last': 27,
                'komikus':'nama komikus',
                'status':'ongoing',
                'total pembaca': 888899
            },{
                'id': 3,
                'rank': 3,
                'filter_2':'manga',
                'filter_3':'crime',
                'title':'ini title 3',
                'desc':'ini desc',
                'chapter_1': 1,
                'chapter_last': 49,
                'komikus':'nama komikus',
                'status':'ongoing',
                'total pembaca': 123456
            },{
                'id': 4,
                'rank': 10,
                'filter_2':'manhwa',
                'filter_3':'crime',
                'title':'ini title 4',
                'desc':'ini desc',
                'chapter_1': 1,
                'chapter_last': 22,
                'komikus':'nama komikus',
                'status':'end',
                'total pembaca': 123456
            },{
                'id': 5,
                'rank': 13,
                'filter_2':'manhua',
                'filter_3':'action',
                'title':'ini title 5',
                'desc':'ini desc',
                'chapter_1': 1,
                'chapter_last': 49,
                'komikus':'nama komikus',
                'status':'ongoing',
                'total pembaca': 123456
            }
        ]
    if filter_2:
        data_filter = filter(lambda d: d['filter_2'] == filter_2, data)
        data = list(data_filter)

    return data

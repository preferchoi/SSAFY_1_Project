import json


def max_revenue(movies):
    # 여기에 코드를 작성합니다.  
    max_name, max_revenue= '', 0
    for i in movies:
        movies_json = open(f'data/movies/{i.get("id")}.json', encoding='utf-8')
        movies_list = json.load(movies_json)
        revenue = movies_list.get('revenue')
        if max_revenue < revenue:
            max_revenue = revenue
            max_name = movies_list.get('title')
    return max_name
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))


'''
import json
import os

def max_revenue(movies):
    # 여기에 코드를 작성합니다.  
    max_name = ''
    max_revenue = 0
    for i in movies:
        if i[1] > max_revenue:
            max_name = i[0]
            max_revenue = i[1]
    return max_name
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    file_list = os.listdir('data/movies/')
    # print(file_list)
    name_revenue_list = []
    for i in file_list:
        movies_json = open(f'data/movies/{i}', encoding='utf-8')
        movies_list = json.load(movies_json)
        name_revenue_list.append([movies_list.get('title'), movies_list.get('revenue')])
    print(max_revenue(name_revenue_list))

    
'''
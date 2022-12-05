import json


def dec_movies(movies):
    # 여기에 코드를 작성합니다. 
    december = []
    for i in movies:
        movies_json = open(f'data/movies/{i.get("id")}.json', encoding='utf-8')
        movies_list = json.load(movies_json)
        date = movies_list.get('release_date')
        if date[5:7] == '12':
            december.append(movies_list.get('title'))
    return december

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))

import json

# 영화 제목, 평점, 평가자 수 출력

def dec_movies(movies):
    # 여기에 코드를 작성합니다. 
    vote_average_list = []
    for i in movies:
        movies_json = open(f'data/movies/{i.get("id")}.json', encoding='utf-8')
        movies_list = json.load(movies_json)
        vote_average_list.append([movies_list.get('title'), movies_list.get('vote_average'), movies_list.get('vote_count')])
    return vote_average_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))

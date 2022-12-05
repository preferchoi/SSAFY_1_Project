import json
from pprint import pprint


def movie_info(movies, genres):
    
    # 여기에 코드를 작성합니다.  
    result_list = []
    for i in movies:
        result = {
            'id':i.get('id'), 
            'title':i.get('title'), 
            'poster_path':i.get('poster_path'), 
            'vote_average':i.get('vote_average'),
            'overview':i.get('overview'), 
            'genre_ids':i.get('genre_ids')}
        movie_ids = i.get('genre_ids')
        res1 = []
        for j in genres:
            if j.get('id') in result['genre_ids']:
                res1.append(j.get('name'))
        result['genre_ids'] = res1
        result_list.append(result)
    
    return result_list
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))

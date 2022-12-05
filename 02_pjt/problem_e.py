import requests
from pprint import pprint


def credits(title):
    # 여기에 코드를 작성합니다.
    result_dict = {}
    api_key = ''
    url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={title}&language=ko&page=1&include_adult=false'
    response = requests.get(url).json()
    result = response.get('results')
    result = response.get('results')

    try:
        movie_id = result[0].get('id')

        url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}&language=ko'
        response = requests.get(url).json()
        result = response.get('cast')
        res_list = []

        for i in result:
            if i.get('cast_id') < 10:
                res_list.append(i.get('name'))
        result_dict['cast'] = res_list
        result = response.get('crew')
        res_list = []

        for i in result:
            if i.get('department') == 'Directing':
                res_list.append(i.get('name'))
        result_dict['crew'] = res_list

        return result_dict
    except IndexError:
        return
    # 아래의 코드는 수정하지 않습니다.


if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None

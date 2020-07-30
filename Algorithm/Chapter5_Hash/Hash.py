'''
해시 테이블의 사용 예: 캐싱
'''
cache = {}
def get_page(url):
    if cache.get(url):
        return cache[url] #캐싱된 자료 전송
    else:
        data = get_data(url)
        cache[url] = data #캐시에 처음으로 자료 저장
        return data
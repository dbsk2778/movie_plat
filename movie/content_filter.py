import pandas as pd 
import warnings; warnings.filterwarnings('ignore')
from ast import literal_eval 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity 


# 데이터 불러오기(전처리 된 데이터)
movies= pd.read_csv('end_movies.csv')
movies_df = movies[['id', 'title', 'genre_ids', 'vote_average', 'vote_count', 'poster_path']]

# 데이터 전처리
movies_df['genre_ids'] = movies_df['genre_ids'].apply(literal_eval)

# CounterVectorizer를 적용하기 위해 공백 문자로 word 단위가 구분되어지는 문자열로 변환시킴
movies_df['genres_liters'] = movies_df['genre_ids'].apply(lambda x : ' '.join(x))

# 장르 빈도수 벡터화
count_vect = CountVectorizer(min_df=0, ngram_range=(1,2)) 
genre_mat = count_vect.fit_transform(movies_df['genres_liters'])

# 코사인 유사도 계산 및 정렬
genre_sim = cosine_similarity(genre_mat, genre_mat) 
genre_sim_sorted_idx = genre_sim.argsort()[:, ::-1]
percentile = 0.6
m = movies['vote_count'].quantile(percentile)
C = movies['vote_average'].mean()

# 가중 평점 도입 (평균 점수와 표본수 반영)
def weighted_vote_average(record): 
    v = record['vote_count'] 
    R = record['vote_average']
    return ((v/(v+m))*R) + ((m/(m+v))*C)

movies_df['weighted_vote'] = movies_df.apply(weighted_vote_average, axis=1)
movies_df[['title', 'vote_average', 'weighted_vote', 'vote_count']].sort_values('weighted_vote', ascending=False)[:10]

sorted_idx = genre_sim_sorted_idx

# 타이틀 입력 시 유사한 영화 추천
def find_sim_movie(title, top_n=21):

    title_movie = movies_df[movies_df['title'] == title]
    title_index = title_movie.index.values

    similar_indexes = sorted_idx[title_index, :(top_n*2)] 
    similar_indexes = similar_indexes.reshape(-1)

    # 검색 값 제외하고 출력
    similar_indexes = similar_indexes[similar_indexes != title_index]

    # response 객체로 보내야하는데 title을 보내야하고 {'title':['이름1', '이름2' ..., '이름10']} 형식으로 보내야 함
    # similar_movies = movies_df.iloc[similar_indexes].sort_values('weighted_vote', ascending=False)[:top_n]
    similar_movies = movies_df.iloc[similar_indexes].sort_values('weighted_vote', ascending=False)

    return movies_df.iloc[similar_indexes].sort_values('weighted_vote', ascending=False)[:top_n]

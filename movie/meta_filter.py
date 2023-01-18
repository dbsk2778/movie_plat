import pandas as pd
import numpy as np
from ast import literal_eval
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings; warnings.simplefilter('ignore')

# meta_filter은 감독, 출연 배우 기반으로 콘텐츠 추천해주는 코드

# 데이터 불러오기 
meta_movies = pd.read_csv('metadata_filter.csv')

# vote_count / vote_averages 값 null값 아닐 경우 int형 변환
vote_counts = meta_movies[meta_movies['vote_count'].notnull()]['vote_count'].astype('int')
vote_averages = meta_movies[meta_movies['vote_average'].notnull()]['vote_average'].astype('int')

# 가중치 설정
C = vote_averages.mean()
m = vote_counts.quantile(0.95)  # 상위 5%
    
# 가중치 주는 함수
def weighted_rating(x):
    v = x['vote_count']
    R = x['vote_average']
    return (v/(v+m) * R) + (m/(m+v) * C)

# 장르 빈도수 벡터화
count = CountVectorizer(analyzer='word', ngram_range=(1,2), min_df=0, stop_words='english')
count_matrix = count.fit_transform(meta_movies['soup'])

# 코사인 유사도 계산
cosine_sim = cosine_similarity(count_matrix, count_matrix)

# meta_movies값 index 변경
meta_movies = meta_movies.reset_index()
titles = meta_movies['title']
indices = pd.Series(meta_movies.index, index=meta_movies['title'])


def meta_recommendations(title):

    idx = indices[title]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:100]
    movie_indices = [i[0] for i in sim_scores]


    movies = meta_movies.iloc[movie_indices][['id','title','vote_count','vote_average','year']]

    
    vote_counts = movies[movies['vote_count'].notnull()]['vote_count'].astype('int')
    vote_averages = movies[movies['vote_average'].notnull()]['vote_average'].astype('int')

    C = vote_averages.mean()
    m = vote_counts.quantile(0.7)

    qualified = movies[(movies['vote_count'] >= m) & (movies['vote_count'].notnull())]

    qualified['vote_count'] = qualified['vote_count'].astype('int')
    qualified['wr'] = qualified.apply(weighted_rating, axis=1)
    qualified = qualified.sort_values('wr', ascending=False).head(21)
    
    return qualified
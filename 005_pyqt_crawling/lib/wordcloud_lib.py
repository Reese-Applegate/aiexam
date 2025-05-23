# 라이브러리 불러오기
import pandas as pd
import re
import matplotlib.pyplot as plt

from wordcloud import WordCloud


# [python] re.sub 정규표현식을 통한 문자열 치환 (특수문자 제거)
# ref.https://clolee.tistory.com/17
def clean_text(inputString):
    text_rmv = re.sub(
        "[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`'…》\”\“\’·]", " ", inputString
    )
    text_rmv = " ".join(text_rmv.split())
    return text_rmv


def WordCloud_Create(
    filename, input_stopwords
):  # 파일명 변수 하나로 이미지까지 생성되도록.
    # 파일 불러오기
    df_crawl = pd.read_csv(filename, encoding="cp949")
    df = df_crawl.drop(["link"], axis="columns")
    list = df["text"].astype(str).tolist()
    word_str = " ".join(s for s in list)
    word_str_cut = clean_text(word_str)

    # 금지어 지정
    refined_stopwords = [word.strip() for word in input_stopwords.split(", ")]

    wc1 = WordCloud(
        font_path="c:\windows\fonts\malgun.ttf",
        stopwords=refined_stopwords,
        background_color="white",
        width=1024,
        height=768,
        random_state=42,
    )

    wc1.generate(word_str_cut)

    saveWc = filename.replace(".csv", ".png")

    wc1.to_file(saveWc)

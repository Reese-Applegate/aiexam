stopwords = "고양이, 고양이가               , 고양이는"

# split_stopwords = (stopwords.split(", "))
# print(split_stopwords)


# strip_stopwords = [] # 빈 리스트 생성
# for word in split_stopwords:
#     strip_stopwords.append(word.strip())
split_stopwords = stopwords.split(", ")
strip_stopwords = [word.strip() for word in stopwords.split(", ")]

print(strip_stopwords)

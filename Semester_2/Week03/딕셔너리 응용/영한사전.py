lib = dict()
lib['one'] = '하나'
lib['two'] = '둘'
lib['three'] ='셋'
lib.update(four = '넷')
lib.update({'five':'다섯'})
print(lib)
word = input("단어를 입력하시오 : ")
print(lib.get(word, '없음')) # get함수 활용

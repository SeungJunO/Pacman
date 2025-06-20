eng_dict = dict()

eng_dict['one'] = '하나'
eng_dict['two'] = '둘'
eng_dict['three'] = '셋'

word = input('단어를 입력하시오:')
print(eng_dict.get(word,"없음"))

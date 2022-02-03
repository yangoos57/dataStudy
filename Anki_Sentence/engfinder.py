#%%
import time
import requests
from bs4 import BeautifulSoup
import re

# list 결과 출력용도
def test_sen(extraction) :
    for num, sen in enumerate(extraction) :
        print(f'{num}. {sen}')


# 영단어 검색 및 추출 Class
class eng_sentence_find :
    '''
    해당 클래스는 
     1. Longman 문장 및 음원 추출 Class
     2. Cambridge 문장 추출 Class
     3. 입력받은 단어를 정제와 단어를 출력하는 과정을 담당하는 Class
     로 구성되어있습니다.
     
     '''

    def __init__(self, word) :
        self.word = word

        # requests 크롤링 접근차단 해제 용도
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko)  Chrome/63.0.3239.132 Safari/537.36'}

    # page를 load하기 위한 매서드입니다. 
    def load_page(self) :
        response = requests.get(self.url,headers= self.headers )
        load_page = BeautifulSoup(response.text, 'html.parser')
        return load_page

    
    # Papago sound 작업 중 
    def papago_sound_extract(self, sen_list):
        # print(sen_list)
        for sen in sen_list :
            sentence = 'https://papago.naver.com/?sk=en&tk=ko&hn=1&st='+ sen
            print(sentence)
        # return 


# Longman 문장 및 음원 추출과 관련된 Class입니다.
class longman_sentence(eng_sentence_find) :

    #  load_page에서 추출된 html에서 모든문장을 추출합니다.
    def extract_examples(self) :
        loaded_page = super().load_page()
        examples = loaded_page.select('.EXAMPLE')
        return examples

    # longman 문장 중 sound가 포함된 문장과 그렇지 않은 문장이 있습니다. 
    # 이중 sound가 포함된 문장만 추출하는 매서드입니다.
    def sound_included_sen_list(self) :
        sound_extract_examples = [sen for sen in self.extract_examples 
                                  if re.search('Play Example',str(sen))]
        return sound_extract_examples

    # Longman class를 선택하면 example과 sound included example이 자동으로 추출됩니다.
    def __init__(self, word):
        super().__init__(word)
        self.url = str('https://www.ldoceonline.com/dictionary/'
                        + self.word)
        self.extract_examples = self.extract_examples()
        self.sound_extract_examples = self.sound_included_sen_list()


    # 추출된 example에 포함된 수식을 제거하는 매서드입니다.
    def refine_all_sen_list(self) :
        refine_examples = [x.text.replace('\n','').replace('\xa0','') 
                          for x in self.extract_examples]
        return refine_examples


    # 추출된 sound_included_sen_list에 포함된 수식을 제거하는 매서드입니다.
    def refine_sound_included_sen_list(self):
        refined_sound_examples = [x.text.replace('\n','').replace('\xa0','') 
                                  for x in self.sound_extract_examples]
        return refined_sound_examples


    # sound url을 추출하는 매서드입니다.
    def sound_url_list(self) : 
        sound_url_list =[str(sen).split('"')[5] 
                         for sen in self.sound_extract_examples]
        return sound_url_list


    # sound 파일을 다운받는 매서드 입니다. (선택한 문장으로 받는 메서드로 바꾸기 )
    def download_sound(self) :
        sound_url_list = self.sound_url_list()
        refine_examples = self.refine_sound_included_sen_list()
        for i in range(len(sound_url_list)) :
            sound_link = sound_url_list[i]
            file_name = refine_examples[i]
            response = requests.get(sound_link, headers=self.headers)
            # with open(f'D:\OneDrive - knou.ac.kr\ANKI\Sound\{file_name}.mp3', 'wb') as f:
            #     f.write(response.content)
            print(f'"{file_name}" 다운로드 중 \n 총 {len(sound_url_list)} 중 {i+1}차례 받는 중')
            time.sleep(1)

    # 사운드가 있는 예문을 앞으로 두고 사운드가 없는 예문을 뒤로 두는 매서드입니다.
    def merge_all_sen_and_sound_sen(self) :
      all_sen = self.refine_all_sen_list()
      sound_sen = self.refine_sound_included_sen_list()
      sound_unincluded_sentence = [sen for sen in all_sen if not sen in sound_sen]
      return sound_sen + sound_unincluded_sentence


# Cambridge 문장 추출 Class 입니다.
class cambridge_sentence(eng_sentence_find) :

    def __init__(self, word):
        super().__init__(word)
        self.url = str('https://dictionary.cambridge.org/us/dictionary/english/' 
                       + self.word)

    # 예문을 추출하고 정제하는 매서드입니다. 
    def refine_all_sen_list(self) :
        loaded_page = super().load_page()
        extract_examples = loaded_page.find_all('span', {'class' : 'eg deg'})
        refine_exmples = [a.text for a in extract_examples]
        return refine_exmples

    def test_refine_all_sen_list(self) :
        loaded_page = super().load_page()
        extract_examples = loaded_page.find_all('span', {'class' : 'eg deg'})
        refine_exmples = [a.text for a in extract_examples][0]
        return refine_exmples




# 원하는 문장을 고르고 출력 기능을 담당하는 class입니다.
class selecting_sentence(eng_sentence_find) :

    def __init__(self, word) :
        super().__init__(word)
        self.long_on() # longman dictionary is default.

    # Longman 검색기능 On
    def long_on(self) :
        self.long = 1
        self.cam = 0
        return self.long, self.cam

    # Cambridge 검색기능 On
    def long_off(self) :
        self.long = 0
        self.cam = 1
        return self.long, self.cam

    # 원하는 문장을 범위로 표현하면 다시 숫자로 바꾸는 매서드입니다.
    # 1~4 => 1,2,3,4 // 1-4 => 1,2,3,4 
    def wave_bar(self, num) : 
        if '~' in num :
            b = num.split('~')
        
        elif '-' in num :
            b = num.split('-')
        
        else :
            print('~ or - 만 가능합니다.')

        b = list(range(int(b[0]),int(b[-1])+1))  
        return b

    # 원하는 문장 번호를 적거나 범위(~ 또는 -)로 적으면 이를 숫자로 표현하는 매서드입니다.
    # 1~4, 5,7 => 1,2,3,4,5,7 
    def sorting_sen(self, num) :

        # 콤마를 기준으로 구분한다.
        a = num.replace(' ','')
        b = a.split(',')

        # ~ 또는 -이 포함되면 wave_bar 매서드로 숫자로 변환
        c = []
        for n, i in enumerate(b) :
            if '~' in i or '-' in  i :
                d = self.wave_bar(b.pop(n))
                c += d

        e = c + b
        e = [int(a)-1 for a in e] 

        return list(set(e))

    # 문장을 고르고 리스트로 반환하는 매서드입니다. 
    def extract_select_sen(self,num) :
        if self.long == True :
            sentence_list = longman_sentence(self.word).merge_all_sen_and_sound_sen()

        elif self.cam == True :
            sentence_list = cambridge_sentence(self.word).refine_all_sen_list()

        self.show_sen(sentence_list) ### 문장 print
        select_sen = self.sorting_sen(num)

        # 문장 sound 추출 
        # longman 추출
            # Longman은 문장 매치를 통해 번호를 뽑고 추출 
            # 이때 번호가 초과하면 Papago 번역 추출 

        # Cambridge 추출 
         # papago 번역으로 추출 
        extract_select_sen = [sentence_list[num] for num in select_sen]
        return extract_select_sen


    def show_sen(self, extraction) :
        for num, sen in enumerate(extraction) :
            print(f'{num}. {sen}')



if __name__ == '__main__' :
    # # 단어 검색
    # a = selecting_sentence('song')
    # # # 원하는 단어 추출 
    # a.long_off()
    # b = a.extract_select_sen('1')
    # print('')
    # print(b)
    k = 'song'
    a = cambridge_sentence(k)
    b = [cambridge_sentence(k).test_refine_all_sen_list()]
    c = a.papago_sound_extract(b)
    


# %%
k = 'pasta'
a = longman_sentence(k)
a_1 = a.merge_all_sen_and_sound_sen()
b = cambridge_sentence(k)
b_1 = b.refine_all_sen_list()
test_sen(a_1)
test_sen(b_1)


#%%
k = input()
print(type(k))
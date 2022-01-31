#%%
import time
import requests
from bs4 import BeautifulSoup
import re

def test_sen(extraction) :
    for num, sen in enumerate(extraction) :
        print(f'{num}. {sen}')

class eng_sentence_find :

    def __init__(self, word) :
        self.word = word
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko)  Chrome/63.0.3239.132 Safari/537.36'}

    def load_page(self) :
        response = requests.get(self.url,headers= self.headers )
        load_page = BeautifulSoup(response.text, 'html.parser')
        return load_page




class longman_sentence(eng_sentence_find) :

    def extract_examples(self) :
        loaded_page = super().load_page()
        examples = loaded_page.select('.EXAMPLE')
        return examples

    def sound_included_sen_list(self) :
        sound_extract_examples = [sen for sen in self.extract_examples 
                                  if re.search('Play Example',str(sen))]
        return sound_extract_examples

    def __init__(self, word):
        super().__init__(word)
        self.url = str('https://www.ldoceonline.com/dictionary/'+ self.word)
        self.extract_examples = self.extract_examples()
        self.sound_included_sen_list = self.sound_included_sen_list()

    def refine_all_sen_list(self) :
        refine_exmples = [x.text.replace('\n','').replace('\xa0','') 
                          for x in self.extract_examples]
        return refine_exmples


    def refine_sound_included_sen_list(self):
        refine_exmples = [x.text.replace('\n','').replace('\xa0','') 
                          for x in self.sound_included_sen_list]
        return refine_exmples


    def sound_url_list(self) : 
        sound_url_list =[str(sen).split('"')[5] 
                         for sen in self.sound_included_sen_list]
        return sound_url_list


    def download_sound(self) :
        sound_url_list = self.sound_url_list()
        refine_examples = self.refine_sound_included_sen_list()
        for i in range(len(sound_url_list)) :
            link = sound_url_list[i]
            name = refine_examples[i]
            response = requests.get(link, headers=self.headers)
            # with open(f'D:\OneDrive - knou.ac.kr\ANKI\Sound\{name}.mp3', 'wb') as f:
            #     f.write(response.content)
            print(f'"{name}" 다운로드 중 \n 총 {len(sound_url_list)} 중 {i+1}차례 받는 중')
            time.sleep(1)


    def merge_all_sen_and_sound_sen(self) :
      all_sen = self.refine_all_sen_list()
      sound_sen = self.refine_sound_included_sen_list()
      sound_unincluded_sentence = [sen for sen in all_sen if not sen in sound_sen]
      return sound_sen + sound_unincluded_sentence

class cambridge_sentence(eng_sentence_find) :

    def __init__(self, word):
        super().__init__(word)
        self.url = str('https://dictionary.cambridge.org/us/dictionary/english/' 
                       + self.word)

    def refine_all_sen_list(self) :
        loaded_page = super().load_page()
        extract_examples = loaded_page.find_all('span', {'class' : 'eg deg'})
        refine_exmples = [a.text for a in extract_examples]
        return refine_exmples
    
    def refine_sound_included_sen_list(self):
        return False



class selecting_sentence(eng_sentence_find) :

  def __init__(self, word) :
    super().__init__(word)
    self.long_on() # longman dictionary is default.

  def long_on(self) :
      self.long = 1
      self.cam = 0
      return self.long, self.cam

  def long_off(self) :
      self.long = 0
      self.cam = 1
      return self.long, self.cam


  def wave_bar(self, num) : 
    if '~' in num :
        b = num.split('~')
    
    elif '-' in num :
        b = num.split('-')
    
    else :
        print('~ or - 만 가능')

    b = list(range(int(b[0]),int(b[-1])+1))  
    return b

  def sorting_sen(self, num) :
    a = num.replace(' ','')
    b = a.split(',')
    c = []

    for n, i in enumerate(b) :
        if '~' in i or '-' in  i :
            d = self.wave_bar(b.pop(n))
            c += d

    e = c + b
    e = [int(a)-1 for a in e] 

    return list(set(e))

  def selecting_sen(self,num) :
    if self.long == True :
      sentence_list = longman_sentence(self.word).merge_all_sen_and_sound_sen()

    elif self.cam == True :
      sentence_list = cambridge_sentence(self.word).refine_all_sen_list()

    self.show_sen(sentence_list)
    select_sen = self.sorting_sen(num)
    
    extract_select_sen = [sentence_list[num] for num in select_sen]
    return extract_select_sen

  def show_sen(self, extraction) :
    for num, sen in enumerate(extraction) :
        print(f'{num}. {sen}')



if __name__ == '__main__' :
    a = selecting_sentence('pizza')
    a.long_on()
    b = a.selecting_sen('1')

    #   c = cambridge_sentence('computer')
    #   d = c.refine_all_sen_list()
    print(a)
    print(b)
    print('')
    #   print(d)
# %%
k = 'pasta'
a = longman_sentence(k)
a_1 = a.merge_all_sen_and_sound_sen()
b = cambridge_sentence(k)
b_1 = b.refine_all_sen_list()
test_sen(a_1)
test_sen(b_1)
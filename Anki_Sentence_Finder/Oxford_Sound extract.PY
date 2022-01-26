#%%
import time # 사이트를 불러올 때, 작업 지연시간을 지정해주기 위한 패키지이다. (사이트가 늦게 켜지면 에러가 발생하기 때문)
import requests
from bs4 import BeautifulSoup
import pyautogui
import pyperclip

### 함수 모으기
def sentence_extraction(ist_name) :  #### 추출하고 싶은 리스트 
    k = input('원하는 문장 고르기')
    if '~' in k : 
        l = k.split('~')
        d = [int(a) for a in l]
        p = list(range(d[0],d[1]+1))

    elif ',' in k :
        l = k.split(',')
        p = [int(a) for a in l]

    elif k =='``' :
        p =[]    

    else :
        p = [int(k)]

    h = [a-1 for a in p]

    ### 원하는 문장만 추출
    ist_name 
    new_list=[]
    for i in h : 
        j = ist_name[i]
        new_list.append(j)
    return new_list


################# 모드 선택하기
mode_choice = input('모드 선택 1: OneNote 붙여넣기 2: Anki 붙여넣기')
if mode_choice == '1':
    Mode_OneNote = True
else :
    Mode_OneNote = False

while True :
    h = [] ; cam_h = [] ### 리스트 갱신
    
### 단어 검색
    word = input('모르는 단어 검색')

    if ' ' in word : 
        a = word.replace(' ','-')
        word = a
    if word == '``' :
        print('\n검색 종료')
        break

################## 문장 추출하기 
    ### 사이트 접속
    url = str('https://www.ldoceonline.com/dictionary/'+word)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    response = requests.get(url,headers=headers )

    url_cam = str('https://dictionary.cambridge.org/ko/%EC%82%AC%EC%A0%84/%EC%98%81%EC%96%B4/'+word)
    response_cam = requests.get(url_cam,headers=headers )

    ### Longman sentences 추출
    lm = BeautifulSoup(response.text, 'html.parser')
    lm_example = lm.select('.EXAMPLE')

    lm_sound =[]
    for i in range(len(lm_example)) : 
        p = lm_example[i]
        k = str(p)
        a = 'Play Example'
        if a in k :
            lm_sound.append(p)
    lm_remove = [a.text for a in lm_sound] ## example 추출
    lm_remove_com =[a.replace('\xa0','').replace('\n','') for a in lm_remove] ## example 정제 및 사운드 없는 문장 제거

    ### Cambridge sentences 추출
    cam = BeautifulSoup(response_cam.text, 'html.parser')
    cam_example = cam.find_all('span', {'class' : 'eg deg'})
    cam_remove = [a.text for a in cam_example]





################ OneNote 붙여넣기 모드
    if Mode_OneNote == True :
        ### Longman 문장 보여주기
        if bool(lm_remove_com) == True : 
            print('\nLongMan 단어 추출')        
            for i in range(len(lm_remove_com)) :
                k = lm_remove_com[i]
                print(f'{i+1}. {k}')
            lm_new_list = sentence_extraction(lm_remove_com)
        else :
            lm_new_list =[]
        if bool(lm_remove_com) == False and bool(cam_remove) == False : 
            print('\n예문이 존재하지 않습니다\n')
            continue

        ### Cambridge리스트 보여주기
        print('\n\nCambridge 단어 추출')
        for i in range(len(cam_remove)) : 
            ist_name = cam_remove[i]
            print(f'{i+1}. {ist_name}')
        cam_new_list = sentence_extraction(cam_remove)



 ### OneNote에 붙여넣기
        total_list = lm_new_list + cam_new_list
        if bool(cam_new_list) == True or bool(lm_new_list) == True : 
            pyautogui.hotkey('win','9')
            time.sleep(0.3)
            pyautogui.click(500,500)
            pyautogui.click(500,500)
            time.sleep(0.3)
            # pyautogui.hotkey('ctrl','n')
            # time.sleep(0.3)
            # pyautogui.press(['tab'])
            # pyautogui.press(['tab'])
            time.sleep(0.3)
            pyautogui.press(['enter'])
            pyautogui.hotkey('ctrl','.')
            for i in range(len(total_list)) : 
                word = total_list[i]
                pyperclip.copy(word)
                pyautogui.hotkey('ctrl','v')
                pyautogui.press(['enter'])
                time.sleep(0.3)
            # pyautogui.hotkey('ctrl','a')
            # pyautogui.hotkey('ctrl','a')
            # pyautogui.hotkey('ctrl','c')


################ Anki 붙여넣기 모드    
    if Mode_OneNote == False :    
        # print(f'Example 추출 :  {len(lm_example)}개')
        print(f'sound 추출 :  {len(lm_sound)}개')

        ### Longman 문장 보여주기
        for i in range(len(lm_remove_com)) :
            k = lm_remove_com[i]
            print(f'{i+1}. {k}')


    ########## 단어 검색 실패 시 사이트 띄우기
            # if len(cam_example) == 0 :
            #     subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\chromdriver\Temp"')
            #     chrome_options = Options()
            #     chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
            #     chrome_driver = "D:\chromdriver\chromedriver.exe"
            #     browser = webdriver.Chrome(chrome_driver, options=chrome_options)
            #     browser.implicitly_wait(time_to_wait=7)
            #     browser.get(url_cam)
            #     sys.exit('자료가 없으므로 종료')

    ############ 원하는 리스트 고르기 시작
        ### Longman 문장 고르기 comma또는 물결로 값 구분하기 
        if len(lm_sound) != 0 :
            k = input('원하는 문장 고르기')
            if '~' in k : 
                l = k.split('~')
                d = [int(a) for a in l]
                p = list(range(d[0],d[1]+1))

            elif ',' in k :
                l = k.split(',')
                p = [int(a) for a in l]

            elif k =='``' :
                p =[]    

            else :
                p = [int(k)]

            h = [a-1 for a in p]
            print(h)

            ### 원하는 문장만 추출
            lm_new_list=[] ; lm_new_sound =[]
            for i in h : 
                j = lm_remove_com[i]
                lm_new_list.append(j)
                o = lm_sound[i]
                lm_new_sound.append(o)

            ### 문장 url 가지고 오기
            lm_sound_pure = []
            for i in range(len(lm_new_sound)) : 
                asd = str(lm_new_sound[i])
                bcd = asd.split('"')[5]
                lm_sound_pure.append(bcd)

            ### 문장 url으로 mp3 다운받기
            for i in range(len(lm_sound_pure)) :
                link = lm_sound_pure[i]
                name = lm_new_list[i].replace('?','.').replace('"','')
                response = requests.get(link,headers=headers )
                with open(f'D:\OneDrive - knou.ac.kr\ANKI\Sound\{name}.mp3', 'wb') as f:
                    f.write(response.content)

            ### Cambridge 문장 추가적으로 불러오기
            more_sen = input("Cambridge 문장을 추가적으로 보고싶으면 a를 아니면 아무 키나 눌러주세요!")

            ### a누르면 Cambridge 문장 불러오기
            if  more_sen == 'a' : 
                print('')
                print('List of cambridge Sentence')
                for i in range(len(cam_remove)) : 
                    ist_name = cam_remove[i]
                    print(f'{i+1}. {ist_name}')

                k = input('원하는 문장 고르기')
                if '~' in k or '-' in k : 
                    l = k.split('~')
                    d = [int(a) for a in l]
                    p = list(range(d[0],d[1]+1))

                elif ',' in k :
                    l = k.split(',')
                    p = [int(a) for a in l]

                elif k =='``' :
                    p =[]    

                else :
                    p = [int(k)]

                cam_h = [a-1 for a in p]
                print(cam_h)                

    ########## Longman 단어가 0건 일 경우 Cambridge 단어 띄우기
        if len(lm_sound) == 0 :
            print('Cambridge 문장 리스트')
            print(f'Cambridge Example 추출 : {len(cam_remove)}개')

            ### Cambridge리스트 보여주기
            for i in range(len(cam_remove)) : 
                ist_name = cam_remove[i]
                print(f'{i+1}. {ist_name}')
            
            ### Cambridge리스트 선택하기
            if cam_remove :
                k = input('원하는 문장 고르기')
                if '~' in k or '-' in k : 
                    l = k.split('~')
                    d = [int(a) for a in l]
                    p = list(range(d[0],d[1]+1))
                elif ',' in k :
                    l = k.split(',')
                    p = [int(a) for a in l]
                elif k =='``' :
                    p =[]
                else :
                    p = [int(k)]

                cam_h = [a-1 for a in p]
                print(cam_h)

    ############### Cambridge 원하는 문장만 추출하기
        cam_new_list=[] 
        for i in cam_h : 
            j = cam_remove[i]
            cam_new_list.append(j)

    ### Anki에 단어 넣기
        if h or cam_h :
            save_location = input('어느 Deck에 넣을까요?')
            if not save_location =='``':
                time.sleep(0.6)
                pyautogui.hotkey('win','6')
                time.sleep(0.6)
                pyautogui.press(['esc'])
                pyautogui.press(['esc'])
                time.sleep(0.6)
                pyautogui.press(['a'])
                time.sleep(0.6)
                pyautogui.hotkey('shift','tab')
                time.sleep(0.6)
                pyautogui.press(['space'])
                pyautogui.write(save_location)
                time.sleep(0.6)
                pyautogui.press(['enter'])
                time.sleep(0.6)
                pyautogui.press(['tab'])
                time.sleep(0.6)
                pyperclip.copy(word)
                pyautogui.hotkey('ctrl','v')
                pyautogui.hotkey('ctrl','a')
                time.sleep(0.1)
                pyautogui.hotkey('ctrl','t')
                time.sleep(0.1)
                pyautogui.hotkey('ctrl','enter')
                time.sleep(4)
                pyautogui.press(['pgup'])
                pyautogui.press(['pgup'])
                time.sleep(0.3) 
                pyperclip.copy(word)
                pyautogui.hotkey('ctrl','v')
                pyautogui.press(['tab'])

        ### longman 문장 있어야 실행하도록 설정해놓음
                if h : 
                    for i in range(len(lm_sound_pure)) : 
                        link = lm_sound_pure[i]
                        name = lm_new_list[i].replace('?','.').replace('"','')
                        time.sleep(0.8)
                        pyperclip.copy(name)
                        pyautogui.hotkey('ctrl','v')
                        time.sleep(0.8)
                        pyautogui.press(['f3'])
                        time.sleep(0.8)
                        pyperclip.copy(name+'.mp3')
                        pyautogui.hotkey('ctrl','v')
                        time.sleep(0.8)
                        pyautogui.press('enter')
                        pyautogui.press('enter')
                        if i != 0 : 
                            pyautogui.press('enter')

        ### Cambridge 문장 있어야 실행하도록 설정해놓음
                if cam_h :  
                    for i in range(len(cam_new_list)) :
                        name_cam = cam_new_list[i]
                        pyperclip.copy(name_cam)
                        pyautogui.hotkey('ctrl','v')
                        time.sleep(0.8)
                        pyautogui.press('enter')
                        if i != 0 : 
                            pyautogui.press('enter')



# %%
a = [1,23]
if bool(a) == True :
    print(a)    


#%%

# for i in range(len(lm_remove_com)) :
#     k = lm_remove_com[i]
#     print(f'{i}. {k}')

# print('----------------------------------')
# print('----------------------------------')
# print('----------------------------------')
te =[]
for i in range(len(lm_example)) : 
    p = lm_example[i]
    k = str(p)
    a = 'Play Example'
    if a in k :
        te.append(p)
print(te)
lm_sound_pure = []
for i in range(len(te)) : 
    asd = str(te[i])
    bcd = asd.split('"')[5]
    lm_sound_pure.append(bcd)
    # print(k.find(a))
    # if k.find(a) :
print(lm_sound_pure)

# print(asd)
# for i in range(1) : 
#     p = asd[i]
#     a = 'Play Example'
#     print(type(p))al

# print()
# print(te)
# print(f'{i}. {k}')
    
#%%


if j in a :
    print('포함')

#%%
for i in range(len(lm_sound)) : 
    k = lm_sound[i]
    print(f'{i}. {k}')
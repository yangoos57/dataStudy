# find_all 에서 class 사용하기

- find_all(tag,class)
- find*all(class*='name')

```python
bookTitle: str = kyoboSoup.find_all('span','prod_title')[0].string
>>>'실무자를 위한 그래프 데이터 활용법'

contents = kyoboSoup.find_all(class_="prod_title")
```

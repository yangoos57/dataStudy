## 배경

데이터 분석에서 일상적으로 사용하는 fitering 함수 세가지를 소개한다. pandas는 다양한 filtering 방법을 지원하고 있는데, 이중 연산속도가 빠르고 가독성이 좋은 query, boolean masking, isin를 상황에 맞게 사용하는 방법을 설명한다.

## DataFrame.query()

query 함수는 filter용으로 안성맞춤인 것에 비해 사람들이 많이 쓰지 않는 기능이다. 보통은 100,000개 이상 row를 다룰 때 성능이 좋다고 알려져있는데, 성능보다는 어떤 조건으로 필터링을 했는지 직관적으로 알 수 있고, 코드를 짧게 쓸 수 있어 가독성이 좋아지는 점이 이 함수를 쓰는 주된 이유이다.
<br><br>

> ### 장점

- **필터링을 단순하게 표현할 수 있다.**

  ```python
    import pandas as pd
    import numpy as np

    # row 100만개, column 3개 df 생성
    df = pd.DataFrame(10+60.5*np.random.randn(1000000,3))
    df.columns = ['num','num2','num3']
    pd.set_option('float_format', '{:f}'.format)
    df.describe()

    # +-------+-------------+-------------+-------------+
    # |       |         num |        num2 |        num3 |
    # +-------+-------------+-------------+-------------+
    # | count |   1000000   |   1000000   |   1000000   |
    # +-------+-------------+-------------+-------------+
    # |  min  | -282.352587 | -287.677283 | -300.389316 |
    # +-------+-------------+-------------+-------------+
    # |  50%  |   9.997371  |  10.014887  |   9.953583  |
    # +-------+-------------+-------------+-------------+
    # |  max  |  308.740897 |  292.197571 |  294.566926 |
    # +-------+-------------+-------------+-------------+


    '''
    필터링 조건
    10 < num < 100
    0.5 < num2 < 10
    255 < num3 < 50
    '''

    # query
    result = df.query('10 < num < 100 & 0.5 < num2 < 10 & 25< num3 < 50')

    len(result)   >>>  3982


    # boolean mask
    BM = (df['num'] > 10) & (df['num'] < 100)
    BM2 = (df['num2'] > 0.5) & (df['num2'] < 10)
    BM3 = (df['num3'] > 25) & (df['num3'] < 50)
    result = df[BM & BM2 & BM3]

    len(result)  >>>  3982

  ```

<br>

- **검색용으로 훌륭하다.**

  ```python
  # 서울 공공데이터 지하철정보
  sub_station = pd.read_csv('\sub_station.csv',encoding='CP949')

  sub_station.query('역사명 == "김포공항"')

  ```

  <div>
  <style scoped>
      .dataframe tbody tr th:only-of-type {
          vertical-align: middle;
      }

      .dataframe tbody tr th {
          vertical-align: top;
      }

      .dataframe thead th {
          text-align: right;
      }

  </style>
  <table border="1" class="dataframe" style="margin-left : 10px">
    <thead>
      <tr style="text-align: right;">
        <th></th>
        <th>역사_ID</th>
        <th>역사명</th>
        <th>호선</th>
        <th>경도</th>
        <th>위도</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th>2</th>
        <td>4929</td>
        <td>김포공항</td>
        <td>김포골드라인</td>
        <td>126.801868</td>
        <td>37.562360</td>
      </tr>
      <tr>
        <th>88</th>
        <td>4207</td>
        <td>김포공항</td>
        <td>공항철도1호선</td>
        <td>126.801904</td>
        <td>37.561842</td>
      </tr>
      <tr>
        <th>130</th>
        <td>4102</td>
        <td>김포공항</td>
        <td>9호선</td>
        <td>126.802152</td>
        <td>37.561916</td>
      </tr>
      <tr>
        <th>352</th>
        <td>2513</td>
        <td>김포공항</td>
        <td>5호선</td>
        <td>126.801292</td>
        <td>37.562384</td>
      </tr>
    </tbody>
  </table>
  </div>

  <br>

- **한번에 여러 values를 검색할 수 있다.**

  Boolean mask는 하나의 조건문에 하나의 value만 검색 가능하다. 그러다보니 코드가 한도없이 길어질 수 있다. query는 column에서 찾고자 하는 value를 list나 array 등으로 묶어주기만 하면 간단하게 검색할 수 있다.

  ```python
      stations = ['김포공항', '신논현']
      sub_station.query('역사명 == @stations').sort_values(by='역사명',ascending=False)
      # @를 붙이면 변수 취급
  ```

  <div style='margin-left : 10px'>
  <style scoped>
      .dataframe tbody tr th:only-of-type {
          vertical-align: middle;
      }

      .dataframe tbody tr th {
          vertical-align: top;
      }

      .dataframe thead th {
          text-align: right;
      }

  </style>
  <table border="1" class="dataframe">
    <thead>
      <tr style="text-align: right;">
        <th></th>
        <th>역사_ID</th>
        <th>역사명</th>
        <th>호선</th>
        <th>경도</th>
        <th>위도</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th>107</th>
        <td>4125</td>
        <td>신논현</td>
        <td>9호선</td>
        <td>127.025060</td>
        <td>37.504598</td>
      </tr>
      <tr>
        <th>2</th>
        <td>4929</td>
        <td>김포공항</td>
        <td>김포골드라인</td>
        <td>126.801868</td>
        <td>37.562360</td>
      </tr>
      <tr>
        <th>88</th>
        <td>4207</td>
        <td>김포공항</td>
        <td>공항철도1호선</td>
        <td>126.801904</td>
        <td>37.561842</td>
      </tr>
      <tr>
        <th>130</th>
        <td>4102</td>
        <td>김포공항</td>
        <td>9호선</td>
        <td>126.802152</td>
        <td>37.561916</td>
      </tr>
      <tr>
        <th>352</th>
        <td>2513</td>
        <td>김포공항</td>
        <td>5호선</td>
        <td>126.801292</td>
        <td>37.562384</td>
      </tr>
    </tbody>
  </table>
  </div>

<br><br>

  <!-- * **직관적으로 좋고 대용량 자료라도 느리지 않다.** 
  
    pandas 공식문서에서도 처리속도를 빠르게 하는 방법중 하나로 query를 추천하고 있다.
    <br><br><br> -->

> ### 단점

- **for문을 써야하는 경우 처리속도가 느리다.**

  처리속도 관련해서는 boolean mask에서 다루겠다.

   <br>

- **사용가능한 문법이 제한된다.**

  사실 사용가능한 문법이 적을뿐이지 필요한 기능은 전부 갖추고 있다. 필터링이 필요한 대부분 상황은 query 하나로 해결가능하다. query 함수가 문법이 제한적인 이유는 처리절차 내에 eval() 함수를 사용하기 때문이다.

    <br>

  **These operations are supported by pandas.eval():**

  > - Arithmetic operations except for the left shift (`<<`) and right shift (`>>`) operators, e.g., `df + 2 * pi / s ** 4 % 42 - the_golden_ratio`
  >
  > - Comparison operations, including chained comparisons, e.g., `2 < df < df2`
  > - Boolean operations, e.g., `df < df2 and df3 < df4 or not df_bool`
  > - `list` and `tuple` literals, e.g., `[1, 2]` or `(1, 2)`
  > - Attribute access, e.g., `df.a`
  > - Subscript expressions, e.g., `df[0]`
  > - Simple variable evaluation, e.g., `pd.eval("df")` (this is not very useful)
  > - Math functions: `sin`, `cos`, `exp`, `log`, `expm1`, `log1p`, `sqrt`, `sinh`, `cosh`, `tanh`, `arcsin`, `arccos`, `arctan`, `arccosh`, `arcsinh`, `arctanh`, `abs`, `arctan2` and `log10`.

    <br>

  **This Python syntax is not allowed:**

  > Expressions
  >
  > - Function calls other than math functions.
  >
  > - `is/is not` operations
  >
  > - `if` expressionslambda expressions
  >
  > - `list/set/dict`comprehensions
  >
  > - Literal `dict` and `set` expressions
  >
  > - `yield` expressions
  >
  > Generator expressions
  >
  > - Boolean expressions consisting of only scalar values
  >
  > - Statements
  >
  > - Neither simple nor compound statements are allowed.
  >
  > - This includes things like `for, while, and if`.

  출처 : [Pandas 공식홈페이지](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#supported-syntax)

<br><br><br><br>

## boolean masking

> ### 장점

- **처리속도가 빠르다.**

  필터 함수를 한번만 사용한다면 세가지 중 어떠한 함수를 사용해도 체감상 차이가 없다. 하지만 데이터 분석을 하다보면 loop와 filter 함수를 함께 사용하는 경우가 많다.

  그런 경우에 boolean masking이 빛을 발한다. 아래 그래프는 row가 1200만개인 데이터를 가지고, 300번 반복처리한 결과이다. 단위는 초당 loop를 처리한 횟수이다.

  boolean masking은 초당 10회의 loop를 수행한 반면 query는 초당 5회로 연산속도가 2배나 차이난다. 연산속도가 중요하지 않을땐 query를 사용하고 그 외에는 isin과 boolean masking을 사용하면 효율적이다.

  <br>

  ![png](images/output1.png)

  <br><br>

> ### 단점

- **한 번에 하나의 필터링만 가능하다**  
  query나 isin은 같은 column 내에 있는 여러 value를 한번에 처리할 수 있다. 하지만 boolean masking은 values별로 일일히 변수를 만들어야한다. 보기엔 간단해 보여도 막상 쓰다보면 실수도 많이 발생하고, 조건을 자주 바꿔서 검색할때 불편함이 이만저만이 아니다.

  ```python
    # boolean mask
    BM1 = sub_station['역사명'] == '김포공항'
    BM2 = sub_station['역사명'] == '신논현'
    BM3 = sub_station['역사명'] == '여의도'
    BM4 = sub_station['역사명'] == '여의나루'
    BM4 = sub_station['역사명'] == '샛강'

    sub_station[BM1 | BM2 | BM3 | BM4].sort_values(by='역사명',ascending=False)
  ```

  <br><br> <br><br>

## Dataframe.isin(list())

> ### 장점

- **빠른속도로 여러 value를 한 번에 처리할 수 있다.**

  isin은 query와 boolean mask의 중간 위치에있다. boolean mask가 가지고 있는 단점을 보완하며, query와 마찬가지로 하나의 column의 여러 value에 대한 처리가 가능하다. boolean mask보다는 처리속도가 느리지만 query보다는 빠르다.

  ```python
    stations = ['김포공항', '신논현','여의도','여의나루']

    # query
    sub_station.query('역사명 == @stations').sort_values(by='역사명',ascending=False)


    # isin
    BM = sub_station['역사명'].isin(stations)
    sub_station[BM].sort_values(by='역사명',ascending=False)


    # boolean mask
    BM1 = sub_station['역사명'] == '김포공항'
    BM2 = sub_station['역사명'] == '신논현'
    BM3 = sub_station['역사명'] == '여의도'
    BM4 = sub_station['역사명'] == '여의나루'
    sub_station[BM1 | BM2 | BM3 | BM4].sort_values(by='역사명',ascending=False)
  ```

    <div style='margin-left : 10px'>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }

    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>역사_ID</th>
          <th>역사명</th>
          <th>호선</th>
          <th>경도</th>
          <th>위도</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>117</th>
          <td>4115</td>
          <td>여의도</td>
          <td>9호선</td>
          <td>126.924030</td>
          <td>37.521760</td>
        </tr>
        <tr>
          <th>338</th>
          <td>2527</td>
          <td>여의도</td>
          <td>5호선</td>
          <td>126.924357</td>
          <td>37.521747</td>
        </tr>
        <tr>
          <th>337</th>
          <td>2528</td>
          <td>여의나루</td>
          <td>5호선</td>
          <td>126.932901</td>
          <td>37.527098</td>
        </tr>
        <tr>
          <th>107</th>
          <td>4125</td>
          <td>신논현</td>
          <td>9호선</td>
          <td>127.025060</td>
          <td>37.504598</td>
        </tr>
        <tr>
          <th>2</th>
          <td>4929</td>
          <td>김포공항</td>
          <td>김포골드라인</td>
          <td>126.801868</td>
          <td>37.562360</td>
        </tr>
        <tr>
          <th>88</th>
          <td>4207</td>
          <td>김포공항</td>
          <td>공항철도1호선</td>
          <td>126.801904</td>
          <td>37.561842</td>
        </tr>
        <tr>
          <th>130</th>
          <td>4102</td>
          <td>김포공항</td>
          <td>9호선</td>
          <td>126.802152</td>
          <td>37.561916</td>
        </tr>
        <tr>
          <th>352</th>
          <td>2513</td>
          <td>김포공항</td>
          <td>5호선</td>
          <td>126.801292</td>
          <td>37.562384</td>
        </tr>
      </tbody>
    </table>
    </div>
  <br><br>

> ### 단점

- **가독성이 떨어진다.**
  isin 역시 boolean mask와 마찬가지로 필터링이 직관적이지 않다는 단점이 있다. 그래도 변수를 줄이는 장점이 있어서 boolean mask보다는 상대적 가독성이 좋다.
  <br><br><br><br>

## 정리

- 대부분 경우는 query를 사용하자. query로 구현할 수 없는 조건이거나 반복문과 함께 쓸 땐 isin 또는 boolean masking 중 선택하자.

- column에서 찾아야하는 value가 2개 이상일 경우 isin을 추천하며, 빠른속도가 필요하거나 하나의 value만 찾는 경우엔 boolean mask를 추천한다.

<br>

<div align="center">

|       함수       | 반복문 x | 반복문 0, 값 =1 | 반복문 0 , 값 > 1 |
| :--------------: | :------: | :-------------: | :---------------: |
|    **query**     |    O     |                 |         △         |
| **boolean_mask** |          |        O        |                   |
|     **isin**     |          |                 |         O         |

</div>

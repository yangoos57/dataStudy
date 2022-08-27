---
title: "ROC Curve와 Precision-Recall Curve 직접 그려보기"
date: 2022-05-11T13:47:07+09:00
image: "images/home/ML1.png"
Tags: ['Confusion Matrix','Data Visualization', Precision-Recall Curve, ROC Curve,Machine Learning,Matplotlip, Plotly]
draft: False
Description: '예시로 자주 활용되는 plot을 그려보는 시리즈의 첫 시작이다. ROC Curve, Precision-Recall Curve를 직접 그려보며 개념을 이해하고 시각화 하는 방법을 익히고 sklearn, pandas, matplotlib 등 data science 관련 툴에 익숙해지는 시간을 갖는다. 이 글은 Confusion matrix 개념에서부터 plot이 그려지는 과정, plot 해석, 예제 코드를 포함하고 있다.  '
Summary: '예시로 자주 활용되는 plot을 그려보는 시리즈의 첫 시작이다. ROC Curve, Precision-Recall Curve를 직접 그려보며 개념을 이해하고 시각화 하는 방법을 익히고 sklearn, pandas, matplotlib 등 data science 관련 툴에 익숙해지는 시간을 갖는다. 이 글은 Confusion matrix 개념에서부터 plot이 그려지는 과정, plot 해석, 예제 코드를 포함하고 있다.  '
---
<br>

>### ROC Curve와 Precision Recall Curve


{{< test tick="false" name="intro_curves" dir="\images\ML\plot\intro_curves"  >}}



<br>

## 이 글의 목적

Confusion matrix는 classification 유형에서 유용하게 사용되며 모델의 실질적인 성능을 판단하는데 매우 효과적이다. 이에 기반한 Roc Curve와 Precision Recall Curve는 Confusion matri를 보다 직관적으로 이해할 수 있도록 돕는다. 

이 글은 Confusion matrix 이해와 그래프를 해석, 그리고 그래프를 직접 그려보며 sklearn, numpy, matplotlib 등 관련 툴에 익숙해지는데 목적이 있다. 개념에 익숙하던 익숙하지 않던 예시 code를 보지 않고 직접 그래프를 그려보는 것을 권장한다. 직접 그리다보면 개념에 대해 잘못알고 있는 부분도 발견할 수 있고 알지 못하는 부분을 발견하게 된다. 이와 더불어 관련 툴에 익숙해지는 연습을 할 수 있다. 

![untitle](/ML/data_viz/main_2.jpg) 

<br>

## 예시로 Confusion matrix 이해하기

<!-- confusion matrix 공부를 하자마자 바로 이 글을 읽는 사람들은 거의 없겠지? 기억이 날듯말듯 할텐데 복습한다는 생각으로 간단히 공부해보자. confusion matrix를 한글로 배우는 사람이 있는지는 모르겠는데 나는 한국어로 된 용어는 잘 모르니까 영어로 쓸게. 그런 사람들은 영어로 된 용어에 익숙해진다고 생각하고 봐

<br>

Confusion matrix를 해석할 때 가장 먼저 염두에 두어야 하는 건 어디가 True lables인지 Predict lables인지 찾는거야. 처음 confusion matrix를 배우고 나서 혼란스러웠던게 그 부분이었어. sklearn에서 그렇고 여러 책들에서 x축을 predict lables로 y축을 True lables 쓰긴 하는데 종종 반대로 사용하는 경우도 있더라고. 축만 바뀌었을 뿐인데 마치 새로배우는 듯한 착각이 들더라. 아무튼 우리는 sklearn을 사용할테니까 x축은 predict labels, y축은 True labels로 배우자고.
<br><br><br><br>

### TP, TN, FP, FN

confusion matrix를 배우는 중에는 머리가 항상 간질긴잘 하는 것 같아. 알듯 모를듯 이해한듯 못한듯 하는 그런 느낌이 사람 묘한 기분들게 만드는거 같아. 나는 이해를 하지 못하면 암기가 전혀 안되는 사람이라 최대한 내가 이해한 바탕으로 여러분들도 이해할수 있도록 작성했어. 같이 머리가 간질간질 해보자.
<br><br>

Confusion matrix를 볼때 x축과 y축 먼저 보라했지? x축은 Predict labels, y축은 True labels야. 
그리고 하위 lables를 잘 기억해줬으면 좋겠어 그래야 TP,TN, FP,FN 같은 기초용어가 헷갈리지 않거든 True labels은 True or False야 사실이니까 boolean으로 표현 됐지. 반면 Predict labels는 Positive, Negative야. x축에도 Positive, Negative라고 쓰여있어도 True Flase로 이해하자. 그래야 헷갈리지 않아.
<br><br>

 그리고 P,N에 힘주고 읽어 . TP는 Positive 예측이 맞구나. TN은 Negative 예측이 맞구나. FP는 Positive 예측이 틀렸구나, FN은 Negative 예측이 틀렸구나. 이런식으로 예측이 맞냐 틀리냐를 기준으로 생각하면 나중에 헷갈리더라도 차근차근 생각해볼 수 있게 돼. 
<br><br><br><br> -->

<br>

> #### 최근 보이스피싱 사기가 급증함에 따라 경찰은 대대적인 단속에 나섰다. 서울 A 경찰청의 보이스피싱 전담팀은 12명의 용의자들을 조사한 뒤 보이스 피싱범일 가능성이 높은 순으로 나열하였다. 

![untitle](/ML/data_viz/main_5.png) 
{{< center >}}**우측으로 갈수록 범인이라는 확신이 증가한다.**{{< /center >}}

A 경찰청 전담팀은 누구까지를 범인으로 간주해야할지 의견이 엇갈리고 있다. 평소 신중에 신중을 가하는 전담팀장은 무고한 피해자를 발생시키지 않기 위해, 가장 확실하게 범인일 것 같은 용의자만 기소해야한다는 의견이다. 

그의 상관인 수사부장은 대대적인 단속에 나선만큼 어느정도 위험을 감수해야 한다는 입장이다. 

반면 관할경찰청장은 보이스 피싱으로 인한 피해자가 급증하고 있으며 경찰이 대대적에 단속에 나선 만큼, 범인을 최대한 색출하여 더이상 피해자가 발생하지 않도록 철저하게 조사해야 한다는 생각이다. 그는 무고한 피해자가 발생하더라도 대를 위해 감내해야 하는 부분이라 생각한다.
<br><br>

![untitle](/ML/data_viz/main_6.png)

위 그림은 어디까지를 범인으로 간주할지에 대한 전담팀장, 수사부장, 경찰청장 기준을 보여준다. 가장 신중한 전담팀장은 빨간색 기준으로 3명의 용의자만 기소해야한다는 의견이다. 수사부장의 생각은 파란색 기준으로 5명의 용의자를 기소해야한다는 의견이다. 범인 색출에 혈안이 된 경찰청장은 12명의 용의자 중 절반인 6명을 기소해야한다는 의견이다.

<br><br>

### TP, FP, TN, FN 짚고 넘어가기

![untitle](/ML/data_viz/main_4.png)

검은색은 범인 흰색은 범인이 아닌 평범한 시민이다. 팀장의 빨간선을 기준으로 용의자를 기소한다면 무고한 피해자 없이 3명의 범인을 색출하겠지만 남은 3은 기소되지 않는다. 부장의 파란선이 기준이라면 6명 중 4명을 기소하지만 그 과정에서 1명의 피해자가 발생한다. 경찰청장의 기준인 초록색 선은 범인 모두를 색출하지만 2명의 피해자가 발생하게된다. 이처럼 기소 기준은 절대적이지 않으며 특정 기준을 택해야하는 선택의 문제이다. 무고한 피해자가 발생하지 않기 위해서는 대신 범인 전체를 잡는걸 포기해야한다. 반면 범인 전체를 잡기 위해서는 무고한 피해자가 발생하는 것을 감내해야한다. 둘다 가질 순 없다.
<br><br> 

> ### True Positive와 False Positive
  True Positive는 범인으로 지목한 용의자가 실제로 범인인 경우이며 False Positive는 지목된 용의자가 범인이 아닌 경우이다. 

  <br>

  ▸ 전담팀장이 지목한 3명 중 3명이 실제 범인이므로 TP는 3, FP는 1이다.

  ▸ 수사부장이 지목한 5명 중 4명이 실제 범인이므로 TP는 4, FP는 1이다.

  ▸ 경찰청장이 지목한 8명 중 6명이 실제 범인이므로 TP는 6, FP는 2이다.

<br><br>

> ### True Negative와 False Negative
  True Negative는 범인으로 지목되지 않은 용의자가 실제로도 범인이 아닌 경우이며 False Negative는 지목된 용의자가 실제로는 범인인 경우이다.

  <br>

  ▸ 전담팀장이 지목하지 않은 9명 중 6명이 범인이 아니므로 TN은 6, FN은 3이다.

  ▸ 수사부장이 지목하지 않은 7명 중 5명이 범인이 아니므로 TN은 5, FN은 2이다.

  ▸ 경찰청장이 지목하지 않은 4명 중 4명이 범인이 아니므로 TN은 4, FN은 0이다.

<br><br>

{{< note title="Type 1 error와 Type 2 error" content=" 전담팀장의 생각은 무죄추정의 원칙과 동일하다. 두 관점 모두 실제 범인이 무죄가 될 경우를 감내하고서라도 무고한 피해자를 발생시키지 않는데 목적이 있다. 목적이 그런다한들 무죄인 사람이 유죄가 되는 경우가 없는 건 아니다. 이처럼 법정에서 범인이라 판단했지만 실제로는 범인이 아닌 경우를 Type 1 error, False Positive 또는 False alarm라 한다. 한편으로는 무죄 추정의 원칙으로 인해 실제 범인이 무죄를 받고 풀려나는 경우가 있다. 이를 Type 2 error 또는 underestimaition이라 한다. <br><br> Type 1 error와 Type 2 error는 confusion matrix에서 FP와 FN과 의미가 같다. Type 1 error의 경우 경찰의 판단(Precit)은 P이지만 예측이 틀렸으므로 FP가 되며,  Type 2 error의 경우 경찰의 판단(Precdict)은 N이지만 예측이 틀렸으므로 FN이 된다. 전담팀장의 생각은 Type2 error를 감수하고도 Type 1 error가 발생시키지 않겠다는 말로 표현할 수 있으며 경찰청장의 생각은 Type 1 error가 늘어나는 것을 감수하고도 Type 2 error를 줄이겠다는 말로 표현할 수 있다." >}}

<br><br>

### Precision과 Recall
  앞서 구한 값으로 Confusion matrix를 만들었다. Confusion Matrix를 읽을때는 label을 주의깊게 봐야한다. 지금 보이는 matrix는 X축이 예측 값이고 Y축이 실제 값이지만 X축과 Y축이 바뀐 confusion matrix도 자주 활용되며, 그런 경우 TP,FP,FP,FN 모두 뒤바뀌므로 주의하지 않는 한 잘못된 해석을 하게된다.

![untitle](/ML/data_viz/main_7.png)

  > ### Precision
  Precision은 예측한 값이 얼마나 잘 맞았는지에 관심있다. 즉 Positive로 예측한 것들 중에 실제로는 얼마나 맞췄는지에 관심있다. 

  <br>

  {{< center >}}$\frac{실제로 \\ True인 \\ 값}{P로\ 예측한\ 값} = \frac{TP}{TP+FP} = \frac{TP}{Predict \ Positive} ${{< /center >}}

  <br><br>

  ▸ 전담팀장의 Precision은 3명을 범인으로 예측했고(`P=3`), 3명 모두 범인(`TP=3`)이므로 100%이다.

  ▸ 수사부장의 Precision은 5명을 범인으로 예측했고(`P=5`), 4명이 범인이므로(`TP=4`) 80%이다.

  ▸ 관할청장의 Precision은 8명을 범인으로 예측했고(`P=8`), 6명이 범인이므로(`TP=6`) 75%이다.
  
  <br><br>

  > ### Recall
  Recall은 실제 True를 얼마나 찾았는지에 관심있다. 예측이 맞는지 틀리는지에는 관심 없다. 오로지 얼마나 찾았는지에 관심있다.

  <br>

  {{< center >}} $\large \frac{실제로  \ True인  \ 값}{전체 \ True} = \frac{TP}{TP+FN} = \frac{TP}{True}$ {{< /center >}}
  
  <br><br>

  ▸ 전담팀장의 Recall은 범인 6명 중(`T=6`) 실제론 3명만을 찾았기에(`TP=3`) 50%이다.

  ▸ 수사부장의 Recall은 범인 6명 중(`T=6`) 실제론 4명만을 찾았기에(`TP=4`) 67%이다.

  ▸ 관할청장의 Recall은 범인 6명 중(`T=6`) 실제로 6명을 찾았으므로(`TP=6`) 100%이다.

<br><br>

  > ### 종합

세명의 Precision과 Recall을 종합하였다.Precision이 높다면 Recall은 낮아지고 Recall이 높다면 Presion이 낮아지는 현상을 발견할 수 있다. Precision과 Recall은 한쪽이 높아지면 한쪽이 낮아지는 Trade off 관계임을 알 수 있다.
<br><br>

|      	| Precision 	| Recall 	|
|-------:	|------------:	|----------:	|
| 팀장 	|      100% 	|    50% 	|
| 부장 	|       80% 	|    67% 	|
| 청장 	|       75% 	|   100% 	|


<br><br><br>



## ROC Curve, PE/RC Curve 해석하기 
<br>

> ### 직관적인 이해를 방해하는 요소
Confusion matrix는 Classification 모델의 성능을 파악하는데 매우 유용한 도구이다. 하지만 데이터 분석에 익숙하지 않은 조직 구성원들과  Confusion matrix를 활용해 소통을 하기엔 어려움이 있다. 

용어를 처음 접하거나 익숙하지 않는 구성원들에게는 TP,TN,FP,FN과 같은 용어가 바로 와닿지 않으며 이를 응용한 용어들 또한 바로 이해하는데 어려움을 겪는다. 

ROC curve와 Precision recall curve를 이해하는데는 용어 말고도 그래프를 이해하는데 방해하는 추가적인 요소가 있다. 어쩌면 그래프를 이해하는데 있어 이 요소가 용어가 주는 어려움보다 더 클 수도 있다. 

그 생각은 바로 x가 변하고 난 뒤 y값이 변한다는 생각이다. 우리는 $y=ax^2+bx+c$와 같이 x값에 따라 y 값이 변하는 함수에 익숙하다. 하지만 우리가 그릴 그래프는 이러한 사고로 해석하려다보면 앞뒤가 맞지 않는 듯한 느낌을 받는다. Precision과 Recall은 기본적으로 trade off 관계이므로 반비례 관계가 성립되긴 하나 Recall이 변하기 때문에 Precision이 변하는 관계는 아니이기 때문이다. 

아래 그래프의 Threshold를 100%에서 0%로 천천히 옮겨보자. Threshold가 변하면서 Confusion matrix가 달라지게 되고, 그에따라 Precision과 Recall이 동시에 변하게 된다. 

Threshold는 앞서 설명한 예시에서 범인을 선정하는 기준이라고 보면 된다. 100% threshold는 100%라고 확신이 드는 범인이지 않는 한 범인으로 예측하지 않는다는 말이다. threshold가 점점 낮아지면서 범인으로 예측하는 수가 늘어나게 되고 0%에 도달해서는 모든 용의자를 범인으로 여기는 순간에 도달하게 된다. 

  {{< test tick="true" name="making_curve" dir="\images\ML\plot\making_curve" >}}


<br>

이처럼 confsion matrix에 기반한 그래프는 threshold가 변함에 따라 confusion matrix가 새롭게 계산되고 그에따라 PE/RC 또는 TPR/FPR이 계산된다. 따라서 x값이 변하면 y값이 변한다는 생각으로 그래프를 해석하려다보면 이해가 되는듯 하지만 앞뒤가 맞지않는 상황에 놓이게 되는 것이다. 

이러한점에 익숙한 구성원들과의 대화에는 confusion matrix와 관련 그래프가 매우 유용하게 사용될 수 있으나 익숙하지 않은 구성원들에게 이를 설명하고자 할 때는 이를 고려해 사전에 충분한 설명이나 차라리 다른 방법으로 설명해야한다.

confusion matrix를 보다 직관적으로 이해하고자 하는 시도로 lift classifier와 curmulative curve 등이 있지만 글의 주제와는 벗어나는 내용이므로 생략한다.

<br><br>


### ROC Curve

<br>


  > ### True Positive Rate = Sensitivity = Recall
  True Positive Rate는 전체 True 중에서 TP를 얼마만큼 식별했는지 관심이 있다. confusion matrix에서 가장 중요한 항목이 TP이다 보니 True Positive를 활용한 방법에는 여러 이름이 붙게되었다. True Positive Rate를 부르는 다른 중 자주 쓰이는 이름으로는 Recall, Sensitivity이 있다.  

  용어 이해를 위한 작은 팁을 주자면, 뒤에 Rate가 붙는 용어들 모두 True labels를 분모로 가진다. TPR은 전체 True 중(TP+FN) TP의 비율을 뜻하며 FPR은 전체 False 중(FP+TN) FP의 비율을 뜻한다. 

<br><br>


  > ### False Positive Rate
  
  FPR은 전체 False(FP+FN)에서 예측이 틀린 경우(FP)가 얼마나 되는지에 관심있다. 

  <br><br>

  > ### 그래프 해석

  그래프 시작인 Threshold = 100%인 상태는 어떤 값도 용의자도 범인으로 지목되지 않은 경우이다. Confusion matrix의 Positive 라인이 모두 (0,0)를 확인 할 수 있으며, 따라서 TPR과 FPR 모두 0이된다. 
  
  hreshold를 내릴수록 범인이라 판단하는 기준이 낮아지고, 범인으로 지목된 용의자가 많아지면서 TP와 FP 모두 증가한다. FPR과 TPR이 증가하고, 0% 까지 기준을 낮추면 결국 모든 값이 Predict로 이동하여 TPR과 FPR 모두 1에 도달한다.

   ROC Curve에서 우리가 관심있게 봐야하는 점은 FPR 대비 TPR의 변화량이다. 모델이 좋을수록 같은 FPR에서 더 높은 TPR을 갖게 된다.
   
   <br><br>

  {{< test tick="true" name="roc_curve" dir="\images\ML\plot\roc_curve" >}}
  


  <br><br>



  > ### 다른 모델과 비교하기

  이번엔 ROC Curve를 활용해 여러 모델을 비교해보자. 이번에는 전국에는 보이스 피싱 전담팀이 A팀 말고도 두 팀이 더 있다. B팀은 경찰청장 직속 팀이라 유능한 형사들로만 팀을 꾸렸고 C팀은 신설된지 얼마되지 않아 경험이 많이 없는 형사들이 주로 있는 팀이다. 
  <br><br>

  A팀 처럼 B팀,C팀도 12명의 용의자를 붙잡고 가장 범인일 것 같은 순으로 나열하였다. 
  <br><br>

  
  B팀의 예상과 실제 범인 분포이다.
    ![untitle](/ML/data_viz/main_8.png)


  C팀 예상과 실제 범인 분포이다. 
    ![untitle](/ML/data_viz/main_9.png)

  이렇게 나열한 그림만 본다면 어느 팀이 더 유능한 팀인지 분간하기 어렵다. A~C 세 팀 중 피해자 발생이 적으면서 최대한 많은 범인을 잡아내는 팀은 어디일까?

  ![untitle](/ML/data_viz/Roc_compare.png)

  A,B,C팀의 ROC Curve를 그려보니 어떤 팀의 성과가 좋은지 바로 확인된다. B팀은 FP Rate 0.2에서 이미 TP Rate가 1에 도달한다. 이에 비해 A팀과 C팀의 TP Rate는 현저히 낮다. 그러므로 B팀이 가장 능력있는 팀이다.


  <!-- <br><br>

  굳이 그래프를 그리지 않고도 모델 성능을 비교할 수 있다.
  누군가에게 설명하거나 지금처럼 연습하지 않는 이상 ROC Curve를 굳이 그릴 필요는 없다. AUC Score을 계산해서 가장 큰 값을 가진 모델이 가장 성능 좋은 모델이다. AUC(Area Under Curve)는 문자 그대로  커브 아래 파란색으로 칠한 면적을 의미한다. AUC가 높아지려면 y값이 빠르게 1에 도달해야 하기 때문에 모델 성능을 보여주는 좋은 지표가 된다. Sklearn에서 AUC를 계산하는 함수가 있으니 이를 사용해 모델 성능을 비교하면 된다.  -->
  <br><br><br>


### Precision-Recall Curve
ROC Curve는 실제 True를 얼마나 찾는지와 동시에 실수를 얼마나 적게 하는지를 그래프를 통해 파악한다면, PE/RC Curve는 모델이 얼마나 정확한 예측을 하는지를 그래프를 통해 파악한다. 
<br><br>

Precision은 모델의 정확도를 확인하는 좋은 지표이다. 하지만 예측 대비 정확도를 판단하는 Precision의 특성 상 판단 기준을 엄격하게 한다면(threshold를 높힌다면) 필연적으로 Precision을 올라갈 수밖에 없다. Precision이 90%인 모델이 실제로는 1000개 Instance 중 10개만을 Positive로 예측해서 나온 결과라면, 이 모델 좋은 모델인지 판단하기 어렵다. 
<br><br>

따라서 Precision을 지표로 활용하기 위해서는 단점을 보완해주는 Recall과 함께 사용해야한다. Recall은 실제 Positive 중 예측으로 실제 Positive를 식별한 경우이다. Recall에는 얼마나 많은 Instance를 예측했는지 설명할 수 있기 때문에 Precision과 함께 사용하면 모델의 예측 정확도를 파악할 수 있다.
<br><br>

PE/RC Curve도 ROC Curve와 마찬가지로 Treshold 변화에 따라 그래프가 그려진다. 기준이 엄격할수록 Precision이 높아지게 되므로 1에서부터 시작하는데, 기준이 낮아질수록 실제 Positive가 포함된 instance와 그렇지 않은 instance가 함께 포함되므로 Precision이 낮아지게 된다. 기준이 낮아질수록 포함하는 instance 수가 증가하고 자연히 Recall도 높아지게 된다. 계속해서 Threshold를 낮춰가다가 0에 도달하게 되면 모든 값을 Positive로 예측하게 되면 Base rate에 도달하게 된다.

{{< test name="pe_rc_curve" dir="/images/ML/plot/pe_rc_curve" >}}

<br><br><br><br>


## 예시 Code
이제는 앞선 설명의 이해를 바탕으로 plot을 그려보자. 제공하는 code는 하나의 참고로서만 활용하고 스스로 그려봤으면 좋겠다. plot을 그려보면서 헷갈리는 개념이 무엇인지, plot을 그리려면 어떤 함수를 써야하는지, 어떤 type의 변수를 넣어야 함수가 작동하는지를 고민하다보면 개념과 실력 모두 내것이 될 수 있다. 
    
<br>


>### Titanic 데이터 불러오기
```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 로드 및 분할
a = sns.load_dataset('titanic')
raw_data = a.drop(columns=['alive','who','deck']).dropna()
data = raw_data.drop(columns='survived')
target = raw_data['survived']
```
    
<br><br>


>### 인코딩
```python
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

#encoding
ordinal = OrdinalEncoder()
ordinal_col = ['pclass','sex','embarked','class','adult_male','embark_town','alone']
standard = StandardScaler()
standard_col = ['age','sibsp','parch','fare']

preprocessing = ColumnTransformer([
    ('ordinal', ordinal, ordinal_col),
    ('standard', standard,standard_col)
])
```
    
<br><br>


>### Logistic Regression으로 모델 학습
plot을 그리는게 주목적이므로 Cross_validaion은 생략했다. 


```python
#모델 학습
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
model = make_pipeline(preprocessing, LogisticRegression())
model.fit(data,target) 

# 모델 성능 및 base_rate 확인
print(f'logistic : {model.score(data,target)}')
print(f'base_rate : {target.mean()}')

# logistic : 0.8216292134831461
# base_rate : 0.4044943820224719
```


    
<br><br>


>### Sklearn 모듈에 있는 Confusion Matrix 활용
알고리즘에 따라 instance를 구분하는 방법이 다르다. logistic regression의 경우 확률을 활용해 대상을 구분한다면 SGDclassifier는 점수를 활용해 대상을 구분한다. 개별 instance별 확률 또는 점수를 알고 싶으면 .predict_proba 또는 .predict_score 함수를 사용하면 된다. 예시에는 Logistic regression을 활용했기 때문에 .predict_probar를 사용했다.

```python
from sklearn.metrics import confusion_matrix
proba_each_row = model.predict_proba(data) 
# predict_proba : instance별 예측 값 도출

thereshhold = 0.5 
con_max = confusion_matrix(y_true=target, 
                           y_pred=(proba_each_row[:,1] > thereshhold),
                           labels=[1, 0]) 
                           # labels=[1, 0] 넣은 이유 : 
                           # 0 = Negative, 1 = Positive를 의미하므로 
                           # label을 설정하지 않으면 Positive와 Negative가 바뀐체로 나온다.


# confusion matrix 시각화
sns.heatmap(con_max,
            xticklabels= ['positive','Negative'],
            yticklabels=['True','False'],
            annot=True, 
            cbar=False,
            cmap='Blues',
            fmt='g',
            annot_kws={'size':12}) 
plt.xlabel('Predict label',fontsize=18) 
plt.ylabel('True label',fontsize=18)
```    
![untitle](/ML/data_viz/ML1.png) 


    
<br><br>

>### Sklearn 모듈에 있는 ROC Curve와 Precision_Recall Curve 사용
```python
from sklearn.metrics import roc_curve
from sklearn.metrics import precision_recall_curve

# ROC Curve 자료생성
fpr_logistic,tpr_logistic,thresholds_logistic = roc_curve(y_true=target, 
                                                          y_score=proba_each_row[:,1])

# Precision-Recall Curve 자료생성
pr_logistic,rc_logistic, pr_rc_thre_logistic = precision_recall_curve(y_true=target,
                                                                      probas_pred=proba_each_row[:,1])
```

<br><br>

>### ROC Curve와 Precision-Recall Curve 그리기
```python


plt.style.use('ggplot')
plt.figure(figsize=(14,8))

## ROC Curve 그리기
plt.subplot(121)
plt.plot(fpr_logistic,tpr_logistic,linewidth=2)
plt.title('ROC CURVE',fontsize=18,fontweight="bold",y=1.05)
plt.fill_between(fpr_logistic,tpr_logistic, facecolor='blue',alpha=0.1)
plt.text(0.55,0.4, 'AUC', fontsize=30)

# styling figure
plt.xlabel('False Positive Rate',fontsize=16,labelpad=13,)
plt.ylabel('True Positive Rate',fontsize=16,labelpad=13)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.plot([0,1],[0,1],'k--')
plt.xlim(-0.01,1.01)
plt.ylim(-0.01,1.01)



# Precision-Recall Curve 그리기
plt.subplot(122)
plt.plot(rc_logistic,pr_logistic)
base_rate = target.mean()
plt.plot([0,1],[base_rate,base_rate],'k--')

#styling figure
plt.title('Precision \ Recall Cureve',fontsize=18,fontweight="bold",y=1.05)
plt.xlabel('Recall',fontsize=16,labelpad=13)
plt.ylabel('Precision',fontsize=16,labelpad=13,)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlim(-0.01,1.01)
plt.ylim(base_rate-0.05,1.01)


plt.tight_layout()
```
    
![untitle](/ML/data_viz/main_1.png) 














<!-- ## 목차
* Confusion Matrix 이해 - 범인 찾기
* Roc Curve 및 Precision Recall Curve 해석
* 예시 Code

<br><br>

이런 장점에도 불구하고 데이터 분야 외 사람들과 소통할 때 confusion matrix를 알고 있는 사람이 아니고서 confusion matrix를 바탕으로 모델 성능을 설명하기에는 어려움이 따른다.

용어, 헷갈린다. 동의어가 많다.


두 그래프는 confusion matrix에서 모델 성능과 관련된 부분을 그린거라 confusion matrix를 이해하고 있는 사람들에게는 잘 활용돼 하지만 이게 단점이기도 해 직관적으로 이해되기에는 confusion matrix를 잘알아야 하고 용어도 잘 알아야해  근데 우리가 상대해야할 사람은 data를 잘 알고 있지 못하는 사람들이잖아. 그래서 이를 직관적으로 이해할수 있도록 약간 변형을 가한 그래프도 있어. 이 주제는 현재 페이지에 벗어나니까 다음에 다뤄보도록 할게
<br><br>




이 글의 목적은 궁극적인 목적은 단순해. ROC curve와 PE/RC Curve를 해석하는 방법을 배우고 직접 그려보면서 Confusion matrix 개념을 단단히 하는 것이지. 만약 Confuion Matrix와 관련 용어에 대해 익숙하다고 생각하는 사람 있다면 이 글을 읽기 전 2시간 정도 본인이 직접 그려보는 것을 추천해. 우리의 주된 목적은 Confusion matrix를 이해하는 것이지만 그래프를 그리려면 Sklearn과 matplotlib, seaborn과 같은 visualization tool을 잘 다뤄야 하거든. 그래서 직접 구현한 code별로 알았으면 좋겠거나 설명이 필요하다고 생각되는 부분에 있어서는 설명을 하고 넘어가려고 해. 
<br><br>

마지막으로 이 글을 단순히 개념을 파악하는데 있다고 생각하지 않았으면 좋겠어. 개념을 이해하는 것 뿐만 아니라 직접 모델도 만들어보고 visualization tool에도 익숙해지는 과정인거야. 그려려면 스스로 그래프를 그려보던 글을 읽으면서 하나씩 따라하며 그려보던 직접 해봐야해. 가장 빠른길이니까 믿고 따라와.
<br><br><br><br> -->




<!-- # 한 통계에 의하면 대한민국 왼손잡이 비율이 5%라고 한다. 대한민국 인구 중 무작위로 100명을 선발한다고 하면 평균 95명은 오른손잡이가 되겠다. 철수는 왼손잡이라서 평소 오른손 잡이 전용으로 만들어진 제품을 사용하면서 큰 불편함을 느꼈다. 이러한 불편한 덕분에 철수는 좋은 사업 아이디어를 떠올리게 됐다. 그는 왼손잡이 용품만 취급하는 쇼핑몰을 운영해 왼손잡이의 마음을 분석하고 사로잡겠다는 전략이었다. 

# 머신러닝에 관심많은 그는 사람들의 여러 특성을 종합해 왼손잡이를 예측하는 모델을 우선 개발하기로 결심한다. 최대한 많은 왼손잡이들에게 쇼핑몰을 홍보해 이윤을 극대화해야겠다는 생각 때문이었다. 하지만 그의 실력이 부족했던지 모델 정확도는 85% 이상을 넘지 못했다. 

# 마음을 바꿔 kaggle에 거액의 상금을 걸어 왼손잡이 문제를 해결하기로 결심한다. 그가 조건으로 내세웠던 가장 높은 정확도를 달성한 A 모델에게 상금이 돌아갔다. 철수는 94.8%의 정확도를 가진 모델을 가지고 왼손잡이를 찾아 마케팅을 진행하기로 했다. 

# 그가 생각하기론 아무리 94.8%라도 현실에는 오차가 크게 발생 할 수 있으므로 마케팅을 수행하는 대상의 약 80%까지가 왼손잡이일거라 예측하고 그중에서 30%는 쇼핑몰에 방문 할 거라 예상했다. 즉 아무리 낮아도 전체 마케팅 대상 중에서 24%정도는 쇼핑몰에 방문한다는 예측이었다.몇주 뒤 마케팅 결과 보고서를 받은 그는 충격을 금치 못했다. 마케팅 대상 중 1%만이 쇼핑몰에 방문했기 때문이었다. 

# 모델 정확도 94.8%를 찍은 A모델은 사실 모든 instance를 오른손잡이로 했고 94.8%의 높은 정확도가 나온 이유는 인구의 95%가 오른손잡이였을 뿐이었다.

# ### xxx
# Classification 문제에서 정확도는 모델의 성능을 확인하는 지표가 되기 어렵다. confusion matrix는 모델의 성능을 낫낫히(?) 파헤치는 아주 유용한 도구이다. ~~~~ -->
## 책 정리

14p

- Transformer는 뉴럴 아키텍쳐 기반으로 2017년에 구글이 만들었다.
- pre-train and fine-tune 개념을 NLP에 적용했다.
- Hugging Face는 Pretrained Model을 불러와 Fine-tune을 간편하게 하도록 돕는다.

25p

- Transformer와 ULMFiT의 개발은 Generative Pretrained Transformer(GPT)와 Bidrectional Encoder Representations from Transformers(BERT)의 탄생을 가져왔다.
- Unsupervised learning과 Transformer 아키텍쳐의 결합은 처음부터 모델을 개발할 필요가 없도록하면서도(손쉬운 활용이 가능하다는 의미) 최고의 성능을 보여줬다.
- 2017년 이후 파생되어 나오는 Transformers를 이해하기 위해서는 3가지 개념을 이해해야한다.
  - The encoder-decoder framework
  - Attention mechanisms
  - Trnasfer learning
- LSTM은 Recurrent Neural Network 기반의 모델이며 Transformer 이전 가장 최신 모델이었다.
  - RNN 모델은 backpropagation을 통한 학습을 진행한다.
- RNN은 이전 단계의 정보를 기억(추적) 할 수 있고 output을 생성하기 위해서 해당 정보를 활용할 수 있다.

### The encoder-decoder framework

- Encoder : input 값을 numerical representation으로 바꾸는 것. The last hidden state라고도 불림
- Decoder : 과정이 끝난 numerical representation을 다시 원래 input 타입으로 같이 반환
- 문제 : the final hidden state의 information bottleneck 발생 | _State로 compressing 하는 과정에서 정보가 유실되는 문제 발생(이해 필요)_
- 해결 : 모든 encoder의 hidden state를 decoder에게 개방하는 방식으로 문제 해결, 이를 Attention이라 부름

### Attention Mechanisms

- encoder-decoder 문제 해결하는 아이디어 : input sequence에 대한 개별 single hidden state를 두는 대신, _매 단계마다 encoder를 만들어서 decoder가 접근하게 만든다.(encoder들을 단계별로 묶는다는 말인가)_ 이런 과정을 진행하다보면 decoder에게 한번에 많은 input이 들어가게 되고 이에 따라서 어느 states를 써야할지에 대한 우선순위 선정을 필요로 했다.
- 우선순위 선정을 돕는 매커니즘이 Attention임.
- _개별 Output을 선정하는 단계에서 Attention을 통해 모든 state를 사용할 수 있도록 했고 그결과 nontrivial alignments를 배웠다고 한다.(무슨 말이지?)_
- Attention은 모델이 아니고 세부 절차와 같은 개념이었으므로 여전히 RNN 기반의 모델이었다. RNN 모델의 처리 방식은 squential이 기본이었기 때문에 parallelizing이 불가능했다고 한다.
- _Self-attention : 이해 못함 공부 필요_
- _FF NN도 공부 필요_

### Transfer Learning in NLP

- image processing에서는 이미 오래전부터 쓰인 방법
- 같은 데이터를 가지고 처음부터 학습한 모델과 기존 학습된 모델에 같은 데이터로 fine-tuning을 하는 경우 후자가 훨씬 좋은 성능을 보임
- ULMFiT에서 이러한 방식을 최초로 도입했음.

  - Pretraining : 이전 단어를 기반으로 다음에 올 단어를 예측하는 방법. Language modeling이라고 불림. labeled data가 필요 없기 때문에 매우 좋음
  - Domain adaptation : 도메인 형태소를 학습. language modeling 방법 사용
  - Fine-tuning : classifier로 만들고 싶으면 label 데이터를 학습시킴

- GPT : _Transformer 아키텍쳐의 decoder 파트만 사용(무슨 의미지)_ language model 적용
- BERT : _Transformer 아키텍쳐의 encoder 파트만 사용(무슨 의미지)_ masked language modeling 적용 | 랜덤하게 masked된 단어를 문장에서 예측하는 방식임. 단순히 뒷 단어 예측이 아니라 어느 공백 부분이라도 예측할 수 있도록 모델을 학습시킴

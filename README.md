# 2018CRA
summer project in CRA



동아리 프로젝트로 진행했던 프로젝트의 몇몇 코드를 직접 실행해볼 수 있게 만들었습니다.

실행환경은 아나콘다(jupyter notebook)입니다.



### calculateWordVector

단어간의 벡터 연산을 진행할 수 있는 코드입니다.

해당 코드를 실행하기 위해서는 gensim 라이브러리가 추가로 필요합니다. 해당 라이브러리가 없으신 분들은 하단의 명령어로 설치가 가능합니다.

```python
pip install gensim
```




연산을 진행하기 위해서는 python calculateWordVector.py [연산을 하려는 단어들] 을 실행하면 됩니다.

예시는 다음과 같습니다.




```python
python calculateWordVector.py 여배우-남자배우+남성
```

![img](https://lh5.googleusercontent.com/yzAl9Ot93M-9i0Bb9saDCaIFulNr8a02cNChHju-CPj350qbV7IdbGEGRQKLan0O2RQhSM4BPDRTpT-kczDeyfDqm2To-PpSjTgt4i7Cu7WFKiZTs-8HQtFUXrC00Yk9YCK6JZsp4fg)





### analyzeSentimental

주어진 문장의 감정(긍정/중립/부정)을 분석하는 코드입니다. 

문장을 input으로 넣으면 해당 문장의 감정을 분석해줍니다. 해당 코드를 실행하기 위해서는 라이브러리 gensim 외에도 konlpy와 pyTorch가 추가로 필요합니다.

해당 라이브러리는 마찬가지로 pip 명령어나 conda 명령어(아나콘다의 경우)로 설치할 수 있습니다.





### generateReview

generate할 문장들의 seed mode를 설정해주시면 128개의 랜덤문장이 생성되어 나옵니다.

seed mode에는 'noun', 'random', 'start' 가 있으며, 이외의 단어가 들어갈 경우에는 에러가 나니 유의해주시기 바랍니다.


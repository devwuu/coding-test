
## 수강 강의
* 인프런 - 입문자를 위한 코딩테스트 핵심(이론과 문제풀이) [Python]


## 자주 사용하는 패키지 또는 함수
```python
    
    # import
    from collections import Counter
    from collections import deque
    from collections import defaultdict
    import math

    # a와 b 중 큰 값
    max(a, b) 
    
    # a와 b 중 작은 값
    min(a, b)
    
    # 오름차순 정렬
    sorted([num1, num2]) 
    
    # 올림
    math.ceil(10.5)
    
    # 반올림
    math.round(10.5)
    
    # 내림
    math.floor(-10.5) # -11
    
    # 버림
    math.trunc(-10.5) # -10
    
    # 삼항연산자
    answer = [num1, num2] if num1 < num2  else [num2, num1]


```

## 자료구조
### 덱
```python
    # default 기준은 오른쪽에서 삽입/제거
    dq = deque([1,2,3,4])
    
    dq.pop() # 오른쪽에서 빼기
    dq.popleft() # 왼쪽에서 빼기
    
    dq.append(9) # 오른쪽에 추가하기
    dq.appendleft(9) # 왼쪽에 추가하기
```
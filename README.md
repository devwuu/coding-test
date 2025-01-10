
## 수강 강의
* 인프런 - 입문자를 위한 코딩테스트 핵심(이론과 문제풀이) [Python]

## 시간복잡도
* 입력값의 갯수가 100,000 **이상**일 경우 고려 대상이 됨
  * 최대 o(nlogn)
* 입력값의 크기도 문제 풀이시 고려되어야 함

## 정확도와 효율성
* 정확도 : 입력값의 갯수를 작게 해서 정확도 측정
  * 1,000개
* 효율성 : 입력값의 갯수를 크게 해서 종료 시간 측정
  * 100,000개 
  * 최대 o(nlogn)
* 최소한 둘 중 하나라도 만족할 수 있게 작성

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
    
    # between
    0 <= i + dx[d] < n and 0 <= j + dy[d] < n
    
    # 정렬
    # list, string, 등 iterable 하면 모두 사용 가능
    # 새로운 list 반환
    sorted(list) # ㅣist를 오름차순 정렬
    sorted(list, reverse=True) # ㅣist를 내림차순 정렬하
    
    # 기타
    list(str) # 문자열을 문자 배열로
    Count(str) # 문자열에 포함된 문자의 빈도, list 요소의 빈도
```

## 자료구조
### 리스트
* idx를 이용한 접근 : o(1)
* 중간 삽입 : o(n)
* 앞에서 삽입/삭제 : o(n)
* 끝에서 삽입/삭제 : o(1)
```python
    # 정렬
    # list 자체를 변경
    list.sort() # 오름차순
    list.sort(reverse = True) # 내림차순
    list.sort(key = lambda v : (v[0])) # 요소 v의 0번째 idx을 key로 오름차순 정렬, key가 동일하면 기존 순서를 유지함
    list.sort(key = lambda v : (-v[0])) # 요소 v의 0번째 idx을 key로 내림차순 정렬, key가 동일하면 기존 순서를 유지함
    list.sort(key = lambda v : (v[0], v[1])) # 요소 v의 0번째 idx을 key로 오름차순 정렬, key가 동일하면 v의 1번째 idx를 key로 오름차순 정렬
```

### 덱
* idx를 이용한 접근 : o(n)
* 중간 삽입 : o(n)
* 양쪽 끝에서 삽입/삭제 : o(1) 
```python
    # default 기준은 오른쪽에서 삽입/제거
    dq = deque([1,2,3,4])
    
    dq.pop() # 오른쪽에서 빼기
    dq.popleft() # 왼쪽에서 빼기
    
    dq.append(9) # 오른쪽에 추가하기
    dq.appendleft(9) # 왼쪽에 추가하기
```
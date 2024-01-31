# APS

## 완전 검색(Exhaustive Search)
- 완전 검색 방법은 문제의 해법으로 생각할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법
- Brute-force 혹은 generate-and-test 기법이라고도 불림
- 모든 경우의 수를 테스트한 후, 최종 해법을 도출
- 상대적으로 빠른 시간에 문제 해결(알고리즘 설계) 가능
- 일반적으로 경우의 수가 상대적으로 작을 때 유용
- 모든 경우의 수를 생성하고 테스트하기 때문에 수행 속도는 느리지만, 해답을 찾아내지 못할 확률이 작음
- 검정 등에서 주어진 문제를 풀 때, 우선 완전 검색으로 접근하여 해답을 도출한 후, 성능 개선을 위해 다른 알고리즘을 사용하고 해답을 확인하는 것이 바람직


- 많은 종류의 문제들이 특정 조건을 만족하는 경우나 요소를 찾는 것
- 또한, 이들은 전형적으로 순열, 조합, 그리고 부분집합과 같은 조합적 문제들과 연관된다.

### 고려할 수 있는 모든 경우의 수 생성하기
- 6개의 숫자로 만들 수 있는 모든 숫자 나열(중복 포함)
- <모든 경우의 순열 나열>

### 순열(Permutation)
- 서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열하는 것
- 서로 다른 n개 중 r개를 택하는 순열은 `nPr`과 같이 표현
- 그리고 nPr은 다음과 같은 식이 성립
```
nPr = n * (n-1) * (n-2) * ... * (n-r+1)
```
- nPn = n!이라고 표기하며 팩토리얼이라고 부름
- 다수의 알고리즘 문제들은 순서화된 요소들의 집합에서 최선의 방법을 찾는 것과 관련 있음
    - ex) TSP(Traveling Salesman Problem)
- N개의 요소들에 대해서 n!개의 순열들이 존재

### 순열 구현 - 반복문
- ex) {1, 2, 3}을 포함하는 모든 순열을 생성
- nPr 에서 r은 반복문 수 결정
- 단 r이 가변적일 때는 재귀로 구현 가능
- 반복문을 통한 순열 생성
```
for i from 1 to 3
    for j from 1 to 3
        if j != i then
            for k from 1 to 3
                if k != i and k !- j then
                    print i, j, k
                end if
            end for
        end if
    end for
end for
```

- 재귀 호출을 통한 순열 생성
```
numbers[]: 순열 저장 배열
isSelected[]: 인덱스에 해당하는 숫자가 사용 중인지 저장하는 배열
perm(cnt) // cnt: 현재까지 뽑은 순열 수의 개수(자리수)
    if cnt == 3
        순열 생성 완료
    else
        for i from 1 to 3
            if isSelected[i] == true then continue
            numbers[cnt] <- i
            isSelected[i] <- true
            perm(cnt+1)
            isSelected[i] <- false
        end for
```
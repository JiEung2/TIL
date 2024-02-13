## 순열 응용 - 비트마스킹 순열
nPn -> n! 경우의 수

## 순열
- 서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열하는 것
- 서로 다른 n개 중 r개를 택하는 순열은 아래와 같이 표현  
    nPr
- 그리고 nPr은 다음과 같은 식이 성립  
    nPr = n * (n-1) * (n-2) * ... * (n-r+1)
- nPn = n!라고 표기하며 Factorial이라 부름  
    n! = n * (n-1) * (n-2) * ... * 2 * 1


```java
import java.util.Arrays;
import java.util.Scanner;

// nPr
public class BitmaskingPermutationTest {

    static int N, R, input[], numbers[];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        R = sc.nextInt();
        input = new int[N];
        numbers = new int[R];

        for(int i = 0; i < N; i++){
            input[i] = sc.nextInt();
        }
        permutation(0, 0);
    }

    public static void permutation(int cnt, int flag){
        if (cnt == R) {
            System.out.println(Arrays.toString(numbers));
            return;
        }
        for(int i = 0; i < N; i++) {
           if((flag & 1<<i) != 0) continue;
           numbers[cnt] = input[i];
           permutation(cnt + 1, flag | 1 << i);
        }

    }

}
```

## 순열을 생성하는 방법 - Next Permutation
- 현 순열에서 사전 순으로 다음 순열 생성 - NextPermutation
- 알고리즘
    - 배열을 오름차순으로 정렬한 후 시작
    - 아래 과정을 반복하여 사전 순으로 다음으로 큰 순열 생성(가장 큰 내림차순 순열을 만들 때까지 반복)
        1. 뒤쪽부터 탐색하며 교환위치(i-1)찾기 (i: 꼭대기)
        2. 뒤쪽부터 탐색하며 교환위치(i-1)와 교환할 큰 값 위치(j) 찾기
        3. 두 위치 값(i-1, j) 교환
        4. 꼭대기 위치(i)부터 맨 뒤까지 오름차순 정렬
- **주의사항**
    - NextPermutation 사용 전에 숫자배열을 **오름차순으로 정렬하여 가장 작은 순열 한번 처리**
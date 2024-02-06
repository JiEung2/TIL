### 단순 연결 리스트 - 삭제연산
- 'A', 'B', 'C', 'D'를 원소로 갖고 있는 리스트의 'B' 노드를 삭제할 때
  1) 삭제할 노드의 앞 노드(선행노드) 탐색
  2) 삭제할 노드의 링크 필드를 선행노드의 링크 필드에 복사
  3) 삭제할 노드의 링크 필드에 Null 저장

### 단순 연결 리스트 응용 - 스택 구현
- 단순 연결리스트로 스택 자료구조 구현
- Push와 Pop에 적합한 삽입/삭제 알고리즘은?

```java
public class Node<T> {
    public T data;
    public Node<T> link;

    public Node(T data) {
        super();
        this.data = data;
    }
    public Node(T data, Node<T> link) {
        super();
        this.data = data;
        this.link = link;
    }
    @Override
    public String toString(){
        return "Node [data=" + data + ", link=" + link +"]"
    }
}

public interface IStack<E> {
    void push(E e);
    E pop();
    E peek();
    boolean isEmpty();
    int size();
}

public class SsafyStack<E> implements IStack<E> {
    
    private Node<E> top;

    public void push(E e){  // top으로 넣기
        top = new Node<E>(e, top)
    }

    public E pop(){
        if(isEmpty()) throw new EmptyStackException();

        Node<E> popNode = top;
        top = popNode.link;
        popNode.link = null;
        return popNode.data;
    }

    public E peek() {
        if(isEmpty()) throw new EmptyStackException();
        return top.data;
    }

    public boolean isEmpty(){
        return top == null;
    }

    public int size() { // 모든 노드를 순회하는 로직을 ㅗ작성(노드 순회 목적)
        int count = 0;

        for(Node<E> temp = top; temp != null; temp = temp.link) ++count;

        return count;
    }
}
```

## 이중 연결 리스트
- 특성
    - 양쪽 방향으로 순회할 수 있도록 노드를 연결한 리스트
    - 두 개의 링크 필드와 한 개의 데이터 필드로 구성
- 연결 구조  
    ![Alt text](List2-1.png)

### 이중 연결 리스트의 삽입 연산
- cur이 가리키는 노드 다음으로 D값을 가진 노드를 삽입하는 과정
    1) 새로운 노드 new를 생성하고 데이터 필드에 'D'를 저장
    2) cur노드의 next를 new노드의 next에 저장하여 cur의 다음노드를 new노드의 다음 노드로 연결

### 이중 연결 리스트의 삭제 연산
- cur이 가리키는 노드를 삭제하는 과정
    1) 삭제할 노드 cur의 next를 cur의 이전 노드 next에 저장하여 cur의 다음 노드를 cur의 이전노드의 다음 노드로 연결
    2) 삭제할 노드 cur의 prev를 cur의 다음노드의 prev에 저장하여 cur의 이전 노드를 cur의 다음 노드의 이전 노드로 연결
    3) 삭제할 노드 cur의 prev, next에 Null을 저장

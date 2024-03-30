public class Tree {
    static class Node {
        int data;   //노드 값
        Node left;  //왼쪽 자식 노드의 참조 값
        Node right; //오른쪽 자식 노드의 참조 값

        Node(int data){
            this.data = data;
        }
    }

    public static Node root; // root 노드
    public static void createNode(int data, int leftData, int rightData){
        if(root == null){   // root노드가 null이라면 root노드 생성
            root = new Node(data);

            if(leftData != -1){     //왼쪽 자식 데이터가 있는 경우 왼쪽 자식 노드 생성
                root.left = new Node(leftData);
            }
            if(rightData != -1) {   //오른쪽 자식 데이터가 있는 경우 오른쪽 자식 노드 생성
                root.right = new Node(rightData);
            }
        }else{  // 생성된 트리가 있다면 루트 노드 생성 이후 만들어진 노드 중 어떤 노드인지 찾아야함
            searchNode(root, data, leftData, rightData);
        }
    }

    public static void searchNode(Node node, int data, int leftData, int rightData){
        if (node == null) {
            return;
        } else if (node.data == data) {
            if (leftData != -1) {
                node.left = new Node(leftData);
            }
            if (rightData != -1) {
                node.right = new Node(rightData);
            }
        } else {    // 찾는 데이터가 아니고 탐색할 노드가 남아있다면
            searchNode(node.left, data, leftData, rightData);   //왼쪽 노드 탐색
            searchNode(node.right, data, leftData, rightData);  //오른쪽 노드 탐색
        }
    }

    public static void preOrder(Node node) {
        if (node != null) {
            System.out.print(node.data + " ");
            if(node.left != null) preOrder(node.left);
            if(node.right != null) preOrder(node.right);
        }
    }

    public static void inOrder(Node node){
        if (node != null) {
            if(node.left != null) inOrder(node.left);
            System.out.print(node.data + " ");
            if(node.right != null) inOrder(node.right);
        }
    }

    public static void postOrder(Node node){
        if (node != null) {
            if(node.left != null) postOrder(node.left);
            if(node.right != null) postOrder(node.right);
            System.out.print(node.data + " ");
        }
    }

    public static void main(String[] args) {
        createNode(0, 1, 2);
        createNode(1, 3, 4);
        createNode(2, 5, 6);

        System.out.println("전위 순회");
        preOrder(root);
        System.out.println();
        System.out.println("중위 순회");
        inOrder(root);
        System.out.println();
        System.out.println("후위 순회");
        postOrder(root);
        System.out.println();
    }
}

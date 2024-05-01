package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Node{
    int id;
    char ch;
    Node left, right;
    public Node(int id){
        this.id = id;
    }
}

class Tree{
    Node root = null;
    public void add(int id, char ch, int left, int right){
        if (root == null) {
            root = new Node(id);
            root.ch = ch;
            if (left != 0) {
                root.left = new Node(left);
            }
            if (right != 0) {
                root.right = new Node(right);
            }
        }
        else{
            search(root, id, ch, left, right);
        }
    }

    public void search(Node now, int id, char ch, int left, int right){
        if(now.id == id){
            now.ch = ch;
            if(left != 0){
                now.left = new Node(left);
            }
            if(right != 0){
                now.right = new Node(right);
            }
        }
        else{
            if (now.left != null) {
                search(now.left, id, ch, left, right);
            }
            if (now.right != null) {
                search(now.right, id, ch, left, right);
            }
        }
    }

    public void inOrder(Node root){
        if (root.left != null) {
            inOrder(root.left);
        }
        System.out.print(root.ch);
        if (root.right != null) {
            inOrder(root.right);
        }
    }
}

public class SWEA1231 {
    static Tree tree;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for(int tc = 1; tc <= 10; tc++){
            int n = Integer.parseInt(br.readLine());
            tree = new Tree();
            for(int i = 0; i < n; i++){
                StringTokenizer st = new StringTokenizer(br.readLine());
                int left = 0, right = 0;
                int id = Integer.parseInt(st.nextToken());
                char ch = st.nextToken().charAt(0);

                if(st.countTokens() == 2){
                    left = Integer.parseInt(st.nextToken());
                    right = Integer.parseInt(st.nextToken());
                }
                else if(st.countTokens() == 1){
                    left = Integer.parseInt(st.nextToken());
                }

                tree.add(id, ch, left, right);
            }
            System.out.print("#" + tc + " ");
            tree.inOrder(tree.root);
            System.out.println();
        }
    }
}

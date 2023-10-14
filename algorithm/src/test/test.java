package test;
import java.util.*;
public class test {
    public static void main(String[] args) {
        String[] park = {"SOO","OOO","OOO"};
        String[] routes = {"E 2","W 2","W 1"};
        test t = new test();
        for(int x : t.solution(park, routes)) {
            System.out.println(x);
        }

    }
    public int[] solution(String[] park, String[] routes) {
        int[] answer = new int[2];
        int x=-1, y=-1;

        for(int i=0; i<park.length; i++){
            if(park[i].indexOf('S') != -1) {
                x = park[i].indexOf('S');
                y = i;
            }
        }
        System.out.println(x);
        System.out.println(y);

        for(int i=0; i<routes.length; i++){
            String[] tmp = routes[i].split(" ");
            String direction = tmp[0];
            int move = Integer.parseInt(tmp[1]);

            if(direction.equals("E")){
                boolean flag = true;
                for(int j=1; j<=move; j++){
                    if(park[0].length() <= (x+j)){
                        flag = false;
                        break;
                    }
                    else if(park[y].charAt(x+j) == 'X'){
                        flag = false;
                        break;
                    }
                }
                if(flag) x += move;
            }
            else if(direction.equals("W")){
                boolean flag = true;
                for(int j=1; j<=move; j++){
                    if(0 > (x-j) ){
                        flag = false;
                        break;
                    }
                    else if(park[y].charAt(x-j) == 'X'){
                        flag = false;
                        break;
                    }
                }
                if(flag) x -= move;
            }
            else if(direction.equals("S")){
                boolean flag = true;
                for(int j=1; j<=move; j++){
                    if(park.length <= (y+j) ){
                        flag = false;
                        break;
                    }
                    else if(park[y+j].charAt(x) == 'X'){
                        flag = false;
                        break;
                    }
                }
                if(flag) y += move;
            }
            else if(direction.equals("N")){
                boolean flag = true;
                for(int j=1; j<=move; j++){
                    if(0 > (y-j) ){
                        flag = false;
                        break;
                    }
                    else if(park[y-j].charAt(x) == 'X'){
                        flag = false;
                        break;
                    }
                }
                if(flag) y -= move;
            }
        }

        answer[0] = y;
        answer[1] = x;
        return answer;
    }

}

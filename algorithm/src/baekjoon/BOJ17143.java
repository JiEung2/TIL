package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ17143 {
    static class Shark {
        int r, c, s, d, z;
        boolean catched= false;
        boolean dead = false;

        public Shark(int r, int c, int s, int d, int z) {
            this.r = r;
            this.c = c;
            this.s = s;
            this.d = d;
            this.z = z;
        }
    }
    static int R, C, M, result;
    static int[] dx = {0, 0, 0, 1, -1};
    static int[] dy = {0, -1, 1, 0, 0};
    static int[][] map;
    static List<Shark> sharkList = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[R][C];

        for(int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            int z = Integer.parseInt(st.nextToken());
            sharkList.add(new Shark(r, c, s, d, z));
        }

        Collections.sort(sharkList, (s1, s2) -> s1.r - s2.r);
        solve();
        System.out.println(result);
    }

    public static void solve() {
        int loc = 0;
        while (loc++ < C) {
            for(int i = 0; i < sharkList.size(); i++){
                Shark s = sharkList.get(i);
                if (loc == s.c) {
                    result += s.z;
                    s.catched = true;
                    sharkList.remove(s);
                    System.out.println(s.z);
                    break;
                }
            }
            move();
        }
    }

    public static void move(){
        for(int i = 0; i < sharkList.size(); i++){
            Shark s = sharkList.get(i);
            int tmp = s.s;
            int x = s.r;
            int y = s.c;
            while (tmp-- > 0) {
                int nx = x + dx[s.d];
                int ny = y + dy[s.d];
                if (nx >= 0 && nx < R && ny >= 0 && ny < C) {
                    x = nx;
                    y = ny;
                }
                else{
                    if (s.d == 1 || s.d == 3) {
                        s.d++;
                    }
                    else{
                        s.d--;
                    }
                    x = x + dx[s.d];
                    y = y + dy[s.d];
                }
            }
            s.r = x;
            s.c = y;
        }
        Collections.sort(sharkList, new Comparator<Shark>() {
            @Override
            public int compare(Shark o1, Shark o2) {
                if (o1.r - o2.r == 0) {
                    return o2.z - o1.z;
                }
                return o1.r - o2.r;
            }
        });
        eat();

    }

    public static void eat(){
        int tmpR = -1;
        int tmpC = -1;

        for(int i = 0; i < sharkList.size(); i++){
            Shark s = sharkList.get(i);
            if (s.r == tmpR && s.c == tmpC) {
                s.dead = true;
            } else {
                tmpR = s.r;
                tmpC = s.c;
            }
        }
        List<Shark> newList = new ArrayList<>();
        for(int i = 0; i < sharkList.size(); i++){
            if (!sharkList.get(i).dead) {
                newList.add(sharkList.get(i));
            }
        }
        sharkList = newList;
    }
}

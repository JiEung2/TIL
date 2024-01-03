package test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class test2 {

    public int solution(int[] nums) {
        int answer = nums.length / 2;
        int size = Arrays.stream(nums).distinct().toArray().length;
        if(size < answer)
            answer = size;
        return answer;
    }
}

package org.example;

import org.junit.jupiter.api.Test;
import static org.assertj.core.api.Assertions.assertThat;

public class QueryStringTest {

    // operand=11 -> 이렇게 QueryString은 하나의 key, value 값을 가지는 객체
    // 따라서 List로 여러 개 사용해야겠지?
    // List<QueryString>
    @Test
    void createTest() {
        QueryString queryString = new QueryString("operand1", "11");

        assertThat(queryString).isNotNull();
    }
}

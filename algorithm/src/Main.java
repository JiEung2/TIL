import java.lang.reflect.Field;

class MyClass {
    private final String name = "JiEung";
}

public class Main {
    public static void main(String[] args) throws Exception {
        // 1. 클래스 타입.class
        final Class<MyClass> class1 = MyClass.class;
        final Field declaredField = class1.getDeclaredField("name");

        final MyClass myClass = new MyClass();
        final String name = (String) declaredField.get(myClass);

        System.out.println("name = " + name);
    }
}
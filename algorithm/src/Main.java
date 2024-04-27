//import java.lang.reflect.Field;
//
//class MyClass {
//    private final String name = "JiEung";
//}
//
//public class Main {
//    public static void main(String[] args) throws Exception {
//        // 1. 클래스 타입.class
//        final Class<MyClass> class1 = MyClass.class;
//        final Field declaredField = class1.getDeclaredField("name");
//
//        final MyClass myClass = new MyClass();
//        final String name = (String) declaredField.get(myClass);
//
//        System.out.println("name = " + name);
//    }
//}

class Parent {
    int x = 100;
    Parent() {
        this(500);
    }

    Parent(int x) {
        this.x = x;
    }

    int getX() {
        return x;
    }
}

class Child extends Parent {
    int x = 4000;
    Child() {
        this(5000);
    }

    Child(int x) {
        this.x = x;
    }
}

public class Main {
    public static void main(String[] args) {
        Child obj = new Child();
        System.out.println(obj.getX());
    }
}
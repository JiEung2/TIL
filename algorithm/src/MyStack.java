//import java.util.Arrays;
//import java.util.EmptyStackException;
//import java.util.LinkedList;
//import java.util.Stack;
//
//public class MyStack<E> {
//    private static final Object[] EMPTY_ARRAY = {};
//    private static final int DEFAULT_SIZE = 10;
//    LinkedList
//    private Object[] array;
//    private int size;
//
//    public MyStack() {
//        this.array = EMPTY_ARRAY;
//        this.size = 0;
//    }
//
//    private void resize() {
//        if (Arrays.equals(array, EMPTY_ARRAY)) {
//            array = new Object[DEFAULT_SIZE];
//
//            return;
//        }
//
//        int arrayCapacity = array.length;
//
//        if (size == arrayCapacity) {
//            int newSize = arrayCapacity * 2;
//            array = Arrays.copyOf(array, newSize);
//
//            return;
//        }
//
//        if (size < arrayCapacity / 2) {
//            int newSize = arrayCapacity / 2;
//            array = Arrays.copyOf(array, Math.max(DEFAULT_SIZE, newSize));
//        }
//    }
//
//    public E push(E item) {
//        if (size == array.length) {
//            resize();
//        }
//
//        array[size] = item;
//        size++;
//
//        return item;
//    }
//
//    public E pop() {
//        if (size == 0) {
//            throw new EmptyStackException();
//        }
//
//        @SuppressWarnings("unchecked")
//        E object = (E) array[size - 1];
//
//        array[size - 1] = null;
//        size--;
//
//        resize();
//
//        return object;
//    }
//
//    @SuppressWarnings("unchecked")
//    public E peek() {
//        if (size == 0) {
//            throw new EmptyStackException();
//        }
//
//        return (E) array[size - 1];
//    }
//
//    public boolean isEmpty() {
//        return size == 0;
//    }
//
//    public int size() {
//        return size;
//    }
//}

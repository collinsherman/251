class ClassA {

    private GreeterInterface greeter;

    public void setGreeter(GreeterInterface greeter) {

        this.greeter = greeter;
    }

    public void invokeGreeter() {

        this.greeter.sayHello();
    }

    public static void main(String [] args) {

        ClassA a = new ClassA();

        ClassB b = new ClassB();

        a.setGreeter(b);

        a.invokeGreeter();
    }
}

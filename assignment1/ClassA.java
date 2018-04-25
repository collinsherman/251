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

        a.setGreeter(new ClassB(){
            @Override
            public void sayHello(){
                System.out.println("\nHello Professor Levy!");
            }
        });

        a.invokeGreeter();
    }
}

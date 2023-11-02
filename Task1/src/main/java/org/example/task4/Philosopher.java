package org.example.task4;
import java.util.Random;
public class Philosopher extends Thread {

    private int id;
    private Fork leftFork;
    private Fork rightFork;
    private Random random = new Random();

    public Philosopher(Fork leftFork, Fork rightFork, int id) {
        this.leftFork = leftFork;
        this.rightFork = rightFork;
        this.id = id;
    }

    public void run() {
        while (true) {
            if (random.nextBoolean()) {
                rightFork.pickUp();
                leftFork.pickUp();
            } else {
                leftFork.pickUp();
                rightFork.pickUp();
            }
            // eating
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
            System.out.println("Philosopher nr " + id + " has finished eating");
            rightFork.putDown();
            leftFork.putDown();
        }
    }
}

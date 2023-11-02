package org.example.task5;

public class Philosopher extends Thread {

    private int id;
    private Fork leftFork;
    private Fork rightFork;
    private Arbitrator arbitrator;

    public Philosopher(Fork leftFork, Fork rightFork, int id, Arbitrator arbitrator) {
        this.leftFork = leftFork;
        this.rightFork = rightFork;
        this.id = id;
        this.arbitrator = arbitrator;
    }

    public void run() {
        while (true) {
            arbitrator.acquire();
            leftFork.pickUp();
            rightFork.pickUp();
            // eating
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
            System.out.println("Philosopher nr " + id + " has finished eating");
            leftFork.putDown();
            rightFork.putDown();
            arbitrator.release();
        }
    }
}

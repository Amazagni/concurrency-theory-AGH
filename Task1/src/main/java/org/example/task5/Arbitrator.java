package org.example.task5;

public class Arbitrator {
    private int currentNumber;

    public Arbitrator(int startingNumber) {
        this.currentNumber = startingNumber;
    }

    public synchronized void acquire() {
        while (currentNumber <= 0) {
            try {
                wait();
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
        currentNumber--;
    }

    public synchronized void release() {
        currentNumber++;
        notify();
    }
}

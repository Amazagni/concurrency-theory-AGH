package org.example.task6;

public class Arbitrator {
    private int currentNumber;

    public Arbitrator(int startingNumber) {
        this.currentNumber = startingNumber;
    }

    public synchronized boolean acquire() {
        boolean hadToWait = false;
        while (currentNumber <= 0) {
            try {
                hadToWait = true;
                wait();
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }

        }
        currentNumber--;
        return hadToWait;
    }

    public synchronized void release() {
        currentNumber++;
        notify();
    }
}

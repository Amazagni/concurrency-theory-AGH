package org.example.task6;

public class Fork {
    private boolean inUse = false;

    public synchronized void pickUp() {
        while (inUse) {
            try {
                wait();
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
        inUse = true;
    }

    public synchronized void putDown() {
        inUse = false;
        notify();
    }
}
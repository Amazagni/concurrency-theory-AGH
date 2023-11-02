package org.example.task3;

public class Main {
    public static void main(String[] args) {
        int n = 3;
        Fork[] forks = new Fork[n];
        for(int i = 0; i < n; i++) {
            forks[i] = new Fork();
        }
        for(int i = 0; i < n; i++) {
            new Philosopher(forks[i], forks[(i + 1) % n], i).start();
        }
    }
}
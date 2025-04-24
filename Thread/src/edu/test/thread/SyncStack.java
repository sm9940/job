package edu.test.thread;

import java.util.Vector;

public class SyncStack {

    private Vector buffer = new Vector(400, 200);

    public  char pop() {
    	while (buffer.size() ==0) {
			try {
				this.wait();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}	
    	
    	char c;
		synchronized(this){
    		c = (char) buffer.remove(buffer.size()-1);
    	}
    	return c;
    }

    public synchronized void push(char c) {
    	buffer.addElement(c);
    	this.notify();
	}
}

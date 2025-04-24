package test.thread;
public class TestThread {
public static void main(String[] args) throws InterruptedException {
   Runnable target = new Runnable(){

	@Override
	public void run() {
		System.out.println(Thread.currentThread()+"����Ǿ����ϴ�.");
		
	}};
   Thread cpu = new Thread(target);
   cpu.start();
   //Thread.yield();
  // Thread.sleep(20);
   cpu.join(); 
   System.out.println(Thread.currentThread()+"����Ǿ����ϴ�.");

	}

}

package test;

public class hello {

	  public static void main(String[] args) {

	    //Animal animal = new Dog(); // animal��Dog�����
	    Dog d = new Dog();
	    Animal a = d;
	    //animal.run(5);
	    //System.out.println(animal.i);
	    System.out.println("dog"+d.i);
	    System.out.println("a"+a.i);
	    a.run(5);
	    System.out.println(10|4);
	    
	    
	    
	    
	  }
	  
}
class Animal {
	  int i = 1;
	  public void run(int units) {
	    System.out.println("�ʪ�����" + units + "�B");
	  }
	}

	class Dog extends Animal {
		int i = 2;
	  @Override
	  public void run(int units){
	    System.out.println("�����]" + units + "�B");
	  }
	}
	
	
	
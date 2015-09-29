package org.demo;

import javax.xml.bind.annotation.XmlRootElement;

/**
 * The persistent class for the PERSON database table.
 * 
 */

@XmlRootElement(name="person")
public class Person {
	private static final long serialVersionUID = 1L;

	
	private int id;

	private int age;

	private String name;

	public Person() {
	}
	
	

	public Person(int id) {		
		this.id = id;
	}

	
	
	

	public int getId() {
		return this.id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public int getAge() {
		return this.age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	public String getName() {
		return this.name;
	}

	public void setName(String name) {
		this.name = name;
	}



	@Override
	public String toString() {
		return "Person [id=" + id + ", age=" + age + ", name=" + name + "]";
	}

	
}
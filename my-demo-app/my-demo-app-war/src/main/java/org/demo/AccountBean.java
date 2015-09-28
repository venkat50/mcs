/**
 * @author Copyright (c) 2008,2013, Oracle and/or its affiliates. All rights reserved.
 *  
 */
package org.demo;

import javax.ejb.EJB;
import javax.enterprise.context.SessionScoped;
import javax.inject.Inject;
import javax.inject.Named;

import java.io.Serializable;

/**
 * CDI Managed Bean Class
 */
@Named
@SessionScoped
public class AccountBean implements Serializable {

	@Inject
	PersonService ps;

	@EJB
	SequenceGenerator sg;

	private String name;

	private int age;
	private int id;

	private String msg;

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getMsg() {
		return msg;
	}

	public void register() {

		ps.addPerson(sg.getKey(), name, age);

		msg = "A new account with name " + name + " has been registered [" + ps.count() + "]";
	}

}

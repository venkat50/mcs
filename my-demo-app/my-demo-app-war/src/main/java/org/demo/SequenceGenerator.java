package org.demo;

import javax.ejb.Singleton;

@Singleton

public class SequenceGenerator {

	private static int key = 0;

	public SequenceGenerator() {
	}

	public int getKey() {
		return key++;
		
	}

}

package org.demo;

import com.tangosol.net.NamedCache;
import javax.annotation.Resource;
import javax.ejb.Stateless;

/**
 *
 * @author venkat
 */

@Stateless

public class PersonService {

    public PersonService() {
    }

    @Resource(mappedName = "Person")
    private NamedCache nc;

    //NamedCache nc = CacheFactory.getCache("Person");
    
    public void addPerson(int id, String name, int age) {
        Person p = new Person(id);    	
        p.setName(name);
        p.setAge(age);       
        nc.put(id, p);       
        
    }
    
    public int count(){
        return nc.entrySet().size();
    }    
    
}

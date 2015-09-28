package org.demo;

import com.tangosol.net.CacheFactory;
import com.tangosol.net.NamedCache;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import javax.annotation.Resource;
import javax.ejb.Stateless;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;

/**
 *
 * @author venkat
 */

@Stateless

public class PersonService {

    public PersonService() {
    }

    //@Resource(mappedName = "Person")
    //private NamedCache nc;

    NamedCache nc = CacheFactory.getCache("Person");
    
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

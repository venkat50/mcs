/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package org.demo;

import com.tangosol.io.pof.PofReader;
import com.tangosol.io.pof.PofSerializer;
import com.tangosol.io.pof.PofWriter;
import java.io.IOException;

/**
 *
 * @author venkat
 */
public class PersonSerializer implements PofSerializer {

    
    
    public void serialize(PofWriter writer, Object o) throws IOException {

        Person p = (Person) o;
        writer.writeInt(ID, p.getId());
        writer.writeString(NAME, p.getName());
        writer.writeInt(AGE, p.getAge());        
        //Very important to do that- it tells we are finished writing
        writer.writeRemainder(null);

    }

    public Object deserialize(PofReader reader) throws IOException {
        
        int id = reader.readInt(ID);
        Person p = new Person(id);
        p.setName(reader.readString(NAME));
        p.setAge(reader.readInt(AGE));
        //Very important to do that- it tells we are finished reading
        reader.readRemainder();
        return p;
    }
    
    public static final int ID = 0;
    public static final int NAME = 1;
    public static final int AGE = 2;
    

}

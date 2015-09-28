/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package org.demo;

import com.tangosol.io.pof.annotation.Portable;
import com.tangosol.net.AbstractInvocable;
import com.tangosol.net.CacheFactory;

/**
 *
 * @author venkat
 */
@Portable
public class MyAgent extends AbstractInvocable {

    public void run() {
            System.out.println(CacheFactory.getCluster().getClusterName());
    }
    
    
}

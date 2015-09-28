/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package org.demo;

import java.io.IOException;
import java.util.Iterator;

import javax.annotation.Resource;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.tangosol.net.CacheFactory;
import com.tangosol.net.Member;
import com.tangosol.net.NamedCache;

import javax.servlet.annotation.WebServlet;

/**
 * Servlet implementation class TestServlet
 */
@WebServlet(name = "TestServlet", urlPatterns = "/test")
public final class TestServlet extends HttpServlet {

	private static final long serialVersionUID = 1L;
	
	@Resource(mappedName = "Person")
    private NamedCache nc;

	/**
	 * @see HttpServlet#HttpServlet()
	 */
	public TestServlet() {
		super();
	}

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		// Get all Coherence cluster members
		Iterator<Member> members = CacheFactory.getCluster().getMemberSet().iterator();

		// Set output type
		response.setContentType("text/plain");
		
		response.getOutputStream().println("Cluster members");

		// Get details of all cluster members
		while (members.hasNext()) {
			response.getOutputStream().println("Member: " + members.next().toString());
		}
		
		response.getOutputStream().println(("Cluster Name: "+ CacheFactory.getCluster().getClusterName()));
		response.getOutputStream().println(("Product Name: "+ CacheFactory.PRODUCT + " Version: "+ CacheFactory.VERSION));
		
		response.getOutputStream().println("Cache entries");
		
		//NamedCache nc = CacheFactory.getCache("Person");
        Iterator entries = nc.entrySet().iterator();

        while (entries.hasNext()) {
            response.getOutputStream().println("Cache entry: " + entries.next().toString());
        }
		
		response.flushBuffer();
	}
}

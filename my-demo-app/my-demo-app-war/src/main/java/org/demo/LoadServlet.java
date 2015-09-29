package org.demo;

import java.io.IOException;
import java.util.stream.IntStream;

import javax.annotation.Resource;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.tangosol.net.NamedCache;

/**
 * Servlet implementation class LoadServlet
 */
@WebServlet(name="LoadServlet", urlPatterns="/load")
public class LoadServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	
	@Resource(mappedName = "Person")
    private NamedCache nc;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public LoadServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		IntStream.range(0, 50).forEach(k -> nc.get(k));
		response.getOutputStream().println("Loaded " + nc.size() + " entries");
	}

}

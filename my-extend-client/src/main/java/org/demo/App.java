package org.demo;

import java.util.Map;
import java.util.stream.IntStream;

import com.tangosol.net.CacheFactory;
import com.tangosol.net.InvocationService;
import com.tangosol.net.NamedCache;
import com.tangosol.util.QueryHelper;
import com.tangosol.util.filter.GreaterFilter;

/**
 * Hello world!
 *
 */
public class App {
	
	public static void main(String[] args) {

		NamedCache cache = CacheFactory.getCache("Person");
		/**
		 CacheFactory.getConfigurableCacheFactory() .getInterceptorRegistry()
		 .registerEventInterceptor(new MyInterceptor());
		**/
		System.out.println("Cache Name = " + cache.getCacheName() + " Cache Size = " + cache.size());

		IntStream.range(1, 25).forEach(k -> cache.get(k));

		System.out.println("Cache Name = " + cache.getCacheName() + " Cache Size = " + cache.size());

		cache.forEach((id, val) -> System.out.println("ID = " + id + " Name = " + ((Person) val).getName()));

		System.out.println(
				"Number of persons with Age Greater than 18 " + cache.entrySet(new GreaterFilter("getAge", 18)).size());

		System.out.println("Number of persons with Age Less than 18 "
				+ cache.entrySet(QueryHelper.createFilter("age < 18")).size());

		System.out.println(
				"Change Name " + cache.invokeAll(QueryHelper.createFilter("age < 20"), new NameUpdater("Test")));

		Person p = (Person) cache.get(1);
		System.out.println(p);
		p.setName("Name4");
		cache.put(4, p);

		cache.forEach((id, val) -> System.out.println("ID = " + id + " Name = " + ((Person) val).getName()));

		System.out.println("Cache Name = " + cache.getCacheName() + " Cache Size = " + cache.size());

		InvocationService service = (InvocationService) CacheFactory.getConfigurableCacheFactory()
			.ensureService("ExtendTcpInvocationService");

		Map map = service.query(new MyAgent(), null);

		
	}
}

import java.util.*;

class HashMapDemo{
	public static void main(String[] args) {
		HashMap <String, Integer> h = new HashMap<String,Integer>();
		h.put("A",10);
		h.put("B",20);
		h.put("C",30);
		System.out.println(h);
		System.out.println(h.get("C"));
		// put() will return the old value, that is replaced with new value, here 10.
		System.out.println(h.put("A",1000));
		//keySet() returns the set of keys
		Set s = h.keySet();
		System.out.println(s);
		Collection c = h.values();
		System.out.println(c);
		
		Set entries = h.entrySet();
		System.out.println(entries);

		//we'll be iterating over entry-set
		Iterator itr = entries.iterator();
		while(itr.hasNext()){
			//accessing the inner interface of Map i.e. Entry interface.
			Map.Entry m1 = (Map.Entry)itr.next();
			System.out.println(m1.getKey()+"---->"+m1.getValue());
			if(m1.getKey().equals("A")){
				m1.setValue(30390);
			}
		}
		System.out.println(h);
	}
}

/**
LinkedHashMap is also same as above HashMap 
the major difference is only that
the later one preserves the order
of Insertion.
*/
package com.hw;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Read {
	public Map Readflie() throws IOException {
		File srcFile = new File("C:\\Users\\linuix\\Desktop\\file.txt");
		InputStreamReader isr = new InputStreamReader(new FileInputStream(srcFile));
		            BufferedReader br = new BufferedReader(isr);
		            String line = br.readLine();
		            Map<String, Integer> map = new HashMap<String, Integer>();
		            Map<String, Integer> map2 = new HashMap<String, Integer>();
		            while (line != null) {
		            	String s[]=line.split("\\s+",2);
		            	String s2 =s[0];
		            	
		            	if(map.containsKey(s2)) {
		            		map.put(s2, map.get(s2)+1);
		            		if(map.get(s2)>=200) {
		            			map2.put(s2, map.get(s2));
		            		}
		            	}else {
		            		map.put(s2, 1);
		            	}
		            	line = br.readLine();
		            }
		            
		   return map2;
	}

}

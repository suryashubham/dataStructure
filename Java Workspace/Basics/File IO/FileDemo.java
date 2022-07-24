import java.io.*;

public class FileDemo{
	public static void main(String[] args) throws IOException {
		// this line will not create file rather chk if file exist it will point to that.
		File f = new File("Test.txt");
		try{
			f.createNewFile();
		}
		catch(Exception e){
			System.out.println("Error while cfreating file.");
		}
		//file object f can represent a directory also
		 File f1 = new File("TestDirectory");
		 f1.mkdir();
		 System.out.println(f1.exists());

		 //file f = new file(subDir,fileName); to create a file in a new sub-dir
		 File f3 = new File("TestDirectory","NewTestFile.txt");
		 f3.createNewFile();

		 //to list all the files
		 File f4 = new File(".\\TestDirectory");
		 String[] s = f4.list();
		 for(String s1:s){
		 	System.out.println(s1);
		 }
	}

}
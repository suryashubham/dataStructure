import java.io.*;

//Better to go for ProntWriter w.r.t. BufferedReader/writer
//To handle binary data(image,movoe,jar files) go for streams

public class PrintWriterDemo{
	public static void main(String[] args) throws IOException {
		File f = new File(".\\TestDirectory\\NewTestFile.txt");
		System.out.println(f.exists());

		FileWriter fw = new FileWriter(f);
		PrintWriter pw = new PrintWriter(fw);
		pw.println("Text inserted from a java program 1");
		pw.println("Text inserted from a java program 2");

		//TODO: appending data to the existing file.
		pw.flush();
		pw.close();
	}
}

//for reading file data go for PrintReader

//NOTE:
/*
when you write something to the stream, it is not written immediately
but it is buffered, meaning it is storedin the memory location in the
computer, the method flush() flushes all the stream of data and executes
them completely giving a new space to new stream.
*/
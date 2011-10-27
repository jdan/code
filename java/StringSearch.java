public class StringSearch {

	public static void main(String[] args) {
		System.out.println(search(args[0], args[1]));
	}

	static boolean search(String str, String str2) {
		if (str == null || str2 == null || str2.length() > str.length())
			return false;
		
		for (int a = 0; a <= str.length() - str2.length(); a++) {
			String compose = "";
			for (int b = 0; b < str2.length(); b++)
				compose += str.charAt(a + b);

			if (str2.equals(compose))
				return true;
		}

		return false;
	}
}

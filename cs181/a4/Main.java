/***********************************************************
 *
 * CS 181     
 *            Assignment 4 --- Command-line warping tool
 * 
 *            Main.java
 * 
 * (c) 2008   Stan Rosenberg
 * (c) 2008--10  Antonio R. Nicolosi
 *
 ***********************************************************/

/* When testing your code, make sure that issuing:

   $ java assign4.Main checkers.jpg 90 45

  on the file available at:

    http://www.cs.stevens.edu/~nicolosi/classes/10fa-cs181/assign4/checkers.jpg

  produces a file named 'warped_checkers.jpg' that looks like the file at:
 
    http://www.cs.stevens.edu/~nicolosi/classes/10fa-cs181/assign4/warped_checkers.jpg

*/

package assign4;

import java.awt.image.BufferedImage;
import java.awt.Point;
import javax.imageio.ImageIO;
import java.io.File;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
	String fileName = args[0];
	Point controlPt = new Point(Integer.parseInt(args[1]),
				    Integer.parseInt(args[2]));
	// read the input image
	BufferedImage image = ImageIO.read(new File(fileName));
	// extract width/height and pixels
	int width = image.getWidth();
	int height = image.getHeight();
	int[] pixels = image.getRGB(0, 0, width, height, null, 0, width);
	
	System.out.println("# of pixels = " + pixels.length);
	System.out.println("width = " + width);
	System.out.println("height = " + height);
	System.out.println("last pixel at " + (width-1 + (height-1)*width));
	// set-up a warping image transform
	ImageTransform imageTransform = new ImageTransform(pixels, width, height, controlPt);
	// apply transformation
	int[] dstPixels = imageTransform.transform();
	// update image pixels
	image.setRGB(0, 0, width, height, dstPixels, 0, width);
	// save the warped image
	ImageIO.write(image, "jpg", new File("warped_" + fileName));
    }
}

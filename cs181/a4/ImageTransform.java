/***********************************************************
 *
 * CS 181     
 *            Assignment 4 --- Command-line warping tool
 * 
 *            ImageTransform.java
 * 
 * (c) 2008   Stan Rosenberg
 * (c) 2008--10  Antonio R. Nicolosi
 *
 ***********************************************************/

package assign4;

import java.awt.Point;
import java.awt.Rectangle;

/*
 * Represents a warping image transform
 */
public class ImageTransform {
    // pixels of the source image (in row-major order)
    int[] srcPixels;
    // width & height of the source image
    int width;
    int height;

    // control point for the warping
    Point controlPt;

    int [] destPixels;

    // initialize image given in pixels whose scan-line is width-many pixels
    public ImageTransform(int[] srcPixels, int width, int height, 
			      Point controlPt) {
	this.srcPixels = srcPixels;
	this.width = width;
	this.height = height;
   	this.controlPt = controlPt;
    }

    /*
     * Perform the warping transformation:
     * The image is split into 4 quadrants (rectangle of equal area)
     * The control point defines 4 quadrilaterals. (Each quadrilateral
     * has one vertex corresponding to the control points. The remaining
     * vertices correspond to the rectangle in each quadrant.)
     * For each quadrant, we invoke warpRegion which maps the
     * quadrilateral into the rectangle.
     */
    public int[] transform() {
	// create the destination pixel array

	destPixels = new int[srcPixels.length];

	// quadrant 1
	warpRegion(destPixels, new Rectangle(0, 0, width / 2, height / 2), 
		   new Point(0, 0), new Point(width / 2, 0), 
		   controlPt, new Point(0, height / 2));

	// quadrant 2
	warpRegion(destPixels, new Rectangle(width / 2, 0, width / 2, height / 2), 
		   new Point(width / 2, 0), new Point(width, 0), 
		   new Point(width, height / 2), controlPt);

	// quadrant 3
	warpRegion(destPixels, new Rectangle(width / 2, height / 2, width / 2, height / 2), 
		   controlPt, new Point(width, height / 2), 
		   new Point(width, height), new Point(width / 2, height));

	// quadrant 4
	warpRegion(destPixels, new Rectangle(0, height / 2, width / 2, height / 2), 
		   new Point(0, height / 2), controlPt, 
		   new Point(width / 2, height), new Point(0, height));

	// return the result of warping transformation

	return destPixels;
    }

    /*
     * Given a rectangle, r, and a quadrilateral, represented by four vertices
     * (nw,ne,sw,se), map the quadrilateral into the rectangle.
    */
    protected void warpRegion(int[] dstPixels, Rectangle rect, 
			      Point nw, Point ne, Point se, Point sw) {
	System.out.println("Warping quadrilateral at ");
	System.out.println(nw);
	System.out.println(ne);
	System.out.println(se);
	System.out.println(sw);
	System.out.println("into rectangle");
	System.out.println(rect);
     
	for (int c = 0; c < rect.getWidth(); c++) {
	    for (int r = 0; r < rect.getHeight(); r++) {

		// portion of the line (CD/BA) that the point covers
		double ratio = Math.abs((double)c / rect.getWidth());

		// find point R'
		int rx = (int)(nw.getX() + (ne.getX() - nw.getX()) * ratio);
		int ry = (int)(nw.getY() + (ne.getY() - nw.getY()) * ratio);
		Point R_ = new Point(rx, ry);

		// find point Q'
		int qx = (int)(sw.getX() + (se.getX() - sw.getX()) * ratio);
		int qy = (int)(sw.getY() + (se.getY() - sw.getY()) * ratio);
		Point Q_ = new Point(qx, qy);

		// portion of the line QR that the point covers
		double ratio2 = Math.abs((double)r / rect.getHeight());

		// finally, find point P'
		int px = (int)(R_.getX() + (Q_.getX() - R_.getX()) * ratio2);
		int py = (int)(R_.getY() + (Q_.getY() - R_.getY()) * ratio2);
		Point P_ = new Point(px, py);

		destPixels[getIndex((int)rect.getX() + c, (int)rect.getY() + r)] = 
			   getPixel((int)P_.getX(), (int)P_.getY());
	    }
	}
    }

    /*
     * Return the pixel at (x,y)
     */
    public int getPixel(int x, int y) {
	return srcPixels[x + y*width];
    }

    public int getIndex(int x, int y) {
	return x + y * width;
    }

    /*
     * Extra-credit 1: Re-implement this to do color interpolation.
     * 
     * The idea of color interpolation is the following.  Say that you
     * want to access the fractionary pixel at coordinates (3.7,4.4). 
     * The default implementation (no color interpolation) just
     * truncates things and get the pixel at (3,4).  This is
     * unsatisfactory, because we are loosing the information encoded
     * in the fractional part: in particular, the pixel we wanted had
     * more overlap (42%) with (4,4) than with (3,4) (18%).
     *
     * Thresholdizing the "fractionary" pixel so that it agrees with the
     * "actual" pixel that maximizes overlap is a better option than the
     * default implementation, but it still is not very "smooth".
     * Instead, color interpolation averages the four real pixels that
     * have overlap with the fractionary pixel (in the example, these
     * are (3,4), (4,4), (3, 5), and (4,5)), weighting them by their
     * relative overlap ratio (respectively 18%, 42%, 12%, and 28%).
     *
     * A complication with interpolating pixels arises because of the
     * way colors are encode as Java int's.  In the RGB model, the
     * color of each pixel is described by three 8-bit unsigned
     * numbers, respectively for the red, green, and blue components
     * of the color (hence the name).  These three 8-bit unsigned are
     * packed together into a Java int as follows: the "blue" byte is
     * stored in the least-significant 8 bits of the int; the "green"
     * byte is stored in the 8 bits immediately to the left; and the
     * "red" byte is stored in the 8 bits further to the left.  (The 8
     * most-significant bits of the int do not matter under the RGB
     * color model.)
     * 
     * So in order to do color interpolation, you will have to do
     * bitwise manipulations to get to the right values; scale them by
     * the corresponding weights, yielding a floating-point value;
     * convert back to whole numbers; and pack the three components
     * back into the int.  You might want to define a helper class (or
     * at least some helper static methods) for carrying out this
     * "color arithmetic".
     * 
     */
    public int getPixel(double x, double y) {
	//Default implementation is no interpolation.

	return getPixel ((int) x, (int) y);

    }

    public int getDistance(int x, int y) {
	return (int)Math.sqrt(x*x + y*y);
    }
}

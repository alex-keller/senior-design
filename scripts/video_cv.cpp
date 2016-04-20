#include <opencv2/core/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui/highgui.hpp>

#include <iostream>
#include <string>

using namespace cv;

using namespace std;

int main( int agrc, int char** argv )
{
	string imagename("../scripts/image.jpg");
	if( argc > 1 )
	{
		imageName = argv[1];
	}
	
	Mat image;
	
	image = imread(imageName.c_str(), IMREAD_COLOR);

	if( image.empty() )
	{
		cout << "Could not open or find the image"
			<< std:endl;
		return -1
	}

	namedWindow( "Display Window", WINDOW_AUTOSIZE );
	imshow( "Display Window:, image);
	waitKey(0);
	return 0;
}

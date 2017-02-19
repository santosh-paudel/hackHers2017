#include "opencv2/opencv.hpp"
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
using namespace cv;

int main()
{
	namedWindow("Before",WINDOW_OPENGL);
	//namedWindow("After",WINDOW_AUTOSIZE);
	Mat img1;
	int index=102;
	string filename;
	while(true)
	{
		filename="filtered_frame"+to_string(index)+".jpg";
		img1 =imread(filename,1);

		if (img1.empty())
		{
			return -1;
		}
		imshow("After",img1);
		waitKey(300);
		index++;
	}


	return 0;
}


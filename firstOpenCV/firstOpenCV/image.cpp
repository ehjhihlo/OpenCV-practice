/*
#include<opencv2/core.hpp>
#include<opencv2/highgui.hpp>
using namespace cv;
int main(int argc, char* argv[]) {
    Mat img = imread(argv[1], IMREAD_ANYCOLOR);
    if (!img.data)
        return -1;
    waitKey(0);
    return 0;
}

*/

#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
using namespace cv;

int main()
{
    cv::Mat img = cv::imread("C:/Users/leo44/Desktop/相片/210209~11浸水營/IMG_0003.JPG");
    namedWindow("First OpenCV Application", WINDOW_AUTOSIZE);
    cv::imshow("First OpenCV Application", img);
    cv::moveWindow("First OpenCV Application", 0, 45);
    cv::waitKey(0);
    cv::destroyAllWindows();
    return 0;
}
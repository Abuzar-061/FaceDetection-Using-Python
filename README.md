# Real-Time Face Detection using OpenCV

This project demonstrates real-time face detection using OpenCV, a popular computer vision library. It utilizes a pre-trained Haar cascade classifier for detecting frontal faces in live video captured from a webcam.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/real-time-face-detection.git
    ```

2. Install the required Python dependencies:
    ```bash
    pip install opencv-python
    ```

3. Download the pre-trained Haar cascade classifier for face detection from [here](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) and place it in the project directory.

## Usage

1. Run the `face_detection.py` script:
    ```bash
    python face_detection.py
    ```

2. A window will open displaying the live video feed from your webcam, with detected faces outlined in green rectangles.

3. To terminate the program, press the "a" key.

## Acknowledgements

This project utilizes the following resources:
- [OpenCV](https://opencv.org/) - Open Source Computer Vision Library
- [Haar cascade classifier](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) for frontal face detection

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to customize and modify the code to suit your needs!

---

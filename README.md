# Google_Image_Search
<details>
  <summary>Table Content</summary>

  1. [About Project](#about-project)
  2. [Getting Started](#getting-started)
     - [Installation](#installation)
  3. [Data](#data)
  4. [Structure](@structure)
  5. [Results](#results)

</details>

### About Project <a name="about-project"></a>
- This project is a content-based image search system. It allows users to upload a test image and find similar images in the CBIR database

### Getting Started <a name="getting-started"></a>
- Installation<a name = "installation"></a> :
    + Tensorflow
    + Pillow
    + Matplotlib
### Data <a name="data"></a>
Use data CBIR (Kaggle):
- [Kaggle](https://www.kaggle.com/datasets/theaayushbajaj/cbir-dataset)
### Structure <a name="structure"></a>
- Use a deep learning model VGG16 to extract features from the image and represent them as feature vectors
![image](https://github.com/Bin2601/Google_Image_Search/assets/106230362/1f8eb772-24a7-40af-8f0d-1c48a6be44d3)
![image](https://github.com/Bin2601/Google_Image_Search/assets/106230362/831ec156-31f3-433f-8308-485f508abbb6)

- Create a database that contains feature vectors from sample images
- Compare the feature vector of the test image with the feature vectors in the database and find the most similar images
![image](https://global-uploads.webflow.com/5ef788f07804fb7d78a4127a/623c68cda43982d04d80a752_Engati-Euclidean-distance%20(1).jpg)
- Show a list of images that are similar to the test image to the user
### Results <a name="results"></a>
- I want find similar images images below:

![image](https://github.com/Bin2601/Google_Image_Search/assets/106230362/7f7a60fc-bd95-4875-993c-3764d8cb9a57)
- And that is results :
![image](https://github.com/Bin2601/Google_Image_Search/assets/106230362/f4b7b942-4451-490b-8748-afde3cf1d2d7)

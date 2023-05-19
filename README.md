# Restore split image

### Description

The program receives a scrambled image and rearranges it.

### Program inputs

1. Scrambled image:

    1.1 Image that is divided into square tiles (36x36 pixels each).

    1.2 Each tile is rotated by 90 degrees, either counterclockwise or clockwise.

2. DB:

   Sqlite DB that contains for every tile: its original position, new position, and direction of rotation.

### Program output
Rearanged image

### Installation

To install and run the Image Restoration Program locally, follow these steps:

1. Install Python 3.11.
2. Install pillow library with the command - $pip install pillow


### Usage

To restore a scrambled image using the Image Restoration Program:

1. You can replace the image and the database with your own, considering the limitations as described.
2. Run the program with the command $py RestoreImage.py
3. The program will process the image, display the restored version, and save it in your folder.

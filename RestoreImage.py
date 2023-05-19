from PIL import Image
import sqlite3


def get_db_data(dbPath, tableName):
    try:
        conn = sqlite3.connect(dbPath)
        cur = conn.cursor()

        cur.execute("SELECT * FROM {}".format(tableName))
        rows = cur.fetchall()

    except sqlite3.Error as e:
        print("Error getting database data")

    finally:
        conn.close()

    return rows


def open_img(fileName):
    try:
        return Image.open(fileName)
    
    except IOError:
        print("Image file not found")


def restore_img(originalImg, squaresData, pixlesSize):

    restoredImg = originalImg.copy()

    for sourceW, sourceH, destW, destH, direction in squaresData:

        rect = originalImg.crop(box=(destW * pixlesSize, destH * pixlesSize,
                                destW * pixlesSize + pixlesSize,  destH * pixlesSize + pixlesSize))

        if direction == 'counterclockwise':
            rectRotate = rect.rotate(90)
        else:
            rectRotate = rect.rotate(270)

        restoredImg.paste(rectRotate, box=(
            sourceW * pixlesSize, sourceH * pixlesSize))

    restoredImg.save("restoredImg.jpg")
    
    return restoredImg


def main():
    PIXLES_SIZE = 36
    TABLE_NAME = 'transform'
    DB_PATH = 'assignment.sqlite'
    IMAGE_NAME = 'assignment.jpg'

    squaresData = get_db_data(DB_PATH, TABLE_NAME)
    img = open_img(IMAGE_NAME)
    restoredImg = restore_img(img, squaresData, PIXLES_SIZE)
    restoredImg.show()


if __name__ == '__main__':
    main()

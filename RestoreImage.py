from PIL import Image
import sqlite3

def connect_db (sqliteName , dbName):
    try:
        # Connect to database
        conn = sqlite3.connect(sqliteName)
        # Create a cursor
        cur = conn.cursor()

        try:
            cur.execute("SELECT * FROM {}".format(dbName))
            # Get a list of Tuples that contains the data
            rows = cur.fetchall()
        
        except sqlite3.Error as e:
            print("Error executing the query")

    except sqlite3.Error as e:
        print("Error connecting to the database")
    
    finally:
         # Close the connection
         conn.close()

    return rows
    



def open_img (fileName):
    try:
        img = Image.open(fileName)
        return img
    except IOError:
        print ("Image file not found")
   




def restore_img (imgOriginal, db , sizePixles):
    imgRestore  = imgOriginal.copy()
    imgRestore.save("imgRestore.jpg")
   
    for sourceW,sourceH,destW,destH,direction in db:
         
         rect = imgOriginal.crop(box = (destW * sizePixles, destH * sizePixles, destW * sizePixles + sizePixles ,  destH * sizePixles + sizePixles))

         if direction == 'counterclockwise':
             rectRotate = rect.rotate(90)
         else:
             rectRotate = rect.rotate(270)

         imgRestore.paste(rectRotate,box = (sourceW * sizePixles, sourceH * sizePixles))

    imgRestore.save("imgRestore.jpg")
    return imgRestore






def main():
    sizePixles = 36
    dbRows = connect_db('assignment.sqlite' , 'transform')
    img = open_img('assignment.jpg')
    imgRestore = restore_img(img , dbRows , sizePixles)
    imgRestore.show()


    


if __name__ == '__main__':
    main()

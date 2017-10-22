from ImageComparator import ImageComparator

f = open("comparision", 'w')

for i in range (400, 600):
    file1 = "frames/frame" + "%d" % i + ".jpg"
    file2 = "frames/frame" + "%d" % (i + 1) + ".jpg"
    ic = ImageComparator(file1, file2)
    ic.load_images()
    ic.to_grayscale()
    result = ic.compare_images()
    print(result)
    stream = str(result[0]) + " " + str(result[1])
    stream = stream + "   frame%d" % i + "/frame%d" % (i + 1)
    print(stream)

    f.write(stream)
    f.write("\n")

f.close()

from PIL import Image
import subprocess

def cleanFile(filepath, newfilePath):
    image = Image.open(filepath)
    # 对图片进行阈值过滤，然后保存
    image = image.point(lambda x : 0 if x < 143 else 255)
    image.save(newfilePath)

    # 调用系统的tesseract命令对图片进行OCR识别
    subprocess.call(["tesseract", newfilePath, "p2_output"])

    # 打开文件读取结果
    outputFile = open("p2_output.txt", 'r')
    print(outputFile.read())
    outputFile.close()

cleanFile("p2.png", "p2_clean.png")

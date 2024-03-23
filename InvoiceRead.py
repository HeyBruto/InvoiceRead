import cv2
from pyzbar.pyzbar import decode
import time

def camera_read():
    ret, frame = cap.read()
    frame_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    codings = decode(frame_grey)
    mirror_frame = cv2.flip(frame, 1)
    cv2.imshow('Image', mirror_frame)

    for coding in codings:
        data = coding.data.decode("utf8")
        return data

def compare(exists, testdata):
    if testdata in exists:
        return 1
    else:
        return 0

def handle_invoice(invocie):
    try:
        invocie_s = invocie.split(",")
        print('发票代码：' + str(invocie_s[2]))
        print('发票号码：' + str(invocie_s[3]))
        print('开票日期：' + str(invocie_s[5]))
        print('发票金额：' + str(invocie_s[4]))
        print('校验码：' + str(invocie_s[6][-6:]))
    except:
        print("------非发票二维码，，请扫描下一张------")
        return

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)  # 默认摄像头为0 外置1,2,...
    exist = set()

    while True:  # 循环读取摄像头帧
        invoice_data = camera_read()
        if invoice_data is not None:
            if compare(exist, invoice_data):
                print("------已读取，请扫描下一张------")
            else:
                print(invoice_data)
                handle_invoice(invoice_data)
                exist.add(invoice_data)
            time.sleep(1)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

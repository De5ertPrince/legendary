# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import subprocess
import re
import requests
import json
import base64
import time
import picamera

# git clone https://github.com/AlexeyAB/darknet.git yolo/darknet
# cd darknet
# make


def send_sms(message_string, image_path):
    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = 'AC5cc646d74576ac20fab0bead25e31fc5'
    auth_token = 'ebb86c14da00dc51adf7abce75c89f0c'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
             body=message_string,
             from_='+15202140081',
             media_url=image_path,
             to='+15209063091'
         )


def run_yolo(pews_path, image_path, model_type):
    working_directory = pews_path + '/yolo'
    yolo_path = './darknet'
    if model_type == 'pews':
        data_path = 'pews.data'
        cfg_path = 'yolov3-tiny-pews.cfg'
        weights_path = 'backup/yolov3-tiny-pews_last.weights'
    else :
        data_path='cfg/coco.data'
        cfg_path='cfg/yolov3.cfg'
        weights_path='yolov3.weights'

    results = {}

    cmd = yolo_path + ' detector test ' + data_path + ' ' + cfg_path + ' ' + weights_path + ' ' + image_path
    print(cmd)
    got_results = False
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=working_directory)
    for line in p.stdout.readlines():
        line_decoded = line.decode('utf-8').rstrip()
        if got_results:
            if not line_decoded:
                got_results=False
            else:
                (label, pct) = line_decoded.split(' ')
                label = re.sub(':', '', label)
                pct = re.sub('%', '', pct)
                results[label] = pct
                # print(lineDecoded)
        else:
            out = re.findall(r"Predicted.*seconds", line_decoded)
            if len(out) > 0 :
                # print('MATCH: '+out[0])
                got_results=True
    retval = p.wait()
    return results

def take_photo(photo_path):  
    # Explicitly open a new file called my_image.jpg
    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(2)
        camera.capture(photo_path)
    # At this point my_file.flush() has been called, but the file has
    # not yet been closed

def is_predator(label):
    if label == 'coyote':
        return True
    if label == 'bobcat':
        return True
    if label == 'mountain_lion':
        return True
    if label == 'fox':
        return True
    if label == 'raccoon':
        return True
    if label == 'dog':
        return True
    if label == 'cat':
        return True
    return False


def upload_image(image_path):
    data = open(image_path, 'rb').read()

    res = requests.post(url='https://api.imgur.com/3/image',
                        data=data,
                        headers={'Content-Type': 'application/octet-stream',
                                 'Authorization': 'Client-ID 327e9a6fd44ce72'})

    # assert base64.b64decode(res.json()['data'][len('data:application/octet-stream;base64,'):]) == data
    print('Image uploaded to '+res.json()['data']['link'])
    return res.json()['data']['link']


def main():
    pews_path = '/home/pi/pews'
    image_path = '/tmp/camera_out.jpg'
    while True:
        take_photo(image_path)
        results = run_yolo(pews_path, image_path, 'pews')
        for label in results:
            print(label + ' was detected with ' + results[label] + ' confidence')
            if is_predator(label):
                print(label + ' IS A PREDATOR! ALERT THE AUTHORITIES!')
               output_image_path = upload_image(pews_path + '/yolo/predictions.jpg')
               message = 'THERES A  PREDATOR!!!!!!!!!!!!: ' + label + ' detected with '+ results[label] + '% confidence'
               send_sms(message, output_image_path)


if __name__ == "__main__":
    main()


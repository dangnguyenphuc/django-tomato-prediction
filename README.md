# Enviroment
* Python v3.11
* Packages:
```bash
pip3.11 install django
pip3.11 install keras
pip3.11 install opencv
pip3.11 install tensorflow
```

# Start server
```
cd <project/path>

python3.11 manage.py runserver 0.0.0.0:8000
```
* Note: you can change the IP:PORT above to another IP:PORT that you can access. Because the 0.0.0.0 is the Broadcast IP, then all the devices in the same submask net can access it.


# Server testing

* Store an image in ```convert_keras/test``` to your phone

* Request a GET METHOD to ```http://<url>/predict```. For example: If your phone has an IP Address 192.168.0.100 and your server has an IP Address 192.168.0.200, then if you want to request to server, this is the URL you need: 192.168.0.200

* Put that image in front of your device webcam and watch the magic happens.
apt-get -y update --fix-missing
apt-get -y  upgrade
apt-get install -y python3 cmake python3-pip python3-django python3-dev python3-opencv libatlas3-base libsz2 libharfbuzz0b libwebp6 libtiff5
dpkg --configure -a
apt autoremove -y
pip install -r requirements.txt
mkdir /temp
cp /home/user/Desktop/raspberrycontroller/raspidjango.service /lib/systemd/system/raspidjango.service
systemctl daemon-reload
systemctl start raspidjango.service
systemctl status raspidjango.service
journalctl -f -u raspidjango

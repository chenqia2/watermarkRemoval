# watermarkRemoval
sudo pip install virtualenv
virtualenv ~/personal/waterm

source ~/personal/waterm/bin/activate
pip install -U scikit-image
./watermark.py
deactivate
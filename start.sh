# shell command to enable bot to run on glitch.com

MD5="$(md5sum requirements.txt | cut -f1 -d' ')-site-packages"

if ! [ -d ".data/$MD5" ]; then
    rm -rf .data/*-site-packages
    pip3 install -U -r requirements.txt -t ".data/$MD5"
fi

exec env PYTHONPATH="$PWD/.data/$MD5" python3 main.py
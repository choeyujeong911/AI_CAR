sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak

sudo tee /etc/apt/sources.list >/dev/null <<'EOF'
deb https://ftp.kaist.ac.kr/debian bookworm main contrib non-free non-free-firmware
deb https://ftp.kaist.ac.kr/debian-security bookworm-security main contrib non-free non-free-firmware
deb https://ftp.kaist.ac.kr/debian bookworm-updates main contrib non-free non-free-firmware
EOF

sudo sed -i \
's|http://archive.raspberrypi.com|https://archive.raspberrypi.com|' \
/etc/apt/sources.list.d/raspi.list

sudo apt clean
sudo apt update

rm ~/AI_CAR/video/test.txt

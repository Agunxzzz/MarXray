clear
domain=$(cat /etc/xray/domain)

cd
curl -fsSL https://get.docker.com | sh
#wget -q -O /etc/nginx/conf.d/xray.conf "https://raw.githubusercontent.com/Agunxzzz/MarXray/main/xray.conf"
#sed -i 's/sg1.jateng.tech/${domain}/g' /etc/nginx/conf.d/xray.conf
rm -r /etc/nginx/conf.d/xray.conf
wget -q -O tesidom.sh https://raw.githubusercontent.com/Agunxzzz/MarXray/main/tesidom.sh && chmod +x tesidom.sh && ./tesidom.sh
sleep 1
rm -r /etc/nginx/nginx.conf
wget -q -O /etc/nginx/nginx.conf "https://raw.githubusercontent.com/Agunxzzz/Mina-Xray-SSH/main/conf/nginx.conf"
service nginx restart
cd
wget -qO- https://github.com/Gozargah/Marzban-examples/releases/latest/download/multi-port.tar.gz | tar xz --xform 's/multi-port/marzban/' && cd marzban
rm -r xray_config.json
wget -q -O /root/marzban/xray_config.json "https://raw.githubusercontent.com/Agunxzzz/MarXray/main/xray_config.json"
docker compose up -d
clear 
echo "Install telah selesai"
echo "Silahkan buka panel di http://domainmu:8880/dashboard"

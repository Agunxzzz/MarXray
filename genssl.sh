clear
domain=$(cat /etc/xray/domain)
Cek=$(lsof -i:80 | cut -d' ' -f1 | awk 'NR==2 {print $1}')
if [[ ! -z "$Cek" ]]; then
sleep 1
echo -e "[ ${red}WARNING${NC} ] Detected port 80 used by $Cek " 
systemctl stop $Cek
sleep 2
echo -e "[ ${GREEN}INFO${NC} ] Processing to stop $Cek " 
sleep 1
fi
echo -e "[ ${GREEN}INFO${NC} ] Starting renew gen-ssl... " 
sleep 2
yum install curl socat -y
curl https://get.acme.sh | sh
~/.acme.sh/acme.sh --set-default-ca --server letsencrypt
~/.acme.sh/acme.sh --register-account -m resaananta42@gmail.com
~/.acme.sh/acme.sh --issue -d $domain --standalone
~/.acme.sh/acme.sh --installcert -d $domain --key-file /etc/xray/xray.key --fullchain-file /etc/xray/xray.crt

echo -e "[ ${GREEN}INFO${NC} ] Renew gen-ssl done... " 
sleep 2
echo -e "[ ${GREEN}INFO${NC} ] Starting service $Cek " 
sleep 2
echo -e "[ ${GREEN}INFO${NC} ] All finished... " 
sleep 0.5
echo ""
cd

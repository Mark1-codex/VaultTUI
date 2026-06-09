#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate
pip install rich keyboard
INSTALL_PATH=$(pwd)
echo "#!/bin/bash" > vault
echo "sudo -E $INSTALL_PATH/.venv/bin/python $INSTALL_PATH/main.py \"\$@\"" >> vault
sudo mv vault /usr/bin/vault
sudo chmod +x /usr/bin/vault
echo "VaultTUI installed successfully! Run 'vault' to launch."

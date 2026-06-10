#!/bin/bash

# Ensure script is run with sudo
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root"
  exit
fi

# Define paths
REPO_URL="https://github.com/Mark1-codex/VaultTUI.git"
INSTALL_DIR="/opt/vault"
BIN_PATH="/usr/bin/vault"

# 1. Clone the repository
echo "Cloning VaultTUI to $INSTALL_DIR..."
rm -rf "$INSTALL_DIR"
git clone "$REPO_URL" "$INSTALL_DIR"

# 2. Setup virtual environment and dependencies
echo "Setting up virtual environment..."
python3 -m venv "$INSTALL_DIR/.venv"
"$INSTALL_DIR/.venv/bin/pip" install --upgrade pip
"$INSTALL_DIR/.venv/bin/pip" install keyboard rich

# 3. Create the executable launcher
echo "Creating launcher at $BIN_PATH..."
cat <<EOF > "$BIN_PATH"
#!/bin/bash
sudo -E /opt/vault/.venv/bin/python /opt/vault/main.py "\$@"
EOF

# 4. Make it executable
chmod +x "$BIN_PATH"

echo "Installation complete. You can now run 'vault' from your terminal."

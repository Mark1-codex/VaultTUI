VaultTUI is a robust file manager which utilizes terminal functional.
## Requirements and launch guide:
The app needs these packages to function properly:
 * Kitty terminal
 * Python 3
 * Nano text editor  
You can install these packages via:
 * Debian-based distributions:  
 ```sudo apt upgrade && sudo apt install python3 && sudo apt install kitty &&  sudo apt install nano```  
 * Arch-based distributions:  
 ```sudo pacman -Syu && sudo pacman -S python && yay -S kitty #You can use paru if you have got paru AUR helper```  
 Download the installer:  
 ```curl -fsSL https://raw.githubusercontent.com/Mark1-codex/VaultTUI/main/installer.sh | sudo bash```    
 Run installer:  
 ```chmod +x installer.sh && ./installer.sh```  
 Then, run with:  
 ```vault```  
## Usage guide:
Once you have successfully set up VaultTUI on your device, run it. Enter user password (required for the keyboard module). Congratulations on setting up VaultTUI!    
Here are basic usage instructions:  
Up / Down arrow keys - Move between items in the selected directory  
Enter - Edit the file with nano if the selected item is a file, move inside a folder if the selected item is a folder  
Space - Select multiple items at a time  
Ctrl+Enter - Move one stage up in the folders (for example, if you were working in /home/user/Documents, you will appear in /home/user)   
Ctrl+N - Make a new file in selected directory  
Ctrl+M - Move the file to a new location   
Ctrl+S - Copy the file (make sure not to confuse with Ctrl+C as it just stops the process)  
Ctrl+D - Delete the selected file  
Ctrl+R - Rename the selected file  
Ctrl+T - Open the terminal emulator (Ctrl+Q to exit)  
Ctrl+C - Stop the app from running.  
Ctrl+H - To display help   
Ctrl+Q - To exit the app (or Ctrl+C but that is unrecommended)  
Shift+H - To view the README.md   

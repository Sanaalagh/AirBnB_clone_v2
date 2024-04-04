#!/usr/bin/env bash
# Script to set up web servers for deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx &>/dev/null; then
	    sudo apt-get -y update
	        sudo apt-get -y install nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/{releases/test,shared}
sudo chown -R ubuntu:ubuntu /data/

# Create a fake HTML file for testing
echo "<html>
  <head>
    </head>
      <body>
          Holberton School
	    </body>
	    </html>" | sudo tee /data/web_static/releases/test/index.html

	    # Create symbolic link if it exists, otherwise recreate it
	    if [ -L /data/web_static/current ]; then
		        sudo rm /data/web_static/current
	    fi
	    sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

	    # Update Nginx configuration
	    config="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
	    sudo sed -i "/server_name _;/a $config" /etc/nginx/sites-available/default

	    # Restart Nginx
	    sudo service nginx restart

	    exit 0

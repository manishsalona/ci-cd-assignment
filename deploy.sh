
#!/bin/bash

# deploy.sh

REPO_URL="https://github.com/manishsalona/ci-cd-assignment.git"
WEB_ROOT="/usr/share/nginx/html"
TEMP_DIR="/tmp/simple-html-project"
GITHUB_TOKEN="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"

# Clone the repository with authentication
rm -rf $TEMP_DIR
git clone https://$GITHUB_TOKEN@github.com/manishsalona/ci-cd-assignment.git $TEMP_DIR

# Deploy to Nginx web root
sudo rm -rf $WEB_ROOT/*
sudo cp -r $TEMP_DIR/* $WEB_ROOT/

# Restart Nginx
sudo systemctl restart nginx

echo "Deployment completed."
~
~

#!/usr/bin/env zsh

CONTAINER_ALREADY_STARTED="CONTAINER_ALREADY_STARTED_PLACEHOLDER"

embrion_env_name=$(cat /embrion/dev/environment.yml | grep -oP '^name:\s*\K(\S+)(?=\s*$)')

if [ ! -e /tmp/$CONTAINER_ALREADY_STARTED ]; then

    echo "-- First container startup --"
    echo "-- Done: First container startup --"

else
    echo "-- Welcome back --"
fi


zsh /embrion/dev/update_environment.sh

echo "-- Starting servers --"

echo "-- Starting jupyter server --"
tmux new -d -s embrion_jupyter
tmux send-keys -t embrion_jupyter.0 "conda activate $embrion_env_name && jupyter lab --ip=0.0.0.0 --no-browser --allow-root" ENTER
echo "-- Done: Starting jupyter server --"

echo "-- Starting vscode server --"
tmux new -d -s embrion_vscode
tmux send-keys -t embrion_vscode.0 "~/code-server /app -e /app/.vscode/extensions -d /app/.vscode/settings --allow-http --no-auth --disable-telemetry" ENTER
echo "-- Done: Starting vscode server --"

echo "-- Starting ssh server --"
service ssh start
echo "-- Done: Starting ssh server --"

echo "-- Done: Starting servers --"

echo "-- Ready... --"


exec "$@"
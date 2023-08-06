#!/usr/bin/env zsh

CONTAINER_ALREADY_STARTED="CONTAINER_ALREADY_STARTED_PLACEHOLDER"

embrion_env_name=$(cat /embrion/dev/environment.yml | grep -oP '^name:\s*\K(\S+)(?=\s*$)')

if [ ! -e /tmp/$CONTAINER_ALREADY_STARTED ]; then

    echo "-- First container startup --"
    echo "-- Done: First container startup --"

else
    echo "-- Welcome back --"
fi


#!/usr/bin/env zsh
if cmp -s environment.yml /tmp/environment.yml ; then
else
    env_name=$(cat environment.yml | grep -oP '^name:\s*\K(\S+)(?=\s*$)')

    if [ -s /tmp/environment.yml ]; then
        old_env_name=$(cat /tmp/environment.yml | grep -oP '^name:\s*\K(\S+)(?=\s*$)')

        if [ "$env_name" = "$old_env_name" ]; then
            echo "-- Updating old project environment --"
            conda env update --prune --name $env_name environment.yml
            echo "-- Updating old project environment --"
        else
            echo "-- Removing old project environment --"
            conda env remove --name $old_env_name
            echo "-- Done: Removing project environment --"
            sed -i -e "s/conda activate $old_env_name//g" ~/.zshrc

            echo "-- New environment is being created --"

            echo "-- Installing project environment --"
            conda env create -f environment.yml
            echo "-- Done: Installing project environment --"

            echo "-- Installing ipykernel --"
            conda install -y -n $env_name ipykernel
            echo "-- Done: Installing ipykernel --"

            echo "-- Installing xeus kernel --"
            conda install -y -n $env_name -c conda-forge xeus-python ptvsd
            echo "-- Done: Installing xeus kernel --"

            echo "-- Registering project environment --"
            echo "conda activate $env_name" >> ~/.zshrc
            echo "-- Done: Registering project environment --"

            echo "-- Done: New environment is being created --"
        fi
    else
        echo "-- New environment is being created --"

        echo "-- Installing project environment --"
        conda env create -f environment.yml
        echo "-- Done: Installing project environment --"

        echo "-- Installing ipykernel --"
        conda install -y -n $env_name ipykernel
        echo "-- Done: Installing ipykernel --"

        echo "-- Installing xeus kernel --"
        conda install -y -n $env_name -c conda-forge xeus-python ptvsd
        echo "-- Done: Installing xeus kernel --"

        echo "-- Registering project environment --"
        echo "conda activate $env_name" >> ~/.zshrc
        echo "-- Done: Registering project environment --"

        echo "-- Done: New environment is being created --"
    fi
    cp environment.yml /tmp/environment.yml
fi

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
echo "-- Go to http://localhost:28888 for jupyterlab --"
echo "-- Go to http://localhost:24443 for vs code --"


exec "$@"
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
    fi
    cp environment.yml /tmp/environment.yml
fi
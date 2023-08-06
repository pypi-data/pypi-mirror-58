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
            conda env create -f environment.yml -n $env_name
            conda env update --name $env_name -f /embrion/dev/environment_extra.yml

            echo "-- Done: Installing project environment --"

            echo "-- Registering project environment --"
            echo "conda activate $env_name" >> ~/.zshrc
            echo "-- Done: Registering project environment --"

            echo "-- Done: New environment is being created --"
        fi
    else
        echo "-- New environment is being created --"

        echo "-- Installing project environment --"
        conda env create -f environment.yml -n $env_name
        conda env update --name $env_name -f /embrion/dev/environment_extra.yml
        echo "-- Done: Installing project environment --"

        echo "-- Registering project environment --"
        echo "conda activate $env_name" >> ~/.zshrc
        echo "-- Done: Registering project environment --"

        echo "-- Done: New environment is being created --"
    fi
    cp environment.yml /tmp/environment.yml
fi
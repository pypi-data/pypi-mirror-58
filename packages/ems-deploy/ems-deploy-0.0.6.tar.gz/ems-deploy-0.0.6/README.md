# EMS Deploy script

This project provides a general-purpose deploy script for the EMS projects. It runs the suitable docker-compose command based on the available docker-compose files located in the directory.

## Install

`pip install ems-eploy`

## Directory structure and required files
Deploy concatenates a `docker-compose` command. The following files are recognized

 1. `docker-compose.yml` Required: Base file
 2. `docker-compose.deploy.yml` Required: This file is added as an additional docker-compose file
 3. `docker-compose.debug.yml` Optional: This files is used instead of `docker-compose.deploy.yml` when using the `debug` flag

## How to use

The following flags are always added to the `docker-compose` command:

 - `--force-recreate`
 - `--renew-anon-volumes`
 - `--build`

### Deploy
To deploy the app, simply run 

`deploy`

Note that it will automatically add the `-d` flag which detaches from the process afterwards.

### Debug
To run in debug mode, run

`deploy debug`

Note that it will NOT automatically detach - this can however be supplied. See the next section for additional flags

### Additional flags

 - `-d` Detaches the process (this is automatically done in deploy-mode, but not in debug-mode)
 - `-v` Writes the resulting command to the terminal.


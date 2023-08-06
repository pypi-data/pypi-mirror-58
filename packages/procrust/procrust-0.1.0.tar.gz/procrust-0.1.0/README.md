# procrust

Limit the time you procrastinate by blocking websites via the hosts file.

# Usage

## Edit block list

Open the list of host names to block when not procrastinating for editing:

    procrust edit

Add one host name per line.

## Start and stop procrastinating

When you start and stop procrastinating the hosts file will be changed, so you need to run the command with root privileges. If you ran the `edit` command without `sudo` you need to preserve the environment with the `-E` option.

    sudo -E procrust start

    sudo -E procrust stop

# Installation

Install the `procrust` command globally so it is accessible by the root user.

    git clone https://github.com/yaph/procrust.git
    cd procrust
    sudo python3 setup.py install

## Authors

`procrust` was written by [Ramiro Gómez](https://ramiro.org/).
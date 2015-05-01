Baryon README
=====================

Copyright (c) 2015 Cha Dong-Hwi

This is experimental project.

Unlike docker, lxc provides os as container not application level.
At first, this project aims to provide os template via lxc, not app level clustering.
But further consideration will change this view.

The sequence of goals to achieve
1. provide lxc as nova compute does
2. provide network as nova compute did (nova network)
3. provide app level clustering

To setup run command below
    # sudo mkdir /etc/baryon
    # sudo chown stack:stack /etc/baryon
    # ln -s /your-workspace-directory/lxccomponent/etc/baryon/api-paste.ini /etc/baryon/api-paste.ini

-- End of broadcast

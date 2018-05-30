# docker-volume-backup
## Overview
This project sets out to make a quick and easy job of backing up and restoring Docker volumes.
* To run a backup:
  * Volume mount the volume in question to the containers '/input' directory.
  * Volume mount a host directory to 'output'; the backup will be saved here.
  * Specify the 'backup' command.
* To run a restore:
  * Place the .tar backup into the 'input' directory.
  * Volume mount a new volume (see 'volume_to_restore' below)
  * Specify the 'restore' command, followed by the relative backup file (i.e. /input/backup.tar.gz)

### How to run
#### Buliding the image
docker build -t docker-volume-backup .
#### Running a backup
docker run -it -v jenkins_jenkins_home:/input -v /home/mccullya/Projects/github/docker-volume-backup/output:/output docker-volume-backup backup
#### Running a restore
docker run -it -v << volume_to_restore >>:/output -v /home/mccullya/Projects/github/docker-volume-backup/input:/input docker-volume-backup restore /input/backup.tar.gz



docker run -it -v boom2:/output -v /home/mccullya/Projects/github/docker-volume-backup/input:/input docker-volume-backup restore /input/backup.tar.gz

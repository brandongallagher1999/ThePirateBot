![Skull Icon](https://upload.wikimedia.org/wikipedia/commons/4/45/The_Pirate_Bay.jpg)

                                                                                Version: Release v1.0

## Github project URL
https://github.com/brandongallagher1999/ThePirateBot/


## Contributors
1. **Brandon Gallagher**
  - Roles: Back-end / Database
  - Email: brandonegallagher@gmail.com
  - [Github Profile](https://github.com/brandongallagher1999)

## Description
- Uses ThePirateBay API and DiscordPy to create a bot that allows users to look up content such as Movies, Games and other things and returns them a revelant
torrent with its respective magnet, name and image.

# How to run
## Docker
1. Download Docker for Desktop (https://www.docker.com/products/docker-desktop)

## Container
1. Go into root folder and run
```
docker-compose build
docker-compose up
```
  
## Commands
- Torrent
```
!!torrent <name>
```
This will return an Embed Link with relevant magnet, name and image.

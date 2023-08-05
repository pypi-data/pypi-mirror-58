# Team-Mates

> A simple python library to analyze team-mates contributions to projects, using tools like Git and Trello. It embed a web interface to easily consult theses informations.

Source: https://github.com/HoshiyoSan/team-mates.git

## Display the web interface

```bash
python3 -m team-mates web -p 8080 --browser
```

Run the dataviz web server on port 8080 (if omitted, default is 5000)

## Helper commands
```bash
help                           display this help
install                        install dev dependencies in a virtualenv
test                           reinstall dev project and try to run web server
```
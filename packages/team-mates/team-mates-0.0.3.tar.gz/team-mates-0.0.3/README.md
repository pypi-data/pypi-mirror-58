# Team-Mates

> A simple python library to analyze team-mates contributions to projects, using tools like Git and Trello. It embed a web interface to easily consult theses informations.

## Sources

* GitHub: https://github.com/HoshiyoSan/team-mates.git
* PyPI: https://pypi.org/project/team-mates

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
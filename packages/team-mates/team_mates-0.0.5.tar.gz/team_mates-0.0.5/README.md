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

## Contribution

### Development environement

To work on this project you need to install the followings:
* Python >= 3.6
* virtualenv
* npm / angular6

### Project structure
```javascript
team-mates
├── frontend    // angular frontend
├── Makefile    // custom commands
├── MANIFEST.in // static files mgmt
├── README.md   // documentation
├── setup.py    // package configuration
└── team_mates  // team-mates package
```

### Utils commands

A full list of commands can be retrieve by doing
```
$ make help
```

Example output
```
help                           display this help
install                        install dev dependencies in a virtualenv
upload                         build and upload package on pypi
```


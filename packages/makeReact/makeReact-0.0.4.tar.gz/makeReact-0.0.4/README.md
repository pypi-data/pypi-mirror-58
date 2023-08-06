# makeReact


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

makeReact is a python package which helps react and react-native developer to speed-up their develoment process. It saves our time of creating new components or screens and writing the bare minimum amount of code every time. So here is a python package with which we can create our components right from the terminal into the projects directory, all that ease is just a pip install away.



> pip install makeReact


### Installation

makeReact has following command line flags:
- -path=Pass the path to the project
- -s=If True, Create files in screens folder( suitable for react-native )
- -c=If True, Create files in components folder( suitable for both react and react-native)
- -n=Pass the name for the component or screen
- -r=If True, create files with react code
- -rn=If True, create files with react-native code

Note: 
- Either of the -s or -c flag must be set to True
- Either of the -r or -rn flag must be set to True
- Components or Screens folder are created if not already present in the

Example:
```sh
makeReact -path=C:/Users/Hur/MyReactProject/src -c=True -n=MyComponent -r=True
```

License
----

MIT





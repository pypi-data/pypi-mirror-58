# dockship

### Installation
You can install dockship from PyPI:

`pip install dockship`

dockship requires python == 3.6 and docker installed.

### How to use
`dockship` is a command line application. It supports two commands:

### run

 Downloads model from Dockship and runs the model in docker container.
 
 Args:
 
    modelID (string) : Model's unique id shown at dockship.io
    port (string)    : Port number for running model
    
### stop

 Stops the already runnng model.
 
 Args:

    modelID : Model's unique id which needs to be stopped.
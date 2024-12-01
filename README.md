# Festival Simulation - FestIEval

This project was made to simulate the usual activities that happen at a music festival. These include: attendee behaviors, resource usage, and revenue computation. The simulation is multi-threaded to model various processes happening concurrently, in such a way that we can model how people enter the festival, their behaviours, and watching performances of various artists among other features.

## Features

- **Attendees**: Simulate thousands of people with unique preferences for artists, hunger, thirst, and other needs.
- **Stages**: Four stages hosting major and minor artists with dynamic schedules. (2 main stages that have greater capacity and 2 small stages with a lower capacity)
- **Resources**: Includes bars, food stands, merchandise stands, and bathrooms, each managed with queues and threading.
- **Real-time UI**: A dynamic user interface to visualize the festival activities, including stage capacities, queue lengths, the usage of resources like the bathrooms, bars, and merch stands.

## File Structure

- `Bathroom.py`: Defines the `Toilet` class for bathroom management.  
- `extra_functions.py`: Helper functions for creating resources and attendees.
- `Festival.py`: Core logic for managing the festival, including scheduling and attendee management.
- `Food.py`: Defines the `Food` class for food stand operations.
- `Merch.py`: Defines the `MerchStand` class for merchandise sales.
- `Bar.py`: Defines the `Bar` class for merchandise sales.
- `Person.py`: Models individual attendee behavior and preferences.
- `Queue.py`: Provides thread-safe queue management for festival resources.
- `Stages.py`: Manages stage operations and artist performances.
- `Ui.py`: Implements the user interface for visualizing the simulation.
- `simulation.py`: Main script to run the festival simulation.


## Requirements
It is necessary to install the requirements that can be found in the requirements.txt file

- pip install -r requirements.txt 

The requirements are for python version 3.2 and above so if you have another version you migth need to install other libraries.


## Ideas for future Improvements
- Optimize thread management for larger-scale simulations
- Try to think of ways to maximize profits
- Add features to the UI so that we can possibly see how each person moves around
- Include even more attendee behaviours like going in groups
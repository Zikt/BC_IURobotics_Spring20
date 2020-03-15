BC_IURobotics_Spring20
======================

Assignments and Labs for Behavioral & Cognitive Robotics Course in Innopolis University for Spring Semester 2020

The guide, instructions for this course and other materials can be found in the repository [here](https://github.com/snolfi/evorobotpy). Course Instructor - [Prof. Stefano Nolfi](https://scholar.google.com/citations?user=YVqJ_u8AAAAJ&hl=en). 

All the software required is available ready to be used through the docker container docker container prepared by Vladislav Kurenkov that can be pulled, built and run. Check the repository above for further instructions. 
*Learn more about [Gym](http://gym.openai.com/docs/#background-why-gym-2016)*

[Lecture notes here](https://drive.google.com/drive/folders/1EpsjCB-iDPjrD0LVzeGLXi3nP1JkSx2k)

---


Exercise 1
---------- 
Getting used to working with Gym.
Testing and learning how to use gym environments.

Exercise 2
----------
 Implement Evolutionary Hill-Climber with simple Neural Network and train it.

**Ex 2a:** 
The task is to implement a neural network controller for a Gym problem (the CartPole-v0). I initialized the network with random
parameters, and evaluated the neuro-agent for 10 evaluation episodes each
lasting 200 steps and printed the toal sum of rewards. Since the cartPole-v0 problem returns a reward of 1 for each step in which the pole is balanced, the fitness(total reward) corresponds to the total number of steps in which the agent manages to keep the pole balanced. As expected, the agent did not balance the pole for many steps by using a policy with random parameters.

Next I implemented the steady state evolutionary strategy (Pagliuca, Milano and Nolfi, 2018) as described by the given pseudo-code. Note that When the population includes only 2 individuals, as in the described example, the algorithm is equivalent to a stochastic hill-climber that operates on a single candidate solution by (i) adding random variation to
the parameters, and (ii) by retaining or discarding the variations depending on whether the addition of variations produce an increase or a decrease of the fitness, respectively.




**Ex 2b:**


Exercise 3
----------

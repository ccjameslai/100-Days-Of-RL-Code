100-Days-Of-RL-Code
===

This is a review of Reinfoircement Learning.

It has three parts, 1) fundation of RL, 2) RL based on value function, 3) RL based on direct policy search.

# Fundation of RL

- ## Markov Decision Process | Day 1

  ### What is MDP
  MDP is a transition matrix with actions and rewards.<br>
  MDP is used to simulate a world in the form of a grid by dividing it into states, actions, rewards, and transition models.
  
  ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/MDP.png)
  
  Circle is state.<br>
  {Facebook, Quit, Study, Pub, Sleep} are actions.<br>
  R is reward.
  
  MDP is defined as the following:
  
  - **States**: S
  - **Actions**:A(s), A
  - **Transition model**: T(s,a,s') ~ P(s'|s,a)
  - **Rewards**: R(s), R(s,a), R(s,a,s')
  - **Policy**: π
  
- ## MDP and RL | Day 2
  
  A reinforcement learning (RL) task composed of states, actions, rewards that follows Markov property would be considered a MDP.
  
  The goal of RL is to find an optimal policy with a given MDP. Policy is a mapping function, which is from state to action and is a probability that an action is selected in a state. 
  
  

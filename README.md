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
  
  ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/MDP_policy.PNG)
  
  The goal of RL is to find an optimal policy with a given MDP. Policy is a mapping function, which is from state to action and is a probability that an action is selected in a state. 
  
  How to find the optimal policy => Optimal value function, optimal policy.
  
  ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/policy_and_value_function.PNG)

  **Definition**

  ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/value_function.PNG)

  **Bellman Equation** (used in programming)

  ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/Bellman_Equation.PNG)
  
- ## Implementing MDP | Day 3
  
  Here is an example. We use a grid of 3*4 to represent a world(shown as below).
  
  ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/grid_map.PNG)
  
  p(desired action) = 0.8, p(other actions prependicular desired action) = 0.1, reward = -3
  
  check out the code [here](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Code/Day3_MDP.py)
  
- ## Dynamic Programming for solving MDP | Day 4
 
  The key idea of DP is the use of value function to find the optimal policy.
  
  RL can be modelled as a MDP, which fits two conditions of DP. 
  
  These two conditions are 
  
      1) main problem can decompose to subproblems
      
      2) the solutions of subproblems can be stored and reused.
  
  There are two ways to get the optimal policy, policy iteration and value iteration. Policy iteration consist of policy evaluation ans policy improvment.
  
  ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/policy_iteration.PNG)
  
  The difference between policy iteration and value iteration is the timing of updating state value. Improving policy after evaluating it once is called value iteration.

- ## Policy iteration and Value iteration | Day 5

  Policy iteration : 
  
      1) Value function have to be converged and then use this value function to decide the optimal policy.
      
      2) Repeat the process until policy is stable.
  
  ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/pesudo_code_of_Policy_iteration.png)
  
  Value iteration:
  
      1) Calculate the optimal policy and assign this value to value function.
      
      2) Repeat the process until value function is stable.
      
  ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/pesudo_code_of_Value_iteration.png)
  
- ## Monte Carlo Methods | Day 6

  It is a model free based method, which transition model(P) is unknow.
  
  But, the critical concept is the same as model based method, policy evaluation and policy improvement.
  
  Because transition model is unknow, it generates many episodes instead of transition model to calculate the total reward(G). 
  
  And it averages these total rewards as value function.
  
  There are two ways to implement Monte Carlo method, on-policy and off-policy. 
  
    - On-policy is that they estimate the value of policy while using it for control
    
    - In off-policy, these two functions(control policy and evaluation policy) are separated
    
   ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/MC_PolicyEvaluation.JPEG)
  
  

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
  
  **check out the code** [here](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Code/Day3_MDP.py)
  
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
  
- ## Value function for Monte Carlo Method | Day 6

  Monte Carlo for RL is a model free based method, which transition model(P) is unknow.
  
  But, the critical concept is the same as model based method, policy evaluation and policy improvement.
  
  Because transition model is unknow, it generates many episodes instead of transition model to calculate the total reward(G). 
  
  And it averages these total rewards as value function.
  
  ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/MC_PolicyEvaluation.JPG)
  
  ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/MC_ES.JPG)
  
- ## Two methods for Monte Carlo Method | Day 7

  There are two ways to implement Monte Carlo method, on-policy and off-policy. 
  
    - On-policy is that they estimate the value of policy while using it for control
    
  ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/MC_onpolicy.JPG)
    
    - In off-policy, these two functions(control policy and evaluation policy) are separated
    
  ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/MC_offpolicy.JPG)
  
 - ## Sample code for Monte Carlo | Day 8 
  
   Example:
  
   ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/maze.JPG)
  
   - Executing Test_mc() in TestMonteCarlo.py can find the best way to terminal state, which is 8.
   
   - There are implements, generating random samples and mc policy evaluation, in TestMonteCarlo.py.
   
   **check out the code** [here](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Code/TestMonteCarlo.py)
  
 - ## Temporal-Diffrerence Learning | Day 9
   
   TD is another model-free method of RL.
   
   TD has adventages of both dynamic programming and Monte Carlo.
     
     - like MC method, TD can learn derictly from raw experience without a model of the environment's dynamics.
     
     - like DP method, TD updates estimates based in part on other learned estimates, without waiting for a final outcome.
     
   TD = MC(sampling) + DP(bootstrapping)
   
     - sampling : episode
     
     - bootstrapping : estimate current value function with value function of next step
     
     ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/dp.JPG)
     
     ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/mcmethod.JPG)
     
     ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/tdlearning.JPG)
  
 - ## The difference among DP, MC and TD | Day 10
   
   The updating formuler of value function of TD
   
   $$
   V(S_t) \leftarrow V(S_t) + \alpha (R_{t+1} + \gamma V(S_{t+1}) - V(S_t))
   $$
   $$
   R_{t+1} + \gamma V(S_{t+1})\ is\ called\ as\ TD\ target\
   $$
   $$
   `R_{t+1} + \gamma V(S_{t+1}) - V(S_t)\ is\ called\ as\ TD\ bias\ `
   $$
   
     ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/difference_among_three_methods.JPG)

     - Value function of MC is an unbiased estimation, but variance is large.
   
     - Value function of TD is an biased estimation, but variance is small.
   
  - ## Introduction of TD(λ) | Day 11
  
    ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/TDlambda.JPG)
    
    As we know, G_t is the goal of TD. We use the next step's value function to update the current value function. Therefore, G_t is used to estimate the current value function. The updating function of n_th step can be represented as follow:
    
    $$
    G^{(n)}_t = R_{(t+1)} + \gamma R_{(t+2)} + \gamma ^ 2R_{(t+3)} + \cdot \cdot \cdot + \gamma^{n-1} R_{(t+n)} + \gamma ^ nV(S_{t+n})
    $$
    
    TD(λ) means that using G_t-lambda to update the current value function 
 
 

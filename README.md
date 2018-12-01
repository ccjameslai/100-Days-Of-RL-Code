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
   R_{t+1} + \gamma V(S_{t+1}) - V(S_t)\ is\ called\ as\ TD\ bias\ 
   $$
   
     ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/difference_among_three_methods.JPG)

     - Value function of MC is an unbiased estimation, but variance is large.
   
     - Value function of TD is an biased estimation, but variance is small.
   
 - ## Introduction of TD(λ) | Day 11
  
   As we know, G_t is the goal of TD. We use the next step's value function to update the current value function. Therefore, G_t is used to estimate the current value function. The updating function of n_th step can be represented as follows
   
     ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/TDgoal.JPG)
   
   TD(λ) means that using G_t-lambda to update the current value function. Hence, we need to fuse G_t of each step and the formula is as follows
    
   $$
   G^\lambda _t = (1-\lambda )G^{(1)}_t + \lambda (1-\lambda )G^{(2)}_t + \lambda ^2(1-\lambda )G^{(3)}_t + \cdot \cdot \cdot + \lambda ^{n-1}(1-\lambda )G^{(n)}_t \approx V(S_t)
   $$

     ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/TDlambda.JPG)
     
 - ## The forward and backward view of TD(λ) | Day 12
 
   The value function of the next state is used to update the value function of the current state. Can it be updated by the next two state's value function ? The answer is positive. It also can be updated by the next n state's value function. Therefore, we have n methods to estimate the current value function. In order to make the approaximate value, weighted sum is the method, that is TD-lambda. 
   
   There are two ways to understand TD-lambda, forward view and backward view.
 
     **Forward view**
     
     ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/forwardTD.JPG)
   
   In forward view, it is the more theoretical view. The way to estimating value function is like MC, which begins to calculate the G_t until an episode terminates. 
   
     ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/TDgoal.JPG)
   
     **Backward view**
     
     ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/backwardTD.JPG)
   
   In backward view, it is more appropriate for programming. There are three steps to update value function, 
   
      1) calculate TD bias
      
     ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/tdbias.JPG)
      
      2) update eligibility trace
      
     ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/updateeligibility.JPG)
      
      3) update value function
      $$
      V(s) \leftarrow V(s) + \alpha \delta _tE_t(s)
      $$
 
 - ## Eligibility trace | Day 13
  
    From the point of view in math, eligibility trace is a differential of optimal approximation value function(reference: http://www.cnblogs.com/steven-yang/p/6617134.html). 
    
    In the backward view of TD(lambda), Eligibility trace is a memory variable associated with each state. In other words, it records which states have been visited recently.
    
    TD method, such as Sarsa or Q-learning, would learn more efficiently with eligibility traces.
    
    ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/eligibilitytrace.JPG)
    
    **check out the code** [here](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Code/TestTD_lambda.py)
 
 - ## Sarsa | Day 14
 
   Sarsa is one of TD method, which is on-policy. That means the action policy and evaluation policy are the same.
   
     ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/sarsaalgorithm.JPG)
   
   Example of Sarsa:
   
     ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/exampleofsarsa.JPG)
     
     **check out the code** [here](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Code/TestSarsa.py)
   
 - ## Q learning | Day 15
 
   ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/qlearning.JPG)
   
   Q learnig is another method of TD, which is off-policy. Off-policy means that action policy and evaluation policy are not the same.
   
   Example of Q learning:
   
     - the maze is the same as Day 14
      
     **check out the code** [here](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Code/TestQlearning.py)
    
 - ## Sara(lambda) | Day 16
   
   ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/sarsalambda.JPG)
   
     **check out the code** [here](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Code/TestSarsaLambda.py)
    
 - ## Qlearning(lambda) | Day 17
 
   ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/qlearninglambda.JPG) 
 
     **check out the code** [here](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Code/TestQlearningLambda.py)
     
 - ## Function approximation | Day 18
 
   There are some pre-conditions in DP, MC and TD, such as
   
     - state space and action space are discrete
     
     - state space and action space can't be too large
     
   The critical point of these methods is the evaluation of value function.
   
   In these methods, DP, MC and TD, value function can be seen as a table and state and state-action pair are index. 
   
   Updating the value function is the same as updating the table. 
   
   Owing to this kind of table form, there are two limitations mentioned above, space is discrete and can't be too large. 
   
   Therefore, fuction approximation could overcome these problems.
   
   The following graph shows a brief concept of function approximation.
   
   ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/funcApproxi.JPG)
   
 - ## Linear function approximation in parameters | Day 19
   
   Approximation in parameters is that value function could be approximated with a set of parameters, 
   $$ 
   \widehat{\upsilon }\left ( s, \theta \right ) = \theta ^{T}\phi \left ( s \right )
   $$
   
   $$
   \phi \left ( s \right ) \ is\ a\ basis\ function\ in\ state\ s.
   $$  
   
   The process of approximating can be seen as a supervised learning, 
   $$
   \left\langle s_{1},G_{1}\right\rangle,\left\langle s_{2},G_{2}\right\rangle,\cdots \left\langle s_{T},G_{T}\right\rangle
   $$
   
   The cost function is,
   $$
   argmin_{\theta }\left ( q\left ( s,a \right ) - \widehat{q}\left ( s,a,\theta  \right )\right )^{2}
   $$
   
   Gradient descent is used to update parameters, and the updating equation is
   
   $$
   \Delta \theta =\alpha[G_{t}-\widehat{\upsilon}(S_{t},\theta_{t})]\bigtriangledown_{\theta}\widehat{\upsilon}
   (S_{t},\theta_{t})
   $$
   
   There are two ways to update parameters, 1) incremental, 2) batch.
   
   In incremental way, there are common basis functions as fallows,
   $$
   Polynaminal\ basis\ function:\ \left ( 1,s_{1},s_{2},s_{1}s_{2},s_{1}^{2},s_{2}^{2},\cdots  \right )
   $$
   
   $$
   Fourier\ basis\ function:\ \phi _{i}\left ( s \right ) = \cos \left ( i\pi s \right ),\ s\in [0,1]
   $$
   
   $$
   Radial\ basis\ function:\ \phi_{i}\left(s\right) = \exp(-\frac{\left \|s-c_{i}\right\|^{2}}{2\sigma_{i}^{2}})
   $$
   
   In batch way, data set D is given, and the goal is to find the best fitting function,
   $$
   \widehat{\upsilon}(s_{t},\theta)
   $$
   
   Such that,
   $$
   min\ LS(\theta)\equiv min\ \sum_{t=1}^{T}(\upsilon_{t}^{\pi}-\widehat{\upsilon_{t}^{\pi}}(s_{t},\theta))^{2}
   $$
   
   The following is an example code of function approximation of MC (Testgradiant_based_policy_evaluation), 
   **check out the code** [here](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Code/TestMonteCarlo.py)
 
 - ## Non-parameters' function approximation | Day 20
   
   The meaning of non-parameters is that the number of parameters and form of basis are not fixed but formed by samples.
   
   For example, given training samples to generate an approximated function fitting these data.
   $$
   T = \left ( x_{1},y_{1} \right ),\left ( x_{2},y_{2} \right ),\cdots ,\left ( x_{N},y_{N} \right )
   $$
   
   $$
   f(x)=\sum_{i=1}^{N}\alpha _{i}y_{i}K(x,x_{i})+b
   $$
   
   There are two common methods for approximation, one is kernel based and the other is Gaussian process based.
   
   
 
 - ## Introduction of DQN(Deep Q learning Network) | Day 21
 
   ![image](https://github.com/ccjameslai/100-Days-Of-RL-Code/blob/master/Info_graph/DQN.JPG)
   
   
   
   
   
   

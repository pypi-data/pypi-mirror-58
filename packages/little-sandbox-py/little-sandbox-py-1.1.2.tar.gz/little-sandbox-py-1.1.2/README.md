# Little Sandbox
- Challenge
initialize a challenge with these parameters
    - filename: str, 
    - code: str, 
    - challenge_input: str， <-- 默认不带input
    - host_path: str, <-- 指定存放代码的路径，默认为当前路径
    - timeout: int,  <-- 单例超时时间，默认为5s
    - cpu: int, <-- CPU个数，默认为1核
    - memory: str, <-- 内存限制， 默认30M
    - memory_swap: str)) <-- 交换空间， 默认100M
Related codes locate in sandbox/testcase/

- Sandbox
transparent to users, only need to use Challenge.
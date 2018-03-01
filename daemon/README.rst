1. 简介：什么是守护进程？

守护护进程（服务），是

3. 计划你的守护进程
3.1 你要用它来做什么？
  守护进程只做而且做好一件事 —— 可能像管理多个domain下的上百个邮箱那么复杂，也可能像使用
sendmail 给管理员发一份报告那么简单。
  无论何种情况，你都应该事先设计好的 daemon 。如果你需要它和别的 daemon interoperate，
那些 daemon 你可能有写的权限，y也可能没有，这也是另外需要考虑的。

3.2 有多少交互？

4. 守护进程的基本结构

1. fork 副进程
2. 改变 umask
3. 打开 logs
4. 创建一个 session id
5. 把当前目录h换到一个安全的目录
6. 关闭标准的 file descriptor
7. 输入 daemon code

4.1 Fork 副进程
守护进程可由系统或用户/脚本创建。


umask
fork
i/o
signal
dup


fork
~~~~

fork 创建一个新进程, 于是有了 parent / child. 
返回两个值, int child_pid, parent_pid. 
这里的 child_pid == 0, parent_pid == 45028. 

比如执行下面这样一段代码::
    print('this programming\'s pid: ', os.getpid())

    pid = os.fork()
    logging.info('fork: {}'.format(pid))

    pid = os.getpid()
    logging.info('getpid: {}'.format(pid))

得到输出::
    this programming's pid:  45677
    fork: 45685
    getpid: 45677
    fork: 0
    getpid: 45685

1. parent 也就是程序本身的 pid 是 45677, 在下面执行 os.getpid() 时, 再一次返回这个值. 
2. fork() 返回两个值, child 返回 0, parent 返回 child 实际的 pid 45685. 
3. getpid() child / parent 分别执行, 于是就返回它们真实的值. 

如果我们再添加两行::
    ppid = os.getppid()
    logging.info('getppid: {}'.format(ppid))

会得到::
    getppid: 37579
    getppid: 45677

第一个是 parent 本身的 parent pid, 下面则是 child 得到了 parent pid, 所以等于前面 programming pid. 


child 共享 parent 数据的 copy, 它们执行的先后顺序不确定. 

setsid
~~~~~~

session 是多个 process group 的集合.

process group
\\\\\\\\\\\\\

每个 process 都有 pid, 和 group id. 一个 group 是若干 process 的集合. 
这个 gid 实际上是这个进程组组长的 pid, 组长可以
    - 创建一个组
    - 创建组中的进程
    - 终止
只要组中还有进程, 无论组长进程是否终止, 它都会存在. 

*python 的 os.getpgrp() / os.getpgid(0) 都可以得到进程所属进程组的 id.*

setsid() 执行会发生 3 件事::
    - 调用这个函数的进程创建一个新 session, 它是这个 session 当前的唯一进程, 也是 session leader. 
    - 该进程同时成为一个新进程组的组长进程, 进程组 id 是组长的 pid. 
    - 没有终端控制 

如果调用 setsid() 的进程本来就是组长进程, 就会出错. 
所以在使用了 fork() 之后, 会先终止 parent, 再调用 setsid(). 
这样既继承了 group id, 使用的是 child pid, 保证不是组长进程. 

terminal
~~~~~~~~

terminal 控制一个 pgroup 或者一个 session, 其中::
    - 与 terminal 连接的 session leader 又称为 controlling process
    - 一个 session 中的多个 pgroup 又可以分为 foreground pgroup / background pgroup. 
    - 有一个 fg 和若干 bg 
    - 中断 & 退出 信号会发送到 fg 的所有进程
    - 终端接口 / 网络 断开, 挂断信号会发送到 session leader.

file descriptor
~~~~~~~~~~~~~~~

Unix 在操作文件使用 open / creat 的时候会返回一个 fd, 它作为文件的标识供 read / write 等使用. 
现在, stdin / stdout / stderr 的 fd 已经规定使用 0 / 1 / 2 了, 也可以用 STDIN_FILENO / STDOUT_FILENO / STDERR_FILENO 这样的形式表示.(因为 C 的 <unistd.h> 有所定义) 
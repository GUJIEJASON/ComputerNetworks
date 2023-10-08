# 计算机网络实验报告
## 实验一socket编程&#x2003;谷杰&#x2003;10222140408
### 测试用例通过情况
![png](https://raw.githubusercontent.com/GUJIEJASON/ComputerNetworks/main/assignment1/output.png)
### 代码实现过程
### client-c
&#x2003;&#x2003;首先先创建socket，并connect到服务端所在的端口。再通过fread从stdin中读取消息并用send发送至服务端，其中用到循环，直到读到"\0"为止，最后关闭通信通道并终止。
### server-c
&#x2003;&#x2003;首先先创建socket，再通过下面这行代码告诉操作系统，允许在套接字关闭后立即重新绑定相同的地址和端口，以便监听多个客户端。
```c
setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &yes,sizeof(int))
```
&#x2003;&#x2003;再通过bind绑定ip地址，然后便是listen监听。当接受到请求后便是accept获取客户端的socket，通过recv接收到客户端发送来的信息，再通过fwrite写至stdout，同时别忘记fflush。处理完当前客户端后即可关闭与当前客户端的连接，等待下一个客户端的连接，全部处理完后关闭服务器。
### client-python
&#x2003;&#x2003;python与c的并没有什么大的区别，只是python是直接read buffer里的内容。
### server-python
&#x2003;&#x2003;服务端与客户端的不同是python服务端要判断一下消息是否为二进制文件，若是二进制文件则无需解码，这里用到了try，先尝试解码，若出现问题，则说明是二进制文件，则直接write，无需decode。
### 实验过程的错误和解决办法
&#x2003;&#x2003;我先完成的python版本，但是python最开始我只通过了4个用例，对于二进制消息我当时无法处理，一直是以下报错：
![png](https://raw.githubusercontent.com/GUJIEJASON/ComputerNetworks/main/assignment1/error.png)
&#x2003;&#x2003;究其原因是python在对于二进制消息时无需解码，后面我通过用一个try和except将其解决，具体解决办法详见代码，上面的代码实验过程也有提及。<br>
&#x2003;&#x2003;c版本我碰到的主要问题是前面部分的连接过程，由于开始是参考网上错误的资料，所以一直失败，直到后面得知《Beej 网络编程指南》中有例子，参考了以后便能成功连接。c语言的二进制消息也遇到了一点小问题，但是其实只是函数没用好，得知得用fwrite和fread即可轻松解决二进制消息的问题后c语言的用例便可全部通过了
### 实验收获
&#x2003;&#x2003;首先最基本的是锻炼了编程能力，虽然代码量不大，但还是温习了基本语法。其次是了解了许多关于socket编程的知识，包括函数，服务端与客户端连接和发送消息的过程,尤其是其中的“TCP三次握手”。
![png](https://raw.githubusercontent.com/GUJIEJASON/ComputerNetworks/main/assignment1/1.png)
&#x2003;&#x2003;最后这次实验更磨砺了我的心态，实验过程中遇到了蛮多的困难，但最后都一一克服了，这也是这次实验对于我最大的收获，培养了解决问题的能力。

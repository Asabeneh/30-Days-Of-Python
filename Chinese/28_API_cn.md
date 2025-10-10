# 30天Python编程挑战：第28天 - API

- [第28天](#-第28天)
- [应用程序编程接口(API)](#应用程序编程接口api)
  - [API](#api)
  - [构建API](#构建api)
  - [HTTP(超文本传输协议)](#http超文本传输协议)
  - [HTTP的结构](#http的结构)
  - [初始请求行(状态行)](#初始请求行状态行)
    - [初始响应行(状态行)](#初始响应行状态行)
    - [头字段](#头字段)
    - [消息体](#消息体)
    - [请求方法](#请求方法)
  - [💻 练习：第28天](#-练习第28天)

# 📘 第28天

# 应用程序编程接口(API)

## API

API是应用程序编程接口(Application Programming Interface)的缩写。我们在本节中将介绍的API类型是Web API。
Web API是定义好的接口，通过这些接口在企业和使用其资产的应用程序之间进行交互，这也是一种服务级别协议(SLA)，用于指定功能提供者并为其API用户公开服务路径或URL。

在Web开发的上下文中，API被定义为一组规范，如超文本传输协议(HTTP)请求消息，以及响应消息结构的定义，通常采用XML或JavaScript对象表示法(JSON)格式。

Web API已经从基于简单对象访问协议(SOAP)的Web服务和面向服务的架构(SOA)转向更直接的表征状态转移(REST)风格的Web资源。

社交媒体服务和Web API已经允许Web社区在社区和不同平台之间共享内容和数据。

使用API，在一个地方创建的内容可以动态地在Web上的多个位置发布和更新。

例如，Twitter的REST API允许开发人员访问核心Twitter数据，而搜索API提供了开发人员与Twitter搜索和趋势数据互动的方法。

许多应用程序提供API端点。一些API的例子，如国家[API](https://restcountries.eu/rest/v2/all)，[猫品种API](https://api.thecatapi.com/v1/breeds)。

在本节中，我们将介绍一个RESTful API，它使用HTTP请求方法来GET、PUT、POST和DELETE数据。

## 构建API

RESTful API是一种应用程序编程接口(API)，使用HTTP请求来GET、PUT、POST和DELETE数据。在前几节中，我们学习了Python、Flask和MongoDB。我们将利用我们获得的知识，使用Python Flask和MongoDB数据库开发一个RESTful API。每个具有CRUD(创建、读取、更新、删除)操作的应用程序都有一个API，用于从数据库创建数据、获取数据、更新数据或删除数据。

要构建API，了解HTTP协议和HTTP请求、响应周期是很好的。

## HTTP(超文本传输协议)

HTTP是客户端和服务器之间建立的通信协议。在这种情况下，客户端是浏览器，服务器是你访问数据的地方。HTTP是一种网络协议，用于传递资源，这些资源可以是万维网上的文件，无论是HTML文件、图像文件、查询结果、脚本或其他文件类型。

浏览器是HTTP客户端，因为它向HTTP服务器(Web服务器)发送请求，而HTTP服务器再向客户端发送响应。

## HTTP的结构

HTTP使用客户端-服务器模型。HTTP客户端打开一个连接并向HTTP服务器发送请求消息，HTTP服务器返回响应消息，即请求的资源。当请求响应周期完成时，服务器关闭连接。

![HTTP请求响应周期](../images/http_request_response_cycle.png)

请求和响应消息的格式类似。两种消息都有

- 一个初始行
- 零个或多个头行
- 一个空行(即单独的CRLF)
- 一个可选的消息体(例如文件、查询数据或查询输出)

让我们通过导航此站点来看一个请求和响应消息的示例：https://thirtydaysofpython-v1-final.herokuapp.com/ 。这个网站已部署在Heroku免费dyno上，在某些月份可能由于高请求量而无法工作。支持这项工作可以让服务器始终运行。

![请求和响应头](../images/request_response_header.png)

## 初始请求行(状态行)

初始请求行与响应不同。
请求行有三个部分，用空格分隔：

- 方法名(GET、POST、HEAD)
- 请求资源的路径
- 使用的HTTP版本。例如 GET / HTTP/1.1

GET是最常见的HTTP方法，用于获取或读取资源，而POST是常见的请求方法，用于创建资源。

### 初始响应行(状态行)

初始响应行，称为状态行，也有三个用空格分隔的部分：

- HTTP版本
- 响应状态码，给出请求的结果，以及描述状态码的原因。状态行的例子有：
  HTTP/1.0 200 OK
  或者
  HTTP/1.0 404 Not Found
  注意：

最常见的状态码是：
200 OK：请求成功，并且生成的资源(例如文件或脚本输出)在消息体中返回。
500 服务器错误
完整的HTTP状态码列表可以在[这里](https://httpstatuses.com/)找到。也可以在[这里](https://httpstatusdogs.com/)找到。

### 头字段

正如你在上面的截图中看到的，头行提供了有关请求或响应的信息，或者有关在消息体中发送的对象的信息。

```sh
GET / HTTP/1.1
Host: thirtydaysofpython-v1-final.herokuapp.com
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36
Sec-Fetch-User: ?1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Referer: https://thirtydaysofpython-v1-final.herokuapp.com/post
Accept-Encoding: gzip, deflate, br
Accept-Language: en-GB,en;q=0.9,fi-FI;q=0.8,fi;q=0.7,en-CA;q=0.6,en-US;q=0.5,fr;q=0.4
```

### 消息体

HTTP消息可能在头行之后发送数据体。在响应中，这是请求的资源返回给客户端的地方(消息体最常用的用途)，或者如果出现错误，这里可能是解释性文本。在请求中，这是用户输入的数据或上传的文件发送到服务器的地方。

如果HTTP消息包含一个消息体，通常在消息中有描述该消息体的头行。特别是：

Content-Type: 头给出消息体中数据的MIME类型(text/html，application/json，text/plain，text/css，image/gif)。
Content-Length: 头给出消息体中的字节数。

### 请求方法

GET、POST、PUT和DELETE是我们将实现API或CRUD操作应用程序的HTTP请求方法。

1. GET：GET方法用于使用给定的URI从给定服务器检索和获取信息。使用GET的请求应该只检索数据，而不应该对数据有任何其他影响。

2. POST：POST请求用于创建数据并将数据发送到服务器，例如使用HTML表单创建新帖子、上传文件等。

3. PUT：用上传的内容替换目标资源的所有当前表示，我们使用它来修改或更新数据。

4. DELETE：删除数据

## 💻 练习：第28天

1. 阅读有关API和HTTP的资料

🎉 恭喜！🎉

[<< 第 27 天](./27_python_with_mongodb_cn.md) | [第 29 天 >>](./29_building_API_cn.md) 
<div align="center">
  <h1> 30 Days Of Python: Day 28 - API </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Author:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>Second Edition: July, 2021</small>
</sub>

</div>
</div>

[<< Day 27](../27_Day_Python_with_mongodb/27_python_with_mongodb.md) | [Day 29 >>](../29_Day_Building_API/29_building_API.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 28](#-day-28)
- [Application Programming Interface(API)](#application-programming-interfaceapi)
  - [API](#api)
  - [API 구축하기](#api-구축하기)
  - [HTTP(Hypertext Transfer Protocol)](#httphypertext-transfer-protocol)
  - [HTTP의 구조](#http의-구조)
  - [초기 요청 라인(상태 라인)](#초기-요청-라인상태-라인)
    - [초기 응답 라인(상태 라인)](#초기-응답-라인상태-라인)
    - [헤더 필드](#헤더-필드)
    - [메시지 본문](#메시지-본문)
    - [요청 메서드](#요청-메서드)
  - [💻 연습문제: Day 28](#-연습문제-day-28)

# 📘 Day 28

# Application Programming Interface(API)

## API

API는 Application Programming Interface(애플리케이션 프로그래밍 인터페이스)의 약자입니다. 이 섹션에서 다룰 API의 종류는 Web API입니다.
Web API는 기업과 해당 자산을 사용하는 애플리케이션 간의 상호작용이 이루어지는 정의된 인터페이스이며, 기능 제공자를 명시하고 API 사용자를 위한 서비스 경로 또는 URL을 노출하는 서비스 수준 계약(SLA)이기도 합니다.

웹 개발의 맥락에서, API는 Hypertext Transfer Protocol(HTTP) 요청 메시지와 같은 일련의 사양으로 정의되며, 일반적으로 XML 또는 JavaScript Object Notation(JSON) 형식의 응답 메시지 구조 정의를 포함합니다.

Web API는 Simple Object Access Protocol(SOAP) 기반 웹 서비스 및 서비스 지향 아키텍처(SOA)에서 벗어나 보다 직접적인 표현 상태 전송(REST) 스타일의 웹 리소스로 이동하고 있습니다.

소셜 미디어 서비스에서 Web API는 웹 커뮤니티가 커뮤니티와 다양한 플랫폼 간에 콘텐츠와 데이터를 공유할 수 있도록 해주었습니다.

API를 사용하면, 한 곳에서 동적으로 생성된 콘텐츠를 웹의 여러 위치에 게시하고 업데이트할 수 있습니다.

예를 들어, Twitter의 REST API는 개발자가 핵심 Twitter 데이터에 접근할 수 있게 해주며, Search API는 개발자가 Twitter 검색 및 트렌드 데이터와 상호작용할 수 있는 메서드를 제공합니다.

많은 애플리케이션이 API 엔드포인트를 제공합니다. 예를 들어, 국가 [API](https://restcountries.eu/rest/v2/all), [고양이 품종 API](https://api.thecatapi.com/v1/breeds) 등이 있습니다.

이 섹션에서는 HTTP 요청 메서드를 사용하여 데이터를 GET, PUT, POST 및 DELETE하는 RESTful API를 다룰 것입니다.

## API 구축하기

RESTful API는 HTTP 요청을 사용하여 데이터를 GET, PUT, POST 및 DELETE하는 애플리케이션 프로그램 인터페이스(API)입니다. 이전 섹션에서 우리는 Python, Flask, MongoDB에 대해 학습했습니다. Python Flask와 MongoDB 데이터베이스를 사용하여 RESTful API를 개발하기 위해 습득한 지식을 활용할 것입니다. CRUD(Create, Read, Update, Delete) 작업이 있는 모든 애플리케이션에는 데이터베이스에서 데이터를 생성, 조회, 수정 또는 삭제하기 위한 API가 있습니다.

API를 구축하려면 HTTP 프로토콜과 HTTP 요청 및 응답 주기를 이해하는 것이 좋습니다.

## HTTP(Hypertext Transfer Protocol)

HTTP는 클라이언트와 서버 간의 확립된 통신 프로토콜입니다. 이 경우 클라이언트는 브라우저이고 서버는 데이터에 접근하는 곳입니다. HTTP는 HTML 파일, 이미지 파일, 쿼리 결과, 스크립트 또는 기타 파일 유형 등 World Wide Web의 파일이 될 수 있는 리소스를 전달하는 데 사용되는 네트워크 프로토콜입니다.

브라우저는 HTTP 클라이언트인데, HTTP 서버(웹 서버)에 요청을 보내고, 서버는 클라이언트에 응답을 다시 보내기 때문입니다.

## HTTP의 구조

HTTP는 클라이언트-서버 모델을 사용합니다. HTTP 클라이언트는 연결을 열고 HTTP 서버에 요청 메시지를 보내며, HTTP 서버는 요청된 리소스인 응답 메시지를 반환합니다. 요청-응답 주기가 완료되면 서버는 연결을 닫습니다.

![HTTP 요청 응답 주기](../../images/http_request_response_cycle.png)

요청 및 응답 메시지의 형식은 유사합니다. 두 종류의 메시지 모두 다음을 포함합니다:

- 초기 라인(initial line),
- 0개 이상의 헤더 라인,
- 빈 줄 (즉, CRLF 자체), 그리고
- 선택적 메시지 본문 (예: 파일, 쿼리 데이터 또는 쿼리 출력).

이 사이트를 탐색하여 요청 및 응답 메시지의 예를 살펴보겠습니다: https://thirtydaysofpython-v1-final.herokuapp.com/. 이 사이트는 Heroku 무료 dyno에 배포되었으며 높은 요청으로 인해 몇 달 후에는 작동하지 않을 수 있습니다. 서버가 항상 작동할 수 있도록 이 작업을 지원해 주세요.

![요청 및 응답 헤더](../../images/request_response_header.png)

## 초기 요청 라인(상태 라인)

초기 요청 라인은 응답과 다릅니다.
요청 라인은 공백으로 구분된 세 부분으로 구성됩니다:

- 메서드 이름(GET, POST, HEAD)
- 요청된 리소스의 경로,
- 사용 중인 HTTP 버전. 예: GET / HTTP/1.1

GET은 리소스를 가져오거나 읽는 데 도움이 되는 가장 일반적인 HTTP이며, POST는 리소스를 생성하는 일반적인 요청 메서드입니다.

### 초기 응답 라인(상태 라인)

초기 응답 라인은 상태 라인이라고도 하며, 공백으로 구분된 세 부분으로 구성됩니다:

- HTTP 버전
- 요청 결과를 제공하는 응답 상태 코드와 상태 코드를 설명하는 이유. 상태 라인의 예:
  HTTP/1.0 200 OK
  또는
  HTTP/1.0 404 Not Found
  참고:

가장 일반적인 상태 코드는 다음과 같습니다:
200 OK: 요청이 성공했으며, 결과 리소스(예: 파일 또는 스크립트 출력)가 메시지 본문에 반환됩니다.
500 Server Error
전체 HTTP 상태 코드 목록은 [여기](https://httpstatuses.com/)에서 확인할 수 있습니다. [여기](https://httpstatusdogs.com/)에서도 확인할 수 있습니다.

### 헤더 필드

위의 스크린샷에서 볼 수 있듯이, 헤더 라인은 요청 또는 응답, 또는 메시지 본문에서 전송되는 객체에 대한 정보를 제공합니다.

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

### 메시지 본문

HTTP 메시지는 헤더 라인 뒤에 전송되는 데이터 본문을 가질 수 있습니다. 응답에서는 요청된 리소스가 클라이언트에 반환되는 곳이며(메시지 본문의 가장 일반적인 사용), 오류가 있는 경우 설명 텍스트가 될 수도 있습니다. 요청에서는 사용자가 입력한 데이터 또는 업로드된 파일이 서버로 전송되는 곳입니다.

HTTP 메시지에 본문이 포함된 경우, 일반적으로 본문을 설명하는 헤더 라인이 메시지에 있습니다. 특히,

Content-Type: 헤더는 본문 데이터의 MIME 유형을 제공합니다(text/html, application/json, text/plain, text/css, image/gif).
Content-Length: 헤더는 본문의 바이트 수를 제공합니다.

### 요청 메서드

GET, POST, PUT 및 DELETE는 API 또는 CRUD 작업 애플리케이션을 구현할 HTTP 요청 메서드입니다.

1. GET: GET 메서드는 주어진 URI를 사용하여 지정된 서버에서 정보를 검색하고 가져오는 데 사용됩니다. GET을 사용하는 요청은 데이터만 검색해야 하며 데이터에 다른 영향을 미치지 않아야 합니다.

2. POST: POST 요청은 HTML 양식을 사용하여 새 게시물 생성, 파일 업로드 등과 같이 데이터를 생성하고 서버에 데이터를 보내는 데 사용됩니다.

3. PUT: 대상 리소스의 모든 현재 표현을 업로드된 콘텐츠로 대체하며, 데이터를 수정하거나 업데이트하는 데 사용합니다.

4. DELETE: 데이터를 삭제합니다.

## 💻 연습문제: Day 28

1. API와 HTTP에 대해 읽어보세요.

🎉 축하합니다! 🎉

[<< Day 27](../27_Day_Python_with_mongodb/27_python_with_mongodb.md) | [Day 29 >>](../29_Day_Building_API/29_building_API.md)

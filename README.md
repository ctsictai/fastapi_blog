FastAPI framework project

Design Pattern

https://camillovisini.com/article/abstracting-fastapi-services/ 참조

![design_pattern](https://d33wubrfki0l68.cloudfront.net/6c6e6d1a9a2252c24c72049f74382abee765095c/9408a/_nuxt/img/request-response.df4b985.jpg)

Controller router / business logic / data access code 분리 패턴

1. controller layer
   - rotuers directory
2. business logic layer
   - services directory
3. data access layer
   - schemas directory
4. util
   - exception - common exception config
   - service_result - common response config
5. core directory

   config - common settings
   auth - common auth setting - middleware
   consts - common constant

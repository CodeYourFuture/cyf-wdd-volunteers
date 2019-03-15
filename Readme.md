# </a>CYF - volunteers manager!!!
[Introduction](#intro) |
[Scope](#scope)|
[Trello Board](#trello) |
[Stack](#stack) |
[Possible Query select](#params) |
[Tech Notes](#technotes)|
[User Stories](#stories) |  
[Your local machine environment](#howto)|
[Useful tutorials](#tutorials)|
[Q&A](#q&a) <br>
### <a name="intro"></a>Introduction :
Website : [Code your future](https://codeyourfuture.io/)
The CYF charity provides the opportunity for people at a disadvantage to learn to code, during an 8 month programme with a weekly Sunday meetup.
Recently, new aspects have been introduced to the programme; the homework clubs (Tuesday and Thursday) and one-to-one mentoring scheme.
A new organogram was designed for volunteers to be involved in outreach, education and development.
CYF has established a setup in multiple locations: London, Manchester, Glasgow, Rome and Bogota. Whilst CYF are experiencing rapid expansion, there is no uniformed approach to their processes.
The website is built in React and JavaScript on AWS Lambda, hosted on GitHub. All other data lives on Google Drive and Gmail in sheets/docs/presentations.
### <a name="scope"></a> Scope :
### <a name="trello"></a>Trello Board :
Link to board if you have one
### <a name="stack"></a>Stack :
|Technology| Version/Docs|
|---|---|
|Java|8|
|Postgres| [Docs Link](https://www.postgresql.org/)|
|Lambda|[Docs Link](https://docs.aws.amazon.com/lambda/index.html#lang/en_us)|
|Docker|[Docs Link](https://www.docker.com/)|
|AWS - EC2|[Docs Link](https://docs.aws.amazon.com/ec2/index.html#lang/en_us)|
|React|[Docs Link](https://reactjs.org/)|
|Springboot|[Docs Link](https://spring.io/)|
|Testing|:speak_no_evil:|
### <a name="technotes"></a>Tech Notes :
> Volunteer information db table

|Data|Type|
|:---:|:---:|
|Name|String|
|Surname|String|
|City|String|
|Email|String|
|Contact number|Int|
> Volunteer skills information db table

| Data    | Type     |
|:-------------:|:-------------:|
| Teaching       | Bool       |
|Running Organisation| Bool|
|Language and Level| Enum|
|General experience |String|
|Weekend Availability (Teachers can only help on weekends. Non-technical volunteers can help any time)|Bool|
|Currently volunteering|Bool|
### <a name="params"/></a>Possible query params  :
| `query params` or `endpoints` TBD  |
|:---|
| Find all volunteers  |
| Find by City |
| Find by Language skill   *the skill level is optional*    |
| Find by Name       |
|Find by Teach or Run Organisation|
|Find by currently volunteering or not|  

### <a name="useful"></a> Useful Information and Links:
**Github codebase:**  
https://github.com/CodeYourFuture/cyf-forms/tree/application-form  
**Volunteer form:**  
https://s3.eu-west-2.amazonaws.com/cyf-test-application-form/index.html  
**Summary of all ideas:**  
https://docs.google.com/document/d/143wMuPheMY5mXdqd0_0InR7P3V5JCV-HqhZLdz66ChM/edit?usp=sharing  
**Some detailed documents:**  
*Activity Tracker:* https://docs.google.com/document/d/1mDe2JpDCKzH3QSaLJHutfXdM3WilKNFm7OODvDKNPpQ/edit  
*Volunteers "CRM":* https://docs.google.com/document/d/1y0zZedSIFZI7X9Efw53_9Gg9zmpl_dTNxNXFOmTK0jU/edit?usp=sharing  
**Students application process**  
*Applicants Companion:*
https://codeyourfuture.io/students#requirements    
*Application form for volunteers*
<<<<<<< Updated upstream
https://s3.eu-west-2.amazonaws.com/cyf-test-application-form/index.html
- https://codeyourfuture.io/apply/mentor
- https://codeyourfuture.io/apply/volunteer
=======
https://s3.eu-west-2.amazonaws.com/cyf-test-application-form/index.html  
- https://codeyourfuture.io/apply/mentor  
- https://codeyourfuture.io/apply/volunteer  
>>>>>>> Stashed changes

# </a>CYF - volunteers manager!!!

[Introduction](#intro) |
[Scope](#scope)|
[Trello Board](#trello) |
[Stack](#stack) |
[Tech Notes](#technotes)|
[Possible Query params](#params) |
[Useful links](#useful) <br>

### <a name="intro"></a>Introduction :

Website : [Code your future](https://codeyourfuture.io/)
The charity provides the opportunity for people at a disadvantage to learn to code during an 8 month programme with a weekly Sunday meetup.
Newly aspects introduced to the programme are the homework clubs (Tuesday and Thursday) and one-to-one mentoring scheme. Whilst CYF are experiencing rapid expansion, there is no uniformed approach to processes. A new organogram was designed for volunteers to be involved in outreach, education development.

_The website website is built in React and JavaScript on AWS Lambda, hosted on GitHub. All other data lives on Google Drive and Gmail in sheets/docs/presentations._

### <a name="scope"></a> Scope :
MVP version 1 :
Post all data from front-end to backend

MVP version 2:
TBD

### <a name="trello"></a>Trello Board :

[Link](https://trello.com/b/fA4sf5J0/cyf-volunteer-tracking)


### <a name="stack"></a>Stack :

|Technology| Version/Docs|
|---|---|
|Java|version 8|
|Postgress| [Docs Link](https://www.postgresql.org/)|
|Lambda|[Docs Link](https://docs.aws.amazon.com/lambda/index.html#lang/en_us)|
|AWS - EC2|[Docs Link](https://docs.aws.amazon.com/ec2/index.html#lang/en_us)|
|React|[Docs Link](https://reactjs.org/)|
|Testing|:speak_no_evil:|


### <a name="technotes"></a>Tech Notes :
> Volunteer information db table

|Data|Type|
|---|---|
|id | auto|
|name | String|
|surname  | String|
|city | String|
|email  | String|
|contact-number | Int|
|general-experience | string|
|weekend-availability | bool|
|currently-volunteering | bool|

> Volunteer skills information db table

| Data    | Type     |
| ------------- | ------------- |
|id | auto|
|user-id| auto|
|volunteer-name|  string|
|language-skill| Enum|
|level| int|

```
Method    endpoint
POST      /volunteers

Table 1 volunteers-info
|id | name |  surname | city  | email | contact | general experience  | weekend availability  | currently volunteering  |

Table 2 volunteers-technical-skill

id  | user id | volunteer name | Skill | Level |
|Name A | Java  | 4 |
```
### <a name="front-end"/></a>Post request schema  :
*for front-end :*

```
{volunteer: {
        name: string,
        surname: string,
        cyf-city: string,
        email: string,
        contact-number: Int || null,
        general-experience: string,
        weekend-availability: bool,
        currently-volunteering: bool,
        technical-skills: {[
                  {skill-type: emun,
                  level: int},
                  {skill-type: enum,
                  level: int},
                  {skill-type: enum,
                  level: int},
                  {skill-type: enum,
                  level: int},
                  ]}
        }
}
```

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
*Activity Tracker:*  
https://docs.google.com/document/d/1mDe2JpDCKzH3QSaLJHutfXdM3WilKNFm7OODvDKNPpQ/edit  
*Volunteers "CRM":*   
https://docs.google.com/document/d/1y0zZedSIFZI7X9Efw53_9Gg9zmpl_dTNxNXFOmTK0jU/edit?usp=sharing  
**Students application process**  
*Applicants Companion:*  
https://codeyourfuture.io/students#requirements    
*Application form for volunteers*  
https://s3.eu-west-2.amazonaws.com/cyf-test-application-form/index.html  
- https://codeyourfuture.io/apply/mentor  
- https://codeyourfuture.io/apply/volunteer   

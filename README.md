
# Projet Joyaux

Very first coding project. The aim is to present on a website (local), the translation of specific information to help player of Monster Hunter Wilds video game.

--------
HOW I'M WORKING 
--------
I'm using live server to display my html page which I use to do my 'exercises'. 
FYI some of the datas are either scrapped from a specialized website, other are in the repo under .xlsx files.


---------
PACKAGES
---------

Here are  my python packages used : 
Package              Version
-------------------- -----------
beautifulsoup4       4.13.4
numpy                2.3.2
RapidFuzz            3.13.0
requests             2.32.4



---------
ABOUT ME
---------

I don't really know how to use git/github or even code, most of the code you see is inherited from Chat GPT, I try to read documentation, ask GPT questions, and do stuff. 
Any remarks, guidelines or help is appreciated. 

I'm really starting from nowhere so please be indulgent. 
## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.


## Appendix

Any additional information goes here


## Authors

- [@cmdnak](https://www.github.com/cmdnak)


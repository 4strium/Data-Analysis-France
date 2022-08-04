<h1 align="center">Data Analysis France</h1>

Script allowing the analysis and recovery of precise data on French cities. 🔍

- [Search Methods](https://github.com/4strium/Data-Analysis-France#search-methods-)
- [Obtained Result](https://github.com/4strium/Data-Analysis-France#obtained-result-)
- [Export](https://github.com/4strium/Data-Analysis-France#export-)
    - [Full Export](https://github.com/4strium/Data-Analysis-France#full-export-)
    - [Targeted Export](https://github.com/4strium/Data-Analysis-France#targeted-export-)
- [Technologies used](https://github.com/4strium/Data-Analysis-France#targeted-export-)
- [Downloads & Installation](https://github.com/4strium/Game-of-Matches#downloads-)

## Search Methods :
You can search for data on one or more French cities, using these different search methods:

|Search Method                           |Example                                    |
|----------------------------------------|-------------------------------------------|
|Département / Department                |`29, 45, 75, ...`                          |
|Nom de la ville / Name                  |`Brest, Orléans, Paris, ...`               |
|Code Postal / Postal Code               |`29200, 45000-45100, 75000-75100-..., ...` |
|Numéro de Commune / Municipality number |`019, 234, 056, ...`                       |
|Arrondissement / Borough                |`1, 2, 1, ...`                             |
|Population / Population (2012)          |`142100, 113300, 2211000, ...`             |

> **Note:** The search by postal code **may not work** if it's a city that has **several postal codes** (such as Paris, Orléans, Lyon, ...), in this case you must enter ALL the codes with a `-` between them!
## Obtained Result :
Normally following your search, you should obtain a list containing one or more city data lists!

Under the form : ` [{'Département': '29', 'Nom reel': 'Brest', 'Code postal': '29200', 'Numéro de commune': '019', 'Arrondissement': '1', 'Population en 2012': '142100'}] `

## Export :

Following your search, the software offers to export the data in a new CSV file, and under the name of your choice!

> **Note:** When typing, you can add the filename extension `.csv` **OR NOT**, the program will add it for you in case you forget! ;)
### Full Export :
The software offers the option of exporting all the data for all French cities, but only taking into account the following descriptors:
- Département / Department
- Nom de la ville / Name of the city 
- Code Postal / Postal Code
- Numéro de Commune / Municipality number
- Arrondissement / Borough 
- Population / Population (2012)

These are therefore useful descriptors for research, in order to reuse this file for future work!
### Targeted Export :
The second type of export is that which is targeted, for example admitting that you are looking for information on the department of Finistère (29), then you can export all the data of the cities of the department (and only them) in a `finistere.csv` file!
## Technologies used :
- [CSV](https://en.wikipedia.org/wiki/Comma-separated_values)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

## Downloads & Installation :
The easiest and fastest way to use the software is to clone this repository!

How?

If you have the [GitHub CLI](https://cli.github.com/) installed on your computer, run the following command in your command prompt:
`gh repo clone 4strium/Data-Analysis-France`

If you don't have the GitHub CLI, just simply hit the [Download](https://github.com/4strium/Data-Analysis-France/archive/refs/heads/main.zip) button!
All you have to do is extract the archive!

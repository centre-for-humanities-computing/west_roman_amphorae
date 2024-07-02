## Western Roman Empire amphorae
This repository includes the data, notebooks, and figures to replicate and reuse the analysis of Western Roman Empire amphorae data.

## Contributors
The notebooks are developed in collaboration with the [Center for Humanities Computing Aarhus (CHCAA)](https://chc.au.dk/). They are based to a high extent on the notebooks of [this repository](https://github.com/Tom-Brughmans/RAAD?tab=readme-ov-file).

* [Daniel Blumenkranz](https://github.com/daniblu)
* [Tom Brughmans](https://pure.au.dk/portal/en/persons/t.b%40cas.au.dk)
*

## Data
The dataset used to create all figures is _Data\_amphorae\_20\_and\_Tarraconensis.csv_ located in the _data_ folder. This is tabular data in which each row represents a unique combination of an amphora type and an excavation site. 
<br /> 

<details>
  <summary>  The data table </summary>

|**Field Name**                |      **Type / Description**                                                                    |
| ---------------------------- | ---------------------------------------------------------------------------------------------- |
|'site_h1'	                   |   string / An excavation site                                                                  |
|'amphora_type'                |   string / A unique amphora type identifier                                                    |
|'latitude'               	   |   float / Latitiude of the excavation site                                                     |
|'longitude'	               |   float / Longitude of the excavation site                                                     |
|'Atlant/Mediterr'	           |   string / An indicator of whether the site is connected to the Atlantic or the Mediterranean  |
|'Modern country'	           |   string / Modern national location of sites                                                   |
|'Early Imperial province'	   |   string / Roman provincial location of sites                                                  |
|'frequency_density' 	       |   float / A density (cg/m^2) of ceramic mass found at the excavation site                      |
|'contents'                    |   string / A product carried in an amphora                                                     |
|'origin_h1_province'          |   string / A province where an amphora was produced                                            |
|'origin_h2_region'            |   string / A region where an amphora was produced                                              |
|'Lower_date_type'	           |   integer / A production start date of an amphora                                              |
|'Upper_date_type'             |   integer / A production end date of an amphora                                                |

</details>

<br /> 

## Notebooks
The iPython notebooks used to generate all figures are available in the _notebooks_ folder. Each notebook reproduces one figure pertaining to one specific query. 

Each notebook is structured in the same way:

1. Import packages
2. Read in data and do some preprocessing if required by the query.
3. Calculation of density frequency of amphorae, count of sites, count of types in the context of the query.
4. Plot the graphs
<br /> 

<details>
  <summary>  Query overview </summary>

* Q1: All data
* Q2: Western provinces versus easter provinces. West includes Italy, Baetica, Narbonense, Lyonese, Tarraconensis, and Africa. East includes Syria et Palestine and Lycia et Pamphilia.
* Q3: Western regions verus eastern regions. West includes Campania, Laietania, Venetia et Histria, Coast Cadiz, Guadalquivir, Narbonense, Lyonese, Tarraconensis, and Africa. East includes Kos, Palestine, and Rhodes.
* Q4: By amphora contents.
* Q4ES: By amphora contents for Spanish sites only.
* Q4FR: By amphora contents for French sites only.
* Q4UK: By amphora contents for British sites only.
* Q5: By modern country.
* Q6: By province.
* Q7: By region.
* Q8: By province for wine amphorae only.
* Q9: By region for wine amphorae only.
* Q10: As Q9 but regions are grouped into high quality (includes Rhodes, Campania, Kos), and low quality (includes Tarraconensis, Laietania, Narbonense, Lyonense, Guadalquivir).
* Q11: Atlantic sites versus Mediterranean sites.
* Q12: By province for Atlantic sites only.
* Q13: By province for Mediterranean sites only.
* Q14: By region for Atlantic sites only.
* Q15: By region for Mediterranean sites only.
* Q16: By early Imperial province.

</details>

<br />

The notebooks with an an 'x' in the file name share the preprocessing step of removing data from the excavation sites Caesaraugusta, Vilarenc, Baetulo, Can Feu, and 'Nª Sra del Port' as these sites contribute with high densities and might dominate some results.

## Setup
Run the following line in the terminal to setup and environment in which all packages listed in _requirements.txt_ are downloaded as well as an ipykernel so that the notebooks can connect to the environment.
```bash
bash setup_env_posix.sh
```
Please note that the script assumes a POSIX system. Make sure to choose the repository environment when selcting an environment for the notebooks.

## License
This software is [MIT licensed](./LICENSE.txt).
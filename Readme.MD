Processing of environmental data from miljoeportal.dk with data science approach using Python with Pandas library.

First what needs to be highlighted here, Danes are model ones, who all we have to follow example of them. A great 
open data collection about environment condition for last 40 years. From chemistry of water to spices variety. 

There are some issues about units, ways and strategy of measurements, but I have treated open source data. These issues
will be left unanswered.
- misleading of units, milligrams vs micrograms
- analyze of  fjords bottom-shell for heavy metal pollutants
- analyze ow underground water in the area where heavy metals were detected in slumps. 
- drinking water data for sitisents are not accessible. 
These data are not available for me and evoke some questions.
But anyway, it is great possibilities for students, enthusiasts and activists to have all data on the table. 

For the custom access are available data with wastewater, lake, lake-bottom condition, rivers, underground water.
We can get raw data in csv format and manipulate with that in desirable way. 
With Pandas approach we can sort, extract from the gigantic data collection information which is interesting for us.
Visualise it graphically in plots after all.

Lets go through the details.

1. About Danish air. 
According to the public data from Aarhus University and environment monitoring department we can state
Danish air can be considered as clean without any limit presence of pollutants.

 [ Alt Text]("https://github.com/tech-science-club/datascience_emvironmental_research/blob/7b2a5cf706c6ceba46438a8d6b252e12efc6f4e0/contamination_air.png")


Presumably, it is because, Denmark does not have a metallurgy, chemical industry, as it might be. 
Government rules and regulations impacted in positive way an agriculture, traffic regulations, building area have been 
playing crucial role in pollutants rates declining.

2. Underground water. 
I don't know why, but very little information about it. Excel files contain only 30 lines for last month about some minerals 
and only for 5 areas in Denmark.

3. Wastewater

Here is much larger variety of data. Unpleasant surprise was a fact Denmark has those same problem as everywhere world 
around - human activity. 
Heavy metal pollutants, organic compounds were found in sludge of slumps and in water samples. Interesting fact is remained
nowadays data about heavy metal presence in wastewater is nat available.
Here was implemented some strategy of investigation. As was a couple of thousands of rows in Excel file, was decided 
to print out a max value of each contaminant, its location and look through it. 
Paying attention to the highest value might be embedded possibilities to withdraw information about certain location, that 
was done. 
The retrieved data can be saved into separate Excel file, is being saved as png file with plot of pollutants.
Then, going further seeing in details about some interesting location we can obtain historical data for it.
Here has been noticed a fact, Roskilde slump had a presence of a big variety of harmful metals in it. Was decided to retrieve 
a historical data of it for the last 40 years from the portal and visualize it in plot view.




Presumably, a reason of its presence is activity of local Plant which has to do to electrochemical production. 
Is well known, it demands of Zink, Chrome, Nikel etc salt as electrolysis components. Those electrolytes leak to the local
wastewater and then to the global city ones. 
Have been expected leading a such environmentally responsible productions has to be followed rules and norms. 
However data results show another history.



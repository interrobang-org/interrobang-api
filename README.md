# interrobang-api
## API
1. **URL**: https://frozen-sands-16144.herokuapp.com/api/getQ
   **Post Request Details**: 

   ```javascript
   header:
   Content-Type:application/json
   body:
   has two parts 
   1. text - the input text data
   2. summarize 1 - use summarize api, 0 - dont use summarize api
   example: 
   {"text":"Mexican President Andres Manuel Lopez Obrador said Friday that he will open up national archives showing how intelligence agencies targeted activists and opposition groups during the country's  dirty war.  They will be opened up so that citizens can have access to them, above all investigators. It is a part of our program to strength our national historic memory,  said the president, commonly known as AMLO.The documents belong to the National Center for Investigation and Security (CISEN) and are housed in the Lecumberri national archive, a former prison in the capital where numerous opposition figures, including members of the 1968 student movement, were once incarcerated.They will be open to the public starting from Monday, Lopez Obrador said.One of the first things the Mexican leader said after he took office on December 1 was to announce that CISEN would be disbanded, while keeping intact the National Intelligence Center.The 65-year-old leftist leader said that Mexico, which for decades was governed by the Institutional Revolutionary Party, or PRI, had a  dark period  which saw the persecution of social activists and opposition figures, mostly from the 1960s to the 1980s, an era historians refer to a the  dirty war.  We lived for decades under an authoritarian regime which limited freedoms and persecuted those who struggled for social change,  he said. In the name of the state, I apologize,  Lopez Obrador added.",
   "summarize":1
   }
   ```

2. **URL**: https://frozen-sands-16144.herokuapp.com/api/getQ

   **Post Request Details**: 

   ```javascript
   header:
   Content-Type:application/json
   body:
   has an array with each element having two parts 
   1. text - the input text data
   2. summarize 1 - use summarize api, 0 - dont use summarize api
   example: 
   [{"text":"Mexican President Andres Manuel Lopez Obrador said Friday that he will open up national archives showing how intelligence agencies targeted activists and opposition groups during the country's  dirty war.  They will be opened up so that citizens can have access to them, above all investigators. It is a part of our program to strength our national historic memory,  said the president, commonly known as AMLO.The documents belong to the National Center for Investigation and Security (CISEN) and are housed in the Lecumberri national archive, a former prison in the capital where numerous opposition figures, including members of the 1968 student movement, were once incarcerated.They will be open to the public starting from Monday, Lopez Obrador said.One of the first things the Mexican leader said after he took office on December 1 was to announce that CISEN would be disbanded, while keeping intact the National Intelligence Center.The 65-year-old leftist leader said that Mexico, which for decades was governed by the Institutional Revolutionary Party, or PRI, had a  dark period  which saw the persecution of social activists and opposition figures, mostly from the 1960s to the 1980s, an era historians refer to a the  dirty war.  We lived for decades under an authoritarian regime which limited freedoms and persecuted those who struggled for social change,  he said. In the name of the state, I apologize,  Lopez Obrador added.",
   "summarize":1
   },
   {"text":"Mexican President Andres Manuel Lopez Obrador said Friday that he will open up national archives showing how intelligence agencies targeted activists and opposition groups during the country's  dirty war.  They will be opened up so that citizens can have access to them, above all investigators. It is a part of our program to strength our national historic memory,  said the president, commonly known as AMLO.The documents belong to the National Center for Investigation and Security (CISEN) and are housed in the Lecumberri national archive, a former prison in the capital where numerous opposition figures, including members of the 1968 student movement, were once incarcerated.They will be open to the public starting from Monday, Lopez Obrador said.One of the first things the Mexican leader said after he took office on December 1 was to announce that CISEN would be disbanded, while keeping intact the National Intelligence Center.The 65-year-old leftist leader said that Mexico, which for decades was governed by the Institutional Revolutionary Party, or PRI, had a  dark period  which saw the persecution of social activists and opposition figures, mostly from the 1960s to the 1980s, an era historians refer to a the  dirty war.  We lived for decades under an authoritarian regime which limited freedoms and persecuted those who struggled for social change,  he said. In the name of the state, I apologize,  Lopez Obrador added.",
   "summarize":0
   }]
   ```

   
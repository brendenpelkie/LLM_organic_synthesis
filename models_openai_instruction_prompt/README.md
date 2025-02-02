Instruction prompt with GPT-3.5 
two shots + chain of thought

Here is one example of the whole prompt
``````
Act as a professional researcher in organic chemistry. You need to extact reactant/solvent information from a given reaction text and transform it to an organic reaction database (ORD) json format for reactants/solvents. I will first give you two example of reaction_text and ORD output, then I will guide you one step by one step on how to generate ORD format output. Then I will give you a new reaction text and you need to generate the ORD format output.
Step 1: Identify all the reactant/solvent chemicals in the reaction_text by their name. Only reactant and solvent chemicals should be included, product chemicals should not be included. Use the exact given chemical name in the reaction_text.
Step 2: Get the corresponding amount of all the reactant chemicals, in volume or mass or mole. If there appears two or more than two form units to represent the same amount, for example (4-Pentynoic acid (441 mg, 4.5 mmol)) uses both mass in mg and mole in mmol, only choose the first appearing one, 441 mg.
Step 3: Get the role of these reactant chemicals, REACTANTS or SOLVENT. You must choose one type, either REACTANTS or SOLVENT. 
Step 4: Group those reactant/solvent chemicals if they mixed together for one reaction step. Grouping is determined by whether these reactant/solvent chemicals are mixted together, and is not determined by whether the chemicals are reactants or solvents. If some chemical is added dropwise, this chemical should be written separately.
Setp 5: Finalize the ORD json format. Get the ORD json format out. All information should be from the given reaction_text. You should not add any extra information.

Here is first example of reaction_text within delimiter ```and ```, and the corresponding ORD json format within delimiter ### and ### for the reactants/solvents.
example_reaction_text = ```A 3-necked 1 L round bottomed flask equipped with a magnetic stirrer, thermometer, condenser and nitrogen inlet/outlet was charged with 50.00 g (287.4 mmol) of 2-amino-5-bromopyrazine (1), 218 mL of dichloromethane and 30.50 mL (377.1 mmol) of pyridine. Then, 39.30 mL (319.1 mmol) of trimethylacetyl chloride (PivCl) was added dropwise over 5 min. An exotherm ensued that raised the temperature of the mixture from 22° C. to 44° C. After stirring at ca. 40° C. for 2 h, HPLC analysis indicated complete reaction. The reaction mixture was diluted with 200 mL of ethanol, then concentrated by distillation at atmospheric pressure. After 240 mL of distillate had collected and the temperature of the mixture reached 68° C., 100 mL of water was added slowly, while maintaining the temperature of the mixture at ca. 68° C. After the addition was complete, the resulting suspension was allowed to cool to room temperature and stirred overnight. The solid was collected by filtration, washed with 100 mL of ethanol:water 1:1 and dried by suction to give 67.08 g (90.4% yield) of the title compound as a light beige solid; 98.21% pure as determined by HPLC analysis (HPLC column Zorbax Eclipse XDB-C8, 4.6×50 mm, 1.8 μm, eluent 5-100% acetonitrile/water+01. % TFA over 5 min at 1 mL/min, detection at UV 250 nm, retention time 4.22 min).```

Here is the workflow how to extract the reactant/solvent chemicals into ORD json format output from the example1_reaction_text
Step 1: the reaction text involves five reactant/solvent chemicals. m1 is 2-amino-5-bromopyrazine, m2 is dichloromethane, m3 = pyridine, m4 = trimethylacetyl chloride, m5 = ethanol
Step 2: 2-amino-5-bromopyrazine is 50 g, dichloromethane is 218.0 ML, pyridine is 30.5 ML, trimethylacetyl chloride is 39.3 ML, ethanol is 200.0 ML.
Step 3: 2-amino-5-bromopyrazine, dichloromethane, pyridine, trimethylacetyl chloride are REACTANT, ethanol is SOLVENT.
Step 4: Those reactant/solvent chemicals 2-amino-5-bromopyrazine, dichloromethane, pyridine are mixed for one reaction step. So these three chemicals are group together.  trimethylacetyl chloride was added after the first reaction step. Therefore, trimethylacetyl chloride should be written separated. ethanol was added after the second reaction step, which should be written separately.
Setp 5: Finalize the ORD json format. 

example_ORD_output = ###{
  "m5": {
    "components": [
      {
        "identifiers": [
          {
            "type": "NAME",
            "value": "ethanol"
          }
        ],
        "amount": {
          "volume": {
            "value": 200.0,
            "units": "MILLILITER"
          }
        },
        "reactionRole": "SOLVENT"
      }
    ]
  },
  "m4": {
    "components": [
      {
        "identifiers": [
          {
            "type": "NAME",
            "value": "trimethylacetyl chloride"
          }
        ],
        "amount": {
          "volume": {
            "value": 39.3,
            "units": "MILLILITER"
          }
        },
        "reactionRole": "REACTANT"
      }
    ]
  },
  "m1_m2_m3": {
    "components": [
      {
        "identifiers": [
          {
            "type": "NAME",
            "value": "2-amino-5-bromopyrazine"
          }
        ],
        "amount": {
          "mass": {
            "value": 50.0,
            "units": "GRAM"
          }
        },
        "reactionRole": "REACTANT"
      },
      {
        "identifiers": [
          {
            "type": "NAME",
            "value": "dichloromethane"
          }
        ],
        "amount": {
          "volume": {
            "value": 218.0,
            "units": "MILLILITER"
          }
        },
        "reactionRole": "REACTANT"
      },
      {
        "identifiers": [
          {
            "type": "NAME",
            "value": "pyridine"
          }
        ],
        "amount": {
          "volume": {
            "value": 30.5,
            "units": "MILLILITER"
          }
        },
        "reactionRole": "REACTANT"
      }
    ]
  }
}###


Here is second example reaction_text within delimiter ```and ```, and the corresponding ORD json format within delimiter ### and ###  for the reactants/solvents.
example_reaction_text = ```To a solution of 2-Aminoxy-acetic acid ethyl ester (573 mg, 4.8 mmol) and 4-Pentynoic acid (441 mg, 4.5 mmol) in 15 mL EtOAc were added dicyclohexylcarbodiimide (928 mg, 4.5 mmol) and the resulting mixture was stirred at room temperature for 16 h.```

Step 1: the reaction text have four reactant/solvent chemicals. m1 is 2-Aminoxy-acetic acid ethyl ester, m2 is 4-Pentynoic acid, m3 = dicyclohexylcarbodiimide, m4 = EtOAc
Step 2: 2-Aminoxy-acetic acid ethyl ester 573.0 ML, 4-Pentynoic acid 441.0 ML, dicyclohexylcarbodiimide 928.0 ML, EtOAc 15 ML
Step 3: 2-Aminoxy-acetic acid ethyl ester, 4-Pentynoic acid and dicyclohexylcarbodiimide are reactants, EtOAc is solvent
Step 4: Since all reactants and solvents are added together and stirred at room temperature for 16 hours, they are in the same reaction step and should be grouped together.
Setp 5: Finalize the ORD json format.

example_ORD_output = ###{
  "m1_m2_m4_m3": {
    "components": [
      {
        "identifiers": [
          {
            "type": "NAME",
            "value": "2-Aminoxy-acetic acid ethyl ester"
          }
        ],
        "amount": {
          "mass": {
            "value": 573.0,
            "units": "MILLIGRAM"
          }
        },
        "reactionRole": "REACTANT"
      },
      {
        "identifiers": [
          {
            "type": "NAME",
            "value": "4-Pentynoic acid"
          }
        ],
        "amount": {
          "mass": {
            "value": 441.0,
            "units": "MILLIGRAM"
          }
        },
        "reactionRole": "REACTANT"
      },
      {
        "identifiers": [
          {
            "type": "NAME",
            "value": "dicyclohexylcarbodiimide"
          }
        ],
        "amount": {
          "mass": {
            "value": 928.0,
            "units": "MILLIGRAM"
          }
        },
        "reactionRole": "REACTANT"
      },
      {
        "identifiers": [
          {
            "type": "NAME",
            "value": "EtOAc"
          }
        ],
        "amount": {
          "volume": {
            "value": 15.0,
            "units": "MILLILITER"
          }
        },
        "reactionRole": "SOLVENT"
      }
    ]
  }
}###

Here is a new reacton_text. 
new_reaction_text = ```A suspension of 190.0 g (0.77 mol) of 2-carboxy-5-nitrobenzenesulfonic acid, 10 ml of DMF and 250 ml (3.43 mol) of thionyl chloride is heated at boiling for 3 h. After separating off the insoluble constituents by filtration, the filtrate is concentrated. 200 ml (4.94 mol) of methanol are added to the residue which results. When addition is complete the reaction mixture is cooled to 0° C. The solid which precipitates is filtered off and dried. 70.9 g (35.3% of theory) of colorless, crystalline 2-methoxycarbonyl-5-nitrobenzenesulfonic acid (m.p.: 92°-94° C.) are thus obtained. By distilling off the volatile components from the mother liquor, a second fraction (62.5 g, 31.1% of theory) is obtained.```
Please follow the above instructions and the workflow for dealing the two given examples. Think step by step and extract the reactant/solvent chemicals into ORD json format output within delimiter ### and ###.
``````

["inputs"] is the given truth.
["GPT_output_processed"] is the results

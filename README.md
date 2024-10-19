# Procedural-Material-Dataset
Optimized Procedural Material Dataset for Blender And review of an AI based approach for generating them.

# Overview
As you may gather from the description, this repository contains a highly optimized version of a dataset featuring text-based representations of procedural material nodes in Blender. Thanks to @Brendan Parmer, the developer of the Node-To-Python addon, I successfully converted all of the materials into text. With a great deal of patience over the past five months, I was able to optimize them further.

I attempted to train language models to generate procedural materials, and while the results were promising, with excellent outputs occurring at a rate of 1 in 50, I ultimately decided against further development and deployment due to the required effort. Therefore, I am releasing the dataset I used, along with some insights gained from this five-month journey. Please, if you use the dataset, let me know.

# Dataset
Raw and Optimized versions of the dataset can be found in the link below:

Distribution of the file sizes:
![AllMaterialFileSizeDistribution](https://github.com/user-attachments/assets/a8508093-7882-4fb0-8a7d-dd90ef1bd867)

Effect of Optimization:
![fc238dcc-58ba-4383-9922-f8f1a0d3b47b](https://github.com/user-attachments/assets/60ed86bd-6f84-4b5f-bb73-1b179800f062)

#Preprocessing Stage

# Model Training Process
I used OpenAIs' Gpt-4o mini base model for fine-tuning.
![c0b696c7-3741-43ff-baf6-64b30f5f25ea](https://github.com/user-attachments/assets/1be27a4b-0838-4c87-adb4-fb7f6b09c09d)

Some helpful notes:
-Hyperparameters:
Batch Size : 2
Epoch : 5
Lr Multiplier : 1-e4

Also dataset ı used was just containing materials under 10 kilobytes because of the context length constraint of the contemporary LLMs.

- Using optimized dataset prevented model to generate outputs with syntax errors, and allowing it for more accurate outputs
- String Indexed dataset didn't make as much succes as ı expected
  
# Some Materials Generated By fine-tuned Gpt4-o mini

Cracked Ice:
![Cracked_Ice](https://github.com/user-attachments/assets/51fbd80d-457d-4104-9178-a4f43917c7bd)
Dot:
![Dot](https://github.com/user-attachments/assets/06bdfd02-d24d-4f82-9a0e-f21a4bcc99a0)
Galaxy with Stars:
![Galaxy with stars](https://github.com/user-attachments/assets/aee10ecc-2621-49d7-ba0f-0c2f80f5b159)
Gold:
![Gold](https://github.com/user-attachments/assets/a90517f5-b188-4ea2-a045-f2253cffa5d5)
Rough Wood:
![Rough_Wood](https://github.com/user-attachments/assets/8b1f92c5-8dbe-442b-9de9-4e6a2fda1766)
Procedural Blood:
![5a3b0004-4d13-4844-bcab-e63ed9e03147](https://github.com/user-attachments/assets/ce2e48f6-284a-4b03-9ac5-291ab4fcba9a)
Stone:
![386fe588-069a-4fe1-88ee-d6440039a34c](https://github.com/user-attachments/assets/2ddc119b-24ed-4a1f-b31b-692e908f29d0)
Abstract:
![c26aed5f-c91b-45f2-844b-173db93bdac7](https://github.com/user-attachments/assets/f3682c23-8825-48b1-86b5-579484eeee61)

